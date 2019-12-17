#! /usr/bin/python3
import json
import sys
from jinja2 import Environment, FileSystemLoader
sys.path.insert(1, './fortimanager-schema')
from api_schema_parser import load_schema
from pprint import pformat
from os import listdir


schematype_displayname_mapping = {
    'array': 'list',
    'dict': 'dict',
    'integer': 'int',
    'string': 'str'
}


def underscore2hyphen(string):
    return string.replace('_', '-')


def hyphen2underscore(string):
    return string.replace('-', '_')


def canonicalize_url_as_path(url):
    url = url.replace('/adom/{adom}/', '/')
    url = url.replace('/global/', '/')
    canocial_url_path = 'fmgr'
    fields = url.split('/')
    for field in fields:
        if field == '':
            continue
        field = hyphen2underscore(field)
        field = field.strip('{')
        field = field.strip('}')
        canocial_url_path += '_' + field
    return canocial_url_path


def canonicalize_text(raw_text):
    delimiters = ['<br/><b>', '<li>']
    stripped_words = ['</b>', '<b>', '</li>', '<ul>', '</ul>']
    utimate_lst = [raw_text]
    for delimiter in delimiters:
        finer_lst = list()
        for item in utimate_lst:
            finer_items = item.split(delimiter)
            for finer_item in finer_items:
                finer_lst.append(finer_item)
        utimate_lst = finer_lst
    ret_lst = list()
    for item in utimate_lst:
        stripped_data = item
        for stripped_chars in stripped_words:
            stripped_data = stripped_data.replace(stripped_chars, '')
        ret_lst.append('\'' + stripped_data.rstrip(' ').rstrip('-').rstrip('-') + '\'')
    return ret_lst


def split_text(text, offset, max_length):
    length_per_line = max_length - offset
    nr_ptr = 0
    nr_left = len(text)
    splitted_text = list()
    while nr_left > 0:
        split_length = length_per_line if nr_left >= length_per_line else nr_left
        tmp_text = text[nr_ptr: nr_ptr + split_length]

        nr_left -= split_length
        nr_ptr += split_length
        if tmp_text[-1].isalpha() and nr_left > 0 and text[nr_ptr].isalpha():
            tmp_text += '-'
        splitted_text.append(tmp_text)
    return splitted_text


def get_params_name_list_with_hypen_char(in_path_params):
    name_list = list()
    for param in in_path_params:
        assert('name') in param
        assert('in' in param and param['in'] == 'path')
        name = param['name']
        if '-' in name:
            name_list.append(name)
    return name_list


def tailor_schema(in_body_params):
    if isinstance(in_body_params, list):
        lst = list()
        for param in in_body_params:
            lst.append(tailor_schema(param))
        return lst
    elif isinstance(in_body_params, dict):
        dct = dict()
        for param_key in in_body_params:
            if param_key in ['in', 'format', 'description', 'example']:
                if isinstance(in_body_params[param_key], str):
                    continue
            dct[param_key] = tailor_schema(in_body_params[param_key])
        return dct
    return in_body_params


def transform_schema(tailored_params):
    schema_objects = dict()
    schema_mappig = dict()
    object_indicator = 0
    for method in tailored_params:
        schema_per_method = tailored_params[method]
        schema_object_key_found = None
        for object_key in schema_objects:
            schema_object = schema_objects[object_key]
            if schema_object == schema_per_method:
                schema_object_key_found = object_key
                break
        if not schema_object_key_found:
            schema_object_key = 'object%s' % (object_indicator)
            object_indicator += 1
            schema_objects[schema_object_key] = schema_per_method
            schema_object_key_found = schema_object_key
        schema_mappig[method] = schema_object_key_found
    return {'schema_objects': schema_objects, 'method_mapping': schema_mappig}


def schema_beautify(schema, initial_indent, depth, include_comma=False,
                    strip_beginning_space=False):
    formatted_data = ''
    if isinstance(schema, dict):
        formatted_data += (' ' if strip_beginning_space else (' ' * (4 * (depth
                                                                          - 1 if depth >= 1 else 0) + initial_indent))) + '{\n'
        nr_items = len(list(schema.keys()))
        item_index = 0
        for item_key in schema:
            item = schema[item_key]
            formatted_data += ' ' * (4 * depth + initial_indent) + '\'' + \
                              item_key + '\':'
            if isinstance(item, str) or isinstance(item, int):
                formatted_data += ' '
            formatted_data += schema_beautify(item, initial_indent, depth + 1,
                                              (item_index + 1) < nr_items, not isinstance(item, int) and not isinstance(item, str))
            item_index += 1
        formatted_data += ' ' * (4 * (depth - 1 if depth >= 1 else 0) +
                                 initial_indent) + '}' + (',\n' if include_comma else '\n')
    if isinstance(schema, list):
        formatted_data += (' ' if strip_beginning_space else (' ' * (4 * (depth
                                                                          - 1 if depth >= 1 else 0) + initial_indent))) + '[\n'
        nr_items = len(schema)
        item_index = 0
        for item in schema:
            if isinstance(item, str) or isinstance(item, int):
                formatted_data += ' ' * (4 * depth + initial_indent)
            formatted_data += schema_beautify(item, initial_indent, depth + 1,
                                              (item_index + 1) < nr_items)
            item_index += 1
        formatted_data += ' ' * (4 * (depth - 1 if depth >= 1 else 0) +
                                 initial_indent) + ']' + (',\n' if include_comma else '\n')
    if isinstance(schema, int):
        formatted_data += str(schema) + ('\n' if not include_comma else ',\n')
    if isinstance(schema, str):
        formatted_data += '\'' + schema + '\'' + ('\n' if not include_comma else ',\n')
    return formatted_data


