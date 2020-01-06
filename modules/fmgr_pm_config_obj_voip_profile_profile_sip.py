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
module: fmgr_pm_config_obj_voip_profile_profile_sip
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/voip/profile/{profile}/sip
    - /pm/config/global/obj/voip/profile/{profile}/sip
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
            profile:
                type: str
    schema_object0:
        methods: [get]
        description: 'SIP.'
        api_categories: [api_tag0]
        api_tag0:
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the object will be returned.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'chksum - Return the check-sum value instead of attributes.'
                choices:
                    - object member
                    - chksum
                    - datasrc
    schema_object1:
        methods: [set, update]
        description: 'SIP.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                ack-rate:
                    type: int
                    description: 'ACK request rate limit (per second, per policy).'
                block-ack:
                    type: str
                    description: 'Enable/disable block ACK requests.'
                    choices:
                        - disable
                        - enable
                block-bye:
                    type: str
                    description: 'Enable/disable block BYE requests.'
                    choices:
                        - disable
                        - enable
                block-cancel:
                    type: str
                    description: 'Enable/disable block CANCEL requests.'
                    choices:
                        - disable
                        - enable
                block-geo-red-options:
                    type: str
                    description: 'Enable/disable block OPTIONS requests, but OPTIONS requests still notify for redundancy.'
                    choices:
                        - disable
                        - enable
                block-info:
                    type: str
                    description: 'Enable/disable block INFO requests.'
                    choices:
                        - disable
                        - enable
                block-invite:
                    type: str
                    description: 'Enable/disable block INVITE requests.'
                    choices:
                        - disable
                        - enable
                block-long-lines:
                    type: str
                    description: 'Enable/disable block requests with headers exceeding max-line-length.'
                    choices:
                        - disable
                        - enable
                block-message:
                    type: str
                    description: 'Enable/disable block MESSAGE requests.'
                    choices:
                        - disable
                        - enable
                block-notify:
                    type: str
                    description: 'Enable/disable block NOTIFY requests.'
                    choices:
                        - disable
                        - enable
                block-options:
                    type: str
                    description: 'Enable/disable block OPTIONS requests and no OPTIONS as notifying message for redundancy either.'
                    choices:
                        - disable
                        - enable
                block-prack:
                    type: str
                    description: 'Enable/disable block prack requests.'
                    choices:
                        - disable
                        - enable
                block-publish:
                    type: str
                    description: 'Enable/disable block PUBLISH requests.'
                    choices:
                        - disable
                        - enable
                block-refer:
                    type: str
                    description: 'Enable/disable block REFER requests.'
                    choices:
                        - disable
                        - enable
                block-register:
                    type: str
                    description: 'Enable/disable block REGISTER requests.'
                    choices:
                        - disable
                        - enable
                block-subscribe:
                    type: str
                    description: 'Enable/disable block SUBSCRIBE requests.'
                    choices:
                        - disable
                        - enable
                block-unknown:
                    type: str
                    description: 'Block unrecognized SIP requests (enabled by default).'
                    choices:
                        - disable
                        - enable
                block-update:
                    type: str
                    description: 'Enable/disable block UPDATE requests.'
                    choices:
                        - disable
                        - enable
                bye-rate:
                    type: int
                    description: 'BYE request rate limit (per second, per policy).'
                call-keepalive:
                    type: int
                    description: 'Continue tracking calls with no RTP for this many minutes.'
                cancel-rate:
                    type: int
                    description: 'CANCEL request rate limit (per second, per policy).'
                contact-fixup:
                    type: str
                    description: 'Fixup contact anyway even if contact's IP:port doesn't match session's IP:port.'
                    choices:
                        - disable
                        - enable
                hnt-restrict-source-ip:
                    type: str
                    description: 'Enable/disable restrict RTP source IP to be the same as SIP source IP when HNT is enabled.'
                    choices:
                        - disable
                        - enable
                hosted-nat-traversal:
                    type: str
                    description: 'Hosted NAT Traversal (HNT).'
                    choices:
                        - disable
                        - enable
                info-rate:
                    type: int
                    description: 'INFO request rate limit (per second, per policy).'
                invite-rate:
                    type: int
                    description: 'INVITE request rate limit (per second, per policy).'
                ips-rtp:
                    type: str
                    description: 'Enable/disable allow IPS on RTP.'
                    choices:
                        - disable
                        - enable
                log-call-summary:
                    type: str
                    description: 'Enable/disable logging of SIP call summary.'
                    choices:
                        - disable
                        - enable
                log-violations:
                    type: str
                    description: 'Enable/disable logging of SIP violations.'
                    choices:
                        - disable
                        - enable
                malformed-header-allow:
                    type: str
                    description: 'Action for malformed Allow header.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-call-id:
                    type: str
                    description: 'Action for malformed Call-ID header.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-contact:
                    type: str
                    description: 'Action for malformed Contact header.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-content-length:
                    type: str
                    description: 'Action for malformed Content-Length header.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-content-type:
                    type: str
                    description: 'Action for malformed Content-Type header.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-cseq:
                    type: str
                    description: 'Action for malformed CSeq header.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-expires:
                    type: str
                    description: 'Action for malformed Expires header.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-from:
                    type: str
                    description: 'Action for malformed From header.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-max-forwards:
                    type: str
                    description: 'Action for malformed Max-Forwards header.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-p-asserted-identity:
                    type: str
                    description: 'Action for malformed P-Asserted-Identity header.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-rack:
                    type: str
                    description: 'Action for malformed RAck header.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-record-route:
                    type: str
                    description: 'Action for malformed Record-Route header.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-route:
                    type: str
                    description: 'Action for malformed Route header.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-rseq:
                    type: str
                    description: 'Action for malformed RSeq header.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-sdp-a:
                    type: str
                    description: 'Action for malformed SDP a line.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-sdp-b:
                    type: str
                    description: 'Action for malformed SDP b line.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-sdp-c:
                    type: str
                    description: 'Action for malformed SDP c line.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-sdp-i:
                    type: str
                    description: 'Action for malformed SDP i line.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-sdp-k:
                    type: str
                    description: 'Action for malformed SDP k line.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-sdp-m:
                    type: str
                    description: 'Action for malformed SDP m line.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-sdp-o:
                    type: str
                    description: 'Action for malformed SDP o line.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-sdp-r:
                    type: str
                    description: 'Action for malformed SDP r line.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-sdp-s:
                    type: str
                    description: 'Action for malformed SDP s line.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-sdp-t:
                    type: str
                    description: 'Action for malformed SDP t line.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-sdp-v:
                    type: str
                    description: 'Action for malformed SDP v line.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-sdp-z:
                    type: str
                    description: 'Action for malformed SDP z line.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-to:
                    type: str
                    description: 'Action for malformed To header.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-header-via:
                    type: str
                    description: 'Action for malformed VIA header.'
                    choices:
                        - pass
                        - discard
                        - respond
                malformed-request-line:
                    type: str
                    description: 'Action for malformed request line.'
                    choices:
                        - pass
                        - discard
                        - respond
                max-body-length:
                    type: int
                    description: 'Maximum SIP message body length (0 meaning no limit).'
                max-dialogs:
                    type: int
                    description: 'Maximum number of concurrent calls/dialogs (per policy).'
                max-idle-dialogs:
                    type: int
                    description: 'Maximum number established but idle dialogs to retain (per policy).'
                max-line-length:
                    type: int
                    description: 'Maximum SIP header line length (78-4096).'
                message-rate:
                    type: int
                    description: 'MESSAGE request rate limit (per second, per policy).'
                nat-trace:
                    type: str
                    description: 'Enable/disable preservation of original IP in SDP i line.'
                    choices:
                        - disable
                        - enable
                no-sdp-fixup:
                    type: str
                    description: 'Enable/disable no SDP fix-up.'
                    choices:
                        - disable
                        - enable
                notify-rate:
                    type: int
                    description: 'NOTIFY request rate limit (per second, per policy).'
                open-contact-pinhole:
                    type: str
                    description: 'Enable/disable open pinhole for non-REGISTER Contact port.'
                    choices:
                        - disable
                        - enable
                open-record-route-pinhole:
                    type: str
                    description: 'Enable/disable open pinhole for Record-Route port.'
                    choices:
                        - disable
                        - enable
                open-register-pinhole:
                    type: str
                    description: 'Enable/disable open pinhole for REGISTER Contact port.'
                    choices:
                        - disable
                        - enable
                open-via-pinhole:
                    type: str
                    description: 'Enable/disable open pinhole for Via port.'
                    choices:
                        - disable
                        - enable
                options-rate:
                    type: int
                    description: 'OPTIONS request rate limit (per second, per policy).'
                prack-rate:
                    type: int
                    description: 'PRACK request rate limit (per second, per policy).'
                preserve-override:
                    type: str
                    description: 'Override i line to preserve original IPS (default: append).'
                    choices:
                        - disable
                        - enable
                provisional-invite-expiry-time:
                    type: int
                    description: 'Expiry time for provisional INVITE (10 - 3600 sec).'
                publish-rate:
                    type: int
                    description: 'PUBLISH request rate limit (per second, per policy).'
                refer-rate:
                    type: int
                    description: 'REFER request rate limit (per second, per policy).'
                register-contact-trace:
                    type: str
                    description: 'Enable/disable trace original IP/port within the contact header of REGISTER requests.'
                    choices:
                        - disable
                        - enable
                register-rate:
                    type: int
                    description: 'REGISTER request rate limit (per second, per policy).'
                rfc2543-branch:
                    type: str
                    description: 'Enable/disable support via branch compliant with RFC 2543.'
                    choices:
                        - disable
                        - enable
                rtp:
                    type: str
                    description: 'Enable/disable create pinholes for RTP traffic to traverse firewall.'
                    choices:
                        - disable
                        - enable
                ssl-algorithm:
                    type: str
                    description: 'Relative strength of encryption algorithms accepted in negotiation.'
                    choices:
                        - high
                        - medium
                        - low
                ssl-auth-client:
                    type: str
                    description: 'Require a client certificate and authenticate it with the peer/peergrp.'
                ssl-auth-server:
                    type: str
                    description: 'Authenticate the server's certificate with the peer/peergrp.'
                ssl-client-certificate:
                    type: str
                    description: 'Name of Certificate to offer to server if requested.'
                ssl-client-renegotiation:
                    type: str
                    description: 'Allow/block client renegotiation by server.'
                    choices:
                        - allow
                        - deny
                        - secure
                ssl-max-version:
                    type: str
                    description: 'Highest SSL/TLS version to negotiate.'
                    choices:
                        - ssl-3.0
                        - tls-1.0
                        - tls-1.1
                        - tls-1.2
                ssl-min-version:
                    type: str
                    description: 'Lowest SSL/TLS version to negotiate.'
                    choices:
                        - ssl-3.0
                        - tls-1.0
                        - tls-1.1
                        - tls-1.2
                ssl-mode:
                    type: str
                    description: 'SSL/TLS mode for encryption & decryption of traffic.'
                    choices:
                        - off
                        - full
                ssl-pfs:
                    type: str
                    description: 'SSL Perfect Forward Secrecy.'
                    choices:
                        - require
                        - deny
                        - allow
                ssl-send-empty-frags:
                    type: str
                    description: 'Send empty fragments to avoid attack on CBC IV (SSL 3.0 & TLS 1.0 only).'
                    choices:
                        - disable
                        - enable
                ssl-server-certificate:
                    type: str
                    description: 'Name of Certificate return to the client in every SSL connection.'
                status:
                    type: str
                    description: 'Enable/disable SIP.'
                    choices:
                        - disable
                        - enable
                strict-register:
                    type: str
                    description: 'Enable/disable only allow the registrar to connect.'
                    choices:
                        - disable
                        - enable
                subscribe-rate:
                    type: int
                    description: 'SUBSCRIBE request rate limit (per second, per policy).'
                unknown-header:
                    type: str
                    description: 'Action for unknown SIP header.'
                    choices:
                        - pass
                        - discard
                        - respond
                update-rate:
                    type: int
                    description: 'UPDATE request rate limit (per second, per policy).'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /pm/config/obj/voip/profile/{profile}/sip
      fmgr_pm_config_obj_voip_profile_profile_sip:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            - 
               option: <value in [object member, chksum, datasrc]>
    - name: send request to /pm/config/obj/voip/profile/{profile}/sip
      fmgr_pm_config_obj_voip_profile_profile_sip:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            - 
               data: 
                  ack-rate: <value of integer>
                  block-ack: <value in [disable, enable]>
                  block-bye: <value in [disable, enable]>
                  block-cancel: <value in [disable, enable]>
                  block-geo-red-options: <value in [disable, enable]>
                  block-info: <value in [disable, enable]>
                  block-invite: <value in [disable, enable]>
                  block-long-lines: <value in [disable, enable]>
                  block-message: <value in [disable, enable]>
                  block-notify: <value in [disable, enable]>
                  block-options: <value in [disable, enable]>
                  block-prack: <value in [disable, enable]>
                  block-publish: <value in [disable, enable]>
                  block-refer: <value in [disable, enable]>
                  block-register: <value in [disable, enable]>
                  block-subscribe: <value in [disable, enable]>
                  block-unknown: <value in [disable, enable]>
                  block-update: <value in [disable, enable]>
                  bye-rate: <value of integer>
                  call-keepalive: <value of integer>
                  cancel-rate: <value of integer>
                  contact-fixup: <value in [disable, enable]>
                  hnt-restrict-source-ip: <value in [disable, enable]>
                  hosted-nat-traversal: <value in [disable, enable]>
                  info-rate: <value of integer>
                  invite-rate: <value of integer>
                  ips-rtp: <value in [disable, enable]>
                  log-call-summary: <value in [disable, enable]>
                  log-violations: <value in [disable, enable]>
                  malformed-header-allow: <value in [pass, discard, respond]>
                  malformed-header-call-id: <value in [pass, discard, respond]>
                  malformed-header-contact: <value in [pass, discard, respond]>
                  malformed-header-content-length: <value in [pass, discard, respond]>
                  malformed-header-content-type: <value in [pass, discard, respond]>
                  malformed-header-cseq: <value in [pass, discard, respond]>
                  malformed-header-expires: <value in [pass, discard, respond]>
                  malformed-header-from: <value in [pass, discard, respond]>
                  malformed-header-max-forwards: <value in [pass, discard, respond]>
                  malformed-header-p-asserted-identity: <value in [pass, discard, respond]>
                  malformed-header-rack: <value in [pass, discard, respond]>
                  malformed-header-record-route: <value in [pass, discard, respond]>
                  malformed-header-route: <value in [pass, discard, respond]>
                  malformed-header-rseq: <value in [pass, discard, respond]>
                  malformed-header-sdp-a: <value in [pass, discard, respond]>
                  malformed-header-sdp-b: <value in [pass, discard, respond]>
                  malformed-header-sdp-c: <value in [pass, discard, respond]>
                  malformed-header-sdp-i: <value in [pass, discard, respond]>
                  malformed-header-sdp-k: <value in [pass, discard, respond]>
                  malformed-header-sdp-m: <value in [pass, discard, respond]>
                  malformed-header-sdp-o: <value in [pass, discard, respond]>
                  malformed-header-sdp-r: <value in [pass, discard, respond]>
                  malformed-header-sdp-s: <value in [pass, discard, respond]>
                  malformed-header-sdp-t: <value in [pass, discard, respond]>
                  malformed-header-sdp-v: <value in [pass, discard, respond]>
                  malformed-header-sdp-z: <value in [pass, discard, respond]>
                  malformed-header-to: <value in [pass, discard, respond]>
                  malformed-header-via: <value in [pass, discard, respond]>
                  malformed-request-line: <value in [pass, discard, respond]>
                  max-body-length: <value of integer>
                  max-dialogs: <value of integer>
                  max-idle-dialogs: <value of integer>
                  max-line-length: <value of integer>
                  message-rate: <value of integer>
                  nat-trace: <value in [disable, enable]>
                  no-sdp-fixup: <value in [disable, enable]>
                  notify-rate: <value of integer>
                  open-contact-pinhole: <value in [disable, enable]>
                  open-record-route-pinhole: <value in [disable, enable]>
                  open-register-pinhole: <value in [disable, enable]>
                  open-via-pinhole: <value in [disable, enable]>
                  options-rate: <value of integer>
                  prack-rate: <value of integer>
                  preserve-override: <value in [disable, enable]>
                  provisional-invite-expiry-time: <value of integer>
                  publish-rate: <value of integer>
                  refer-rate: <value of integer>
                  register-contact-trace: <value in [disable, enable]>
                  register-rate: <value of integer>
                  rfc2543-branch: <value in [disable, enable]>
                  rtp: <value in [disable, enable]>
                  ssl-algorithm: <value in [high, medium, low]>
                  ssl-auth-client: <value of string>
                  ssl-auth-server: <value of string>
                  ssl-client-certificate: <value of string>
                  ssl-client-renegotiation: <value in [allow, deny, secure]>
                  ssl-max-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
                  ssl-min-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
                  ssl-mode: <value in [off, full]>
                  ssl-pfs: <value in [require, deny, allow]>
                  ssl-send-empty-frags: <value in [disable, enable]>
                  ssl-server-certificate: <value of string>
                  status: <value in [disable, enable]>
                  strict-register: <value in [disable, enable]>
                  subscribe-rate: <value of integer>
                  unknown-header: <value in [pass, discard, respond]>
                  update-rate: <value of integer>

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
            ack-rate:
               type: int
               description: 'ACK request rate limit (per second, per policy).'
            block-ack:
               type: str
               description: 'Enable/disable block ACK requests.'
            block-bye:
               type: str
               description: 'Enable/disable block BYE requests.'
            block-cancel:
               type: str
               description: 'Enable/disable block CANCEL requests.'
            block-geo-red-options:
               type: str
               description: 'Enable/disable block OPTIONS requests, but OPTIONS requests still notify for redundancy.'
            block-info:
               type: str
               description: 'Enable/disable block INFO requests.'
            block-invite:
               type: str
               description: 'Enable/disable block INVITE requests.'
            block-long-lines:
               type: str
               description: 'Enable/disable block requests with headers exceeding max-line-length.'
            block-message:
               type: str
               description: 'Enable/disable block MESSAGE requests.'
            block-notify:
               type: str
               description: 'Enable/disable block NOTIFY requests.'
            block-options:
               type: str
               description: 'Enable/disable block OPTIONS requests and no OPTIONS as notifying message for redundancy either.'
            block-prack:
               type: str
               description: 'Enable/disable block prack requests.'
            block-publish:
               type: str
               description: 'Enable/disable block PUBLISH requests.'
            block-refer:
               type: str
               description: 'Enable/disable block REFER requests.'
            block-register:
               type: str
               description: 'Enable/disable block REGISTER requests.'
            block-subscribe:
               type: str
               description: 'Enable/disable block SUBSCRIBE requests.'
            block-unknown:
               type: str
               description: 'Block unrecognized SIP requests (enabled by default).'
            block-update:
               type: str
               description: 'Enable/disable block UPDATE requests.'
            bye-rate:
               type: int
               description: 'BYE request rate limit (per second, per policy).'
            call-keepalive:
               type: int
               description: 'Continue tracking calls with no RTP for this many minutes.'
            cancel-rate:
               type: int
               description: 'CANCEL request rate limit (per second, per policy).'
            contact-fixup:
               type: str
               description: 'Fixup contact anyway even if contact's IP:port doesn't match session's IP:port.'
            hnt-restrict-source-ip:
               type: str
               description: 'Enable/disable restrict RTP source IP to be the same as SIP source IP when HNT is enabled.'
            hosted-nat-traversal:
               type: str
               description: 'Hosted NAT Traversal (HNT).'
            info-rate:
               type: int
               description: 'INFO request rate limit (per second, per policy).'
            invite-rate:
               type: int
               description: 'INVITE request rate limit (per second, per policy).'
            ips-rtp:
               type: str
               description: 'Enable/disable allow IPS on RTP.'
            log-call-summary:
               type: str
               description: 'Enable/disable logging of SIP call summary.'
            log-violations:
               type: str
               description: 'Enable/disable logging of SIP violations.'
            malformed-header-allow:
               type: str
               description: 'Action for malformed Allow header.'
            malformed-header-call-id:
               type: str
               description: 'Action for malformed Call-ID header.'
            malformed-header-contact:
               type: str
               description: 'Action for malformed Contact header.'
            malformed-header-content-length:
               type: str
               description: 'Action for malformed Content-Length header.'
            malformed-header-content-type:
               type: str
               description: 'Action for malformed Content-Type header.'
            malformed-header-cseq:
               type: str
               description: 'Action for malformed CSeq header.'
            malformed-header-expires:
               type: str
               description: 'Action for malformed Expires header.'
            malformed-header-from:
               type: str
               description: 'Action for malformed From header.'
            malformed-header-max-forwards:
               type: str
               description: 'Action for malformed Max-Forwards header.'
            malformed-header-p-asserted-identity:
               type: str
               description: 'Action for malformed P-Asserted-Identity header.'
            malformed-header-rack:
               type: str
               description: 'Action for malformed RAck header.'
            malformed-header-record-route:
               type: str
               description: 'Action for malformed Record-Route header.'
            malformed-header-route:
               type: str
               description: 'Action for malformed Route header.'
            malformed-header-rseq:
               type: str
               description: 'Action for malformed RSeq header.'
            malformed-header-sdp-a:
               type: str
               description: 'Action for malformed SDP a line.'
            malformed-header-sdp-b:
               type: str
               description: 'Action for malformed SDP b line.'
            malformed-header-sdp-c:
               type: str
               description: 'Action for malformed SDP c line.'
            malformed-header-sdp-i:
               type: str
               description: 'Action for malformed SDP i line.'
            malformed-header-sdp-k:
               type: str
               description: 'Action for malformed SDP k line.'
            malformed-header-sdp-m:
               type: str
               description: 'Action for malformed SDP m line.'
            malformed-header-sdp-o:
               type: str
               description: 'Action for malformed SDP o line.'
            malformed-header-sdp-r:
               type: str
               description: 'Action for malformed SDP r line.'
            malformed-header-sdp-s:
               type: str
               description: 'Action for malformed SDP s line.'
            malformed-header-sdp-t:
               type: str
               description: 'Action for malformed SDP t line.'
            malformed-header-sdp-v:
               type: str
               description: 'Action for malformed SDP v line.'
            malformed-header-sdp-z:
               type: str
               description: 'Action for malformed SDP z line.'
            malformed-header-to:
               type: str
               description: 'Action for malformed To header.'
            malformed-header-via:
               type: str
               description: 'Action for malformed VIA header.'
            malformed-request-line:
               type: str
               description: 'Action for malformed request line.'
            max-body-length:
               type: int
               description: 'Maximum SIP message body length (0 meaning no limit).'
            max-dialogs:
               type: int
               description: 'Maximum number of concurrent calls/dialogs (per policy).'
            max-idle-dialogs:
               type: int
               description: 'Maximum number established but idle dialogs to retain (per policy).'
            max-line-length:
               type: int
               description: 'Maximum SIP header line length (78-4096).'
            message-rate:
               type: int
               description: 'MESSAGE request rate limit (per second, per policy).'
            nat-trace:
               type: str
               description: 'Enable/disable preservation of original IP in SDP i line.'
            no-sdp-fixup:
               type: str
               description: 'Enable/disable no SDP fix-up.'
            notify-rate:
               type: int
               description: 'NOTIFY request rate limit (per second, per policy).'
            open-contact-pinhole:
               type: str
               description: 'Enable/disable open pinhole for non-REGISTER Contact port.'
            open-record-route-pinhole:
               type: str
               description: 'Enable/disable open pinhole for Record-Route port.'
            open-register-pinhole:
               type: str
               description: 'Enable/disable open pinhole for REGISTER Contact port.'
            open-via-pinhole:
               type: str
               description: 'Enable/disable open pinhole for Via port.'
            options-rate:
               type: int
               description: 'OPTIONS request rate limit (per second, per policy).'
            prack-rate:
               type: int
               description: 'PRACK request rate limit (per second, per policy).'
            preserve-override:
               type: str
               description: 'Override i line to preserve original IPS (default: append).'
            provisional-invite-expiry-time:
               type: int
               description: 'Expiry time for provisional INVITE (10 - 3600 sec).'
            publish-rate:
               type: int
               description: 'PUBLISH request rate limit (per second, per policy).'
            refer-rate:
               type: int
               description: 'REFER request rate limit (per second, per policy).'
            register-contact-trace:
               type: str
               description: 'Enable/disable trace original IP/port within the contact header of REGISTER requests.'
            register-rate:
               type: int
               description: 'REGISTER request rate limit (per second, per policy).'
            rfc2543-branch:
               type: str
               description: 'Enable/disable support via branch compliant with RFC 2543.'
            rtp:
               type: str
               description: 'Enable/disable create pinholes for RTP traffic to traverse firewall.'
            ssl-algorithm:
               type: str
               description: 'Relative strength of encryption algorithms accepted in negotiation.'
            ssl-auth-client:
               type: str
               description: 'Require a client certificate and authenticate it with the peer/peergrp.'
            ssl-auth-server:
               type: str
               description: 'Authenticate the server's certificate with the peer/peergrp.'
            ssl-client-certificate:
               type: str
               description: 'Name of Certificate to offer to server if requested.'
            ssl-client-renegotiation:
               type: str
               description: 'Allow/block client renegotiation by server.'
            ssl-max-version:
               type: str
               description: 'Highest SSL/TLS version to negotiate.'
            ssl-min-version:
               type: str
               description: 'Lowest SSL/TLS version to negotiate.'
            ssl-mode:
               type: str
               description: 'SSL/TLS mode for encryption & decryption of traffic.'
            ssl-pfs:
               type: str
               description: 'SSL Perfect Forward Secrecy.'
            ssl-send-empty-frags:
               type: str
               description: 'Send empty fragments to avoid attack on CBC IV (SSL 3.0 & TLS 1.0 only).'
            ssl-server-certificate:
               type: str
               description: 'Name of Certificate return to the client in every SSL connection.'
            status:
               type: str
               description: 'Enable/disable SIP.'
            strict-register:
               type: str
               description: 'Enable/disable only allow the registrar to connect.'
            subscribe-rate:
               type: int
               description: 'SUBSCRIBE request rate limit (per second, per policy).'
            unknown-header:
               type: str
               description: 'Action for unknown SIP header.'
            update-rate:
               type: int
               description: 'UPDATE request rate limit (per second, per policy).'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/obj/voip/profile/{profile}/sip
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
            example: /pm/config/adom/{adom}/obj/voip/profile/{profile}/sip

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
        '/pm/config/adom/{adom}/obj/voip/profile/{profile}/sip',
        '/pm/config/global/obj/voip/profile/{profile}/sip'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'profile',
            'type': 'string'
        }
    ]

    body_schema =  {
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
                        'ack-rate': {
                            'type': 'integer'
                        },
                        'block-ack': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'block-bye': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'block-cancel': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'block-geo-red-options': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'block-info': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'block-invite': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'block-long-lines': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'block-message': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'block-notify': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'block-options': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'block-prack': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'block-publish': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'block-refer': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'block-register': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'block-subscribe': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'block-unknown': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'block-update': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'bye-rate': {
                            'type': 'integer'
                        },
                        'call-keepalive': {
                            'type': 'integer'
                        },
                        'cancel-rate': {
                            'type': 'integer'
                        },
                        'contact-fixup': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'hnt-restrict-source-ip': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'hosted-nat-traversal': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'info-rate': {
                            'type': 'integer'
                        },
                        'invite-rate': {
                            'type': 'integer'
                        },
                        'ips-rtp': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'log-call-summary': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'log-violations': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'malformed-header-allow': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-call-id': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-contact': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-content-length': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-content-type': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-cseq': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-expires': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-from': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-max-forwards': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-p-asserted-identity': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-rack': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-record-route': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-route': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-rseq': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-sdp-a': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-sdp-b': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-sdp-c': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-sdp-i': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-sdp-k': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-sdp-m': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-sdp-o': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-sdp-r': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-sdp-s': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-sdp-t': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-sdp-v': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-sdp-z': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-to': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-header-via': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'malformed-request-line': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'max-body-length': {
                            'type': 'integer'
                        },
                        'max-dialogs': {
                            'type': 'integer'
                        },
                        'max-idle-dialogs': {
                            'type': 'integer'
                        },
                        'max-line-length': {
                            'type': 'integer'
                        },
                        'message-rate': {
                            'type': 'integer'
                        },
                        'nat-trace': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'no-sdp-fixup': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'notify-rate': {
                            'type': 'integer'
                        },
                        'open-contact-pinhole': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'open-record-route-pinhole': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'open-register-pinhole': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'open-via-pinhole': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'options-rate': {
                            'type': 'integer'
                        },
                        'prack-rate': {
                            'type': 'integer'
                        },
                        'preserve-override': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'provisional-invite-expiry-time': {
                            'type': 'integer'
                        },
                        'publish-rate': {
                            'type': 'integer'
                        },
                        'refer-rate': {
                            'type': 'integer'
                        },
                        'register-contact-trace': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'register-rate': {
                            'type': 'integer'
                        },
                        'rfc2543-branch': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'rtp': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ssl-algorithm': {
                            'type': 'string',
                            'enum': [
                                'high',
                                'medium',
                                'low'
                            ]
                        },
                        'ssl-auth-client': {
                            'type': 'string'
                        },
                        'ssl-auth-server': {
                            'type': 'string'
                        },
                        'ssl-client-certificate': {
                            'type': 'string'
                        },
                        'ssl-client-renegotiation': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny',
                                'secure'
                            ]
                        },
                        'ssl-max-version': {
                            'type': 'string',
                            'enum': [
                                'ssl-3.0',
                                'tls-1.0',
                                'tls-1.1',
                                'tls-1.2'
                            ]
                        },
                        'ssl-min-version': {
                            'type': 'string',
                            'enum': [
                                'ssl-3.0',
                                'tls-1.0',
                                'tls-1.1',
                                'tls-1.2'
                            ]
                        },
                        'ssl-mode': {
                            'type': 'string',
                            'enum': [
                                'off',
                                'full'
                            ]
                        },
                        'ssl-pfs': {
                            'type': 'string',
                            'enum': [
                                'require',
                                'deny',
                                'allow'
                            ]
                        },
                        'ssl-send-empty-frags': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ssl-server-certificate': {
                            'type': 'string'
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'strict-register': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'subscribe-rate': {
                            'type': 'integer'
                        },
                        'unknown-header': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'discard',
                                'respond'
                            ]
                        },
                        'update-rate': {
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