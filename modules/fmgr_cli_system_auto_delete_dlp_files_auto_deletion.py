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
module: fmgr_cli_system_auto_delete_dlp_files_auto_deletion
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /cli/global/system/auto-delete/dlp-files-auto-deletion
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
        description: 'Automatic deletion policy for DLP archives.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Automatic deletion policy for DLP archives.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                retention:
                    type: str
                    default: 'days'
                    description:
                     - 'Automatic deletion in days, weeks, or months.'
                     - 'days - Auto-delete data older than <value> days.'
                     - 'weeks - Auto-delete data older than <value> weeks.'
                     - 'months - Auto-delete data older than <value> months.'
                    choices:
                        - 'days'
                        - 'weeks'
                        - 'months'
                runat:
                    type: int
                    default: 0
                    description: 'Automatic deletion run at (0 - 23) oclock.'
                status:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable automatic deletion.'
                     - 'disable - Disable automatic deletion.'
                     - 'enable - Enable automatic deletion.'
                    choices:
                        - 'disable'
                        - 'enable'
                value:
                    type: int
                    default: 0
                    description: 'Automatic deletion in x days, weeks, or months.'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /CLI/SYSTEM/AUTO-DELETE/DLP-FILES-AUTO-DELETION
      fmgr_cli_system_auto_delete_dlp_files_auto_deletion:
         method: <value in [set, update]>
         params:
            -
               data:
                  retention: <value in [days, weeks, months] default: 'days'>
                  runat: <value of integer default: 0>
                  status: <value in [disable, enable] default: 'disable'>
                  value: <value of integer default: 0>

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
            retention:
               type: str
               description: |
                  'Automatic deletion in days, weeks, or months.'
                  'days - Auto-delete data older than <value> days.'
                  'weeks - Auto-delete data older than <value> weeks.'
                  'months - Auto-delete data older than <value> months.'
               example: 'days'
            runat:
               type: int
               description: 'Automatic deletion run at (0 - 23) oclock.'
               example: 0
            status:
               type: str
               description: |
                  'Enable/disable automatic deletion.'
                  'disable - Disable automatic deletion.'
                  'enable - Enable automatic deletion.'
               example: 'disable'
            value:
               type: int
               description: 'Automatic deletion in x days, weeks, or months.'
               example: 0
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/cli/global/system/auto-delete/dlp-files-auto-deletion'
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
            example: '/cli/global/system/auto-delete/dlp-files-auto-deletion'

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
        '/cli/global/system/auto-delete/dlp-files-auto-deletion'
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
                        'retention': {
                            'type': 'string',
                            'enum': [
                                'days',
                                'weeks',
                                'months'
                            ]
                        },
                        'runat': {
                            'type': 'integer',
                            'default': 0,
                            'example': 0
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'value': {
                            'type': 'integer',
                            'default': 0,
                            'example': 0
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

    module.exit_json(**response[1])


if __name__ == '__main__':
    main()
