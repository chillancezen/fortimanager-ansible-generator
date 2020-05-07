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
module: fmgr_firewall_vip6_dynamicmapping_obj
short_description: no description
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/firewall/vip6/{vip6}/dynamic_mapping/{dynamic_mapping}
    - /pm/config/global/obj/firewall/vip6/{vip6}/dynamic_mapping/{dynamic_mapping}
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
            vip6:
                type: str
            dynamic_mapping:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
            data:
                _scope:
                    -
                        name:
                            type: str
                        vdom:
                            type: str
                arp-reply:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                color:
                    type: int
                comment:
                    type: str
                extip:
                    type: str
                extport:
                    type: str
                http-cookie-age:
                    type: int
                http-cookie-domain:
                    type: str
                http-cookie-domain-from-host:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                http-cookie-generation:
                    type: int
                http-cookie-path:
                    type: str
                http-cookie-share:
                    type: str
                    choices:
                        - 'disable'
                        - 'same-ip'
                http-ip-header:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                http-ip-header-name:
                    type: str
                http-multiplex:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                https-cookie-secure:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                id:
                    type: int
                ldb-method:
                    type: str
                    choices:
                        - 'static'
                        - 'round-robin'
                        - 'weighted'
                        - 'least-session'
                        - 'least-rtt'
                        - 'first-alive'
                        - 'http-host'
                mappedip:
                    type: str
                mappedport:
                    type: str
                max-embryonic-connections:
                    type: int
                monitor:
                    type: str
                outlook-web-access:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                persistence:
                    type: str
                    choices:
                        - 'none'
                        - 'http-cookie'
                        - 'ssl-session-id'
                portforward:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                protocol:
                    type: str
                    choices:
                        - 'tcp'
                        - 'udp'
                        - 'sctp'
                server-type:
                    type: str
                    choices:
                        - 'http'
                        - 'https'
                        - 'ssl'
                        - 'tcp'
                        - 'udp'
                        - 'ip'
                        - 'imaps'
                        - 'pop3s'
                        - 'smtps'
                src-filter:
                    -
                        type: str
                ssl-algorithm:
                    type: str
                    choices:
                        - 'high'
                        - 'low'
                        - 'medium'
                        - 'custom'
                ssl-certificate:
                    type: str
                ssl-client-fallback:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ssl-client-renegotiation:
                    type: str
                    choices:
                        - 'deny'
                        - 'allow'
                        - 'secure'
                ssl-client-session-state-max:
                    type: int
                ssl-client-session-state-timeout:
                    type: int
                ssl-client-session-state-type:
                    type: str
                    choices:
                        - 'disable'
                        - 'time'
                        - 'count'
                        - 'both'
                ssl-dh-bits:
                    type: str
                    choices:
                        - '768'
                        - '1024'
                        - '1536'
                        - '2048'
                        - '3072'
                        - '4096'
                ssl-hpkp:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                        - 'report-only'
                ssl-hpkp-age:
                    type: int
                ssl-hpkp-backup:
                    type: str
                ssl-hpkp-include-subdomains:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ssl-hpkp-primary:
                    type: str
                ssl-hpkp-report-uri:
                    type: str
                ssl-hsts:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ssl-hsts-age:
                    type: int
                ssl-hsts-include-subdomains:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ssl-http-location-conversion:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ssl-http-match-host:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ssl-max-version:
                    type: str
                    choices:
                        - 'ssl-3.0'
                        - 'tls-1.0'
                        - 'tls-1.1'
                        - 'tls-1.2'
                ssl-min-version:
                    type: str
                    choices:
                        - 'ssl-3.0'
                        - 'tls-1.0'
                        - 'tls-1.1'
                        - 'tls-1.2'
                ssl-mode:
                    type: str
                    choices:
                        - 'half'
                        - 'full'
                ssl-pfs:
                    type: str
                    choices:
                        - 'require'
                        - 'deny'
                        - 'allow'
                ssl-send-empty-frags:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ssl-server-algorithm:
                    type: str
                    choices:
                        - 'high'
                        - 'low'
                        - 'medium'
                        - 'custom'
                        - 'client'
                ssl-server-max-version:
                    type: str
                    choices:
                        - 'ssl-3.0'
                        - 'tls-1.0'
                        - 'tls-1.1'
                        - 'tls-1.2'
                        - 'client'
                ssl-server-min-version:
                    type: str
                    choices:
                        - 'ssl-3.0'
                        - 'tls-1.0'
                        - 'tls-1.1'
                        - 'tls-1.2'
                        - 'client'
                ssl-server-session-state-max:
                    type: int
                ssl-server-session-state-timeout:
                    type: int
                ssl-server-session-state-type:
                    type: str
                    choices:
                        - 'disable'
                        - 'time'
                        - 'count'
                        - 'both'
                type:
                    type: str
                    choices:
                        - 'static-nat'
                        - 'server-load-balance'
                uuid:
                    type: str
                weblogic-server:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                websphere-server:
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/VIP6/{VIP6}/DYNAMIC_MAPPING/{DYNAMIC_MAPPING}
      fmgr_firewall_vip6_dynamicmapping_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vip6: <value of string>
            dynamic_mapping: <value of string>
         params:
            -
               data:
                  _scope:
                    -
                        name: <value of string>
                        vdom: <value of string>
                  arp-reply: <value in [disable, enable]>
                  color: <value of integer>
                  comment: <value of string>
                  extip: <value of string>
                  extport: <value of string>
                  http-cookie-age: <value of integer>
                  http-cookie-domain: <value of string>
                  http-cookie-domain-from-host: <value in [disable, enable]>
                  http-cookie-generation: <value of integer>
                  http-cookie-path: <value of string>
                  http-cookie-share: <value in [disable, same-ip]>
                  http-ip-header: <value in [disable, enable]>
                  http-ip-header-name: <value of string>
                  http-multiplex: <value in [disable, enable]>
                  https-cookie-secure: <value in [disable, enable]>
                  id: <value of integer>
                  ldb-method: <value in [static, round-robin, weighted, ...]>
                  mappedip: <value of string>
                  mappedport: <value of string>
                  max-embryonic-connections: <value of integer>
                  monitor: <value of string>
                  outlook-web-access: <value in [disable, enable]>
                  persistence: <value in [none, http-cookie, ssl-session-id]>
                  portforward: <value in [disable, enable]>
                  protocol: <value in [tcp, udp, sctp]>
                  server-type: <value in [http, https, ssl, ...]>
                  src-filter:
                    - <value of string>
                  ssl-algorithm: <value in [high, low, medium, ...]>
                  ssl-certificate: <value of string>
                  ssl-client-fallback: <value in [disable, enable]>
                  ssl-client-renegotiation: <value in [deny, allow, secure]>
                  ssl-client-session-state-max: <value of integer>
                  ssl-client-session-state-timeout: <value of integer>
                  ssl-client-session-state-type: <value in [disable, time, count, ...]>
                  ssl-dh-bits: <value in [768, 1024, 1536, ...]>
                  ssl-hpkp: <value in [disable, enable, report-only]>
                  ssl-hpkp-age: <value of integer>
                  ssl-hpkp-backup: <value of string>
                  ssl-hpkp-include-subdomains: <value in [disable, enable]>
                  ssl-hpkp-primary: <value of string>
                  ssl-hpkp-report-uri: <value of string>
                  ssl-hsts: <value in [disable, enable]>
                  ssl-hsts-age: <value of integer>
                  ssl-hsts-include-subdomains: <value in [disable, enable]>
                  ssl-http-location-conversion: <value in [disable, enable]>
                  ssl-http-match-host: <value in [disable, enable]>
                  ssl-max-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
                  ssl-min-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
                  ssl-mode: <value in [half, full]>
                  ssl-pfs: <value in [require, deny, allow]>
                  ssl-send-empty-frags: <value in [disable, enable]>
                  ssl-server-algorithm: <value in [high, low, medium, ...]>
                  ssl-server-max-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
                  ssl-server-min-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
                  ssl-server-session-state-max: <value of integer>
                  ssl-server-session-state-timeout: <value of integer>
                  ssl-server-session-state-type: <value in [disable, time, count, ...]>
                  type: <value in [static-nat, server-load-balance]>
                  uuid: <value of string>
                  weblogic-server: <value in [disable, enable]>
                  websphere-server: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/VIP6/{VIP6}/DYNAMIC_MAPPING/{DYNAMIC_MAPPING}
      fmgr_firewall_vip6_dynamicmapping_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vip6: <value of string>
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
            example: '/pm/config/adom/{adom}/obj/firewall/vip6/{vip6}/dynamic_mapping/{dynamic_map...'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            _scope:
               type: array
               suboptions:
                  name:
                     type: str
                  vdom:
                     type: str
            arp-reply:
               type: str
            color:
               type: int
            comment:
               type: str
            extip:
               type: str
            extport:
               type: str
            http-cookie-age:
               type: int
            http-cookie-domain:
               type: str
            http-cookie-domain-from-host:
               type: str
            http-cookie-generation:
               type: int
            http-cookie-path:
               type: str
            http-cookie-share:
               type: str
            http-ip-header:
               type: str
            http-ip-header-name:
               type: str
            http-multiplex:
               type: str
            https-cookie-secure:
               type: str
            id:
               type: int
            ldb-method:
               type: str
            mappedip:
               type: str
            mappedport:
               type: str
            max-embryonic-connections:
               type: int
            monitor:
               type: str
            outlook-web-access:
               type: str
            persistence:
               type: str
            portforward:
               type: str
            protocol:
               type: str
            server-type:
               type: str
            src-filter:
               type: array
               suboptions:
                  type: str
            ssl-algorithm:
               type: str
            ssl-certificate:
               type: str
            ssl-client-fallback:
               type: str
            ssl-client-renegotiation:
               type: str
            ssl-client-session-state-max:
               type: int
            ssl-client-session-state-timeout:
               type: int
            ssl-client-session-state-type:
               type: str
            ssl-dh-bits:
               type: str
            ssl-hpkp:
               type: str
            ssl-hpkp-age:
               type: int
            ssl-hpkp-backup:
               type: str
            ssl-hpkp-include-subdomains:
               type: str
            ssl-hpkp-primary:
               type: str
            ssl-hpkp-report-uri:
               type: str
            ssl-hsts:
               type: str
            ssl-hsts-age:
               type: int
            ssl-hsts-include-subdomains:
               type: str
            ssl-http-location-conversion:
               type: str
            ssl-http-match-host:
               type: str
            ssl-max-version:
               type: str
            ssl-min-version:
               type: str
            ssl-mode:
               type: str
            ssl-pfs:
               type: str
            ssl-send-empty-frags:
               type: str
            ssl-server-algorithm:
               type: str
            ssl-server-max-version:
               type: str
            ssl-server-min-version:
               type: str
            ssl-server-session-state-max:
               type: int
            ssl-server-session-state-timeout:
               type: int
            ssl-server-session-state-type:
               type: str
            type:
               type: str
            uuid:
               type: str
            weblogic-server:
               type: str
            websphere-server:
               type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/firewall/vip6/{vip6}/dynamic_mapping/{dynamic_map...'

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
        '/pm/config/adom/{adom}/obj/firewall/vip6/{vip6}/dynamic_mapping/{dynamic_mapping}',
        '/pm/config/global/obj/firewall/vip6/{vip6}/dynamic_mapping/{dynamic_mapping}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'vip6',
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
                        'arp-reply': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'color': {
                            'type': 'integer'
                        },
                        'comment': {
                            'type': 'string'
                        },
                        'extip': {
                            'type': 'string'
                        },
                        'extport': {
                            'type': 'string'
                        },
                        'http-cookie-age': {
                            'type': 'integer'
                        },
                        'http-cookie-domain': {
                            'type': 'string'
                        },
                        'http-cookie-domain-from-host': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'http-cookie-generation': {
                            'type': 'integer'
                        },
                        'http-cookie-path': {
                            'type': 'string'
                        },
                        'http-cookie-share': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'same-ip'
                            ]
                        },
                        'http-ip-header': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'http-ip-header-name': {
                            'type': 'string'
                        },
                        'http-multiplex': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'https-cookie-secure': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'id': {
                            'type': 'integer'
                        },
                        'ldb-method': {
                            'type': 'string',
                            'enum': [
                                'static',
                                'round-robin',
                                'weighted',
                                'least-session',
                                'least-rtt',
                                'first-alive',
                                'http-host'
                            ]
                        },
                        'mappedip': {
                            'type': 'string'
                        },
                        'mappedport': {
                            'type': 'string'
                        },
                        'max-embryonic-connections': {
                            'type': 'integer'
                        },
                        'monitor': {
                            'type': 'string'
                        },
                        'outlook-web-access': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'persistence': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'http-cookie',
                                'ssl-session-id'
                            ]
                        },
                        'portforward': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'protocol': {
                            'type': 'string',
                            'enum': [
                                'tcp',
                                'udp',
                                'sctp'
                            ]
                        },
                        'server-type': {
                            'type': 'string',
                            'enum': [
                                'http',
                                'https',
                                'ssl',
                                'tcp',
                                'udp',
                                'ip',
                                'imaps',
                                'pop3s',
                                'smtps'
                            ]
                        },
                        'src-filter': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'ssl-algorithm': {
                            'type': 'string',
                            'enum': [
                                'high',
                                'low',
                                'medium',
                                'custom'
                            ]
                        },
                        'ssl-certificate': {
                            'type': 'string'
                        },
                        'ssl-client-fallback': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ssl-client-renegotiation': {
                            'type': 'string',
                            'enum': [
                                'deny',
                                'allow',
                                'secure'
                            ]
                        },
                        'ssl-client-session-state-max': {
                            'type': 'integer'
                        },
                        'ssl-client-session-state-timeout': {
                            'type': 'integer'
                        },
                        'ssl-client-session-state-type': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'time',
                                'count',
                                'both'
                            ]
                        },
                        'ssl-dh-bits': {
                            'type': 'string',
                            'enum': [
                                '768',
                                '1024',
                                '1536',
                                '2048',
                                '3072',
                                '4096'
                            ]
                        },
                        'ssl-hpkp': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable',
                                'report-only'
                            ]
                        },
                        'ssl-hpkp-age': {
                            'type': 'integer'
                        },
                        'ssl-hpkp-backup': {
                            'type': 'string'
                        },
                        'ssl-hpkp-include-subdomains': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ssl-hpkp-primary': {
                            'type': 'string'
                        },
                        'ssl-hpkp-report-uri': {
                            'type': 'string'
                        },
                        'ssl-hsts': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ssl-hsts-age': {
                            'type': 'integer'
                        },
                        'ssl-hsts-include-subdomains': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ssl-http-location-conversion': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ssl-http-match-host': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
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
                                'half',
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
                        'ssl-server-algorithm': {
                            'type': 'string',
                            'enum': [
                                'high',
                                'low',
                                'medium',
                                'custom',
                                'client'
                            ]
                        },
                        'ssl-server-max-version': {
                            'type': 'string',
                            'enum': [
                                'ssl-3.0',
                                'tls-1.0',
                                'tls-1.1',
                                'tls-1.2',
                                'client'
                            ]
                        },
                        'ssl-server-min-version': {
                            'type': 'string',
                            'enum': [
                                'ssl-3.0',
                                'tls-1.0',
                                'tls-1.1',
                                'tls-1.2',
                                'client'
                            ]
                        },
                        'ssl-server-session-state-max': {
                            'type': 'integer'
                        },
                        'ssl-server-session-state-timeout': {
                            'type': 'integer'
                        },
                        'ssl-server-session-state-type': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'time',
                                'count',
                                'both'
                            ]
                        },
                        'type': {
                            'type': 'string',
                            'enum': [
                                'static-nat',
                                'server-load-balance'
                            ]
                        },
                        'uuid': {
                            'type': 'string'
                        },
                        'weblogic-server': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'websphere-server': {
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