def _generate_schema_document_options_recursilve(schema, depth):
    rdata = ''
    if 'type' not in schema or schema['type'] not in [
            'string', 'integer', 'array', 'dict']:
        for discrete_schema_key in schema:
            discrete_schema = schema[discrete_schema_key]
            rdata += ' ' * depth * 4 + \
                discrete_schema_key.replace('{', r'\{').replace('}', r'\}') + ':\n'
            rdata += _generate_schema_document_options_recursilve(
                discrete_schema, depth + 1)
        return rdata

    if schema['type'] in ['string', 'integer']:
        rdata += ' ' * depth * 4 + 'type: ' + \
            schematype_displayname_mapping[schema['type']] + '\n'
        if 'default' in schema:
            rdata += ' ' * depth * 4 + 'default: ' + str(schema['default']) + '\n'
        # FIXED: some characters in description are not recognized by yaml.
        if 'description' in schema:
            desc_list = canonicalize_text(schema['description'])
            if (len(desc_list) > 1):
                rdata += ' ' * depth * 4 + 'description:\n'
                for item in desc_list:
                    rdata += ' ' * depth * 4 + ' - %s\n' % (item)
            else:
                rdata += ' ' * depth * 4 + 'description: '
                rdata += '\n' if not len(desc_list) else (desc_list[0] + '\n')
        if 'enum' in schema:
            rdata += ' ' * depth * 4 + 'choices:\n'
            for item in schema['enum']:
                rdata += ' ' * (depth + 1) * 4 + '- ' + str(item) + '\n'
    elif schema['type'] is 'dict':
        assert('dict' in schema)
        rdata += _generate_schema_document_options_recursilve(schema['dict'], depth)

    elif schema['type'] is 'array':
        rdata += ' ' * depth * 4 + '-\n'
        assert('items' in schema)
        rdata += _generate_schema_document_options_recursilve(schema['items'], depth + 1)
    else:
        assert(False)

    return rdata


def generate_schema_document_options(
        raw_body_schemas, in_path_params, api_endpoint_tags):
    options_data = ''
    body_schema = transform_schema(raw_body_schemas)
    if len(in_path_params):
        options_data += ' ' * 4 + 'url_params: \n'
        options_data += ' ' * 8 + 'description: the parameters in url path\n'
        options_data += ' ' * 8 + 'required: True\n'
        options_data += ' ' * 8 + 'type: dict\n'
        options_data += ' ' * 8 + 'suboptions:\n'
        for url_param in in_path_params:
            options_data += ' ' * 12 + url_param['name'] + ':\n'
            options_data += ' ' * 16 + 'type: ' + ('int' if url_param['type']
                                                   == 'integer' else 'str') + '\n'
            if  url_param['name'] == 'adom':
                options_data += ' ' * 16 + 'description: the domain prefix, the none and global are reserved\n'
                options_data += ' ' * 16 + 'choices:\n'
                options_data += ' ' * 16 + '  - none\n'
                options_data += ' ' * 16 + '  - global\n'
                options_data += ' ' * 16 + '  - custom dom\n'
    for schema_object_key in body_schema['schema_objects']:
        schema_object = body_schema['schema_objects'][schema_object_key]
        method_list = [method for method in body_schema['method_mapping'] if
                       body_schema['method_mapping'][method] == schema_object_key]
        schema_object_key_display_name = 'schema_%s' % (schema_object_key)
        options_data += ' ' * 4 + schema_object_key_display_name + ':\n'
        options_data += ' ' * 8 + 'methods: ' + str(method_list).replace('\'', '') + '\n'
        options_data += ' ' * 8 + \
            'description: \'%s\'\n' % (api_endpoint_tags[method_list[0]])
        tagged_params = dict()
        for param in schema_object:
            assert('api_tag' in param)
            api_tag = param['api_tag']
            if api_tag not in tagged_params:
                tagged_params[api_tag] = list()
            tagged_params[api_tag].append(param)
        options_data += ' ' * 8 + 'api_categories: ' + str(['api_tag%s' % (tag)
                                                            for tag in tagged_params]).replace('\'', '') + '\n'
        for tag in tagged_params:
            options_data += ' ' * 8 + 'api_tag%s' % (tag) + ':\n'
            for param in tagged_params[tag]:
                if param['name'] == 'url':
                    continue
                options_data += ' ' * 12 + param['name'] + ':\n'
                options_data += _generate_schema_document_options_recursilve(param, 4)
    return options_data
