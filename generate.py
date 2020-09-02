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

def get_param_tokens(url):
    rc = list()
    for token in url.split('{'):
        if '}' in token:
            rc.append(token.split('}')[0])
    return rc

def underscore2hyphen(string):
    return string.replace('_', '-')


def hyphen2underscore(string):
    return string.replace('-', '_')

def extract_one_url_param(uri):
    left_bracket_pos = uri.find('{')
    if left_bracket_pos < 0:
        return None
    right_bracket_pos = uri.find('}')
    assert(right_bracket_pos > 0)
    param = uri[left_bracket_pos + 1: right_bracket_pos]
    assert(param != '')
    return param

def extract_url_params(uri):
    lst = list()
    while True:
        param = extract_one_url_param(uri)
        if not param:
            break
        lst.append(param)
        uri = uri.replace('/{' + param + '}', '')
    return lst

def shorten_url(uri):
    params = extract_url_params(uri)
    short_url = uri
    if len(params):
        for param in params:
            short_url = short_url.replace('/{' + param + '}', '')
        if uri.endswith('/{' + params[-1] + '}'):
            short_url += '/obj'
    return short_url

def canonicalize_url_as_path(url, ignore_last_token=False):
    exceptional_map = {
        '/pm/pkg/adom/{adom}/{pkg_path}': 'fmgr_pm_pkg',
        '/pm/pkg/global/{pkg_path}': 'fmgr_pm_pkg',
        '/pm/devprof/adom/{adom}/{pkg_path}': 'fmgr_pm_devprof_pkg',
        '/pm/wanprof/adom/{adom}/{pkg_path}': 'fmgr_pm_wanprof_pkg'
    }
    if url in exceptional_map:
        return exceptional_map[url]

    if ignore_last_token:
        url_tokens = url.split('/')
        if url_tokens[-1].startswith('{') and url_tokens[-1].endswith('}'):
            url = url[:-len(url_tokens[-1])]
            if url[-1] == '/':
                url = url[:-1]
    # the token with which to strip in the url, the order matters.
    tokens = {
        '_pm_config_obj_wireless_controller_': '_wireless_',
        '_pm_config_obj_': '_',
        '_pm_config_devprof_': '_devprof_',
        '_pm_config_pkg_': '_pkg_',
        '_pm_config_wanprof_': '_wanprof_',
        '_pm_config_device_vdom_': '_',
        'fmgr_cli_': 'fmgr_',
        '_vpn_ssl_web_': '_vpnsslweb_',
        '_wirelesscontroller_': '_',
        '+': '_',
        '__': '_'
    }
    url = url.replace('/adom/{adom}/', '/')
    url = url.replace('/global/', '/')
    url = shorten_url(url)
    canocial_url_path = 'fmgr'
    fields = url.replace('-', '').replace('_', '').split('/')
    for field in fields:
        if field == '':
            continue
        field = hyphen2underscore(field)
        field = field.strip('{')
        field = field.strip('}')
        canocial_url_path += '_' + field
    canocial_url_path = canocial_url_path.lower().replace('+', '')
    for token_key in tokens:
        canocial_url_path = canocial_url_path.replace(token_key, tokens[token_key])
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
        stripped_data = stripped_data.rstrip(' ').rstrip('-').rstrip('-')
        stripped_data = stripped_data.replace('\'', '')
        ret_lst.append('\'' + stripped_data + '\'')
    return ret_lst
def shorten_description(raw_desc, nr_start_pos):
    nr_left = 160 - nr_start_pos
    if len(raw_desc) <= nr_left:
        return raw_desc
    return raw_desc[: nr_left - 4] + '...' + ('\'' if raw_desc[0] == '\'' else '')

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
            #if param_key in ['in', 'format', 'description', 'example', 'default']:
            if param_key in ['in', 'format', 'example', 'default']:
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
            if '{' in discrete_schema_key and '}' in discrete_schema_key:
                discrete_schema_key = discrete_schema_key.replace('{', '')
                discrete_schema_key = discrete_schema_key.replace('}', '')
                discrete_schema_key = 'varidic.' + discrete_schema_key
            rdata += ' ' * depth * 4 + discrete_schema_key + ':\n'
            rdata += _generate_schema_document_options_recursilve(
                discrete_schema, depth + 1)
        return rdata

    if schema['type'] in ['string', 'integer']:
        quote = '\'' if schema['type'] == 'string' else ''
        rdata += ' ' * depth * 4 + 'type: ' + \
            schematype_displayname_mapping[schema['type']] + '\n'
        if 'default' in schema:
            default_value = str(schema['default'])
            default_value = shorten_description(default_value, depth * 4 + len('default: ') + 2)
            rdata += ' ' * depth * 4 + 'default: ' + quote + default_value + quote + '\n'
        # FIXED: some characters in description are not recognized by yaml.
        # XXX: DO NOT PUT ANY DESCRIPTION IN IN-FILE OPTIONS
        if False and 'description' in schema:
            desc_list = canonicalize_text(schema['description'])
            if (len(desc_list) > 1):
                rdata += ' ' * depth * 4 + 'description:\n'
                for item in desc_list:
                    rdata += ' ' * depth * 4 + ' - %s\n' % (shorten_description(item, depth * 4 + 3))
            else:
                rdata += ' ' * depth * 4 + 'description: '
                rdata += '\n' if not len(desc_list) else (shorten_description(desc_list[0], depth * 4 + len('description: ')) + '\n')
        if 'enum' in schema:
            rdata += ' ' * depth * 4 + 'choices:\n'
            for item in schema['enum']:
                rdata += ' ' * (depth + 1) * 4 + '- ' + quote + str(item) + quote + '\n'
    elif schema['type'] == 'dict':
        #assert('dict' in schema)
        if 'dict' in schema:
            rdata += _generate_schema_document_options_recursilve(schema['dict'], depth)
        else:
            rdata += ' ' * depth * 4 + 'type: dict\n'

    elif schema['type'] == 'array':
        assert('items' in schema)
        subitem = schema['items']
        if 'type' not in subitem or subitem['type'] not in ['string', 'integer', 'array']:
            rdata += ' ' * depth * 4 + 'type: list\n'
            rdata += ' ' * depth * 4 + 'suboptions:\n'
            rdata += _generate_schema_document_options_recursilve(schema['items'], depth + 1)
        elif subitem['type'] in ['string', 'integer']:
            if 'enum' in subitem:
                rdata += ' ' * depth * 4 + 'type: list\n'
                rdata += ' ' * depth * 4 + 'choices:\n'
                for _item in subitem['enum']:
                    rdata += ' ' * depth * 4 + ' - %s\n' % (_item)
            else:
                if '_donot_convert' not in subitem:
                    rdata += ' ' * depth * 4 + 'type: %s\n' % (schematype_displayname_mapping[subitem['type']])
                else:
                    rdata += ' ' * depth * 4 + 'type: list\n'
        else:
            assert(False)

    else:
        assert(False)

    return rdata


