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
module: fmgr_pkg_footer_policy6
short_description: no description
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/global/pkg/{pkg}/global/footer/policy6
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
    schema_object0:
        methods: [add, set, update]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    action:
                        type: str
                        choices:
                            - 'deny'
                            - 'accept'
                            - 'ipsec'
                            - 'ssl-vpn'
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
                    auto-asic-offload:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    av-profile:
                        type: str
                    casi-profile:
                        type: str
                    cifs-profile:
                        type: str
                    comments:
                        type: str
                    custom-log-fields:
                        type: str
                    deep-inspection-options:
                        type: str
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
                    dlp-sensor:
                        type: str
                    dnsfilter-profile:
                        type: str
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
                    dynamic-profile-group:
                        type: str
                    email-collection-portal:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    emailfilter-profile:
                        type: str
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
                    fsae:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    global-label:
                        type: str
                    groups:
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
                    identity-based-policy6:
                        -
                            action:
                                type: str
                                choices:
                                    - 'deny'
                                    - 'accept'
                            application-list:
                                type: str
                            av-profile:
                                type: str
                            deep-inspection-options:
                                type: str
                            devices:
                                type: str
                            dlp-sensor:
                                type: str
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
                            utm-status:
                                type: str
                                choices:
                                    - 'disable'
                                    - 'enable'
                            voip-profile:
                                type: str
                            webfilter-profile:
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
                    ippool:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    ips-sensor:
                        type: str
                    label:
                        type: str
                    logtraffic:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'all'
                            - 'utm'
                    logtraffic-start:
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
                    natoutbound:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    np-accelation:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    np-acceleration:
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
                    replacemsg-group:
                        type: str
                    replacemsg-override-group:
                        type: str
                    rsso:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
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
                    session-ttl:
                        type: int
                    spamfilter-profile:
                        type: str
                    srcaddr:
                        type: str
                    srcaddr-negate:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
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
                    webfilter-profile:
                        type: str
    schema_object1:
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
                            - 'anti-replay'
                            - 'app-category'
                            - 'app-group'
                            - 'application'
                            - 'application-charts'
                            - 'application-list'
                            - 'auto-asic-offload'
                            - 'av-profile'
                            - 'casi-profile'
                            - 'cifs-profile'
                            - 'comments'
                            - 'custom-log-fields'
                            - 'deep-inspection-options'
                            - 'device-detection-portal'
                            - 'devices'
                            - 'diffserv-forward'
                            - 'diffserv-reverse'
                            - 'diffservcode-forward'
                            - 'diffservcode-rev'
                            - 'dlp-sensor'
                            - 'dnsfilter-profile'
                            - 'dscp-match'
                            - 'dscp-negate'
                            - 'dscp-value'
                            - 'dsri'
                            - 'dstaddr'
                            - 'dstaddr-negate'
                            - 'dstintf'
                            - 'dynamic-profile'
                            - 'dynamic-profile-access'
                            - 'dynamic-profile-group'
                            - 'email-collection-portal'
                            - 'emailfilter-profile'
                            - 'firewall-session-dirty'
                            - 'fixedport'
                            - 'fsae'
                            - 'global-label'
                            - 'groups'
                            - 'http-policy-redirect'
                            - 'icap-profile'
                            - 'identity-based'
                            - 'identity-from'
                            - 'inbound'
                            - 'inspection-mode'
                            - 'ippool'
                            - 'ips-sensor'
                            - 'label'
                            - 'logtraffic'
                            - 'logtraffic-start'
                            - 'mms-profile'
                            - 'name'
                            - 'nat'
                            - 'natinbound'
                            - 'natoutbound'
                            - 'np-accelation'
                            - 'np-acceleration'
                            - 'outbound'
                            - 'per-ip-shaper'
                            - 'policyid'
                            - 'poolname'
                            - 'profile-group'
                            - 'profile-protocol-options'
                            - 'profile-type'
                            - 'replacemsg-group'
                            - 'replacemsg-override-group'
                            - 'rsso'
                            - 'schedule'
                            - 'send-deny-packet'
                            - 'service'
                            - 'service-negate'
                            - 'session-ttl'
                            - 'spamfilter-profile'
                            - 'srcaddr'
                            - 'srcaddr-negate'
                            - 'srcintf'
                            - 'ssh-filter-profile'
                            - 'ssh-policy-redirect'
                            - 'ssl-mirror'
                            - 'ssl-mirror-intf'
                            - 'ssl-ssh-profile'
                            - 'sslvpn-auth'
                            - 'sslvpn-ccert'
                            - 'sslvpn-cipher'
                            - 'status'
                            - 'tags'
                            - 'tcp-mss-receiver'
                            - 'tcp-mss-sender'
                            - 'tcp-session-without-syn'
                            - 'timeout-send-rst'
                            - 'tos'
                            - 'tos-mask'
                            - 'tos-negate'
                            - 'traffic-shaper'
                            - 'traffic-shaper-reverse'
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
                            - 'webfilter-profile'
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

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FOOTER/POLICY6
      fmgr_pkg_footer_policy6:
         method: <value in [add, set, update]>
         url_params:
            pkg: <value of string>
         params:
            -
               data:
                 -
                     action: <value in [deny, accept, ipsec, ...]>
                     anti-replay: <value in [disable, enable]>
                     app-category: <value of string>
                     app-group: <value of string>
                     application:
                       - <value of integer>
                     application-charts:
                       - <value in [top10-app, top10-p2p-user, top10-media-user]>
                     application-list: <value of string>
                     auto-asic-offload: <value in [disable, enable]>
                     av-profile: <value of string>
                     casi-profile: <value of string>
                     cifs-profile: <value of string>
                     comments: <value of string>
                     custom-log-fields: <value of string>
                     deep-inspection-options: <value of string>
                     device-detection-portal: <value in [disable, enable]>
                     devices: <value of string>
                     diffserv-forward: <value in [disable, enable]>
                     diffserv-reverse: <value in [disable, enable]>
                     diffservcode-forward: <value of string>
                     diffservcode-rev: <value of string>
                     dlp-sensor: <value of string>
                     dnsfilter-profile: <value of string>
                     dscp-match: <value in [disable, enable]>
                     dscp-negate: <value in [disable, enable]>
                     dscp-value: <value of string>
                     dsri: <value in [disable, enable]>
                     dstaddr: <value of string>
                     dstaddr-negate: <value in [disable, enable]>
                     dstintf: <value of string>
                     dynamic-profile: <value in [disable, enable]>
                     dynamic-profile-access:
                       - <value in [imap, smtp, pop3, ...]>
                     dynamic-profile-group: <value of string>
                     email-collection-portal: <value in [disable, enable]>
                     emailfilter-profile: <value of string>
                     firewall-session-dirty: <value in [check-all, check-new]>
                     fixedport: <value in [disable, enable]>
                     fsae: <value in [disable, enable]>
                     global-label: <value of string>
                     groups: <value of string>
                     http-policy-redirect: <value in [disable, enable]>
                     icap-profile: <value of string>
                     identity-based: <value in [disable, enable]>
                     identity-based-policy6:
                       -
                           action: <value in [deny, accept]>
                           application-list: <value of string>
                           av-profile: <value of string>
                           deep-inspection-options: <value of string>
                           devices: <value of string>
                           dlp-sensor: <value of string>
                           endpoint-compliance: <value in [disable, enable]>
                           groups: <value of string>
                           icap-profile: <value of string>
                           id: <value of integer>
                           ips-sensor: <value of string>
                           logtraffic: <value in [disable, enable, all, ...]>
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
                           utm-status: <value in [disable, enable]>
                           voip-profile: <value of string>
                           webfilter-profile: <value of string>
                     identity-from: <value in [auth, device]>
                     inbound: <value in [disable, enable]>
                     inspection-mode: <value in [proxy, flow]>
                     ippool: <value in [disable, enable]>
                     ips-sensor: <value of string>
                     label: <value of string>
                     logtraffic: <value in [disable, enable, all, ...]>
                     logtraffic-start: <value in [disable, enable]>
                     mms-profile: <value of string>
                     name: <value of string>
                     nat: <value in [disable, enable]>
                     natinbound: <value in [disable, enable]>
                     natoutbound: <value in [disable, enable]>
                     np-accelation: <value in [disable, enable]>
                     np-acceleration: <value in [disable, enable]>
                     outbound: <value in [disable, enable]>
                     per-ip-shaper: <value of string>
                     policyid: <value of integer>
                     poolname: <value of string>
                     profile-group: <value of string>
                     profile-protocol-options: <value of string>
                     profile-type: <value in [single, group]>
                     replacemsg-group: <value of string>
                     replacemsg-override-group: <value of string>
                     rsso: <value in [disable, enable]>
                     schedule: <value of string>
                     send-deny-packet: <value in [disable, enable]>
                     service: <value of string>
                     service-negate: <value in [disable, enable]>
                     session-ttl: <value of integer>
                     spamfilter-profile: <value of string>
                     srcaddr: <value of string>
                     srcaddr-negate: <value in [disable, enable]>
                     srcintf: <value of string>
                     ssh-filter-profile: <value of string>
                     ssh-policy-redirect: <value in [disable, enable]>
                     ssl-mirror: <value in [disable, enable]>
                     ssl-mirror-intf: <value of string>
                     ssl-ssh-profile: <value of string>
                     sslvpn-auth: <value in [any, local, radius, ...]>
                     sslvpn-ccert: <value in [disable, enable]>
                     sslvpn-cipher: <value in [any, high, medium]>
                     status: <value in [disable, enable]>
                     tags: <value of string>
                     tcp-mss-receiver: <value of integer>
                     tcp-mss-sender: <value of integer>
                     tcp-session-without-syn: <value in [all, data-only, disable]>
                     timeout-send-rst: <value in [disable, enable]>
                     tos: <value of string>
                     tos-mask: <value of string>
                     tos-negate: <value in [disable, enable]>
                     traffic-shaper: <value of string>
                     traffic-shaper-reverse: <value of string>
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
                     webfilter-profile: <value of string>

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FOOTER/POLICY6
      fmgr_pkg_footer_policy6:
         method: <value in [get]>
         url_params:
            pkg: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [action, anti-replay, app-category, ...]>
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
         data:
            type: array
            suboptions:
               policyid:
                  type: int
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/global/pkg/{pkg}/global/footer/policy6'
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
               auto-asic-offload:
                  type: str
               av-profile:
                  type: str
               casi-profile:
                  type: str
               cifs-profile:
                  type: str
               comments:
                  type: str
               custom-log-fields:
                  type: str
               deep-inspection-options:
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
               dlp-sensor:
                  type: str
               dnsfilter-profile:
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
               dstintf:
                  type: str
               dynamic-profile:
                  type: str
               dynamic-profile-access:
                  type: array
                  suboptions:
                     type: str
               dynamic-profile-group:
                  type: str
               email-collection-portal:
                  type: str
               emailfilter-profile:
                  type: str
               firewall-session-dirty:
                  type: str
               fixedport:
                  type: str
               fsae:
                  type: str
               global-label:
                  type: str
               groups:
                  type: str
               http-policy-redirect:
                  type: str
               icap-profile:
                  type: str
               identity-based:
                  type: str
               identity-based-policy6:
                  type: array
                  suboptions:
                     action:
                        type: str
                     application-list:
                        type: str
                     av-profile:
                        type: str
                     deep-inspection-options:
                        type: str
                     devices:
                        type: str
                     dlp-sensor:
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
                     utm-status:
                        type: str
                     voip-profile:
                        type: str
                     webfilter-profile:
                        type: str
               identity-from:
                  type: str
               inbound:
                  type: str
               inspection-mode:
                  type: str
               ippool:
                  type: str
               ips-sensor:
                  type: str
               label:
                  type: str
               logtraffic:
                  type: str
               logtraffic-start:
                  type: str
               mms-profile:
                  type: str
               name:
                  type: str
               nat:
                  type: str
               natinbound:
                  type: str
               natoutbound:
                  type: str
               np-accelation:
                  type: str
               np-acceleration:
                  type: str
               outbound:
                  type: str
               per-ip-shaper:
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
               replacemsg-group:
                  type: str
               replacemsg-override-group:
                  type: str
               rsso:
                  type: str
               schedule:
                  type: str
               send-deny-packet:
                  type: str
               service:
                  type: str
               service-negate:
                  type: str
               session-ttl:
                  type: int
               spamfilter-profile:
                  type: str
               srcaddr:
                  type: str
               srcaddr-negate:
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
               status:
                  type: str
               tags:
                  type: str
               tcp-mss-receiver:
                  type: int
               tcp-mss-sender:
                  type: int
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
               webfilter-profile:
                  type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/global/pkg/{pkg}/global/footer/policy6'

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
        '/pm/config/global/pkg/{pkg}/global/footer/policy6'
    ]

    url_schema = [
        {
            'name': 'pkg',
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
                        'action': {
                            'type': 'string',
                            'enum': [
                                'deny',
                                'accept',
                                'ipsec',
                                'ssl-vpn'
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
                        'casi-profile': {
                            'type': 'string'
                        },
                        'cifs-profile': {
                            'type': 'string'
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
                        'dlp-sensor': {
                            'type': 'string'
                        },
                        'dnsfilter-profile': {
                            'type': 'string'
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
                                    'ftps'
                                ]
                            }
                        },
                        'dynamic-profile-group': {
                            'type': 'string'
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
                        'fsae': {
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
                        'identity-based-policy6': {
                            'type': 'array',
                            'items': {
                                'action': {
                                    'type': 'string',
                                    'enum': [
                                        'deny',
                                        'accept'
                                    ]
                                },
                                'application-list': {
                                    'type': 'string'
                                },
                                'av-profile': {
                                    'type': 'string'
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
                        'logtraffic': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable',
                                'all',
                                'utm'
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
                        'natoutbound': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'np-accelation': {
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
                        'replacemsg-group': {
                            'type': 'string'
                        },
                        'replacemsg-override-group': {
                            'type': 'string'
                        },
                        'rsso': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
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
                        'session-ttl': {
                            'type': 'integer'
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
                        'webfilter-profile': {
                            'type': 'string'
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
                                'action',
                                'anti-replay',
                                'app-category',
                                'app-group',
                                'application',
                                'application-charts',
                                'application-list',
                                'auto-asic-offload',
                                'av-profile',
                                'casi-profile',
                                'cifs-profile',
                                'comments',
                                'custom-log-fields',
                                'deep-inspection-options',
                                'device-detection-portal',
                                'devices',
                                'diffserv-forward',
                                'diffserv-reverse',
                                'diffservcode-forward',
                                'diffservcode-rev',
                                'dlp-sensor',
                                'dnsfilter-profile',
                                'dscp-match',
                                'dscp-negate',
                                'dscp-value',
                                'dsri',
                                'dstaddr',
                                'dstaddr-negate',
                                'dstintf',
                                'dynamic-profile',
                                'dynamic-profile-access',
                                'dynamic-profile-group',
                                'email-collection-portal',
                                'emailfilter-profile',
                                'firewall-session-dirty',
                                'fixedport',
                                'fsae',
                                'global-label',
                                'groups',
                                'http-policy-redirect',
                                'icap-profile',
                                'identity-based',
                                'identity-from',
                                'inbound',
                                'inspection-mode',
                                'ippool',
                                'ips-sensor',
                                'label',
                                'logtraffic',
                                'logtraffic-start',
                                'mms-profile',
                                'name',
                                'nat',
                                'natinbound',
                                'natoutbound',
                                'np-accelation',
                                'np-acceleration',
                                'outbound',
                                'per-ip-shaper',
                                'policyid',
                                'poolname',
                                'profile-group',
                                'profile-protocol-options',
                                'profile-type',
                                'replacemsg-group',
                                'replacemsg-override-group',
                                'rsso',
                                'schedule',
                                'send-deny-packet',
                                'service',
                                'service-negate',
                                'session-ttl',
                                'spamfilter-profile',
                                'srcaddr',
                                'srcaddr-negate',
                                'srcintf',
                                'ssh-filter-profile',
                                'ssh-policy-redirect',
                                'ssl-mirror',
                                'ssl-mirror-intf',
                                'ssl-ssh-profile',
                                'sslvpn-auth',
                                'sslvpn-ccert',
                                'sslvpn-cipher',
                                'status',
                                'tags',
                                'tcp-mss-receiver',
                                'tcp-mss-sender',
                                'tcp-session-without-syn',
                                'timeout-send-rst',
                                'tos',
                                'tos-mask',
                                'tos-negate',
                                'traffic-shaper',
                                'traffic-shaper-reverse',
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
                                'webfilter-profile'
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