def _generate_docgen_paramters_recursively(schema):
    params_data = ''
    if 'type' not in schema or schema['type'] not in ['string', 'integer', 'array', 'dict']:
        for discrete_schema_key in schema:
            discrete_schema = schema[discrete_schema_key]
            params_data +=  ' <li><span class="li-head">%s</span>'%(discrete_schema_key)
            params_data += _generate_docgen_paramters_recursively(discrete_schema)
        return params_data

    if schema['type'] in ['string', 'integer']:
        if 'description' in schema:
            desc_list = canonicalize_text(schema['description'])
            the_desc = desc_list[0].strip('\'')
            first_dot_pos = the_desc.find('.')
            if first_dot_pos >= 0:
                the_desc = the_desc[: first_dot_pos + 1]
            params_data += ' - %s'%(the_desc)
        else:
            params_data += ' - No description for the parameter'
        params_data += ' <span class="li-normal">type: %s</span> '%(schematype_displayname_mapping[schema['type']])
        if 'enum' in schema:
            params_data += ' <span class="li-normal">choices: %s</span> '%(str([str(item) for item in schema['enum']]).replace('\'', ''))
        if 'default' in schema:
            params_data += ' <span class="li-normal">default: %s</span> '%(schema['default'])
        params_data += '</li>\n'
    elif schema['type'] is 'dict':
        fold = 'type' not in schema['dict'] or schema['dict']['type'] not in ['string', 'integer', 'array', 'dict']
        params_data += ' - No description for the parameter' if fold else ''
        params_data += ' <span class="li-normal">type: dict</span>' if fold else ''
        params_data += ' <ul class="ul-self">\n' if fold else ''
        params_data += _generate_docgen_paramters_recursively(schema['dict'])
        params_data += ' </ul>\n' if fold else ''
    elif schema['type'] is 'array':
        params_data += ' - No description for the parameter'
        params_data += ' <span class="li-normal">type: array</span>'
        params_data += ' <ul class="ul-self">\n'
        if 'type' in schema['items'] and schema['items']['type'] in ['string', 'integer', 'array', 'dict']:
            params_data +=  ' <li><span class="li-head">{no-name}</span>'
        params_data += _generate_docgen_paramters_recursively(schema['items'])
        params_data += ' </ul>\n'
    return params_data

def generate_docgen_parameters(raw_body_schemas, in_path_params, api_endpoint_tags):
    params_data = ' <ul>\n'
    if len(in_path_params):
        params_data += ' <li><span class="li-head">url_params</span> - parameters in url path <span class="li-normal">type: dict</span> <span class="li-required">required: true</span></li>\n'
        params_data += ' <ul class="ul-self">\n'
        for url_param in in_path_params:
            params_data += ' <li><span class="li-head">' + url_param['name']
            params_data += '</span> - ' + ('the domain prefix' if url_param['name'] == 'adom' else 'the object name') + ' <span class="li-normal">'
            params_data += 'type: '+ ('int' if url_param['type'] == 'integer' else 'str') + '</span> '
            params_data += ('<span class="li-normal"> choices: none, global, custom dom</span>' if url_param['name'] == 'adom' else '') + '</li>\n'
        params_data += ' </ul>\n'
    body_schema = transform_schema(raw_body_schemas)

    for schema_object_key in body_schema['schema_objects']:
        schema_object = body_schema['schema_objects'][schema_object_key]
        method_list = [method for method in body_schema['method_mapping'] if
                       body_schema['method_mapping'][method] == schema_object_key]
        params_data += ' <li><span class="li-head">parameters for method: %s</span> - %s</li>\n'%(str(method_list).replace('\'', ''), api_endpoint_tags[method_list[0]])

        tagged_params = dict()
        for param in schema_object:
            assert('api_tag' in param)
            api_tag = param['api_tag']
            if api_tag not in tagged_params:
                tagged_params[api_tag] = list()
            tagged_params[api_tag].append(param)

        params_data += ' <ul class="ul-self">\n'

        has_multi_tags = len(tagged_params) > 1
        for tag in tagged_params:
            if has_multi_tags:
                params_data += ' <ul class="ul-self">\n'
                params_data += ' <li><span class="li-head">parameter collection %s</span></li>\n'%(tag)
                params_data += ' <ul class="ul-self">\n'
            for param in tagged_params[tag]:
                if param['name'] == 'url':
                    continue
                params_data +=  ' <li><span class="li-head">%s</span>'%(param['name'])
                params_data += _generate_docgen_paramters_recursively(param)
                #params_data += '</li>\n'
            if has_multi_tags:
                params_data += ' </ul>\n'
                params_data += ' </ul>\n'
        params_data += ' </ul>\n'
    params_data += ' </ul>\n'
    return params_data