def generate_unified_schema_document_options(all_methods):
    options_data = ''
    options_data += ' ' * 4 + 'loose_validation:\n'
    options_data += ' ' * 8 + 'description:\n'
    options_data += ' ' * 8 + '  - Do parameter validation in a loose way\n'
    options_data += ' ' * 8 + 'type: bool\n'
    options_data += ' ' * 8 + 'required: false\n'

    options_data += ' ' * 4 + 'workspace_locking_adom:\n'
    options_data += ' ' * 8 + 'description:\n'
    options_data += ' ' * 8 + '  - the adom name to lock in case FortiManager running in workspace mode\n'
    options_data += ' ' * 8 + '  - it can be global or any other custom adom names\n'
    options_data += ' ' * 8 + 'required: false\n'
    options_data += ' ' * 8 + 'type: str\n'

    options_data += ' ' * 4 + 'workspace_locking_timeout:\n'
    options_data += ' ' * 8 + 'description:\n'
    options_data += ' ' * 8 + '  - the maximum time in seconds to wait for other user to release the workspace lock\n'
    options_data += ' ' * 8 + 'required: false\n'
    options_data += ' ' * 8 + 'type: int\n'
    options_data += ' ' * 8 + 'default: 300\n'

    options_data += ' ' * 4 + 'method:\n'
    options_data += ' ' * 8 + 'description:\n'
    options_data += ' ' * 8 + '  - The method in request\n'
    options_data += ' ' * 8 + 'required: true\n'
    options_data += ' ' * 8 + 'type: str\n'
    options_data += ' ' * 8 + 'choices:\n'
    for m in all_methods:
        options_data += ' ' * 8 + ('  - %s\n' % (m))

    options_data += ' ' * 4 + 'params:\n'
    options_data += ' ' * 8 + 'description:\n'
    options_data += ' ' * 8 + '  - The parameters for each method\n'
    options_data += ' ' * 8 + '  - See full parameters list in https://ansible-galaxy-fortimanager-docs.readthedocs.io/en/latest\n'
    options_data += ' ' * 8 + 'type: list\n'
    options_data += ' ' * 8 + 'required: false\n'

    options_data += ' ' * 4 + 'url_params:\n'
    options_data += ' ' * 8 + 'description:\n'
    options_data += ' ' * 8 + '  - The parameters for each API request URL\n'
    options_data += ' ' * 8 + '  - Also see full URL parameters in https://ansible-galaxy-fortimanager-docs.readthedocs.io/en/latest\n'
    options_data += ' ' * 8 + 'required: false\n'
    options_data += ' ' * 8 + 'type: dict\n'
    return options_data

def napi_generate_schema_document_options(in_path_schema, body_schema, level2_name, is_exec=False):
    options_data = ''
    options_data += ' ' * 4 + 'bypass_validation:\n'
    options_data += ' ' * 8 + 'description: only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters\n'
    options_data += ' ' * 8 + 'required: false\n'
    options_data += ' ' * 8 + 'type: bool\n'
    options_data += ' ' * 8 + 'default: false\n'
    options_data += ' ' * 4 + 'workspace_locking_adom:\n'
    options_data += ' ' * 8 + 'description: the adom to lock for FortiManager running in workspace mode, the value can be global and others including root\n'
    options_data += ' ' * 8 + 'required: false\n'
    options_data += ' ' * 8 + 'type: str\n'
    options_data += ' ' * 4 + 'workspace_locking_timeout:\n'
    options_data += ' ' * 8 + 'description: the maximum time in seconds to wait for other user to release the workspace lock\n'
    options_data += ' ' * 8 + 'required: false\n'
    options_data += ' ' * 8 + 'type: int\n'
    options_data += ' ' * 8 + 'default: 300\n'
    if not is_exec:
        options_data += ' ' * 4 + 'state:\n'
        options_data += ' ' * 8 + 'description: the directive to create, update or delete an object\n'
        options_data += ' ' * 8 + 'type: str\n'
        options_data += ' ' * 8 + 'required: true\n'
        options_data += ' ' * 8 + 'choices:\n'
        options_data += ' ' * 8 + '  - present\n'
        options_data += ' ' * 8 + '  - absent\n'
    options_data += ' ' * 4 + 'rc_succeeded:\n'
    options_data += ' ' * 8 + 'description: the rc codes list with which the conditions to succeed will be overriden\n'
    options_data += ' ' * 8 + 'type: list\n'
    options_data += ' ' * 8 + 'required: false\n'
    options_data += ' ' * 4 + 'rc_failed:\n'
    options_data += ' ' * 8 + 'description: the rc codes list with which the conditions to fail will be overriden\n'
    options_data += ' ' * 8 + 'type: list\n'
    options_data += ' ' * 8 + 'required: false\n'
    for param in in_path_schema:
        assert('name' in param)
        assert('type' in param)
        options_data += ' ' * 4 + param['name'] + ':\n'
        options_data += ' ' * 8 + 'type: ' + schematype_displayname_mapping[param['type']] + '\n'
        options_data += ' ' * 8 + 'required: true\n'

    if body_schema and len(body_schema) > 0:
        options_data += ' ' * 4 + level2_name + ':\n'
        options_data += ' ' * 8 + 'required: false\n'
        options_data += ' ' * 8 + 'type: dict\n'
        options_data += ' ' * 8 + 'suboptions:\n'
        options_data += _generate_schema_document_options_recursilve(body_schema, 3)
    return options_data

