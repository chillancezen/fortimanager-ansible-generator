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
module: fmgr_cli_system_certificate_local_local
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ delete get set update ] the following apis.
    - /cli/global/system/certificate/local/{local}
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
            local:
                type: str
    schema_object0:
        methods: [delete, get]
        description: 'Local keys and certificates.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Local keys and certificates.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                certificate:
                    -
                        type: str
                comment:
                    type: str
                    description: 'Local certificate comment.'
                csr:
                    -
                        type: str
                name:
                    type: str
                    description: 'Name of local certificate.'
                password:
                    -
                        type: str
                        default: ENC MTU2NTY2MTI5MDA3MDkxNBB2U7GXAKMJnXNp1HA5qlMS8x60LYYPH59UftMARK2yBZSIyOKVdX6+LwsW+HCuCyxLGSjNDtDBuxlRE0O7Wq9sKZOknxG2S1rADC1fQWbul8eYa0wrzplnDD/u8OlHAf4q/+Ubo19o8BlFW8Pg8Fi+WhVP
                private-key:
                    -
                        type: str

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /cli/system/certificate/local/{local}
      fmgr_cli_system_certificate_local_local:
         method: <value in [set, update]>
         url_params:
            local: <value of string>
         params:
            - 
               data: 
                  certificate: 
                   - <value of string>
                  comment: <value of string>
                  csr: 
                   - <value of string>
                  name: <value of string>
                  password: 
                   - <value of string default: ENC MTU2NTY2MTI5MDA3MDkxNBB2U7GXAKMJnXNp1HA5qlMS8x60LYYPH59UftMARK2yBZSIyOKVdX6+LwsW+HCuCyxLGSjNDtDBuxlRE0O7Wq9sKZOknxG2S1rADC1fQWbul8eYa0wrzplnDD/u8OlHAf4q/+Ubo19o8BlFW8Pg8Fi+WhVP>
                  private-key: 
                   - <value of string>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[delete, set, update]
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
            example: /cli/global/system/certificate/local/{local}
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            certificate:
               type: array
               suboptions:
                  type: str
            comment:
               type: str
               description: 'Local certificate comment.'
            csr:
               type: array
               suboptions:
                  type: str
            name:
               type: str
               description: 'Name of local certificate.'
            password:
               type: array
               suboptions:
                  type: str
                  example: ENC MTU2NTY2MTI5MDA3MDkxNBB2U7GXAKMJnXNp1HA5qlMS8x60LYYPH59UftMARK2yBZSIyOKVdX6+LwsW+HCuCyxLGSjNDtDBuxlRE0O7Wq9sKZOknxG2S1rADC1fQWbul8eYa0wrzplnDD/u8OlHAf4q/+Ubo19o8BlFW8Pg8Fi+WhVP
            private-key:
               type: array
               suboptions:
                  type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /cli/global/system/certificate/local/{local}

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
        '/cli/global/system/certificate/local/{local}'
    ]

    url_schema = [
        {
            'name': 'local',
            'type': 'string'
        }
    ]

    body_schema =  {
        'schema_objects': {
            'object0': [
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object1': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'certificate': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'comment': {
                            'type': 'string'
                        },
                        'csr': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'name': {
                            'type': 'string'
                        },
                        'password': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'default': 'ENC MTU2NTY2MTI5MDA3MDkxNBB2U7GXAKMJnXNp1HA5qlMS8x60LYYPH59UftMARK2yBZSIyOKVdX6+LwsW+HCuCyxLGSjNDtDBuxlRE0O7Wq9sKZOknxG2S1rADC1fQWbul8eYa0wrzplnDD/u8OlHAf4q/+Ubo19o8BlFW8Pg8Fi+WhVP'
                            }
                        },
                        'private-key': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        }
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
            'delete': 'object0',
            'get': 'object0',
            'set': 'object1',
            'update': 'object1'
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