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
module: fmgr_cli_system_backup_all_settings
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /cli/global/system/backup/all-settings
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
        description: 'Scheduled backup settings.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Scheduled backup settings.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                cert:
                    type: str
                    description: 'SSH certificate for authentication.'
                crptpasswd:
                    -
                        type: str
                        default: 'ENC MTMzMDc1MDgxNzQ0ODY0M2NSZUKD2VMvwzY+fu/IOqXefv5r84Cvz6X817vduD08gM1BG0K7muAtsALrSSvZjpqR08ZjShNGdhTR6Y7clcN6rnCh7jFAA...'
                directory:
                    type: str
                    description: 'Directory in which file will be stored on backup server.'
                passwd:
                    -
                        type: str
                        default: 'ENC NjE1OTk5NjcxODE1MDYyOR9zgwo4rNRY0psUIe6ZdXfehJTrTnmzU4GJWXfob8IxqxmLrU/5rQxywxo85lXVAnrjLD1WUkUEls6PMhOwReIaAQVP0y0g8...'
                protocol:
                    type: str
                    default: 'sftp'
                    description:
                     - 'Protocol used to backup.'
                     - 'sftp - SFTP.'
                     - 'ftp - FTP.'
                     - 'scp - SCP.'
                    choices:
                        - 'sftp'
                        - 'ftp'
                        - 'scp'
                server:
                    type: str
                    description: 'Backup server name/IP.'
                status:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable schedule backup.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                time:
                    type: str
                    description: 'Time to backup.'
                user:
                    type: str
                    description: 'Backup server login user.'
                week_days:
                    -
                        type: str
                        choices:
                            - 'monday'
                            - 'tuesday'
                            - 'wednesday'
                            - 'thursday'
                            - 'friday'
                            - 'saturday'
                            - 'sunday'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /CLI/SYSTEM/BACKUP/ALL-SETTINGS
      fmgr_cli_system_backup_all_settings:
         method: <value in [set, update]>
         params:
            -
               data:
                  cert: <value of string>
                  crptpasswd:
                    - <value of string default: 'ENC MTMzMDc1MDgxNzQ0ODY0M2NSZUKD2VMvwzY+fu/IOqXefv5r84Cvz6X817vduD08gM1BG0K7...'>
                  directory: <value of string>
                  passwd:
                    - <value of string default: 'ENC NjE1OTk5NjcxODE1MDYyOR9zgwo4rNRY0psUIe6ZdXfehJTrTnmzU4GJWXfob8IxqxmLrU/5...'>
                  protocol: <value in [sftp, ftp, scp] default: 'sftp'>
                  server: <value of string>
                  status: <value in [disable, enable] default: 'disable'>
                  time: <value of string>
                  user: <value of string>
                  week_days:
                    - <value in [monday, tuesday, wednesday, ...]>

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
            cert:
               type: str
               description: 'SSH certificate for authentication.'
            crptpasswd:
               type: array
               suboptions:
                  type: str
                  example: 'ENC MTMzMDc1MDgxNzQ0ODY0M2NSZUKD2VMvwzY+fu/IOqXefv5r84Cvz6X817vduD08gM1BG0K7...'
            directory:
               type: str
               description: 'Directory in which file will be stored on backup server.'
            passwd:
               type: array
               suboptions:
                  type: str
                  example: 'ENC NjE1OTk5NjcxODE1MDYyOR9zgwo4rNRY0psUIe6ZdXfehJTrTnmzU4GJWXfob8IxqxmLrU/5...'
            protocol:
               type: str
               description: |
                  'Protocol used to backup.'
                  'sftp - SFTP.'
                  'ftp - FTP.'
                  'scp - SCP.'
               example: 'sftp'
            server:
               type: str
               description: 'Backup server name/IP.'
            status:
               type: str
               description: |
                  'Enable/disable schedule backup.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'disable'
            time:
               type: str
               description: 'Time to backup.'
            user:
               type: str
               description: 'Backup server login user.'
            week_days:
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
            example: '/cli/global/system/backup/all-settings'
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
            example: '/cli/global/system/backup/all-settings'

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
        '/cli/global/system/backup/all-settings'
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
                        'cert': {
                            'type': 'string'
                        },
                        'crptpasswd': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'directory': {
                            'type': 'string'
                        },
                        'passwd': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'protocol': {
                            'type': 'string',
                            'enum': [
                                'sftp',
                                'ftp',
                                'scp'
                            ]
                        },
                        'server': {
                            'type': 'string'
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'time': {
                            'type': 'string'
                        },
                        'user': {
                            'type': 'string'
                        },
                        'week_days': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'monday',
                                    'tuesday',
                                    'wednesday',
                                    'thursday',
                                    'friday',
                                    'saturday',
                                    'sunday'
                                ]
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

    module.exit_json(**response[1])


if __name__ == '__main__':
    main()
