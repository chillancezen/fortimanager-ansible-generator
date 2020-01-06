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
module: fmgr_pm_config_pkg_pkg_firewall_dos_policy_dos_policy
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get move set update ] the following apis.
    - /pm/config/adom/{adom}/pkg/{pkg}/firewall/DoS-policy/{DoS-policy}
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
            pkg:
                type: str
            DoS-policy:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Configure IPv4 DoS policies.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                anomaly:
                    -
                        action:
                            type: str
                            description: 'Action taken when the threshold is reached.'
                            choices:
                                - 'pass'
                                - 'block'
                                - 'proxy'
                        log:
                            type: str
                            description: 'Enable/disable logging for this anomaly.'
                            choices:
                                - 'disable'
                                - 'enable'
                        name:
                            type: str
                            description: 'Anomaly name.'
                        quarantine:
                            type: str
                            description: 'Quarantine method.'
                            choices:
                                - 'none'
                                - 'attacker'
                                - 'both'
                                - 'interface'
                        quarantine-expiry:
                            type: str
                            description: 'Duration of quarantine, from 1 minute to 364 days, 23 hours, and 59 minutes from now. (format: ###d##h##m, default = 5m). Requires quarantine set to attacker.'
                        quarantine-log:
                            type: str
                            description: 'Enable/disable quarantine logging.'
                            choices:
                                - 'disable'
                                - 'enable'
                        status:
                            type: str
                            description: 'Enable/disable the active status of this anomaly sensor.'
                            choices:
                                - 'disable'
                                - 'enable'
                        threshold:
                            type: int
                            description: 'Number of detected instances per minute which triggers action (1 - 2147483647, default = 1000). Note that each anomaly has a different threshold value assigned to it.'
                        threshold(default):
                            type: int
                comments:
                    type: str
                    description: 'Comment.'
                dstaddr:
                    type: str
                    description: 'Destination address name from available addresses.'
                interface:
                    type: str
                    description: 'Incoming interface name from available interfaces.'
                policyid:
                    type: int
                    description: 'Policy ID.'
                service:
                    type: str
                    description: 'Service object from available options.'
                srcaddr:
                    type: str
                    description: 'Source address name from available addresses.'
                status:
                    type: str
                    description: 'Enable/disable this policy.'
                    choices:
                        - 'disable'
                        - 'enable'
    schema_object1:
        methods: [delete]
        description: 'Configure IPv4 DoS policies.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Configure IPv4 DoS policies.'
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
    schema_object3:
        methods: [move]
        description: 'Configure IPv4 DoS policies.'
        api_categories: [api_tag0]
        api_tag0:
            option:
                type: str
                choices:
                    - 'before'
                    - 'after'
            target:
                type: str
                description: 'Key to the target entry.'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /pm/config/pkg/{pkg}/firewall/DoS-policy/{DoS-policy}
      fmgr_pm_config_pkg_pkg_firewall_dos_policy_dos_policy:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            DoS-policy: <value of string>
         params:
            - 
               data: 
                  anomaly: 
                   - 
                        action: <value in [pass, block, proxy]>
                        log: <value in [disable, enable]>
                        name: <value of string>
                        quarantine: <value in [none, attacker, both, ...]>
                        quarantine-expiry: <value of string>
                        quarantine-log: <value in [disable, enable]>
                        status: <value in [disable, enable]>
                        threshold: <value of integer>
                        threshold(default): <value of integer>
                  comments: <value of string>
                  dstaddr: <value of string>
                  interface: <value of string>
                  policyid: <value of integer>
                  service: <value of string>
                  srcaddr: <value of string>
                  status: <value in [disable, enable]>
    - name: send request to /pm/config/pkg/{pkg}/firewall/DoS-policy/{DoS-policy}
      fmgr_pm_config_pkg_pkg_firewall_dos_policy_dos_policy:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            DoS-policy: <value of string>
         params:
            - 
               option: <value in [object member, chksum, datasrc]>
    - name: send request to /pm/config/pkg/{pkg}/firewall/DoS-policy/{DoS-policy}
      fmgr_pm_config_pkg_pkg_firewall_dos_policy_dos_policy:
         method: <value in [move]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            DoS-policy: <value of string>
         params:
            - 
               option: <value in [before, after]>
               target: <value of string>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[clone, move, set, update]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            policyid:
               type: int
               description: 'Policy ID.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/DoS-policy/{DoS-policy}
