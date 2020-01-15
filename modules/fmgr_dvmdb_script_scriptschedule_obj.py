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
module: fmgr_dvmdb_script_scriptschedule_obj
short_description: Script schedule table.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ delete get set update ] the following apis.
    - /dvmdb/adom/{adom}/script/{script}/script_schedule/{script_schedule}
    - /dvmdb/global/script/{script}/script_schedule/{script_schedule}
    - /dvmdb/script/{script}/script_schedule/{script_schedule}
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
            script:
                type: str
            script_schedule:
                type: str
    schema_object0:
        methods: [delete]
        description: 'Script schedule table.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [get]
        description: 'Script schedule table.'
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
    schema_object2:
        methods: [set, update]
        description: 'Script schedule table.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                datetime:
                    type: str
                    description:
                     - 'Indicates the date and time of the schedule. It should follow the following format for each scheduling type:'
                     - 'onetime: "YYYY-MM-DD hh:mm:ss"'
                     - 'daily: "hh:mm"'
                     - 'weekly: "hh:mm"'
                     - 'monthly: "DD hh:mm"'
                day_of_week:
                    type: str
                    default: 'sun'
                    choices:
                        - 'unknown'
                        - 'sun'
                        - 'mon'
                        - 'tue'
                        - 'wed'
                        - 'thu'
                        - 'fri'
                        - 'sat'
                device:
                    type: int
                    description: 'Name or id of an existing device in the database.'
                name:
                    type: str
                run_on_db:
                    type: str
                    default: 'disable'
                    description: 'Indicates if the scheduled script should be executed on device database. It should always be disable for tcl scripts.'
                    choices:
                        - 'disable'
                        - 'enable'
                type:
                    type: str
                    choices:
                        - 'auto'
                        - 'onetime'
                        - 'daily'
                        - 'weekly'
                        - 'monthly'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /DVMDB/SCRIPT/{SCRIPT}/SCRIPT_SCHEDULE/{SCRIPT_SCHEDULE}
      fmgr_dvmdb_script_scriptschedule_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            script: <value of string>
            script_schedule: <value of string>
         params:
            -
               option: <value in [object member, chksum]>

    - name: REQUESTING /DVMDB/SCRIPT/{SCRIPT}/SCRIPT_SCHEDULE/{SCRIPT_SCHEDULE}
      fmgr_dvmdb_script_scriptschedule_obj:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            script: <value of string>
            script_schedule: <value of string>
         params:
            -
               data:
                  datetime: <value of string>
                  day_of_week: <value in [unknown, sun, mon, ...] default: 'sun'>
                  device: <value of integer>
                  name: <value of string>
                  run_on_db: <value in [disable, enable] default: 'disable'>
                  type: <value in [auto, onetime, daily, ...]>

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
            example: '/dvmdb/adom/{adom}/script/{script}/script_schedule/{script_schedule}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            datetime:
               type: str
               description: |
                  'Indicates the date and time of the schedule. It should follow the following format for each scheduling type:'
                  'onetime: "YYYY-MM-DD hh:mm:ss"'
                  'daily: "hh:mm"'
                  'weekly: "hh:mm"'
                  'monthly: "DD hh:mm"'
            day_of_week:
               type: str
               example: 'sun'
            device:
               type: int
               description: 'Name or id of an existing device in the database.'
            name:
               type: str
            run_on_db:
               type: str
               description: 'Indicates if the scheduled script should be executed on device database. It should always be disable for tcl scripts.'
               example: 'disable'
            type:
               type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/dvmdb/adom/{adom}/script/{script}/script_schedule/{script_schedule}'

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
        '/dvmdb/adom/{adom}/script/{script}/script_schedule/{script_schedule}',
        '/dvmdb/global/script/{script}/script_schedule/{script_schedule}',
        '/dvmdb/script/{script}/script_schedule/{script_schedule}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'script',
            'type': 'string'
        },
        {
            'name': 'script_schedule',
            'type': 'string'
        }
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
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'object member',
                            'chksum'
                        ]
                    },
                    'api_tag': 0
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object2': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'datetime': {
                            'type': 'string'
                        },
                        'day_of_week': {
                            'type': 'string',
                            'enum': [
                                'unknown',
                                'sun',
                                'mon',
                                'tue',
                                'wed',
                                'thu',
                                'fri',
                                'sat'
                            ]
                        },
                        'device': {
                            'type': 'integer'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'run_on_db': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'type': {
                            'type': 'string',
                            'enum': [
                                'auto',
                                'onetime',
                                'daily',
                                'weekly',
                                'monthly'
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
            'delete': 'object0',
            'get': 'object1',
            'set': 'object2',
            'update': 'object2'
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
