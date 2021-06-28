#! /usr/bin/python3
import os
import sys
import json
from os import listdir
from api_schema_parser import load_schema

to_validate_schema = False

def load_schemas_per_version(version_directory, exception_def=None, default_ref=None):
    schema_per_version = dict()
    digest_blob = dict()
    for schema_file in listdir(version_directory):
        full_path = '%s/%s' % (version_directory, schema_file)
        print('loading \033[4m\033[36m%s\033[0m' % (full_path))
        schema_per_file = load_schema(full_path, exception_def[schema_file] if exception_def and schema_file in exception_def else None, default_ref)
        schema_per_file_digest = schema_per_file.get_api_digest()
        for _url in schema_per_file_digest:
            if _url not in schema_per_version:
                schema_per_version[_url] = dict()
               # print('\033[37m[URL]: %s\033[0m' % (_url))
            else:
                # XXX: must override the previous definition
                print("[DUPLICATED_DEFINITION]: \033[04m\033[31m%s\033[0m" % (_url))
            for _method, digests in schema_per_file_digest[_url].items():
                if _method not in schema_per_version[_url]:
                        schema_per_version[_url][_method] = list()
                for _digest in digests:
                    if _digest not in schema_per_version[_url][_method]:
                        schema_per_version[_url][_method].append(_digest)
                    if _digest in digest_blob:
                        print('[DUPLICATED_DIGEST    ]: \033[04m\033[31m%s\033[0m' % (_digest))
                    digest_blob[_digest] = schema_per_file
    if to_validate_schema:
        validate_schema(schema_per_version, digest_blob)
    return schema_per_version, digest_blob
     
def validate_schema(schemas, blobs):
    for _url, _schema in schemas.items():
        _methods = list(_schema.keys())
        for _method in _methods:
            _digests = _schema[_method]
            for _digest in _digests:
                inpath_params, inbody_params, result, api_desc = blobs[_digest].get_function_schema(_url, _method)
                #print(json.dumps(inbody_params, indent=3))


def merge_digest(super_schema):
    super_digest = dict()
    api_new_stats = dict()
    for version in super_schema:
        digest_per_version = super_schema[version][0]
        for url in digest_per_version:
            if url not in super_digest:
                super_digest[url] = dict()
                super_digest[url]['revision'] = dict()
                super_digest[url]['digests'] = dict()
                for method in digest_per_version[url]:
                    super_digest[url]['digests'][method] = digest_per_version[url][method]
                #print('new in %s : %s' % (version, url))
                if version not in api_new_stats:
                    api_new_stats[version] = 0
                api_new_stats[version] += 1
            super_digest[url]['revision'][version] = True
            for method in digest_per_version[url]:
                if method not in super_digest[url]['digests']:
                    super_digest[url]['digests'][method] = digest_per_version[url][method]
                for _digested_url in digest_per_version[url][method]:
                    if _digested_url not in super_digest[url]['digests'][method]:
                        super_digest[url]['digests'][method].append(_digested_url)

    api_stats = dict()
    for url in super_digest:
        for version in super_digest[url]['revision']:
            if version not in api_stats:
                api_stats[version] = 0
            api_stats[version] += 1
    print('Number of Total API:')
    print(json.dumps(api_stats, indent=3))

    print('Number of New API(never appears in previous versions):')
    print(json.dumps(api_new_stats, indent=3))
    return super_digest


def mark_inpath_params(m_inpath_params, new_inpath_params, version, is_present=False):
    if is_present:
        for param in new_inpath_params:
            assert('name' in param and 'api_tag' in param)
            found = False
            item_index = 0
            for _param in m_inpath_params:
                if _param['name'] == param['name'] and _param['api_tag'] == param['api_tag']:
                    found = True
                    break
                item_index += 1
            if not found:
                # XXX: several cases where in-path parameters are inconsistent
                continue
            if 'revision' not in m_inpath_params[item_index]:
                m_inpath_params[item_index]['revision'] = dict()
            m_inpath_params[item_index]['revision'][version] = True
    else:
        for _param in m_inpath_params:
            if 'revision' not in _param:
                _param['revision'] = dict()
                _param['revision'][version] = False

def _mark_param_version(param, version, present):
    assert(param)
    if 'revision' not in param:
        param['revision'] = dict()
    param['revision'][version] = present

def _mark_inbody_param_definitely(param, version, is_present, recursive=True):
    if 'type' not in param or param['type'] not in ['string', 'integer', 'array', 'dict']:
        for key in param:
            if recursive:
                _mark_inbody_param_definitely(param[key], version, is_present, recursive)
    elif param['type'] == 'dict':
        _mark_param_version(param, version, is_present)
        if recursive and 'dict' in param:
            _mark_inbody_param_definitely(param['dict'], version, is_present, recursive)
    elif param['type'] in ['string', 'integer']:
        _mark_param_version(param, version, is_present)
    elif param['type'] == 'array':
        _mark_param_version(param, version, is_present)
        if recursive and 'items' in param:
            subitem = param['items']
            if 'type' not in subitem or subitem['type'] not in ['string', 'integer', 'array']:
                _mark_inbody_param_definitely(subitem, version, is_present, recursive)
            else:
                assert(subitem['type'] in ['string', 'integer'])
    else:
        assert(False)

