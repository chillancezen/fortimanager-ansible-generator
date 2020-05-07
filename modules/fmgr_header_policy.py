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
module: fmgr_header_policy
short_description: no description
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get ] the following apis.
    - /pm/config/adom/{adom}/obj/global/header/policy
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
    schema_object0:
        methods: [get]
        description: ''
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
                            - 'action'
                            - 'active-auth-method'
                            - 'anti-replay'
                            - 'app-category'
                            - 'app-group'
                            - 'application'
                            - 'application-charts'
                            - 'application-list'
                            - 'auth-cert'
                            - 'auth-method'
                            - 'auth-path'
                            - 'auth-portal'
                            - 'auth-redirect-addr'
                            - 'auto-asic-offload'
                            - 'av-profile'
                            - 'bandwidth'
                            - 'block-notification'
                            - 'captive-portal-exempt'
                            - 'capture-packet'
                            - 'casi-profile'
                            - 'central-nat'
                            - 'cifs-profile'
                            - 'client-reputation'
                            - 'client-reputation-mode'
                            - 'custom-log-fields'
                            - 'deep-inspection-options'
                            - 'delay-tcp-npu-session'
                            - 'delay-tcp-npu-sessoin'
                            - 'device-detection-portal'
                            - 'devices'
                            - 'diffserv-forward'
                            - 'diffserv-reverse'
                            - 'diffservcode-forward'
                            - 'diffservcode-rev'
                            - 'disclaimer'
                            - 'dlp-sensor'
                            - 'dnsfilter-profile'
                            - 'dponly'
                            - 'dscp-match'
                            - 'dscp-negate'
                            - 'dscp-value'
                            - 'dsri'
                            - 'dstaddr'
                            - 'dstaddr-negate'
                            - 'dstaddr6'
                            - 'dstintf'
                            - 'dynamic-profile'
                            - 'dynamic-profile-access'
                            - 'dynamic-profile-fallthrough'
                            - 'dynamic-profile-group'
                            - 'email-collect'
                            - 'email-collection-portal'
                            - 'emailfilter-profile'
                            - 'endpoint-check'
                            - 'endpoint-compliance'
                            - 'endpoint-keepalive-interface'
                            - 'endpoint-profile'
                            - 'failed-connection'
                            - 'fall-through-unauthenticated'
                            - 'firewall-session-dirty'
                            - 'fixedport'
                            - 'forticlient-compliance-devices'
                            - 'forticlient-compliance-enforcement-portal'
                            - 'fsae'
                            - 'fsae-server-for-ntlm'
                            - 'fsso'
                            - 'fsso-agent-for-ntlm'
                            - 'geo-location'
                            - 'geoip-anycast'
                            - 'global-label'
                            - 'groups'
                            - 'gtp-profile'
                            - 'http-policy-redirect'
                            - 'icap-profile'
                            - 'identity-based'
                            - 'identity-based-route'
                            - 'identity-from'
                            - 'inbound'
                            - 'inspection-mode'
                            - 'internet-service'
                            - 'internet-service-custom'
                            - 'internet-service-custom-group'
                            - 'internet-service-group'
                            - 'internet-service-id'
                            - 'internet-service-negate'
                            - 'internet-service-src'
                            - 'internet-service-src-custom'
                            - 'internet-service-src-custom-group'
                            - 'internet-service-src-group'
                            - 'internet-service-src-id'
                            - 'internet-service-src-negate'
                            - 'ip-based'
                            - 'ippool'
                            - 'ips-sensor'
                            - 'label'
                            - 'learning-mode'
                            - 'log-unmatched-traffic'
                            - 'logtraffic'
                            - 'logtraffic-app'
                            - 'logtraffic-start'
                            - 'match-vip'
                            - 'mms-profile'
                            - 'name'
                            - 'nat'
                            - 'natinbound'
                            - 'natip'
                            - 'natoutbound'
                            - 'np-acceleration'
                            - 'ntlm'
                            - 'ntlm-enabled-browsers'
                            - 'ntlm-guest'
                            - 'outbound'
                            - 'per-ip-shaper'
                            - 'permit-any-host'
                            - 'permit-stun-host'
                            - 'policyid'
                            - 'poolname'
                            - 'profile-group'
                            - 'profile-protocol-options'
                            - 'profile-type'
                            - 'radius-mac-auth-bypass'
                            - 'redirect-url'
                            - 'replacemsg-group'
                            - 'replacemsg-override-group'
                            - 'reputation-direction'
                            - 'reputation-minimum'
                            - 'require-tfa'
                            - 'rsso'
                            - 'rtp-addr'
                            - 'rtp-nat'
                            - 'scan-botnet-connections'
                            - 'schedule'
                            - 'schedule-timeout'
                            - 'send-deny-packet'
                            - 'service'
                            - 'service-negate'
                            - 'session-ttl'
                            - 'sessions'
                            - 'spamfilter-profile'
                            - 'srcaddr'
                            - 'srcaddr-negate'
                            - 'srcaddr6'
                            - 'srcintf'
                            - 'ssh-filter-profile'
                            - 'ssh-policy-redirect'
                            - 'ssl-mirror'
                            - 'ssl-mirror-intf'
                            - 'ssl-ssh-profile'
                            - 'sslvpn-auth'
                            - 'sslvpn-ccert'
                            - 'sslvpn-cipher'
                            - 'sso-auth-method'
                            - 'status'
                            - 'tags'
                            - 'tcp-mss-receiver'
                            - 'tcp-mss-sender'
                            - 'tcp-reset'
                            - 'tcp-session-without-syn'
                            - 'timeout-send-rst'
                            - 'tos'
                            - 'tos-mask'
                            - 'tos-negate'
                            - 'traffic-shaper'
                            - 'traffic-shaper-reverse'
                            - 'transaction-based'
                            - 'url-category'
                            - 'users'
                            - 'utm-inspection-mode'
                            - 'utm-status'
                            - 'uuid'
                            - 'vlan-cos-fwd'
                            - 'vlan-cos-rev'
                            - 'vlan-filter'
                            - 'voip-profile'
                            - 'vpntunnel'
                            - 'waf-profile'
                            - 'wanopt'
                            - 'wanopt-detection'
                            - 'wanopt-passive-opt'
                            - 'wanopt-peer'
                            - 'wanopt-profile'
                            - 'wccp'
                            - 'web-auth-cookie'
                            - 'webcache'
                            - 'webcache-https'
                            - 'webfilter-profile'
                            - 'webproxy-forward-server'
                            - 'webproxy-profile'
                            - 'wsso'
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

    - name: REQUESTING /PM/CONFIG/OBJ/HEADER/POLICY
      fmgr_header_policy:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [action, active-auth-method, anti-replay, ...]>
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
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            type: array
            suboptions:
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
            example: '/pm/config/adom/{adom}/obj/global/header/policy'

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
        '/pm/config/adom/{adom}/obj/global/header/policy'
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
                                'action',
                                'active-auth-method',
                                'anti-replay',
                                'app-category',
                                'app-group',
                                'application',
                                'application-charts',
                                'application-list',
                                'auth-cert',
                                'auth-method',
                                'auth-path',
                                'auth-portal',
                                'auth-redirect-addr',
                                'auto-asic-offload',
                                'av-profile',
                                'bandwidth',
                                'block-notification',
                                'captive-portal-exempt',
                                'capture-packet',
                                'casi-profile',
                                'central-nat',
                                'cifs-profile',
                                'client-reputation',
                                'client-reputation-mode',
                                'custom-log-fields',
                                'deep-inspection-options',
                                'delay-tcp-npu-session',
                                'delay-tcp-npu-sessoin',
                                'device-detection-portal',
                                'devices',
                                'diffserv-forward',
                                'diffserv-reverse',
                                'diffservcode-forward',
                                'diffservcode-rev',
                                'disclaimer',
                                'dlp-sensor',
                                'dnsfilter-profile',
                                'dponly',
                                'dscp-match',
                                'dscp-negate',
                                'dscp-value',
                                'dsri',
                                'dstaddr',
                                'dstaddr-negate',
                                'dstaddr6',
                                'dstintf',
                                'dynamic-profile',
                                'dynamic-profile-access',
                                'dynamic-profile-fallthrough',
                                'dynamic-profile-group',
                                'email-collect',
                                'email-collection-portal',
                                'emailfilter-profile',
                                'endpoint-check',
                                'endpoint-compliance',
                                'endpoint-keepalive-interface',
                                'endpoint-profile',
                                'failed-connection',
                                'fall-through-unauthenticated',
                                'firewall-session-dirty',
                                'fixedport',
                                'forticlient-compliance-devices',
                                'forticlient-compliance-enforcement-portal',
                                'fsae',
                                'fsae-server-for-ntlm',
                                'fsso',
                                'fsso-agent-for-ntlm',
                                'geo-location',
                                'geoip-anycast',
                                'global-label',
                                'groups',
                                'gtp-profile',
                                'http-policy-redirect',
                                'icap-profile',
                                'identity-based',
                                'identity-based-route',
                                'identity-from',
                                'inbound',
                                'inspection-mode',
                                'internet-service',
                                'internet-service-custom',
                                'internet-service-custom-group',
                                'internet-service-group',
                                'internet-service-id',
                                'internet-service-negate',
                                'internet-service-src',
                                'internet-service-src-custom',
                                'internet-service-src-custom-group',
                                'internet-service-src-group',
                                'internet-service-src-id',
                                'internet-service-src-negate',
                                'ip-based',
                                'ippool',
                                'ips-sensor',
                                'label',
                                'learning-mode',
                                'log-unmatched-traffic',
                                'logtraffic',
                                'logtraffic-app',
                                'logtraffic-start',
                                'match-vip',
                                'mms-profile',
                                'name',
                                'nat',
                                'natinbound',
                                'natip',
                                'natoutbound',
                                'np-acceleration',
                                'ntlm',
                                'ntlm-enabled-browsers',
                                'ntlm-guest',
                                'outbound',
                                'per-ip-shaper',
                                'permit-any-host',
                                'permit-stun-host',
                                'policyid',
                                'poolname',
                                'profile-group',
                                'profile-protocol-options',
                                'profile-type',
                                'radius-mac-auth-bypass',
                                'redirect-url',
                                'replacemsg-group',
                                'replacemsg-override-group',
                                'reputation-direction',
                                'reputation-minimum',
                                'require-tfa',
                                'rsso',
                                'rtp-addr',
                                'rtp-nat',
                                'scan-botnet-connections',
                                'schedule',
                                'schedule-timeout',
                                'send-deny-packet',
                                'service',
                                'service-negate',
                                'session-ttl',
                                'sessions',
                                'spamfilter-profile',
                                'srcaddr',
                                'srcaddr-negate',
                                'srcaddr6',
                                'srcintf',
                                'ssh-filter-profile',
                                'ssh-policy-redirect',
                                'ssl-mirror',
                                'ssl-mirror-intf',
                                'ssl-ssh-profile',
                                'sslvpn-auth',
                                'sslvpn-ccert',
                                'sslvpn-cipher',
                                'sso-auth-method',
                                'status',
                                'tags',
                                'tcp-mss-receiver',
                                'tcp-mss-sender',
                                'tcp-reset',
                                'tcp-session-without-syn',
                                'timeout-send-rst',
                                'tos',
                                'tos-mask',
                                'tos-negate',
                                'traffic-shaper',
                                'traffic-shaper-reverse',
                                'transaction-based',
                                'url-category',
                                'users',
                                'utm-inspection-mode',
                                'utm-status',
                                'uuid',
                                'vlan-cos-fwd',
                                'vlan-cos-rev',
                                'vlan-filter',
                                'voip-profile',
                                'vpntunnel',
                                'waf-profile',
                                'wanopt',
                                'wanopt-detection',
                                'wanopt-passive-opt',
                                'wanopt-peer',
                                'wanopt-profile',
                                'wccp',
                                'web-auth-cookie',
                                'webcache',
                                'webcache-https',
                                'webfilter-profile',
                                'webproxy-forward-server',
                                'webproxy-profile',
                                'wsso'
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
            'get': 'object0'
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
                'get'
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