def generate_schema_document_options(
        raw_body_schemas, in_path_params, api_endpoint_tags):
    options_data = ''
    body_schema = transform_schema(raw_body_schemas)
    options_data += ' ' * 4 + 'loose_validation:\n'
    options_data += ' ' * 8 + 'description: Do parameter validation in a loose way\n'
    options_data += ' ' * 8 + 'required: False\n'
    options_data += ' ' * 8 + 'type: bool\n'
    options_data += ' ' * 8 + 'default: false\n'
    options_data += ' ' * 4 + 'workspace_locking_adom:\n'
    options_data += ' ' * 8 + 'description: the adom to lock in case FortiManager running in workspace mode\n'
    options_data += ' ' * 8 + 'required: False\n'
    options_data += ' ' * 8 + 'type: string\n'
    options_data += ' ' * 8 + 'choices:\n'
    options_data += ' ' * 8 + '  - global\n'
    options_data += ' ' * 8 + '  - custom adom\n'
    options_data += ' ' * 4 + 'workspace_locking_timeout:\n'
    options_data += ' ' * 8 + 'description: the maximum time in seconds to wait for other user to release the workspace lock\n'
    options_data += ' ' * 8 + 'required: False\n'
    options_data += ' ' * 8 + 'type: integer\n'
    options_data += ' ' * 8 + 'default: 300\n'
    if len(in_path_params):
        options_data += ' ' * 4 + 'url_params:\n'
        options_data += ' ' * 8 + 'description: the parameters in url path\n'
        options_data += ' ' * 8 + 'required: True\n'
        options_data += ' ' * 8 + 'type: dict\n'
        options_data += ' ' * 8 + 'suboptions:\n'
        for url_param in in_path_params:
            options_data += ' ' * 12 + url_param['name'] + ':\n'
            options_data += ' ' * 16 + 'type: ' + ('int' if url_param['type']
                                                   == 'integer' else 'str') + '\n'
            if url_param['name'] == 'adom':
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
            'description: %s\n' % (shorten_description(canonicalize_text(api_endpoint_tags[method_list[0]])[0], 8 + len('description: ')))
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
            params_data += ' <li><span class="li-head">%s</span>' % (discrete_schema_key)
            is_dict = 'type' not in discrete_schema or discrete_schema['type'] not in ['string', 'integer', 'array', 'dict']
            if is_dict:
                params_data += ' <span class="li-normal">type: dict</span> </li>\n'
                params_data += ' <ul class="ul-self">\n'
            params_data += _generate_docgen_paramters_recursively(discrete_schema)
            if is_dict:
                params_data += ' </ul>\n'
        return params_data

    if schema['type'] in ['string', 'integer']:
        if 'description' in schema:
            desc_list = canonicalize_text(schema['description'])
            the_desc = desc_list[0].strip('\'')
            first_dot_pos = the_desc.find('.')
            if first_dot_pos >= 0:
                the_desc = the_desc[: first_dot_pos + 1]
            params_data += ' - %s' % (the_desc)
        else:
            params_data += ' - No description for the parameter'
        params_data += ' <span class="li-normal">type: %s</span> ' % (schematype_displayname_mapping[schema['type']])
        if 'enum' in schema:
            params_data += ' <span class="li-normal">choices: %s</span> ' % (str([str(item) for item in schema['enum']]).replace('\'', ''))
        if 'default' in schema:
            params_data += ' <span class="li-normal">default: %s</span> ' % (schema['default'])
        params_data += '</li>\n'
    elif schema['type'] == 'dict':
        #assert(False)
        fold = True
        #fold = 'type' not in schema['dict'] or schema['dict']['type'] not in ['string', 'integer', 'array', 'dict']
        params_data += ' - No description for the parameter' if fold else ''
        params_data += ' <span class="li-normal">type: dict</span> </li>\n' if fold else '<li>\n'
        #params_data += ' <ul class="ul-self">\n' if fold else ''
        #params_data += _generate_docgen_paramters_recursively(schema['dict'])
        #params_data += ' </ul>\n' if fold else '\n'
    elif schema['type'] == 'array':
        assert('items' in schema)
        subitem = schema['items']
        params_data += ' - No description for the parameter'
        if 'type' not in subitem or subitem['type'] not in ['string', 'integer', 'array']:
            params_data += ' <span class="li-normal">type: array</span>'
            params_data += ' <ul class="ul-self">\n'
            #if 'type' in schema['items'] and schema['items']['type'] in ['string', 'integer', 'array', 'dict']:
            #    params_data += ' <li><span class="li-head">{no-name}</span>'
            params_data += _generate_docgen_paramters_recursively(schema['items'])
            params_data += ' </ul>\n'
        elif subitem['type'] in ['string', 'integer']:
            if 'enum' not in subitem:
                if '_donot_convert' not in subitem:
                    params_data += ' <span class="li-normal">type: %s</span>' % (schematype_displayname_mapping[subitem['type']])
                else:
                    params_data += ' <span class="li-normal">type: list</span>'
                params_data += '</li>\n'
            else:
                params_data += ' <span class="li-normal">type: array</span>'
                params_data += ' <span class="li-normal">choices: %s</span> ' % (str([str(item) for item in subitem['enum']]).replace('\'', ''))
                params_data += '</li>\n'
        else:
            assert(False)
    else:
        assert(False)
    return params_data

def napi_generate_docgen_parameters(in_path_schema, body_schema, module_name, short_desc, is_exec=False, is_partial=False):
    params_data = ' <ul>\n'
    params_data += ' <li><span class="li-head">bypass_validation</span> - Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal"> default: False</span> </li>\n'
    params_data += ' <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom adom including root</span> </li>\n'
    params_data += ' <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>\n'
    params_data += ' <li><span class="li-head">rc_succeeded</span> - The rc codes list with which the conditions to succeed will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>\n'
    params_data += ' <li><span class="li-head">rc_failed</span> - The rc codes list with which the conditions to fail will be overriden <span class="li-normal">type: list</span> <span class="li-required">required: false</span> </li>\n'
    if not is_exec and not is_partial:
        params_data += ' <li><span class="li-head">state</span> - The directive to create, update or delete an object <span class="li-normal">type: str</span> <span class="li-required">required: true</span> <span class="li-normal"> choices: present, absent</span> </li>\n'
    for param in in_path_schema:
        params_data += ' <li><span class="li-head">' + param['name'] + '</span> - The parameter in requested url <span class="li-normal">type: str</span> <span class="li-required">required: true</span> </li>\n'
    if body_schema and len(body_schema) >0:
        params_data += ' <li><span class="li-head">' + module_name[5:] +'</span> - ' + short_desc +' <span class="li-normal">type: dict</span></li>\n'
        params_data += ' <ul class="ul-self">\n'
        params_data += _generate_docgen_paramters_recursively(body_schema)
        params_data += ' </ul>\n'
    params_data += ' </ul>\n'
    return params_data