def _generate_schema_document_examples_recursive(schema, depth):
    rdata = ''

    if 'type' not in schema or schema['type'] not in [
            'string', 'integer', 'array', 'dict']:
        to_fold = True
        for discrete_schema_key in schema:
            discrete_schema = schema[discrete_schema_key]
            if to_fold:
                rdata += '\n'
                to_fold = False
            rdata += ' ' * depth * 3 + \
                discrete_schema_key.replace('{', r'\{').replace('}', r'\}') + ': '
            rdata += _generate_schema_document_examples_recursive(
                discrete_schema, depth + 1)
        return rdata

    if schema['type'] in ['string', 'integer']:
        if 'enum' in schema:
            enum_list = list()
            enum_index = 0
            for item in schema['enum']:
                if enum_index == 3:
                    enum_list.append('...')
                    break
                else:
                    enum_list.append(item)
                enum_index += 1
            rdata += '<value in %s%s>' % (str(enum_list).replace('\'', ''),
                                          ' default: %s' % (str(schema['default'])) if 'default' in
                                          schema and schema['default'] != '' else '') + '\n'
        else:
            rdata += '<value of %s%s>' % (schema['type'], ' default: %s' % (str(
                     schema['default'])) if 'default' in schema and schema[
                'default'] != '' else '') + '\n'
    elif schema['type'] is 'array':
        rdata += '\n'
        rdata += ' ' * (depth - 1) * 3 + ' - '
        assert('items' in schema)
        rdata += _generate_schema_document_examples_recursive(schema['items'], depth + 1)
    elif schema['type'] is 'dict':
        assert('dict' in schema)
        rdata += _generate_schema_document_examples_recursive(schema['dict'], depth)
    else:
        assert(False)
    return rdata


def generate_schema_document_examples(
        raw_body_schemas, module_name, jrpc_url, in_path_params):
    example_data = ''
    example_data += ' - ' + 'hosts: fortimanager-inventory\n'
    example_data += ' ' * 3 + 'connection: httpapi\n'
    example_data += ' ' * 3 + 'vars:\n'
    example_data += ' ' * 6 + 'ansible_httpapi_use_ssl: True\n'
    example_data += ' ' * 6 + 'ansible_httpapi_validate_certs: False\n'
    example_data += ' ' * 6 + 'ansible_httpapi_port: 443\n'
    example_data += ' ' * 3 + 'tasks:\n'
    body_schema = transform_schema(raw_body_schemas)
    for schema_object_key in body_schema['schema_objects']:
        schema_object = body_schema['schema_objects'][schema_object_key]
        method_list = [method for method in body_schema['method_mapping'] if
                       body_schema['method_mapping'][method] == schema_object_key]
        tagged_params = dict()
        for param in schema_object:
            if param['name'] == 'url':
                continue
            assert('api_tag' in param)
            api_tag = param['api_tag']
            if api_tag not in tagged_params:
                tagged_params[api_tag] = list()
            tagged_params[api_tag].append(param)
        for tag in tagged_params:
            example_data += ' ' * 3 + ' - name: send request to %s\n' % (jrpc_url.replace('/adom/{adom}/', '/').replace('/global/', '/'))
            example_data += ' ' * 6 + module_name + ':\n'
            example_data += ' ' * 9 + \
                'method: <value in %s>\n' % (str(method_list).replace('\'', ''))
            if len(in_path_params):
                example_data += ' ' * 9 + 'url_params:\n'
                for url_param in in_path_params:
                    if url_param['name'] == 'adom':
                        example_data += ' ' * 12 + url_param['name'] + ': <value in [none, global, custom dom]>\n'
                        continue
                    example_data += ' ' * 12 + \
                        url_param['name'] + ': <value of %s>\n' % (url_param['type'])
            example_data += ' ' * 9 + 'params:\n'
            example_data += ' ' * 12 + '- \n'
            for param in tagged_params[tag]:
                example_data += ' ' * 15 + '%s: ' % (param['name'])
                example_data += _generate_schema_document_examples_recursive(param, 6)
    return example_data


