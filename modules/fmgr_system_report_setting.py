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
module: fmgr_system_report_setting
short_description: Report settings.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /cli/global/system/report/setting
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
    loose_validation:
        description: Do parameter validation in a loose way
        required: False
        type: bool
        default: false
    workspace_locking_adom:
        description: the adom to lock in case FortiManager running in workspace mode
        required: False
        type: string
        choices:
          - global
          - custom adom
    workspace_locking_timeout:
        description: teh maximum time in seconds to wait for other user to release the workspace lock
        required: False
        type: integer
        default: 300
    schema_object0:
        methods: [get]
        description: 'Report settings.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Report settings.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                aggregate-report:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable including a group report along with the per-device reports.'
                     - 'disable - Exclude a group report along with the per-device reports.'
                     - 'enable - Include a group report along with the per-device reports.'
                    choices:
                        - 'disable'
                        - 'enable'
                hcache-lossless:
                    type: str
                    default: 'disable'
                    description:
                     - 'Usableness of ready-with-loss hcaches.'
                     - 'disable - Use ready-with-loss hcaches.'
                     - 'enable - Do not use ready-with-loss hcaches.'
                    choices:
                        - 'disable'
                        - 'enable'
                ldap-cache-timeout:
                    type: int
                    default: 60
                    description: 'LDAP cache timeout in minutes, default 60, 0 means not use cache.'
                max-table-rows:
                    type: int
                    default: 10000
                    description: 'Maximum number of rows can be generated in a single table.'
                report-priority:
                    type: str
                    default: 'auto'
                    description:
                     - 'Priority of sql report.'
                     - 'high - High'
                     - 'low - Low'
                     - 'auto - Auto'
                    choices:
                        - 'high'
                        - 'low'
                        - 'auto'
                template-auto-install:
                    type: str
                    default: 'default'
                    description:
                     - 'The language used for new ADOMs (default = default).'
                     - 'default - Default.'
                     - 'english - English.'
                    choices:
                        - 'default'
                        - 'english'
                week-start:
                    type: str
                    default: 'sun'
                    description:
                     - 'Day of the week on which the week starts.'
                     - 'sun - Sunday.'
                     - 'mon - Monday.'
                    choices:
                        - 'sun'
                        - 'mon'

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

    - name: REQUESTING /CLI/SYSTEM/REPORT/SETTING
      fmgr_system_report_setting:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [set, update]>
         params:
            -
               data:
                  aggregate-report: <value in [disable, enable] default: 'disable'>
                  hcache-lossless: <value in [disable, enable] default: 'disable'>
                  ldap-cache-timeout: <value of integer default: 60>
                  max-table-rows: <value of integer default: 10000>
                  report-priority: <value in [high, low, auto] default: 'auto'>
                  template-auto-install: <value in [default, english] default: 'default'>
                  week-start: <value in [sun, mon] default: 'sun'>

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
            aggregate-report:
               type: str
               description: |
                  'Enable/disable including a group report along with the per-device reports.'
                  'disable - Exclude a group report along with the per-device reports.'
                  'enable - Include a group report along with the per-device reports.'
               example: 'disable'
            hcache-lossless:
               type: str
               description: |
                  'Usableness of ready-with-loss hcaches.'
                  'disable - Use ready-with-loss hcaches.'
                  'enable - Do not use ready-with-loss hcaches.'
               example: 'disable'
            ldap-cache-timeout:
               type: int
               description: 'LDAP cache timeout in minutes, default 60, 0 means not use cache.'
               example: 60
            max-table-rows:
               type: int
               description: 'Maximum number of rows can be generated in a single table.'
               example: 10000
            report-priority:
               type: str
               description: |
                  'Priority of sql report.'
                  'high - High'
                  'low - Low'
                  'auto - Auto'
               example: 'auto'
            template-auto-install:
               type: str
               description: |
                  'The language used for new ADOMs (default = default).'
                  'default - Default.'
                  'english - English.'
               example: 'default'
            week-start:
               type: str
               description: |
                  'Day of the week on which the week starts.'
                  'sun - Sunday.'
                  'mon - Monday.'
               example: 'sun'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/cli/global/system/report/setting'
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
            example: '/cli/global/system/report/setting'

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
        '/cli/global/system/report/setting'
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
                        'aggregate-report': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'hcache-lossless': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ldap-cache-timeout': {
                            'type': 'integer',
                            'default': 60,
                            'example': 60
                        },
                        'max-table-rows': {
                            'type': 'integer',
                            'default': 10000,
                            'example': 10000
                        },
                        'report-priority': {
                            'type': 'string',
                            'enum': [
                                'high',
                                'low',
                                'auto'
                            ]
                        },
                        'template-auto-install': {
                            'type': 'string',
                            'enum': [
                                'default',
                                'english'
                            ]
                        },
                        'week-start': {
                            'type': 'string',
                            'enum': [
                                'sun',
                                'mon'
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
        'loose_validation': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'workspace_locking_adom': {
            'type': 'str',
            'required': False
        },
        'workspace_locking_timeout': {
            'type': 'int',
            'required': False,
            'default': 300
        },
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
    loose_validation = module.params['loose_validation']

    fmgr = None
    payload = None
    response = DEFAULT_RESULT_OBJ

    if module._socket_path:
        connection = Connection(module._socket_path)
        tools = FMGRCommon()
        if loose_validation == False:
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
