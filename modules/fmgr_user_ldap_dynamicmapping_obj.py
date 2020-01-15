#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019-2020 Fortinet, Inc.
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
module: fmgr_user_ldap_dynamicmapping_obj
short_description: no description
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/user/ldap/{ldap}/dynamic_mapping/{dynamic_mapping}
    - /pm/config/global/obj/user/ldap/{ldap}/dynamic_mapping/{dynamic_mapping}
    - Examples include all parameters and values need to be adjusted to data sources before usage.

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
    url_params:
        description: the parameters in url path
        required: True
        type: dict
        suboptions:
            adom:
                type: str
                description: the domain prefix, the none and global are reserved
                choices:
                  - none
                  - global
                  - custom dom
            ldap:
                type: str
            dynamic_mapping:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
            data:
                _scope:
                    -
                        name:
                            type: str
                        vdom:
                            type: str
                account-key-filter:
                    type: str
                account-key-name:
                    type: str
                account-key-processing:
                    type: str
                    choices:
                        - 'same'
                        - 'strip'
                ca-cert:
                    type: str
                cnid:
                    type: str
                dn:
                    type: str
                filter:
                    type: str
                group:
                    type: str
                group-filter:
                    type: str
                group-member-check:
                    type: str
                    choices:
                        - 'user-attr'
                        - 'group-object'
                        - 'posix-group-object'
                group-object-filter:
                    type: str
                group-object-search-base:
                    type: str
                group-search-base:
                    type: str
                member-attr:
                    type: str
                obtain-user-info:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                password:
                    -
                        type: str
                password-expiry-warning:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                password-renewal:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                port:
                    type: int
                retrieve-protection-profile:
                    type: str
                search-type:
                    -
                        type: str
                        choices:
                            - 'nested'
                            - 'recursive'
                secondary-server:
                    type: str
                secure:
                    type: str
                    choices:
                        - 'disable'
                        - 'starttls'
                        - 'ldaps'
                server:
                    type: str
                server-identity-check:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                source-ip:
                    type: str
                ssl-min-proto-version:
                    type: str
                    choices:
                        - 'default'
                        - 'TLSv1'
                        - 'TLSv1-1'
                        - 'TLSv1-2'
                        - 'SSLv3'
                tertiary-server:
                    type: str
                type:
                    type: str
                    choices:
                        - 'simple'
                        - 'anonymous'
                        - 'regular'
                user-info-exchange-server:
                    type: str
                username:
                    type: str
    schema_object1:
        methods: [delete]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the object will be returned.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'chksum - Return the check-sum value instead of attributes.'
                choices:
                    - 'object member'
                    - 'chksum'
                    - 'datasrc'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/USER/LDAP/{LDAP}/DYNAMIC_MAPPING/{DYNAMIC_MAPPING}
      fmgr_user_ldap_dynamicmapping_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            ldap: <value of string>
            dynamic_mapping: <value of string>
         params:
            -
               data:
                  _scope:
                    -
                        name: <value of string>
                        vdom: <value of string>
                  account-key-filter: <value of string>
                  account-key-name: <value of string>
                  account-key-processing: <value in [same, strip]>
                  ca-cert: <value of string>
                  cnid: <value of string>
                  dn: <value of string>
                  filter: <value of string>
                  group: <value of string>
                  group-filter: <value of string>
                  group-member-check: <value in [user-attr, group-object, posix-group-object]>
                  group-object-filter: <value of string>
                  group-object-search-base: <value of string>
                  group-search-base: <value of string>
                  member-attr: <value of string>
                  obtain-user-info: <value in [disable, enable]>
                  password:
                    - <value of string>
                  password-expiry-warning: <value in [disable, enable]>
                  password-renewal: <value in [disable, enable]>
                  port: <value of integer>
                  retrieve-protection-profile: <value of string>
                  search-type:
                    - <value in [nested, recursive]>
                  secondary-server: <value of string>
                  secure: <value in [disable, starttls, ldaps]>
                  server: <value of string>
                  server-identity-check: <value in [disable, enable]>
                  source-ip: <value of string>
                  ssl-min-proto-version: <value in [default, TLSv1, TLSv1-1, ...]>
                  tertiary-server: <value of string>
                  type: <value in [simple, anonymous, regular]>
                  user-info-exchange-server: <value of string>
                  username: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/USER/LDAP/{LDAP}/DYNAMIC_MAPPING/{DYNAMIC_MAPPING}
      fmgr_user_ldap_dynamicmapping_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            ldap: <value of string>
            dynamic_mapping: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[clone, delete, set, update]
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
            example: '/pm/config/adom/{adom}/obj/user/ldap/{ldap}/dynamic_mapping/{dynamic_mapping}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            _scope:
               type: array
               suboptions:
                  name:
                     type: str
                  vdom:
                     type: str
            account-key-filter:
               type: str
            account-key-name:
               type: str
            account-key-processing:
               type: str
            ca-cert:
               type: str
            cnid:
               type: str
            dn:
               type: str
            filter:
               type: str
            group:
               type: str
            group-filter:
               type: str
            group-member-check:
               type: str
            group-object-filter:
               type: str
            group-object-search-base:
               type: str
            group-search-base:
               type: str
            member-attr:
               type: str
            obtain-user-info:
               type: str
            password:
               type: array
               suboptions:
                  type: str
            password-expiry-warning:
               type: str
            password-renewal:
               type: str
            port:
               type: int
            retrieve-protection-profile:
               type: str
            search-type:
               type: array
               suboptions:
                  type: str
            secondary-server:
               type: str
            secure:
               type: str
            server:
               type: str
            server-identity-check:
               type: str
            source-ip:
               type: str
            ssl-min-proto-version:
               type: str
            tertiary-server:
               type: str
            type:
               type: str
            user-info-exchange-server:
               type: str
            username:
               type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/user/ldap/{ldap}/dynamic_mapping/{dynamic_mapping}'

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import FAIL_SOCKET_MSG
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import DEFAULT_RESULT_OBJ
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import FMGRCommon
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import FMGBaseException
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.fortimanager import FortiManagerHandler


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/user/ldap/{ldap}/dynamic_mapping/{dynamic_mapping}',
        '/pm/config/global/obj/user/ldap/{ldap}/dynamic_mapping/{dynamic_mapping}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'ldap',
            'type': 'string'
        },
        {
            'name': 'dynamic_mapping',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        '_scope': {
                            'type': 'array',
                            'items': {
                                'name': {
                                    'type': 'string'
                                },
                                'vdom': {
                                    'type': 'string'
                                }
                            }
                        },
                        'account-key-filter': {
                            'type': 'string'
                        },
                        'account-key-name': {
                            'type': 'string'
                        },
                        'account-key-processing': {
                            'type': 'string',
                            'enum': [
                                'same',
                                'strip'
                            ]
                        },
                        'ca-cert': {
                            'type': 'string'
                        },
                        'cnid': {
                            'type': 'string'
                        },
                        'dn': {
                            'type': 'string'
                        },
                        'filter': {
                            'type': 'string'
                        },
                        'group': {
                            'type': 'string'
                        },
                        'group-filter': {
                            'type': 'string'
                        },
                        'group-member-check': {
                            'type': 'string',
                            'enum': [
                                'user-attr',
                                'group-object',
                                'posix-group-object'
                            ]
                        },
                        'group-object-filter': {
                            'type': 'string'
                        },
                        'group-object-search-base': {
                            'type': 'string'
                        },
                        'group-search-base': {
                            'type': 'string'
                        },
                        'member-attr': {
                            'type': 'string'
                        },
                        'obtain-user-info': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'password': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'password-expiry-warning': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'password-renewal': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'port': {
                            'type': 'integer'
                        },
                        'retrieve-protection-profile': {
                            'type': 'string'
                        },
                        'search-type': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'nested',
                                    'recursive'
                                ]
                            }
                        },
                        'secondary-server': {
                            'type': 'string'
                        },
                        'secure': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'starttls',
                                'ldaps'
                            ]
                        },
                        'server': {
                            'type': 'string'
                        },
                        'server-identity-check': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'source-ip': {
                            'type': 'string'
                        },
                        'ssl-min-proto-version': {
                            'type': 'string',
                            'enum': [
                                'default',
                                'TLSv1',
                                'TLSv1-1',
                                'TLSv1-2',
                                'SSLv3'
                            ]
                        },
                        'tertiary-server': {
                            'type': 'string'
                        },
                        'type': {
                            'type': 'string',
                            'enum': [
                                'simple',
                                'anonymous',
                                'regular'
                            ]
                        },
                        'user-info-exchange-server': {
                            'type': 'string'
                        },
                        'username': {
                            'type': 'string'
                        }
                    },
                    'api_tag': 0
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object1': [
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object2': [
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'object member',
                            'chksum',
                            'datasrc'
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
            'clone': 'object0',
            'delete': 'object1',
            'get': 'object2',
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
                'clone',
                'delete',
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
    module = AnsibleModule(argument_spec=module_arg_spec,
                           supports_check_mode=False)
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
        fmgr.govern_response(module=module, results=response,
                             msg='Operation Finished',
                             ansible_facts=fmgr.construct_ansible_facts(response, module.params, module.params))
    except Exception as e:
        raise FMGBaseException(e)

    module.exit_json(meta=response[1])


if __name__ == '__main__':
    main()