def _generate_schema_document_return_recursive(schema, depth):
    rdata = ''

    if 'type' not in schema or schema['type'] not in [
            'string', 'integer', 'array', 'dict']:
        for discrete_schema_key in schema:
            discrete_schema = schema[discrete_schema_key]
            rdata += ' ' * depth * 3 + \
                discrete_schema_key.replace('{', r'\{').replace('}', r'\}') + ':\n'
            rdata += _generate_schema_document_return_recursive(
                discrete_schema, depth + 1)
        return rdata
    if schema['type'] in ['string', 'integer']:
        rdata += ' ' * depth * 3 + \
            'type: %s\n' % (schematype_displayname_mapping[schema['type']])
        if 'description' in schema:
            desc_list = canonicalize_text(schema['description'])
            if (len(desc_list) > 1):
                rdata += ' ' * depth * 3 + 'description: |\n'
                for item in desc_list:
                    rdata += ' ' * depth * 3 + '   %s\n' % (item)
            else:
                rdata += ' ' * depth * 3 + 'description: '
                rdata += '\n' if not len(desc_list) else (desc_list[0] + '\n')
        if 'example' in schema:
            rdata += ' ' * depth * 3 + 'example: %s\n' % (schema['example'])
    elif schema['type'] is 'array':
        assert('items' in schema)
        rdata += ' ' * depth * 3 + 'type: array\n'
        rdata += ' ' * depth * 3 + 'suboptions:\n'
        rdata += _generate_schema_document_return_recursive(schema['items'], depth + 1)
    elif schema['type'] is 'dict':
        assert('dict' in schema)
        rdata += _generate_schema_document_return_recursive(schema['dict'], depth)
    else:
        assert(False)
    return rdata


def generate_schema_document_return(raw_results_schemas):
    return_data = ''
    result_schemas = transform_schema(raw_results_schemas)
    for schema_object_key in result_schemas['schema_objects']:
        schema_object = result_schemas['schema_objects'][schema_object_key]
        method_list = [method for method in result_schemas['method_mapping'] if
                       result_schemas['method_mapping'][method] == schema_object_key]
        tagged_params = dict()
        for param in schema_object:
            assert('api_tag' in param)
            api_tag = param['api_tag']
            if api_tag not in tagged_params:
                tagged_params[api_tag] = list()
            tagged_params[api_tag].append(param)

        for tag in tagged_params:
            return_data += 'return_of_api_category_%s:' % (tag) + '\n'
            return_data += ' ' * 3 + \
                'description: items returned for method:%s\n' % (
                    str(method_list).replace('\'', ''))
            return_data += ' ' * 3 + 'returned: always\n'
            return_data += ' ' * 3 + 'suboptions:\n'
            return_data += ' ' * 6 + 'id:\n'
            return_data += ' ' * 9 + 'type: int\n'
            return_data += ' ' * 6 + 'result:\n'
            for param in tagged_params[tag]:
                return_data += ' ' * 9 + '%s:\n' % (param['name'])
                return_data += _generate_schema_document_return_recursive(param, 4)
    return return_data

def _generate_docgen_return_value_recursive(schema):
    return_data = ''
    if 'type' not in schema or schema['type'] not in ['string', 'integer', 'array', 'dict']:
        for discrete_schema_key in schema:
            discrete_schema = schema[discrete_schema_key]
            return_data +=  ' <li> <span class="li-return"> %s </span>'%(discrete_schema_key)
            return_data += _generate_docgen_return_value_recursive(discrete_schema)
        return return_data
    if schema['type'] in ['string', 'integer']:
        if 'description' in schema:
            desc_list = canonicalize_text(schema['description'])
            the_desc = desc_list[0].strip('\'')
            first_dot_pos = the_desc.find('.')
            if first_dot_pos >= 0:
                the_desc = the_desc[: first_dot_pos + 1]
            return_data += ' - %s'%(the_desc)
        else:
            return_data += ' - No description for the parameter'
        return_data += ' <span class="li-normal">type: %s</span> '%(schematype_displayname_mapping[schema['type']])
        if 'example' in schema:
            return_data += ' <span class="li-normal">example: %s</span> '%(schema['example'])
        return_data += ' </li>\n'
    elif schema['type'] is 'dict':
        fold = 'type' not in schema['dict'] or schema['dict']['type'] not in ['string', 'integer', 'array', 'dict']
        return_data += ' - No description for the parameter' if fold else ''
        return_data += ' <span class="li-normal">type: dict</span>' if fold else ''
        return_data += ' <ul class="ul-self">\n' if fold else ''
        return_data += _generate_docgen_return_value_recursive(schema['dict'])
        return_data += ' </ul>\n' if fold else ''
    elif schema['type'] is 'array':
        return_data += ' - No description for the parameter'
        return_data += ' <span class="li-normal">type: array</span>'
        return_data += ' <ul class="ul-self">\n'
        if 'type' in schema['items'] and schema['items']['type'] in ['string', 'integer', 'array', 'dict']:
            return_data +=  ' <li><span class="li-return">{no-name}</span>'
        return_data += _generate_docgen_return_value_recursive(schema['items'])
        return_data += ' </ul>\n'

    return return_data

