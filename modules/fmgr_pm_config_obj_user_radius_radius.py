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
module: fmgr_pm_config_obj_user_radius_radius
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/user/radius/{radius}
    - /pm/config/global/obj/user/radius/{radius}
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
            radius:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Configure RADIUS server entries.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                accounting-server:
                    -
                        id:
                            type: int
                            description: 'ID (0 - 4294967295).'
                        port:
                            type: int
                            description: 'RADIUS accounting port number.'
                        secret:
                            -
                                type: str
                        server:
                            type: str
                            description: '{&lt;name_str|ip_str&gt;} Server CN domain name or IP.'
                        source-ip:
                            type: str
                            description: 'Source IP address for communications to the RADIUS server.'
                        status:
                            type: str
                            description: 'Status.'
                            choices:
                                - 'disable'
                                - 'enable'
                acct-all-servers:
                    type: str
                    description: 'Enable/disable sending of accounting messages to all configured servers (default = disable).'
                    choices:
                        - 'disable'
                        - 'enable'
                acct-interim-interval:
                    type: int
                    description: 'Time in seconds between each accounting interim update message.'
                all-usergroup:
                    type: str
                    description: 'Enable/disable automatically including this RADIUS server in all user groups.'
                    choices:
                        - 'disable'
                        - 'enable'
                auth-type:
                    type: str
                    description: 'Authentication methods/protocols permitted for this RADIUS server.'
                    choices:
                        - 'pap'
                        - 'chap'
                        - 'ms_chap'
                        - 'ms_chap_v2'
                        - 'auto'
                class:
                    -
                        type: str
                dynamic_mapping:
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
                h3c-compatibility:
                    type: str
                    description: 'Enable/disable compatibility with the H3C, a mechanism that performs security checking for authentication.'
                    choices:
                        - 'disable'
                        - 'enable'
                name:
                    type: str
                    description: 'RADIUS server entry name.'
                nas-ip:
                    type: str
                    description: 'IP address used to communicate with the RADIUS server and used as NAS-IP-Address and Called-Station-ID attributes.'
                password-encoding:
                    type: str
                    description: 'Password encoding.'
                    choices:
                        - 'ISO-8859-1'
                        - 'auto'
                password-renewal:
                    type: str
                    description: 'Enable/disable password renewal.'
                    choices:
                        - 'disable'
                        - 'enable'
                radius-coa:
                    type: str
                    description: 'Enable to allow a mechanism to change the attributes of an authentication, authorization, and accounting session after it is authenticated.'
                    choices:
                        - 'disable'
                        - 'enable'
                radius-port:
                    type: int
                    description: 'RADIUS service port number.'
                rsso:
                    type: str
                    description: 'Enable/disable RADIUS based single sign on feature.'
                    choices:
                        - 'disable'
                        - 'enable'
                rsso-context-timeout:
                    type: int
                    description: 'Time in seconds before the logged out user is removed from the "user context list" of logged on users.'
                rsso-endpoint-attribute:
                    type: str
                    description: 'RADIUS attributes used to extract the user end point identifer from the RADIUS Start record.'
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
                    description: 'RADIUS attributes used to block a user.'
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
                    description: 'Enable/disable the replacement of old IP addresses with new ones for the same endpoint on RADIUS accounting Start messages.'
                    choices:
                        - 'disable'
                        - 'enable'
                rsso-flush-ip-session:
                    type: str
                    description: 'Enable/disable flushing user IP sessions on RADIUS accounting Stop messages.'
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
                    description: 'Time interval in seconds that group event log messages will be generated for dynamic profile events.'
                rsso-radius-response:
                    type: str
                    description: 'Enable/disable sending RADIUS response packets after receiving Start and Stop records.'
                    choices:
                        - 'disable'
                        - 'enable'
                rsso-radius-server-port:
                    type: int
                    description: 'UDP port to listen on for RADIUS Start and Stop records.'
                rsso-secret:
                    -
                        type: str
                rsso-validate-request-secret:
                    type: str
                    description: 'Enable/disable validating the RADIUS request shared secret in the Start or End record.'
                    choices:
                        - 'disable'
                        - 'enable'
                secondary-secret:
                    -
                        type: str
                secondary-server:
                    type: str
                    description: '{&lt;name_str|ip_str&gt;} secondary RADIUS CN domain name or IP.'
                secret:
                    -
                        type: str
                server:
                    type: str
                    description: 'Primary RADIUS server CN domain name or IP address.'
                source-ip:
                    type: str
                    description: 'Source IP address for communications to the RADIUS server.'
                sso-attribute:
                    type: str
                    description: 'RADIUS attribute that contains the profile group name to be extracted from the RADIUS Start record.'
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
                    description: 'Key prefix for SSO group value in the SSO attribute.'
                sso-attribute-value-override:
                    type: str
                    description: 'Enable/disable override old attribute value with new value for the same endpoint.'
                    choices:
                        - 'disable'
                        - 'enable'
                tertiary-secret:
                    -
                        type: str
                tertiary-server:
                    type: str
                    description: '{&lt;name_str|ip_str&gt;} tertiary RADIUS CN domain name or IP.'
                timeout:
                    type: int
                    description: 'Time in seconds between re-sending authentication requests.'
                use-management-vdom:
                    type: str
                    description: 'Enable/disable using management VDOM to send requests.'
                    choices:
                        - 'disable'
                        - 'enable'
                username-case-sensitive:
                    type: str
                    description: 'Enable/disable case sensitive user names.'
                    choices:
                        - 'disable'
                        - 'enable'
    schema_object1:
        methods: [delete]
        description: 'Configure RADIUS server entries.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Configure RADIUS server entries.'
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
    - name: send request to /pm/config/obj/user/radius/{radius}
      fmgr_pm_config_obj_user_radius_radius:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            radius: <value of string>
         params:
            - 
               data: 
                  accounting-server: 
                   - 
                        id: <value of integer>
                        port: <value of integer>
                        secret: 
                         - <value of string>
                        server: <value of string>
                        source-ip: <value of string>
                        status: <value in [disable, enable]>
                  acct-all-servers: <value in [disable, enable]>
                  acct-interim-interval: <value of integer>
                  all-usergroup: <value in [disable, enable]>
                  auth-type: <value in [pap, chap, ms_chap, ...]>
                  class: 
                   - <value of string>
                  dynamic_mapping: 
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
                  h3c-compatibility: <value in [disable, enable]>
                  name: <value of string>
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
                  use-management-vdom: <value in [disable, enable]>
                  username-case-sensitive: <value in [disable, enable]>
    - name: send request to /pm/config/obj/user/radius/{radius}
      fmgr_pm_config_obj_user_radius_radius:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            radius: <value of string>
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
            example: /pm/config/adom/{adom}/obj/user/radius/{radius}
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            accounting-server:
               type: array
               suboptions:
                  id:
                     type: int
                     description: 'ID (0 - 4294967295).'
                  port:
                     type: int
                     description: 'RADIUS accounting port number.'
                  secret:
                     type: array
                     suboptions:
                        type: str
                  server:
                     type: str
                     description: '{&lt;name_str|ip_str&gt;} Server CN domain name or IP.'
                  source-ip:
                     type: str
                     description: 'Source IP address for communications to the RADIUS server.'
                  status:
                     type: str
                     description: 'Status.'
            acct-all-servers:
               type: str
               description: 'Enable/disable sending of accounting messages to all configured servers (default = disable).'
            acct-interim-interval:
               type: int
               description: 'Time in seconds between each accounting interim update message.'
            all-usergroup:
               type: str
               description: 'Enable/disable automatically including this RADIUS server in all user groups.'
            auth-type:
               type: str
               description: 'Authentication methods/protocols permitted for this RADIUS server.'
            class:
               type: array
               suboptions:
                  type: str
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
            h3c-compatibility:
               type: str
               description: 'Enable/disable compatibility with the H3C, a mechanism that performs security checking for authentication.'
            name:
               type: str
               description: 'RADIUS server entry name.'
            nas-ip:
               type: str
               description: 'IP address used to communicate with the RADIUS server and used as NAS-IP-Address and Called-Station-ID attributes.'
            password-encoding:
               type: str
               description: 'Password encoding.'
            password-renewal:
               type: str
               description: 'Enable/disable password renewal.'
            radius-coa:
               type: str
               description: 'Enable to allow a mechanism to change the attributes of an authentication, authorization, and accounting session after it is authenticated.'
            radius-port:
               type: int
               description: 'RADIUS service port number.'
            rsso:
               type: str
               description: 'Enable/disable RADIUS based single sign on feature.'
            rsso-context-timeout:
               type: int
               description: 'Time in seconds before the logged out user is removed from the "user context list" of logged on users.'
            rsso-endpoint-attribute:
               type: str
               description: 'RADIUS attributes used to extract the user end point identifer from the RADIUS Start record.'
            rsso-endpoint-block-attribute:
               type: str
               description: 'RADIUS attributes used to block a user.'
            rsso-ep-one-ip-only:
               type: str
               description: 'Enable/disable the replacement of old IP addresses with new ones for the same endpoint on RADIUS accounting Start messages.'
            rsso-flush-ip-session:
               type: str
               description: 'Enable/disable flushing user IP sessions on RADIUS accounting Stop messages.'
            rsso-log-flags:
               type: array
               suboptions:
                  type: str
            rsso-log-period:
               type: int
               description: 'Time interval in seconds that group event log messages will be generated for dynamic profile events.'
            rsso-radius-response:
               type: str
               description: 'Enable/disable sending RADIUS response packets after receiving Start and Stop records.'
            rsso-radius-server-port:
               type: int
               description: 'UDP port to listen on for RADIUS Start and Stop records.'
            rsso-secret:
               type: array
               suboptions:
                  type: str
            rsso-validate-request-secret:
               type: str
               description: 'Enable/disable validating the RADIUS request shared secret in the Start or End record.'
            secondary-secret:
               type: array
               suboptions:
                  type: str
            secondary-server:
               type: str
               description: '{&lt;name_str|ip_str&gt;} secondary RADIUS CN domain name or IP.'
            secret:
               type: array
               suboptions:
                  type: str
            server:
               type: str
               description: 'Primary RADIUS server CN domain name or IP address.'
            source-ip:
               type: str
               description: 'Source IP address for communications to the RADIUS server.'
            sso-attribute:
               type: str
               description: 'RADIUS attribute that contains the profile group name to be extracted from the RADIUS Start record.'
            sso-attribute-key:
               type: str
               description: 'Key prefix for SSO group value in the SSO attribute.'
            sso-attribute-value-override:
               type: str
               description: 'Enable/disable override old attribute value with new value for the same endpoint.'
            tertiary-secret:
               type: array
               suboptions:
                  type: str
            tertiary-server:
               type: str
               description: '{&lt;name_str|ip_str&gt;} tertiary RADIUS CN domain name or IP.'
            timeout:
               type: int
               description: 'Time in seconds between re-sending authentication requests.'
            use-management-vdom:
               type: str
               description: 'Enable/disable using management VDOM to send requests.'
            username-case-sensitive:
               type: str
               description: 'Enable/disable case sensitive user names.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/obj/user/radius/{radius}

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
        '/pm/config/adom/{adom}/obj/user/radius/{radius}',
        '/pm/config/global/obj/user/radius/{radius}'
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

    body_schema =  {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'accounting-server': {
                            'type': 'array',
                            'items': {
                                'id': {
                                    'type': 'integer'
                                },
                                'port': {
                                    'type': 'integer'
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
                                'status': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
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
                        'h3c-compatibility': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'name': {
                            'type': 'string'
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