def generate_docgen_parameters(raw_body_schemas, in_path_params, api_endpoint_tags):
    params_data = ' <ul>\n'
    params_data += ' <li><span class="li-head">loose_validation</span> - Do parameter validation in a loose way <span class="li-normal">type: bool</span> <span class="li-required">required: false</span> <span class="li-normal">default: false</span>  </li>\n'
    params_data += ' <li><span class="li-head">workspace_locking_adom</span> - Acquire the workspace lock if FortiManager is running in workspace mode <span class="li-normal">type: str</span> <span class="li-required">required: false</span> <span class="li-normal"> choices: global, custom dom</span> </li>\n'
    params_data += ' <li><span class="li-head">workspace_locking_timeout</span> - The maximum time in seconds to wait for other users to release workspace lock <span class="li-normal">type: integer</span> <span class="li-required">required: false</span>  <span class="li-normal">default: 300</span> </li>\n'
    if len(in_path_params):
        params_data += ' <li><span class="li-head">url_params</span> - parameters in url path <span class="li-normal">type: dict</span> <span class="li-required">required: true</span></li>\n'
        params_data += ' <ul class="ul-self">\n'
        for url_param in in_path_params:
            params_data += ' <li><span class="li-head">' + url_param['name']
            params_data += '</span> - ' + ('the domain prefix' if url_param['name'] == 'adom' else 'the object name') + ' <span class="li-normal">'
            params_data += 'type: ' + ('int' if url_param['type'] == 'integer' else 'str') + '</span> '
            params_data += ('<span class="li-normal"> choices: none, global, custom dom</span>' if url_param['name'] == 'adom' else '') + '</li>\n'
        params_data += ' </ul>\n'
    body_schema = transform_schema(raw_body_schemas)

    for schema_object_key in body_schema['schema_objects']:
        schema_object = body_schema['schema_objects'][schema_object_key]
        method_list = [method for method in body_schema['method_mapping'] if
                       body_schema['method_mapping'][method] == schema_object_key]
        params_data += ' <li><span class="li-head">parameters for method: %s</span> - %s</li>\n' % (
            str(method_list).replace('\'', ''), api_endpoint_tags[method_list[0]])

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
                params_data += ' <li><span class="li-head">parameter collection %s</span></li>\n' % (tag)
                params_data += ' <ul class="ul-self">\n'
            for param in tagged_params[tag]:
                if param['name'] == 'url':
                    continue
                params_data += ' <li><span class="li-head">%s</span>' % (param['name'])
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
            if '{' in discrete_schema_key and '}' in discrete_schema_key:
                discrete_schema_key = discrete_schema_key.replace('{', '')
                discrete_schema_key = discrete_schema_key.replace('}', '')
                discrete_schema_key = 'varidic.' + discrete_schema_key
            rdata += ' ' * depth * 3 + discrete_schema_key + ':'
            rdata += _generate_schema_document_examples_recursive(
                discrete_schema, depth + 1)
        return rdata

    if schema['type'] in ['string', 'integer']:
        quote = '\'' if schema['type'] == 'string' else ''
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
            rdata += ' <value in %s%s>' % (str(enum_list).replace('\'', ''),
                                          (' default: ' + quote + '%s' + quote) % (shorten_description(str(schema['default']), 80)) if 'XXX_DONNOT_SET_default' in
                                          schema and schema['default'] != '' else '') + '\n'
        else:
            rdata += ' <value of %s%s>' % (schema['type'], (' default: ' + quote + '%s' + quote) % (shorten_description(str(schema['default']), 80)) if 'XXX_DONNOT_SET_default' in schema and schema['default'] != '' else '') + '\n'
    elif schema['type'] == 'array':
        assert('items' in schema)
        subitem = schema['items']
        if 'type' not in subitem or subitem['type'] not in ['string', 'integer', 'array']:
            rdata += '\n'
            rdata += ' ' * (depth - 1) * 3 + '  -'
            rdata += _generate_schema_document_examples_recursive(schema['items'], depth + 1)
        elif subitem['type'] in ['string', 'integer']:
            if 'enum' not in subitem:
                if '_donot_convert' not in subitem:
                    rdata += ' <value of %s>\n' % (subitem['type'])
                else:
                    rdata += ' <value of list>\n'
            else:
                rdata += '\n'
                for _item in subitem['enum']:
                    rdata += ' ' * (depth - 1) * 3 + '  - %s\n' % (_item)
        else:
            assert(False)
    elif schema['type'] == 'dict':
        #assert('dict' in schema)
        if 'dict' in schema:
            rdata += _generate_schema_document_examples_recursive(schema['dict'], depth)
        else:
            rdata += ' <value of dict>\n'
    else:
        assert(False)
    return rdata

def napi_generate_schema_document_examples(module_name, in_path_schema, body_schema, short_desc, is_exec=False, is_partial=False):
    example_data = ''
    example_data += ' - ' + 'hosts: fortimanager-inventory\n'
    example_data += ' ' * 3 + 'collections:\n'
    example_data += ' ' * 3 + '  - fortinet.fortimanager\n'
    example_data += ' ' * 3 + 'connection: httpapi\n'
    example_data += ' ' * 3 + 'vars:\n'
    example_data += ' ' * 6 + 'ansible_httpapi_use_ssl: True\n'
    example_data += ' ' * 6 + 'ansible_httpapi_validate_certs: False\n'
    example_data += ' ' * 6 + 'ansible_httpapi_port: 443\n'
    example_data += ' ' * 3 + 'tasks:\n'
    example_data += ' ' * 3 + ' - name: ' + short_desc + '\n'
    example_data += ' ' * 6 + module_name + ':\n'
    example_data += ' ' * 9 + 'bypass_validation: False\n'
    example_data += ' ' * 9 + 'workspace_locking_adom: <value in [global, custom adom including root]>\n'
    example_data += ' ' * 9 + 'workspace_locking_timeout: 300\n'
    example_data += ' ' * 9 + 'rc_succeeded: [0, -2, -3, ...]\n'
    example_data += ' ' * 9 + 'rc_failed: [-2, -3, ...]\n'
    for param in in_path_schema:
        example_data += ' ' * 9 + param['name'] + ': <your own value>\n'
    if not is_exec and not is_partial:
        example_data += ' ' * 9 + 'state: <value in [present, absent]>\n'
    if body_schema and len(body_schema) > 0:
        example_data += ' ' * 9 + module_name[5:] + ':'
        example_data += _generate_schema_document_examples_recursive(body_schema, 4)

    return example_data
def generate_schema_document_examples(
        raw_body_schemas, module_name, jrpc_url, in_path_params):
    example_data = ''
    example_data += ' - ' + 'hosts: fortimanager-inventory\n'
    example_data += ' ' * 3 + 'collections:\n'
    example_data += ' ' * 3 + '  - fortinet.fortimanager\n'
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
            example_data += '\n'
            example_data += ' ' * 3 + ' - name: '
            example_data += shorten_description(('requesting %s' % (jrpc_url.replace('/adom/{adom}/', '/').replace('/global/', '/'))).upper(), 3 + len(' - name: '))
            example_data += '\n'
            example_data += ' ' * 6 + module_name + ':\n'
            example_data += ' ' * 9 + 'loose_validation: False\n'
            example_data += ' ' * 9 + 'workspace_locking_adom: <value in [global, custom adom]>\n'
            example_data += ' ' * 9 + 'workspace_locking_timeout: 300\n'
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
            example_data += ' ' * 12 + '-\n'
            for param in tagged_params[tag]:
                example_data += ' ' * 15 + '%s:' % (param['name'])
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
        quote = '\'' if schema['type'] == 'string' else ''
        rdata += ' ' * depth * 3 + \
            'type: %s\n' % (schematype_displayname_mapping[schema['type']])
        if 'description' in schema:
            desc_list = canonicalize_text(schema['description'])
            if (len(desc_list) > 1):
                rdata += ' ' * depth * 3 + 'description: |\n'
                for item in desc_list:
                    rdata += ' ' * depth * 3 + '   %s\n' % (shorten_description(item, depth * 3 + 4))
            else:
                rdata += ' ' * depth * 3 + 'description: '
                rdata += '\n' if not len(desc_list) else (shorten_description(desc_list[0], depth * 3 + len('description: ')) + '\n')
        if 'example' in schema:
            rdata += ' ' * depth * 3 + 'example: ' + (quote + '%s' + quote +'\n') % (shorten_description(str(schema['example']), 80))
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