def generate_docgen_return_value(raw_results_schemas):
    return_data = ' <ul>\n'
    result_schemas = transform_schema(raw_results_schemas)
    for schema_object_key in result_schemas['schema_objects']:
        schema_object = result_schemas['schema_objects'][schema_object_key]
        method_list = [method for method in result_schemas['method_mapping'] if result_schemas['method_mapping'][method] == schema_object_key]
        return_data += ' <li><span class="li-return"> return values for method: ' + str(method_list).replace('\'', '') + '</span> </li>\n'
        tagged_params = dict()
        for param in schema_object:
            assert('api_tag' in param)
            api_tag = param['api_tag']
            if api_tag not in tagged_params:
                tagged_params[api_tag] = list()
            tagged_params[api_tag].append(param)
        return_data += ' <ul class="ul-self">\n'
        has_multi_tags = len(tagged_params) > 1
        for tag in tagged_params:
            if has_multi_tags:
                return_data += ' <ul class="ul-self">\n'
                return_data += ' <li><span class="li-return">return values collection %s</span></li>\n'%(tag)
                return_data += ' <ul class="ul-self">\n'
            for param in tagged_params[tag]:
                return_data += ' <li><span class="li-return">%s</span>\n'%(param['name'])
                return_data += _generate_docgen_return_value_recursive(param)
            if has_multi_tags:
                return_data += ' </ul>\n'
                return_data += ' </ul>\n'
        return_data += ' </ul>\n'
    return_data += ' </ul>\n'
    return return_data

def resolve_schema_file(schema_path, per_schema_except, doc_template, code_template):
    schema = load_schema(schema_path, per_schema_except)
    for url in schema._digest:
        resolve_schema(url, schema, doc_template, code_template, [(url, schema)])

def validate_multiurls_schema(url, schema, multiurls):
    # Validate schemas which have multiple domains dependent urls.
    multiurls_allowed_methods_set = set(schema._digest[url].keys())
    for _url, _schema in multiurls[1:]:
        assert(multiurls_allowed_methods_set == set(_schema._digest[_url].keys()))
    multiurls_in_path_params = dict()
    multiurls_in_body_params = dict()
    multiurls_result_schema = dict()
    multiurls_api_endpoint_tag = dict()
    for method in multiurls_allowed_methods_set:
        multiurls_in_path_params[method] = dict()
        multiurls_in_body_params[method] = dict()
        multiurls_result_schema[method] = dict()
        multiurls_api_endpoint_tag[method] = dict()
        for _url, _schema in multiurls:
            _in_path_params, _in_body_params, _result_schema, _api_endpoint_tag = _schema.get_function_schema(_url, method)
            multiurls_in_path_params[method][_url] = _in_path_params
            multiurls_in_body_params[method][_url] = _in_body_params
            multiurls_result_schema[method][_url] = _result_schema
            multiurls_api_endpoint_tag[method][_url] = _api_endpoint_tag
        # It's expected that all fields are identical except for those in `in_path_params`
        per_method_api_endpoint_tags = set()
        the_one_body_schema = None
        the_one_result_schema = None
        for _url in multiurls_api_endpoint_tag[method]:
            per_method_api_endpoint_tags.add(multiurls_api_endpoint_tag[method][_url])
            _body_schema = multiurls_in_body_params[method][_url]
            body_schema = list()
            for item in _body_schema:
                if item['name'] == 'url':
                    continue
                body_schema.append(item)
            if not the_one_body_schema:
                the_one_body_schema = body_schema
            else:
                pass
                #assert(the_one_body_schema == body_schema)
            _result_schema = multiurls_result_schema[method][_url]
            result_schema = list()
            for item in _result_schema:
                if item['name'] == 'url':
                    continue
                result_schema.append(item)
            if not the_one_result_schema:
                the_one_result_schema = result_schema
            else:
                assert(the_one_result_schema == result_schema)
        assert(len(per_method_api_endpoint_tags) == 1)
    