def _mark_inbody_param(m_inbody_params, new_inbody_params, version, is_present):
    if not m_inbody_params:
        return
    if not new_inbody_params:
        _mark_inbody_param_definitely(m_inbody_params, version, False)
        return

    assert(m_inbody_params and new_inbody_params)
    if 'type' not in m_inbody_params or m_inbody_params['type'] not in ['string', 'integer', 'array', 'dict']:
        for key_present in m_inbody_params:
            _mark_inbody_param(m_inbody_params[key_present], new_inbody_params[key_present] if key_present in new_inbody_params else None, version, True)
        for key_new in new_inbody_params:
            if key_new in m_inbody_params:
                continue
            m_inbody_params[key_new] = new_inbody_params[key_new]
            _mark_inbody_param_definitely(m_inbody_params[key_new], version, True)
    elif m_inbody_params['type'] == 'dict':
        assert(new_inbody_params['type'] == 'dict')
        if 'dict' not in m_inbody_params:
            assert('dict' not in new_inbody_params)
            _mark_inbody_param_definitely(m_inbody_params, version, True)
        else:
            assert('dict' in new_inbody_params)
            _mark_inbody_param_definitely(m_inbody_params, version, True, recursive=False)
            _mark_inbody_param(m_inbody_params['dict'], new_inbody_params['dict'], version, True)
    elif m_inbody_params['type'] in ['string', 'integer']:
        # XXX: discrpendency found if types are not equal, use 1st one
        #if m_inbody_params['type'] != new_inbody_params['type']:
        #    print('found one discrpendency')
        _mark_inbody_param_definitely(m_inbody_params, version, True, recursive=False)
        if 'enum' in new_inbody_params:
            if 'enum' not in m_inbody_params:
                m_inbody_params['enum'] = list()
            for _enum_item in new_inbody_params['enum']:
                if _enum_item not in m_inbody_params['enum']:
                    assert(type(_enum_item) in [int, str])
                    m_inbody_params['enum'].append(_enum_item)
    elif m_inbody_params['type'] == 'array':
        assert('items' in m_inbody_params)
        m_subitem = m_inbody_params['items']
        if 'items' not in new_inbody_params:
            # XXX:Found another discrpendency.
            _mark_inbody_param_definitely(m_inbody_params, version, True, recursive=False)
        else:
            new_subitem = new_inbody_params['items']
            _mark_inbody_param_definitely(m_inbody_params, version, True, recursive=False)
            if 'type' not in m_subitem or m_subitem['type'] not in ['string', 'integer', 'array']:
                assert('type' not in new_subitem or new_subitem['type'] not in ['string', 'integer', 'array'])
                _mark_inbody_param(m_subitem, new_subitem, version, True)
            elif m_subitem['type'] in ['string', 'integer']:
                assert(new_subitem['type'] in ['string', 'integer'])
                if 'enum' in new_subitem:
                    if 'enum' not in m_subitem:
                        m_subitem['enum'] = list()
                    for _enum_item in new_subitem['enum']:
                        assert(type(_enum_item) in [int, str])
                        if m_subitem != new_subitem and _enum_item not in m_subitem['enum']:
                            m_subitem['enum'].append(_enum_item)
            else:
                assert(False)
    else:
        assert(False)

def mark_inbody_params(m_inbody_params, new_inbody_params, version, is_present=False):
    if is_present:
        for param_item in new_inbody_params:
            name = param_item['name']
            api_tag = param_item['api_tag']
            found = False
            item_index = 0
            for m_param_item in m_inbody_params:
                if m_param_item['name'] == name and m_param_item['api_tag'] == api_tag:
                    found = True
                    break
                item_index += 1
            if name == 'data' and found:
                _mark_inbody_param(m_inbody_params[item_index], param_item, version, True)
            elif name == 'data' and not found:
                _mark_inbody_param_definitely(param_item, version, False)
    else:
        for param_item in m_inbody_params:
            if param_item['name'] != 'data':
                continue
            _mark_inbody_param_definitely(param_item, version, False)

def get_api_definition(super_schema, url, method):
    m_inpath_params = []
    m_inbody_params = []
    m_result = None
    m_api_desc = None
    presence = dict()
    for version in super_schema:
        digest_per_version, digest_blob = super_schema[version]
        if url in digest_per_version and method not in digest_per_version[url]:
            print('mthod:%s of url:%s does not exist for version:%s' % (method, url, version))
            continue
        if url in digest_per_version:
            digests = digest_per_version[url][method]
            fmgapi_handler = None
            for _digest in digests:
                if not fmgapi_handler:
                    fmgapi_handler = digest_blob[_digest]
                else:
                    assert(fmgapi_handler == fmgapi_handler)
            inpath_params, inbody_params, result, api_desc = fmgapi_handler.get_function_schema(url, method)
            if not m_inpath_params:
                m_inpath_params = inpath_params
            if not m_inbody_params:
                m_inbody_params = inbody_params
            if not m_result:
                m_result = result
            if not m_api_desc:
                m_api_desc = api_desc
            mark_inpath_params(m_inpath_params, inpath_params, version, True)
            mark_inbody_params(m_inbody_params, inbody_params, version, True)
            presence[version] = True
        else:
            mark_inpath_params(m_inpath_params, None, version, False)
            mark_inbody_params(m_inbody_params, None, version, False)
            presence[version] = False
    return m_inpath_params, m_inbody_params, m_result, m_api_desc


if __name__ == '__main__':
    to_validate_schema = True
    version_dirs = list()
    super_schema = dict()
    for item in listdir('.'):
        if not os.path.isdir(item) or not item.startswith('schemas.'):
            continue
        version_dirs.append(item)
    version_dirs.sort()
    with open('../exceptional_definition_list.json') as f:
        except_defs = json.load(f)
    for version_dir in version_dirs:
        version = version_dir[8:]
        schema_per_version, digest_blob = load_schemas_per_version(version_dir, except_defs)
        super_schema[version] = (schema_per_version, digest_blob)
    super_digest = merge_digest(super_schema)

    for url in super_digest:
        for method in super_digest[url]['digests']:
            get_api_definition(super_schema, url, method)

