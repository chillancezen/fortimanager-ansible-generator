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
module: fmgr_wtpprofile_radio1
short_description: Configuration options for radio 1.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/radio-1
    - /pm/config/global/obj/wireless-controller/wtp-profile/{wtp-profile}/radio-1
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
    loose_validation:
        description: Do parameter validation in a loose way
        required: False
        type: bool
        default: false
    workspace_locking_adom:
        description: the adom to lock in case FortiManager running in workspace mode
        required: False
        type: string
        choices:
          - global
          - custom adom
    workspace_locking_timeout:
        description: teh maximum time in seconds to wait for other user to release the workspace lock
        required: False
        type: integer
        default: 300
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
        methods: [get]
        description: 'Configuration options for radio 1.'
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
        description: 'Configuration options for radio 1.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                amsdu:
                    type: str
                    description: 'Enable/disable 802.11n AMSDU support. AMSDU can improve performance if supported by your WiFi clients (default = enable).'
                    choices:
                        - 'disable'
                        - 'enable'
                ap-handoff:
                    type: str
                    description: 'Enable/disable AP handoff of clients to other APs (default = disable).'
                    choices:
                        - 'disable'
                        - 'enable'
                ap-sniffer-addr:
                    type: str
                    description: 'MAC address to monitor.'
                ap-sniffer-bufsize:
                    type: int
                    description: 'Sniffer buffer size (1 - 32 MB, default = 16).'
                ap-sniffer-chan:
                    type: int
                    description: 'Channel on which to operate the sniffer (default = 6).'
                ap-sniffer-ctl:
                    type: str
                    description: 'Enable/disable sniffer on WiFi control frame (default = enable).'
                    choices:
                        - 'disable'
                        - 'enable'
                ap-sniffer-data:
                    type: str
                    description: 'Enable/disable sniffer on WiFi data frame (default = enable).'
                    choices:
                        - 'disable'
                        - 'enable'
                ap-sniffer-mgmt-beacon:
                    type: str
                    description: 'Enable/disable sniffer on WiFi management Beacon frames (default = enable).'
                    choices:
                        - 'disable'
                        - 'enable'
                ap-sniffer-mgmt-other:
                    type: str
                    description: 'Enable/disable sniffer on WiFi management other frames  (default = enable).'
                    choices:
                        - 'disable'
                        - 'enable'
                ap-sniffer-mgmt-probe:
                    type: str
                    description: 'Enable/disable sniffer on WiFi management probe frames (default = enable).'
                    choices:
                        - 'disable'
                        - 'enable'
                auto-power-high:
                    type: int
                    description: 'Automatic transmit power high limit in dBm (the actual range of transmit power depends on the AP platform type).'
                auto-power-level:
                    type: str
                    description: 'Enable/disable automatic power-level adjustment to prevent co-channel interference (default = disable).'
                    choices:
                        - 'disable'
                        - 'enable'
                auto-power-low:
                    type: int
                    description: 'Automatic transmission power low limit in dBm (the actual range of transmit power depends on the AP platform type).'
                band:
                    type: str
                    description: 'WiFi band that Radio 1 operates on.'
                    choices:
                        - '802.11b'
                        - '802.11a'
                        - '802.11g'
                        - '802.11n'
                        - '802.11ac'
                        - '802.11n-5G'
                        - '802.11g-only'
                        - '802.11n-only'
                        - '802.11n,g-only'
                        - '802.11ac-only'
                        - '802.11ac,n-only'
                        - '802.11n-5G-only'
                bandwidth-admission-control:
                    type: str
                    description: 'Enable/disable WiFi multimedia (WMM) bandwidth admission control to optimize WiFi bandwidth use. A request to join the wir...'
                    choices:
                        - 'disable'
                        - 'enable'
                bandwidth-capacity:
                    type: int
                    description: 'Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000).'
                beacon-interval:
                    type: int
                    description: 'Beacon interval. The time between beacon frames in msec (the actual range of beacon interval depends on the AP platform ty...'
                call-admission-control:
                    type: str
                    description: 'Enable/disable WiFi multimedia (WMM) call admission control to optimize WiFi bandwidth use for VoIP calls. New VoIP calls ...'
                    choices:
                        - 'disable'
                        - 'enable'
                call-capacity:
                    type: int
                    description: 'Maximum number of Voice over WLAN (VoWLAN) phones supported by the radio (0 - 60, default = 10).'
                channel:
                    -
                        type: str
                channel-bonding:
                    type: str
                    description: 'Channel bandwidth: 80, 40, or 20MHz. Channels may use both 20 and 40 by enabling coexistence.'
                    choices:
                        - 'disable'
                        - 'enable'
                        - '80MHz'
                        - '40MHz'
                        - '20MHz'
                channel-utilization:
                    type: str
                    description: 'Enable/disable measuring channel utilization.'
                    choices:
                        - 'disable'
                        - 'enable'
                coexistence:
                    type: str
                    description: 'Enable/disable allowing both HT20 and HT40 on the same radio (default = enable).'
                    choices:
                        - 'disable'
                        - 'enable'
                darrp:
                    type: str
                    description: 'Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most o...'
                    choices:
                        - 'disable'
                        - 'enable'
                dtim:
                    type: int
                    description: 'DTIM interval. The frequency to transmit Delivery Traffic Indication Message (or Map) (DTIM) messages (1 - 255, default = ...'
                frag-threshold:
                    type: int
                    description: 'Maximum packet size that can be sent without fragmentation (800 - 2346 bytes, default = 2346).'
                frequency-handoff:
                    type: str
                    description: 'Enable/disable frequency handoff of clients to other channels (default = disable).'
                    choices:
                        - 'disable'
                        - 'enable'
                max-clients:
                    type: int
                    description: 'Maximum number of stations (STAs) or WiFi clients supported by the radio. Range depends on the hardware.'
                max-distance:
                    type: int
                    description: 'Maximum expected distance between the AP and clients (0 - 54000 m, default = 0).'
                mode:
                    type: str
                    description: 'Mode of radio 1. Radio 1 can be disabled, configured as an access point, a rogue AP monitor, or a sniffer.'
                    choices:
                        - 'disabled'
                        - 'ap'
                        - 'monitor'
                        - 'sniffer'
                power-level:
                    type: int
                    description: 'Radio power level as a percentage of the maximum transmit power (0 - 100, default = 100).'
                powersave-optimize:
                    -
                        type: str
                        choices:
                            - 'tim'
                            - 'ac-vo'
                            - 'no-obss-scan'
                            - 'no-11b-rate'
                            - 'client-rate-follow'
                protection-mode:
                    type: str
                    description: 'Enable/disable 802.11g protection modes to support backwards compatibility with older clients (rtscts, ctsonly, disable).'
                    choices:
                        - 'rtscts'
                        - 'ctsonly'
                        - 'disable'
                radio-id:
                    type: int
                rts-threshold:
                    type: int
                    description: 'Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS (256 - 2346 bytes, ...'
                short-guard-interval:
                    type: str
                    description: 'Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns.'
                    choices:
                        - 'disable'
                        - 'enable'
                spectrum-analysis:
                    type: str
                    description: 'Enable/disable spectrum analysis to find interference that would negatively impact wireless performance.'
                    choices:
                        - 'disable'
                        - 'enable'
                transmit-optimize:
                    -
                        type: str
                        choices:
                            - 'disable'
                            - 'power-save'
                            - 'aggr-limit'
                            - 'retry-limit'
                            - 'send-bar'
                vap-all:
                    type: str
                    description: 'Enable/disable the automatic inheritance of all Virtual Access Points (VAPs) (default = enable).'
                    choices:
                        - 'disable'
                        - 'enable'
                vaps:
                    type: str
                    description: 'Manually selected list of Virtual Access Points (VAPs).'
                wids-profile:
                    type: str
                    description: 'Wireless Intrusion Detection System (WIDS) profile name to assign to the radio.'

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

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WTP-PROFILE/{WTP-PROFILE}/RADIO-1
      fmgr_wtpprofile_radio1:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wtp-profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WTP-PROFILE/{WTP-PROFILE}/RADIO-1
      fmgr_wtpprofile_radio1:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wtp-profile: <value of string>
         params:
            -
               data:
                  amsdu: <value in [disable, enable]>
                  ap-handoff: <value in [disable, enable]>
                  ap-sniffer-addr: <value of string>
                  ap-sniffer-bufsize: <value of integer>
                  ap-sniffer-chan: <value of integer>
                  ap-sniffer-ctl: <value in [disable, enable]>
                  ap-sniffer-data: <value in [disable, enable]>
                  ap-sniffer-mgmt-beacon: <value in [disable, enable]>
                  ap-sniffer-mgmt-other: <value in [disable, enable]>
                  ap-sniffer-mgmt-probe: <value in [disable, enable]>
                  auto-power-high: <value of integer>
                  auto-power-level: <value in [disable, enable]>
                  auto-power-low: <value of integer>
                  band: <value in [802.11b, 802.11a, 802.11g, ...]>
                  bandwidth-admission-control: <value in [disable, enable]>
                  bandwidth-capacity: <value of integer>
                  beacon-interval: <value of integer>
                  call-admission-control: <value in [disable, enable]>
                  call-capacity: <value of integer>
                  channel:
                    - <value of string>
                  channel-bonding: <value in [disable, enable, 80MHz, ...]>
                  channel-utilization: <value in [disable, enable]>
                  coexistence: <value in [disable, enable]>
                  darrp: <value in [disable, enable]>
                  dtim: <value of integer>
                  frag-threshold: <value of integer>
                  frequency-handoff: <value in [disable, enable]>
                  max-clients: <value of integer>
                  max-distance: <value of integer>
                  mode: <value in [disabled, ap, monitor, ...]>
                  power-level: <value of integer>
                  powersave-optimize:
                    - <value in [tim, ac-vo, no-obss-scan, ...]>
                  protection-mode: <value in [rtscts, ctsonly, disable]>
                  radio-id: <value of integer>
                  rts-threshold: <value of integer>
                  short-guard-interval: <value in [disable, enable]>
                  spectrum-analysis: <value in [disable, enable]>
                  transmit-optimize:
                    - <value in [disable, power-save, aggr-limit, ...]>
                  vap-all: <value in [disable, enable]>
                  vaps: <value of string>
                  wids-profile: <value of string>

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
            amsdu:
               type: str
               description: 'Enable/disable 802.11n AMSDU support. AMSDU can improve performance if supported by your WiFi clients (default = enable).'
            ap-handoff:
               type: str
               description: 'Enable/disable AP handoff of clients to other APs (default = disable).'
            ap-sniffer-addr:
               type: str
               description: 'MAC address to monitor.'
            ap-sniffer-bufsize:
               type: int
               description: 'Sniffer buffer size (1 - 32 MB, default = 16).'
            ap-sniffer-chan:
               type: int
               description: 'Channel on which to operate the sniffer (default = 6).'
            ap-sniffer-ctl:
               type: str
               description: 'Enable/disable sniffer on WiFi control frame (default = enable).'
            ap-sniffer-data:
               type: str
               description: 'Enable/disable sniffer on WiFi data frame (default = enable).'
            ap-sniffer-mgmt-beacon:
               type: str
               description: 'Enable/disable sniffer on WiFi management Beacon frames (default = enable).'
            ap-sniffer-mgmt-other:
               type: str
               description: 'Enable/disable sniffer on WiFi management other frames  (default = enable).'
            ap-sniffer-mgmt-probe:
               type: str
               description: 'Enable/disable sniffer on WiFi management probe frames (default = enable).'
            auto-power-high:
               type: int
               description: 'Automatic transmit power high limit in dBm (the actual range of transmit power depends on the AP platform type).'
            auto-power-level:
               type: str
               description: 'Enable/disable automatic power-level adjustment to prevent co-channel interference (default = disable).'
            auto-power-low:
               type: int
               description: 'Automatic transmission power low limit in dBm (the actual range of transmit power depends on the AP platform type).'
            band:
               type: str
               description: 'WiFi band that Radio 1 operates on.'
            bandwidth-admission-control:
               type: str
               description: 'Enable/disable WiFi multimedia (WMM) bandwidth admission control to optimize WiFi bandwidth use. A request to join the wireless...'
            bandwidth-capacity:
               type: int
               description: 'Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000).'
            beacon-interval:
               type: int
               description: 'Beacon interval. The time between beacon frames in msec (the actual range of beacon interval depends on the AP platform type, d...'
            call-admission-control:
               type: str
               description: 'Enable/disable WiFi multimedia (WMM) call admission control to optimize WiFi bandwidth use for VoIP calls. New VoIP calls are o...'
            call-capacity:
               type: int
               description: 'Maximum number of Voice over WLAN (VoWLAN) phones supported by the radio (0 - 60, default = 10).'
            channel:
               type: array
               suboptions:
                  type: str
            channel-bonding:
               type: str
               description: 'Channel bandwidth: 80, 40, or 20MHz. Channels may use both 20 and 40 by enabling coexistence.'
            channel-utilization:
               type: str
               description: 'Enable/disable measuring channel utilization.'
            coexistence:
               type: str
               description: 'Enable/disable allowing both HT20 and HT40 on the same radio (default = enable).'
            darrp:
               type: str
               description: 'Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optima...'
            dtim:
               type: int
               description: 'DTIM interval. The frequency to transmit Delivery Traffic Indication Message (or Map) (DTIM) messages (1 - 255, default = 1). S...'
            frag-threshold:
               type: int
               description: 'Maximum packet size that can be sent without fragmentation (800 - 2346 bytes, default = 2346).'
            frequency-handoff:
               type: str
               description: 'Enable/disable frequency handoff of clients to other channels (default = disable).'
            max-clients:
               type: int
               description: 'Maximum number of stations (STAs) or WiFi clients supported by the radio. Range depends on the hardware.'
            max-distance:
               type: int
               description: 'Maximum expected distance between the AP and clients (0 - 54000 m, default = 0).'
            mode:
               type: str
               description: 'Mode of radio 1. Radio 1 can be disabled, configured as an access point, a rogue AP monitor, or a sniffer.'
            power-level:
               type: int
               description: 'Radio power level as a percentage of the maximum transmit power (0 - 100, default = 100).'
            powersave-optimize:
               type: array
               suboptions:
                  type: str
            protection-mode:
               type: str
               description: 'Enable/disable 802.11g protection modes to support backwards compatibility with older clients (rtscts, ctsonly, disable).'
            radio-id:
               type: int
            rts-threshold:
               type: int
               description: 'Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS (256 - 2346 bytes, defau...'
            short-guard-interval:
               type: str
               description: 'Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns.'
            spectrum-analysis:
               type: str
               description: 'Enable/disable spectrum analysis to find interference that would negatively impact wireless performance.'
            transmit-optimize:
               type: array
               suboptions:
                  type: str
            vap-all:
               type: str
               description: 'Enable/disable the automatic inheritance of all Virtual Access Points (VAPs) (default = enable).'
            vaps:
               type: str
               description: 'Manually selected list of Virtual Access Points (VAPs).'
            wids-profile:
               type: str
               description: 'Wireless Intrusion Detection System (WIDS) profile name to assign to the radio.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/radio-1'
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
            example: '/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/radio-1'

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
        '/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/radio-1',
        '/pm/config/global/obj/wireless-controller/wtp-profile/{wtp-profile}/radio-1'
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
                        'amsdu': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ap-handoff': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ap-sniffer-addr': {
                            'type': 'string'
                        },
                        'ap-sniffer-bufsize': {
                            'type': 'integer'
                        },
                        'ap-sniffer-chan': {
                            'type': 'integer'
                        },
                        'ap-sniffer-ctl': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ap-sniffer-data': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ap-sniffer-mgmt-beacon': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ap-sniffer-mgmt-other': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ap-sniffer-mgmt-probe': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'auto-power-high': {
                            'type': 'integer'
                        },
                        'auto-power-level': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'auto-power-low': {
                            'type': 'integer'
                        },
                        'band': {
                            'type': 'string',
                            'enum': [
                                '802.11b',
                                '802.11a',
                                '802.11g',
                                '802.11n',
                                '802.11ac',
                                '802.11n-5G',
                                '802.11g-only',
                                '802.11n-only',
                                '802.11n,g-only',
                                '802.11ac-only',
                                '802.11ac,n-only',
                                '802.11n-5G-only'
                            ]
                        },
                        'bandwidth-admission-control': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'bandwidth-capacity': {
                            'type': 'integer'
                        },
                        'beacon-interval': {
                            'type': 'integer'
                        },
                        'call-admission-control': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'call-capacity': {
                            'type': 'integer'
                        },
                        'channel': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'channel-bonding': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable',
                                '80MHz',
                                '40MHz',
                                '20MHz'
                            ]
                        },
                        'channel-utilization': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'coexistence': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'darrp': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dtim': {
                            'type': 'integer'
                        },
                        'frag-threshold': {
                            'type': 'integer'
                        },
                        'frequency-handoff': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'max-clients': {
                            'type': 'integer'
                        },
                        'max-distance': {
                            'type': 'integer'
                        },
                        'mode': {
                            'type': 'string',
                            'enum': [
                                'disabled',
                                'ap',
                                'monitor',
                                'sniffer'
                            ]
                        },
                        'power-level': {
                            'type': 'integer'
                        },
                        'powersave-optimize': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'tim',
                                    'ac-vo',
                                    'no-obss-scan',
                                    'no-11b-rate',
                                    'client-rate-follow'
                                ]
                            }
                        },
                        'protection-mode': {
                            'type': 'string',
                            'enum': [
                                'rtscts',
                                'ctsonly',
                                'disable'
                            ]
                        },
                        'radio-id': {
                            'type': 'integer'
                        },
                        'rts-threshold': {
                            'type': 'integer'
                        },
                        'short-guard-interval': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'spectrum-analysis': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'transmit-optimize': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'power-save',
                                    'aggr-limit',
                                    'retry-limit',
                                    'send-bar'
                                ]
                            }
                        },
                        'vap-all': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'vaps': {
                            'type': 'string'
                        },
                        'wids-profile': {
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
        'loose_validation': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'workspace_locking_adom': {
            'type': 'str',
            'required': False
        },
        'workspace_locking_timeout': {
            'type': 'int',
            'required': False,
            'default': 300
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