def resolve_schema(url, schema, doc_template, code_template, multiurls):  
    validate_multiurls_schema(url, schema, multiurls)
    body_schemas = dict()
    raw_body_schemas = dict()
    results_schemas = dict()
    api_endpoint_tags = dict()
    multiurls_in_path_params = dict()
    the_one_in_path_params = None

    for method in schema._digest[url]:
        in_path_params, in_body_params, result_schema, api_endpoint_tag = schema.get_function_schema(url, method)
        raw_body_schemas[method] = in_body_params
        body_schemas[method] = tailor_schema(in_body_params)
        results_schemas[method] = result_schema
        api_endpoint_tags[method] = api_endpoint_tag
        in_body_params_without_apitags = list()
        for item in in_path_params:
            if item['api_tag'] != 0:
                continue
            in_body_params_without_apitags.append(item)
        if url not in multiurls_in_path_params:
            multiurls_in_path_params[url] = in_body_params_without_apitags
        else:
            assert(multiurls_in_path_params[url] == in_body_params_without_apitags)
        
    for _url, _schema in multiurls[1:]:
        for _method in _schema._digest[_url]:
            in_path_params, in_body_params, result_schema, api_endpoint_tag = schema.get_function_schema(_url, _method)
            in_body_params_without_apitags = list()
            for item in in_path_params:
                if item['api_tag'] != 0:
                    continue
                in_body_params_without_apitags.append(item)
            if _url not in multiurls_in_path_params:
                multiurls_in_path_params[_url] = in_body_params_without_apitags
            else:
                assert(multiurls_in_path_params[_url] == in_body_params_without_apitags)
    for _url in multiurls_in_path_params:
        _in_path_params = multiurls_in_path_params[_url]
        if not the_one_in_path_params or len(the_one_in_path_params) < len(_in_path_params):
            the_one_in_path_params = _in_path_params
    for _url in multiurls_in_path_params:
        _in_path_params = multiurls_in_path_params[_url]
        for _param in _in_path_params:
            assert(_param in the_one_in_path_params)
    adom_is_in_path_params = False
    for item in the_one_in_path_params:
        if item['name'] == 'adom':
            adom_is_in_path_params = True
            break

    canonical_path = canonicalize_url_as_path(url)
    supported_methods = list(schema._digest[url].keys())

    # Now we have all the parameters in path for all the urls which can be merged
    # dump lots of useful information to screen.
    mutiurls_names = [_url for _url, _schema in multiurls]
    print('\t\033[36mmodule.name:\033[0m \033[37m%s\033[0m'%(canonical_path))
    print('\t\033[36mfull.url.params:\033[0m \033[37m%s\033[0m'%(str([item['name'] for item in the_one_in_path_params]).replace('\'', '')))
    print('\t\033[36msupported.method:\033[0m \033[37m%s\033[0m'%(str(supported_methods).replace('\'', '')))
    if len(multiurls) > 1:
        for _url in mutiurls_names:
            print('\t\033[36msub.url:\033[0m \033[37m%s\033[0m'%(_url))
    code_rdata = {'supported_methods': supported_methods,
                  'in_path_params': the_one_in_path_params,
                  'jrpc_urls': mutiurls_names,
                  'body_schemas': schema_beautify(transform_schema(body_schemas), 4, 1, False, True)}
    code_body = code_template.render(**code_rdata)
    
    doc_examples = generate_schema_document_examples(raw_body_schemas, canonical_path, url, the_one_in_path_params)
    doc_rdata = {'module_name': canonical_path,
                 'jrpc_urls': mutiurls_names,
                 'allowed_methods': supported_methods,
                 'doc_options': generate_schema_document_options(raw_body_schemas, the_one_in_path_params, api_endpoint_tags),
                 'doc_examples': doc_examples,
                 'doc_return': generate_schema_document_return(results_schemas)
    }
    doc_body = doc_template.render(**doc_rdata)

    with open('modules/%s.py' % (canonical_path), 'w') as f:
        f.write(doc_body)
        f.write(code_body)
        f.flush()

    # Now, generate all the .rst files
    the_one_api_endpoint_tag = None
    for method in api_endpoint_tags:
        if not the_one_api_endpoint_tag:
            the_one_api_endpoint_tag = api_endpoint_tags[method]
        else:
            assert(the_one_api_endpoint_tag == api_endpoint_tags[method])
    the_one_api_endpoint_tag = the_one_api_endpoint_tag.strip(' ')
    first_dot_pos = the_one_api_endpoint_tag.find('.')
    if first_dot_pos >= 0:
        the_one_api_endpoint_tag = the_one_api_endpoint_tag[: first_dot_pos + 1]

    docgen_data = ':source: ' + canonical_path + '.py\n'
    docgen_data += '\n:orphan:\n'
    docgen_data += '\n.. _' + canonical_path + ':\n\n'

    title = canonical_path
    if the_one_api_endpoint_tag.strip(' ') != '':
        title += ' -- ' + the_one_api_endpoint_tag
    docgen_data += title + '\n'
    docgen_data += len(title) * '+' + '\n'
    # FIXME: version is hardcoded, need a fix
    docgen_data += '\n.. versionadded:: 2.10\n\n'
    docgen_data += '.. contents::\n'
    docgen_data += '   :local:\n'
    docgen_data += '   :depth: 1\n\n\n'

    # SYNOPSIS IN DOCGEN
    docgen_data += 'Synopsis\n'
    docgen_data += '--------\n\n'
    docgen_data += '- This module is able to configure a FortiManager device by '
    docgen_data += 'allowing the user to **' + str(supported_methods).replace('\'', '')
    docgen_data += '** the following FortiManager json-rpc urls.\n'
    for url in mutiurls_names:
        docgen_data += '- `' + url + '`\n'
    docgen_data += '- Examples include all parameters and values need to be adjusted to data sources before usage.\n'
    # FIXME: need to decide which the fortimanager version is
    docgen_data += '- Tested with FortiManager v6.0.0\n\n\n'

    # REQUIREMENT IN DOCGEN
    docgen_data += 'Requirements\n'
    docgen_data += '------------\n'
    docgen_data += 'The below requirements are needed on the host that executes this module.\n\n'
    docgen_data += '- ansible>=2.10.0\n\n\n\n'
    # PARAMETERS IN DOCGEN
    docgen_data += 'Parameters\n'
    docgen_data += '----------\n\n'
    docgen_data += '.. raw:: html\n\n'
    docgen_data += generate_docgen_parameters(raw_body_schemas, the_one_in_path_params, api_endpoint_tags)
    docgen_data += '\n\n\n\n\n\n'
    #NOTES IN DOCGEN
    docgen_data += 'Notes\n'
    docgen_data += '-----\n'
    docgen_data += '.. note::\n\n'
    docgen_data += '   - The module may supports multiple method, every method has different parameters definition\n\n'
    docgen_data += '   - One method may also have more than one parameter definition collection, each collection is dedicated to one API endpoint\n\n'
    docgen_data += '   - The module may include domain dependent urls, the domain can be specified in url_params as adom\n\n'
    # EXAMPLE IN DOCGEN
    docgen_data += 'Examples\n' + '--------\n\n'
    docgen_data += '.. code-block:: yaml+jinja\n\n'
    docgen_data += doc_examples + '\n\n\n'
    
    # RETURN VALUE IN DOCGEN
    docgen_data += 'Return Values\n'
    docgen_data += '-------------\n\n\n'
    docgen_data += 'Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:\n\n'
    docgen_data += '\n.. raw:: html\n\n'
    docgen_data += generate_docgen_return_value(results_schemas)
    docgen_data += '\n\n\n\n\n'

    # STATUS IN DOCGEN
    docgen_data += 'Status\n'
    docgen_data += '------\n\n'
    docgen_data += '- This module is not guaranteed to have a backwards compatible interface.\n\n\n'
    #AUTHORS IN DOCGEN
    docgen_data += 'Authors\n'
    docgen_data += '-------\n\n'
    docgen_data += '- Frank Shen (@fshen01)\n'
    docgen_data += '- Link Zheng (@zhengl)\n\n\n'
    #HINT IN DOCGEN
    docgen_data += '.. hint::\n\n'
    docgen_data += '    If you notice any issues in this documentation, you can create a pull request to improve it.\n'
    docgen_data += '\n\n\n'
    with open('docgen/%s.rst' %(canonical_path), 'w') as f:
        f.write(docgen_data)
        f.flush()