def generate_unified_schema_document_return():
    return_data = ''
    return_data += 'request_url:\n'
    return_data += '    description: The full url requested\n'
    return_data += '    returned: always\n'
    return_data += '    type: str\n'
    return_data += '    sample: /sys/login/user\n'

    return_data += 'response_code:\n'
    return_data += '    description: The status of api request\n'
    return_data += '    returned: always\n'
    return_data += '    type: int\n'
    return_data += '    sample: 0\n'

    return_data += 'response_message:\n'
    return_data += '    description: The descriptive message of the api response\n'
    return_data += '    type: str\n'
    return_data += '    returned: always\n'
    return_data += '    sample: OK.\n'
    return return_data


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
            return_data += ' <li> <span class="li-return"> %s </span>' % (discrete_schema_key)
            return_data += _generate_docgen_return_value_recursive(discrete_schema)
        return return_data
    if schema['type'] in ['string', 'integer']:
        if 'description' in schema:
            desc_list = canonicalize_text(schema['description'])
            the_desc = desc_list[0].strip('\'')
            first_dot_pos = the_desc.find('.')
            if first_dot_pos >= 0:
                the_desc = the_desc[: first_dot_pos + 1]
            return_data += ' - %s' % (the_desc)
        else:
            return_data += ' - No description for the parameter'
        return_data += ' <span class="li-normal">type: %s</span> ' % (schematype_displayname_mapping[schema['type']])
        if 'example' in schema:
            return_data += ' <span class="li-normal">example: %s</span> ' % (schema['example'])
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
            return_data += ' <li><span class="li-return">{no-name}</span>'
        return_data += _generate_docgen_return_value_recursive(schema['items'])
        return_data += ' </ul>\n'

    return return_data

def napi_generate_docgen_return_value():
    return_data = ' <ul>\n'
    return_data += ' <li> <span class="li-return">request_url</span> - The full url requested <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: /sys/login/user</span></li>\n'
    return_data += ' <li> <span class="li-return">response_code</span> - The status of api request <span class="li-normal">returned: always</span> <span class="li-normal">type: int</span> <span class="li-normal">sample: 0</span></li>\n'
    return_data += ' <li> <span class="li-return">response_message</span> - The descriptive message of the api response <span class="li-normal">returned: always</span> <span class="li-normal">type: str</span> <span class="li-normal">sample: OK</li>\n'
    return_data += ' <li> <span class="li-return">response_data</span> - The data body of the api response <span class="li-normal">returned: optional</span> <span class="li-normal">type: list or dict</span></li>\n'
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
                return_data += ' <li><span class="li-return">return values collection %s</span></li>\n' % (tag)
                return_data += ' <ul class="ul-self">\n'
            for param in tagged_params[tag]:
                return_data += ' <li><span class="li-return">%s</span>\n' % (param['name'])
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

def schema_to_layer2_params(schema, to_search_mkey, mkey):
    pdata = dict()
    for item_name in schema:
        item = schema[item_name]
        pdata[item_name] = dict()
        pdata[item_name]['required'] = False
        if to_search_mkey and mkey == item_name:
            pdata[item_name]['required'] = True
        if 'enum' in item:
            pdata[item_name]['choices'] = [e for e in item['enum']]
        if 'default' in item:
            pdata[item_name]['default'] = item['default']
        if to_search_mkey and mkey == item_name and 'default' in pdata[item_name]:
            del pdata[item_name]['default']

        if 'type' not in item or item['type'] not in ['string', 'integer', 'array']:
            if 'type' in item:
                assert(item['type'] == 'dict')
                assert(len(item.keys()) == 1)
            pdata[item_name]['type'] = 'dict'
            if 'type' not in item or len(item.keys()) > 1:
                pdata[item_name]['options'] = schema_to_layer2_params(item, False, None)
            continue
        if item['type'] == 'string':
            pdata[item_name]['type'] = 'str'
        elif item['type'] == 'integer':
            pdata[item_name]['type'] = 'int'
        elif item['type'] == 'array':
            assert('items' in item)
            pdata[item_name]['type'] = 'list'
            subitem = item['items']
            if 'type' not in subitem or subitem['type'] not in ['string', 'integer', 'array']:
                pdata[item_name]['options'] = schema_to_layer2_params(subitem, False, None)
            elif subitem['type'] in ['string', 'integer']:
                if 'enum' not in subitem:
                    if '_donot_convert' not in subitem:
                        pdata[item_name]['type'] = 'str' if subitem['type'] == 'string' else 'int'
                        # XXX: set a warning message here.
                        print('\t\33[33mWARNING: list to atomic type conversion:' + item_name + '\033[0m')
                else:
                    pdata[item_name]['choices'] = [i for i in subitem['enum']]
            else:
                assert(False)
        else:
            # Other type MUST NOT appear
            assert(False)
    return pdata

mkey_dataset = None
with open('module_primary_key.json', 'r') as f:
    mkey_dataset = json.load(f)
def module_primary_key(module_name, schema):
    if module_name in mkey_dataset:
        return mkey_dataset[module_name]
    for item_name in schema:
        if item_name == 'id':
            return 'id'
    for item_name in schema:
        if item_name == 'name':
            return 'name'
    print('\t\033[33mWarning: Cannot find primary key, possible options:', list(schema.keys()), '\033[0m')
    return None

wrapper_dataset = None
with open('module_toplevel_wrapper.json', 'r') as f:
    wrapper_dataset = json.load(f)

string_to_list_dataset = None
with open('module_params_list_exception.json', 'r') as f:
    string_to_list_dataset = json.load(f)

def process_string2list_parameters(module_name, schema):
    if module_name not in string_to_list_dataset:
        return schema
    for params in string_to_list_dataset[module_name]:
        assert(len(params) >= 1)
        # process 1st parameter.
        pointer = None
        ptype = None
        assert(params[0].split(':')[0] in schema)
        if len(params) == 1:
            final_key = params[0].split(':')[0]
            final_target_type = 'array'
            if len(params[0].split(':')) == 2:
                final_target_type = params[0].split(':')[1]
                assert(final_target_type in ['arrary', 'dict'])
            pointer = schema[final_key]
            assert('type' in pointer)
            assert(pointer['type'] == 'string')
            ptype = pointer['type']
            pointer['type'] = final_target_type
        else:
            pointer = schema[params[0]]
            for _item in params[1:]:
                _item_key = _item.split(':')[0]
                _item_target_type = 'array'
                if len(_item.split(':')) == 2:
                    _item_target_type = _item.split(':')[1]
                    assert(_item_target_type in ['arrary', 'dict'])

                if 'type' in pointer and pointer['type'] == 'array':
                    assert('items' in pointer)
                    assert(_item_key in pointer['items'])
                    pointer = pointer['items'][_item_key]
                else:
                    pointer = pointer[_item_key]

            ptype = pointer['type']
            pointer['type'] = _item_target_type
        assert(pointer and ptype in ['string', 'integer'])
        if pointer['type'] =='array':
            pointer['items'] = dict()
            pointer['items']['type'] = ptype
            pointer['items']['_donot_convert'] =  True
        else:
            all_keys = list(pointer.keys())
            for _key in all_keys:
                if _key == 'type':
                    continue
                del pointer[_key]

