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
module: fmgr_pm_config_obj_switch_controller_lldp_profile_per_object
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/switch-controller/lldp-profile/{lldp-profile}
    - /pm/config/global/obj/switch-controller/lldp-profile/{lldp-profile}
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
            lldp-profile:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Configure FortiSwitch LLDP profiles.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                802.1-tlvs:
                    -
                        type: str
                        choices:
                            - 'port-vlan-id'
                802.3-tlvs:
                    -
                        type: str
                        choices:
                            - 'max-frame-size'
                auto-isl:
                    type: str
                    description: 'Enable/disable auto inter-switch LAG.'
                    choices:
                        - 'disable'
                        - 'enable'
                auto-isl-hello-timer:
                    type: int
                    description: 'Auto inter-switch LAG hello timer duration (1 - 30 sec, default = 3).'
                auto-isl-port-group:
                    type: int
                    description: 'Auto inter-switch LAG port group ID (0 - 9).'
                auto-isl-receive-timeout:
                    type: int
                    description: 'Auto inter-switch LAG timeout if no response is received (3 - 90 sec, default = 9).'
                custom-tlvs:
                    -
                        information-string:
                            type: str
                            description: 'Organizationally defined information string (0 - 507 hexadecimal bytes).'
                        name:
                            type: str
                            description: 'TLV name (not sent).'
                        oui:
                            type: str
                            description: 'Organizationally unique identifier (OUI), a 3-byte hexadecimal number, for this TLV.'
                        subtype:
                            type: int
                            description: 'Organizationally defined subtype (0 - 255).'
                med-network-policy:
                    -
                        dscp:
                            type: int
                            description: 'Advertised Differentiated Services Code Point (DSCP) value, a packet header value indicating the level of service ...'
                        name:
                            type: str
                            description: 'Policy type name.'
                        priority:
                            type: int
                            description: 'Advertised Layer 2 priority (0 - 7; from lowest to highest priority).'
                        status:
                            type: str
                            description: 'Enable or disable this TLV.'
                            choices:
                                - 'disable'
                                - 'enable'
                        vlan:
                            type: int
                            description: 'ID of VLAN to advertise, if configured on port (0 - 4094, 0 = priority tag).'
                med-tlvs:
                    -
                        type: str
                        choices:
                            - 'inventory-management'
                            - 'network-policy'
                            - 'power-management'
                            - 'location-identification'
                name:
                    type: str
                    description: 'Profile name.'
    schema_object1:
        methods: [delete]
        description: 'Configure FortiSwitch LLDP profiles.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Configure FortiSwitch LLDP profiles.'
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

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/SWITCH-CONTROLLER/LLDP-PROFILE/{LLDP-PROFILE}
      fmgr_pm_config_obj_switch_controller_lldp_profile_per_object:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            lldp-profile: <value of string>
         params:
            -
               data:
                  802.1-tlvs:
                    - <value in [port-vlan-id]>
                  802.3-tlvs:
                    - <value in [max-frame-size]>
                  auto-isl: <value in [disable, enable]>
                  auto-isl-hello-timer: <value of integer>
                  auto-isl-port-group: <value of integer>
                  auto-isl-receive-timeout: <value of integer>
                  custom-tlvs:
                    -
                        information-string: <value of string>
                        name: <value of string>
                        oui: <value of string>
                        subtype: <value of integer>
                  med-network-policy:
                    -
                        dscp: <value of integer>
                        name: <value of string>
                        priority: <value of integer>
                        status: <value in [disable, enable]>
                        vlan: <value of integer>
                  med-tlvs:
                    - <value in [inventory-management, network-policy, power-management, ...]>
                  name: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/SWITCH-CONTROLLER/LLDP-PROFILE/{LLDP-PROFILE}
      fmgr_pm_config_obj_switch_controller_lldp_profile_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            lldp-profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[clone, delete, set, update]
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
            example: '/pm/config/adom/{adom}/obj/switch-controller/lldp-profile/{lldp-profile}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            802.1-tlvs:
               type: array
               suboptions:
                  type: str
            802.3-tlvs:
               type: array
               suboptions:
                  type: str
            auto-isl:
               type: str
               description: 'Enable/disable auto inter-switch LAG.'
            auto-isl-hello-timer:
               type: int
               description: 'Auto inter-switch LAG hello timer duration (1 - 30 sec, default = 3).'
            auto-isl-port-group:
               type: int
               description: 'Auto inter-switch LAG port group ID (0 - 9).'
            auto-isl-receive-timeout:
               type: int
               description: 'Auto inter-switch LAG timeout if no response is received (3 - 90 sec, default = 9).'
            custom-tlvs:
               type: array
               suboptions:
                  information-string:
                     type: str
                     description: 'Organizationally defined information string (0 - 507 hexadecimal bytes).'
                  name:
                     type: str
                     description: 'TLV name (not sent).'
                  oui:
                     type: str
                     description: 'Organizationally unique identifier (OUI), a 3-byte hexadecimal number, for this TLV.'
                  subtype:
                     type: int
                     description: 'Organizationally defined subtype (0 - 255).'
            med-network-policy:
               type: array
               suboptions:
                  dscp:
                     type: int
                     description: 'Advertised Differentiated Services Code Point (DSCP) value, a packet header value indicating the level of service request...'
                  name:
                     type: str
                     description: 'Policy type name.'
                  priority:
                     type: int
                     description: 'Advertised Layer 2 priority (0 - 7; from lowest to highest priority).'
                  status:
                     type: str
                     description: 'Enable or disable this TLV.'
                  vlan:
                     type: int
                     description: 'ID of VLAN to advertise, if configured on port (0 - 4094, 0 = priority tag).'
            med-tlvs:
               type: array
               suboptions:
                  type: str
            name:
               type: str
               description: 'Profile name.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/switch-controller/lldp-profile/{lldp-profile}'

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
        '/pm/config/adom/{adom}/obj/switch-controller/lldp-profile/{lldp-profile}',
        '/pm/config/global/obj/switch-controller/lldp-profile/{lldp-profile}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'lldp-profile',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        '802.1-tlvs': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'port-vlan-id'
                                ]
                            }
                        },
                        '802.3-tlvs': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'max-frame-size'
                                ]
                            }
                        },
                        'auto-isl': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'auto-isl-hello-timer': {
                            'type': 'integer'
                        },
                        'auto-isl-port-group': {
                            'type': 'integer'
                        },
                        'auto-isl-receive-timeout': {
                            'type': 'integer'
                        },
                        'custom-tlvs': {
                            'type': 'array',
                            'items': {
                                'information-string': {
                                    'type': 'string'
                                },
                                'name': {
                                    'type': 'string'
                                },
                                'oui': {
                                    'type': 'string'
                                },
                                'subtype': {
                                    'type': 'integer'
                                }
                            }
                        },
                        'med-network-policy': {
                            'type': 'array',
                            'items': {
                                'dscp': {
                                    'type': 'integer'
                                },
                                'name': {
                                    'type': 'string'
                                },
                                'priority': {
                                    'type': 'integer'
                                },
                                'status': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'vlan': {
                                    'type': 'integer'
                                }
                            }
                        },
                        'med-tlvs': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'inventory-management',
                                    'network-policy',
                                    'power-management',
                                    'location-identification'
                                ]
                            }
                        },
                        'name': {
                            'type': 'string'
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
            ]
        },
        'method_mapping': {
            'clone': 'object0',
            'delete': 'object1',
            'get': 'object2',
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
