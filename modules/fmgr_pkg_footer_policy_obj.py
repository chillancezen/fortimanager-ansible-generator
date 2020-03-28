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
module: fmgr_pkg_footer_policy_obj
short_description: no description
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/global/pkg/{pkg}/global/footer/policy/{policy}
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
            pkg:
                type: str
            policy:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
            data:
                action:
                    type: str
                    choices:
                        - 'deny'
                        - 'accept'
                        - 'ipsec'
                        - 'ssl-vpn'
                active-auth-method:
                    type: str
                    choices:
                        - 'ntlm'
                        - 'basic'
                        - 'digest'
                        - 'form'
                anti-replay:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                app-category:
                    type: str
                app-group:
                    type: str
                application:
                    -
                        type: int
                application-charts:
                    -
                        type: str
                        choices:
                            - 'top10-app'
                            - 'top10-p2p-user'
                            - 'top10-media-user'
                application-list:
                    type: str
                auth-cert:
                    type: str
                auth-method:
                    type: str
                    choices:
                        - 'basic'
                        - 'digest'
                        - 'ntlm'
                        - 'fsae'
                        - 'form'
                        - 'fsso'
                        - 'rsso'
                auth-path:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                auth-portal:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                auth-redirect-addr:
                    type: str
                auto-asic-offload:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                av-profile:
                    type: str
                bandwidth:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                block-notification:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                captive-portal-exempt:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                capture-packet:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                casi-profile:
                    type: str
                central-nat:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                cifs-profile:
                    type: str
                client-reputation:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                client-reputation-mode:
                    type: str
                    choices:
                        - 'learning'
                        - 'monitoring'
                comments:
                    type: str
                custom-log-fields:
                    type: str
                deep-inspection-options:
                    type: str
                delay-tcp-npu-session:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                delay-tcp-npu-sessoin:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                device-detection-portal:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                devices:
                    type: str
                diffserv-forward:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                diffserv-reverse:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                diffservcode-forward:
                    type: str
                diffservcode-rev:
                    type: str
                disclaimer:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                dlp-sensor:
                    type: str
                dnsfilter-profile:
                    type: str
                dponly:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                dscp-match:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                dscp-negate:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                dscp-value:
                    type: str
                dsri:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                dstaddr:
                    type: str
                dstaddr-negate:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                dstaddr6:
                    type: str
                dstintf:
                    type: str
                dynamic-profile:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                dynamic-profile-access:
                    -
                        type: str
                        choices:
                            - 'imap'
                            - 'smtp'
                            - 'pop3'
                            - 'http'
                            - 'ftp'
                            - 'im'
                            - 'nntp'
                            - 'imaps'
                            - 'smtps'
                            - 'pop3s'
                            - 'https'
                            - 'ftps'
                            - 'ssh'
                dynamic-profile-fallthrough:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                dynamic-profile-group:
                    type: str
                email-collect:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                email-collection-portal:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                emailfilter-profile:
                    type: str
                endpoint-check:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                endpoint-compliance:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                endpoint-keepalive-interface:
                    type: str
                endpoint-profile:
                    type: str
                failed-connection:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                fall-through-unauthenticated:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                firewall-session-dirty:
                    type: str
                    choices:
                        - 'check-all'
                        - 'check-new'
                fixedport:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                forticlient-compliance-devices:
                    -
                        type: str
                        choices:
                            - 'windows-pc'
                            - 'mac'
                            - 'iphone-ipad'
                            - 'android'
                forticlient-compliance-enforcement-portal:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                fsae:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                fsae-server-for-ntlm:
                    type: str
                fsso:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                fsso-agent-for-ntlm:
                    type: str
                geo-location:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                geoip-anycast:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                global-label:
                    type: str
                groups:
                    type: str
                gtp-profile:
                    type: str
                http-policy-redirect:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                icap-profile:
                    type: str
                identity-based:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                identity-based-policy:
                    -
                        action:
                            type: str
                            choices:
                                - 'deny'
                                - 'accept'
                        application-charts:
                            -
                                type: str
                                choices:
                                    - 'top10-app'
                                    - 'top10-p2p-user'
                                    - 'top10-media-user'
                        application-list:
                            type: str
                        av-profile:
                            type: str
                        capture-packet:
                            type: str
                            choices:
                                - 'disable'
                                - 'enable'
                        deep-inspection-options:
                            type: str
                        devices:
                            type: str
                        dlp-sensor:
                            type: str
                        dstaddr:
                            type: str
                        dstaddr-negate:
                            type: str
                            choices:
                                - 'disable'
                                - 'enable'
                        endpoint-compliance:
                            type: str
                            choices:
                                - 'disable'
                                - 'enable'
                        groups:
                            type: str
                        icap-profile:
                            type: str
                        id:
                            type: int
                        ips-sensor:
                            type: str
                        logtraffic:
                            type: str
                            choices:
                                - 'disable'
                                - 'enable'
                                - 'all'
                                - 'utm'
                        logtraffic-app:
                            type: str
                            choices:
                                - 'disable'
                                - 'enable'
                        logtraffic-start:
                            type: str
                            choices:
                                - 'disable'
                                - 'enable'
                        mms-profile:
                            type: str
                        per-ip-shaper:
                            type: str
                        profile-group:
                            type: str
                        profile-protocol-options:
                            type: str
                        profile-type:
                            type: str
                            choices:
                                - 'single'
                                - 'group'
                        replacemsg-group:
                            type: str
                        schedule:
                            type: str
                        send-deny-packet:
                            type: str
                            choices:
                                - 'disable'
                                - 'enable'
                        service:
                            type: str
                        service-negate:
                            type: str
                            choices:
                                - 'disable'
                                - 'enable'
                        spamfilter-profile:
                            type: str
                        sslvpn-portal:
                            type: str
                        sslvpn-realm:
                            type: str
                        traffic-shaper:
                            type: str
                        traffic-shaper-reverse:
                            type: str
                        users:
                            type: str
                        utm-status:
                            type: str
                            choices:
                                - 'disable'
                                - 'enable'
                        voip-profile:
                            type: str
                        webfilter-profile:
                            type: str
                identity-based-route:
                    type: str
                identity-from:
                    type: str
                    choices:
                        - 'auth'
                        - 'device'
                inbound:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                inspection-mode:
                    type: str
                    choices:
                        - 'proxy'
                        - 'flow'
                internet-service:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                internet-service-custom:
                    type: str
                internet-service-custom-group:
                    type: str
                internet-service-group:
                    type: str
                internet-service-id:
                    type: str
                internet-service-negate:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                internet-service-src:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                internet-service-src-custom:
                    type: str
                internet-service-src-custom-group:
                    type: str
                internet-service-src-group:
                    type: str
                internet-service-src-id:
                    type: str
                internet-service-src-negate:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ip-based:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ippool:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ips-sensor:
                    type: str
                label:
                    type: str
                learning-mode:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                log-unmatched-traffic:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                logtraffic:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                        - 'all'
                        - 'utm'
                logtraffic-app:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                logtraffic-start:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                match-vip:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                mms-profile:
                    type: str
                name:
                    type: str
                nat:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                natinbound:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                natip:
                    type: str
                natoutbound:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                np-acceleration:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ntlm:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ntlm-enabled-browsers:
                    -
                        type: str
                ntlm-guest:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                outbound:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                per-ip-shaper:
                    type: str
                permit-any-host:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                permit-stun-host:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                policyid:
                    type: int
                poolname:
                    type: str
                profile-group:
                    type: str
                profile-protocol-options:
                    type: str
                profile-type:
                    type: str
                    choices:
                        - 'single'
                        - 'group'
                radius-mac-auth-bypass:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                redirect-url:
                    type: str
                replacemsg-group:
                    type: str
                replacemsg-override-group:
                    type: str
                reputation-direction:
                    type: str
                    choices:
                        - 'source'
                        - 'destination'
                reputation-minimum:
                    type: int
                require-tfa:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                rsso:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                rtp-addr:
                    type: str
                rtp-nat:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                scan-botnet-connections:
                    type: str
                    choices:
                        - 'disable'
                        - 'block'
                        - 'monitor'
                schedule:
                    type: str
                schedule-timeout:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                send-deny-packet:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                service:
                    type: str
                service-negate:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                session-ttl:
                    type: int
                sessions:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                spamfilter-profile:
                    type: str
                srcaddr:
                    type: str
                srcaddr-negate:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                srcaddr6:
                    type: str
                srcintf:
                    type: str
                ssh-filter-profile:
                    type: str
                ssh-policy-redirect:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ssl-mirror:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ssl-mirror-intf:
                    type: str
                ssl-ssh-profile:
                    type: str
                sslvpn-auth:
                    type: str
                    choices:
                        - 'any'
                        - 'local'
                        - 'radius'
                        - 'ldap'
                        - 'tacacs+'
                sslvpn-ccert:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                sslvpn-cipher:
                    type: str
                    choices:
                        - 'any'
                        - 'high'
                        - 'medium'
                sso-auth-method:
                    type: str
                    choices:
                        - 'fsso'
                        - 'rsso'
                status:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                tags:
                    type: str
                tcp-mss-receiver:
                    type: int
                tcp-mss-sender:
                    type: int
                tcp-reset:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                tcp-session-without-syn:
                    type: str
                    choices:
                        - 'all'
                        - 'data-only'
                        - 'disable'
                timeout-send-rst:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                tos:
                    type: str
                tos-mask:
                    type: str
                tos-negate:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                traffic-shaper:
                    type: str
                traffic-shaper-reverse:
                    type: str
                transaction-based:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                url-category:
                    type: str
                users:
                    type: str
                utm-inspection-mode:
                    type: str
                    choices:
                        - 'proxy'
                        - 'flow'
                utm-status:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                uuid:
                    type: str
                vlan-cos-fwd:
                    type: int
                vlan-cos-rev:
                    type: int
                vlan-filter:
                    type: str
                voip-profile:
                    type: str
                vpntunnel:
                    type: str
                waf-profile:
                    type: str
                wanopt:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                wanopt-detection:
                    type: str
                    choices:
                        - 'active'
                        - 'passive'
                        - 'off'
                wanopt-passive-opt:
                    type: str
                    choices:
                        - 'default'
                        - 'transparent'
                        - 'non-transparent'
                wanopt-peer:
                    type: str
                wanopt-profile:
                    type: str
                wccp:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                web-auth-cookie:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                webcache:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                webcache-https:
                    type: str
                    choices:
                        - 'disable'
                        - 'ssl-server'
                        - 'any'
                        - 'enable'
                webfilter-profile:
                    type: str
                webproxy-forward-server:
                    type: str
                webproxy-profile:
                    type: str
                wsso:
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
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FOOTER/POLICY/{POLICY}
      fmgr_pkg_footer_policy_obj:
         method: <value in [clone, set, update]>
         url_params:
            pkg: <value of string>
            policy: <value of string>
         params:
            -
               data:
                  action: <value in [deny, accept, ipsec, ...]>
                  active-auth-method: <value in [ntlm, basic, digest, ...]>
                  anti-replay: <value in [disable, enable]>
                  app-category: <value of string>
                  app-group: <value of string>
                  application:
                    - <value of integer>
                  application-charts:
                    - <value in [top10-app, top10-p2p-user, top10-media-user]>
                  application-list: <value of string>
                  auth-cert: <value of string>
                  auth-method: <value in [basic, digest, ntlm, ...]>
                  auth-path: <value in [disable, enable]>
                  auth-portal: <value in [disable, enable]>
                  auth-redirect-addr: <value of string>
                  auto-asic-offload: <value in [disable, enable]>
                  av-profile: <value of string>
                  bandwidth: <value in [disable, enable]>
                  block-notification: <value in [disable, enable]>
                  captive-portal-exempt: <value in [disable, enable]>
                  capture-packet: <value in [disable, enable]>
                  casi-profile: <value of string>
                  central-nat: <value in [disable, enable]>
                  cifs-profile: <value of string>
                  client-reputation: <value in [disable, enable]>
                  client-reputation-mode: <value in [learning, monitoring]>
                  comments: <value of string>
                  custom-log-fields: <value of string>
                  deep-inspection-options: <value of string>
                  delay-tcp-npu-session: <value in [disable, enable]>
                  delay-tcp-npu-sessoin: <value in [disable, enable]>
                  device-detection-portal: <value in [disable, enable]>
                  devices: <value of string>
                  diffserv-forward: <value in [disable, enable]>
                  diffserv-reverse: <value in [disable, enable]>
                  diffservcode-forward: <value of string>
                  diffservcode-rev: <value of string>
                  disclaimer: <value in [disable, enable]>
                  dlp-sensor: <value of string>
                  dnsfilter-profile: <value of string>
                  dponly: <value in [disable, enable]>
                  dscp-match: <value in [disable, enable]>
                  dscp-negate: <value in [disable, enable]>
                  dscp-value: <value of string>
                  dsri: <value in [disable, enable]>
                  dstaddr: <value of string>
                  dstaddr-negate: <value in [disable, enable]>
                  dstaddr6: <value of string>
                  dstintf: <value of string>
                  dynamic-profile: <value in [disable, enable]>
                  dynamic-profile-access:
                    - <value in [imap, smtp, pop3, ...]>
                  dynamic-profile-fallthrough: <value in [disable, enable]>
                  dynamic-profile-group: <value of string>
                  email-collect: <value in [disable, enable]>
                  email-collection-portal: <value in [disable, enable]>
                  emailfilter-profile: <value of string>
                  endpoint-check: <value in [disable, enable]>
                  endpoint-compliance: <value in [disable, enable]>
                  endpoint-keepalive-interface: <value of string>
                  endpoint-profile: <value of string>
                  failed-connection: <value in [disable, enable]>
                  fall-through-unauthenticated: <value in [disable, enable]>
                  firewall-session-dirty: <value in [check-all, check-new]>
                  fixedport: <value in [disable, enable]>
                  forticlient-compliance-devices:
                    - <value in [windows-pc, mac, iphone-ipad, ...]>
                  forticlient-compliance-enforcement-portal: <value in [disable, enable]>
                  fsae: <value in [disable, enable]>
                  fsae-server-for-ntlm: <value of string>
                  fsso: <value in [disable, enable]>
                  fsso-agent-for-ntlm: <value of string>
                  geo-location: <value in [disable, enable]>
                  geoip-anycast: <value in [disable, enable]>
                  global-label: <value of string>
                  groups: <value of string>
                  gtp-profile: <value of string>
                  http-policy-redirect: <value in [disable, enable]>
                  icap-profile: <value of string>
                  identity-based: <value in [disable, enable]>
                  identity-based-policy:
                    -
                        action: <value in [deny, accept]>
                        application-charts:
                          - <value in [top10-app, top10-p2p-user, top10-media-user]>
                        application-list: <value of string>
                        av-profile: <value of string>
                        capture-packet: <value in [disable, enable]>
                        deep-inspection-options: <value of string>
                        devices: <value of string>
                        dlp-sensor: <value of string>
                        dstaddr: <value of string>
                        dstaddr-negate: <value in [disable, enable]>
                        endpoint-compliance: <value in [disable, enable]>
                        groups: <value of string>
                        icap-profile: <value of string>
                        id: <value of integer>
                        ips-sensor: <value of string>
                        logtraffic: <value in [disable, enable, all, ...]>
                        logtraffic-app: <value in [disable, enable]>
                        logtraffic-start: <value in [disable, enable]>
                        mms-profile: <value of string>
                        per-ip-shaper: <value of string>
                        profile-group: <value of string>
                        profile-protocol-options: <value of string>
                        profile-type: <value in [single, group]>
                        replacemsg-group: <value of string>
                        schedule: <value of string>
                        send-deny-packet: <value in [disable, enable]>
                        service: <value of string>
                        service-negate: <value in [disable, enable]>
                        spamfilter-profile: <value of string>
                        sslvpn-portal: <value of string>
                        sslvpn-realm: <value of string>
                        traffic-shaper: <value of string>
                        traffic-shaper-reverse: <value of string>
                        users: <value of string>
                        utm-status: <value in [disable, enable]>
                        voip-profile: <value of string>
                        webfilter-profile: <value of string>
                  identity-based-route: <value of string>
                  identity-from: <value in [auth, device]>
                  inbound: <value in [disable, enable]>
                  inspection-mode: <value in [proxy, flow]>
                  internet-service: <value in [disable, enable]>
                  internet-service-custom: <value of string>
                  internet-service-custom-group: <value of string>
                  internet-service-group: <value of string>
                  internet-service-id: <value of string>
                  internet-service-negate: <value in [disable, enable]>
                  internet-service-src: <value in [disable, enable]>
                  internet-service-src-custom: <value of string>
                  internet-service-src-custom-group: <value of string>
                  internet-service-src-group: <value of string>
                  internet-service-src-id: <value of string>
                  internet-service-src-negate: <value in [disable, enable]>
                  ip-based: <value in [disable, enable]>
                  ippool: <value in [disable, enable]>
                  ips-sensor: <value of string>
                  label: <value of string>
                  learning-mode: <value in [disable, enable]>
                  log-unmatched-traffic: <value in [disable, enable]>
                  logtraffic: <value in [disable, enable, all, ...]>
                  logtraffic-app: <value in [disable, enable]>
                  logtraffic-start: <value in [disable, enable]>
                  match-vip: <value in [disable, enable]>
                  mms-profile: <value of string>
                  name: <value of string>
                  nat: <value in [disable, enable]>
                  natinbound: <value in [disable, enable]>
                  natip: <value of string>
                  natoutbound: <value in [disable, enable]>
                  np-acceleration: <value in [disable, enable]>
                  ntlm: <value in [disable, enable]>
                  ntlm-enabled-browsers:
                    - <value of string>
                  ntlm-guest: <value in [disable, enable]>
                  outbound: <value in [disable, enable]>
                  per-ip-shaper: <value of string>
                  permit-any-host: <value in [disable, enable]>
                  permit-stun-host: <value in [disable, enable]>
                  policyid: <value of integer>
                  poolname: <value of string>
                  profile-group: <value of string>
                  profile-protocol-options: <value of string>
                  profile-type: <value in [single, group]>
                  radius-mac-auth-bypass: <value in [disable, enable]>
                  redirect-url: <value of string>
                  replacemsg-group: <value of string>
                  replacemsg-override-group: <value of string>
                  reputation-direction: <value in [source, destination]>
                  reputation-minimum: <value of integer>
                  require-tfa: <value in [disable, enable]>
                  rsso: <value in [disable, enable]>
                  rtp-addr: <value of string>
                  rtp-nat: <value in [disable, enable]>
                  scan-botnet-connections: <value in [disable, block, monitor]>
                  schedule: <value of string>
                  schedule-timeout: <value in [disable, enable]>
                  send-deny-packet: <value in [disable, enable]>
                  service: <value of string>
                  service-negate: <value in [disable, enable]>
                  session-ttl: <value of integer>
                  sessions: <value in [disable, enable]>
                  spamfilter-profile: <value of string>
                  srcaddr: <value of string>
                  srcaddr-negate: <value in [disable, enable]>
                  srcaddr6: <value of string>
                  srcintf: <value of string>
                  ssh-filter-profile: <value of string>
                  ssh-policy-redirect: <value in [disable, enable]>
                  ssl-mirror: <value in [disable, enable]>
                  ssl-mirror-intf: <value of string>
                  ssl-ssh-profile: <value of string>
                  sslvpn-auth: <value in [any, local, radius, ...]>
                  sslvpn-ccert: <value in [disable, enable]>
                  sslvpn-cipher: <value in [any, high, medium]>
                  sso-auth-method: <value in [fsso, rsso]>
                  status: <value in [disable, enable]>
                  tags: <value of string>
                  tcp-mss-receiver: <value of integer>
                  tcp-mss-sender: <value of integer>
                  tcp-reset: <value in [disable, enable]>
                  tcp-session-without-syn: <value in [all, data-only, disable]>
                  timeout-send-rst: <value in [disable, enable]>
                  tos: <value of string>
                  tos-mask: <value of string>
                  tos-negate: <value in [disable, enable]>
                  traffic-shaper: <value of string>
                  traffic-shaper-reverse: <value of string>
                  transaction-based: <value in [disable, enable]>
                  url-category: <value of string>
                  users: <value of string>
                  utm-inspection-mode: <value in [proxy, flow]>
                  utm-status: <value in [disable, enable]>
                  uuid: <value of string>
                  vlan-cos-fwd: <value of integer>
                  vlan-cos-rev: <value of integer>
                  vlan-filter: <value of string>
                  voip-profile: <value of string>
                  vpntunnel: <value of string>
                  waf-profile: <value of string>
                  wanopt: <value in [disable, enable]>
                  wanopt-detection: <value in [active, passive, off]>
                  wanopt-passive-opt: <value in [default, transparent, non-transparent]>
                  wanopt-peer: <value of string>
                  wanopt-profile: <value of string>
                  wccp: <value in [disable, enable]>
                  web-auth-cookie: <value in [disable, enable]>
                  webcache: <value in [disable, enable]>
                  webcache-https: <value in [disable, ssl-server, any, ...]>
                  webfilter-profile: <value of string>
                  webproxy-forward-server: <value of string>
                  webproxy-profile: <value of string>
                  wsso: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FOOTER/POLICY/{POLICY}
      fmgr_pkg_footer_policy_obj:
         method: <value in [get]>
         url_params:
            pkg: <value of string>
            policy: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[clone, set, update]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            policyid:
               type: int
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/global/pkg/{pkg}/global/footer/policy/{policy}'
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
            example: '/pm/config/global/pkg/{pkg}/global/footer/policy/{policy}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            action:
               type: str
            active-auth-method:
               type: str
            anti-replay:
               type: str
            app-category:
               type: str
            app-group:
               type: str
            application:
               type: array
               suboptions:
                  type: int
            application-charts:
               type: array
               suboptions:
                  type: str
            application-list:
               type: str
            auth-cert:
               type: str
            auth-method:
               type: str
            auth-path:
               type: str
            auth-portal:
               type: str
            auth-redirect-addr:
               type: str
            auto-asic-offload:
               type: str
            av-profile:
               type: str
            bandwidth:
               type: str
            block-notification:
               type: str
            captive-portal-exempt:
               type: str
            capture-packet:
               type: str
            casi-profile:
               type: str
            central-nat:
               type: str
            cifs-profile:
               type: str
            client-reputation:
               type: str
            client-reputation-mode:
               type: str
            comments:
               type: str
            custom-log-fields:
               type: str
            deep-inspection-options:
               type: str
            delay-tcp-npu-session:
               type: str
            delay-tcp-npu-sessoin:
               type: str
            device-detection-portal:
               type: str
            devices:
               type: str
            diffserv-forward:
               type: str
            diffserv-reverse:
               type: str
            diffservcode-forward:
               type: str
            diffservcode-rev:
               type: str
            disclaimer:
               type: str
            dlp-sensor:
               type: str
            dnsfilter-profile:
               type: str
            dponly:
               type: str
            dscp-match:
               type: str
            dscp-negate:
               type: str
            dscp-value:
               type: str
            dsri:
               type: str
            dstaddr:
               type: str
            dstaddr-negate:
               type: str
            dstaddr6:
               type: str
            dstintf:
               type: str
            dynamic-profile:
               type: str
            dynamic-profile-access:
               type: array
               suboptions:
                  type: str
            dynamic-profile-fallthrough:
               type: str
            dynamic-profile-group:
               type: str
            email-collect:
               type: str
            email-collection-portal:
               type: str
            emailfilter-profile:
               type: str
            endpoint-check:
               type: str
            endpoint-compliance:
               type: str
            endpoint-keepalive-interface:
               type: str
            endpoint-profile:
               type: str
            failed-connection:
               type: str
            fall-through-unauthenticated:
               type: str
            firewall-session-dirty:
               type: str
            fixedport:
               type: str
            forticlient-compliance-devices:
               type: array
               suboptions:
                  type: str
            forticlient-compliance-enforcement-portal:
               type: str
            fsae:
               type: str
            fsae-server-for-ntlm:
               type: str
            fsso:
               type: str
            fsso-agent-for-ntlm:
               type: str
            geo-location:
               type: str
            geoip-anycast:
               type: str
            global-label:
               type: str
            groups:
               type: str
            gtp-profile:
               type: str
            http-policy-redirect:
               type: str
            icap-profile:
               type: str
            identity-based:
               type: str
            identity-based-policy:
               type: array
               suboptions:
                  action:
                     type: str
                  application-charts:
                     type: array
                     suboptions:
                        type: str
                  application-list:
                     type: str
                  av-profile:
                     type: str
                  capture-packet:
                     type: str
                  deep-inspection-options:
                     type: str
                  devices:
                     type: str
                  dlp-sensor:
                     type: str
                  dstaddr:
                     type: str
                  dstaddr-negate:
                     type: str
                  endpoint-compliance:
                     type: str
                  groups:
                     type: str
                  icap-profile:
                     type: str
                  id:
                     type: int
                  ips-sensor:
                     type: str
                  logtraffic:
                     type: str
                  logtraffic-app:
                     type: str
                  logtraffic-start:
                     type: str
                  mms-profile:
                     type: str
                  per-ip-shaper:
                     type: str
                  profile-group:
                     type: str
                  profile-protocol-options:
                     type: str
                  profile-type:
                     type: str
                  replacemsg-group:
                     type: str
                  schedule:
                     type: str
                  send-deny-packet:
                     type: str
                  service:
                     type: str
                  service-negate:
                     type: str
                  spamfilter-profile:
                     type: str
                  sslvpn-portal:
                     type: str
                  sslvpn-realm:
                     type: str
                  traffic-shaper:
                     type: str
                  traffic-shaper-reverse:
                     type: str
                  users:
                     type: str
                  utm-status:
                     type: str
                  voip-profile:
                     type: str
                  webfilter-profile:
                     type: str
            identity-based-route:
               type: str
            identity-from:
               type: str
            inbound:
               type: str
            inspection-mode:
               type: str
            internet-service:
               type: str
            internet-service-custom:
               type: str
            internet-service-custom-group:
               type: str
            internet-service-group:
               type: str
            internet-service-id:
               type: str
            internet-service-negate:
               type: str
            internet-service-src:
               type: str
            internet-service-src-custom:
               type: str
            internet-service-src-custom-group:
               type: str
            internet-service-src-group:
               type: str
            internet-service-src-id:
               type: str
            internet-service-src-negate:
               type: str
            ip-based:
               type: str
            ippool:
               type: str
            ips-sensor:
               type: str
            label:
               type: str
            learning-mode:
               type: str
            log-unmatched-traffic:
               type: str
            logtraffic:
               type: str
            logtraffic-app:
               type: str
            logtraffic-start:
               type: str
            match-vip:
               type: str
            mms-profile:
               type: str
            name:
               type: str
            nat:
               type: str
            natinbound:
               type: str
            natip:
               type: str
            natoutbound:
               type: str
            np-acceleration:
               type: str
            ntlm:
               type: str
            ntlm-enabled-browsers:
               type: array
               suboptions:
                  type: str
            ntlm-guest:
               type: str
            outbound:
               type: str
            per-ip-shaper:
               type: str
            permit-any-host:
               type: str
            permit-stun-host:
               type: str
            policyid:
               type: int
            poolname:
               type: str
            profile-group:
               type: str
            profile-protocol-options:
               type: str
            profile-type:
               type: str
            radius-mac-auth-bypass:
               type: str
            redirect-url:
               type: str
            replacemsg-group:
               type: str
            replacemsg-override-group:
               type: str
            reputation-direction:
               type: str
            reputation-minimum:
               type: int
            require-tfa:
               type: str
            rsso:
               type: str
            rtp-addr:
               type: str
            rtp-nat:
               type: str
            scan-botnet-connections:
               type: str
            schedule:
               type: str
            schedule-timeout:
               type: str
            send-deny-packet:
               type: str
            service:
               type: str
            service-negate:
               type: str
            session-ttl:
               type: int
            sessions:
               type: str
            spamfilter-profile:
               type: str
            srcaddr:
               type: str
            srcaddr-negate:
               type: str
            srcaddr6:
               type: str
            srcintf:
               type: str
            ssh-filter-profile:
               type: str
            ssh-policy-redirect:
               type: str
            ssl-mirror:
               type: str
            ssl-mirror-intf:
               type: str
            ssl-ssh-profile:
               type: str
            sslvpn-auth:
               type: str
            sslvpn-ccert:
               type: str
            sslvpn-cipher:
               type: str
            sso-auth-method:
               type: str
            status:
               type: str
            tags:
               type: str
            tcp-mss-receiver:
               type: int
            tcp-mss-sender:
               type: int
            tcp-reset:
               type: str
            tcp-session-without-syn:
               type: str
            timeout-send-rst:
               type: str
            tos:
               type: str
            tos-mask:
               type: str
            tos-negate:
               type: str
            traffic-shaper:
               type: str
            traffic-shaper-reverse:
               type: str
            transaction-based:
               type: str
            url-category:
               type: str
            users:
               type: str
            utm-inspection-mode:
               type: str
            utm-status:
               type: str
            uuid:
               type: str
            vlan-cos-fwd:
               type: int
            vlan-cos-rev:
               type: int
            vlan-filter:
               type: str
            voip-profile:
               type: str
            vpntunnel:
               type: str
            waf-profile:
               type: str
            wanopt:
               type: str
            wanopt-detection:
               type: str
            wanopt-passive-opt:
               type: str
            wanopt-peer:
               type: str
            wanopt-profile:
               type: str
            wccp:
               type: str
            web-auth-cookie:
               type: str
            webcache:
               type: str
            webcache-https:
               type: str
            webfilter-profile:
               type: str
            webproxy-forward-server:
               type: str
            webproxy-profile:
               type: str
            wsso:
               type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/global/pkg/{pkg}/global/footer/policy/{policy}'

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
        '/pm/config/global/pkg/{pkg}/global/footer/policy/{policy}'
    ]

    url_schema = [
        {
            'name': 'pkg',
            'type': 'string'
        },
        {
            'name': 'policy',
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
                        'action': {
                            'type': 'string',
                            'enum': [
                                'deny',
                                'accept',
                                'ipsec',
                                'ssl-vpn'
                            ]
                        },
                        'active-auth-method': {
                            'type': 'string',
                            'enum': [
                                'ntlm',
                                'basic',
                                'digest',
                                'form'
                            ]
                        },
                        'anti-replay': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'app-category': {
                            'type': 'string'
                        },
                        'app-group': {
                            'type': 'string'
                        },
                        'application': {
                            'type': 'array',
                            'items': {
                                'type': 'integer'
                            }
                        },
                        'application-charts': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'top10-app',
                                    'top10-p2p-user',
                                    'top10-media-user'
                                ]
                            }
                        },
                        'application-list': {
                            'type': 'string'
                        },
                        'auth-cert': {
                            'type': 'string'
                        },
                        'auth-method': {
                            'type': 'string',
                            'enum': [
                                'basic',
                                'digest',
                                'ntlm',
                                'fsae',
                                'form',
                                'fsso',
                                'rsso'
                            ]
                        },
                        'auth-path': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'auth-portal': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'auth-redirect-addr': {
                            'type': 'string'
                        },
                        'auto-asic-offload': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'av-profile': {
                            'type': 'string'
                        },
                        'bandwidth': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'block-notification': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'captive-portal-exempt': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'capture-packet': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'casi-profile': {
                            'type': 'string'
                        },
                        'central-nat': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'cifs-profile': {
                            'type': 'string'
                        },
                        'client-reputation': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'client-reputation-mode': {
                            'type': 'string',
                            'enum': [
                                'learning',
                                'monitoring'
                            ]
                        },
                        'comments': {
                            'type': 'string'
                        },
                        'custom-log-fields': {
                            'type': 'string'
                        },
                        'deep-inspection-options': {
                            'type': 'string'
                        },
                        'delay-tcp-npu-session': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'delay-tcp-npu-sessoin': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'device-detection-portal': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'devices': {
                            'type': 'string'
                        },
                        'diffserv-forward': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'diffserv-reverse': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'diffservcode-forward': {
                            'type': 'string'
                        },
                        'diffservcode-rev': {
                            'type': 'string'
                        },
                        'disclaimer': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dlp-sensor': {
                            'type': 'string'
                        },
                        'dnsfilter-profile': {
                            'type': 'string'
                        },
                        'dponly': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dscp-match': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dscp-negate': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dscp-value': {
                            'type': 'string'
                        },
                        'dsri': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dstaddr': {
                            'type': 'string'
                        },
                        'dstaddr-negate': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dstaddr6': {
                            'type': 'string'
                        },
                        'dstintf': {
                            'type': 'string'
                        },
                        'dynamic-profile': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dynamic-profile-access': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'imap',
                                    'smtp',
                                    'pop3',
                                    'http',
                                    'ftp',
                                    'im',
                                    'nntp',
                                    'imaps',
                                    'smtps',
                                    'pop3s',
                                    'https',
                                    'ftps',
                                    'ssh'
                                ]
                            }
                        },
                        'dynamic-profile-fallthrough': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dynamic-profile-group': {
                            'type': 'string'
                        },
                        'email-collect': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'email-collection-portal': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'emailfilter-profile': {
                            'type': 'string'
                        },
                        'endpoint-check': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'endpoint-compliance': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'endpoint-keepalive-interface': {
                            'type': 'string'
                        },
                        'endpoint-profile': {
                            'type': 'string'
                        },
                        'failed-connection': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fall-through-unauthenticated': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'firewall-session-dirty': {
                            'type': 'string',
                            'enum': [
                                'check-all',
                                'check-new'
                            ]
                        },
                        'fixedport': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'forticlient-compliance-devices': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'windows-pc',
                                    'mac',
                                    'iphone-ipad',
                                    'android'
                                ]
                            }
                        },
                        'forticlient-compliance-enforcement-portal': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fsae': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fsae-server-for-ntlm': {
                            'type': 'string'
                        },
                        'fsso': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fsso-agent-for-ntlm': {
                            'type': 'string'
                        },
                        'geo-location': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'geoip-anycast': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'global-label': {
                            'type': 'string'
                        },
                        'groups': {
                            'type': 'string'
                        },
                        'gtp-profile': {
                            'type': 'string'
                        },
                        'http-policy-redirect': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'icap-profile': {
                            'type': 'string'
                        },
                        'identity-based': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'identity-based-policy': {
                            'type': 'array',
                            'items': {
                                'action': {
                                    'type': 'string',
                                    'enum': [
                                        'deny',
                                        'accept'
                                    ]
                                },
                                'application-charts': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string',
                                        'enum': [
                                            'top10-app',
                                            'top10-p2p-user',
                                            'top10-media-user'
                                        ]
                                    }
                                },
                                'application-list': {
                                    'type': 'string'
                                },
                                'av-profile': {
                                    'type': 'string'
                                },
                                'capture-packet': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'deep-inspection-options': {
                                    'type': 'string'
                                },
                                'devices': {
                                    'type': 'string'
                                },
                                'dlp-sensor': {
                                    'type': 'string'
                                },
                                'dstaddr': {
                                    'type': 'string'
                                },
                                'dstaddr-negate': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'endpoint-compliance': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'groups': {
                                    'type': 'string'
                                },
                                'icap-profile': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'ips-sensor': {
                                    'type': 'string'
                                },
                                'logtraffic': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable',
                                        'all',
                                        'utm'
                                    ]
                                },
                                'logtraffic-app': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'logtraffic-start': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'mms-profile': {
                                    'type': 'string'
                                },
                                'per-ip-shaper': {
                                    'type': 'string'
                                },
                                'profile-group': {
                                    'type': 'string'
                                },
                                'profile-protocol-options': {
                                    'type': 'string'
                                },
                                'profile-type': {
                                    'type': 'string',
                                    'enum': [
                                        'single',
                                        'group'
                                    ]
                                },
                                'replacemsg-group': {
                                    'type': 'string'
                                },
                                'schedule': {
                                    'type': 'string'
                                },
                                'send-deny-packet': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'service': {
                                    'type': 'string'
                                },
                                'service-negate': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'spamfilter-profile': {
                                    'type': 'string'
                                },
                                'sslvpn-portal': {
                                    'type': 'string'
                                },
                                'sslvpn-realm': {
                                    'type': 'string'
                                },
                                'traffic-shaper': {
                                    'type': 'string'
                                },
                                'traffic-shaper-reverse': {
                                    'type': 'string'
                                },
                                'users': {
                                    'type': 'string'
                                },
                                'utm-status': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'voip-profile': {
                                    'type': 'string'
                                },
                                'webfilter-profile': {
                                    'type': 'string'
                                }
                            }
                        },
                        'identity-based-route': {
                            'type': 'string'
                        },
                        'identity-from': {
                            'type': 'string',
                            'enum': [
                                'auth',
                                'device'
                            ]
                        },
                        'inbound': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'inspection-mode': {
                            'type': 'string',
                            'enum': [
                                'proxy',
                                'flow'
                            ]
                        },
                        'internet-service': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'internet-service-custom': {
                            'type': 'string'
                        },
                        'internet-service-custom-group': {
                            'type': 'string'
                        },
                        'internet-service-group': {
                            'type': 'string'
                        },
                        'internet-service-id': {
                            'type': 'string'
                        },
                        'internet-service-negate': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'internet-service-src': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'internet-service-src-custom': {
                            'type': 'string'
                        },
                        'internet-service-src-custom-group': {
                            'type': 'string'
                        },
                        'internet-service-src-group': {
                            'type': 'string'
                        },
                        'internet-service-src-id': {
                            'type': 'string'
                        },
                        'internet-service-src-negate': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ip-based': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ippool': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ips-sensor': {
                            'type': 'string'
                        },
                        'label': {
                            'type': 'string'
                        },
                        'learning-mode': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'log-unmatched-traffic': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'logtraffic': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable',
                                'all',
                                'utm'
                            ]
                        },
                        'logtraffic-app': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'logtraffic-start': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'match-vip': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mms-profile': {
                            'type': 'string'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'nat': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'natinbound': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'natip': {
                            'type': 'string'
                        },
                        'natoutbound': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'np-acceleration': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ntlm': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ntlm-enabled-browsers': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'ntlm-guest': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'outbound': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'per-ip-shaper': {
                            'type': 'string'
                        },
                        'permit-any-host': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'permit-stun-host': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'policyid': {
                            'type': 'integer'
                        },
                        'poolname': {
                            'type': 'string'
                        },
                        'profile-group': {
                            'type': 'string'
                        },
                        'profile-protocol-options': {
                            'type': 'string'
                        },
                        'profile-type': {
                            'type': 'string',
                            'enum': [
                                'single',
                                'group'
                            ]
                        },
                        'radius-mac-auth-bypass': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'redirect-url': {
                            'type': 'string'
                        },
                        'replacemsg-group': {
                            'type': 'string'
                        },
                        'replacemsg-override-group': {
                            'type': 'string'
                        },
                        'reputation-direction': {
                            'type': 'string',
                            'enum': [
                                'source',
                                'destination'
                            ]
                        },
                        'reputation-minimum': {
                            'type': 'integer'
                        },
                        'require-tfa': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'rsso': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'rtp-addr': {
                            'type': 'string'
                        },
                        'rtp-nat': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'scan-botnet-connections': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'block',
                                'monitor'
                            ]
                        },
                        'schedule': {
                            'type': 'string'
                        },
                        'schedule-timeout': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'send-deny-packet': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'service': {
                            'type': 'string'
                        },
                        'service-negate': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'session-ttl': {
                            'type': 'integer'
                        },
                        'sessions': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'spamfilter-profile': {
                            'type': 'string'
                        },
                        'srcaddr': {
                            'type': 'string'
                        },
                        'srcaddr-negate': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'srcaddr6': {
                            'type': 'string'
                        },
                        'srcintf': {
                            'type': 'string'
                        },
                        'ssh-filter-profile': {
                            'type': 'string'
                        },
                        'ssh-policy-redirect': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ssl-mirror': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ssl-mirror-intf': {
                            'type': 'string'
                        },
                        'ssl-ssh-profile': {
                            'type': 'string'
                        },
                        'sslvpn-auth': {
                            'type': 'string',
                            'enum': [
                                'any',
                                'local',
                                'radius',
                                'ldap',
                                'tacacs+'
                            ]
                        },
                        'sslvpn-ccert': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'sslvpn-cipher': {
                            'type': 'string',
                            'enum': [
                                'any',
                                'high',
                                'medium'
                            ]
                        },
                        'sso-auth-method': {
                            'type': 'string',
                            'enum': [
                                'fsso',
                                'rsso'
                            ]
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'tags': {
                            'type': 'string'
                        },
                        'tcp-mss-receiver': {
                            'type': 'integer'
                        },
                        'tcp-mss-sender': {
                            'type': 'integer'
                        },
                        'tcp-reset': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'tcp-session-without-syn': {
                            'type': 'string',
                            'enum': [
                                'all',
                                'data-only',
                                'disable'
                            ]
                        },
                        'timeout-send-rst': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'tos': {
                            'type': 'string'
                        },
                        'tos-mask': {
                            'type': 'string'
                        },
                        'tos-negate': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'traffic-shaper': {
                            'type': 'string'
                        },
                        'traffic-shaper-reverse': {
                            'type': 'string'
                        },
                        'transaction-based': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'url-category': {
                            'type': 'string'
                        },
                        'users': {
                            'type': 'string'
                        },
                        'utm-inspection-mode': {
                            'type': 'string',
                            'enum': [
                                'proxy',
                                'flow'
                            ]
                        },
                        'utm-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'uuid': {
                            'type': 'string'
                        },
                        'vlan-cos-fwd': {
                            'type': 'integer'
                        },
                        'vlan-cos-rev': {
                            'type': 'integer'
                        },
                        'vlan-filter': {
                            'type': 'string'
                        },
                        'voip-profile': {
                            'type': 'string'
                        },
                        'vpntunnel': {
                            'type': 'string'
                        },
                        'waf-profile': {
                            'type': 'string'
                        },
                        'wanopt': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'wanopt-detection': {
                            'type': 'string',
                            'enum': [
                                'active',
                                'passive',
                                'off'
                            ]
                        },
                        'wanopt-passive-opt': {
                            'type': 'string',
                            'enum': [
                                'default',
                                'transparent',
                                'non-transparent'
                            ]
                        },
                        'wanopt-peer': {
                            'type': 'string'
                        },
                        'wanopt-profile': {
                            'type': 'string'
                        },
                        'wccp': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'web-auth-cookie': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'webcache': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'webcache-https': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'ssl-server',
                                'any',
                                'enable'
                            ]
                        },
                        'webfilter-profile': {
                            'type': 'string'
                        },
                        'webproxy-forward-server': {
                            'type': 'string'
                        },
                        'webproxy-profile': {
                            'type': 'string'
                        },
                        'wsso': {
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
        'loose_validation': {
            'type': 'bool',
            'required': False,
            'default': False
        },
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
