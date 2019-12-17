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
module: fmgr_cli_fmupdate_service
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis:
    - /cli/global/fmupdate/service
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
        methods: [get]
        description: 'Enable/disable services provided by the built-in FortiGuard.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Enable/disable services provided by the built-in FortiGuard.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                avips:
                    type: str
                    default: enable
                    description:
                     - 'Enable/disable the built-in FortiGuard to provide FortiGuard antivirus and IPS updates (default = enable).'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - disable
                        - enable
                query-antispam:
                    type: str
                    default: disable
                    description:
                     - 'Enable/disable antispam service (default = disable).'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - disable
                        - enable
                query-antivirus:
                    type: str
                    default: disable
                    description:
                     - 'Enable/disable antivirus query service (default = disable).'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - disable
                        - enable
                query-filequery:
                    type: str
                    default: disable
                    description:
                     - 'Enable/disable file query service (default = disable).'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - disable
                        - enable
                query-geoip:
                    type: str
                    default: enable
                    description:
                     - 'Enable/disable geoip service (default = enable).'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - disable
                        - enable
                query-outbreak-prevention:
                    type: str
                    default: disable
                    description:
                     - 'Enable/disable  outbreak prevention query service (default = disable).'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - disable
                        - enable
                query-webfilter:
                    type: str
                    default: disable
                    description:
                     - 'Enable/disable Web Filter service (default = disable).'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - disable
                        - enable
                webfilter-https-traversal:
                    type: str
                    default: disable
                    description:
                     - 'Enable/disable Web Filter HTTPS traversal (default = disable).'
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
    - name: send request to /cli/fmupdate/service
      fmgr_cli_fmupdate_service:
         method: <value in [set, update]>
         params:
            - 
               data: 
                  avips: <value in [disable, enable] default: enable>
                  query-antispam: <value in [disable, enable] default: disable>
                  query-antivirus: <value in [disable, enable] default: disable>
                  query-filequery: <value in [disable, enable] default: disable>
                  query-geoip: <value in [disable, enable] default: enable>
                  query-outbreak-prevention: <value in [disable, enable] default: disable>
                  query-webfilter: <value in [disable, enable] default: disable>
                  webfilter-https-traversal: <value in [disable, enable] default: disable>

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
            avips:
               type: str
               description: |
                  'Enable/disable the built-in FortiGuard to provide FortiGuard antivirus and IPS updates (default = enable).'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            query-antispam:
               type: str
               description: |
                  'Enable/disable antispam service (default = disable).'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: disable
            query-antivirus:
               type: str
               description: |
                  'Enable/disable antivirus query service (default = disable).'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: disable
            query-filequery:
               type: str
               description: |
                  'Enable/disable file query service (default = disable).'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: disable
            query-geoip:
               type: str
               description: |
                  'Enable/disable geoip service (default = enable).'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            query-outbreak-prevention:
               type: str
               description: |
                  'Enable/disable  outbreak prevention query service (default = disable).'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: disable
            query-webfilter:
               type: str
               description: |
                  'Enable/disable Web Filter service (default = disable).'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: disable
            webfilter-https-traversal:
               type: str
               description: |
                  'Enable/disable Web Filter HTTPS traversal (default = disable).'
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
            example: /cli/global/fmupdate/service
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
            example: /cli/global/fmupdate/service

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
        '/cli/global/fmupdate/service'
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
                        'avips': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'query-antispam': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'query-antivirus': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'query-filequery': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'query-geoip': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'query-outbreak-prevention': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'query-webfilter': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'webfilter-https-traversal': {
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