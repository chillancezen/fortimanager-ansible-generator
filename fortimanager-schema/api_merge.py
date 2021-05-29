#! /usr/bin/python3
import os
import sys
import json
from os import listdir
from api_schema_parser import load_schema

to_validate_schema = False

def load_schemas_per_version(version_directory, exception_def=None):
    schema_per_version = dict()
    digest_blob = dict()
    for schema_file in listdir(version_directory):
        full_path = '%s/%s' % (version_directory, schema_file)
        print('loading \033[4m\033[36m%s\033[0m' % (full_path))
        schema_per_file = load_schema(full_path, exception_def[schema_file] if exception_def and schema_file in exception_def else None)
        schema_per_file_digest = schema_per_file.get_api_digest()
        for _url in schema_per_file_digest:
            if _url not in schema_per_version:
                schema_per_version[_url] = dict()
                print('\033[37m[URL]: %s\033[0m' % (_url))
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
    validate_schema(schema_per_version, digest_blob)
     
def validate_schema(schemas, blobs):
    if not to_validate_schema:
        return
    for _url, _schema in schemas.items():
        _methods = list(_schema.keys())
        for _method in _methods:
            _digests = _schema[_method]
            assert(len(_digests))
            blobs[_digests[0]].get_function_schema(_url, _method)

if __name__ == '__main__':
    to_validate_schema = True
    version_dirs = list()
    for item in listdir('.'):
        if not os.path.isdir(item) or not item.startswith('schemas.'):
            continue
        version_dirs.append(item)
    version_dirs.sort()
    with open('../exceptional_definition_list.json') as f:
        except_defs = json.load(f)
    for version_dir in version_dirs:
        load_schemas_per_version(version_dir, except_defs)
