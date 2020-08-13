#! /usr/bin/python3
import json
import sys

class FMGApiSchema:    
 
    def __init__(self, data, exceptional_defs = None):
        self._data = data
        self._paths = data['swaggerData']['paths']
        self._defs = data['swaggerData']['definitions']
        self._tags = data['swaggerData']['tags']
        self._digest = self.get_api_digest()
        if exceptional_defs:
            self._except_defs = exceptional_defs
            for def_key in exceptional_defs:
                def_sub_key = exceptional_defs[def_key]
                assert(def_key in self._defs)
                assert('properties' in self._defs[def_key])
                assert(def_sub_key in self._defs[def_key]['properties'])
                del self._defs[def_key]['properties'][def_sub_key]

    def get_api_summary_keys(self):
        return [api_key for api_key in self._paths]
    
    def get_api_digest(self):
        api_keys = dict()
        api_summary_keys = self.get_api_summary_keys()
        for ask in api_summary_keys:
            params = self._paths[ask]['post']['parameters']
            in_body_param = None
            for param in params:
                if param['in'] == 'body':
                    in_body_param = param
                    break
            assert(in_body_param)
            assert('schema' in in_body_param)
            assert('properties' in in_body_param['schema'])
            assert('method' in in_body_param['schema']['properties'] and \
                   'params' in in_body_param['schema']['properties'])
            method = in_body_param['schema']['properties']['method']['example']
            url = in_body_param['schema']['properties']['params']['items']['properties']['url']['example']
            if url not in api_keys:
                api_keys[url] = dict()
            #For Certain URL, there are more than one API for it, we may coalesce
            #them into one. 
            if method not in api_keys[url]:
                api_keys[url][method] = list()
            api_keys[url][method].append(ask)
        return api_keys

    def dump_api_digest(self):
        api_keys = self.get_api_digest()
        for url in api_keys:
            print(url)
            for method in api_keys[url]:
                print("\t", method, api_keys[url][method])
 
    def __resolve_reference(self, definition):
        plain_collection = dict()
        for _key in definition:
            if _key in ['name', 'in', 'api_tag']:
                plain_collection[_key] = definition[_key]
        #recursively expand the reference point
        if '$ref' in definition:
            return self.resolve_reference(definition['$ref'])

        assert('type' in definition)
        # 'string' and 'integer' are considered atomic
        if definition['type'] == 'string' or \
           definition['type'] == 'integer':
            return definition
        elif definition['type'] == 'array':
            plain_collection['type'] = 'array'
            plain_collection['items'] = self.__resolve_reference(definition['items'])
        elif definition['type'] == 'dict':
            plain_collection = dict(definition)
            plain_collection['dict'] = self.resolve_reference(definition['dict'])
        elif definition['type'] == 'object':
            if 'properties' not in definition:
                assert('additionalProperties' in definition)
                assert(len(definition['additionalProperties'].keys()) == 1)
                assert('type' in definition['additionalProperties'])
                assert(definition['additionalProperties']['type'] == 'string')
                plain_collection['type'] = 'dict'
                #for _field in definition['additionalProperties']:
                #    plain_collection[_field] =  definition['additionalProperties'][_field]
            else:
                for prop in definition['properties']:
                    plain_collection[prop] = self.__resolve_reference(definition['properties'][prop])
        return plain_collection
                
    def resolve_reference(self, reference_name):
        return self.__resolve_reference(self._defs[reference_name.split('/')[-1]])

    def get_function_schema(self, function_url, method):
        assert(function_url in self._digest)
        assert(method in self._digest[function_url])
        schema_keys = self._digest[function_url][method]
        in_path_params = list()
        in_body_params = list()
        expanded_body_params = list()
        in_result_params = list()
        expanded_result_params = list()
        api_tag = 0
        per_url_method_tags = set()
        for schema_key in schema_keys:
            parameters = self._paths[schema_key]['post']['parameters']
            responses = self._paths[schema_key]['post']['responses']
            tags = self._paths[schema_key]['post']['tags']
            assert(len(tags) == 1)
            per_url_method_tags.add(tags[0])
            for param in parameters:
                if param['in'] == 'path':
                    _in_path_param = dict(param)
                    _in_path_param['api_tag'] = api_tag
                    in_path_params.append(_in_path_param)
                else:
                    assert('body' == param['in'])
                    body_schemas_params = param['schema']['properties']['params']
                    assert(body_schemas_params['type'] == 'array')
                    body_schemas_params = body_schemas_params['items']['properties']
                    for __param_name in body_schemas_params:
                        __param = body_schemas_params[__param_name]
                        __in_body_param = None
                        if 'type' in __param:
                            assert(__param['type'] in ['string', 'array', 'integer'])
                            __in_body_param = dict(__param)
                            __in_body_param['name'] = __param_name
                            __in_body_param['in'] = 'body'
                        else:
                            #FIXED: we will expand reference later, we introduce
                            #a new type: dict here to indicate this is a pure dictionary,
                            #not an array 
                            assert('$ref' in __param and len(__param) == 1)
                            __in_body_param = dict()
                            __in_body_param['name'] = __param_name
                            __in_body_param['in'] = 'body'
                            __in_body_param['type'] = 'dict'
                            __in_body_param['dict'] = __param['$ref']
                        __in_body_param['api_tag'] = api_tag
                        in_body_params.append(__in_body_param)
            for result_key in responses['200']['schema']['properties']['result']['items']['properties']:
                result_item = responses['200']['schema']['properties']['result']['items']['properties'][result_key]
                assert('id' in responses['200']['schema']['properties'])
                __result_param = dict()
                if 'type' in result_item:
                    assert(result_item['type'] in ['string', 'array', 'integer'])
                    __result_param = dict(result_item)
                    __result_param['name'] = result_key
                else:
                    assert('$ref' in result_item and len(result_item) == 1)
                    __result_param = dict()
                    __result_param['name'] = result_key
                    __result_param['type'] = 'dict'
                    __result_param['dict'] = result_item['$ref']
                __result_param['api_tag'] = api_tag
                in_result_params.append(__result_param)
            api_tag += 1
        #expand reference in extracted parameters
        for param in in_body_params:
            expanded_body_params.append(self.__resolve_reference(param))
        for param in in_result_params:
            expanded_result_params.append(self.__resolve_reference(param))
        # extract tag string for endpoint api endpoint
        api_endpoint_description = ''
        assert(len(per_url_method_tags) == 1)
        url_tag = per_url_method_tags.pop()
        for tag_item in self._tags:
            if tag_item['name'] == url_tag:
                api_endpoint_description = tag_item['description']
        return in_path_params, expanded_body_params, expanded_result_params, api_endpoint_description

def load_schema(schema_file, exceptional_defs = None):
    data = None
    with open(schema_file) as f:
        data = json.load(f)
    return FMGApiSchema(data, exceptional_defs)

if __name__ == '__main__':
    #except_def = {"pm.pkg":"subobj"}
    schema = load_schema(sys.argv[1])
    schema.dump_api_digest()
    #path, body = schema.get_function_schema('/dvmdb/adom/{adom}/script', 'add')
    #path, body = schema.get_function_schema('/dvmdb/global/script/{script}', 'delete')
    #print(json.dumps(body))
    #print(json.dumps(schema.resolve_reference('dvmdb.device')))
    sys.exit(1)
    for url in schema._digest:
        for method in schema._digest[url]:
            in_path, in_body, result = schema.get_function_schema(url, method)
            print(json.dumps(in_path))