return_of_api_category_0:
   description: items returned for method:[delete]
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
            example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/DoS-policy/{DoS-policy}
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            anomaly:
               type: array
               suboptions:
                  action:
                     type: str
                     description: 'Action taken when the threshold is reached.'
                  log:
                     type: str
                     description: 'Enable/disable logging for this anomaly.'
                  name:
                     type: str
                     description: 'Anomaly name.'
                  quarantine:
                     type: str
                     description: 'Quarantine method.'
                  quarantine-expiry:
                     type: str
                     description: 'Duration of quarantine, from 1 minute to 364 days, 23 hours, and 59 minutes from now. (format: ###d##h##m, default = 5m). Requires quarantine set to attacker.'
                  quarantine-log:
                     type: str
                     description: 'Enable/disable quarantine logging.'
                  status:
                     type: str
                     description: 'Enable/disable the active status of this anomaly sensor.'
                  threshold:
                     type: int
                     description: 'Number of detected instances per minute which triggers action (1 - 2147483647, default = 1000). Note that each anomaly has a different threshold value assigned to it.'
                  threshold(default):
                     type: int
            comments:
               type: str
               description: 'Comment.'
            dstaddr:
               type: str
               description: 'Destination address name from available addresses.'
            interface:
               type: str
               description: 'Incoming interface name from available interfaces.'
            policyid:
               type: int
               description: 'Policy ID.'
            service:
               type: str
               description: 'Service object from available options.'
            srcaddr:
               type: str
               description: 'Source address name from available addresses.'
            status:
               type: str
               description: 'Enable/disable this policy.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/DoS-policy/{DoS-policy}

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
        '/pm/config/adom/{adom}/pkg/{pkg}/firewall/DoS-policy/{DoS-policy}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'pkg',
            'type': 'string'
        },
        {
            'name': 'DoS-policy',
            'type': 'string'
        }
    ]

    body_schema =  {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'anomaly': {
                            'type': 'array',
                            'items': {
                                'action': {
                                    'type': 'string',
                                    'enum': [
                                        'pass',
                                        'block',
                                        'proxy'
                                    ]
                                },
                                'log': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'name': {
                                    'type': 'string'
                                },
                                'quarantine': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'attacker',
                                        'both',
                                        'interface'
                                    ]
                                },
                                'quarantine-expiry': {
                                    'type': 'string'
                                },
                                'quarantine-log': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'status': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'threshold': {
                                    'type': 'integer'
                                },
                                'threshold(default)': {
                                    'type': 'integer'
                                }
                            }
                        },
                        'comments': {
                            'type': 'string'
                        },
                        'dstaddr': {
                            'type': 'string'
                        },
                        'interface': {
                            'type': 'string'
                        },
                        'policyid': {
                            'type': 'integer'
                        },
                        'service': {
                            'type': 'string'
                        },
                        'srcaddr': {
                            'type': 'string'
                        },
                        'status': {
                            'type': 'string',
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
            ],
            'object1': [
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object2': [
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
            'object3': [
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'before',
                            'after'
                        ]
                    },
                    'api_tag': 0
                },
                {
                    'type': 'string',
                    'name': 'target',
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
            'clone': 'object0',
            'delete': 'object1',
            'get': 'object2',
            'move': 'object3',
            'set': 'object0',
            'update': 'object0'
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
                'clone',
                'delete',
                'get',
                'move',
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