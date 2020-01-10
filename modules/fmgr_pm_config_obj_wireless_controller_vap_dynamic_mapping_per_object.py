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
module: fmgr_pm_config_obj_wireless_controller_vap_dynamic_mapping_per_object
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/wireless-controller/vap/{vap}/dynamic_mapping/{dynamic_mapping}
    - /pm/config/global/obj/wireless-controller/vap/{vap}/dynamic_mapping/{dynamic_mapping}
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
            vap:
                type: str
            dynamic_mapping:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
            data:
                _centmgmt:
                    type: str
                    default: 'disable'
                    choices:
                        - 'disable'
                        - 'enable'
                _dhcp_svr_id:
                    type: str
                _intf_allowaccess:
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
                            - 'auto-ipsec'
                            - 'radius-acct'
                            - 'probe-response'
                            - 'capwap'
                _intf_device-identification:
                    type: str
                    default: 'disable'
                    choices:
                        - 'disable'
                        - 'enable'
                _intf_device-netscan:
                    type: str
                    default: 'disable'
                    choices:
                        - 'disable'
                        - 'enable'
                _intf_dhcp-relay-ip:
                    -
                        type: str
                _intf_dhcp-relay-service:
                    type: str
                    default: 'disable'
                    choices:
                        - 'disable'
                        - 'enable'
                _intf_dhcp-relay-type:
                    type: str
                    default: 'regular'
                    choices:
                        - 'regular'
                        - 'ipsec'
                _intf_dhcp6-relay-ip:
                    type: str
                _intf_dhcp6-relay-service:
                    type: str
                    default: 'disable'
                    choices:
                        - 'disable'
                        - 'enable'
                _intf_dhcp6-relay-type:
                    type: str
                    default: 'regular'
                    choices:
                        - 'regular'
                _intf_ip:
                    type: str
                _intf_ip6-address:
                    type: str
                _intf_ip6-allowaccess:
                    -
                        type: str
                        choices:
                            - 'https'
                            - 'ping'
                            - 'ssh'
                            - 'snmp'
                            - 'http'
                            - 'telnet'
                            - 'any'
                            - 'fgfm'
                            - 'capwap'
                _intf_listen-forticlient-connection:
                    type: str
                    default: 'disable'
                    choices:
                        - 'disable'
                        - 'enable'
                _scope:
                    -
                        name:
                            type: str
                        vdom:
                            type: str
                acct-interim-interval:
                    type: int
                address-group:
                    type: str
                alias:
                    type: str
                atf-weight:
                    type: int
                auth:
                    type: str
                    choices:
                        - 'PSK'
                        - 'psk'
                        - 'RADIUS'
                        - 'radius'
                        - 'usergroup'
                broadcast-ssid:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                broadcast-suppression:
                    -
                        type: str
                        choices:
                            - 'dhcp'
                            - 'arp'
                            - 'dhcp2'
                            - 'arp2'
                            - 'netbios-ns'
                            - 'netbios-ds'
                            - 'arp3'
                            - 'dhcp-up'
                            - 'dhcp-down'
                            - 'arp-known'
                            - 'arp-unknown'
                            - 'arp-reply'
                            - 'ipv6'
                            - 'dhcp-starvation'
                            - 'arp-poison'
                            - 'all-other-mc'
                            - 'all-other-bc'
                            - 'arp-proxy'
                            - 'dhcp-ucast'
                captive-portal-ac-name:
                    type: str
                captive-portal-macauth-radius-secret:
                    -
                        type: str
                captive-portal-macauth-radius-server:
                    type: str
                captive-portal-radius-secret:
                    -
                        type: str
                captive-portal-radius-server:
                    type: str
                captive-portal-session-timeout-interval:
                    type: int
                client-count:
                    type: int
                dhcp-lease-time:
                    type: int
                dhcp-option82-circuit-id-insertion:
                    type: str
                    choices:
                        - 'disable'
                        - 'style-1'
                        - 'style-2'
                dhcp-option82-insertion:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                dhcp-option82-remote-id-insertion:
                    type: str
                    choices:
                        - 'disable'
                        - 'style-1'
                dynamic-vlan:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                eap-reauth:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                eap-reauth-intv:
                    type: int
                eapol-key-retries:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                encrypt:
                    type: str
                    choices:
                        - 'TKIP'
                        - 'AES'
                        - 'TKIP-AES'
                external-fast-roaming:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                external-logout:
                    type: str
                external-web:
                    type: str
                fast-bss-transition:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                fast-roaming:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ft-mobility-domain:
                    type: int
                ft-over-ds:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ft-r0-key-lifetime:
                    type: int
                gtk-rekey:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                gtk-rekey-intv:
                    type: int
                hotspot20-profile:
                    type: str
                intra-vap-privacy:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ip:
                    type: str
                key:
                    -
                        type: str
                keyindex:
                    type: int
                ldpc:
                    type: str
                    choices:
                        - 'disable'
                        - 'tx'
                        - 'rx'
                        - 'rxtx'
                local-authentication:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                local-bridging:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                local-lan:
                    type: str
                    choices:
                        - 'deny'
                        - 'allow'
                local-standalone:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                local-standalone-nat:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                local-switching:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                mac-auth-bypass:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                mac-filter:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                mac-filter-policy-other:
                    type: str
                    choices:
                        - 'deny'
                        - 'allow'
                max-clients:
                    type: int
                max-clients-ap:
                    type: int
                me-disable-thresh:
                    type: int
                mesh-backhaul:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                mpsk:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                mpsk-concurrent-clients:
                    type: int
                multicast-enhance:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                multicast-rate:
                    type: str
                    choices:
                        - '0'
                        - '6000'
                        - '12000'
                        - '24000'
                okc:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                owe-groups:
                    -
                        type: str
                        choices:
                            - '19'
                            - '20'
                            - '21'
                owe-transition:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                owe-transition-ssid:
                    type: str
                passphrase:
                    -
                        type: str
                pmf:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                        - 'optional'
                pmf-assoc-comeback-timeout:
                    type: int
                pmf-sa-query-retry-timeout:
                    type: int
                portal-message-override-group:
                    type: str
                portal-type:
                    type: str
                    choices:
                        - 'auth'
                        - 'auth+disclaimer'
                        - 'disclaimer'
                        - 'email-collect'
                        - 'cmcc'
                        - 'cmcc-macauth'
                        - 'auth-mac'
                probe-resp-suppression:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                probe-resp-threshold:
                    type: str
                ptk-rekey:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ptk-rekey-intv:
                    type: int
                qos-profile:
                    type: str
                quarantine:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                radio-2g-threshold:
                    type: str
                radio-5g-threshold:
                    type: str
                radio-sensitivity:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                radius-mac-auth:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                radius-mac-auth-server:
                    type: str
                radius-mac-auth-usergroups:
                    -
                        type: str
                radius-server:
                    type: str
                rates-11a:
                    -
                        type: str
                        choices:
                            - '1'
                            - '1-basic'
                            - '2'
                            - '2-basic'
                            - '5.5'
                            - '5.5-basic'
                            - '6'
                            - '6-basic'
                            - '9'
                            - '9-basic'
                            - '12'
                            - '12-basic'
                            - '18'
                            - '18-basic'
                            - '24'
                            - '24-basic'
                            - '36'
                            - '36-basic'
                            - '48'
                            - '48-basic'
                            - '54'
                            - '54-basic'
                            - '11'
                            - '11-basic'
                rates-11ac-ss12:
                    -
                        type: str
                        choices:
                            - 'mcs0/1'
                            - 'mcs1/1'
                            - 'mcs2/1'
                            - 'mcs3/1'
                            - 'mcs4/1'
                            - 'mcs5/1'
                            - 'mcs6/1'
                            - 'mcs7/1'
                            - 'mcs8/1'
                            - 'mcs9/1'
                            - 'mcs0/2'
                            - 'mcs1/2'
                            - 'mcs2/2'
                            - 'mcs3/2'
                            - 'mcs4/2'
                            - 'mcs5/2'
                            - 'mcs6/2'
                            - 'mcs7/2'
                            - 'mcs8/2'
                            - 'mcs9/2'
                            - 'mcs10/1'
                            - 'mcs11/1'
                            - 'mcs10/2'
                            - 'mcs11/2'
                rates-11ac-ss34:
                    -
                        type: str
                        choices:
                            - 'mcs0/3'
                            - 'mcs1/3'
                            - 'mcs2/3'
                            - 'mcs3/3'
                            - 'mcs4/3'
                            - 'mcs5/3'
                            - 'mcs6/3'
                            - 'mcs7/3'
                            - 'mcs8/3'
                            - 'mcs9/3'
                            - 'mcs0/4'
                            - 'mcs1/4'
                            - 'mcs2/4'
                            - 'mcs3/4'
                            - 'mcs4/4'
                            - 'mcs5/4'
                            - 'mcs6/4'
                            - 'mcs7/4'
                            - 'mcs8/4'
                            - 'mcs9/4'
                            - 'mcs10/3'
                            - 'mcs11/3'
                            - 'mcs10/4'
                            - 'mcs11/4'
                rates-11bg:
                    -
                        type: str
                        choices:
                            - '1'
                            - '1-basic'
                            - '2'
                            - '2-basic'
                            - '5.5'
                            - '5.5-basic'
                            - '6'
                            - '6-basic'
                            - '9'
                            - '9-basic'
                            - '12'
                            - '12-basic'
                            - '18'
                            - '18-basic'
                            - '24'
                            - '24-basic'
                            - '36'
                            - '36-basic'
                            - '48'
                            - '48-basic'
                            - '54'
                            - '54-basic'
                            - '11'
                            - '11-basic'
                rates-11n-ss12:
                    -
                        type: str
                        choices:
                            - 'mcs0/1'
                            - 'mcs1/1'
                            - 'mcs2/1'
                            - 'mcs3/1'
                            - 'mcs4/1'
                            - 'mcs5/1'
                            - 'mcs6/1'
                            - 'mcs7/1'
                            - 'mcs8/2'
                            - 'mcs9/2'
                            - 'mcs10/2'
                            - 'mcs11/2'
                            - 'mcs12/2'
                            - 'mcs13/2'
                            - 'mcs14/2'
                            - 'mcs15/2'
                rates-11n-ss34:
                    -
                        type: str
                        choices:
                            - 'mcs16/3'
                            - 'mcs17/3'
                            - 'mcs18/3'
                            - 'mcs19/3'
                            - 'mcs20/3'
                            - 'mcs21/3'
                            - 'mcs22/3'
                            - 'mcs23/3'
                            - 'mcs24/4'
                            - 'mcs25/4'
                            - 'mcs26/4'
                            - 'mcs27/4'
                            - 'mcs28/4'
                            - 'mcs29/4'
                            - 'mcs30/4'
                            - 'mcs31/4'
                sae-groups:
                    -
                        type: str
                        choices:
                            - '1'
                            - '2'
                            - '5'
                            - '14'
                            - '15'
                            - '16'
                            - '17'
                            - '18'
                            - '19'
                            - '20'
                            - '21'
                            - '27'
                            - '28'
                            - '29'
                            - '30'
                            - '31'
                sae-password:
                    -
                        type: str
                schedule:
                    type: str
                security:
                    type: str
                    choices:
                        - 'None'
                        - 'WEP64'
                        - 'wep64'
                        - 'WEP128'
                        - 'wep128'
                        - 'WPA_PSK'
                        - 'WPA_RADIUS'
                        - 'WPA'
                        - 'WPA2'
                        - 'WPA2_AUTO'
                        - 'open'
                        - 'wpa-personal'
                        - 'wpa-enterprise'
                        - 'captive-portal'
                        - 'wpa-only-personal'
                        - 'wpa-only-enterprise'
                        - 'wpa2-only-personal'
                        - 'wpa2-only-enterprise'
                        - 'wpa-personal+captive-portal'
                        - 'wpa-only-personal+captive-portal'
                        - 'wpa2-only-personal+captive-portal'
                        - 'osen'
                        - 'wpa3-enterprise'
                        - 'sae'
                        - 'sae-transition'
                        - 'owe'
                        - 'wpa3-sae'
                        - 'wpa3-sae-transition'
                security-exempt-list:
                    type: str
                security-obsolete-option:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                security-redirect-url:
                    type: str
                selected-usergroups:
                    type: str
                split-tunneling:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ssid:
                    type: str
                tkip-counter-measure:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                usergroup:
                    type: str
                utm-profile:
                    type: str
                vdom:
                    type: str
                vlan-auto:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                vlan-pooling:
                    type: str
                    choices:
                        - 'wtp-group'
                        - 'round-robin'
                        - 'hash'
                        - 'disable'
                vlanid:
                    type: int
                voice-enterprise:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
    schema_object1:
        methods: [delete]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
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

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/VAP/{VAP}/DYNAMIC_MAPPING/{DYNAMIC_MAPPING}
      fmgr_pm_config_obj_wireless_controller_vap_dynamic_mapping_per_object:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vap: <value of string>
            dynamic_mapping: <value of string>
         params:
            -
               data:
                  _centmgmt: <value in [disable, enable] default: 'disable'>
                  _dhcp_svr_id: <value of string>
                  _intf_allowaccess:
                    - <value in [https, ping, ssh, ...]>
                  _intf_device-identification: <value in [disable, enable] default: 'disable'>
                  _intf_device-netscan: <value in [disable, enable] default: 'disable'>
                  _intf_dhcp-relay-ip:
                    - <value of string>
                  _intf_dhcp-relay-service: <value in [disable, enable] default: 'disable'>
                  _intf_dhcp-relay-type: <value in [regular, ipsec] default: 'regular'>
                  _intf_dhcp6-relay-ip: <value of string>
                  _intf_dhcp6-relay-service: <value in [disable, enable] default: 'disable'>
                  _intf_dhcp6-relay-type: <value in [regular] default: 'regular'>
                  _intf_ip: <value of string>
                  _intf_ip6-address: <value of string>
                  _intf_ip6-allowaccess:
                    - <value in [https, ping, ssh, ...]>
                  _intf_listen-forticlient-connection: <value in [disable, enable] default: 'disable'>
                  _scope:
                    -
                        name: <value of string>
                        vdom: <value of string>
                  acct-interim-interval: <value of integer>
                  address-group: <value of string>
                  alias: <value of string>
                  atf-weight: <value of integer>
                  auth: <value in [PSK, psk, RADIUS, ...]>
                  broadcast-ssid: <value in [disable, enable]>
                  broadcast-suppression:
                    - <value in [dhcp, arp, dhcp2, ...]>
                  captive-portal-ac-name: <value of string>
                  captive-portal-macauth-radius-secret:
                    - <value of string>
                  captive-portal-macauth-radius-server: <value of string>
                  captive-portal-radius-secret:
                    - <value of string>
                  captive-portal-radius-server: <value of string>
                  captive-portal-session-timeout-interval: <value of integer>
                  client-count: <value of integer>
                  dhcp-lease-time: <value of integer>
                  dhcp-option82-circuit-id-insertion: <value in [disable, style-1, style-2]>
                  dhcp-option82-insertion: <value in [disable, enable]>
                  dhcp-option82-remote-id-insertion: <value in [disable, style-1]>
                  dynamic-vlan: <value in [disable, enable]>
                  eap-reauth: <value in [disable, enable]>
                  eap-reauth-intv: <value of integer>
                  eapol-key-retries: <value in [disable, enable]>
                  encrypt: <value in [TKIP, AES, TKIP-AES]>
                  external-fast-roaming: <value in [disable, enable]>
                  external-logout: <value of string>
                  external-web: <value of string>
                  fast-bss-transition: <value in [disable, enable]>
                  fast-roaming: <value in [disable, enable]>
                  ft-mobility-domain: <value of integer>
                  ft-over-ds: <value in [disable, enable]>
                  ft-r0-key-lifetime: <value of integer>
                  gtk-rekey: <value in [disable, enable]>
                  gtk-rekey-intv: <value of integer>
                  hotspot20-profile: <value of string>
                  intra-vap-privacy: <value in [disable, enable]>
                  ip: <value of string>
                  key:
                    - <value of string>
                  keyindex: <value of integer>
                  ldpc: <value in [disable, tx, rx, ...]>
                  local-authentication: <value in [disable, enable]>
                  local-bridging: <value in [disable, enable]>
                  local-lan: <value in [deny, allow]>
                  local-standalone: <value in [disable, enable]>
                  local-standalone-nat: <value in [disable, enable]>
                  local-switching: <value in [disable, enable]>
                  mac-auth-bypass: <value in [disable, enable]>
                  mac-filter: <value in [disable, enable]>
                  mac-filter-policy-other: <value in [deny, allow]>
                  max-clients: <value of integer>
                  max-clients-ap: <value of integer>
                  me-disable-thresh: <value of integer>
                  mesh-backhaul: <value in [disable, enable]>
                  mpsk: <value in [disable, enable]>
                  mpsk-concurrent-clients: <value of integer>
                  multicast-enhance: <value in [disable, enable]>
                  multicast-rate: <value in [0, 6000, 12000, ...]>
                  okc: <value in [disable, enable]>
                  owe-groups:
                    - <value in [19, 20, 21]>
                  owe-transition: <value in [disable, enable]>
                  owe-transition-ssid: <value of string>
                  passphrase:
                    - <value of string>
                  pmf: <value in [disable, enable, optional]>
                  pmf-assoc-comeback-timeout: <value of integer>
                  pmf-sa-query-retry-timeout: <value of integer>
                  portal-message-override-group: <value of string>
                  portal-type: <value in [auth, auth+disclaimer, disclaimer, ...]>
                  probe-resp-suppression: <value in [disable, enable]>
                  probe-resp-threshold: <value of string>
                  ptk-rekey: <value in [disable, enable]>
                  ptk-rekey-intv: <value of integer>
                  qos-profile: <value of string>
                  quarantine: <value in [disable, enable]>
                  radio-2g-threshold: <value of string>
                  radio-5g-threshold: <value of string>
                  radio-sensitivity: <value in [disable, enable]>
                  radius-mac-auth: <value in [disable, enable]>
                  radius-mac-auth-server: <value of string>
                  radius-mac-auth-usergroups:
                    - <value of string>
                  radius-server: <value of string>
                  rates-11a:
                    - <value in [1, 1-basic, 2, ...]>
                  rates-11ac-ss12:
                    - <value in [mcs0/1, mcs1/1, mcs2/1, ...]>
                  rates-11ac-ss34:
                    - <value in [mcs0/3, mcs1/3, mcs2/3, ...]>
                  rates-11bg:
                    - <value in [1, 1-basic, 2, ...]>
                  rates-11n-ss12:
                    - <value in [mcs0/1, mcs1/1, mcs2/1, ...]>
                  rates-11n-ss34:
                    - <value in [mcs16/3, mcs17/3, mcs18/3, ...]>
                  sae-groups:
                    - <value in [1, 2, 5, ...]>
                  sae-password:
                    - <value of string>
                  schedule: <value of string>
                  security: <value in [None, WEP64, wep64, ...]>
                  security-exempt-list: <value of string>
                  security-obsolete-option: <value in [disable, enable]>
                  security-redirect-url: <value of string>
                  selected-usergroups: <value of string>
                  split-tunneling: <value in [disable, enable]>
                  ssid: <value of string>
                  tkip-counter-measure: <value in [disable, enable]>
                  usergroup: <value of string>
                  utm-profile: <value of string>
                  vdom: <value of string>
                  vlan-auto: <value in [disable, enable]>
                  vlan-pooling: <value in [wtp-group, round-robin, hash, ...]>
                  vlanid: <value of integer>
                  voice-enterprise: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/VAP/{VAP}/DYNAMIC_MAPPING/{DYNAMIC_MAPPING}
      fmgr_pm_config_obj_wireless_controller_vap_dynamic_mapping_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vap: <value of string>
            dynamic_mapping: <value of string>
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
            example: '/pm/config/adom/{adom}/obj/wireless-controller/vap/{vap}/dynamic_mapping/{dy...'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            _centmgmt:
               type: str
               example: 'disable'
            _dhcp_svr_id:
               type: str
            _intf_allowaccess:
               type: array
               suboptions:
                  type: str
            _intf_device-identification:
               type: str
               example: 'disable'
            _intf_device-netscan:
               type: str
               example: 'disable'
            _intf_dhcp-relay-ip:
               type: array
               suboptions:
                  type: str
            _intf_dhcp-relay-service:
               type: str
               example: 'disable'
            _intf_dhcp-relay-type:
               type: str
               example: 'regular'
            _intf_dhcp6-relay-ip:
               type: str
            _intf_dhcp6-relay-service:
               type: str
               example: 'disable'
            _intf_dhcp6-relay-type:
               type: str
               example: 'regular'
            _intf_ip:
               type: str
            _intf_ip6-address:
               type: str
            _intf_ip6-allowaccess:
               type: array
               suboptions:
                  type: str
            _intf_listen-forticlient-connection:
               type: str
               example: 'disable'
            _scope:
               type: array
               suboptions:
                  name:
                     type: str
                  vdom:
                     type: str
            acct-interim-interval:
               type: int
            address-group:
               type: str
            alias:
               type: str
            atf-weight:
               type: int
            auth:
               type: str
            broadcast-ssid:
               type: str
            broadcast-suppression:
               type: array
               suboptions:
                  type: str
            captive-portal-ac-name:
               type: str
            captive-portal-macauth-radius-secret:
               type: array
               suboptions:
                  type: str
            captive-portal-macauth-radius-server:
               type: str
            captive-portal-radius-secret:
               type: array
               suboptions:
                  type: str
            captive-portal-radius-server:
               type: str
            captive-portal-session-timeout-interval:
               type: int
            client-count:
               type: int
            dhcp-lease-time:
               type: int
            dhcp-option82-circuit-id-insertion:
               type: str
            dhcp-option82-insertion:
               type: str
            dhcp-option82-remote-id-insertion:
               type: str
            dynamic-vlan:
               type: str
            eap-reauth:
               type: str
            eap-reauth-intv:
               type: int
            eapol-key-retries:
               type: str
            encrypt:
               type: str
            external-fast-roaming:
               type: str
            external-logout:
               type: str
            external-web:
               type: str
            fast-bss-transition:
               type: str
            fast-roaming:
               type: str
            ft-mobility-domain:
               type: int
            ft-over-ds:
               type: str
            ft-r0-key-lifetime:
               type: int
            gtk-rekey:
               type: str
            gtk-rekey-intv:
               type: int
            hotspot20-profile:
               type: str
            intra-vap-privacy:
               type: str
            ip:
               type: str
            key:
               type: array
               suboptions:
                  type: str
            keyindex:
               type: int
            ldpc:
               type: str
            local-authentication:
               type: str
            local-bridging:
               type: str
            local-lan:
               type: str
            local-standalone:
               type: str
            local-standalone-nat:
               type: str
            local-switching:
               type: str
            mac-auth-bypass:
               type: str
            mac-filter:
               type: str
            mac-filter-policy-other:
               type: str
            max-clients:
               type: int
            max-clients-ap:
               type: int
            me-disable-thresh:
               type: int
            mesh-backhaul:
               type: str
            mpsk:
               type: str
            mpsk-concurrent-clients:
               type: int
            multicast-enhance:
               type: str
            multicast-rate:
               type: str
            okc:
               type: str
            owe-groups:
               type: array
               suboptions:
                  type: str
            owe-transition:
               type: str
            owe-transition-ssid:
               type: str
            passphrase:
               type: array
               suboptions:
                  type: str
            pmf:
               type: str
            pmf-assoc-comeback-timeout:
               type: int
            pmf-sa-query-retry-timeout:
               type: int
            portal-message-override-group:
               type: str
            portal-type:
               type: str
            probe-resp-suppression:
               type: str
            probe-resp-threshold:
               type: str
            ptk-rekey:
               type: str
            ptk-rekey-intv:
               type: int
            qos-profile:
               type: str
            quarantine:
               type: str
            radio-2g-threshold:
               type: str
            radio-5g-threshold:
               type: str
            radio-sensitivity:
               type: str
            radius-mac-auth:
               type: str
            radius-mac-auth-server:
               type: str
            radius-mac-auth-usergroups:
               type: array
               suboptions:
                  type: str
            radius-server:
               type: str
            rates-11a:
               type: array
               suboptions:
                  type: str
            rates-11ac-ss12:
               type: array
               suboptions:
                  type: str
            rates-11ac-ss34:
               type: array
               suboptions:
                  type: str
            rates-11bg:
               type: array
               suboptions:
                  type: str
            rates-11n-ss12:
               type: array
               suboptions:
                  type: str
            rates-11n-ss34:
               type: array
               suboptions:
                  type: str
            sae-groups:
               type: array
               suboptions:
                  type: str
            sae-password:
               type: array
               suboptions:
                  type: str
            schedule:
               type: str
            security:
               type: str
            security-exempt-list:
               type: str
            security-obsolete-option:
               type: str
            security-redirect-url:
               type: str
            selected-usergroups:
               type: str
            split-tunneling:
               type: str
            ssid:
               type: str
            tkip-counter-measure:
               type: str
            usergroup:
               type: str
            utm-profile:
               type: str
            vdom:
               type: str
            vlan-auto:
               type: str
            vlan-pooling:
               type: str
            vlanid:
               type: int
            voice-enterprise:
               type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/wireless-controller/vap/{vap}/dynamic_mapping/{dy...'

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
        '/pm/config/adom/{adom}/obj/wireless-controller/vap/{vap}/dynamic_mapping/{dynamic_mapping}',
        '/pm/config/global/obj/wireless-controller/vap/{vap}/dynamic_mapping/{dynamic_mapping}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'vap',
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
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        '_centmgmt': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        '_dhcp_svr_id': {
                            'type': 'string'
                        },
                        '_intf_allowaccess': {
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
                                    'auto-ipsec',
                                    'radius-acct',
                                    'probe-response',
                                    'capwap'
                                ]
                            }
                        },
                        '_intf_device-identification': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        '_intf_device-netscan': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        '_intf_dhcp-relay-ip': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        '_intf_dhcp-relay-service': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        '_intf_dhcp-relay-type': {
                            'type': 'string',
                            'enum': [
                                'regular',
                                'ipsec'
                            ]
                        },
                        '_intf_dhcp6-relay-ip': {
                            'type': 'string'
                        },
                        '_intf_dhcp6-relay-service': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        '_intf_dhcp6-relay-type': {
                            'type': 'string',
                            'enum': [
                                'regular'
                            ]
                        },
                        '_intf_ip': {
                            'type': 'string'
                        },
                        '_intf_ip6-address': {
                            'type': 'string'
                        },
                        '_intf_ip6-allowaccess': {
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
                                    'any',
                                    'fgfm',
                                    'capwap'
                                ]
                            }
                        },
                        '_intf_listen-forticlient-connection': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        '_scope': {
                            'type': 'array',
                            'items': {
                                'name': {
                                    'type': 'string'
                                },
                                'vdom': {
                                    'type': 'string'
                                }
                            }
                        },
                        'acct-interim-interval': {
                            'type': 'integer'
                        },
                        'address-group': {
                            'type': 'string'
                        },
                        'alias': {
                            'type': 'string'
                        },
                        'atf-weight': {
                            'type': 'integer'
                        },
                        'auth': {
                            'type': 'string',
                            'enum': [
                                'PSK',
                                'psk',
                                'RADIUS',
                                'radius',
                                'usergroup'
                            ]
                        },
                        'broadcast-ssid': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'broadcast-suppression': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'dhcp',
                                    'arp',
                                    'dhcp2',
                                    'arp2',
                                    'netbios-ns',
                                    'netbios-ds',
                                    'arp3',
                                    'dhcp-up',
                                    'dhcp-down',
                                    'arp-known',
                                    'arp-unknown',
                                    'arp-reply',
                                    'ipv6',
                                    'dhcp-starvation',
                                    'arp-poison',
                                    'all-other-mc',
                                    'all-other-bc',
                                    'arp-proxy',
                                    'dhcp-ucast'
                                ]
                            }
                        },
                        'captive-portal-ac-name': {
                            'type': 'string'
                        },
                        'captive-portal-macauth-radius-secret': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'captive-portal-macauth-radius-server': {
                            'type': 'string'
                        },
                        'captive-portal-radius-secret': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'captive-portal-radius-server': {
                            'type': 'string'
                        },
                        'captive-portal-session-timeout-interval': {
                            'type': 'integer'
                        },
                        'client-count': {
                            'type': 'integer'
                        },
                        'dhcp-lease-time': {
                            'type': 'integer'
                        },
                        'dhcp-option82-circuit-id-insertion': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'style-1',
                                'style-2'
                            ]
                        },
                        'dhcp-option82-insertion': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dhcp-option82-remote-id-insertion': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'style-1'
                            ]
                        },
                        'dynamic-vlan': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'eap-reauth': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'eap-reauth-intv': {
                            'type': 'integer'
                        },
                        'eapol-key-retries': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'encrypt': {
                            'type': 'string',
                            'enum': [
                                'TKIP',
                                'AES',
                                'TKIP-AES'
                            ]
                        },
                        'external-fast-roaming': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'external-logout': {
                            'type': 'string'
                        },
                        'external-web': {
                            'type': 'string'
                        },
                        'fast-bss-transition': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fast-roaming': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ft-mobility-domain': {
                            'type': 'integer'
                        },
                        'ft-over-ds': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ft-r0-key-lifetime': {
                            'type': 'integer'
                        },
                        'gtk-rekey': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'gtk-rekey-intv': {
                            'type': 'integer'
                        },
                        'hotspot20-profile': {
                            'type': 'string'
                        },
                        'intra-vap-privacy': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ip': {
                            'type': 'string'
                        },
                        'key': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'keyindex': {
                            'type': 'integer'
                        },
                        'ldpc': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'tx',
                                'rx',
                                'rxtx'
                            ]
                        },
                        'local-authentication': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'local-bridging': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'local-lan': {
                            'type': 'string',
                            'enum': [
                                'deny',
                                'allow'
                            ]
                        },
                        'local-standalone': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'local-standalone-nat': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'local-switching': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mac-auth-bypass': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mac-filter': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mac-filter-policy-other': {
                            'type': 'string',
                            'enum': [
                                'deny',
                                'allow'
                            ]
                        },
                        'max-clients': {
                            'type': 'integer'
                        },
                        'max-clients-ap': {
                            'type': 'integer'
                        },
                        'me-disable-thresh': {
                            'type': 'integer'
                        },
                        'mesh-backhaul': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mpsk': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mpsk-concurrent-clients': {
                            'type': 'integer'
                        },
                        'multicast-enhance': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'multicast-rate': {
                            'type': 'string',
                            'enum': [
                                '0',
                                '6000',
                                '12000',
                                '24000'
                            ]
                        },
                        'okc': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'owe-groups': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    '19',
                                    '20',
                                    '21'
                                ]
                            }
                        },
                        'owe-transition': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'owe-transition-ssid': {
                            'type': 'string'
                        },
                        'passphrase': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'pmf': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable',
                                'optional'
                            ]
                        },
                        'pmf-assoc-comeback-timeout': {
                            'type': 'integer'
                        },
                        'pmf-sa-query-retry-timeout': {
                            'type': 'integer'
                        },
                        'portal-message-override-group': {
                            'type': 'string'
                        },
                        'portal-type': {
                            'type': 'string',
                            'enum': [
                                'auth',
                                'auth+disclaimer',
                                'disclaimer',
                                'email-collect',
                                'cmcc',
                                'cmcc-macauth',
                                'auth-mac'
                            ]
                        },
                        'probe-resp-suppression': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'probe-resp-threshold': {
                            'type': 'string'
                        },
                        'ptk-rekey': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ptk-rekey-intv': {
                            'type': 'integer'
                        },
                        'qos-profile': {
                            'type': 'string'
                        },
                        'quarantine': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'radio-2g-threshold': {
                            'type': 'string'
                        },
                        'radio-5g-threshold': {
                            'type': 'string'
                        },
                        'radio-sensitivity': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'radius-mac-auth': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'radius-mac-auth-server': {
                            'type': 'string'
                        },
                        'radius-mac-auth-usergroups': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'radius-server': {
                            'type': 'string'
                        },
                        'rates-11a': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    '1',
                                    '1-basic',
                                    '2',
                                    '2-basic',
                                    '5.5',
                                    '5.5-basic',
                                    '6',
                                    '6-basic',
                                    '9',
                                    '9-basic',
                                    '12',
                                    '12-basic',
                                    '18',
                                    '18-basic',
                                    '24',
                                    '24-basic',
                                    '36',
                                    '36-basic',
                                    '48',
                                    '48-basic',
                                    '54',
                                    '54-basic',
                                    '11',
                                    '11-basic'
                                ]
                            }
                        },
                        'rates-11ac-ss12': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'mcs0/1',
                                    'mcs1/1',
                                    'mcs2/1',
                                    'mcs3/1',
                                    'mcs4/1',
                                    'mcs5/1',
                                    'mcs6/1',
                                    'mcs7/1',
                                    'mcs8/1',
                                    'mcs9/1',
                                    'mcs0/2',
                                    'mcs1/2',
                                    'mcs2/2',
                                    'mcs3/2',
                                    'mcs4/2',
                                    'mcs5/2',
                                    'mcs6/2',
                                    'mcs7/2',
                                    'mcs8/2',
                                    'mcs9/2',
                                    'mcs10/1',
                                    'mcs11/1',
                                    'mcs10/2',
                                    'mcs11/2'
                                ]
                            }
                        },
                        'rates-11ac-ss34': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'mcs0/3',
                                    'mcs1/3',
                                    'mcs2/3',
                                    'mcs3/3',
                                    'mcs4/3',
                                    'mcs5/3',
                                    'mcs6/3',
                                    'mcs7/3',
                                    'mcs8/3',
                                    'mcs9/3',
                                    'mcs0/4',
                                    'mcs1/4',
                                    'mcs2/4',
                                    'mcs3/4',
                                    'mcs4/4',
                                    'mcs5/4',
                                    'mcs6/4',
                                    'mcs7/4',
                                    'mcs8/4',
                                    'mcs9/4',
                                    'mcs10/3',
                                    'mcs11/3',
                                    'mcs10/4',
                                    'mcs11/4'
                                ]
                            }
                        },
                        'rates-11bg': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    '1',
                                    '1-basic',
                                    '2',
                                    '2-basic',
                                    '5.5',
                                    '5.5-basic',
                                    '6',
                                    '6-basic',
                                    '9',
                                    '9-basic',
                                    '12',
                                    '12-basic',
                                    '18',
                                    '18-basic',
                                    '24',
                                    '24-basic',
                                    '36',
                                    '36-basic',
                                    '48',
                                    '48-basic',
                                    '54',
                                    '54-basic',
                                    '11',
                                    '11-basic'
                                ]
                            }
                        },
                        'rates-11n-ss12': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'mcs0/1',
                                    'mcs1/1',
                                    'mcs2/1',
                                    'mcs3/1',
                                    'mcs4/1',
                                    'mcs5/1',
                                    'mcs6/1',
                                    'mcs7/1',
                                    'mcs8/2',
                                    'mcs9/2',
                                    'mcs10/2',
                                    'mcs11/2',
                                    'mcs12/2',
                                    'mcs13/2',
                                    'mcs14/2',
                                    'mcs15/2'
                                ]
                            }
                        },
                        'rates-11n-ss34': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'mcs16/3',
                                    'mcs17/3',
                                    'mcs18/3',
                                    'mcs19/3',
                                    'mcs20/3',
                                    'mcs21/3',
                                    'mcs22/3',
                                    'mcs23/3',
                                    'mcs24/4',
                                    'mcs25/4',
                                    'mcs26/4',
                                    'mcs27/4',
                                    'mcs28/4',
                                    'mcs29/4',
                                    'mcs30/4',
                                    'mcs31/4'
                                ]
                            }
                        },
                        'sae-groups': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    '1',
                                    '2',
                                    '5',
                                    '14',
                                    '15',
                                    '16',
                                    '17',
                                    '18',
                                    '19',
                                    '20',
                                    '21',
                                    '27',
                                    '28',
                                    '29',
                                    '30',
                                    '31'
                                ]
                            }
                        },
                        'sae-password': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'schedule': {
                            'type': 'string'
                        },
                        'security': {
                            'type': 'string',
                            'enum': [
                                'None',
                                'WEP64',
                                'wep64',
                                'WEP128',
                                'wep128',
                                'WPA_PSK',
                                'WPA_RADIUS',
                                'WPA',
                                'WPA2',
                                'WPA2_AUTO',
                                'open',
                                'wpa-personal',
                                'wpa-enterprise',
                                'captive-portal',
                                'wpa-only-personal',
                                'wpa-only-enterprise',
                                'wpa2-only-personal',
                                'wpa2-only-enterprise',
                                'wpa-personal+captive-portal',
                                'wpa-only-personal+captive-portal',
                                'wpa2-only-personal+captive-portal',
                                'osen',
                                'wpa3-enterprise',
                                'sae',
                                'sae-transition',
                                'owe',
                                'wpa3-sae',
                                'wpa3-sae-transition'
                            ]
                        },
                        'security-exempt-list': {
                            'type': 'string'
                        },
                        'security-obsolete-option': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'security-redirect-url': {
                            'type': 'string'
                        },
                        'selected-usergroups': {
                            'type': 'string'
                        },
                        'split-tunneling': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ssid': {
                            'type': 'string'
                        },
                        'tkip-counter-measure': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'usergroup': {
                            'type': 'string'
                        },
                        'utm-profile': {
                            'type': 'string'
                        },
                        'vdom': {
                            'type': 'string'
                        },
                        'vlan-auto': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'vlan-pooling': {
                            'type': 'string',
                            'enum': [
                                'wtp-group',
                                'round-robin',
                                'hash',
                                'disable'
                            ]
                        },
                        'vlanid': {
                            'type': 'integer'
                        },
                        'voice-enterprise': {
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
