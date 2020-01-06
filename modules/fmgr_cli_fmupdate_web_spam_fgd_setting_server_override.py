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
module: fmgr_cli_fmupdate_web_spam_fgd_setting_server_override
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /cli/global/fmupdate/web-spam/fgd-setting/server-override
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
    schema_object0:
        methods: [get]
        description: 'Server override configure.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Server override configure.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                servlist:
                    -
                        id:
                            type: int
                            default: 0
                            description: 'Override server ID (1 - 10).'
                        ip:
                            type: str
                            default: 0.0.0.0
                            description: 'IPv4 address of the override server.'
                        ip6:
                            type: str
                            default: ::
                            description: 'IPv6 address of the override server.'
                        port:
                            type: int
                            default: 443
                            description: 'Port number to use when contacting FortiGuard (1 - 65535, default = 443).'
                        service-type:
                            -
                                type: str
                                choices:
                                    - fgd
                                    - fgc
                                    - fsa
                status:
                    type: str
                    default: disable
                    description:
                     - 'Override status.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - disable
                        - enable

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /cli/fmupdate/web-spam/fgd-setting/server-override
      fmgr_cli_fmupdate_web_spam_fgd_setting_server_override:
         method: <value in [set, update]>
         params:
            - 
               data: 
                  servlist: 
                   - 
                        id: <value of integer default: 0>
                        ip: <value of string default: 0.0.0.0>
                        ip6: <value of string default: ::>
                        port: <value of integer default: 443>
                        service-type: 
                         - <value in [fgd, fgc, fsa]>
                  status: <value in [disable, enable] default: disable>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            servlist:
               type: array
               suboptions:
                  id:
                     type: int
                     description: 'Override server ID (1 - 10).'
                     example: 0
                  ip:
                     type: str
                     description: 'IPv4 address of the override server.'
                     example: 0.0.0.0
                  ip6:
                     type: str
                     description: 'IPv6 address of the override server.'
                     example: ::
                  port:
                     type: int
                     description: 'Port number to use when contacting FortiGuard (1 - 65535, default = 443).'
                     example: 443
                  service-type:
                     type: array
                     suboptions:
                        type: str
            status:
               type: str
               description: |
                  'Override status.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: disable
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /cli/global/fmupdate/web-spam/fgd-setting/server-override
return_of_api_category_0:
   description: items returned for method:[set, update]
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
            example: /cli/global/fmupdate/web-spam/fgd-setting/server-override

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
        '/cli/global/fmupdate/web-spam/fgd-setting/server-override'
    ]

    url_schema = [
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
                        'servlist': {
                            'type': 'array',
                            'items': {
                                'id': {
                                    'type': 'integer',
                                    'default': 0,
                                    'example': 0
                                },
                                'ip': {
                                    'type': 'string',
                                    'default': '0.0.0.0'
                                },
                                'ip6': {
                                    'type': 'string',
                                    'default': '::'
                                },
                                'port': {
                                    'type': 'integer',
                                    'default': 443,
                                    'example': 443
                                },
                                'service-type': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string',
                                        'enum': [
                                            'fgd',
                                            'fgc',
                                            'fsa'
                                        ]
                                    }
                                }
                            }
                        },
                        'status': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
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