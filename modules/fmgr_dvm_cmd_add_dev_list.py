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
module: fmgr_dvm_cmd_add_dev_list
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ exec ] the following apis.
    - /dvm/cmd/add/dev-list
    - /dvm/cmd/add/dev-list
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
        methods: [exec]
        description: 'Add multiple devices to the Device Manager database.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                add-dev-list:
                    -
                        adm_pass:
                            -
                                type: str
                        adm_usr:
                            type: str
                            description: '<i>add real and promote device</i>.'
                        desc:
                            type: str
                            description: '<i>available for all operations</i>.'
                        device action:
                            type: str
                            description:
                             - 'Specify add device operations, or leave blank to add real device:'
                             - '"add_model" - add a model device.'
                             - '"promote_unreg" - promote an unregistered device to be managed by FortiManager using information from database.'
                        faz.quota:
                            type: int
                            description: '<i>available for all operations</i>.'
                        ip:
                            type: str
                            description: '<i>add real device only</i>. Add device will probe with this IP using the log in credential specified.'
                        meta fields:
                            type: str
                            description: '<i>add real and model device</i>.'
                        mgmt_mode:
                            type: str
                            description: '<i>add real and model device</i>.'
                            choices:
                                - 'unreg'
                                - 'fmg'
                                - 'faz'
                                - 'fmgfaz'
                        mr:
                            type: int
                            description: '<i>add model device only</i>.'
                        name:
                            type: str
                            description: '<i>required for all operations</i>. Unique name for the device.'
                        os_type:
                            type: str
                            description: '<i>add model device only</i>.'
                            choices:
                                - 'unknown'
                                - 'fos'
                                - 'fsw'
                                - 'foc'
                                - 'fml'
                                - 'faz'
                                - 'fwb'
                                - 'fch'
                                - 'fct'
                                - 'log'
                                - 'fmg'
                                - 'fsa'
                                - 'fdd'
                                - 'fac'
                        os_ver:
                            type: str
                            description: '<i>add model device only</i>.'
                            choices:
                                - 'unknown'
                                - '0.0'
                                - '1.0'
                                - '2.0'
                                - '3.0'
                                - '4.0'
                                - '5.0'
                        patch:
                            type: int
                            description: '<i>add model device only</i>.'
                        platform_str:
                            type: str
                            description: '<i>add model device only</i>. Required for determine the platform for VM platforms.'
                        sn:
                            type: str
                            description: '<i>add model device only</i>. This attribute will be used to determine the device platform, except for VM platform...'
                adom:
                    type: str
                    description: 'Name or ID of the ADOM where the command is to be executed on.'
                flags:
                    -
                        type: str
                        choices:
                            - 'none'
                            - 'create_task'
                            - 'nonblocking'
                            - 'log_dev'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /DVM/CMD/ADD/DEV-LIST
      fmgr_dvm_cmd_add_dev_list:
         method: <value in [exec]>
         params:
            -
               data:
                  add-dev-list:
                    -
                        adm_pass:
                          - <value of string>
                        adm_usr: <value of string>
                        desc: <value of string>
                        device action: <value of string>
                        faz.quota: <value of integer>
                        ip: <value of string>
                        meta fields: <value of string>
                        mgmt_mode: <value in [unreg, fmg, faz, ...]>
                        mr: <value of integer>
                        name: <value of string>
                        os_type: <value in [unknown, fos, fsw, ...]>
                        os_ver: <value in [unknown, 0.0, 1.0, ...]>
                        patch: <value of integer>
                        platform_str: <value of string>
                        sn: <value of string>
                  adom: <value of string>
                  flags:
                    - <value in [none, create_task, nonblocking, ...]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[exec]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            pid:
               type: int
               description: 'When "nonblocking" flag is set, return the process ID for the command.'
            taskid:
               type: str
               description: 'When "create_task" flag is set, return the ID of the task associated with the command.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/dvm/cmd/add/dev-list'

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
        '/dvm/cmd/add/dev-list',
        '/dvm/cmd/add/dev-list'
    ]

    url_schema = [
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'add-dev-list': {
                            'type': 'array',
                            'items': {
                                'adm_pass': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                },
                                'adm_usr': {
                                    'type': 'string'
                                },
                                'desc': {
                                    'type': 'string'
                                },
                                'device action': {
                                    'type': 'string'
                                },
                                'faz.quota': {
                                    'type': 'integer'
                                },
                                'ip': {
                                    'type': 'string'
                                },
                                'meta fields': {
                                    'type': 'string'
                                },
                                'mgmt_mode': {
                                    'type': 'string',
                                    'enum': [
                                        'unreg',
                                        'fmg',
                                        'faz',
                                        'fmgfaz'
                                    ]
                                },
                                'mr': {
                                    'type': 'integer'
                                },
                                'name': {
                                    'type': 'string'
                                },
                                'os_type': {
                                    'type': 'string',
                                    'enum': [
                                        'unknown',
                                        'fos',
                                        'fsw',
                                        'foc',
                                        'fml',
                                        'faz',
                                        'fwb',
                                        'fch',
                                        'fct',
                                        'log',
                                        'fmg',
                                        'fsa',
                                        'fdd',
                                        'fac'
                                    ]
                                },
                                'os_ver': {
                                    'type': 'string',
                                    'enum': [
                                        'unknown',
                                        '0.0',
                                        '1.0',
                                        '2.0',
                                        '3.0',
                                        '4.0',
                                        '5.0'
                                    ]
                                },
                                'patch': {
                                    'type': 'integer'
                                },
                                'platform_str': {
                                    'type': 'string'
                                },
                                'sn': {
                                    'type': 'string'
                                }
                            }
                        },
                        'adom': {
                            'type': 'string'
                        },
                        'flags': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'none',
                                    'create_task',
                                    'nonblocking',
                                    'log_dev'
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
            'exec': 'object0'
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
                'exec'
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
