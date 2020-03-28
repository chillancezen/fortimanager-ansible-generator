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
module: fmgr_pkg_firewall_proxypolicy
short_description: Configure proxy policies.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/pkg/{pkg}/firewall/proxy-policy
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
            pkg:
                type: str
    schema_object0:
        methods: [add, set, update]
        description: 'Configure proxy policies.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    action:
                        type: str
                        description: 'Accept or deny traffic matching the policy parameters.'
                        choices:
                            - 'accept'
                            - 'deny'
                            - 'redirect'
                    application-list:
                        type: str
                        description: 'Name of an existing Application list.'
                    av-profile:
                        type: str
                        description: 'Name of an existing Antivirus profile.'
                    comments:
                        type: str
                        description: 'Optional comments.'
                    disclaimer:
                        type: str
                        description: 'Web proxy disclaimer setting: by domain, policy, or user.'
                        choices:
                            - 'disable'
                            - 'domain'
                            - 'policy'
                            - 'user'
                    dlp-sensor:
                        type: str
                        description: 'Name of an existing DLP sensor.'
                    dstaddr:
                        type: str
                        description: 'Destination address objects.'
                    dstaddr-negate:
                        type: str
                        description: 'When enabled, destination addresses match against any address EXCEPT the specified destination addresses.'
                        choices:
                            - 'disable'
                            - 'enable'
                    dstaddr6:
                        type: str
                        description: 'IPv6 destination address objects.'
                    dstintf:
                        type: str
                        description: 'Destination interface names.'
                    global-label:
                        type: str
                        description: 'Global web-based manager visible label.'
                    groups:
                        type: str
                        description: 'Names of group objects.'
                    http-tunnel-auth:
                        type: str
                        description: 'Enable/disable HTTP tunnel authentication.'
                        choices:
                            - 'disable'
                            - 'enable'
                    icap-profile:
                        type: str
                        description: 'Name of an existing ICAP profile.'
                    internet-service:
                        type: str
                        description: 'Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.'
                        choices:
                            - 'disable'
                            - 'enable'
                    internet-service-custom:
                        type: str
                        description: 'Custom Internet Service name.'
                    internet-service-id:
                        type: str
                        description: 'Internet Service ID.'
                    internet-service-negate:
                        type: str
                        description: 'When enabled, Internet Services match against any internet service EXCEPT the selected Internet Service.'
                        choices:
                            - 'disable'
                            - 'enable'
                    ips-sensor:
                        type: str
                        description: 'Name of an existing IPS sensor.'
                    label:
                        type: str
                        description: 'VDOM-specific GUI visible label.'
                    logtraffic:
                        type: str
                        description: 'Enable/disable logging traffic through the policy.'
                        choices:
                            - 'disable'
                            - 'all'
                            - 'utm'
                    logtraffic-start:
                        type: str
                        description: 'Enable/disable policy log traffic start.'
                        choices:
                            - 'disable'
                            - 'enable'
                    mms-profile:
                        type: str
                        description: 'Name of an existing MMS profile.'
                    policyid:
                        type: int
                        description: 'Policy ID.'
                    poolname:
                        type: str
                        description: 'Name of IP pool object.'
                    profile-group:
                        type: str
                        description: 'Name of profile group.'
                    profile-protocol-options:
                        type: str
                        description: 'Name of an existing Protocol options profile.'
                    profile-type:
                        type: str
                        description: 'Determine whether the firewall policy allows security profile groups or single profiles only.'
                        choices:
                            - 'single'
                            - 'group'
                    proxy:
                        type: str
                        description: 'Type of explicit proxy.'
                        choices:
                            - 'explicit-web'
                            - 'transparent-web'
                            - 'ftp'
                            - 'wanopt'
                            - 'ssh'
                            - 'ssh-tunnel'
                    redirect-url:
                        type: str
                        description: 'Redirect URL for further explicit web proxy processing.'
                    replacemsg-override-group:
                        type: str
                        description: 'Authentication replacement message override group.'
                    scan-botnet-connections:
                        type: str
                        description: 'Enable/disable scanning of connections to Botnet servers.'
                        choices:
                            - 'disable'
                            - 'block'
                            - 'monitor'
                    schedule:
                        type: str
                        description: 'Name of schedule object.'
                    service:
                        type: str
                        description: 'Name of service objects.'
                    service-negate:
                        type: str
                        description: 'When enabled, services match against any service EXCEPT the specified destination services.'
                        choices:
                            - 'disable'
                            - 'enable'
                    spamfilter-profile:
                        type: str
                        description: 'Name of an existing Spam filter profile.'
                    srcaddr:
                        type: str
                        description: 'Source address objects (must be set when using Web proxy).'
                    srcaddr-negate:
                        type: str
                        description: 'When enabled, source addresses match against any address EXCEPT the specified source addresses.'
                        choices:
                            - 'disable'
                            - 'enable'
                    srcaddr6:
                        type: str
                        description: 'IPv6 source address objects.'
                    srcintf:
                        type: str
                        description: 'Source interface names.'
                    ssl-ssh-profile:
                        type: str
                        description: 'Name of an existing SSL SSH profile.'
                    status:
                        type: str
                        description: 'Enable/disable the active status of the policy.'
                        choices:
                            - 'disable'
                            - 'enable'
                    tags:
                        type: str
                        description: 'Names of object-tags applied to address. Tags need to be preconfigured in config system object-tag. Separate multiple ...'
                    transparent:
                        type: str
                        description: 'Enable to use the IP address of the client to connect to the server.'
                        choices:
                            - 'disable'
                            - 'enable'
                    users:
                        type: str
                        description: 'Names of user objects.'
                    utm-status:
                        type: str
                        description: 'Enable the use of UTM profiles/sensors/lists.'
                        choices:
                            - 'disable'
                            - 'enable'
                    uuid:
                        type: str
                        description: 'Universally Unique Identifier (UUID; automatically assigned but can be manually reset).'
                    waf-profile:
                        type: str
                        description: 'Name of an existing Web application firewall profile.'
                    webcache:
                        type: str
                        description: 'Enable/disable web caching.'
                        choices:
                            - 'disable'
                            - 'enable'
                    webcache-https:
                        type: str
                        description: 'Enable/disable web caching for HTTPS (Requires deep-inspection enabled in ssl-ssh-profile).'
                        choices:
                            - 'disable'
                            - 'enable'
                    webfilter-profile:
                        type: str
                        description: 'Name of an existing Web filter profile.'
                    webproxy-forward-server:
                        type: str
                        description: 'Name of web proxy forward server.'
                    webproxy-profile:
                        type: str
                        description: 'Name of web proxy profile.'
    schema_object1:
        methods: [get]
        description: 'Configure proxy policies.'
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
                            - 'application-list'
                            - 'av-profile'
                            - 'comments'
                            - 'disclaimer'
                            - 'dlp-sensor'
                            - 'dstaddr'
                            - 'dstaddr-negate'
                            - 'dstaddr6'
                            - 'dstintf'
                            - 'global-label'
                            - 'groups'
                            - 'http-tunnel-auth'
                            - 'icap-profile'
                            - 'internet-service'
                            - 'internet-service-custom'
                            - 'internet-service-id'
                            - 'internet-service-negate'
                            - 'ips-sensor'
                            - 'label'
                            - 'logtraffic'
                            - 'logtraffic-start'
                            - 'mms-profile'
                            - 'policyid'
                            - 'poolname'
                            - 'profile-group'
                            - 'profile-protocol-options'
                            - 'profile-type'
                            - 'proxy'
                            - 'redirect-url'
                            - 'replacemsg-override-group'
                            - 'scan-botnet-connections'
                            - 'schedule'
                            - 'service'
                            - 'service-negate'
                            - 'spamfilter-profile'
                            - 'srcaddr'
                            - 'srcaddr-negate'
                            - 'srcaddr6'
                            - 'srcintf'
                            - 'ssl-ssh-profile'
                            - 'status'
                            - 'tags'
                            - 'transparent'
                            - 'users'
                            - 'utm-status'
                            - 'uuid'
                            - 'waf-profile'
                            - 'webcache'
                            - 'webcache-https'
                            - 'webfilter-profile'
                            - 'webproxy-forward-server'
                            - 'webproxy-profile'
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

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/PROXY-POLICY
      fmgr_pkg_firewall_proxypolicy:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
         params:
            -
               data:
                 -
                     action: <value in [accept, deny, redirect]>
                     application-list: <value of string>
                     av-profile: <value of string>
                     comments: <value of string>
                     disclaimer: <value in [disable, domain, policy, ...]>
                     dlp-sensor: <value of string>
                     dstaddr: <value of string>
                     dstaddr-negate: <value in [disable, enable]>
                     dstaddr6: <value of string>
                     dstintf: <value of string>
                     global-label: <value of string>
                     groups: <value of string>
                     http-tunnel-auth: <value in [disable, enable]>
                     icap-profile: <value of string>
                     internet-service: <value in [disable, enable]>
                     internet-service-custom: <value of string>
                     internet-service-id: <value of string>
                     internet-service-negate: <value in [disable, enable]>
                     ips-sensor: <value of string>
                     label: <value of string>
                     logtraffic: <value in [disable, all, utm]>
                     logtraffic-start: <value in [disable, enable]>
                     mms-profile: <value of string>
                     policyid: <value of integer>
                     poolname: <value of string>
                     profile-group: <value of string>
                     profile-protocol-options: <value of string>
                     profile-type: <value in [single, group]>
                     proxy: <value in [explicit-web, transparent-web, ftp, ...]>
                     redirect-url: <value of string>
                     replacemsg-override-group: <value of string>
                     scan-botnet-connections: <value in [disable, block, monitor]>
                     schedule: <value of string>
                     service: <value of string>
                     service-negate: <value in [disable, enable]>
                     spamfilter-profile: <value of string>
                     srcaddr: <value of string>
                     srcaddr-negate: <value in [disable, enable]>
                     srcaddr6: <value of string>
                     srcintf: <value of string>
                     ssl-ssh-profile: <value of string>
                     status: <value in [disable, enable]>
                     tags: <value of string>
                     transparent: <value in [disable, enable]>
                     users: <value of string>
                     utm-status: <value in [disable, enable]>
                     uuid: <value of string>
                     waf-profile: <value of string>
                     webcache: <value in [disable, enable]>
                     webcache-https: <value in [disable, enable]>
                     webfilter-profile: <value of string>
                     webproxy-forward-server: <value of string>
                     webproxy-profile: <value of string>

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/PROXY-POLICY
      fmgr_pkg_firewall_proxypolicy:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [action, application-list, av-profile, ...]>
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
                  description: 'Policy ID.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/pkg/{pkg}/firewall/proxy-policy'
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
                  description: 'Accept or deny traffic matching the policy parameters.'
               application-list:
                  type: str
                  description: 'Name of an existing Application list.'
               av-profile:
                  type: str
                  description: 'Name of an existing Antivirus profile.'
               comments:
                  type: str
                  description: 'Optional comments.'
               disclaimer:
                  type: str
                  description: 'Web proxy disclaimer setting: by domain, policy, or user.'
               dlp-sensor:
                  type: str
                  description: 'Name of an existing DLP sensor.'
               dstaddr:
                  type: str
                  description: 'Destination address objects.'
               dstaddr-negate:
                  type: str
                  description: 'When enabled, destination addresses match against any address EXCEPT the specified destination addresses.'
               dstaddr6:
                  type: str
                  description: 'IPv6 destination address objects.'
               dstintf:
                  type: str
                  description: 'Destination interface names.'
               global-label:
                  type: str
                  description: 'Global web-based manager visible label.'
               groups:
                  type: str
                  description: 'Names of group objects.'
               http-tunnel-auth:
                  type: str
                  description: 'Enable/disable HTTP tunnel authentication.'
               icap-profile:
                  type: str
                  description: 'Name of an existing ICAP profile.'
               internet-service:
                  type: str
                  description: 'Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.'
               internet-service-custom:
                  type: str
                  description: 'Custom Internet Service name.'
               internet-service-id:
                  type: str
                  description: 'Internet Service ID.'
               internet-service-negate:
                  type: str
                  description: 'When enabled, Internet Services match against any internet service EXCEPT the selected Internet Service.'
               ips-sensor:
                  type: str
                  description: 'Name of an existing IPS sensor.'
               label:
                  type: str
                  description: 'VDOM-specific GUI visible label.'
               logtraffic:
                  type: str
                  description: 'Enable/disable logging traffic through the policy.'
               logtraffic-start:
                  type: str
                  description: 'Enable/disable policy log traffic start.'
               mms-profile:
                  type: str
                  description: 'Name of an existing MMS profile.'
               policyid:
                  type: int
                  description: 'Policy ID.'
               poolname:
                  type: str
                  description: 'Name of IP pool object.'
               profile-group:
                  type: str
                  description: 'Name of profile group.'
               profile-protocol-options:
                  type: str
                  description: 'Name of an existing Protocol options profile.'
               profile-type:
                  type: str
                  description: 'Determine whether the firewall policy allows security profile groups or single profiles only.'
               proxy:
                  type: str
                  description: 'Type of explicit proxy.'
               redirect-url:
                  type: str
                  description: 'Redirect URL for further explicit web proxy processing.'
               replacemsg-override-group:
                  type: str
                  description: 'Authentication replacement message override group.'
               scan-botnet-connections:
                  type: str
                  description: 'Enable/disable scanning of connections to Botnet servers.'
               schedule:
                  type: str
                  description: 'Name of schedule object.'
               service:
                  type: str
                  description: 'Name of service objects.'
               service-negate:
                  type: str
                  description: 'When enabled, services match against any service EXCEPT the specified destination services.'
               spamfilter-profile:
                  type: str
                  description: 'Name of an existing Spam filter profile.'
               srcaddr:
                  type: str
                  description: 'Source address objects (must be set when using Web proxy).'
               srcaddr-negate:
                  type: str
                  description: 'When enabled, source addresses match against any address EXCEPT the specified source addresses.'
               srcaddr6:
                  type: str
                  description: 'IPv6 source address objects.'
               srcintf:
                  type: str
                  description: 'Source interface names.'
               ssl-ssh-profile:
                  type: str
                  description: 'Name of an existing SSL SSH profile.'
               status:
                  type: str
                  description: 'Enable/disable the active status of the policy.'
               tags:
                  type: str
                  description: 'Names of object-tags applied to address. Tags need to be preconfigured in config system object-tag. Separate multiple tags w...'
               transparent:
                  type: str
                  description: 'Enable to use the IP address of the client to connect to the server.'
               users:
                  type: str
                  description: 'Names of user objects.'
               utm-status:
                  type: str
                  description: 'Enable the use of UTM profiles/sensors/lists.'
               uuid:
                  type: str
                  description: 'Universally Unique Identifier (UUID; automatically assigned but can be manually reset).'
               waf-profile:
                  type: str
                  description: 'Name of an existing Web application firewall profile.'
               webcache:
                  type: str
                  description: 'Enable/disable web caching.'
               webcache-https:
                  type: str
                  description: 'Enable/disable web caching for HTTPS (Requires deep-inspection enabled in ssl-ssh-profile).'
               webfilter-profile:
                  type: str
                  description: 'Name of an existing Web filter profile.'
               webproxy-forward-server:
                  type: str
                  description: 'Name of web proxy forward server.'
               webproxy-profile:
                  type: str
                  description: 'Name of web proxy profile.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/pkg/{pkg}/firewall/proxy-policy'

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
        '/pm/config/adom/{adom}/pkg/{pkg}/firewall/proxy-policy'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
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
                                'accept',
                                'deny',
                                'redirect'
                            ]
                        },
                        'application-list': {
                            'type': 'string'
                        },
                        'av-profile': {
                            'type': 'string'
                        },
                        'comments': {
                            'type': 'string'
                        },
                        'disclaimer': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'domain',
                                'policy',
                                'user'
                            ]
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
                        'dstaddr6': {
                            'type': 'string'
                        },
                        'dstintf': {
                            'type': 'string'
                        },
                        'global-label': {
                            'type': 'string'
                        },
                        'groups': {
                            'type': 'string'
                        },
                        'http-tunnel-auth': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'icap-profile': {
                            'type': 'string'
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
                        'proxy': {
                            'type': 'string',
                            'enum': [
                                'explicit-web',
                                'transparent-web',
                                'ftp',
                                'wanopt',
                                'ssh',
                                'ssh-tunnel'
                            ]
                        },
                        'redirect-url': {
                            'type': 'string'
                        },
                        'replacemsg-override-group': {
                            'type': 'string'
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
                        'ssl-ssh-profile': {
                            'type': 'string'
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
                        'transparent': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
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
                        'uuid': {
                            'type': 'string'
                        },
                        'waf-profile': {
                            'type': 'string'
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
                                'application-list',
                                'av-profile',
                                'comments',
                                'disclaimer',
                                'dlp-sensor',
                                'dstaddr',
                                'dstaddr-negate',
                                'dstaddr6',
                                'dstintf',
                                'global-label',
                                'groups',
                                'http-tunnel-auth',
                                'icap-profile',
                                'internet-service',
                                'internet-service-custom',
                                'internet-service-id',
                                'internet-service-negate',
                                'ips-sensor',
                                'label',
                                'logtraffic',
                                'logtraffic-start',
                                'mms-profile',
                                'policyid',
                                'poolname',
                                'profile-group',
                                'profile-protocol-options',
                                'profile-type',
                                'proxy',
                                'redirect-url',
                                'replacemsg-override-group',
                                'scan-botnet-connections',
                                'schedule',
                                'service',
                                'service-negate',
                                'spamfilter-profile',
                                'srcaddr',
                                'srcaddr-negate',
                                'srcaddr6',
                                'srcintf',
                                'ssl-ssh-profile',
                                'status',
                                'tags',
                                'transparent',
                                'users',
                                'utm-status',
                                'uuid',
                                'waf-profile',
                                'webcache',
                                'webcache-https',
                                'webfilter-profile',
                                'webproxy-forward-server',
                                'webproxy-profile'
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
