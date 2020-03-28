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
module: fmgr_fmupdate_fdssetting_updateschedule
short_description: Configure the schedule when built-in FortiGuard retrieves antivirus and IPS updates.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /cli/global/fmupdate/fds-setting/update-schedule
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
        description: 'Configure the schedule when built-in FortiGuard retrieves antivirus and IPS updates.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Configure the schedule when built-in FortiGuard retrieves antivirus and IPS updates.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                day:
                    type: str
                    default: 'Monday'
                    description:
                     - 'Configure the day the update will occur, if the freqnecy is weekly (Sunday - Saturday, default = Monday).'
                     - 'Sunday - Update every Sunday.'
                     - 'Monday - Update every Monday.'
                     - 'Tuesday - Update every Tuesday.'
                     - 'Wednesday - Update every Wednesday.'
                     - 'Thursday - Update every Thursday.'
                     - 'Friday - Update every Friday.'
                     - 'Saturday - Update every Saturday.'
                    choices:
                        - 'Sunday'
                        - 'Monday'
                        - 'Tuesday'
                        - 'Wednesday'
                        - 'Thursday'
                        - 'Friday'
                        - 'Saturday'
                frequency:
                    type: str
                    default: 'every'
                    description:
                     - 'Configure update frequency: every - time interval, daily - once a day, weekly - once a week (default = every).'
                     - 'every - Time interval.'
                     - 'daily - Every day.'
                     - 'weekly - Every week.'
                    choices:
                        - 'every'
                        - 'daily'
                        - 'weekly'
                status:
                    type: str
                    default: 'enable'
                    description:
                     - 'Enable/disable scheduled updates.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                time:
                    -
                        type: str

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

    - name: REQUESTING /CLI/FMUPDATE/FDS-SETTING/UPDATE-SCHEDULE
      fmgr_fmupdate_fdssetting_updateschedule:
         method: <value in [set, update]>
         params:
            -
               data:
                  day: <value in [Sunday, Monday, Tuesday, ...] default: 'Monday'>
                  frequency: <value in [every, daily, weekly] default: 'every'>
                  status: <value in [disable, enable] default: 'enable'>
                  time:
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
            day:
               type: str
               description: |
                  'Configure the day the update will occur, if the freqnecy is weekly (Sunday - Saturday, default = Monday).'
                  'Sunday - Update every Sunday.'
                  'Monday - Update every Monday.'
                  'Tuesday - Update every Tuesday.'
                  'Wednesday - Update every Wednesday.'
                  'Thursday - Update every Thursday.'
                  'Friday - Update every Friday.'
                  'Saturday - Update every Saturday.'
               example: 'Monday'
            frequency:
               type: str
               description: |
                  'Configure update frequency: every - time interval, daily - once a day, weekly - once a week (default = every).'
                  'every - Time interval.'
                  'daily - Every day.'
                  'weekly - Every week.'
               example: 'every'
            status:
               type: str
               description: |
                  'Enable/disable scheduled updates.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'enable'
            time:
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
            example: '/cli/global/fmupdate/fds-setting/update-schedule'
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
            example: '/cli/global/fmupdate/fds-setting/update-schedule'

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
        '/cli/global/fmupdate/fds-setting/update-schedule'
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
                        'day': {
                            'type': 'string',
                            'enum': [
                                'Sunday',
                                'Monday',
                                'Tuesday',
                                'Wednesday',
                                'Thursday',
                                'Friday',
                                'Saturday'
                            ]
                        },
                        'frequency': {
                            'type': 'string',
                            'enum': [
                                'every',
                                'daily',
                                'weekly'
                            ]
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'time': {
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
        'loose_validation': {
            'type': 'bool',
            'required': False,
            'default': False
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
