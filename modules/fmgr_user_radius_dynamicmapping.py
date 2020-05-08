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
module: fmgr_user_radius_dynamicmapping
short_description: no description
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/user/radius/{radius}/dynamic_mapping
    - /pm/config/global/obj/user/radius/{radius}/dynamic_mapping
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
        description: the maximum time in seconds to wait for other user to release the workspace lock
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
            radius:
                type: str
    schema_object0:
        methods: [add, set, update]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    _scope:
                        -
                            name:
                                type: str
                            vdom:
                                type: str
                    acct-all-servers:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    acct-interim-interval:
                        type: int
                    all-usergroup:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    auth-type:
                        type: str
                        choices:
                            - 'pap'
                            - 'chap'
                            - 'ms_chap'
                            - 'ms_chap_v2'
                            - 'auto'
                    class:
                        -
                            type: str
                    dp-carrier-endpoint-attribute:
                        type: str
                        choices:
                            - 'User-Name'
                            - 'User-Password'
                            - 'CHAP-Password'
                            - 'NAS-IP-Address'
                            - 'NAS-Port'
                            - 'Service-Type'
                            - 'Framed-Protocol'
                            - 'Framed-IP-Address'
                            - 'Framed-IP-Netmask'
                            - 'Framed-Routing'
                            - 'Filter-Id'
                            - 'Framed-MTU'
                            - 'Framed-Compression'
                            - 'Login-IP-Host'
                            - 'Login-Service'
                            - 'Login-TCP-Port'
                            - 'Reply-Message'
                            - 'Callback-Number'
                            - 'Callback-Id'
                            - 'Framed-Route'
                            - 'Framed-IPX-Network'
                            - 'State'
                            - 'Class'
                            - 'Vendor-Specific'
                            - 'Session-Timeout'
                            - 'Idle-Timeout'
                            - 'Termination-Action'
                            - 'Called-Station-Id'
                            - 'Calling-Station-Id'
                            - 'NAS-Identifier'
                            - 'Proxy-State'
                            - 'Login-LAT-Service'
                            - 'Login-LAT-Node'
                            - 'Login-LAT-Group'
                            - 'Framed-AppleTalk-Link'
                            - 'Framed-AppleTalk-Network'
                            - 'Framed-AppleTalk-Zone'
                            - 'Acct-Status-Type'
                            - 'Acct-Delay-Time'
                            - 'Acct-Input-Octets'
                            - 'Acct-Output-Octets'
                            - 'Acct-Session-Id'
                            - 'Acct-Authentic'
                            - 'Acct-Session-Time'
                            - 'Acct-Input-Packets'
                            - 'Acct-Output-Packets'
                            - 'Acct-Terminate-Cause'
                            - 'Acct-Multi-Session-Id'
                            - 'Acct-Link-Count'
                            - 'CHAP-Challenge'
                            - 'NAS-Port-Type'
                            - 'Port-Limit'
                            - 'Login-LAT-Port'
                    dp-carrier-endpoint-block-attribute:
                        type: str
                        choices:
                            - 'User-Name'
                            - 'User-Password'
                            - 'CHAP-Password'
                            - 'NAS-IP-Address'
                            - 'NAS-Port'
                            - 'Service-Type'
                            - 'Framed-Protocol'
                            - 'Framed-IP-Address'
                            - 'Framed-IP-Netmask'
                            - 'Framed-Routing'
                            - 'Filter-Id'
                            - 'Framed-MTU'
                            - 'Framed-Compression'
                            - 'Login-IP-Host'
                            - 'Login-Service'
                            - 'Login-TCP-Port'
                            - 'Reply-Message'
                            - 'Callback-Number'
                            - 'Callback-Id'
                            - 'Framed-Route'
                            - 'Framed-IPX-Network'
                            - 'State'
                            - 'Class'
                            - 'Vendor-Specific'
                            - 'Session-Timeout'
                            - 'Idle-Timeout'
                            - 'Termination-Action'
                            - 'Called-Station-Id'
                            - 'Calling-Station-Id'
                            - 'NAS-Identifier'
                            - 'Proxy-State'
                            - 'Login-LAT-Service'
                            - 'Login-LAT-Node'
                            - 'Login-LAT-Group'
                            - 'Framed-AppleTalk-Link'
                            - 'Framed-AppleTalk-Network'
                            - 'Framed-AppleTalk-Zone'
                            - 'Acct-Status-Type'
                            - 'Acct-Delay-Time'
                            - 'Acct-Input-Octets'
                            - 'Acct-Output-Octets'
                            - 'Acct-Session-Id'
                            - 'Acct-Authentic'
                            - 'Acct-Session-Time'
                            - 'Acct-Input-Packets'
                            - 'Acct-Output-Packets'
                            - 'Acct-Terminate-Cause'
                            - 'Acct-Multi-Session-Id'
                            - 'Acct-Link-Count'
                            - 'CHAP-Challenge'
                            - 'NAS-Port-Type'
                            - 'Port-Limit'
                            - 'Login-LAT-Port'
                    dp-context-timeout:
                        type: int
                    dp-flush-ip-session:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    dp-hold-time:
                        type: int
                    dp-http-header:
                        type: str
                    dp-http-header-fallback:
                        type: str
                        choices:
                            - 'ip-header-address'
                            - 'default-profile'
                    dp-http-header-status:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    dp-http-header-suppress:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    dp-log-dyn_flags:
                        -
                            type: str
                            choices:
                                - 'none'
                                - 'protocol-error'
                                - 'profile-missing'
                                - 'context-missing'
                                - 'accounting-stop-missed'
                                - 'accounting-event'
                                - 'radiusd-other'
                                - 'endpoint-block'
                    dp-log-period:
                        type: int
                    dp-mem-percent:
                        type: int
                    dp-profile-attribute:
                        type: str
                        choices:
                            - 'User-Name'
                            - 'User-Password'
                            - 'CHAP-Password'
                            - 'NAS-IP-Address'
                            - 'NAS-Port'
                            - 'Service-Type'
                            - 'Framed-Protocol'
                            - 'Framed-IP-Address'
                            - 'Framed-IP-Netmask'
                            - 'Framed-Routing'
                            - 'Filter-Id'
                            - 'Framed-MTU'
                            - 'Framed-Compression'
                            - 'Login-IP-Host'
                            - 'Login-Service'
                            - 'Login-TCP-Port'
                            - 'Reply-Message'
                            - 'Callback-Number'
                            - 'Callback-Id'
                            - 'Framed-Route'
                            - 'Framed-IPX-Network'
                            - 'State'
                            - 'Class'
                            - 'Vendor-Specific'
                            - 'Session-Timeout'
                            - 'Idle-Timeout'
                            - 'Termination-Action'
                            - 'Called-Station-Id'
                            - 'Calling-Station-Id'
                            - 'NAS-Identifier'
                            - 'Proxy-State'
                            - 'Login-LAT-Service'
                            - 'Login-LAT-Node'
                            - 'Login-LAT-Group'
                            - 'Framed-AppleTalk-Link'
                            - 'Framed-AppleTalk-Network'
                            - 'Framed-AppleTalk-Zone'
                            - 'Acct-Status-Type'
                            - 'Acct-Delay-Time'
                            - 'Acct-Input-Octets'
                            - 'Acct-Output-Octets'
                            - 'Acct-Session-Id'
                            - 'Acct-Authentic'
                            - 'Acct-Session-Time'
                            - 'Acct-Input-Packets'
                            - 'Acct-Output-Packets'
                            - 'Acct-Terminate-Cause'
                            - 'Acct-Multi-Session-Id'
                            - 'Acct-Link-Count'
                            - 'CHAP-Challenge'
                            - 'NAS-Port-Type'
                            - 'Port-Limit'
                            - 'Login-LAT-Port'
                    dp-profile-attribute-key:
                        type: str
                    dp-radius-response:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    dp-radius-server-port:
                        type: int
                    dp-secret:
                        -
                            type: str
                    dp-validate-request-secret:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    dynamic-profile:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    endpoint-translation:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    ep-carrier-endpoint-convert-hex:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    ep-carrier-endpoint-header:
                        type: str
                    ep-carrier-endpoint-header-suppress:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    ep-carrier-endpoint-prefix:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    ep-carrier-endpoint-prefix-range-max:
                        type: int
                    ep-carrier-endpoint-prefix-range-min:
                        type: int
                    ep-carrier-endpoint-prefix-string:
                        type: str
                    ep-carrier-endpoint-source:
                        type: str
                        choices:
                            - 'http-header'
                            - 'cookie'
                    ep-ip-header:
                        type: str
                    ep-ip-header-suppress:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    ep-missing-header-fallback:
                        type: str
                        choices:
                            - 'session-ip'
                            - 'policy-profile'
                    ep-profile-query-type:
                        type: str
                        choices:
                            - 'session-ip'
                            - 'extract-ip'
                            - 'extract-carrier-endpoint'
                    h3c-compatibility:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    nas-ip:
                        type: str
                    password-encoding:
                        type: str
                        choices:
                            - 'ISO-8859-1'
                            - 'auto'
                    password-renewal:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    radius-coa:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    radius-port:
                        type: int
                    rsso:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    rsso-context-timeout:
                        type: int
                    rsso-endpoint-attribute:
                        type: str
                        choices:
                            - 'User-Name'
                            - 'User-Password'
                            - 'CHAP-Password'
                            - 'NAS-IP-Address'
                            - 'NAS-Port'
                            - 'Service-Type'
                            - 'Framed-Protocol'
                            - 'Framed-IP-Address'
                            - 'Framed-IP-Netmask'
                            - 'Framed-Routing'
                            - 'Filter-Id'
                            - 'Framed-MTU'
                            - 'Framed-Compression'
                            - 'Login-IP-Host'
                            - 'Login-Service'
                            - 'Login-TCP-Port'
                            - 'Reply-Message'
                            - 'Callback-Number'
                            - 'Callback-Id'
                            - 'Framed-Route'
                            - 'Framed-IPX-Network'
                            - 'State'
                            - 'Class'
                            - 'Session-Timeout'
                            - 'Idle-Timeout'
                            - 'Termination-Action'
                            - 'Called-Station-Id'
                            - 'Calling-Station-Id'
                            - 'NAS-Identifier'
                            - 'Proxy-State'
                            - 'Login-LAT-Service'
                            - 'Login-LAT-Node'
                            - 'Login-LAT-Group'
                            - 'Framed-AppleTalk-Link'
                            - 'Framed-AppleTalk-Network'
                            - 'Framed-AppleTalk-Zone'
                            - 'Acct-Status-Type'
                            - 'Acct-Delay-Time'
                            - 'Acct-Input-Octets'
                            - 'Acct-Output-Octets'
                            - 'Acct-Session-Id'
                            - 'Acct-Authentic'
                            - 'Acct-Session-Time'
                            - 'Acct-Input-Packets'
                            - 'Acct-Output-Packets'
                            - 'Acct-Terminate-Cause'
                            - 'Acct-Multi-Session-Id'
                            - 'Acct-Link-Count'
                            - 'CHAP-Challenge'
                            - 'NAS-Port-Type'
                            - 'Port-Limit'
                            - 'Login-LAT-Port'
                    rsso-endpoint-block-attribute:
                        type: str
                        choices:
                            - 'User-Name'
                            - 'User-Password'
                            - 'CHAP-Password'
                            - 'NAS-IP-Address'
                            - 'NAS-Port'
                            - 'Service-Type'
                            - 'Framed-Protocol'
                            - 'Framed-IP-Address'
                            - 'Framed-IP-Netmask'
                            - 'Framed-Routing'
                            - 'Filter-Id'
                            - 'Framed-MTU'
                            - 'Framed-Compression'
                            - 'Login-IP-Host'
                            - 'Login-Service'
                            - 'Login-TCP-Port'
                            - 'Reply-Message'
                            - 'Callback-Number'
                            - 'Callback-Id'
                            - 'Framed-Route'
                            - 'Framed-IPX-Network'
                            - 'State'
                            - 'Class'
                            - 'Session-Timeout'
                            - 'Idle-Timeout'
                            - 'Termination-Action'
                            - 'Called-Station-Id'
                            - 'Calling-Station-Id'
                            - 'NAS-Identifier'
                            - 'Proxy-State'
                            - 'Login-LAT-Service'
                            - 'Login-LAT-Node'
                            - 'Login-LAT-Group'
                            - 'Framed-AppleTalk-Link'
                            - 'Framed-AppleTalk-Network'
                            - 'Framed-AppleTalk-Zone'
                            - 'Acct-Status-Type'
                            - 'Acct-Delay-Time'
                            - 'Acct-Input-Octets'
                            - 'Acct-Output-Octets'
                            - 'Acct-Session-Id'
                            - 'Acct-Authentic'
                            - 'Acct-Session-Time'
                            - 'Acct-Input-Packets'
                            - 'Acct-Output-Packets'
                            - 'Acct-Terminate-Cause'
                            - 'Acct-Multi-Session-Id'
                            - 'Acct-Link-Count'
                            - 'CHAP-Challenge'
                            - 'NAS-Port-Type'
                            - 'Port-Limit'
                            - 'Login-LAT-Port'
                    rsso-ep-one-ip-only:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    rsso-flush-ip-session:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    rsso-log-flags:
                        -
                            type: str
                            choices:
                                - 'none'
                                - 'protocol-error'
                                - 'profile-missing'
                                - 'context-missing'
                                - 'accounting-stop-missed'
                                - 'accounting-event'
                                - 'radiusd-other'
                                - 'endpoint-block'
                    rsso-log-period:
                        type: int
                    rsso-radius-response:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    rsso-radius-server-port:
                        type: int
                    rsso-secret:
                        -
                            type: str
                    rsso-validate-request-secret:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    secondary-secret:
                        -
                            type: str
                    secondary-server:
                        type: str
                    secret:
                        -
                            type: str
                    server:
                        type: str
                    source-ip:
                        type: str
                    sso-attribute:
                        type: str
                        choices:
                            - 'User-Name'
                            - 'User-Password'
                            - 'CHAP-Password'
                            - 'NAS-IP-Address'
                            - 'NAS-Port'
                            - 'Service-Type'
                            - 'Framed-Protocol'
                            - 'Framed-IP-Address'
                            - 'Framed-IP-Netmask'
                            - 'Framed-Routing'
                            - 'Filter-Id'
                            - 'Framed-MTU'
                            - 'Framed-Compression'
                            - 'Login-IP-Host'
                            - 'Login-Service'
                            - 'Login-TCP-Port'
                            - 'Reply-Message'
                            - 'Callback-Number'
                            - 'Callback-Id'
                            - 'Framed-Route'
                            - 'Framed-IPX-Network'
                            - 'State'
                            - 'Class'
                            - 'Session-Timeout'
                            - 'Idle-Timeout'
                            - 'Termination-Action'
                            - 'Called-Station-Id'
                            - 'Calling-Station-Id'
                            - 'NAS-Identifier'
                            - 'Proxy-State'
                            - 'Login-LAT-Service'
                            - 'Login-LAT-Node'
                            - 'Login-LAT-Group'
                            - 'Framed-AppleTalk-Link'
                            - 'Framed-AppleTalk-Network'
                            - 'Framed-AppleTalk-Zone'
                            - 'Acct-Status-Type'
                            - 'Acct-Delay-Time'
                            - 'Acct-Input-Octets'
                            - 'Acct-Output-Octets'
                            - 'Acct-Session-Id'
                            - 'Acct-Authentic'
                            - 'Acct-Session-Time'
                            - 'Acct-Input-Packets'
                            - 'Acct-Output-Packets'
                            - 'Acct-Terminate-Cause'
                            - 'Acct-Multi-Session-Id'
                            - 'Acct-Link-Count'
                            - 'CHAP-Challenge'
                            - 'NAS-Port-Type'
                            - 'Port-Limit'
                            - 'Login-LAT-Port'
                    sso-attribute-key:
                        type: str
                    sso-attribute-value-override:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    tertiary-secret:
                        -
                            type: str
                    tertiary-server:
                        type: str
                    timeout:
                        type: int
                    use-group-for-profile:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    use-management-vdom:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    username-case-sensitive:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
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
                            - '_scope'
                            - 'acct-all-servers'
                            - 'acct-interim-interval'
                            - 'all-usergroup'
                            - 'auth-type'
                            - 'class'
                            - 'dp-carrier-endpoint-attribute'
                            - 'dp-carrier-endpoint-block-attribute'
                            - 'dp-context-timeout'
                            - 'dp-flush-ip-session'
                            - 'dp-hold-time'
                            - 'dp-http-header'
                            - 'dp-http-header-fallback'
                            - 'dp-http-header-status'
                            - 'dp-http-header-suppress'
                            - 'dp-log-dyn_flags'
                            - 'dp-log-period'
                            - 'dp-mem-percent'
                            - 'dp-profile-attribute'
                            - 'dp-profile-attribute-key'
                            - 'dp-radius-response'
                            - 'dp-radius-server-port'
                            - 'dp-secret'
                            - 'dp-validate-request-secret'
                            - 'dynamic-profile'
                            - 'endpoint-translation'
                            - 'ep-carrier-endpoint-convert-hex'
                            - 'ep-carrier-endpoint-header'
                            - 'ep-carrier-endpoint-header-suppress'
                            - 'ep-carrier-endpoint-prefix'
                            - 'ep-carrier-endpoint-prefix-range-max'
                            - 'ep-carrier-endpoint-prefix-range-min'
                            - 'ep-carrier-endpoint-prefix-string'
                            - 'ep-carrier-endpoint-source'
                            - 'ep-ip-header'
                            - 'ep-ip-header-suppress'
                            - 'ep-missing-header-fallback'
                            - 'ep-profile-query-type'
                            - 'h3c-compatibility'
                            - 'nas-ip'
                            - 'password-encoding'
                            - 'password-renewal'
                            - 'radius-coa'
                            - 'radius-port'
                            - 'rsso'
                            - 'rsso-context-timeout'
                            - 'rsso-endpoint-attribute'
                            - 'rsso-endpoint-block-attribute'
                            - 'rsso-ep-one-ip-only'
                            - 'rsso-flush-ip-session'
                            - 'rsso-log-flags'
                            - 'rsso-log-period'
                            - 'rsso-radius-response'
                            - 'rsso-radius-server-port'
                            - 'rsso-secret'
                            - 'rsso-validate-request-secret'
                            - 'secondary-secret'
                            - 'secondary-server'
                            - 'secret'
                            - 'server'
                            - 'source-ip'
                            - 'sso-attribute'
                            - 'sso-attribute-key'
                            - 'sso-attribute-value-override'
                            - 'tertiary-secret'
                            - 'tertiary-server'
                            - 'timeout'
                            - 'use-group-for-profile'
                            - 'use-management-vdom'
                            - 'username-case-sensitive'
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

    - name: REQUESTING /PM/CONFIG/OBJ/USER/RADIUS/{RADIUS}/DYNAMIC_MAPPING
      fmgr_user_radius_dynamicmapping:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            radius: <value of string>
         params:
            -
               data:
                 -
                     _scope:
                       -
                           name: <value of string>
                           vdom: <value of string>
                     acct-all-servers: <value in [disable, enable]>
                     acct-interim-interval: <value of integer>
                     all-usergroup: <value in [disable, enable]>
                     auth-type: <value in [pap, chap, ms_chap, ...]>
                     class:
                       - <value of string>
                     dp-carrier-endpoint-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
                     dp-carrier-endpoint-block-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
                     dp-context-timeout: <value of integer>
                     dp-flush-ip-session: <value in [disable, enable]>
                     dp-hold-time: <value of integer>
                     dp-http-header: <value of string>
                     dp-http-header-fallback: <value in [ip-header-address, default-profile]>
                     dp-http-header-status: <value in [disable, enable]>
                     dp-http-header-suppress: <value in [disable, enable]>
                     dp-log-dyn_flags:
                       - <value in [none, protocol-error, profile-missing, ...]>
                     dp-log-period: <value of integer>
                     dp-mem-percent: <value of integer>
                     dp-profile-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
                     dp-profile-attribute-key: <value of string>
                     dp-radius-response: <value in [disable, enable]>
                     dp-radius-server-port: <value of integer>
                     dp-secret:
                       - <value of string>
                     dp-validate-request-secret: <value in [disable, enable]>
                     dynamic-profile: <value in [disable, enable]>
                     endpoint-translation: <value in [disable, enable]>
                     ep-carrier-endpoint-convert-hex: <value in [disable, enable]>
                     ep-carrier-endpoint-header: <value of string>
                     ep-carrier-endpoint-header-suppress: <value in [disable, enable]>
                     ep-carrier-endpoint-prefix: <value in [disable, enable]>
                     ep-carrier-endpoint-prefix-range-max: <value of integer>
                     ep-carrier-endpoint-prefix-range-min: <value of integer>
                     ep-carrier-endpoint-prefix-string: <value of string>
                     ep-carrier-endpoint-source: <value in [http-header, cookie]>
                     ep-ip-header: <value of string>
                     ep-ip-header-suppress: <value in [disable, enable]>
                     ep-missing-header-fallback: <value in [session-ip, policy-profile]>
                     ep-profile-query-type: <value in [session-ip, extract-ip, extract-carrier-endpoint]>
                     h3c-compatibility: <value in [disable, enable]>
                     nas-ip: <value of string>
                     password-encoding: <value in [ISO-8859-1, auto]>
                     password-renewal: <value in [disable, enable]>
                     radius-coa: <value in [disable, enable]>
                     radius-port: <value of integer>
                     rsso: <value in [disable, enable]>
                     rsso-context-timeout: <value of integer>
                     rsso-endpoint-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
                     rsso-endpoint-block-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
                     rsso-ep-one-ip-only: <value in [disable, enable]>
                     rsso-flush-ip-session: <value in [disable, enable]>
                     rsso-log-flags:
                       - <value in [none, protocol-error, profile-missing, ...]>
                     rsso-log-period: <value of integer>
                     rsso-radius-response: <value in [disable, enable]>
                     rsso-radius-server-port: <value of integer>
                     rsso-secret:
                       - <value of string>
                     rsso-validate-request-secret: <value in [disable, enable]>
                     secondary-secret:
                       - <value of string>
                     secondary-server: <value of string>
                     secret:
                       - <value of string>
                     server: <value of string>
                     source-ip: <value of string>
                     sso-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
                     sso-attribute-key: <value of string>
                     sso-attribute-value-override: <value in [disable, enable]>
                     tertiary-secret:
                       - <value of string>
                     tertiary-server: <value of string>
                     timeout: <value of integer>
                     use-group-for-profile: <value in [disable, enable]>
                     use-management-vdom: <value in [disable, enable]>
                     username-case-sensitive: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/USER/RADIUS/{RADIUS}/DYNAMIC_MAPPING
      fmgr_user_radius_dynamicmapping:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            radius: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [_scope, acct-all-servers, acct-interim-interval, ...]>
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
            example: '/pm/config/adom/{adom}/obj/user/radius/{radius}/dynamic_mapping'
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
               _scope:
                  type: array
                  suboptions:
                     name:
                        type: str
                     vdom:
                        type: str
               acct-all-servers:
                  type: str
               acct-interim-interval:
                  type: int
               all-usergroup:
                  type: str
               auth-type:
                  type: str
               class:
                  type: array
                  suboptions:
                     type: str
               dp-carrier-endpoint-attribute:
                  type: str
               dp-carrier-endpoint-block-attribute:
                  type: str
               dp-context-timeout:
                  type: int
               dp-flush-ip-session:
                  type: str
               dp-hold-time:
                  type: int
               dp-http-header:
                  type: str
               dp-http-header-fallback:
                  type: str
               dp-http-header-status:
                  type: str
               dp-http-header-suppress:
                  type: str
               dp-log-dyn_flags:
                  type: array
                  suboptions:
                     type: str
               dp-log-period:
                  type: int
               dp-mem-percent:
                  type: int
               dp-profile-attribute:
                  type: str
               dp-profile-attribute-key:
                  type: str
               dp-radius-response:
                  type: str
               dp-radius-server-port:
                  type: int
               dp-secret:
                  type: array
                  suboptions:
                     type: str
               dp-validate-request-secret:
                  type: str
               dynamic-profile:
                  type: str
               endpoint-translation:
                  type: str
               ep-carrier-endpoint-convert-hex:
                  type: str
               ep-carrier-endpoint-header:
                  type: str
               ep-carrier-endpoint-header-suppress:
                  type: str
               ep-carrier-endpoint-prefix:
                  type: str
               ep-carrier-endpoint-prefix-range-max:
                  type: int
               ep-carrier-endpoint-prefix-range-min:
                  type: int
               ep-carrier-endpoint-prefix-string:
                  type: str
               ep-carrier-endpoint-source:
                  type: str
               ep-ip-header:
                  type: str
               ep-ip-header-suppress:
                  type: str
               ep-missing-header-fallback:
                  type: str
               ep-profile-query-type:
                  type: str
               h3c-compatibility:
                  type: str
               nas-ip:
                  type: str
               password-encoding:
                  type: str
               password-renewal:
                  type: str
               radius-coa:
                  type: str
               radius-port:
                  type: int
               rsso:
                  type: str
               rsso-context-timeout:
                  type: int
               rsso-endpoint-attribute:
                  type: str
               rsso-endpoint-block-attribute:
                  type: str
               rsso-ep-one-ip-only:
                  type: str
               rsso-flush-ip-session:
                  type: str
               rsso-log-flags:
                  type: array
                  suboptions:
                     type: str
               rsso-log-period:
                  type: int
               rsso-radius-response:
                  type: str
               rsso-radius-server-port:
                  type: int
               rsso-secret:
                  type: array
                  suboptions:
                     type: str
               rsso-validate-request-secret:
                  type: str
               secondary-secret:
                  type: array
                  suboptions:
                     type: str
               secondary-server:
                  type: str
               secret:
                  type: array
                  suboptions:
                     type: str
               server:
                  type: str
               source-ip:
                  type: str
               sso-attribute:
                  type: str
               sso-attribute-key:
                  type: str
               sso-attribute-value-override:
                  type: str
               tertiary-secret:
                  type: array
                  suboptions:
                     type: str
               tertiary-server:
                  type: str
               timeout:
                  type: int
               use-group-for-profile:
                  type: str
               use-management-vdom:
                  type: str
               username-case-sensitive:
                  type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/user/radius/{radius}/dynamic_mapping'

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
        '/pm/config/adom/{adom}/obj/user/radius/{radius}/dynamic_mapping',
        '/pm/config/global/obj/user/radius/{radius}/dynamic_mapping'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'radius',
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
                        'acct-all-servers': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'acct-interim-interval': {
                            'type': 'integer'
                        },
                        'all-usergroup': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'auth-type': {
                            'type': 'string',
                            'enum': [
                                'pap',
                                'chap',
                                'ms_chap',
                                'ms_chap_v2',
                                'auto'
                            ]
                        },
                        'class': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'dp-carrier-endpoint-attribute': {
                            'type': 'string',
                            'enum': [
                                'User-Name',
                                'User-Password',
                                'CHAP-Password',
                                'NAS-IP-Address',
                                'NAS-Port',
                                'Service-Type',
                                'Framed-Protocol',
                                'Framed-IP-Address',
                                'Framed-IP-Netmask',
                                'Framed-Routing',
                                'Filter-Id',
                                'Framed-MTU',
                                'Framed-Compression',
                                'Login-IP-Host',
                                'Login-Service',
                                'Login-TCP-Port',
                                'Reply-Message',
                                'Callback-Number',
                                'Callback-Id',
                                'Framed-Route',
                                'Framed-IPX-Network',
                                'State',
                                'Class',
                                'Vendor-Specific',
                                'Session-Timeout',
                                'Idle-Timeout',
                                'Termination-Action',
                                'Called-Station-Id',
                                'Calling-Station-Id',
                                'NAS-Identifier',
                                'Proxy-State',
                                'Login-LAT-Service',
                                'Login-LAT-Node',
                                'Login-LAT-Group',
                                'Framed-AppleTalk-Link',
                                'Framed-AppleTalk-Network',
                                'Framed-AppleTalk-Zone',
                                'Acct-Status-Type',
                                'Acct-Delay-Time',
                                'Acct-Input-Octets',
                                'Acct-Output-Octets',
                                'Acct-Session-Id',
                                'Acct-Authentic',
                                'Acct-Session-Time',
                                'Acct-Input-Packets',
                                'Acct-Output-Packets',
                                'Acct-Terminate-Cause',
                                'Acct-Multi-Session-Id',
                                'Acct-Link-Count',
                                'CHAP-Challenge',
                                'NAS-Port-Type',
                                'Port-Limit',
                                'Login-LAT-Port'
                            ]
                        },
                        'dp-carrier-endpoint-block-attribute': {
                            'type': 'string',
                            'enum': [
                                'User-Name',
                                'User-Password',
                                'CHAP-Password',
                                'NAS-IP-Address',
                                'NAS-Port',
                                'Service-Type',
                                'Framed-Protocol',
                                'Framed-IP-Address',
                                'Framed-IP-Netmask',
                                'Framed-Routing',
                                'Filter-Id',
                                'Framed-MTU',
                                'Framed-Compression',
                                'Login-IP-Host',
                                'Login-Service',
                                'Login-TCP-Port',
                                'Reply-Message',
                                'Callback-Number',
                                'Callback-Id',
                                'Framed-Route',
                                'Framed-IPX-Network',
                                'State',
                                'Class',
                                'Vendor-Specific',
                                'Session-Timeout',
                                'Idle-Timeout',
                                'Termination-Action',
                                'Called-Station-Id',
                                'Calling-Station-Id',
                                'NAS-Identifier',
                                'Proxy-State',
                                'Login-LAT-Service',
                                'Login-LAT-Node',
                                'Login-LAT-Group',
                                'Framed-AppleTalk-Link',
                                'Framed-AppleTalk-Network',
                                'Framed-AppleTalk-Zone',
                                'Acct-Status-Type',
                                'Acct-Delay-Time',
                                'Acct-Input-Octets',
                                'Acct-Output-Octets',
                                'Acct-Session-Id',
                                'Acct-Authentic',
                                'Acct-Session-Time',
                                'Acct-Input-Packets',
                                'Acct-Output-Packets',
                                'Acct-Terminate-Cause',
                                'Acct-Multi-Session-Id',
                                'Acct-Link-Count',
                                'CHAP-Challenge',
                                'NAS-Port-Type',
                                'Port-Limit',
                                'Login-LAT-Port'
                            ]
                        },
                        'dp-context-timeout': {
                            'type': 'integer'
                        },
                        'dp-flush-ip-session': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dp-hold-time': {
                            'type': 'integer'
                        },
                        'dp-http-header': {
                            'type': 'string'
                        },
                        'dp-http-header-fallback': {
                            'type': 'string',
                            'enum': [
                                'ip-header-address',
                                'default-profile'
                            ]
                        },
                        'dp-http-header-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dp-http-header-suppress': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dp-log-dyn_flags': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'none',
                                    'protocol-error',
                                    'profile-missing',
                                    'context-missing',
                                    'accounting-stop-missed',
                                    'accounting-event',
                                    'radiusd-other',
                                    'endpoint-block'
                                ]
                            }
                        },
                        'dp-log-period': {
                            'type': 'integer'
                        },
                        'dp-mem-percent': {
                            'type': 'integer'
                        },
                        'dp-profile-attribute': {
                            'type': 'string',
                            'enum': [
                                'User-Name',
                                'User-Password',
                                'CHAP-Password',
                                'NAS-IP-Address',
                                'NAS-Port',
                                'Service-Type',
                                'Framed-Protocol',
                                'Framed-IP-Address',
                                'Framed-IP-Netmask',
                                'Framed-Routing',
                                'Filter-Id',
                                'Framed-MTU',
                                'Framed-Compression',
                                'Login-IP-Host',
                                'Login-Service',
                                'Login-TCP-Port',
                                'Reply-Message',
                                'Callback-Number',
                                'Callback-Id',
                                'Framed-Route',
                                'Framed-IPX-Network',
                                'State',
                                'Class',
                                'Vendor-Specific',
                                'Session-Timeout',
                                'Idle-Timeout',
                                'Termination-Action',
                                'Called-Station-Id',
                                'Calling-Station-Id',
                                'NAS-Identifier',
                                'Proxy-State',
                                'Login-LAT-Service',
                                'Login-LAT-Node',
                                'Login-LAT-Group',
                                'Framed-AppleTalk-Link',
                                'Framed-AppleTalk-Network',
                                'Framed-AppleTalk-Zone',
                                'Acct-Status-Type',
                                'Acct-Delay-Time',
                                'Acct-Input-Octets',
                                'Acct-Output-Octets',
                                'Acct-Session-Id',
                                'Acct-Authentic',
                                'Acct-Session-Time',
                                'Acct-Input-Packets',
                                'Acct-Output-Packets',
                                'Acct-Terminate-Cause',
                                'Acct-Multi-Session-Id',
                                'Acct-Link-Count',
                                'CHAP-Challenge',
                                'NAS-Port-Type',
                                'Port-Limit',
                                'Login-LAT-Port'
                            ]
                        },
                        'dp-profile-attribute-key': {
                            'type': 'string'
                        },
                        'dp-radius-response': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dp-radius-server-port': {
                            'type': 'integer'
                        },
                        'dp-secret': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'dp-validate-request-secret': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dynamic-profile': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'endpoint-translation': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ep-carrier-endpoint-convert-hex': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ep-carrier-endpoint-header': {
                            'type': 'string'
                        },
                        'ep-carrier-endpoint-header-suppress': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ep-carrier-endpoint-prefix': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ep-carrier-endpoint-prefix-range-max': {
                            'type': 'integer'
                        },
                        'ep-carrier-endpoint-prefix-range-min': {
                            'type': 'integer'
                        },
                        'ep-carrier-endpoint-prefix-string': {
                            'type': 'string'
                        },
                        'ep-carrier-endpoint-source': {
                            'type': 'string',
                            'enum': [
                                'http-header',
                                'cookie'
                            ]
                        },
                        'ep-ip-header': {
                            'type': 'string'
                        },
                        'ep-ip-header-suppress': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ep-missing-header-fallback': {
                            'type': 'string',
                            'enum': [
                                'session-ip',
                                'policy-profile'
                            ]
                        },
                        'ep-profile-query-type': {
                            'type': 'string',
                            'enum': [
                                'session-ip',
                                'extract-ip',
                                'extract-carrier-endpoint'
                            ]
                        },
                        'h3c-compatibility': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'nas-ip': {
                            'type': 'string'
                        },
                        'password-encoding': {
                            'type': 'string',
                            'enum': [
                                'ISO-8859-1',
                                'auto'
                            ]
                        },
                        'password-renewal': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'radius-coa': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'radius-port': {
                            'type': 'integer'
                        },
                        'rsso': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'rsso-context-timeout': {
                            'type': 'integer'
                        },
                        'rsso-endpoint-attribute': {
                            'type': 'string',
                            'enum': [
                                'User-Name',
                                'User-Password',
                                'CHAP-Password',
                                'NAS-IP-Address',
                                'NAS-Port',
                                'Service-Type',
                                'Framed-Protocol',
                                'Framed-IP-Address',
                                'Framed-IP-Netmask',
                                'Framed-Routing',
                                'Filter-Id',
                                'Framed-MTU',
                                'Framed-Compression',
                                'Login-IP-Host',
                                'Login-Service',
                                'Login-TCP-Port',
                                'Reply-Message',
                                'Callback-Number',
                                'Callback-Id',
                                'Framed-Route',
                                'Framed-IPX-Network',
                                'State',
                                'Class',
                                'Session-Timeout',
                                'Idle-Timeout',
                                'Termination-Action',
                                'Called-Station-Id',
                                'Calling-Station-Id',
                                'NAS-Identifier',
                                'Proxy-State',
                                'Login-LAT-Service',
                                'Login-LAT-Node',
                                'Login-LAT-Group',
                                'Framed-AppleTalk-Link',
                                'Framed-AppleTalk-Network',
                                'Framed-AppleTalk-Zone',
                                'Acct-Status-Type',
                                'Acct-Delay-Time',
                                'Acct-Input-Octets',
                                'Acct-Output-Octets',
                                'Acct-Session-Id',
                                'Acct-Authentic',
                                'Acct-Session-Time',
                                'Acct-Input-Packets',
                                'Acct-Output-Packets',
                                'Acct-Terminate-Cause',
                                'Acct-Multi-Session-Id',
                                'Acct-Link-Count',
                                'CHAP-Challenge',
                                'NAS-Port-Type',
                                'Port-Limit',
                                'Login-LAT-Port'
                            ]
                        },
                        'rsso-endpoint-block-attribute': {
                            'type': 'string',
                            'enum': [
                                'User-Name',
                                'User-Password',
                                'CHAP-Password',
                                'NAS-IP-Address',
                                'NAS-Port',
                                'Service-Type',
                                'Framed-Protocol',
                                'Framed-IP-Address',
                                'Framed-IP-Netmask',
                                'Framed-Routing',
                                'Filter-Id',
                                'Framed-MTU',
                                'Framed-Compression',
                                'Login-IP-Host',
                                'Login-Service',
                                'Login-TCP-Port',
                                'Reply-Message',
                                'Callback-Number',
                                'Callback-Id',
                                'Framed-Route',
                                'Framed-IPX-Network',
                                'State',
                                'Class',
                                'Session-Timeout',
                                'Idle-Timeout',
                                'Termination-Action',
                                'Called-Station-Id',
                                'Calling-Station-Id',
                                'NAS-Identifier',
                                'Proxy-State',
                                'Login-LAT-Service',
                                'Login-LAT-Node',
                                'Login-LAT-Group',
                                'Framed-AppleTalk-Link',
                                'Framed-AppleTalk-Network',
                                'Framed-AppleTalk-Zone',
                                'Acct-Status-Type',
                                'Acct-Delay-Time',
                                'Acct-Input-Octets',
                                'Acct-Output-Octets',
                                'Acct-Session-Id',
                                'Acct-Authentic',
                                'Acct-Session-Time',
                                'Acct-Input-Packets',
                                'Acct-Output-Packets',
                                'Acct-Terminate-Cause',
                                'Acct-Multi-Session-Id',
                                'Acct-Link-Count',
                                'CHAP-Challenge',
                                'NAS-Port-Type',
                                'Port-Limit',
                                'Login-LAT-Port'
                            ]
                        },
                        'rsso-ep-one-ip-only': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'rsso-flush-ip-session': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'rsso-log-flags': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'none',
                                    'protocol-error',
                                    'profile-missing',
                                    'context-missing',
                                    'accounting-stop-missed',
                                    'accounting-event',
                                    'radiusd-other',
                                    'endpoint-block'
                                ]
                            }
                        },
                        'rsso-log-period': {
                            'type': 'integer'
                        },
                        'rsso-radius-response': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'rsso-radius-server-port': {
                            'type': 'integer'
                        },
                        'rsso-secret': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'rsso-validate-request-secret': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'secondary-secret': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'secondary-server': {
                            'type': 'string'
                        },
                        'secret': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'server': {
                            'type': 'string'
                        },
                        'source-ip': {
                            'type': 'string'
                        },
                        'sso-attribute': {
                            'type': 'string',
                            'enum': [
                                'User-Name',
                                'User-Password',
                                'CHAP-Password',
                                'NAS-IP-Address',
                                'NAS-Port',
                                'Service-Type',
                                'Framed-Protocol',
                                'Framed-IP-Address',
                                'Framed-IP-Netmask',
                                'Framed-Routing',
                                'Filter-Id',
                                'Framed-MTU',
                                'Framed-Compression',
                                'Login-IP-Host',
                                'Login-Service',
                                'Login-TCP-Port',
                                'Reply-Message',
                                'Callback-Number',
                                'Callback-Id',
                                'Framed-Route',
                                'Framed-IPX-Network',
                                'State',
                                'Class',
                                'Session-Timeout',
                                'Idle-Timeout',
                                'Termination-Action',
                                'Called-Station-Id',
                                'Calling-Station-Id',
                                'NAS-Identifier',
                                'Proxy-State',
                                'Login-LAT-Service',
                                'Login-LAT-Node',
                                'Login-LAT-Group',
                                'Framed-AppleTalk-Link',
                                'Framed-AppleTalk-Network',
                                'Framed-AppleTalk-Zone',
                                'Acct-Status-Type',
                                'Acct-Delay-Time',
                                'Acct-Input-Octets',
                                'Acct-Output-Octets',
                                'Acct-Session-Id',
                                'Acct-Authentic',
                                'Acct-Session-Time',
                                'Acct-Input-Packets',
                                'Acct-Output-Packets',
                                'Acct-Terminate-Cause',
                                'Acct-Multi-Session-Id',
                                'Acct-Link-Count',
                                'CHAP-Challenge',
                                'NAS-Port-Type',
                                'Port-Limit',
                                'Login-LAT-Port'
                            ]
                        },
                        'sso-attribute-key': {
                            'type': 'string'
                        },
                        'sso-attribute-value-override': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'tertiary-secret': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'tertiary-server': {
                            'type': 'string'
                        },
                        'timeout': {
                            'type': 'integer'
                        },
                        'use-group-for-profile': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'use-management-vdom': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'username-case-sensitive': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
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
                                '_scope',
                                'acct-all-servers',
                                'acct-interim-interval',
                                'all-usergroup',
                                'auth-type',
                                'class',
                                'dp-carrier-endpoint-attribute',
                                'dp-carrier-endpoint-block-attribute',
                                'dp-context-timeout',
                                'dp-flush-ip-session',
                                'dp-hold-time',
                                'dp-http-header',
                                'dp-http-header-fallback',
                                'dp-http-header-status',
                                'dp-http-header-suppress',
                                'dp-log-dyn_flags',
                                'dp-log-period',
                                'dp-mem-percent',
                                'dp-profile-attribute',
                                'dp-profile-attribute-key',
                                'dp-radius-response',
                                'dp-radius-server-port',
                                'dp-secret',
                                'dp-validate-request-secret',
                                'dynamic-profile',
                                'endpoint-translation',
                                'ep-carrier-endpoint-convert-hex',
                                'ep-carrier-endpoint-header',
                                'ep-carrier-endpoint-header-suppress',
                                'ep-carrier-endpoint-prefix',
                                'ep-carrier-endpoint-prefix-range-max',
                                'ep-carrier-endpoint-prefix-range-min',
                                'ep-carrier-endpoint-prefix-string',
                                'ep-carrier-endpoint-source',
                                'ep-ip-header',
                                'ep-ip-header-suppress',
                                'ep-missing-header-fallback',
                                'ep-profile-query-type',
                                'h3c-compatibility',
                                'nas-ip',
                                'password-encoding',
                                'password-renewal',
                                'radius-coa',
                                'radius-port',
                                'rsso',
                                'rsso-context-timeout',
                                'rsso-endpoint-attribute',
                                'rsso-endpoint-block-attribute',
                                'rsso-ep-one-ip-only',
                                'rsso-flush-ip-session',
                                'rsso-log-flags',
                                'rsso-log-period',
                                'rsso-radius-response',
                                'rsso-radius-server-port',
                                'rsso-secret',
                                'rsso-validate-request-secret',
                                'secondary-secret',
                                'secondary-server',
                                'secret',
                                'server',
                                'source-ip',
                                'sso-attribute',
                                'sso-attribute-key',
                                'sso-attribute-value-override',
                                'tertiary-secret',
                                'tertiary-server',
                                'timeout',
                                'use-group-for-profile',
                                'use-management-vdom',
                                'username-case-sensitive'
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
        if loose_validation is False:
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
