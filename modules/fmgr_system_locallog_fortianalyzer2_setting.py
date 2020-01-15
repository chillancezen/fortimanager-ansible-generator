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
module: fmgr_system_locallog_fortianalyzer2_setting
short_description: Settings for locallog to fortianalyzer.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /cli/global/system/locallog/fortianalyzer2/setting
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
        description: 'Settings for locallog to fortianalyzer.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Settings for locallog to fortianalyzer.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                reliable:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable reliable realtime logging.'
                     - 'disable - Disable reliable realtime logging.'
                     - 'enable - Enable reliable realtime logging.'
                    choices:
                        - 'disable'
                        - 'enable'
                secure-connection:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable connection secured by TLS/SSL.'
                     - 'disable - Disable SSL connection.'
                     - 'enable - Enable SSL connection.'
                    choices:
                        - 'disable'
                        - 'enable'
                server-ip:
                    type: str
                    default: '0.0.0.0'
                    description: 'Remote FortiAnalyzer server IP address.'
                severity:
                    type: str
                    default: 'notification'
                    description:
                     - 'Least severity level to log.'
                     - 'emergency - Emergency level.'
                     - 'alert - Alert level.'
                     - 'critical - Critical level.'
                     - 'error - Error level.'
                     - 'warning - Warning level.'
                     - 'notification - Notification level.'
                     - 'information - Information level.'
                     - 'debug - Debug level.'
                    choices:
                        - 'emergency'
                        - 'alert'
                        - 'critical'
                        - 'error'
                        - 'warning'
                        - 'notification'
                        - 'information'
                        - 'debug'
                status:
                    type: str
                    default: 'disable'
                    description:
                     - 'Log to FortiAnalyzer status.'
                     - 'disable - Log to FortiAnalyzer disabled.'
                     - 'realtime - Log to FortiAnalyzer in realtime.'
                     - 'upload - Log to FortiAnalyzer at schedule time.'
                    choices:
                        - 'disable'
                        - 'realtime'
                        - 'upload'
                upload-time:
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

    - name: REQUESTING /CLI/SYSTEM/LOCALLOG/FORTIANALYZER2/SETTING
      fmgr_system_locallog_fortianalyzer2_setting:
         method: <value in [set, update]>
         params:
            -
               data:
                  reliable: <value in [disable, enable] default: 'disable'>
                  secure-connection: <value in [disable, enable] default: 'disable'>
                  server-ip: <value of string default: '0.0.0.0'>
                  severity: <value in [emergency, alert, critical, ...] default: 'notification'>
                  status: <value in [disable, realtime, upload] default: 'disable'>
                  upload-time:
                    - <value of string>

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
            reliable:
               type: str
               description: |
                  'Enable/disable reliable realtime logging.'
                  'disable - Disable reliable realtime logging.'
                  'enable - Enable reliable realtime logging.'
               example: 'disable'
            secure-connection:
               type: str
               description: |
                  'Enable/disable connection secured by TLS/SSL.'
                  'disable - Disable SSL connection.'
                  'enable - Enable SSL connection.'
               example: 'disable'
            server-ip:
               type: str
               description: 'Remote FortiAnalyzer server IP address.'
               example: '0.0.0.0'
            severity:
               type: str
               description: |
                  'Least severity level to log.'
                  'emergency - Emergency level.'
                  'alert - Alert level.'
                  'critical - Critical level.'
                  'error - Error level.'
                  'warning - Warning level.'
                  'notification - Notification level.'
                  'information - Information level.'
                  'debug - Debug level.'
               example: 'notification'
            status:
               type: str
               description: |
                  'Log to FortiAnalyzer status.'
                  'disable - Log to FortiAnalyzer disabled.'
                  'realtime - Log to FortiAnalyzer in realtime.'
                  'upload - Log to FortiAnalyzer at schedule time.'
               example: 'disable'
            upload-time:
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
            example: '/cli/global/system/locallog/fortianalyzer2/setting'
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
            example: '/cli/global/system/locallog/fortianalyzer2/setting'

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
        '/cli/global/system/locallog/fortianalyzer2/setting'
    ]

    url_schema = [
    ]

    body_schema = {
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
                        'reliable': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'secure-connection': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'server-ip': {
                            'type': 'string'
                        },
                        'severity': {
                            'type': 'string',
                            'enum': [
                                'emergency',
                                'alert',
                                'critical',
                                'error',
                                'warning',
                                'notification',
                                'information',
                                'debug'
                            ]
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'realtime',
                                'upload'
                            ]
                        },
                        'upload-time': {
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
