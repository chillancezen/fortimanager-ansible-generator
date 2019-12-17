#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fmgr_cli_system_admin_ldap
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis:
    - /cli/global/system/admin/ldap
    - Examples include all parameters and values need to be adjusted to data 
      sources before usage.
     

version_added: "2.10"
author:
    - Frank Shen (@fshen01)
    - Link Zheng (@zhengl)
notes:
    - There are only three top-level parameters where 'method' is always required
      while other two 'params' and 'url_params' can be optional
    - Due to the complexity of fortimanager api schema, the validation is done
      out of Ansible native parameter validation procedure.
    - The syntax of OPTIONS doen not comply with the standard Ansible argument 
      specification, but with the structure of fortimanager API schema, we need
      a trivial transformation when we are filling the ansible playbook
options:
    schema_object0:
        methods: [add, set, update]
        description: 'LDAP server entry configuration.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    adom:
                        -
                            adom-name:
                                type: str
                                description: 'Admin domain names.'
                    adom-attr:
                        type: str
                        description: 'Attribute used to retrieve adom'
                    attributes:
                        type: str
                        default: member,uniquemember,memberuid
                        description: 'Attributes used for group searching.'
                    ca-cert:
                        type: str
                        description: 'CA certificate name.'
                    cnid:
                        type: str
                        default: cn
                        description: 'Common Name Identifier (default = CN).'
                    connect-timeout:
                        type: int
                        default: 500
                        description: 'LDAP connection timeout (msec).'
                    dn:
                        type: str
                        description: 'Distinguished Name.'
                    filter:
                        type: str
                        default: (objectclass=*)
                        description: 'Filter used for group searching.'
                    group:
                        type: str
                        description: 'Full base DN used for group searching.'
                    memberof-attr:
                        type: str
                        description: 'Attribute used to retrieve memeberof.'
                    name:
                        type: str
                        description: 'LDAP server entry name.'
                    password:
                        -
                            type: str
                            default: ENC MTEyODQwMzUzNTU5OTkxNiMZsnjCaX8v5NaNPmglZ1pwQh+wPb8bwCFjVP5hUgQnOleEpUJ7ARHGG9tpPDKAZE74Ep4RHCgPsKLw3wtuNG0kB3r6RBqrFQcvA/t/txyxY2LlhN4+ewvQsITXDVyOmmyE1tqgG/9GpJNNqPCgZsW36+Oo
                    port:
                        type: int
                        default: 389
                        description: 'Port number of LDAP server (default = 389).'
                    profile-attr:
                        type: str
                        description: 'Attribute used to retrieve admin profile.'
                    secondary-server:
                        type: str
                        description: '{<name_str|ip_str>} secondary LDAP server domain name or IP.'
                    secure:
                        type: str
                        default: disable
                        description:
                         - 'SSL connection.'
                         - 'disable - No SSL.'
                         - 'starttls - Use StartTLS.'
                         - 'ldaps - Use LDAPS.'
                        choices:
                            - disable
                            - starttls
                            - ldaps
                    server:
                        type: str
                        description: '{<name_str|ip_str>} LDAP server domain name or IP.'
                    tertiary-server:
                        type: str
                        description: '{<name_str|ip_str>} tertiary LDAP server domain name or IP.'
                    type:
                        type: str
                        default: simple
                        description:
                         - 'Type of LDAP binding.'
                         - 'simple - Simple password authentication without search.'
                         - 'anonymous - Bind using anonymous user search.'
                         - 'regular - Bind using username/password and then search.'
                        choices:
                            - simple
                            - anonymous
                            - regular
                    username:
                        type: str
                        description: 'Username (full DN) for initial binding.'
    schema_object1:
        methods: [get]
        description: 'LDAP server entry configuration.'
        api_categories: [api_tag0]
        api_tag0:
            fields:
                -
                    -
                        type: str
                        choices:
                            - adom-attr
                            - attributes
                            - ca-cert
                            - cnid
                            - connect-timeout
                            - dn
                            - filter
                            - group
                            - memberof-attr
                            - name
                            - password
                            - port
                            - profile-attr
                            - secondary-server
                            - secure
                            - server
                            - tertiary-server
                            - type
                            - username
            filter:
                -
                    type: str
            loadsub:
                type: int
                description: 'Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.'
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.'
                 - 'count - Return the number of matching entries instead of the actual entry data.'
                 - 'syntax - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.'
                choices:
                    - count
                    - syntax

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /cli/system/admin/ldap
      fmgr_cli_system_admin_ldap:
         method: <value in [add, set, update]>
         params:
            - 
               data: 
                - 
                     adom: 
                      - 
                           adom-name: <value of string>
                     adom-attr: <value of string>
                     attributes: <value of string default: member,uniquemember,memberuid>
                     ca-cert: <value of string>
                     cnid: <value of string default: cn>
                     connect-timeout: <value of integer default: 500>
                     dn: <value of string>
                     filter: <value of string default: (objectclass=*)>
                     group: <value of string>
                     memberof-attr: <value of string>
                     name: <value of string>
                     password: 
                      - <value of string default: ENC MTEyODQwMzUzNTU5OTkxNiMZsnjCaX8v5NaNPmglZ1pwQh+wPb8bwCFjVP5hUgQnOleEpUJ7ARHGG9tpPDKAZE74Ep4RHCgPsKLw3wtuNG0kB3r6RBqrFQcvA/t/txyxY2LlhN4+ewvQsITXDVyOmmyE1tqgG/9GpJNNqPCgZsW36+Oo>
                     port: <value of integer default: 389>
                     profile-attr: <value of string>
                     secondary-server: <value of string>
                     secure: <value in [disable, starttls, ldaps] default: disable>
                     server: <value of string>
                     tertiary-server: <value of string>
                     type: <value in [simple, anonymous, regular] default: simple>
                     username: <value of string>
    - name: send request to /cli/system/admin/ldap
      fmgr_cli_system_admin_ldap:
         method: <value in [get]>
         params:
            - 
               fields: 
                - 
                   - <value in [adom-attr, attributes, ca-cert, ...]>
               filter: 
                - <value of string>
               loadsub: <value of integer>
               option: <value in [count, syntax]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[add, set, update]
   returned: always
   suboptions:
      id:
         type: int
      result:
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /cli/global/system/admin/ldap
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            type: array
            suboptions:
               adom:
                  type: array
                  suboptions:
                     adom-name:
                        type: str
                        description: 'Admin domain names.'
               adom-attr:
                  type: str
                  description: 'Attribute used to retrieve adom'
               attributes:
                  type: str
                  description: 'Attributes used for group searching.'
                  example: member,uniquemember,memberuid
               ca-cert:
                  type: str
                  description: 'CA certificate name.'
               cnid:
                  type: str
                  description: 'Common Name Identifier (default = CN).'
                  example: cn
               connect-timeout:
                  type: int
                  description: 'LDAP connection timeout (msec).'
                  example: 500
               dn:
                  type: str
                  description: 'Distinguished Name.'
               filter:
                  type: str
                  description: 'Filter used for group searching.'
                  example: (objectclass=*)
               group:
                  type: str
                  description: 'Full base DN used for group searching.'
               memberof-attr:
                  type: str
                  description: 'Attribute used to retrieve memeberof.'
               name:
                  type: str
                  description: 'LDAP server entry name.'
               password:
                  type: array
                  suboptions:
                     type: str
                     example: ENC MTEyODQwMzUzNTU5OTkxNiMZsnjCaX8v5NaNPmglZ1pwQh+wPb8bwCFjVP5hUgQnOleEpUJ7ARHGG9tpPDKAZE74Ep4RHCgPsKLw3wtuNG0kB3r6RBqrFQcvA/t/txyxY2LlhN4+ewvQsITXDVyOmmyE1tqgG/9GpJNNqPCgZsW36+Oo
               port:
                  type: int
                  description: 'Port number of LDAP server (default = 389).'
                  example: 389
               profile-attr:
                  type: str
                  description: 'Attribute used to retrieve admin profile.'
               secondary-server:
                  type: str
                  description: '{<name_str|ip_str>} secondary LDAP server domain name or IP.'
               secure:
                  type: str
                  description: |
                     'SSL connection.'
                     'disable - No SSL.'
                     'starttls - Use StartTLS.'
                     'ldaps - Use LDAPS.'
                  example: disable
               server:
                  type: str
                  description: '{<name_str|ip_str>} LDAP server domain name or IP.'
               tertiary-server:
                  type: str
                  description: '{<name_str|ip_str>} tertiary LDAP server domain name or IP.'
               type:
                  type: str
                  description: |
                     'Type of LDAP binding.'
                     'simple - Simple password authentication without search.'
                     'anonymous - Bind using anonymous user search.'
                     'regular - Bind using username/password and then search.'
                  example: simple
               username:
                  type: str
                  description: 'Username (full DN) for initial binding.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /cli/global/system/admin/ldap

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible.module_utils.network.fortimanager.common import FAIL_SOCKET_MSG
from ansible.module_utils.network.fortimanager.common import DEFAULT_RESULT_OBJ
from ansible.module_utils.network.fortimanager.common import FMGRCommon
from ansible.module_utils.network.fortimanager.common import FMGBaseException
from ansible.module_utils.network.fortimanager.fortimanager import FortiManagerHandler

