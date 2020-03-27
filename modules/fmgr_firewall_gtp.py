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
module: fmgr_firewall_gtp
short_description: Configure GTP.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/firewall/gtp
    - /pm/config/global/obj/firewall/gtp
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
    schema_object0:
        methods: [add, set, update]
        description: 'Configure GTP.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    addr-notify:
                        type: str
                        description: 'overbilling notify address'
                    apn:
                        -
                            action:
                                type: str
                                description: 'Action.'
                                choices:
                                    - 'allow'
                                    - 'deny'
                            apnmember:
                                type: str
                                description: 'APN member.'
                            id:
                                type: int
                                description: 'ID.'
                            selection-mode:
                                -
                                    type: str
                                    choices:
                                        - 'ms'
                                        - 'net'
                                        - 'vrf'
                    apn-filter:
                        type: str
                        description: 'apn filter'
                        choices:
                            - 'disable'
                            - 'enable'
                    authorized-ggsns:
                        type: str
                        description: 'Authorized GGSN group'
                    authorized-sgsns:
                        type: str
                        description: 'Authorized SGSN group'
                    comment:
                        type: str
                        description: 'Comment.'
                    context-id:
                        type: int
                        description: 'Overbilling context.'
                    control-plane-message-rate-limit:
                        type: int
                        description: 'control plane message rate limit'
                    default-apn-action:
                        type: str
                        description: 'default apn action'
                        choices:
                            - 'allow'
                            - 'deny'
                    default-imsi-action:
                        type: str
                        description: 'default imsi action'
                        choices:
                            - 'allow'
                            - 'deny'
                    default-ip-action:
                        type: str
                        description: 'default action for encapsulated IP traffic'
                        choices:
                            - 'allow'
                            - 'deny'
                    default-noip-action:
                        type: str
                        description: 'default action for encapsulated non-IP traffic'
                        choices:
                            - 'allow'
                            - 'deny'
                    default-policy-action:
                        type: str
                        description: 'default advanced policy action'
                        choices:
                            - 'allow'
                            - 'deny'
                    denied-log:
                        type: str
                        description: 'log denied'
                        choices:
                            - 'disable'
                            - 'enable'
                    echo-request-interval:
                        type: int
                        description: 'echo request interval (in seconds)'
                    extension-log:
                        type: str
                        description: 'log in extension format'
                        choices:
                            - 'disable'
                            - 'enable'
                    forwarded-log:
                        type: str
                        description: 'log forwarded'
                        choices:
                            - 'disable'
                            - 'enable'
                    global-tunnel-limit:
                        type: str
                        description: 'Global tunnel limit.'
                    gtp-in-gtp:
                        type: str
                        description: 'gtp in gtp'
                        choices:
                            - 'allow'
                            - 'deny'
                    gtpu-denied-log:
                        type: str
                        description: 'Enable/disable logging of denied GTP-U packets.'
                        choices:
                            - 'disable'
                            - 'enable'
                    gtpu-forwarded-log:
                        type: str
                        description: 'Enable/disable logging of forwarded GTP-U packets.'
                        choices:
                            - 'disable'
                            - 'enable'
                    gtpu-log-freq:
                        type: int
                        description: 'Logging of frequency of GTP-U packets.'
                    half-close-timeout:
                        type: int
                        description: 'Half-close tunnel timeout (in seconds).'
                    half-open-timeout:
                        type: int
                        description: 'Half-open tunnel timeout (in seconds).'
                    handover-group:
                        type: str
                        description: 'Handover SGSN group'
                    ie-remove-policy:
                        -
                            id:
                                type: int
                                description: 'ID.'
                            remove-ies:
                                -
                                    type: str
                                    choices:
                                        - 'apn-restriction'
                                        - 'rat-type'
                                        - 'rai'
                                        - 'uli'
                                        - 'imei'
                            sgsn-addr:
                                type: str
                                description: 'SGSN address name.'
                    ie-remover:
                        type: str
                        description: 'IE removal policy.'
                        choices:
                            - 'disable'
                            - 'enable'
                    ie-white-list-v0v1:
                        type: str
                        description: 'IE white list.'
                    ie-white-list-v2:
                        type: str
                        description: 'IE white list.'
                    imsi:
                        -
                            action:
                                type: str
                                description: 'Action.'
                                choices:
                                    - 'allow'
                                    - 'deny'
                            apnmember:
                                type: str
                                description: 'APN member.'
                            id:
                                type: int
                                description: 'ID.'
                            mcc-mnc:
                                type: str
                                description: 'MCC MNC.'
                            msisdn-prefix:
                                type: str
                                description: 'MSISDN prefix.'
                            selection-mode:
                                -
                                    type: str
                                    choices:
                                        - 'ms'
                                        - 'net'
                                        - 'vrf'
                    imsi-filter:
                        type: str
                        description: 'imsi filter'
                        choices:
                            - 'disable'
                            - 'enable'
                    interface-notify:
                        type: str
                        description: 'overbilling interface'
                    invalid-reserved-field:
                        type: str
                        description: 'Invalid reserved field in GTP header'
                        choices:
                            - 'allow'
                            - 'deny'
                    invalid-sgsns-to-log:
                        type: str
                        description: 'Invalid SGSN group to be logged'
                    ip-filter:
                        type: str
                        description: 'IP filter for encapsulted traffic'
                        choices:
                            - 'disable'
                            - 'enable'
                    ip-policy:
                        -
                            action:
                                type: str
                                description: 'Action.'
                                choices:
                                    - 'allow'
                                    - 'deny'
                            dstaddr:
                                type: str
                                description: 'Destination address name.'
                            id:
                                type: int
                                description: 'ID.'
                            srcaddr:
                                type: str
                                description: 'Source address name.'
                    log-freq:
                        type: int
                        description: 'Logging of frequency of GTP-C packets.'
                    log-gtpu-limit:
                        type: int
                        description: 'the user data log limit (0-512 bytes)'
                    log-imsi-prefix:
                        type: str
                        description: 'IMSI prefix for selective logging.'
                    log-msisdn-prefix:
                        type: str
                        description: 'the msisdn prefix for selective logging'
                    max-message-length:
                        type: int
                        description: 'max message length'
                    message-filter-v0v1:
                        type: str
                        description: 'Message filter.'
                    message-filter-v2:
                        type: str
                        description: 'Message filter.'
                    min-message-length:
                        type: int
                        description: 'min message length'
                    miss-must-ie:
                        type: str
                        description: 'Missing mandatory information element'
                        choices:
                            - 'allow'
                            - 'deny'
                    monitor-mode:
                        type: str
                        description: 'GTP monitor mode'
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'vdom'
                    name:
                        type: str
                        description: 'Profile name.'
                    noip-filter:
                        type: str
                        description: 'non-IP filter for encapsulted traffic'
                        choices:
                            - 'disable'
                            - 'enable'
                    noip-policy:
                        -
                            action:
                                type: str
                                description: 'Action.'
                                choices:
                                    - 'allow'
                                    - 'deny'
                            end:
                                type: int
                                description: 'End of protocol range (0 - 255).'
                            id:
                                type: int
                                description: 'ID.'
                            start:
                                type: int
                                description: 'Start of protocol range (0 - 255).'
                            type:
                                type: str
                                description: 'Protocol field type.'
                                choices:
                                    - 'etsi'
                                    - 'ietf'
                    out-of-state-ie:
                        type: str
                        description: 'Out of state information element.'
                        choices:
                            - 'allow'
                            - 'deny'
                    out-of-state-message:
                        type: str
                        description: 'Out of state GTP message'
                        choices:
                            - 'allow'
                            - 'deny'
                    per-apn-shaper:
                        -
                            apn:
                                type: str
                                description: 'APN name.'
                            id:
                                type: int
                                description: 'ID.'
                            rate-limit:
                                type: int
                                description: 'Rate limit (packets/s) for create PDP context request.'
                            version:
                                type: int
                                description: 'GTP version number: 0 or 1.'
                    policy:
                        -
                            action:
                                type: str
                                description: 'Action.'
                                choices:
                                    - 'allow'
                                    - 'deny'
                            apn-sel-mode:
                                -
                                    type: str
                                    choices:
                                        - 'ms'
                                        - 'net'
                                        - 'vrf'
                            apnmember:
                                type: str
                                description: 'APN member.'
                            id:
                                type: int
                                description: 'ID.'
                            imei:
                                type: str
                                description: 'IMEI(SV) pattern.'
                            imsi:
                                type: str
                                description: 'IMSI prefix.'
                            max-apn-restriction:
                                type: str
                                description: 'Maximum APN restriction value.'
                                choices:
                                    - 'all'
                                    - 'public-1'
                                    - 'public-2'
                                    - 'private-1'
                                    - 'private-2'
                            messages:
                                -
                                    type: str
                                    choices:
                                        - 'create-req'
                                        - 'create-res'
                                        - 'update-req'
                                        - 'update-res'
                            msisdn:
                                type: str
                                description: 'MSISDN prefix.'
                            rai:
                                type: str
                                description: 'RAI pattern.'
                            rat-type:
                                -
                                    type: str
                                    choices:
                                        - 'any'
                                        - 'utran'
                                        - 'geran'
                                        - 'wlan'
                                        - 'gan'
                                        - 'hspa'
                                        - 'eutran'
                                        - 'virtual'
                                        - 'nbiot'
                            uli:
                                type: str
                                description: 'ULI pattern.'
                    policy-filter:
                        type: str
                        description: 'Advanced policy filter'
                        choices:
                            - 'disable'
                            - 'enable'
                    port-notify:
                        type: int
                        description: 'overbilling notify port'
                    rate-limit-mode:
                        type: str
                        description: 'GTP rate limit mode.'
                        choices:
                            - 'per-profile'
                            - 'per-stream'
                            - 'per-apn'
                    rate-limited-log:
                        type: str
                        description: 'log rate limited'
                        choices:
                            - 'disable'
                            - 'enable'
                    rate-sampling-interval:
                        type: int
                        description: 'rate sampling interval (1-3600 seconds)'
                    remove-if-echo-expires:
                        type: str
                        description: 'remove if echo response expires'
                        choices:
                            - 'disable'
                            - 'enable'
                    remove-if-recovery-differ:
                        type: str
                        description: 'remove upon different Recovery IE'
                        choices:
                            - 'disable'
                            - 'enable'
                    reserved-ie:
                        type: str
                        description: 'reserved information element'
                        choices:
                            - 'allow'
                            - 'deny'
                    send-delete-when-timeout:
                        type: str
                        description: 'send DELETE request to path endpoints when GTPv0/v1 tunnel timeout.'
                        choices:
                            - 'disable'
                            - 'enable'
                    send-delete-when-timeout-v2:
                        type: str
                        description: 'send DELETE request to path endpoints when GTPv2 tunnel timeout.'
                        choices:
                            - 'disable'
                            - 'enable'
                    spoof-src-addr:
                        type: str
                        description: 'Spoofed source address for Mobile Station.'
                        choices:
                            - 'allow'
                            - 'deny'
                    state-invalid-log:
                        type: str
                        description: 'log state invalid'
                        choices:
                            - 'disable'
                            - 'enable'
                    traffic-count-log:
                        type: str
                        description: 'log tunnel traffic counter'
                        choices:
                            - 'disable'
                            - 'enable'
                    tunnel-limit:
                        type: int
                        description: 'tunnel limit'
                    tunnel-limit-log:
                        type: str
                        description: 'tunnel limit'
                        choices:
                            - 'disable'
                            - 'enable'
                    tunnel-timeout:
                        type: int
                        description: 'Established tunnel timeout (in seconds).'
                    unknown-version-action:
                        type: str
                        description: 'action for unknown gtp version'
                        choices:
                            - 'allow'
                            - 'deny'
                    user-plane-message-rate-limit:
                        type: int
                        description: 'user plane message rate limit'
                    warning-threshold:
                        type: int
                        description: 'Warning threshold for rate limiting (0 - 99 percent).'
    schema_object1:
        methods: [get]
        description: 'Configure GTP.'
        api_categories: [api_tag0]
        api_tag0:
            attr:
                type: str
                description: 'The name of the attribute to retrieve its datasource. Only used with &lt;i&gt;datasrc&lt;/i&gt; option.'
            fields:
                -
                    -
                        type: str
                        choices:
                            - 'addr-notify'
                            - 'apn-filter'
                            - 'authorized-ggsns'
                            - 'authorized-sgsns'
                            - 'comment'
                            - 'context-id'
                            - 'control-plane-message-rate-limit'
                            - 'default-apn-action'
                            - 'default-imsi-action'
                            - 'default-ip-action'
                            - 'default-noip-action'
                            - 'default-policy-action'
                            - 'denied-log'
                            - 'echo-request-interval'
                            - 'extension-log'
                            - 'forwarded-log'
                            - 'global-tunnel-limit'
                            - 'gtp-in-gtp'
                            - 'gtpu-denied-log'
                            - 'gtpu-forwarded-log'
                            - 'gtpu-log-freq'
                            - 'half-close-timeout'
                            - 'half-open-timeout'
                            - 'handover-group'
                            - 'ie-remover'
                            - 'ie-white-list-v0v1'
                            - 'ie-white-list-v2'
                            - 'imsi-filter'
                            - 'interface-notify'
                            - 'invalid-reserved-field'
                            - 'invalid-sgsns-to-log'
                            - 'ip-filter'
                            - 'log-freq'
                            - 'log-gtpu-limit'
                            - 'log-imsi-prefix'
                            - 'log-msisdn-prefix'
                            - 'max-message-length'
                            - 'message-filter-v0v1'
                            - 'message-filter-v2'
                            - 'min-message-length'
                            - 'miss-must-ie'
                            - 'monitor-mode'
                            - 'name'
                            - 'noip-filter'
                            - 'out-of-state-ie'
                            - 'out-of-state-message'
                            - 'policy-filter'
                            - 'port-notify'
                            - 'rate-limit-mode'
                            - 'rate-limited-log'
                            - 'rate-sampling-interval'
                            - 'remove-if-echo-expires'
                            - 'remove-if-recovery-differ'
                            - 'reserved-ie'
                            - 'send-delete-when-timeout'
                            - 'send-delete-when-timeout-v2'
                            - 'spoof-src-addr'
                            - 'state-invalid-log'
                            - 'traffic-count-log'
                            - 'tunnel-limit'
                            - 'tunnel-limit-log'
                            - 'tunnel-timeout'
                            - 'unknown-version-action'
                            - 'user-plane-message-rate-limit'
                            - 'warning-threshold'
            filter:
                -
                    type: str
            get used:
                type: int
            loadsub:
                type: int
                description: 'Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.'
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.'
                 - 'count - Return the number of matching entries instead of the actual entry data.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'datasrc - Return all objects that can be referenced by an attribute. Require <i>attr</i> parameter.'
                 - 'get reserved - Also return reserved objects in the result.'
                 - 'syntax - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.'
                choices:
                    - 'count'
                    - 'object member'
                    - 'datasrc'
                    - 'get reserved'
                    - 'syntax'
            range:
                -
                    type: int
            sortings:
                -
                    varidic.attr_name:
                        type: int
                        choices:
                            - 1
                            - -1

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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/GTP
      fmgr_firewall_gtp:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     addr-notify: <value of string>
                     apn:
                       -
                           action: <value in [allow, deny]>
                           apnmember: <value of string>
                           id: <value of integer>
                           selection-mode:
                             - <value in [ms, net, vrf]>
                     apn-filter: <value in [disable, enable]>
                     authorized-ggsns: <value of string>
                     authorized-sgsns: <value of string>
                     comment: <value of string>
                     context-id: <value of integer>
                     control-plane-message-rate-limit: <value of integer>
                     default-apn-action: <value in [allow, deny]>
                     default-imsi-action: <value in [allow, deny]>
                     default-ip-action: <value in [allow, deny]>
                     default-noip-action: <value in [allow, deny]>
                     default-policy-action: <value in [allow, deny]>
                     denied-log: <value in [disable, enable]>
                     echo-request-interval: <value of integer>
                     extension-log: <value in [disable, enable]>
                     forwarded-log: <value in [disable, enable]>
                     global-tunnel-limit: <value of string>
                     gtp-in-gtp: <value in [allow, deny]>
                     gtpu-denied-log: <value in [disable, enable]>
                     gtpu-forwarded-log: <value in [disable, enable]>
                     gtpu-log-freq: <value of integer>
                     half-close-timeout: <value of integer>
                     half-open-timeout: <value of integer>
                     handover-group: <value of string>
                     ie-remove-policy:
                       -
                           id: <value of integer>
                           remove-ies:
                             - <value in [apn-restriction, rat-type, rai, ...]>
                           sgsn-addr: <value of string>
                     ie-remover: <value in [disable, enable]>
                     ie-white-list-v0v1: <value of string>
                     ie-white-list-v2: <value of string>
                     imsi:
                       -
                           action: <value in [allow, deny]>
                           apnmember: <value of string>
                           id: <value of integer>
                           mcc-mnc: <value of string>
                           msisdn-prefix: <value of string>
                           selection-mode:
                             - <value in [ms, net, vrf]>
                     imsi-filter: <value in [disable, enable]>
                     interface-notify: <value of string>
                     invalid-reserved-field: <value in [allow, deny]>
                     invalid-sgsns-to-log: <value of string>
                     ip-filter: <value in [disable, enable]>
                     ip-policy:
                       -
                           action: <value in [allow, deny]>
                           dstaddr: <value of string>
                           id: <value of integer>
                           srcaddr: <value of string>
                     log-freq: <value of integer>
                     log-gtpu-limit: <value of integer>
                     log-imsi-prefix: <value of string>
                     log-msisdn-prefix: <value of string>
                     max-message-length: <value of integer>
                     message-filter-v0v1: <value of string>
                     message-filter-v2: <value of string>
                     min-message-length: <value of integer>
                     miss-must-ie: <value in [allow, deny]>
                     monitor-mode: <value in [disable, enable, vdom]>
                     name: <value of string>
                     noip-filter: <value in [disable, enable]>
                     noip-policy:
                       -
                           action: <value in [allow, deny]>
                           end: <value of integer>
                           id: <value of integer>
                           start: <value of integer>
                           type: <value in [etsi, ietf]>
                     out-of-state-ie: <value in [allow, deny]>
                     out-of-state-message: <value in [allow, deny]>
                     per-apn-shaper:
                       -
                           apn: <value of string>
                           id: <value of integer>
                           rate-limit: <value of integer>
                           version: <value of integer>
                     policy:
                       -
                           action: <value in [allow, deny]>
                           apn-sel-mode:
                             - <value in [ms, net, vrf]>
                           apnmember: <value of string>
                           id: <value of integer>
                           imei: <value of string>
                           imsi: <value of string>
                           max-apn-restriction: <value in [all, public-1, public-2, ...]>
                           messages:
                             - <value in [create-req, create-res, update-req, ...]>
                           msisdn: <value of string>
                           rai: <value of string>
                           rat-type:
                             - <value in [any, utran, geran, ...]>
                           uli: <value of string>
                     policy-filter: <value in [disable, enable]>
                     port-notify: <value of integer>
                     rate-limit-mode: <value in [per-profile, per-stream, per-apn]>
                     rate-limited-log: <value in [disable, enable]>
                     rate-sampling-interval: <value of integer>
                     remove-if-echo-expires: <value in [disable, enable]>
                     remove-if-recovery-differ: <value in [disable, enable]>
                     reserved-ie: <value in [allow, deny]>
                     send-delete-when-timeout: <value in [disable, enable]>
                     send-delete-when-timeout-v2: <value in [disable, enable]>
                     spoof-src-addr: <value in [allow, deny]>
                     state-invalid-log: <value in [disable, enable]>
                     traffic-count-log: <value in [disable, enable]>
                     tunnel-limit: <value of integer>
                     tunnel-limit-log: <value in [disable, enable]>
                     tunnel-timeout: <value of integer>
                     unknown-version-action: <value in [allow, deny]>
                     user-plane-message-rate-limit: <value of integer>
                     warning-threshold: <value of integer>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/GTP
      fmgr_firewall_gtp:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [addr-notify, apn-filter, authorized-ggsns, ...]>
               filter:
                 - <value of string>
               get used: <value of integer>
               loadsub: <value of integer>
               option: <value in [count, object member, datasrc, ...]>
               range:
                 - <value of integer>
               sortings:
                 -
                     varidic.attr_name: <value in [1, -1]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[add, set, update]
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
            example: '/pm/config/adom/{adom}/obj/firewall/gtp'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            type: array
            suboptions:
               addr-notify:
                  type: str
                  description: 'overbilling notify address'
               apn:
                  type: array
                  suboptions:
                     action:
                        type: str
                        description: 'Action.'
                     apnmember:
                        type: str
                        description: 'APN member.'
                     id:
                        type: int
                        description: 'ID.'
                     selection-mode:
                        type: array
                        suboptions:
                           type: str
               apn-filter:
                  type: str
                  description: 'apn filter'
               authorized-ggsns:
                  type: str
                  description: 'Authorized GGSN group'
               authorized-sgsns:
                  type: str
                  description: 'Authorized SGSN group'
               comment:
                  type: str
                  description: 'Comment.'
               context-id:
                  type: int
                  description: 'Overbilling context.'
               control-plane-message-rate-limit:
                  type: int
                  description: 'control plane message rate limit'
               default-apn-action:
                  type: str
                  description: 'default apn action'
               default-imsi-action:
                  type: str
                  description: 'default imsi action'
               default-ip-action:
                  type: str
                  description: 'default action for encapsulated IP traffic'
               default-noip-action:
                  type: str
                  description: 'default action for encapsulated non-IP traffic'
               default-policy-action:
                  type: str
                  description: 'default advanced policy action'
               denied-log:
                  type: str
                  description: 'log denied'
               echo-request-interval:
                  type: int
                  description: 'echo request interval (in seconds)'
               extension-log:
                  type: str
                  description: 'log in extension format'
               forwarded-log:
                  type: str
                  description: 'log forwarded'
               global-tunnel-limit:
                  type: str
                  description: 'Global tunnel limit.'
               gtp-in-gtp:
                  type: str
                  description: 'gtp in gtp'
               gtpu-denied-log:
                  type: str
                  description: 'Enable/disable logging of denied GTP-U packets.'
               gtpu-forwarded-log:
                  type: str
                  description: 'Enable/disable logging of forwarded GTP-U packets.'
               gtpu-log-freq:
                  type: int
                  description: 'Logging of frequency of GTP-U packets.'
               half-close-timeout:
                  type: int
                  description: 'Half-close tunnel timeout (in seconds).'
               half-open-timeout:
                  type: int
                  description: 'Half-open tunnel timeout (in seconds).'
               handover-group:
                  type: str
                  description: 'Handover SGSN group'
               ie-remove-policy:
                  type: array
                  suboptions:
                     id:
                        type: int
                        description: 'ID.'
                     remove-ies:
                        type: array
                        suboptions:
                           type: str
                     sgsn-addr:
                        type: str
                        description: 'SGSN address name.'
               ie-remover:
                  type: str
                  description: 'IE removal policy.'
               ie-white-list-v0v1:
                  type: str
                  description: 'IE white list.'
               ie-white-list-v2:
                  type: str
                  description: 'IE white list.'
               imsi:
                  type: array
                  suboptions:
                     action:
                        type: str
                        description: 'Action.'
                     apnmember:
                        type: str
                        description: 'APN member.'
                     id:
                        type: int
                        description: 'ID.'
                     mcc-mnc:
                        type: str
                        description: 'MCC MNC.'
                     msisdn-prefix:
                        type: str
                        description: 'MSISDN prefix.'
                     selection-mode:
                        type: array
                        suboptions:
                           type: str
               imsi-filter:
                  type: str
                  description: 'imsi filter'
               interface-notify:
                  type: str
                  description: 'overbilling interface'
               invalid-reserved-field:
                  type: str
                  description: 'Invalid reserved field in GTP header'
               invalid-sgsns-to-log:
                  type: str
                  description: 'Invalid SGSN group to be logged'
               ip-filter:
                  type: str
                  description: 'IP filter for encapsulted traffic'
               ip-policy:
                  type: array
                  suboptions:
                     action:
                        type: str
                        description: 'Action.'
                     dstaddr:
                        type: str
                        description: 'Destination address name.'
                     id:
                        type: int
                        description: 'ID.'
                     srcaddr:
                        type: str
                        description: 'Source address name.'
               log-freq:
                  type: int
                  description: 'Logging of frequency of GTP-C packets.'
               log-gtpu-limit:
                  type: int
                  description: 'the user data log limit (0-512 bytes)'
               log-imsi-prefix:
                  type: str
                  description: 'IMSI prefix for selective logging.'
               log-msisdn-prefix:
                  type: str
                  description: 'the msisdn prefix for selective logging'
               max-message-length:
                  type: int
                  description: 'max message length'
               message-filter-v0v1:
                  type: str
                  description: 'Message filter.'
               message-filter-v2:
                  type: str
                  description: 'Message filter.'
               min-message-length:
                  type: int
                  description: 'min message length'
               miss-must-ie:
                  type: str
                  description: 'Missing mandatory information element'
               monitor-mode:
                  type: str
                  description: 'GTP monitor mode'
               name:
                  type: str
                  description: 'Profile name.'
               noip-filter:
                  type: str
                  description: 'non-IP filter for encapsulted traffic'
               noip-policy:
                  type: array
                  suboptions:
                     action:
                        type: str
                        description: 'Action.'
                     end:
                        type: int
                        description: 'End of protocol range (0 - 255).'
                     id:
                        type: int
                        description: 'ID.'
                     start:
                        type: int
                        description: 'Start of protocol range (0 - 255).'
                     type:
                        type: str
                        description: 'Protocol field type.'
               out-of-state-ie:
                  type: str
                  description: 'Out of state information element.'
               out-of-state-message:
                  type: str
                  description: 'Out of state GTP message'
               per-apn-shaper:
                  type: array
                  suboptions:
                     apn:
                        type: str
                        description: 'APN name.'
                     id:
                        type: int
                        description: 'ID.'
                     rate-limit:
                        type: int
                        description: 'Rate limit (packets/s) for create PDP context request.'
                     version:
                        type: int
                        description: 'GTP version number: 0 or 1.'
               policy:
                  type: array
                  suboptions:
                     action:
                        type: str
                        description: 'Action.'
                     apn-sel-mode:
                        type: array
                        suboptions:
                           type: str
                     apnmember:
                        type: str
                        description: 'APN member.'
                     id:
                        type: int
                        description: 'ID.'
                     imei:
                        type: str
                        description: 'IMEI(SV) pattern.'
                     imsi:
                        type: str
                        description: 'IMSI prefix.'
                     max-apn-restriction:
                        type: str
                        description: 'Maximum APN restriction value.'
                     messages:
                        type: array
                        suboptions:
                           type: str
                     msisdn:
                        type: str
                        description: 'MSISDN prefix.'
                     rai:
                        type: str
                        description: 'RAI pattern.'
                     rat-type:
                        type: array
                        suboptions:
                           type: str
                     uli:
                        type: str
                        description: 'ULI pattern.'
               policy-filter:
                  type: str
                  description: 'Advanced policy filter'
               port-notify:
                  type: int
                  description: 'overbilling notify port'
               rate-limit-mode:
                  type: str
                  description: 'GTP rate limit mode.'
               rate-limited-log:
                  type: str
                  description: 'log rate limited'
               rate-sampling-interval:
                  type: int
                  description: 'rate sampling interval (1-3600 seconds)'
               remove-if-echo-expires:
                  type: str
                  description: 'remove if echo response expires'
               remove-if-recovery-differ:
                  type: str
                  description: 'remove upon different Recovery IE'
               reserved-ie:
                  type: str
                  description: 'reserved information element'
               send-delete-when-timeout:
                  type: str
                  description: 'send DELETE request to path endpoints when GTPv0/v1 tunnel timeout.'
               send-delete-when-timeout-v2:
                  type: str
                  description: 'send DELETE request to path endpoints when GTPv2 tunnel timeout.'
               spoof-src-addr:
                  type: str
                  description: 'Spoofed source address for Mobile Station.'
               state-invalid-log:
                  type: str
                  description: 'log state invalid'
               traffic-count-log:
                  type: str
                  description: 'log tunnel traffic counter'
               tunnel-limit:
                  type: int
                  description: 'tunnel limit'
               tunnel-limit-log:
                  type: str
                  description: 'tunnel limit'
               tunnel-timeout:
                  type: int
                  description: 'Established tunnel timeout (in seconds).'
               unknown-version-action:
                  type: str
                  description: 'action for unknown gtp version'
               user-plane-message-rate-limit:
                  type: int
                  description: 'user plane message rate limit'
               warning-threshold:
                  type: int
                  description: 'Warning threshold for rate limiting (0 - 99 percent).'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/firewall/gtp'

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
        '/pm/config/adom/{adom}/obj/firewall/gtp',
        '/pm/config/global/obj/firewall/gtp'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'addr-notify': {
                            'type': 'string'
                        },
                        'apn': {
                            'type': 'array',
                            'items': {
                                'action': {
                                    'type': 'string',
                                    'enum': [
                                        'allow',
                                        'deny'
                                    ]
                                },
                                'apnmember': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'selection-mode': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string',
                                        'enum': [
                                            'ms',
                                            'net',
                                            'vrf'
                                        ]
                                    }
                                }
                            }
                        },
                        'apn-filter': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'authorized-ggsns': {
                            'type': 'string'
                        },
                        'authorized-sgsns': {
                            'type': 'string'
                        },
                        'comment': {
                            'type': 'string'
                        },
                        'context-id': {
                            'type': 'integer'
                        },
                        'control-plane-message-rate-limit': {
                            'type': 'integer'
                        },
                        'default-apn-action': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'default-imsi-action': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'default-ip-action': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'default-noip-action': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'default-policy-action': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'denied-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'echo-request-interval': {
                            'type': 'integer'
                        },
                        'extension-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'forwarded-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'global-tunnel-limit': {
                            'type': 'string'
                        },
                        'gtp-in-gtp': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'gtpu-denied-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'gtpu-forwarded-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'gtpu-log-freq': {
                            'type': 'integer'
                        },
                        'half-close-timeout': {
                            'type': 'integer'
                        },
                        'half-open-timeout': {
                            'type': 'integer'
                        },
                        'handover-group': {
                            'type': 'string'
                        },
                        'ie-remove-policy': {
                            'type': 'array',
                            'items': {
                                'id': {
                                    'type': 'integer'
                                },
                                'remove-ies': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string',
                                        'enum': [
                                            'apn-restriction',
                                            'rat-type',
                                            'rai',
                                            'uli',
                                            'imei'
                                        ]
                                    }
                                },
                                'sgsn-addr': {
                                    'type': 'string'
                                }
                            }
                        },
                        'ie-remover': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ie-white-list-v0v1': {
                            'type': 'string'
                        },
                        'ie-white-list-v2': {
                            'type': 'string'
                        },
                        'imsi': {
                            'type': 'array',
                            'items': {
                                'action': {
                                    'type': 'string',
                                    'enum': [
                                        'allow',
                                        'deny'
                                    ]
                                },
                                'apnmember': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'mcc-mnc': {
                                    'type': 'string'
                                },
                                'msisdn-prefix': {
                                    'type': 'string'
                                },
                                'selection-mode': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string',
                                        'enum': [
                                            'ms',
                                            'net',
                                            'vrf'
                                        ]
                                    }
                                }
                            }
                        },
                        'imsi-filter': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'interface-notify': {
                            'type': 'string'
                        },
                        'invalid-reserved-field': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'invalid-sgsns-to-log': {
                            'type': 'string'
                        },
                        'ip-filter': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ip-policy': {
                            'type': 'array',
                            'items': {
                                'action': {
                                    'type': 'string',
                                    'enum': [
                                        'allow',
                                        'deny'
                                    ]
                                },
                                'dstaddr': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'srcaddr': {
                                    'type': 'string'
                                }
                            }
                        },
                        'log-freq': {
                            'type': 'integer'
                        },
                        'log-gtpu-limit': {
                            'type': 'integer'
                        },
                        'log-imsi-prefix': {
                            'type': 'string'
                        },
                        'log-msisdn-prefix': {
                            'type': 'string'
                        },
                        'max-message-length': {
                            'type': 'integer'
                        },
                        'message-filter-v0v1': {
                            'type': 'string'
                        },
                        'message-filter-v2': {
                            'type': 'string'
                        },
                        'min-message-length': {
                            'type': 'integer'
                        },
                        'miss-must-ie': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'monitor-mode': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable',
                                'vdom'
                            ]
                        },
                        'name': {
                            'type': 'string'
                        },
                        'noip-filter': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'noip-policy': {
                            'type': 'array',
                            'items': {
                                'action': {
                                    'type': 'string',
                                    'enum': [
                                        'allow',
                                        'deny'
                                    ]
                                },
                                'end': {
                                    'type': 'integer'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'start': {
                                    'type': 'integer'
                                },
                                'type': {
                                    'type': 'string',
                                    'enum': [
                                        'etsi',
                                        'ietf'
                                    ]
                                }
                            }
                        },
                        'out-of-state-ie': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'out-of-state-message': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'per-apn-shaper': {
                            'type': 'array',
                            'items': {
                                'apn': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'rate-limit': {
                                    'type': 'integer'
                                },
                                'version': {
                                    'type': 'integer'
                                }
                            }
                        },
                        'policy': {
                            'type': 'array',
                            'items': {
                                'action': {
                                    'type': 'string',
                                    'enum': [
                                        'allow',
                                        'deny'
                                    ]
                                },
                                'apn-sel-mode': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string',
                                        'enum': [
                                            'ms',
                                            'net',
                                            'vrf'
                                        ]
                                    }
                                },
                                'apnmember': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'imei': {
                                    'type': 'string'
                                },
                                'imsi': {
                                    'type': 'string'
                                },
                                'max-apn-restriction': {
                                    'type': 'string',
                                    'enum': [
                                        'all',
                                        'public-1',
                                        'public-2',
                                        'private-1',
                                        'private-2'
                                    ]
                                },
                                'messages': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string',
                                        'enum': [
                                            'create-req',
                                            'create-res',
                                            'update-req',
                                            'update-res'
                                        ]
                                    }
                                },
                                'msisdn': {
                                    'type': 'string'
                                },
                                'rai': {
                                    'type': 'string'
                                },
                                'rat-type': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string',
                                        'enum': [
                                            'any',
                                            'utran',
                                            'geran',
                                            'wlan',
                                            'gan',
                                            'hspa',
                                            'eutran',
                                            'virtual',
                                            'nbiot'
                                        ]
                                    }
                                },
                                'uli': {
                                    'type': 'string'
                                }
                            }
                        },
                        'policy-filter': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'port-notify': {
                            'type': 'integer'
                        },
                        'rate-limit-mode': {
                            'type': 'string',
                            'enum': [
                                'per-profile',
                                'per-stream',
                                'per-apn'
                            ]
                        },
                        'rate-limited-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'rate-sampling-interval': {
                            'type': 'integer'
                        },
                        'remove-if-echo-expires': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'remove-if-recovery-differ': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'reserved-ie': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'send-delete-when-timeout': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'send-delete-when-timeout-v2': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'spoof-src-addr': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'state-invalid-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'traffic-count-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'tunnel-limit': {
                            'type': 'integer'
                        },
                        'tunnel-limit-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'tunnel-timeout': {
                            'type': 'integer'
                        },
                        'unknown-version-action': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'user-plane-message-rate-limit': {
                            'type': 'integer'
                        },
                        'warning-threshold': {
                            'type': 'integer'
                        }
                    }
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
                    'name': 'attr',
                    'api_tag': 0
                },
                {
                    'name': 'fields',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'enum': [
                                'addr-notify',
                                'apn-filter',
                                'authorized-ggsns',
                                'authorized-sgsns',
                                'comment',
                                'context-id',
                                'control-plane-message-rate-limit',
                                'default-apn-action',
                                'default-imsi-action',
                                'default-ip-action',
                                'default-noip-action',
                                'default-policy-action',
                                'denied-log',
                                'echo-request-interval',
                                'extension-log',
                                'forwarded-log',
                                'global-tunnel-limit',
                                'gtp-in-gtp',
                                'gtpu-denied-log',
                                'gtpu-forwarded-log',
                                'gtpu-log-freq',
                                'half-close-timeout',
                                'half-open-timeout',
                                'handover-group',
                                'ie-remover',
                                'ie-white-list-v0v1',
                                'ie-white-list-v2',
                                'imsi-filter',
                                'interface-notify',
                                'invalid-reserved-field',
                                'invalid-sgsns-to-log',
                                'ip-filter',
                                'log-freq',
                                'log-gtpu-limit',
                                'log-imsi-prefix',
                                'log-msisdn-prefix',
                                'max-message-length',
                                'message-filter-v0v1',
                                'message-filter-v2',
                                'min-message-length',
                                'miss-must-ie',
                                'monitor-mode',
                                'name',
                                'noip-filter',
                                'out-of-state-ie',
                                'out-of-state-message',
                                'policy-filter',
                                'port-notify',
                                'rate-limit-mode',
                                'rate-limited-log',
                                'rate-sampling-interval',
                                'remove-if-echo-expires',
                                'remove-if-recovery-differ',
                                'reserved-ie',
                                'send-delete-when-timeout',
                                'send-delete-when-timeout-v2',
                                'spoof-src-addr',
                                'state-invalid-log',
                                'traffic-count-log',
                                'tunnel-limit',
                                'tunnel-limit-log',
                                'tunnel-timeout',
                                'unknown-version-action',
                                'user-plane-message-rate-limit',
                                'warning-threshold'
                            ]
                        }
                    }
                },
                {
                    'name': 'filter',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'example': [
                                '<attr>',
                                '==',
                                'test'
                            ]
                        }
                    },
                    'api_tag': 0
                },
                {
                    'type': 'integer',
                    'name': 'get used',
                    'api_tag': 0
                },
                {
                    'type': 'integer',
                    'name': 'loadsub',
                    'api_tag': 0
                },
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'count',
                            'object member',
                            'datasrc',
                            'get reserved',
                            'syntax'
                        ]
                    },
                    'api_tag': 0
                },
                {
                    'name': 'range',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            'type': 'integer',
                            'example': [
                                2,
                                5
                            ]
                        }
                    },
                    'api_tag': 0
                },
                {
                    'name': 'sortings',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            '{attr_name}': {
                                'type': 'integer',
                                'enum': [
                                    1,
                                    -1
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
            'add': 'object0',
            'get': 'object1',
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
                'add',
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
