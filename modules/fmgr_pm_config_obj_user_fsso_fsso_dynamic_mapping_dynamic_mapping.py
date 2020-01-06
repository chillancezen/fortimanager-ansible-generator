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
module: fmgr_pm_config_obj_user_fsso_fsso_dynamic_mapping_dynamic_mapping
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/user/fsso/{fsso}/dynamic_mapping/{dynamic_mapping}
    - /pm/config/global/obj/user/fsso/{fsso}/dynamic_mapping/{dynamic_mapping}
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
            fsso:
                type: str
            dynamic_mapping:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
            data:
                _gui_meta:
                    type: str
                _scope:
                    -
                        name:
                            type: str
                        vdom:
                            type: str
                ldap-server:
                    type: str
                password:
                    -
                        type: str
                password2:
                    -
                        type: str
                password3:
                    -
                        type: str
                password4:
                    -
                        type: str
                password5:
                    -
                        type: str
                port:
                    type: int
                port2:
                    type: int
                port3:
                    type: int
                port4:
                    type: int
                port5:
                    type: int
                server:
                    type: str
                server2:
                    type: str
                server3:
                    type: str
                server4:
                    type: str
                server5:
                    type: str
                source-ip:
                    type: str
                source-ip6:
                    type: str
                ssl:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ssl-trusted-cert:
                    type: str
                type:
                    type: str
                    choices:
                        - 'default'
                        - 'fortiems'
                        - 'fortinac'
                user-info-server:
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
    - name: send request to /pm/config/obj/user/fsso/{fsso}/dynamic_mapping/{dynamic_mapping}
      fmgr_pm_config_obj_user_fsso_fsso_dynamic_mapping_dynamic_mapping:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            fsso: <value of string>
            dynamic_mapping: <value of string>
         params:
            - 
               data: 
                  _gui_meta: <value of string>
                  _scope: 
                   - 
                        name: <value of string>
                        vdom: <value of string>
                  ldap-server: <value of string>
                  password: 
                   - <value of string>
                  password2: 
                   - <value of string>
                  password3: 
                   - <value of string>
                  password4: 
                   - <value of string>
                  password5: 
                   - <value of string>
                  port: <value of integer>
                  port2: <value of integer>
                  port3: <value of integer>
                  port4: <value of integer>
                  port5: <value of integer>
                  server: <value of string>
                  server2: <value of string>
                  server3: <value of string>
                  server4: <value of string>
                  server5: <value of string>
                  source-ip: <value of string>
                  source-ip6: <value of string>
                  ssl: <value in [disable, enable]>
                  ssl-trusted-cert: <value of string>
                  type: <value in [default, fortiems, fortinac]>
                  user-info-server: <value of string>
    - name: send request to /pm/config/obj/user/fsso/{fsso}/dynamic_mapping/{dynamic_mapping}
      fmgr_pm_config_obj_user_fsso_fsso_dynamic_mapping_dynamic_mapping:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            fsso: <value of string>
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
            example: /pm/config/adom/{adom}/obj/user/fsso/{fsso}/dynamic_mapping/{dynamic_mapping}
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            _gui_meta:
               type: str
            _scope:
               type: array
               suboptions:
                  name:
                     type: str
                  vdom:
                     type: str
            ldap-server:
               type: str
            password:
               type: array
               suboptions:
                  type: str
            password2:
               type: array
               suboptions:
                  type: str
            password3:
               type: array
               suboptions:
                  type: str
            password4:
               type: array
               suboptions:
                  type: str
            password5:
               type: array
               suboptions:
                  type: str
            port:
               type: int
            port2:
               type: int
            port3:
               type: int
            port4:
               type: int
            port5:
               type: int
            server:
               type: str
            server2:
               type: str
            server3:
               type: str
            server4:
               type: str
            server5:
               type: str
            source-ip:
               type: str
            source-ip6:
               type: str
            ssl:
               type: str
            ssl-trusted-cert:
               type: str
            type:
               type: str
            user-info-server:
               type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/obj/user/fsso/{fsso}/dynamic_mapping/{dynamic_mapping}

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
        '/pm/config/adom/{adom}/obj/user/fsso/{fsso}/dynamic_mapping/{dynamic_mapping}',
        '/pm/config/global/obj/user/fsso/{fsso}/dynamic_mapping/{dynamic_mapping}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'fsso',
            'type': 'string'
        },
        {
            'name': 'dynamic_mapping',
            'type': 'string'
        }
    ]

    body_schema =  {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        '_gui_meta': {
                            'type': 'string'
                        },
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
                        'ldap-server': {
                            'type': 'string'
                        },
                        'password': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'password2': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'password3': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'password4': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'password5': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'port': {
                            'type': 'integer'
                        },
                        'port2': {
                            'type': 'integer'
                        },
                        'port3': {
                            'type': 'integer'
                        },
                        'port4': {
                            'type': 'integer'
                        },
                        'port5': {
                            'type': 'integer'
                        },
                        'server': {
                            'type': 'string'
                        },
                        'server2': {
                            'type': 'string'
                        },
                        'server3': {
                            'type': 'string'
                        },
                        'server4': {
                            'type': 'string'
                        },
                        'server5': {
                            'type': 'string'
                        },
                        'source-ip': {
                            'type': 'string'
                        },
                        'source-ip6': {
                            'type': 'string'
                        },
                        'ssl': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ssl-trusted-cert': {
                            'type': 'string'
                        },
                        'type': {
                            'type': 'string',
                            'enum': [
                                'default',
                                'fortiems',
                                'fortinac'
                            ]
                        },
                        'user-info-server': {
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