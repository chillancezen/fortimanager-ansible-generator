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
module: fmgr_cli_system_snmp_user_user
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ delete get set update ] the following apis:
    - /cli/global/system/snmp/user/{user}
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
    url_params: 
        description: the parameters in url path
        required: True
        type: dict
        suboptions:
            user:
                type: str
    schema_object0:
        methods: [delete, get]
        description: 'SNMP user configuration.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'SNMP user configuration.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                auth-proto:
                    type: str
                    default: sha
                    description:
                     - 'Authentication protocol.'
                     - 'md5 - HMAC-MD5-96 authentication protocol.'
                     - 'sha - HMAC-SHA-96 authentication protocol.'
                    choices:
                        - md5
                        - sha
                auth-pwd:
                    -
                        type: str
                        default: ENC NjAyNzczNjcyNzY3Nzg1Of2B29hwP1lYq82MXmrQ1PG7EGaRNDqkrqYFYL1NNEgm54idZER+oDi44SCyPKkvrPPrxgkkBtYnh1uQ3hobimfdeMd2rooTubF9B+lKXyq06wTtneMsxzjLK1SP1NNDy91keEpVFpDTpHpRtZ1meW8+NS8k
                events:
                    -
                        type: str
                        choices:
                            - disk_low
                            - ha_switch
                            - intf_ip_chg
                            - sys_reboot
                            - cpu_high
                            - mem_low
                            - log-alert
                            - log-rate
                            - log-data-rate
                            - lic-gbday
                            - lic-dev-quota
                            - cpu-high-exclude-nice
                name:
                    type: str
                    description: 'SNMP user name.'
                notify-hosts:
                    type: str
                    description: 'Hosts to send notifications (traps) to.'
                notify-hosts6:
                    type: str
                    description: 'IPv6 hosts to send notifications (traps) to.'
                priv-proto:
                    type: str
                    default: aes
                    description:
                     - 'Privacy (encryption) protocol.'
                     - 'aes - CFB128-AES-128 symmetric encryption protocol.'
                     - 'des - CBC-DES symmetric encryption protocol.'
                    choices:
                        - aes
                        - des
                priv-pwd:
                    -
                        type: str
                        default: ENC OTA3MDU5Nzg1ODQ2MDM2NInoPzPSYfTulrcxKZ65Re1ROZUOMQVvU4dqPX5WkABZ8PkpLAOtCEZJPjCcJbybir6Dw9yptXUDyKN4hUHbzauIOAQ2Az8BlB5n4ifkMNTkDDDxZ7r6oB0GK+QmJM9n2wjUGMCcVi0sG9l4bc9sFFuBi4mJ
                queries:
                    type: str
                    default: enable
                    description:
                     - 'Enable/disable queries for this user.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - disable
                        - enable
                query-port:
                    type: int
                    default: 161
                    description: 'SNMPv3 query port.'
                security-level:
                    type: str
                    default: no-auth-no-priv
                    description:
                     - 'Security level for message authentication and encryption.'
                     - 'no-auth-no-priv - Message with no authentication and no privacy (encryption).'
                     - 'auth-no-priv - Message with authentication but no privacy (encryption).'
                     - 'auth-priv - Message with authentication and privacy (encryption).'
                    choices:
                        - no-auth-no-priv
                        - auth-no-priv
                        - auth-priv

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /cli/system/snmp/user/{user}
      fmgr_cli_system_snmp_user_user:
         method: <value in [set, update]>
         url_params:
            user: <value of string>
         params:
            - 
               data: 
                  auth-proto: <value in [md5, sha] default: sha>
                  auth-pwd: 
                   - <value of string default: ENC NjAyNzczNjcyNzY3Nzg1Of2B29hwP1lYq82MXmrQ1PG7EGaRNDqkrqYFYL1NNEgm54idZER+oDi44SCyPKkvrPPrxgkkBtYnh1uQ3hobimfdeMd2rooTubF9B+lKXyq06wTtneMsxzjLK1SP1NNDy91keEpVFpDTpHpRtZ1meW8+NS8k>
                  events: 
                   - <value in [disk_low, ha_switch, intf_ip_chg, ...]>
                  name: <value of string>
                  notify-hosts: <value of string>
                  notify-hosts6: <value of string>
                  priv-proto: <value in [aes, des] default: aes>
                  priv-pwd: 
                   - <value of string default: ENC OTA3MDU5Nzg1ODQ2MDM2NInoPzPSYfTulrcxKZ65Re1ROZUOMQVvU4dqPX5WkABZ8PkpLAOtCEZJPjCcJbybir6Dw9yptXUDyKN4hUHbzauIOAQ2Az8BlB5n4ifkMNTkDDDxZ7r6oB0GK+QmJM9n2wjUGMCcVi0sG9l4bc9sFFuBi4mJ>
                  queries: <value in [disable, enable] default: enable>
                  query-port: <value of integer default: 161>
                  security-level: <value in [no-auth-no-priv, auth-no-priv, auth-priv] default: no-auth-no-priv>

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
            example: /cli/global/system/snmp/user/{user}
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            auth-proto:
               type: str
               description: |
                  'Authentication protocol.'
                  'md5 - HMAC-MD5-96 authentication protocol.'
                  'sha - HMAC-SHA-96 authentication protocol.'
               example: sha
            auth-pwd:
               type: array
               suboptions:
                  type: str
                  example: ENC NjAyNzczNjcyNzY3Nzg1Of2B29hwP1lYq82MXmrQ1PG7EGaRNDqkrqYFYL1NNEgm54idZER+oDi44SCyPKkvrPPrxgkkBtYnh1uQ3hobimfdeMd2rooTubF9B+lKXyq06wTtneMsxzjLK1SP1NNDy91keEpVFpDTpHpRtZ1meW8+NS8k
            events:
               type: array
               suboptions:
                  type: str
            name:
               type: str
               description: 'SNMP user name.'
            notify-hosts:
               type: str
               description: 'Hosts to send notifications (traps) to.'
            notify-hosts6:
               type: str
               description: 'IPv6 hosts to send notifications (traps) to.'
            priv-proto:
               type: str
               description: |
                  'Privacy (encryption) protocol.'
                  'aes - CFB128-AES-128 symmetric encryption protocol.'
                  'des - CBC-DES symmetric encryption protocol.'
               example: aes
            priv-pwd:
               type: array
               suboptions:
                  type: str
                  example: ENC OTA3MDU5Nzg1ODQ2MDM2NInoPzPSYfTulrcxKZ65Re1ROZUOMQVvU4dqPX5WkABZ8PkpLAOtCEZJPjCcJbybir6Dw9yptXUDyKN4hUHbzauIOAQ2Az8BlB5n4ifkMNTkDDDxZ7r6oB0GK+QmJM9n2wjUGMCcVi0sG9l4bc9sFFuBi4mJ
            queries:
               type: str
               description: |
                  'Enable/disable queries for this user.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            query-port:
               type: int
               description: 'SNMPv3 query port.'
               example: 161
            security-level:
               type: str
               description: |
                  'Security level for message authentication and encryption.'
                  'no-auth-no-priv - Message with no authentication and no privacy (encryption).'
                  'auth-no-priv - Message with authentication but no privacy (encryption).'
                  'auth-priv - Message with authentication and privacy (encryption).'
               example: no-auth-no-priv
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /cli/global/system/snmp/user/{user}

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
        '/cli/global/system/snmp/user/{user}'
    ]

    url_schema = [
        {
            'name': 'user',
            'type': 'string'
        }
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
                        'auth-proto': {
                            'type': 'string',
                            'default': 'sha',
                            'enum': [
                                'md5',
                                'sha'
                            ]
                        },
                        'auth-pwd': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'default': 'ENC NjAyNzczNjcyNzY3Nzg1Of2B29hwP1lYq82MXmrQ1PG7EGaRNDqkrqYFYL1NNEgm54idZER+oDi44SCyPKkvrPPrxgkkBtYnh1uQ3hobimfdeMd2rooTubF9B+lKXyq06wTtneMsxzjLK1SP1NNDy91keEpVFpDTpHpRtZ1meW8+NS8k'
                            }
                        },
                        'events': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'disk_low',
                                    'ha_switch',
                                    'intf_ip_chg',
                                    'sys_reboot',
                                    'cpu_high',
                                    'mem_low',
                                    'log-alert',
                                    'log-rate',
                                    'log-data-rate',
                                    'lic-gbday',
                                    'lic-dev-quota',
                                    'cpu-high-exclude-nice'
                                ]
                            }
                        },
                        'name': {
                            'type': 'string'
                        },
                        'notify-hosts': {
                            'type': 'string'
                        },
                        'notify-hosts6': {
                            'type': 'string'
                        },
                        'priv-proto': {
                            'type': 'string',
                            'default': 'aes',
                            'enum': [
                                'aes',
                                'des'
                            ]
                        },
                        'priv-pwd': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'default': 'ENC OTA3MDU5Nzg1ODQ2MDM2NInoPzPSYfTulrcxKZ65Re1ROZUOMQVvU4dqPX5WkABZ8PkpLAOtCEZJPjCcJbybir6Dw9yptXUDyKN4hUHbzauIOAQ2Az8BlB5n4ifkMNTkDDDxZ7r6oB0GK+QmJM9n2wjUGMCcVi0sG9l4bc9sFFuBi4mJ'
                            }
                        },
                        'queries': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'query-port': {
                            'type': 'integer',
                            'default': 161,
                            'example': 161
                        },
                        'security-level': {
                            'type': 'string',
                            'default': 'no-auth-no-priv',
                            'enum': [
                                'no-auth-no-priv',
                                'auth-no-priv',
                                'auth-priv'
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