if __name__ == '__main__':
    jinja2_file_loader = FileSystemLoader('templates')
    jinja2_env = Environment(loader=jinja2_file_loader)
    code_template = jinja2_env.get_template('code.j2')
    doc_template = jinja2_env.get_template('doc.j2')
    except_defs = dict()
    domain_independent_urls = dict()
    with open('./exceptional_definition_list.json') as f:
        except_defs = json.load(f)
    schema_directory = './fortimanager-schema/schemas'
    for schema_file in listdir(schema_directory):
        per_schema_except_def = None
        if schema_file in except_defs:
            per_schema_except_def = except_defs[schema_file]
        full_schema_path = schema_directory + '/' + schema_file
        schema = load_schema(full_schema_path, per_schema_except_def)

        for url in schema._digest:
            stripped_domain_url = url.replace('/adom/{adom}/', '/')
            stripped_domain_url = stripped_domain_url.replace('/global/', '/')
            if stripped_domain_url not in domain_independent_urls:
                domain_independent_urls[stripped_domain_url] = list()
            domain_independent_urls[stripped_domain_url].append((url, schema))
    for stripped_url in domain_independent_urls:
        url0, schema0 = domain_independent_urls[stripped_url][0]
        print('\033[32mprocessing multi-domain url:\033[0m', stripped_url)
        resolve_schema(url0, schema0, doc_template, code_template, domain_independent_urls[stripped_url])
