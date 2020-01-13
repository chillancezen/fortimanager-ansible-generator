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
module: fmgr_wtpprofile_obj
short_description: Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}
    - /pm/config/global/obj/wireless-controller/wtp-profile/{wtp-profile}
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
            wtp-profile:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                allowaccess:
                    -
                        type: str
                        choices:
                            - 'https'
                            - 'ssh'
                            - 'snmp'
                            - 'http'
                            - 'telnet'
                ap-country:
                    type: str
                    description: 'Country in which this WTP, FortiAP or AP will operate (default = NA, automatically use the country configured for the curr...'
                    choices:
                        - 'AL'
                        - 'DZ'
                        - 'AR'
                        - 'AM'
                        - 'AU'
                        - 'AT'
                        - 'AZ'
                        - 'BH'
                        - 'BD'
                        - 'BY'
                        - 'BE'
                        - 'BZ'
                        - 'BO'
                        - 'BA'
                        - 'BR'
                        - 'BN'
                        - 'BG'
                        - 'CA'
                        - 'CL'
                        - 'CN'
                        - 'CO'
                        - 'CR'
                        - 'HR'
                        - 'CY'
                        - 'CZ'
                        - 'DK'
                        - 'DO'
                        - 'EC'
                        - 'EG'
                        - 'SV'
                        - 'EE'
                        - 'FI'
                        - 'FR'
                        - 'GE'
                        - 'DE'
                        - 'GR'
                        - 'GT'
                        - 'HN'
                        - 'HK'
                        - 'HU'
                        - 'IS'
                        - 'IN'
                        - 'ID'
                        - 'IR'
                        - 'IE'
                        - 'IL'
                        - 'IT'
                        - 'JM'
                        - 'JP'
                        - 'JO'
                        - 'KZ'
                        - 'KE'
                        - 'KP'
                        - 'KR'
                        - 'KW'
                        - 'LV'
                        - 'LB'
                        - 'LI'
                        - 'LT'
                        - 'LU'
                        - 'MO'
                        - 'MK'
                        - 'MY'
                        - 'MT'
                        - 'MX'
                        - 'MC'
                        - 'MA'
                        - 'NP'
                        - 'NL'
                        - 'AN'
                        - 'NZ'
                        - 'NO'
                        - 'OM'
                        - 'PK'
                        - 'PA'
                        - 'PG'
                        - 'PE'
                        - 'PH'
                        - 'PL'
                        - 'PT'
                        - 'PR'
                        - 'QA'
                        - 'RO'
                        - 'RU'
                        - 'SA'
                        - 'SG'
                        - 'SK'
                        - 'SI'
                        - 'ZA'
                        - 'ES'
                        - 'LK'
                        - 'SE'
                        - 'CH'
                        - 'SY'
                        - 'TW'
                        - 'TH'
                        - 'TT'
                        - 'TN'
                        - 'TR'
                        - 'AE'
                        - 'UA'
                        - 'GB'
                        - 'US'
                        - 'PS'
                        - 'UY'
                        - 'UZ'
                        - 'VE'
                        - 'VN'
                        - 'YE'
                        - 'ZW'
                        - 'NA'
                        - 'KH'
                        - 'TZ'
                        - 'SD'
                        - 'AO'
                        - 'RW'
                        - 'MZ'
                        - 'RS'
                        - 'ME'
                        - 'BB'
                        - 'GD'
                        - 'GL'
                        - 'GU'
                        - 'PY'
                        - 'HT'
                        - 'AW'
                        - 'MM'
                        - 'ZB'
                ble-profile:
                    type: str
                    description: 'Bluetooth Low Energy profile name.'
                comment:
                    type: str
                    description: 'Comment.'
                control-message-offload:
                    -
                        type: str
                        choices:
                            - 'ebp-frame'
                            - 'aeroscout-tag'
                            - 'ap-list'
                            - 'sta-list'
                            - 'sta-cap-list'
                            - 'stats'
                            - 'aeroscout-mu'
                            - 'sta-health'
                deny-mac-list:
                    -
                        id:
                            type: int
                            description: 'ID.'
                        mac:
                            type: str
                            description: 'A WiFi device with this MAC address is denied access to this WTP, FortiAP or AP.'
                dtls-in-kernel:
                    type: str
                    description: 'Enable/disable data channel DTLS in kernel.'
                    choices:
                        - 'disable'
                        - 'enable'
                dtls-policy:
                    -
                        type: str
                        choices:
                            - 'clear-text'
                            - 'dtls-enabled'
                            - 'ipsec-vpn'
                energy-efficient-ethernet:
                    type: str
                    description: 'Enable/disable use of energy efficient Ethernet on WTP.'
                    choices:
                        - 'disable'
                        - 'enable'
                ext-info-enable:
                    type: str
                    description: 'Enable/disable station/VAP/radio extension information.'
                    choices:
                        - 'disable'
                        - 'enable'
                handoff-roaming:
                    type: str
                    description: 'Enable/disable client load balancing during roaming to avoid roaming delay (default = disable).'
                    choices:
                        - 'disable'
                        - 'enable'
                handoff-rssi:
                    type: int
                    description: 'Minimum received signal strength indicator (RSSI) value for handoff (20 - 30, default = 25).'
                handoff-sta-thresh:
                    type: int
                    description: 'Threshold value for AP handoff.'
                ip-fragment-preventing:
                    -
                        type: str
                        choices:
                            - 'tcp-mss-adjust'
                            - 'icmp-unreachable'
                led-schedules:
                    type: str
                    description: 'Recurring firewall schedules for illuminating LEDs on the FortiAP. If led-state is enabled, LEDs will be visible when at l...'
                led-state:
                    type: str
                    description: 'Enable/disable use of LEDs on WTP (default = disable).'
                    choices:
                        - 'disable'
                        - 'enable'
                lldp:
                    type: str
                    description: 'Enable/disable Link Layer Discovery Protocol (LLDP) for the WTP, FortiAP, or AP (default = disable).'
                    choices:
                        - 'disable'
                        - 'enable'
                login-passwd:
                    -
                        type: str
                login-passwd-change:
                    type: str
                    description: 'Change or reset the administrator password of a managed WTP, FortiAP or AP (yes, default, or no, default = no).'
                    choices:
                        - 'no'
                        - 'yes'
                        - 'default'
                max-clients:
                    type: int
                    description: 'Maximum number of stations (STAs) supported by the WTP (default = 0, meaning no client limitation).'
                name:
                    type: str
                    description: 'WTP (or FortiAP or AP) profile name.'
                poe-mode:
                    type: str
                    description: 'Set the WTP, FortiAP, or APs PoE mode.'
                    choices:
                        - 'auto'
                        - '8023af'
                        - '8023at'
                        - 'power-adapter'
                split-tunneling-acl:
                    -
                        dest-ip:
                            type: str
                            description: 'Destination IP and mask for the split-tunneling subnet.'
                        id:
                            type: int
                            description: 'ID.'
                split-tunneling-acl-local-ap-subnet:
                    type: str
                    description: 'Enable/disable automatically adding local subnetwork of FortiAP to split-tunneling ACL (default = disable).'
                    choices:
                        - 'disable'
                        - 'enable'
                split-tunneling-acl-path:
                    type: str
                    description: 'Split tunneling ACL path is local/tunnel.'
                    choices:
                        - 'tunnel'
                        - 'local'
                tun-mtu-downlink:
                    type: int
                    description: 'Downlink CAPWAP tunnel MTU (0, 576, or 1500 bytes, default = 0).'
                tun-mtu-uplink:
                    type: int
                    description: 'Uplink CAPWAP tunnel MTU (0, 576, or 1500 bytes, default = 0).'
                wan-port-mode:
                    type: str
                    description: 'Enable/disable using a WAN port as a LAN port.'
                    choices:
                        - 'wan-lan'
                        - 'wan-only'
    schema_object1:
        methods: [delete]
        description: 'Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.'
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

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WTP-PROFILE/{WTP-PROFILE}
      fmgr_wtpprofile_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wtp-profile: <value of string>
         params:
            -
               data:
                  allowaccess:
                    - <value in [https, ssh, snmp, ...]>
                  ap-country: <value in [AL, DZ, AR, ...]>
                  ble-profile: <value of string>
                  comment: <value of string>
                  control-message-offload:
                    - <value in [ebp-frame, aeroscout-tag, ap-list, ...]>
                  deny-mac-list:
                    -
                        id: <value of integer>
                        mac: <value of string>
                  dtls-in-kernel: <value in [disable, enable]>
                  dtls-policy:
                    - <value in [clear-text, dtls-enabled, ipsec-vpn]>
                  energy-efficient-ethernet: <value in [disable, enable]>
                  ext-info-enable: <value in [disable, enable]>
                  handoff-roaming: <value in [disable, enable]>
                  handoff-rssi: <value of integer>
                  handoff-sta-thresh: <value of integer>
                  ip-fragment-preventing:
                    - <value in [tcp-mss-adjust, icmp-unreachable]>
                  led-schedules: <value of string>
                  led-state: <value in [disable, enable]>
                  lldp: <value in [disable, enable]>
                  login-passwd:
                    - <value of string>
                  login-passwd-change: <value in [no, yes, default]>
                  max-clients: <value of integer>
                  name: <value of string>
                  poe-mode: <value in [auto, 8023af, 8023at, ...]>
                  split-tunneling-acl:
                    -
                        dest-ip: <value of string>
                        id: <value of integer>
                  split-tunneling-acl-local-ap-subnet: <value in [disable, enable]>
                  split-tunneling-acl-path: <value in [tunnel, local]>
                  tun-mtu-downlink: <value of integer>
                  tun-mtu-uplink: <value of integer>
                  wan-port-mode: <value in [wan-lan, wan-only]>

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WTP-PROFILE/{WTP-PROFILE}
      fmgr_wtpprofile_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wtp-profile: <value of string>
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
            example: '/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            allowaccess:
               type: array
               suboptions:
                  type: str
            ap-country:
               type: str
               description: 'Country in which this WTP, FortiAP or AP will operate (default = NA, automatically use the country configured for the current V...'
            ble-profile:
               type: str
               description: 'Bluetooth Low Energy profile name.'
            comment:
               type: str
               description: 'Comment.'
            control-message-offload:
               type: array
               suboptions:
                  type: str
            deny-mac-list:
               type: array
               suboptions:
                  id:
                     type: int
                     description: 'ID.'
                  mac:
                     type: str
                     description: 'A WiFi device with this MAC address is denied access to this WTP, FortiAP or AP.'
            dtls-in-kernel:
               type: str
               description: 'Enable/disable data channel DTLS in kernel.'
            dtls-policy:
               type: array
               suboptions:
                  type: str
            energy-efficient-ethernet:
               type: str
               description: 'Enable/disable use of energy efficient Ethernet on WTP.'
            ext-info-enable:
               type: str
               description: 'Enable/disable station/VAP/radio extension information.'
            handoff-roaming:
               type: str
               description: 'Enable/disable client load balancing during roaming to avoid roaming delay (default = disable).'
            handoff-rssi:
               type: int
               description: 'Minimum received signal strength indicator (RSSI) value for handoff (20 - 30, default = 25).'
            handoff-sta-thresh:
               type: int
               description: 'Threshold value for AP handoff.'
            ip-fragment-preventing:
               type: array
               suboptions:
                  type: str
            led-schedules:
               type: str
               description: 'Recurring firewall schedules for illuminating LEDs on the FortiAP. If led-state is enabled, LEDs will be visible when at least ...'
            led-state:
               type: str
               description: 'Enable/disable use of LEDs on WTP (default = disable).'
            lldp:
               type: str
               description: 'Enable/disable Link Layer Discovery Protocol (LLDP) for the WTP, FortiAP, or AP (default = disable).'
            login-passwd:
               type: array
               suboptions:
                  type: str
            login-passwd-change:
               type: str
               description: 'Change or reset the administrator password of a managed WTP, FortiAP or AP (yes, default, or no, default = no).'
            max-clients:
               type: int
               description: 'Maximum number of stations (STAs) supported by the WTP (default = 0, meaning no client limitation).'
            name:
               type: str
               description: 'WTP (or FortiAP or AP) profile name.'
            poe-mode:
               type: str
               description: 'Set the WTP, FortiAP, or APs PoE mode.'
            split-tunneling-acl:
               type: array
               suboptions:
                  dest-ip:
                     type: str
                     description: 'Destination IP and mask for the split-tunneling subnet.'
                  id:
                     type: int
                     description: 'ID.'
            split-tunneling-acl-local-ap-subnet:
               type: str
               description: 'Enable/disable automatically adding local subnetwork of FortiAP to split-tunneling ACL (default = disable).'
            split-tunneling-acl-path:
               type: str
               description: 'Split tunneling ACL path is local/tunnel.'
            tun-mtu-downlink:
               type: int
               description: 'Downlink CAPWAP tunnel MTU (0, 576, or 1500 bytes, default = 0).'
            tun-mtu-uplink:
               type: int
               description: 'Uplink CAPWAP tunnel MTU (0, 576, or 1500 bytes, default = 0).'
            wan-port-mode:
               type: str
               description: 'Enable/disable using a WAN port as a LAN port.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}'

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
        '/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}',
        '/pm/config/global/obj/wireless-controller/wtp-profile/{wtp-profile}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'wtp-profile',
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
                        'allowaccess': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'https',
                                    'ssh',
                                    'snmp',
                                    'http',
                                    'telnet'
                                ]
                            }
                        },
                        'ap-country': {
                            'type': 'string',
                            'enum': [
                                'AL',
                                'DZ',
                                'AR',
                                'AM',
                                'AU',
                                'AT',
                                'AZ',
                                'BH',
                                'BD',
                                'BY',
                                'BE',
                                'BZ',
                                'BO',
                                'BA',
                                'BR',
                                'BN',
                                'BG',
                                'CA',
                                'CL',
                                'CN',
                                'CO',
                                'CR',
                                'HR',
                                'CY',
                                'CZ',
                                'DK',
                                'DO',
                                'EC',
                                'EG',
                                'SV',
                                'EE',
                                'FI',
                                'FR',
                                'GE',
                                'DE',
                                'GR',
                                'GT',
                                'HN',
                                'HK',
                                'HU',
                                'IS',
                                'IN',
                                'ID',
                                'IR',
                                'IE',
                                'IL',
                                'IT',
                                'JM',
                                'JP',
                                'JO',
                                'KZ',
                                'KE',
                                'KP',
                                'KR',
                                'KW',
                                'LV',
                                'LB',
                                'LI',
                                'LT',
                                'LU',
                                'MO',
                                'MK',
                                'MY',
                                'MT',
                                'MX',
                                'MC',
                                'MA',
                                'NP',
                                'NL',
                                'AN',
                                'NZ',
                                'NO',
                                'OM',
                                'PK',
                                'PA',
                                'PG',
                                'PE',
                                'PH',
                                'PL',
                                'PT',
                                'PR',
                                'QA',
                                'RO',
                                'RU',
                                'SA',
                                'SG',
                                'SK',
                                'SI',
                                'ZA',
                                'ES',
                                'LK',
                                'SE',
                                'CH',
                                'SY',
                                'TW',
                                'TH',
                                'TT',
                                'TN',
                                'TR',
                                'AE',
                                'UA',
                                'GB',
                                'US',
                                'PS',
                                'UY',
                                'UZ',
                                'VE',
                                'VN',
                                'YE',
                                'ZW',
                                'NA',
                                'KH',
                                'TZ',
                                'SD',
                                'AO',
                                'RW',
                                'MZ',
                                'RS',
                                'ME',
                                'BB',
                                'GD',
                                'GL',
                                'GU',
                                'PY',
                                'HT',
                                'AW',
                                'MM',
                                'ZB'
                            ]
                        },
                        'ble-profile': {
                            'type': 'string'
                        },
                        'comment': {
                            'type': 'string'
                        },
                        'control-message-offload': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'ebp-frame',
                                    'aeroscout-tag',
                                    'ap-list',
                                    'sta-list',
                                    'sta-cap-list',
                                    'stats',
                                    'aeroscout-mu',
                                    'sta-health'
                                ]
                            }
                        },
                        'deny-mac-list': {
                            'type': 'array',
                            'items': {
                                'id': {
                                    'type': 'integer'
                                },
                                'mac': {
                                    'type': 'string'
                                }
                            }
                        },
                        'dtls-in-kernel': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dtls-policy': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'clear-text',
                                    'dtls-enabled',
                                    'ipsec-vpn'
                                ]
                            }
                        },
                        'energy-efficient-ethernet': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ext-info-enable': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'handoff-roaming': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'handoff-rssi': {
                            'type': 'integer'
                        },
                        'handoff-sta-thresh': {
                            'type': 'integer'
                        },
                        'ip-fragment-preventing': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'tcp-mss-adjust',
                                    'icmp-unreachable'
                                ]
                            }
                        },
                        'led-schedules': {
                            'type': 'string'
                        },
                        'led-state': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'lldp': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'login-passwd': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'login-passwd-change': {
                            'type': 'string',
                            'enum': [
                                'no',
                                'yes',
                                'default'
                            ]
                        },
                        'max-clients': {
                            'type': 'integer'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'poe-mode': {
                            'type': 'string',
                            'enum': [
                                'auto',
                                '8023af',
                                '8023at',
                                'power-adapter'
                            ]
                        },
                        'split-tunneling-acl': {
                            'type': 'array',
                            'items': {
                                'dest-ip': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                }
                            }
                        },
                        'split-tunneling-acl-local-ap-subnet': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'split-tunneling-acl-path': {
                            'type': 'string',
                            'enum': [
                                'tunnel',
                                'local'
                            ]
                        },
                        'tun-mtu-downlink': {
                            'type': 'integer'
                        },
                        'tun-mtu-uplink': {
                            'type': 'integer'
                        },
                        'wan-port-mode': {
                            'type': 'string',
                            'enum': [
                                'wan-lan',
                                'wan-only'
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
