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
module: fmgr_firewall_mmsprofile_flood
short_description: Flood configuration.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/firewall/mms-profile/{mms-profile}/flood
    - /pm/config/global/obj/firewall/mms-profile/{mms-profile}/flood
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
            mms-profile:
                type: str
    schema_object0:
        methods: [get]
        description: 'Flood configuration.'
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
                    - 'datasrc'
    schema_object1:
        methods: [set, update]
        description: 'Flood configuration.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                action1:
                    -
                        type: str
                        choices:
                            - 'log'
                            - 'archive'
                            - 'intercept'
                            - 'block'
                            - 'archive-first'
                            - 'alert-notif'
                action2:
                    -
                        type: str
                        choices:
                            - 'log'
                            - 'archive'
                            - 'intercept'
                            - 'block'
                            - 'archive-first'
                            - 'alert-notif'
                action3:
                    -
                        type: str
                        choices:
                            - 'log'
                            - 'archive'
                            - 'intercept'
                            - 'block'
                            - 'archive-first'
                            - 'alert-notif'
                block-time1:
                    type: int
                    description: 'Duration for which action takes effect (0 - 35791 min).'
                block-time2:
                    type: int
                    description: 'Duration for which action takes effect (0 - 35791 min).'
                block-time3:
                    type: int
                    description: 'Duration action takes effect (0 - 35791 min).'
                limit1:
                    type: int
                    description: 'Maximum number of messages allowed.'
                limit2:
                    type: int
                    description: 'Maximum number of messages allowed.'
                limit3:
                    type: int
                    description: 'Maximum number of messages allowed.'
                protocol:
                    type: str
                    description: 'Protocol.'
                status1:
                    type: str
                    description: 'Enable/disable status1 detection.'
                    choices:
                        - 'disable'
                        - 'enable'
                status2:
                    type: str
                    description: 'Enable/disable status2 detection.'
                    choices:
                        - 'disable'
                        - 'enable'
                status3:
                    type: str
                    description: 'Enable/disable status3 detection.'
                    choices:
                        - 'disable'
                        - 'enable'
                window1:
                    type: int
                    description: 'Window to count messages over (1 - 2880 min).'
                window2:
                    type: int
                    description: 'Window to count messages over (1 - 2880 min).'
                window3:
                    type: int
                    description: 'Window to count messages over (1 - 2880 min).'

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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/MMS-PROFILE/{MMS-PROFILE}/FLOOD
      fmgr_firewall_mmsprofile_flood:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            mms-profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/MMS-PROFILE/{MMS-PROFILE}/FLOOD
      fmgr_firewall_mmsprofile_flood:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            mms-profile: <value of string>
         params:
            -
               data:
                  action1:
                    - <value in [log, archive, intercept, ...]>
                  action2:
                    - <value in [log, archive, intercept, ...]>
                  action3:
                    - <value in [log, archive, intercept, ...]>
                  block-time1: <value of integer>
                  block-time2: <value of integer>
                  block-time3: <value of integer>
                  limit1: <value of integer>
                  limit2: <value of integer>
                  limit3: <value of integer>
                  protocol: <value of string>
                  status1: <value in [disable, enable]>
                  status2: <value in [disable, enable]>
                  status3: <value in [disable, enable]>
                  window1: <value of integer>
                  window2: <value of integer>
                  window3: <value of integer>

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
            action1:
               type: array
               suboptions:
                  type: str
            action2:
               type: array
               suboptions:
                  type: str
            action3:
               type: array
               suboptions:
                  type: str
            block-time1:
               type: int
               description: 'Duration for which action takes effect (0 - 35791 min).'
            block-time2:
               type: int
               description: 'Duration for which action takes effect (0 - 35791 min).'
            block-time3:
               type: int
               description: 'Duration action takes effect (0 - 35791 min).'
            limit1:
               type: int
               description: 'Maximum number of messages allowed.'
            limit2:
               type: int
               description: 'Maximum number of messages allowed.'
            limit3:
               type: int
               description: 'Maximum number of messages allowed.'
            protocol:
               type: str
               description: 'Protocol.'
            status1:
               type: str
               description: 'Enable/disable status1 detection.'
            status2:
               type: str
               description: 'Enable/disable status2 detection.'
            status3:
               type: str
               description: 'Enable/disable status3 detection.'
            window1:
               type: int
               description: 'Window to count messages over (1 - 2880 min).'
            window2:
               type: int
               description: 'Window to count messages over (1 - 2880 min).'
            window3:
               type: int
               description: 'Window to count messages over (1 - 2880 min).'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/firewall/mms-profile/{mms-profile}/flood'
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
            example: '/pm/config/adom/{adom}/obj/firewall/mms-profile/{mms-profile}/flood'

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
        '/pm/config/adom/{adom}/obj/firewall/mms-profile/{mms-profile}/flood',
        '/pm/config/global/obj/firewall/mms-profile/{mms-profile}/flood'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'mms-profile',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'object member',
                            'chksum',
                            'datasrc'
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
            'object1': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'action1': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'log',
                                    'archive',
                                    'intercept',
                                    'block',
                                    'archive-first',
                                    'alert-notif'
                                ]
                            }
                        },
                        'action2': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'log',
                                    'archive',
                                    'intercept',
                                    'block',
                                    'archive-first',
                                    'alert-notif'
                                ]
                            }
                        },
                        'action3': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'log',
                                    'archive',
                                    'intercept',
                                    'block',
                                    'archive-first',
                                    'alert-notif'
                                ]
                            }
                        },
                        'block-time1': {
                            'type': 'integer'
                        },
                        'block-time2': {
                            'type': 'integer'
                        },
                        'block-time3': {
                            'type': 'integer'
                        },
                        'limit1': {
                            'type': 'integer'
                        },
                        'limit2': {
                            'type': 'integer'
                        },
                        'limit3': {
                            'type': 'integer'
                        },
                        'protocol': {
                            'type': 'string'
                        },
                        'status1': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'status2': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'status3': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'window1': {
                            'type': 'integer'
                        },
                        'window2': {
                            'type': 'integer'
                        },
                        'window3': {
                            'type': 'integer'
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