exec_mod_tracking = list()
url_mod_tracking = dict()
def resolve_generic_schema(url, schema, doc_template, code_template, multiurls, peer_url, is_exec=False, is_partial=False, api_tag=0, is_object_member=False, url_sufix=None):
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
            if item['api_tag'] != api_tag:
                continue
            in_body_params_without_apitags.append(item)
        if url not in multiurls_in_path_params:
            multiurls_in_path_params[url] = in_body_params_without_apitags
        else:
            pass
            # for object member / section value, the get has only one api_tag..
            #assert(multiurls_in_path_params[url] == in_body_params_without_apitags)
    for _url, _schema in multiurls[1:]:
        for _method in _schema._digest[_url]:
            in_path_params, in_body_params, result_schema, api_endpoint_tag = schema.get_function_schema(_url, _method)
            in_body_params_without_apitags = list()
            for item in in_path_params:
                if item['api_tag'] != api_tag:
                    continue
                in_body_params_without_apitags.append(item)
            if _url not in multiurls_in_path_params:
                multiurls_in_path_params[_url] = in_body_params_without_apitags
            else:
                pass
                #assert(multiurls_in_path_params[_url] == in_body_params_without_apitags)
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
    ignore_last_token = False if not is_exec else True
    if is_partial:
        ignore_last_token = True
    canonical_path = canonicalize_url_as_path(url, ignore_last_token=ignore_last_token)
    if is_object_member:
        assert(url_sufix)
        if canonical_path.endswith('_obj'):
            canonical_path = canonical_path[:-4]
        canonical_path += '_' + url_sufix.replace(' ', '')
    supported_methods = list(schema._digest[url].keys())
    if is_exec:
        exec_mod_tracking.append(canonical_path)
    #print(json.dumps(body_schemas))
    # Now we have all the parameters in path for all the urls which can be merged
    # dump lots of useful information to screen.
    global url_mod_tracking
    if canonical_path not in url_mod_tracking:
        url_mod_tracking[canonical_path] = list()
    url_mod_tracking[canonical_path].append(url)
    last_token = url.split('/')[-1]
    mutiurls_names = [_url for _url, _schema in multiurls]
    perobject_mutiurls_names = [_url + '/{' + last_token + '}' for _url in mutiurls_names]
    print('\t\033[36mmodule.name:\033[0m \033[37m%s\033[0m' % (canonical_path))
    print('\t\033[36mfull.url.params:\033[0m \033[37m%s\033[0m' % (str([item['name'] for item in the_one_in_path_params]).replace('\'', '')))
    print('\t\033[36msupported.method:\033[0m \033[37m%s\033[0m' % (str(supported_methods).replace('\'', '')))
    if len(multiurls) > 1:
        if not is_exec:
            assert(adom_is_in_path_params)
    for _url in mutiurls_names:
        print('\t\033[36msub.url:\033[0m \033[37m%s\033[0m' % (_url))
    for _url in perobject_mutiurls_names:
        print('\t\033[36msub.url:\033[0m \033[37m%s\033[0m' % (_url))

    # Note method Add/Update share the same schema
    the_unique_schema = None
    the_unique_method = 'add' if not is_exec else 'exec'
    if the_unique_method == 'add' and the_unique_method not in body_schemas:
        assert('set' in body_schemas)
        the_unique_method = 'set'
    the_unique_type = 'array' if not is_exec else 'dict'
    the_unique_subitem = 'items' if not is_exec else 'dict'
    for top_schema in body_schemas[the_unique_method]:
        if top_schema['name'] != 'url':
            #assert(not the_unique_schema)
            the_unique_schema = top_schema
    #assert(the_unique_schema)
    if the_unique_schema:
        the_unique_type = the_unique_schema['type']
        the_unique_subitem = 'items' if 'items' in the_unique_schema else 'dict'
        assert(the_unique_type in ['array', 'dict'])
        assert(the_unique_subitem in ['items', 'dict'])
    # Determine the primary key for the module
    mkey = None
    if not is_exec and the_unique_schema and not is_partial:
        mkey = module_primary_key(canonical_path, the_unique_schema[the_unique_subitem])
    if mkey:
        print('\t\033[36mprimary key:\033[0m \033[37m', mkey, '\033[0m')
    if the_unique_schema:
        process_string2list_parameters(canonical_path, the_unique_schema[the_unique_subitem])

    if is_object_member and 'items' in the_unique_schema[the_unique_subitem]:
        #assert('items' in the_unique_schema[the_unique_subitem])
        the_unique_schema[the_unique_subitem] = the_unique_schema[the_unique_subitem]['items']
    code_rdata = {'supported_methods': supported_methods,
                  'in_path_params': the_one_in_path_params,
                  'jrpc_urls': mutiurls_names if not is_object_member else [e + '/' + url_sufix for e in mutiurls_names],
                  'perobject_jrpc_urls': perobject_mutiurls_names if not is_object_member else [e + '/' + url_sufix for e in perobject_mutiurls_names],
                  'mkey': mkey,
                  'top_level_schema_name': wrapper_dataset[canonical_path] if canonical_path in wrapper_dataset else (the_unique_schema['name'] if the_unique_schema else None),
                  'is_partial': is_partial,
                  'level2_name': canonical_path[5:],
                  'body_schemas': schema_beautify(schema_to_layer2_params(the_unique_schema[the_unique_subitem], True, mkey), 12, 1, False, True) if the_unique_schema else {}}
                  #'body_schemas': schema_beautify(transform_schema(body_schemas), 4, 1, False, True)}
    code_body = code_template.render(**code_rdata)
    short_description = shorten_description(canonicalize_text(api_endpoint_tags[supported_methods[0]])[0], len('short_description: ')).replace('\'', '')
    #doc_examples = generate_schema_document_examples(raw_body_schemas, canonical_path, url, the_one_in_path_params)
    doc_examples = napi_generate_schema_document_examples(canonical_path, the_one_in_path_params, the_unique_schema[the_unique_subitem] if the_unique_schema else {}, 'no description' if short_description == '' else short_description, is_exec=is_exec, is_partial=is_partial)
    doc_rdata = {'module_name': canonical_path,
                 'jrpc_urls': mutiurls_names,
                 'short_description': 'no description' if short_description == '' else short_description,
                 'allowed_methods': supported_methods,
                 #'doc_options': generate_schema_document_options(raw_body_schemas, the_one_in_path_params, api_endpoint_tags),
                 #'doc_options': generate_unified_schema_document_options(supported_methods),
                 'doc_options': napi_generate_schema_document_options(the_one_in_path_params, the_unique_schema[the_unique_subitem] if the_unique_schema else {}, canonical_path[5:], is_exec=is_exec),
                 'doc_examples': doc_examples,
                 #'doc_return': generate_schema_document_return(results_schemas)
                 'doc_return': generate_unified_schema_document_return()
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
    docgen_data += '- This module is able to configure a FortiManager device.\n'
    docgen_data += '- Examples include all parameters and values need to be adjusted to data sources before usage.\n'
    # FIXME: need to decide which the fortimanager version is
    docgen_data += '- Tested with FortiManager v6.0.0.\n\n\n'

    # REQUIREMENT IN DOCGEN
    docgen_data += 'Requirements\n'
    docgen_data += '------------\n'
    docgen_data += 'The below requirements are needed on the host that executes this module.\n\n'
    docgen_data += '- ansible>=2.9.0\n\n\n\n'
    # PARAMETERS IN DOCGEN
    docgen_data += 'Parameters\n'
    docgen_data += '----------\n\n'
    docgen_data += '.. raw:: html\n\n'
    #docgen_data += generate_docgen_parameters(raw_body_schemas, the_one_in_path_params, api_endpoint_tags)
    docgen_data += napi_generate_docgen_parameters(the_one_in_path_params, the_unique_schema[the_unique_subitem] if the_unique_schema else {}, canonical_path, 'no description' if short_description == '' else short_description, is_exec=is_exec, is_partial=is_partial)
    docgen_data += '\n\n\n\n\n\n'
    # NOTES IN DOCGEN
    docgen_data += 'Notes\n'
    docgen_data += '-----\n'
    docgen_data += '.. note::\n\n'
    docgen_data += '   - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.\n\n'
    docgen_data += '   - To create or update an object, use state: present directive.\n\n'
    docgen_data += '   - To delete an object, use state: absent directive\n\n'
    docgen_data += '   - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded\n\n'
    # EXAMPLE IN DOCGEN
    docgen_data += 'Examples\n' + '--------\n\n'
    docgen_data += '.. code-block:: yaml+jinja\n\n'
    docgen_data += doc_examples + '\n\n\n'

    # RETURN VALUE IN DOCGEN
    docgen_data += 'Return Values\n'
    docgen_data += '-------------\n\n\n'
    docgen_data += 'Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:\n\n'
    docgen_data += '\n.. raw:: html\n\n'
    #docgen_data += generate_docgen_return_value(results_schemas)
    docgen_data += napi_generate_docgen_return_value()
    docgen_data += '\n\n\n\n\n'

    # STATUS IN DOCGEN
    docgen_data += 'Status\n'
    docgen_data += '------\n\n'
    docgen_data += '- This module is not guaranteed to have a backwards compatible interface.\n\n\n'
    # AUTHORS IN DOCGEN
    docgen_data += 'Authors\n'
    docgen_data += '-------\n\n'
    docgen_data += '- Link Zheng (@chillancezen)\n'
    docgen_data += '- Jie Xue (@JieX19)\n'
    docgen_data += '- Frank Shen (@fshen01)\n'
    docgen_data += '- Hongbin Lu (@fgtdev-hblu)\n\n\n'
    # HINT IN DOCGEN
    docgen_data += '.. hint::\n\n'
    docgen_data += '    If you notice any issues in this documentation, you can create a pull request to improve it.\n'
    docgen_data += '\n\n\n'
    doc_prefix = 'docgen' if not is_exec else 'daemon_docgen'
    with open('%s/%s.rst' % (doc_prefix, canonical_path), 'w') as f:
        f.write(docgen_data)
        f.flush()


def __validate_schema_for_method_move(path_schema, body_schema):
    assert(len(body_schema) == 3)
    flag = dict()
    for _schema in body_schema:
        assert('name' in _schema)
        flag[_schema['name']] = True
    assert('option' in flag)
    assert('target' in flag)
    assert('url' in flag)
    assert(len(path_schema))

if __name__ == '__main__':
    jinja2_file_loader = FileSystemLoader('templates')
    jinja2_env = Environment(loader=jinja2_file_loader)
    code_template = jinja2_env.get_template('code.j2')
    exec_code_template = jinja2_env.get_template('exec_code.j2')
    doc_template = jinja2_env.get_template('doc.j2')
    facts_template = jinja2_env.get_template('fact.j2')
    facts_rst_template = jinja2_env.get_template('fmgr_fact.rst.j2')
    move_template = jinja2_env.get_template('move.j2')
    move_rst_template = jinja2_env.get_template('fmgr_move.rst.j2')
    clone_template = jinja2_env.get_template('clone.j2')
    clone_rst_template =jinja2_env.get_template('fmgr_clone_rst.j2')

    except_defs = dict()
    domain_independent_urls = dict()
    curd_urls = dict()
    partial_curd_urls = dict()
    with open('./exceptional_definition_list.json') as f:
        except_defs = json.load(f)
    schema_directory = './fortimanager-schema/schemas'

    # Categorize all domain independent urls.
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
    # module with move/clone methods
    clone_metadata = dict()
    for stripped_url in domain_independent_urls:
        _url, _schema = domain_independent_urls[stripped_url][0]
        _methods = set(_schema._digest[_url].keys())
        if 'clone' not in _methods:
            continue
        _schemas = _schema.get_function_schema(_url, 'clone')
        _path_schema = _schemas[0]
        _body_schema = _schemas[1]
        _the_unique_schema = None
        for _item in _body_schema:
            if _item['name'] == 'data':
                _the_unique_schema = _item
                break
        assert(_the_unique_schema)
        assert(_the_unique_schema['type'] == 'dict')
        assert('dict' in _the_unique_schema)
        selector = canonicalize_url_as_path(stripped_url)
        assert(selector.startswith('fmgr_') and selector.endswith('_obj'))
        selector = selector[5: -4]
        mkey = module_primary_key('fmgr_' + selector, _the_unique_schema['dict'])
        complex_mkey_mapping = {
            'complex:{{module}}["_scope"][0]["name"]+"/"+{{module}}["_scope"][0]["vdom"]': '_scope'
        }
        if mkey and mkey.startswith('complex:'):
            if mkey in complex_mkey_mapping:
                mkey = complex_mkey_mapping[mkey]
        metadata = dict()
        metadata['urls'] = [_url for _url, _schema in domain_independent_urls[stripped_url]]
        metadata['params'] = [_item['name'] for _item in _path_schema]
        if len(metadata['urls']) > 1:
            assert('adom' in metadata['params'])
        metadata['selector'] = selector
        metadata['mkey'] = mkey
        clone_metadata[selector] = metadata
    rdata = {
        'metadata': clone_metadata
    }
    rbody = clone_template.render(**rdata)
    rst_rbody = clone_rst_template.render(**rdata)

    with open('modules/fmgr_clone.py', 'w') as f:
        f.write(rbody)
        f.flush()
    with open('fmgr_clone.rst', 'w') as f:
        f.write(rst_rbody)
        f.flush()

    move_metadata = dict()
    for stripped_url in domain_independent_urls:
        _url, _schema = domain_independent_urls[stripped_url][0]
        _methods = set(_schema._digest[_url].keys())
        if 'move' not in _methods:
            continue
        _schemas = _schema.get_function_schema(_url, 'move')
        _path_schema = _schemas[0]
        _body_schema = _schemas[1]
        __validate_schema_for_method_move(_path_schema, _body_schema)
        _allurls = [_url for _url, _schema in domain_independent_urls[stripped_url]]
        metadata = dict()
        metadata['urls'] = _allurls
        metadata['params'] = [_item['name'] for _item in _path_schema]
        assert('adom' in metadata['params'])
        selector = canonicalize_url_as_path(stripped_url)
        assert(selector.startswith('fmgr_') and selector.endswith('_obj'))
        selector = selector[5: -4]
        metadata['selector'] = selector
        move_metadata[selector] = metadata
    rdata = {
        'metadata': move_metadata
    }
    rbody = move_template.render(**rdata)
    rst_rbody = move_rst_template.render(**rdata)
    with open('modules/fmgr_move.py', 'w') as f:
        f.write(rbody)
        f.flush()
    with open('fmgr_move.rst', 'w') as f:
        f.write(rst_rbody)
        f.flush()
    # modules with Object Member
    for stripped_url in domain_independent_urls:
        _url, _schema = domain_independent_urls[stripped_url][0]
        _methods = set(_schema._digest[_url].keys())
        if 'set' not in _methods or 'delete' not in _methods:
            continue
        if len(_schema._digest[_url]['set']) > 1:
            assert(len(_schema._digest[_url]['delete']) > 1)
            urls_descs = _schema._digest[_url]['set']
            long_url = urls_descs[0] if len(urls_descs[0]) > len(urls_descs[1]) else urls_descs[1]
            token = long_url.split('/')[-1][:-len(' (set)')]
            print('\033[32mprocessing object-member/section value url:\033[0m', stripped_url)
            resolve_generic_schema(_url, _schema, doc_template, code_template, domain_independent_urls[stripped_url], None, is_partial=False, api_tag=1, is_object_member=True, url_sufix=token)
    # Find out all the urls with EXEC methods.
    for stripped_url in domain_independent_urls:
        _url, _schema = domain_independent_urls[stripped_url][0]
        _methods = set(_schema._digest[_url].keys())
        if 'exec' not in _methods:
            continue
        print('\033[32mprocessing EXEC multi-domain url:\033[0m', stripped_url)
        resolve_generic_schema(_url, _schema, doc_template, exec_code_template, domain_independent_urls[stripped_url], None, is_exec=True)
    # Find out all the urls with GET methods.
    facts_metadata = dict()
    for stripped_url in domain_independent_urls:
        if not stripped_url.endswith('}'):
            continue
        perobj_url, perobj_schema = domain_independent_urls[stripped_url][0]
        perobj_methods = set(perobj_schema._digest[perobj_url].keys())
        perobj_allurls = [_url for _url, _schema in domain_independent_urls[stripped_url]]
        if 'get' not in perobj_methods:
            continue
        selector = canonicalize_url_as_path(stripped_url)
        assert(selector.startswith('fmgr_') and selector.endswith('_obj'))
        selector = selector[5: -4]
        all_params = get_param_tokens(stripped_url)
        for url in perobj_allurls:
            if '/adom/{adom}/' in url:
                assert('adom' not in all_params)
                all_params.append('adom')
                break
        facts_metadata[selector] = dict()
        facts_metadata[selector]['params'] = all_params
        facts_metadata[selector]['urls'] = perobj_allurls
   
    rdata = {
        'metadata': facts_metadata   
    }
    rbody = facts_template.render(**rdata)
    rst_rbody = facts_rst_template.render(**rdata)

    with open('modules/fmgr_fact.py', 'w') as f:
        f.write(rbody)
        f.flush()

    with open('fmgr_fact.rst', 'w') as f:
        f.write(rst_rbody)
        f.flush()

    # Merge those modules which have CRUD semantics
    for stripped_url in domain_independent_urls:
        if not stripped_url.endswith('}'):
            last_token = stripped_url.split('/')[-1]
            perobj_stripped_url = stripped_url + '/{' + last_token + '}'
            has_perobj = perobj_stripped_url in domain_independent_urls
            if not has_perobj:
                print('does not have peer:' + stripped_url)
                continue
            nonperobj_url, nonperobj_schema = domain_independent_urls[stripped_url][0]
            perobj_url, perobj_schema = domain_independent_urls[perobj_stripped_url][0]

            nonperobj_methods = set(nonperobj_schema._digest[nonperobj_url].keys())
            perobj_methods = set(perobj_schema._digest[perobj_url].keys())
            all_methods = nonperobj_methods | perobj_methods
            if 'get' in all_methods and \
               'add' in all_methods and \
               'delete' in all_methods and \
               'update' in all_methods:
                curd_urls[stripped_url] = perobj_stripped_url
                curd_urls[perobj_stripped_url] = stripped_url
                assert('add' in nonperobj_methods)
                assert('get' in perobj_methods)
                assert('delete' in perobj_methods)
                assert('update' in perobj_methods)
            else:
                print('have incomplete peer:' + str(set([nonperobj_url, perobj_url])) + str(nonperobj_methods) + str(perobj_methods))
    # Find those modules who have partial CRUD semantics: every module of this category must have update/get method
    for stripped_url in domain_independent_urls:
        if stripped_url in curd_urls:
            continue
        _url, _schema = domain_independent_urls[stripped_url][0]
        _methods = set(_schema._digest[_url].keys())
        if 'set' not in _methods or 'get' not in _methods:
            continue
        _module_name = canonicalize_url_as_path(stripped_url, True)
        partial_curd_urls[_module_name] = stripped_url
        print('\033[32mprocessing partial CURD multi-domain url:\033[0m', stripped_url)
        resolve_generic_schema(_url, _schema, doc_template, code_template, domain_independent_urls[stripped_url], None, is_partial=True)
    # Now we have per-object url mapping, these modules will be applied with present/absent Ansible semantics
    for stripped_url in curd_urls:
        if stripped_url.endswith('}'):
            continue
        url0, schema0 = domain_independent_urls[stripped_url][0]
        print('\033[32mprocessing CURD multi-domain url:\033[0m', stripped_url)
        print('\t\033[32m                peer url:\033[0m', curd_urls[stripped_url])
        resolve_generic_schema(url0, schema0, doc_template, code_template, domain_independent_urls[stripped_url], curd_urls[stripped_url])
