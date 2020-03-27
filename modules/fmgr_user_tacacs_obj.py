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
module: fmgr_user_tacacs_obj
short_description: Configure TACACS+ server entries.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/user/tacacs+/{tacacs+}
    - /pm/config/global/obj/user/tacacs+/{tacacs+}
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
            tacacs+:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Configure TACACS+ server entries.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                authen-type:
                    type: str
                    description: 'Allowed authentication protocols/methods.'
                    choices:
                        - 'auto'
                        - 'ascii'
                        - 'pap'
                        - 'chap'
                        - 'mschap'
                authorization:
                    type: str
                    description: 'Enable/disable TACACS+ authorization.'
                    choices:
                        - 'disable'
                        - 'enable'
                dynamic_mapping:
                    -
                        _scope:
                            -
                                name:
                                    type: str
                                vdom:
                                    type: str
                        authen-type:
                            type: str
                            choices:
                                - 'auto'
                                - 'ascii'
                                - 'pap'
                                - 'chap'
                                - 'mschap'
                        authorization:
                            type: str
                            choices:
                                - 'disable'
                                - 'enable'
                        key:
                            -
                                type: str
                        port:
                            type: int
                        secondary-key:
                            -
                                type: str
                        secondary-server:
                            type: str
                        server:
                            type: str
                        source-ip:
                            type: str
                        tertiary-key:
                            -
                                type: str
                        tertiary-server:
                            type: str
                key:
                    -
                        type: str
                name:
                    type: str
                    description: 'TACACS+ server entry name.'
                port:
                    type: int
                    description: 'Port number of the TACACS+ server.'
                secondary-key:
                    -
                        type: str
                secondary-server:
                    type: str
                    description: 'Secondary TACACS+ server CN domain name or IP address.'
                server:
                    type: str
                    description: 'Primary TACACS+ server CN domain name or IP address.'
                source-ip:
                    type: str
                    description: 'source IP for communications to TACACS+ server.'
                tertiary-key:
                    -
                        type: str
                tertiary-server:
                    type: str
                    description: 'Tertiary TACACS+ server CN domain name or IP address.'
    schema_object1:
        methods: [delete]
        description: 'Configure TACACS+ server entries.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Configure TACACS+ server entries.'
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
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/USER/TACACS+/{TACACS+}
      fmgr_user_tacacs_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            tacacs+: <value of string>
         params:
            -
               data:
                  authen-type: <value in [auto, ascii, pap, ...]>
                  authorization: <value in [disable, enable]>
                  dynamic_mapping:
                    -
                        _scope:
                          -
                              name: <value of string>
                              vdom: <value of string>
                        authen-type: <value in [auto, ascii, pap, ...]>
                        authorization: <value in [disable, enable]>
                        key:
                          - <value of string>
                        port: <value of integer>
                        secondary-key:
                          - <value of string>
                        secondary-server: <value of string>
                        server: <value of string>
                        source-ip: <value of string>
                        tertiary-key:
                          - <value of string>
                        tertiary-server: <value of string>
                  key:
                    - <value of string>
                  name: <value of string>
                  port: <value of integer>
                  secondary-key:
                    - <value of string>
                  secondary-server: <value of string>
                  server: <value of string>
                  source-ip: <value of string>
                  tertiary-key:
                    - <value of string>
                  tertiary-server: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/USER/TACACS+/{TACACS+}
      fmgr_user_tacacs_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            tacacs+: <value of string>
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
            example: '/pm/config/adom/{adom}/obj/user/tacacs+/{tacacs+}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            authen-type:
               type: str
               description: 'Allowed authentication protocols/methods.'
            authorization:
               type: str
               description: 'Enable/disable TACACS+ authorization.'
            dynamic_mapping:
               type: array
               suboptions:
                  _scope:
                     type: array
                     suboptions:
                        name:
                           type: str
                        vdom:
                           type: str
                  authen-type:
                     type: str
                  authorization:
                     type: str
                  key:
                     type: array
                     suboptions:
                        type: str
                  port:
                     type: int
                  secondary-key:
                     type: array
                     suboptions:
                        type: str
                  secondary-server:
                     type: str
                  server:
                     type: str
                  source-ip:
                     type: str
                  tertiary-key:
                     type: array
                     suboptions:
                        type: str
                  tertiary-server:
                     type: str
            key:
               type: array
               suboptions:
                  type: str
            name:
               type: str
               description: 'TACACS+ server entry name.'
            port:
               type: int
               description: 'Port number of the TACACS+ server.'
            secondary-key:
               type: array
               suboptions:
                  type: str
            secondary-server:
               type: str
               description: 'Secondary TACACS+ server CN domain name or IP address.'
            server:
               type: str
               description: 'Primary TACACS+ server CN domain name or IP address.'
            source-ip:
               type: str
               description: 'source IP for communications to TACACS+ server.'
            tertiary-key:
               type: array
               suboptions:
                  type: str
            tertiary-server:
               type: str
               description: 'Tertiary TACACS+ server CN domain name or IP address.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/user/tacacs+/{tacacs+}'

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FAIL_SOCKET_MSG
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import DEFAULT_RESULT_OBJ
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FMGRCommon
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FMGBaseException
from ansible_collections.fortinet.fortimanager.plugins.module_utils.fortimanager import FortiManagerHandler


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/user/tacacs+/{tacacs+}',
        '/pm/config/global/obj/user/tacacs+/{tacacs+}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'tacacs+',
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
                        'authen-type': {
                            'type': 'string',
                            'enum': [
                                'auto',
                                'ascii',
                                'pap',
                                'chap',
                                'mschap'
                            ]
                        },
                        'authorization': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dynamic_mapping': {
                            'type': 'array',
                            'items': {
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
                                'authen-type': {
                                    'type': 'string',
                                    'enum': [
                                        'auto',
                                        'ascii',
                                        'pap',
                                        'chap',
                                        'mschap'
                                    ]
                                },
                                'authorization': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'key': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                },
                                'port': {
                                    'type': 'integer'
                                },
                                'secondary-key': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                },
                                'secondary-server': {
                                    'type': 'string'
                                },
                                'server': {
                                    'type': 'string'
                                },
                                'source-ip': {
                                    'type': 'string'
                                },
                                'tertiary-key': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                },
                                'tertiary-server': {
                                    'type': 'string'
                                }
                            }
                        },
                        'key': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'name': {
                            'type': 'string'
                        },
                        'port': {
                            'type': 'integer'
                        },
                        'secondary-key': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'secondary-server': {
                            'type': 'string'
                        },
                        'server': {
                            'type': 'string'
                        },
                        'source-ip': {
                            'type': 'string'
                        },
                        'tertiary-key': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'tertiary-server': {
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