def main():
    jrpc_urls = [
        '/cli/global/system/admin/ldap'
    ]

    url_schema = [
    ]

    body_schema =  {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'adom': {
                            'type': 'array',
                            'items': {
                                'adom-name': {
                                    'type': 'string'
                                }
                            }
                        },
                        'adom-attr': {
                            'type': 'string'
                        },
                        'attributes': {
                            'type': 'string',
                            'default': 'member,uniquemember,memberuid'
                        },
                        'ca-cert': {
                            'type': 'string'
                        },
                        'cnid': {
                            'type': 'string',
                            'default': 'cn'
                        },
                        'connect-timeout': {
                            'type': 'integer',
                            'default': 500,
                            'example': 500
                        },
                        'dn': {
                            'type': 'string'
                        },
                        'filter': {
                            'type': 'string',
                            'default': '(objectclass=*)'
                        },
                        'group': {
                            'type': 'string'
                        },
                        'memberof-attr': {
                            'type': 'string'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'password': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'default': 'ENC MTEyODQwMzUzNTU5OTkxNiMZsnjCaX8v5NaNPmglZ1pwQh+wPb8bwCFjVP5hUgQnOleEpUJ7ARHGG9tpPDKAZE74Ep4RHCgPsKLw3wtuNG0kB3r6RBqrFQcvA/t/txyxY2LlhN4+ewvQsITXDVyOmmyE1tqgG/9GpJNNqPCgZsW36+Oo'
                            }
                        },
                        'port': {
                            'type': 'integer',
                            'default': 389,
                            'example': 389
                        },
                        'profile-attr': {
                            'type': 'string'
                        },
                        'secondary-server': {
                            'type': 'string'
                        },
                        'secure': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'starttls',
                                'ldaps'
                            ]
                        },
                        'server': {
                            'type': 'string'
                        },
                        'tertiary-server': {
                            'type': 'string'
                        },
                        'type': {
                            'type': 'string',
                            'default': 'simple',
                            'enum': [
                                'simple',
                                'anonymous',
                                'regular'
                            ]
                        },
                        'username': {
                            'type': 'string'
                        }
                    }
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object1': [
                {
                    'name': 'fields',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'enum': [
                                'adom-attr',
                                'attributes',
                                'ca-cert',
                                'cnid',
                                'connect-timeout',
                                'dn',
                                'filter',
                                'group',
                                'memberof-attr',
                                'name',
                                'password',
                                'port',
                                'profile-attr',
                                'secondary-server',
                                'secure',
                                'server',
                                'tertiary-server',
                                'type',
                                'username'
                            ]
                        }
                    }
                },
                {
                    'name': 'filter',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'example': [
                                '<attr>',
                                '==',
                                'test'
                            ]
                        }
                    },
                    'api_tag': 0
                },
                {
                    'type': 'integer',
                    'name': 'loadsub',
                    'api_tag': 0
                },
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'count',
                            'syntax'
                        ]
                    },
                    'api_tag': 0
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ]
        },
        'method_mapping': {
            'add': 'object0',
            'get': 'object1',
            'set': 'object0',
            'update': 'object0'
        }
    }


    module_arg_spec = {
        'params': {
            'type': 'list',
            'required': False
        },
        'method': {
            'type': 'str',
            'required': True,
            'choices': [
                'add',
                'get',
                'set',
                'update'
            ]
        },
        'url_params': {
            'type': 'dict',
            'required': False
        }
    }
    module = AnsibleModule(argument_spec = module_arg_spec,
                           supports_check_mode = False)
    method = module.params['method']

    fmgr = None
    payload = None
    response = DEFAULT_RESULT_OBJ

    if module._socket_path:
        connection = Connection(module._socket_path)
        tools = FMGRCommon()
        tools.validate_module_params(module, body_schema)
        tools.validate_module_url_params(module, jrpc_urls, url_schema)
        full_url = tools.get_full_url_path(module, jrpc_urls)
        payload = tools.get_full_payload(module, full_url)
        fmgr = FortiManagerHandler(connection, module)
        fmgr.tools = tools
    else:
        module.fail_json(**FAIL_SOCKET_MSG)

    try:
        response = fmgr._conn.send_request(method, payload)
        fmgr.govern_response(module = module, results = response,
                             msg = 'Operation Finished',
                             ansible_facts = fmgr.construct_ansible_facts(
                                response, module.params, module.params))
    except Exception as e:
        raise FMGBaseException(e)

    module.exit_json(**response[1])

if __name__ == '__main__':
    main()