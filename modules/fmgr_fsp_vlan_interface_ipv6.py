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
module: fmgr_fsp_vlan_interface_ipv6
short_description: no description
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/interface/ipv6
    - /pm/config/global/obj/fsp/vlan/{vlan}/interface/ipv6
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
            vlan:
                type: str
    schema_object0:
        methods: [get]
        description: ''
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
        description: ''
        api_categories: [api_tag0]
        api_tag0:
            data:
                autoconf:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                dhcp6-client-options:
                    -
                        type: str
                        choices:
                            - 'rapid'
                            - 'iapd'
                            - 'iana'
                            - 'dns'
                            - 'dnsname'
                dhcp6-information-request:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                dhcp6-prefix-delegation:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                dhcp6-prefix-hint:
                    type: str
                dhcp6-prefix-hint-plt:
                    type: int
                dhcp6-prefix-hint-vlt:
                    type: int
                dhcp6-relay-ip:
                    type: str
                dhcp6-relay-service:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                dhcp6-relay-type:
                    type: str
                    choices:
                        - 'regular'
                ip6-address:
                    type: str
                ip6-allowaccess:
                    -
                        type: str
                        choices:
                            - 'https'
                            - 'ping'
                            - 'ssh'
                            - 'snmp'
                            - 'http'
                            - 'telnet'
                            - 'fgfm'
                            - 'capwap'
                ip6-default-life:
                    type: int
                ip6-dns-server-override:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ip6-hop-limit:
                    type: int
                ip6-link-mtu:
                    type: int
                ip6-manage-flag:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ip6-max-interval:
                    type: int
                ip6-min-interval:
                    type: int
                ip6-mode:
                    type: str
                    choices:
                        - 'static'
                        - 'dhcp'
                        - 'pppoe'
                        - 'delegated'
                ip6-other-flag:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ip6-reachable-time:
                    type: int
                ip6-retrans-time:
                    type: int
                ip6-send-adv:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ip6-subnet:
                    type: str
                ip6-upstream-interface:
                    type: str
                nd-cert:
                    type: str
                nd-cga-modifier:
                    type: str
                nd-mode:
                    type: str
                    choices:
                        - 'basic'
                        - 'SEND-compatible'
                nd-security-level:
                    type: int
                nd-timestamp-delta:
                    type: int
                nd-timestamp-fuzz:
                    type: int
                vrip6_link_local:
                    type: str
                vrrp-virtual-mac6:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'

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

    - name: REQUESTING /PM/CONFIG/OBJ/FSP/VLAN/{VLAN}/INTERFACE/IPV6
      fmgr_fsp_vlan_interface_ipv6:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vlan: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/FSP/VLAN/{VLAN}/INTERFACE/IPV6
      fmgr_fsp_vlan_interface_ipv6:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vlan: <value of string>
         params:
            -
               data:
                  autoconf: <value in [disable, enable]>
                  dhcp6-client-options:
                    - <value in [rapid, iapd, iana, ...]>
                  dhcp6-information-request: <value in [disable, enable]>
                  dhcp6-prefix-delegation: <value in [disable, enable]>
                  dhcp6-prefix-hint: <value of string>
                  dhcp6-prefix-hint-plt: <value of integer>
                  dhcp6-prefix-hint-vlt: <value of integer>
                  dhcp6-relay-ip: <value of string>
                  dhcp6-relay-service: <value in [disable, enable]>
                  dhcp6-relay-type: <value in [regular]>
                  ip6-address: <value of string>
                  ip6-allowaccess:
                    - <value in [https, ping, ssh, ...]>
                  ip6-default-life: <value of integer>
                  ip6-dns-server-override: <value in [disable, enable]>
                  ip6-hop-limit: <value of integer>
                  ip6-link-mtu: <value of integer>
                  ip6-manage-flag: <value in [disable, enable]>
                  ip6-max-interval: <value of integer>
                  ip6-min-interval: <value of integer>
                  ip6-mode: <value in [static, dhcp, pppoe, ...]>
                  ip6-other-flag: <value in [disable, enable]>
                  ip6-reachable-time: <value of integer>
                  ip6-retrans-time: <value of integer>
                  ip6-send-adv: <value in [disable, enable]>
                  ip6-subnet: <value of string>
                  ip6-upstream-interface: <value of string>
                  nd-cert: <value of string>
                  nd-cga-modifier: <value of string>
                  nd-mode: <value in [basic, SEND-compatible]>
                  nd-security-level: <value of integer>
                  nd-timestamp-delta: <value of integer>
                  nd-timestamp-fuzz: <value of integer>
                  vrip6_link_local: <value of string>
                  vrrp-virtual-mac6: <value in [disable, enable]>

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
            autoconf:
               type: str
            dhcp6-client-options:
               type: array
               suboptions:
                  type: str
            dhcp6-information-request:
               type: str
            dhcp6-prefix-delegation:
               type: str
            dhcp6-prefix-hint:
               type: str
            dhcp6-prefix-hint-plt:
               type: int
            dhcp6-prefix-hint-vlt:
               type: int
            dhcp6-relay-ip:
               type: str
            dhcp6-relay-service:
               type: str
            dhcp6-relay-type:
               type: str
            ip6-address:
               type: str
            ip6-allowaccess:
               type: array
               suboptions:
                  type: str
            ip6-default-life:
               type: int
            ip6-dns-server-override:
               type: str
            ip6-hop-limit:
               type: int
            ip6-link-mtu:
               type: int
            ip6-manage-flag:
               type: str
            ip6-max-interval:
               type: int
            ip6-min-interval:
               type: int
            ip6-mode:
               type: str
            ip6-other-flag:
               type: str
            ip6-reachable-time:
               type: int
            ip6-retrans-time:
               type: int
            ip6-send-adv:
               type: str
            ip6-subnet:
               type: str
            ip6-upstream-interface:
               type: str
            nd-cert:
               type: str
            nd-cga-modifier:
               type: str
            nd-mode:
               type: str
            nd-security-level:
               type: int
            nd-timestamp-delta:
               type: int
            nd-timestamp-fuzz:
               type: int
            vrip6_link_local:
               type: str
            vrrp-virtual-mac6:
               type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/interface/ipv6'
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
            example: '/pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/interface/ipv6'

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
        '/pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/interface/ipv6',
        '/pm/config/global/obj/fsp/vlan/{vlan}/interface/ipv6'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'vlan',
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
                        'autoconf': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dhcp6-client-options': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'rapid',
                                    'iapd',
                                    'iana',
                                    'dns',
                                    'dnsname'
                                ]
                            }
                        },
                        'dhcp6-information-request': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dhcp6-prefix-delegation': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dhcp6-prefix-hint': {
                            'type': 'string'
                        },
                        'dhcp6-prefix-hint-plt': {
                            'type': 'integer'
                        },
                        'dhcp6-prefix-hint-vlt': {
                            'type': 'integer'
                        },
                        'dhcp6-relay-ip': {
                            'type': 'string'
                        },
                        'dhcp6-relay-service': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dhcp6-relay-type': {
                            'type': 'string',
                            'enum': [
                                'regular'
                            ]
                        },
                        'ip6-address': {
                            'type': 'string'
                        },
                        'ip6-allowaccess': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'https',
                                    'ping',
                                    'ssh',
                                    'snmp',
                                    'http',
                                    'telnet',
                                    'fgfm',
                                    'capwap'
                                ]
                            }
                        },
                        'ip6-default-life': {
                            'type': 'integer'
                        },
                        'ip6-dns-server-override': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ip6-hop-limit': {
                            'type': 'integer'
                        },
                        'ip6-link-mtu': {
                            'type': 'integer'
                        },
                        'ip6-manage-flag': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ip6-max-interval': {
                            'type': 'integer'
                        },
                        'ip6-min-interval': {
                            'type': 'integer'
                        },
                        'ip6-mode': {
                            'type': 'string',
                            'enum': [
                                'static',
                                'dhcp',
                                'pppoe',
                                'delegated'
                            ]
                        },
                        'ip6-other-flag': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ip6-reachable-time': {
                            'type': 'integer'
                        },
                        'ip6-retrans-time': {
                            'type': 'integer'
                        },
                        'ip6-send-adv': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ip6-subnet': {
                            'type': 'string'
                        },
                        'ip6-upstream-interface': {
                            'type': 'string'
                        },
                        'nd-cert': {
                            'type': 'string'
                        },
                        'nd-cga-modifier': {
                            'type': 'string'
                        },
                        'nd-mode': {
                            'type': 'string',
                            'enum': [
                                'basic',
                                'SEND-compatible'
                            ]
                        },
                        'nd-security-level': {
                            'type': 'integer'
                        },
                        'nd-timestamp-delta': {
                            'type': 'integer'
                        },
                        'nd-timestamp-fuzz': {
                            'type': 'integer'
                        },
                        'vrip6_link_local': {
                            'type': 'string'
                        },
                        'vrrp-virtual-mac6': {
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
