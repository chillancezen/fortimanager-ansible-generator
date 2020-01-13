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
module: fmgr_fsp_vlan_dynamicmapping_dhcpserver
short_description: no description
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/dynamic_mapping/{dynamic_mapping}/dhcp-server
    - /pm/config/global/obj/fsp/vlan/{vlan}/dynamic_mapping/{dynamic_mapping}/dhcp-server
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
            dynamic_mapping:
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
                auto-configuration:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                conflicted-ip-timeout:
                    type: int
                ddns-auth:
                    type: str
                    choices:
                        - 'disable'
                        - 'tsig'
                ddns-key:
                    type: str
                ddns-keyname:
                    type: str
                ddns-server-ip:
                    type: str
                ddns-ttl:
                    type: int
                ddns-update:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ddns-update-override:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ddns-zone:
                    type: str
                default-gateway:
                    type: str
                dns-server1:
                    type: str
                dns-server2:
                    type: str
                dns-server3:
                    type: str
                dns-service:
                    type: str
                    choices:
                        - 'default'
                        - 'specify'
                        - 'local'
                domain:
                    type: str
                enable:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                exclude-range:
                    -
                        end-ip:
                            type: str
                        id:
                            type: int
                        start-ip:
                            type: str
                filename:
                    type: str
                forticlient-on-net-status:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                id:
                    type: int
                interface:
                    type: str
                ip-mode:
                    type: str
                    choices:
                        - 'range'
                        - 'usrgrp'
                ip-range:
                    -
                        end-ip:
                            type: str
                        id:
                            type: int
                        start-ip:
                            type: str
                ipsec-lease-hold:
                    type: int
                lease-time:
                    type: int
                mac-acl-default-action:
                    type: str
                    choices:
                        - 'assign'
                        - 'block'
                netmask:
                    type: str
                next-server:
                    type: str
                ntp-server1:
                    type: str
                ntp-server2:
                    type: str
                ntp-server3:
                    type: str
                ntp-service:
                    type: str
                    choices:
                        - 'default'
                        - 'specify'
                        - 'local'
                option1:
                    -
                        type: str
                option2:
                    -
                        type: str
                option3:
                    -
                        type: str
                option4:
                    type: str
                option5:
                    type: str
                option6:
                    type: str
                options:
                    -
                        code:
                            type: int
                        id:
                            type: int
                        ip:
                            -
                                type: str
                        type:
                            type: str
                            choices:
                                - 'hex'
                                - 'string'
                                - 'ip'
                                - 'fqdn'
                        value:
                            type: str
                reserved-address:
                    -
                        action:
                            type: str
                            choices:
                                - 'assign'
                                - 'block'
                                - 'reserved'
                        circuit-id:
                            type: str
                        circuit-id-type:
                            type: str
                            choices:
                                - 'hex'
                                - 'string'
                        description:
                            type: str
                        id:
                            type: int
                        ip:
                            type: str
                        mac:
                            type: str
                        remote-id:
                            type: str
                        remote-id-type:
                            type: str
                            choices:
                                - 'hex'
                                - 'string'
                        type:
                            type: str
                            choices:
                                - 'mac'
                                - 'option82'
                server-type:
                    type: str
                    choices:
                        - 'regular'
                        - 'ipsec'
                status:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                tftp-server:
                    -
                        type: str
                timezone:
                    type: str
                    choices:
                        - '00'
                        - '01'
                        - '02'
                        - '03'
                        - '04'
                        - '05'
                        - '06'
                        - '07'
                        - '08'
                        - '09'
                        - '10'
                        - '11'
                        - '12'
                        - '13'
                        - '14'
                        - '15'
                        - '16'
                        - '17'
                        - '18'
                        - '19'
                        - '20'
                        - '21'
                        - '22'
                        - '23'
                        - '24'
                        - '25'
                        - '26'
                        - '27'
                        - '28'
                        - '29'
                        - '30'
                        - '31'
                        - '32'
                        - '33'
                        - '34'
                        - '35'
                        - '36'
                        - '37'
                        - '38'
                        - '39'
                        - '40'
                        - '41'
                        - '42'
                        - '43'
                        - '44'
                        - '45'
                        - '46'
                        - '47'
                        - '48'
                        - '49'
                        - '50'
                        - '51'
                        - '52'
                        - '53'
                        - '54'
                        - '55'
                        - '56'
                        - '57'
                        - '58'
                        - '59'
                        - '60'
                        - '61'
                        - '62'
                        - '63'
                        - '64'
                        - '65'
                        - '66'
                        - '67'
                        - '68'
                        - '69'
                        - '70'
                        - '71'
                        - '72'
                        - '73'
                        - '74'
                        - '75'
                        - '76'
                        - '77'
                        - '78'
                        - '79'
                        - '80'
                        - '81'
                        - '82'
                        - '83'
                        - '84'
                        - '85'
                        - '86'
                        - '87'
                timezone-option:
                    type: str
                    choices:
                        - 'disable'
                        - 'default'
                        - 'specify'
                vci-match:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                vci-string:
                    -
                        type: str
                wifi-ac1:
                    type: str
                wifi-ac2:
                    type: str
                wifi-ac3:
                    type: str
                wins-server1:
                    type: str
                wins-server2:
                    type: str

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/FSP/VLAN/{VLAN}/DYNAMIC_MAPPING/{DYNAMIC_MAPPING}/DHCP-SERVER
      fmgr_fsp_vlan_dynamicmapping_dhcpserver:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vlan: <value of string>
            dynamic_mapping: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/FSP/VLAN/{VLAN}/DYNAMIC_MAPPING/{DYNAMIC_MAPPING}/DHCP-SERVER
      fmgr_fsp_vlan_dynamicmapping_dhcpserver:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vlan: <value of string>
            dynamic_mapping: <value of string>
         params:
            -
               data:
                  auto-configuration: <value in [disable, enable]>
                  conflicted-ip-timeout: <value of integer>
                  ddns-auth: <value in [disable, tsig]>
                  ddns-key: <value of string>
                  ddns-keyname: <value of string>
                  ddns-server-ip: <value of string>
                  ddns-ttl: <value of integer>
                  ddns-update: <value in [disable, enable]>
                  ddns-update-override: <value in [disable, enable]>
                  ddns-zone: <value of string>
                  default-gateway: <value of string>
                  dns-server1: <value of string>
                  dns-server2: <value of string>
                  dns-server3: <value of string>
                  dns-service: <value in [default, specify, local]>
                  domain: <value of string>
                  enable: <value in [disable, enable]>
                  exclude-range:
                    -
                        end-ip: <value of string>
                        id: <value of integer>
                        start-ip: <value of string>
                  filename: <value of string>
                  forticlient-on-net-status: <value in [disable, enable]>
                  id: <value of integer>
                  interface: <value of string>
                  ip-mode: <value in [range, usrgrp]>
                  ip-range:
                    -
                        end-ip: <value of string>
                        id: <value of integer>
                        start-ip: <value of string>
                  ipsec-lease-hold: <value of integer>
                  lease-time: <value of integer>
                  mac-acl-default-action: <value in [assign, block]>
                  netmask: <value of string>
                  next-server: <value of string>
                  ntp-server1: <value of string>
                  ntp-server2: <value of string>
                  ntp-server3: <value of string>
                  ntp-service: <value in [default, specify, local]>
                  option1:
                    - <value of string>
                  option2:
                    - <value of string>
                  option3:
                    - <value of string>
                  option4: <value of string>
                  option5: <value of string>
                  option6: <value of string>
                  options:
                    -
                        code: <value of integer>
                        id: <value of integer>
                        ip:
                          - <value of string>
                        type: <value in [hex, string, ip, ...]>
                        value: <value of string>
                  reserved-address:
                    -
                        action: <value in [assign, block, reserved]>
                        circuit-id: <value of string>
                        circuit-id-type: <value in [hex, string]>
                        description: <value of string>
                        id: <value of integer>
                        ip: <value of string>
                        mac: <value of string>
                        remote-id: <value of string>
                        remote-id-type: <value in [hex, string]>
                        type: <value in [mac, option82]>
                  server-type: <value in [regular, ipsec]>
                  status: <value in [disable, enable]>
                  tftp-server:
                    - <value of string>
                  timezone: <value in [00, 01, 02, ...]>
                  timezone-option: <value in [disable, default, specify]>
                  vci-match: <value in [disable, enable]>
                  vci-string:
                    - <value of string>
                  wifi-ac1: <value of string>
                  wifi-ac2: <value of string>
                  wifi-ac3: <value of string>
                  wins-server1: <value of string>
                  wins-server2: <value of string>

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
            auto-configuration:
               type: str
            conflicted-ip-timeout:
               type: int
            ddns-auth:
               type: str
            ddns-key:
               type: str
            ddns-keyname:
               type: str
            ddns-server-ip:
               type: str
            ddns-ttl:
               type: int
            ddns-update:
               type: str
            ddns-update-override:
               type: str
            ddns-zone:
               type: str
            default-gateway:
               type: str
            dns-server1:
               type: str
            dns-server2:
               type: str
            dns-server3:
               type: str
            dns-service:
               type: str
            domain:
               type: str
            enable:
               type: str
            exclude-range:
               type: array
               suboptions:
                  end-ip:
                     type: str
                  id:
                     type: int
                  start-ip:
                     type: str
            filename:
               type: str
            forticlient-on-net-status:
               type: str
            id:
               type: int
            interface:
               type: str
            ip-mode:
               type: str
            ip-range:
               type: array
               suboptions:
                  end-ip:
                     type: str
                  id:
                     type: int
                  start-ip:
                     type: str
            ipsec-lease-hold:
               type: int
            lease-time:
               type: int
            mac-acl-default-action:
               type: str
            netmask:
               type: str
            next-server:
               type: str
            ntp-server1:
               type: str
            ntp-server2:
               type: str
            ntp-server3:
               type: str
            ntp-service:
               type: str
            option1:
               type: array
               suboptions:
                  type: str
            option2:
               type: array
               suboptions:
                  type: str
            option3:
               type: array
               suboptions:
                  type: str
            option4:
               type: str
            option5:
               type: str
            option6:
               type: str
            options:
               type: array
               suboptions:
                  code:
                     type: int
                  id:
                     type: int
                  ip:
                     type: array
                     suboptions:
                        type: str
                  type:
                     type: str
                  value:
                     type: str
            reserved-address:
               type: array
               suboptions:
                  action:
                     type: str
                  circuit-id:
                     type: str
                  circuit-id-type:
                     type: str
                  description:
                     type: str
                  id:
                     type: int
                  ip:
                     type: str
                  mac:
                     type: str
                  remote-id:
                     type: str
                  remote-id-type:
                     type: str
                  type:
                     type: str
            server-type:
               type: str
            status:
               type: str
            tftp-server:
               type: array
               suboptions:
                  type: str
            timezone:
               type: str
            timezone-option:
               type: str
            vci-match:
               type: str
            vci-string:
               type: array
               suboptions:
                  type: str
            wifi-ac1:
               type: str
            wifi-ac2:
               type: str
            wifi-ac3:
               type: str
            wins-server1:
               type: str
            wins-server2:
               type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/dynamic_mapping/{dynamic_mapping}...'
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
            example: '/pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/dynamic_mapping/{dynamic_mapping}...'

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
        '/pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/dynamic_mapping/{dynamic_mapping}/dhcp-server',
        '/pm/config/global/obj/fsp/vlan/{vlan}/dynamic_mapping/{dynamic_mapping}/dhcp-server'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'vlan',
            'type': 'string'
        },
        {
            'name': 'dynamic_mapping',
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
                        'auto-configuration': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'conflicted-ip-timeout': {
                            'type': 'integer'
                        },
                        'ddns-auth': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'tsig'
                            ]
                        },
                        'ddns-key': {
                            'type': 'string'
                        },
                        'ddns-keyname': {
                            'type': 'string'
                        },
                        'ddns-server-ip': {
                            'type': 'string'
                        },
                        'ddns-ttl': {
                            'type': 'integer'
                        },
                        'ddns-update': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ddns-update-override': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ddns-zone': {
                            'type': 'string'
                        },
                        'default-gateway': {
                            'type': 'string'
                        },
                        'dns-server1': {
                            'type': 'string'
                        },
                        'dns-server2': {
                            'type': 'string'
                        },
                        'dns-server3': {
                            'type': 'string'
                        },
                        'dns-service': {
                            'type': 'string',
                            'enum': [
                                'default',
                                'specify',
                                'local'
                            ]
                        },
                        'domain': {
                            'type': 'string'
                        },
                        'enable': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'exclude-range': {
                            'type': 'array',
                            'items': {
                                'end-ip': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'start-ip': {
                                    'type': 'string'
                                }
                            }
                        },
                        'filename': {
                            'type': 'string'
                        },
                        'forticlient-on-net-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'id': {
                            'type': 'integer'
                        },
                        'interface': {
                            'type': 'string'
                        },
                        'ip-mode': {
                            'type': 'string',
                            'enum': [
                                'range',
                                'usrgrp'
                            ]
                        },
                        'ip-range': {
                            'type': 'array',
                            'items': {
                                'end-ip': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'start-ip': {
                                    'type': 'string'
                                }
                            }
                        },
                        'ipsec-lease-hold': {
                            'type': 'integer'
                        },
                        'lease-time': {
                            'type': 'integer'
                        },
                        'mac-acl-default-action': {
                            'type': 'string',
                            'enum': [
                                'assign',
                                'block'
                            ]
                        },
                        'netmask': {
                            'type': 'string'
                        },
                        'next-server': {
                            'type': 'string'
                        },
                        'ntp-server1': {
                            'type': 'string'
                        },
                        'ntp-server2': {
                            'type': 'string'
                        },
                        'ntp-server3': {
                            'type': 'string'
                        },
                        'ntp-service': {
                            'type': 'string',
                            'enum': [
                                'default',
                                'specify',
                                'local'
                            ]
                        },
                        'option1': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'option2': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'option3': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'option4': {
                            'type': 'string'
                        },
                        'option5': {
                            'type': 'string'
                        },
                        'option6': {
                            'type': 'string'
                        },
                        'options': {
                            'type': 'array',
                            'items': {
                                'code': {
                                    'type': 'integer'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'ip': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                },
                                'type': {
                                    'type': 'string',
                                    'enum': [
                                        'hex',
                                        'string',
                                        'ip',
                                        'fqdn'
                                    ]
                                },
                                'value': {
                                    'type': 'string'
                                }
                            }
                        },
                        'reserved-address': {
                            'type': 'array',
                            'items': {
                                'action': {
                                    'type': 'string',
                                    'enum': [
                                        'assign',
                                        'block',
                                        'reserved'
                                    ]
                                },
                                'circuit-id': {
                                    'type': 'string'
                                },
                                'circuit-id-type': {
                                    'type': 'string',
                                    'enum': [
                                        'hex',
                                        'string'
                                    ]
                                },
                                'description': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'ip': {
                                    'type': 'string'
                                },
                                'mac': {
                                    'type': 'string'
                                },
                                'remote-id': {
                                    'type': 'string'
                                },
                                'remote-id-type': {
                                    'type': 'string',
                                    'enum': [
                                        'hex',
                                        'string'
                                    ]
                                },
                                'type': {
                                    'type': 'string',
                                    'enum': [
                                        'mac',
                                        'option82'
                                    ]
                                }
                            }
                        },
                        'server-type': {
                            'type': 'string',
                            'enum': [
                                'regular',
                                'ipsec'
                            ]
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'tftp-server': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'timezone': {
                            'type': 'string',
                            'enum': [
                                '00',
                                '01',
                                '02',
                                '03',
                                '04',
                                '05',
                                '06',
                                '07',
                                '08',
                                '09',
                                '10',
                                '11',
                                '12',
                                '13',
                                '14',
                                '15',
                                '16',
                                '17',
                                '18',
                                '19',
                                '20',
                                '21',
                                '22',
                                '23',
                                '24',
                                '25',
                                '26',
                                '27',
                                '28',
                                '29',
                                '30',
                                '31',
                                '32',
                                '33',
                                '34',
                                '35',
                                '36',
                                '37',
                                '38',
                                '39',
                                '40',
                                '41',
                                '42',
                                '43',
                                '44',
                                '45',
                                '46',
                                '47',
                                '48',
                                '49',
                                '50',
                                '51',
                                '52',
                                '53',
                                '54',
                                '55',
                                '56',
                                '57',
                                '58',
                                '59',
                                '60',
                                '61',
                                '62',
                                '63',
                                '64',
                                '65',
                                '66',
                                '67',
                                '68',
                                '69',
                                '70',
                                '71',
                                '72',
                                '73',
                                '74',
                                '75',
                                '76',
                                '77',
                                '78',
                                '79',
                                '80',
                                '81',
                                '82',
                                '83',
                                '84',
                                '85',
                                '86',
                                '87'
                            ]
                        },
                        'timezone-option': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'default',
                                'specify'
                            ]
                        },
                        'vci-match': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'vci-string': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'wifi-ac1': {
                            'type': 'string'
                        },
                        'wifi-ac2': {
                            'type': 'string'
                        },
                        'wifi-ac3': {
                            'type': 'string'
                        },
                        'wins-server1': {
                            'type': 'string'
                        },
                        'wins-server2': {
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
