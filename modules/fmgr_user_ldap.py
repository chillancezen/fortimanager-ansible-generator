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
module: fmgr_user_ldap
short_description: Configure LDAP server entries.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/user/ldap
    - /pm/config/global/obj/user/ldap
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
        methods: [add, set, update]
        description: 'Configure LDAP server entries.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    account-key-filter:
                        type: str
                        description: 'Account key filter, using the UPN as the search filter.'
                    account-key-processing:
                        type: str
                        description: 'Account key processing operation, either keep or strip domain string of UPN in the token.'
                        choices:
                            - 'same'
                            - 'strip'
                    ca-cert:
                        type: str
                        description: 'CA certificate name.'
                    cnid:
                        type: str
                        description: 'Common name identifier for the LDAP server. The common name identifier for most LDAP servers is "cn".'
                    dn:
                        type: str
                        description: 'Distinguished name used to look up entries on the LDAP server.'
                    dynamic_mapping:
                        -
                            _scope:
                                -
                                    name:
                                        type: str
                                    vdom:
                                        type: str
                            account-key-filter:
                                type: str
                            account-key-name:
                                type: str
                            account-key-processing:
                                type: str
                                choices:
                                    - 'same'
                                    - 'strip'
                            ca-cert:
                                type: str
                            cnid:
                                type: str
                            dn:
                                type: str
                            filter:
                                type: str
                            group:
                                type: str
                            group-filter:
                                type: str
                            group-member-check:
                                type: str
                                choices:
                                    - 'user-attr'
                                    - 'group-object'
                                    - 'posix-group-object'
                            group-object-filter:
                                type: str
                            group-object-search-base:
                                type: str
                            group-search-base:
                                type: str
                            member-attr:
                                type: str
                            obtain-user-info:
                                type: str
                                choices:
                                    - 'disable'
                                    - 'enable'
                            password:
                                -
                                    type: str
                            password-expiry-warning:
                                type: str
                                choices:
                                    - 'disable'
                                    - 'enable'
                            password-renewal:
                                type: str
                                choices:
                                    - 'disable'
                                    - 'enable'
                            port:
                                type: int
                            retrieve-protection-profile:
                                type: str
                            search-type:
                                -
                                    type: str
                                    choices:
                                        - 'nested'
                                        - 'recursive'
                            secondary-server:
                                type: str
                            secure:
                                type: str
                                choices:
                                    - 'disable'
                                    - 'starttls'
                                    - 'ldaps'
                            server:
                                type: str
                            server-identity-check:
                                type: str
                                choices:
                                    - 'disable'
                                    - 'enable'
                            source-ip:
                                type: str
                            ssl-min-proto-version:
                                type: str
                                choices:
                                    - 'default'
                                    - 'TLSv1'
                                    - 'TLSv1-1'
                                    - 'TLSv1-2'
                                    - 'SSLv3'
                            tertiary-server:
                                type: str
                            type:
                                type: str
                                choices:
                                    - 'simple'
                                    - 'anonymous'
                                    - 'regular'
                            user-info-exchange-server:
                                type: str
                            username:
                                type: str
                    group-filter:
                        type: str
                        description: 'Filter used for group matching.'
                    group-member-check:
                        type: str
                        description: 'Group member checking methods.'
                        choices:
                            - 'user-attr'
                            - 'group-object'
                            - 'posix-group-object'
                    group-object-filter:
                        type: str
                        description: 'Filter used for group searching.'
                    group-search-base:
                        type: str
                        description: 'Search base used for group searching.'
                    member-attr:
                        type: str
                        description: 'Name of attribute from which to get group membership.'
                    name:
                        type: str
                        description: 'LDAP server entry name.'
                    password:
                        -
                            type: str
                    password-expiry-warning:
                        type: str
                        description: 'Enable/disable password expiry warnings.'
                        choices:
                            - 'disable'
                            - 'enable'
                    password-renewal:
                        type: str
                        description: 'Enable/disable online password renewal.'
                        choices:
                            - 'disable'
                            - 'enable'
                    port:
                        type: int
                        description: 'Port to be used for communication with the LDAP server (default = 389).'
                    secondary-server:
                        type: str
                        description: 'Secondary LDAP server CN domain name or IP.'
                    secure:
                        type: str
                        description: 'Port to be used for authentication.'
                        choices:
                            - 'disable'
                            - 'starttls'
                            - 'ldaps'
                    server:
                        type: str
                        description: 'LDAP server CN domain name or IP.'
                    server-identity-check:
                        type: str
                        description: 'Enable/disable LDAP server identity check (verify server domain name/IP address against the server certificate).'
                        choices:
                            - 'disable'
                            - 'enable'
                    source-ip:
                        type: str
                        description: 'Source IP for communications to LDAP server.'
                    ssl-min-proto-version:
                        type: str
                        description: 'Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).'
                        choices:
                            - 'default'
                            - 'TLSv1'
                            - 'TLSv1-1'
                            - 'TLSv1-2'
                            - 'SSLv3'
                    tertiary-server:
                        type: str
                        description: 'Tertiary LDAP server CN domain name or IP.'
                    type:
                        type: str
                        description: 'Authentication type for LDAP searches.'
                        choices:
                            - 'simple'
                            - 'anonymous'
                            - 'regular'
                    username:
                        type: str
                        description: 'Username (full DN) for initial binding.'
    schema_object1:
        methods: [get]
        description: 'Configure LDAP server entries.'
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
                            - 'account-key-filter'
                            - 'account-key-processing'
                            - 'ca-cert'
                            - 'cnid'
                            - 'dn'
                            - 'group-filter'
                            - 'group-member-check'
                            - 'group-object-filter'
                            - 'group-search-base'
                            - 'member-attr'
                            - 'name'
                            - 'password'
                            - 'password-expiry-warning'
                            - 'password-renewal'
                            - 'port'
                            - 'secondary-server'
                            - 'secure'
                            - 'server'
                            - 'server-identity-check'
                            - 'source-ip'
                            - 'ssl-min-proto-version'
                            - 'tertiary-server'
                            - 'type'
                            - 'username'
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

    - name: REQUESTING /PM/CONFIG/OBJ/USER/LDAP
      fmgr_user_ldap:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     account-key-filter: <value of string>
                     account-key-processing: <value in [same, strip]>
                     ca-cert: <value of string>
                     cnid: <value of string>
                     dn: <value of string>
                     dynamic_mapping:
                       -
                           _scope:
                             -
                                 name: <value of string>
                                 vdom: <value of string>
                           account-key-filter: <value of string>
                           account-key-name: <value of string>
                           account-key-processing: <value in [same, strip]>
                           ca-cert: <value of string>
                           cnid: <value of string>
                           dn: <value of string>
                           filter: <value of string>
                           group: <value of string>
                           group-filter: <value of string>
                           group-member-check: <value in [user-attr, group-object, posix-group-object]>
                           group-object-filter: <value of string>
                           group-object-search-base: <value of string>
                           group-search-base: <value of string>
                           member-attr: <value of string>
                           obtain-user-info: <value in [disable, enable]>
                           password:
                             - <value of string>
                           password-expiry-warning: <value in [disable, enable]>
                           password-renewal: <value in [disable, enable]>
                           port: <value of integer>
                           retrieve-protection-profile: <value of string>
                           search-type:
                             - <value in [nested, recursive]>
                           secondary-server: <value of string>
                           secure: <value in [disable, starttls, ldaps]>
                           server: <value of string>
                           server-identity-check: <value in [disable, enable]>
                           source-ip: <value of string>
                           ssl-min-proto-version: <value in [default, TLSv1, TLSv1-1, ...]>
                           tertiary-server: <value of string>
                           type: <value in [simple, anonymous, regular]>
                           user-info-exchange-server: <value of string>
                           username: <value of string>
                     group-filter: <value of string>
                     group-member-check: <value in [user-attr, group-object, posix-group-object]>
                     group-object-filter: <value of string>
                     group-search-base: <value of string>
                     member-attr: <value of string>
                     name: <value of string>
                     password:
                       - <value of string>
                     password-expiry-warning: <value in [disable, enable]>
                     password-renewal: <value in [disable, enable]>
                     port: <value of integer>
                     secondary-server: <value of string>
                     secure: <value in [disable, starttls, ldaps]>
                     server: <value of string>
                     server-identity-check: <value in [disable, enable]>
                     source-ip: <value of string>
                     ssl-min-proto-version: <value in [default, TLSv1, TLSv1-1, ...]>
                     tertiary-server: <value of string>
                     type: <value in [simple, anonymous, regular]>
                     username: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/USER/LDAP
      fmgr_user_ldap:
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
                    - <value in [account-key-filter, account-key-processing, ca-cert, ...]>
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
            example: '/pm/config/adom/{adom}/obj/user/ldap'
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
               account-key-filter:
                  type: str
                  description: 'Account key filter, using the UPN as the search filter.'
               account-key-processing:
                  type: str
                  description: 'Account key processing operation, either keep or strip domain string of UPN in the token.'
               ca-cert:
                  type: str
                  description: 'CA certificate name.'
               cnid:
                  type: str
                  description: 'Common name identifier for the LDAP server. The common name identifier for most LDAP servers is "cn".'
               dn:
                  type: str
                  description: 'Distinguished name used to look up entries on the LDAP server.'
               dynamic_mapping:
                  type: array
                  suboptions:
                     _scope:
                        type: array
                        suboptions:
                           name:
                              type: str
                           vdom:
                              type: str
                     account-key-filter:
                        type: str
                     account-key-name:
                        type: str
                     account-key-processing:
                        type: str
                     ca-cert:
                        type: str
                     cnid:
                        type: str
                     dn:
                        type: str
                     filter:
                        type: str
                     group:
                        type: str
                     group-filter:
                        type: str
                     group-member-check:
                        type: str
                     group-object-filter:
                        type: str
                     group-object-search-base:
                        type: str
                     group-search-base:
                        type: str
                     member-attr:
                        type: str
                     obtain-user-info:
                        type: str
                     password:
                        type: array
                        suboptions:
                           type: str
                     password-expiry-warning:
                        type: str
                     password-renewal:
                        type: str
                     port:
                        type: int
                     retrieve-protection-profile:
                        type: str
                     search-type:
                        type: array
                        suboptions:
                           type: str
                     secondary-server:
                        type: str
                     secure:
                        type: str
                     server:
                        type: str
                     server-identity-check:
                        type: str
                     source-ip:
                        type: str
                     ssl-min-proto-version:
                        type: str
                     tertiary-server:
                        type: str
                     type:
                        type: str
                     user-info-exchange-server:
                        type: str
                     username:
                        type: str
               group-filter:
                  type: str
                  description: 'Filter used for group matching.'
               group-member-check:
                  type: str
                  description: 'Group member checking methods.'
               group-object-filter:
                  type: str
                  description: 'Filter used for group searching.'
               group-search-base:
                  type: str
                  description: 'Search base used for group searching.'
               member-attr:
                  type: str
                  description: 'Name of attribute from which to get group membership.'
               name:
                  type: str
                  description: 'LDAP server entry name.'
               password:
                  type: array
                  suboptions:
                     type: str
               password-expiry-warning:
                  type: str
                  description: 'Enable/disable password expiry warnings.'
               password-renewal:
                  type: str
                  description: 'Enable/disable online password renewal.'
               port:
                  type: int
                  description: 'Port to be used for communication with the LDAP server (default = 389).'
               secondary-server:
                  type: str
                  description: 'Secondary LDAP server CN domain name or IP.'
               secure:
                  type: str
                  description: 'Port to be used for authentication.'
               server:
                  type: str
                  description: 'LDAP server CN domain name or IP.'
               server-identity-check:
                  type: str
                  description: 'Enable/disable LDAP server identity check (verify server domain name/IP address against the server certificate).'
               source-ip:
                  type: str
                  description: 'Source IP for communications to LDAP server.'
               ssl-min-proto-version:
                  type: str
                  description: 'Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).'
               tertiary-server:
                  type: str
                  description: 'Tertiary LDAP server CN domain name or IP.'
               type:
                  type: str
                  description: 'Authentication type for LDAP searches.'
               username:
                  type: str
                  description: 'Username (full DN) for initial binding.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/user/ldap'

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
        '/pm/config/adom/{adom}/obj/user/ldap',
        '/pm/config/global/obj/user/ldap'
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
                        'account-key-filter': {
                            'type': 'string'
                        },
                        'account-key-processing': {
                            'type': 'string',
                            'enum': [
                                'same',
                                'strip'
                            ]
                        },
                        'ca-cert': {
                            'type': 'string'
                        },
                        'cnid': {
                            'type': 'string'
                        },
                        'dn': {
                            'type': 'string'
                        },
                        'dynamic_mapping': {
                            'type': 'array',
                            'items': {
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
                                'account-key-filter': {
                                    'type': 'string'
                                },
                                'account-key-name': {
                                    'type': 'string'
                                },
                                'account-key-processing': {
                                    'type': 'string',
                                    'enum': [
                                        'same',
                                        'strip'
                                    ]
                                },
                                'ca-cert': {
                                    'type': 'string'
                                },
                                'cnid': {
                                    'type': 'string'
                                },
                                'dn': {
                                    'type': 'string'
                                },
                                'filter': {
                                    'type': 'string'
                                },
                                'group': {
                                    'type': 'string'
                                },
                                'group-filter': {
                                    'type': 'string'
                                },
                                'group-member-check': {
                                    'type': 'string',
                                    'enum': [
                                        'user-attr',
                                        'group-object',
                                        'posix-group-object'
                                    ]
                                },
                                'group-object-filter': {
                                    'type': 'string'
                                },
                                'group-object-search-base': {
                                    'type': 'string'
                                },
                                'group-search-base': {
                                    'type': 'string'
                                },
                                'member-attr': {
                                    'type': 'string'
                                },
                                'obtain-user-info': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'password': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                },
                                'password-expiry-warning': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'password-renewal': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'port': {
                                    'type': 'integer'
                                },
                                'retrieve-protection-profile': {
                                    'type': 'string'
                                },
                                'search-type': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string',
                                        'enum': [
                                            'nested',
                                            'recursive'
                                        ]
                                    }
                                },
                                'secondary-server': {
                                    'type': 'string'
                                },
                                'secure': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'starttls',
                                        'ldaps'
                                    ]
                                },
                                'server': {
                                    'type': 'string'
                                },
                                'server-identity-check': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'source-ip': {
                                    'type': 'string'
                                },
                                'ssl-min-proto-version': {
                                    'type': 'string',
                                    'enum': [
                                        'default',
                                        'TLSv1',
                                        'TLSv1-1',
                                        'TLSv1-2',
                                        'SSLv3'
                                    ]
                                },
                                'tertiary-server': {
                                    'type': 'string'
                                },
                                'type': {
                                    'type': 'string',
                                    'enum': [
                                        'simple',
                                        'anonymous',
                                        'regular'
                                    ]
                                },
                                'user-info-exchange-server': {
                                    'type': 'string'
                                },
                                'username': {
                                    'type': 'string'
                                }
                            }
                        },
                        'group-filter': {
                            'type': 'string'
                        },
                        'group-member-check': {
                            'type': 'string',
                            'enum': [
                                'user-attr',
                                'group-object',
                                'posix-group-object'
                            ]
                        },
                        'group-object-filter': {
                            'type': 'string'
                        },
                        'group-search-base': {
                            'type': 'string'
                        },
                        'member-attr': {
                            'type': 'string'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'password': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'password-expiry-warning': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'password-renewal': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'port': {
                            'type': 'integer'
                        },
                        'secondary-server': {
                            'type': 'string'
                        },
                        'secure': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'starttls',
                                'ldaps'
                            ]
                        },
                        'server': {
                            'type': 'string'
                        },
                        'server-identity-check': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'source-ip': {
                            'type': 'string'
                        },
                        'ssl-min-proto-version': {
                            'type': 'string',
                            'enum': [
                                'default',
                                'TLSv1',
                                'TLSv1-1',
                                'TLSv1-2',
                                'SSLv3'
                            ]
                        },
                        'tertiary-server': {
                            'type': 'string'
                        },
                        'type': {
                            'type': 'string',
                            'enum': [
                                'simple',
                                'anonymous',
                                'regular'
                            ]
                        },
                        'username': {
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
                                'account-key-filter',
                                'account-key-processing',
                                'ca-cert',
                                'cnid',
                                'dn',
                                'group-filter',
                                'group-member-check',
                                'group-object-filter',
                                'group-search-base',
                                'member-attr',
                                'name',
                                'password',
                                'password-expiry-warning',
                                'password-renewal',
                                'port',
                                'secondary-server',
                                'secure',
                                'server',
                                'server-identity-check',
                                'source-ip',
                                'ssl-min-proto-version',
                                'tertiary-server',
                                'type',
                                'username'
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
