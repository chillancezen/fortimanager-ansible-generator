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
module: fmgr_vpnsslweb_portal
short_description: Portal.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/vpn/ssl/web/portal
    - /pm/config/global/obj/vpn/ssl/web/portal
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
        description: 'Portal.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    allow-user-access:
                        -
                            type: str
                            choices:
                                - 'web'
                                - 'ftp'
                                - 'telnet'
                                - 'smb'
                                - 'vnc'
                                - 'rdp'
                                - 'ssh'
                                - 'ping'
                                - 'citrix'
                                - 'portforward'
                                - 'sftp'
                    auto-connect:
                        type: str
                        description: 'Enable/disable automatic connect by client when system is up.'
                        choices:
                            - 'disable'
                            - 'enable'
                    bookmark-group:
                        -
                            bookmarks:
                                -
                                    additional-params:
                                        type: str
                                        description: 'Additional parameters.'
                                    apptype:
                                        type: str
                                        description: 'Application type.'
                                        choices:
                                            - 'web'
                                            - 'telnet'
                                            - 'ssh'
                                            - 'ftp'
                                            - 'smb'
                                            - 'vnc'
                                            - 'rdp'
                                            - 'citrix'
                                            - 'rdpnative'
                                            - 'portforward'
                                            - 'sftp'
                                    description:
                                        type: str
                                        description: 'Description.'
                                    folder:
                                        type: str
                                        description: 'Network shared file folder parameter.'
                                    form-data:
                                        -
                                            name:
                                                type: str
                                                description: 'Name.'
                                            value:
                                                type: str
                                                description: 'Value.'
                                    host:
                                        type: str
                                        description: 'Host name/IP parameter.'
                                    listening-port:
                                        type: int
                                        description: 'Listening port (0 - 65535).'
                                    load-balancing-info:
                                        type: str
                                        description: 'The load balancing information or cookie which should be provided to the connection broker.'
                                    logon-password:
                                        -
                                            type: str
                                    logon-user:
                                        type: str
                                        description: 'Logon user.'
                                    name:
                                        type: str
                                        description: 'Bookmark name.'
                                    port:
                                        type: int
                                        description: 'Remote port.'
                                    preconnection-blob:
                                        type: str
                                        description: 'An arbitrary string which identifies the RDP source.'
                                    preconnection-id:
                                        type: int
                                        description: 'The numeric ID of the RDP source (0-2147483648).'
                                    remote-port:
                                        type: int
                                        description: 'Remote port (0 - 65535).'
                                    security:
                                        type: str
                                        description: 'Security mode for RDP connection.'
                                        choices:
                                            - 'rdp'
                                            - 'nla'
                                            - 'tls'
                                            - 'any'
                                    server-layout:
                                        type: str
                                        description: 'Server side keyboard layout.'
                                        choices:
                                            - 'en-us-qwerty'
                                            - 'de-de-qwertz'
                                            - 'fr-fr-azerty'
                                            - 'it-it-qwerty'
                                            - 'sv-se-qwerty'
                                            - 'failsafe'
                                            - 'en-gb-qwerty'
                                            - 'es-es-qwerty'
                                            - 'fr-ch-qwertz'
                                            - 'ja-jp-qwerty'
                                            - 'pt-br-qwerty'
                                            - 'tr-tr-qwerty'
                                    show-status-window:
                                        type: str
                                        description: 'Enable/disable showing of status window.'
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    sso:
                                        type: str
                                        description: 'Single Sign-On.'
                                        choices:
                                            - 'disable'
                                            - 'static'
                                            - 'auto'
                                    sso-credential:
                                        type: str
                                        description: 'Single sign-on credentials.'
                                        choices:
                                            - 'sslvpn-login'
                                            - 'alternative'
                                    sso-credential-sent-once:
                                        type: str
                                        description: 'Single sign-on credentials are only sent once to remote server.'
                                        choices:
                                            - 'disable'
                                            - 'enable'
                                    sso-password:
                                        -
                                            type: str
                                    sso-username:
                                        type: str
                                        description: 'SSO user name.'
                                    url:
                                        type: str
                                        description: 'URL parameter.'
                            name:
                                type: str
                                description: 'Bookmark group name.'
                    custom-lang:
                        type: str
                        description: 'Change the web portal display language. Overrides config system global set language. You can use config system custom-...'
                    customize-forticlient-download-url:
                        type: str
                        description: 'Enable support of customized download URL for FortiClient.'
                        choices:
                            - 'disable'
                            - 'enable'
                    display-bookmark:
                        type: str
                        description: 'Enable to display the web portal bookmark widget.'
                        choices:
                            - 'disable'
                            - 'enable'
                    display-connection-tools:
                        type: str
                        description: 'Enable to display the web portal connection tools widget.'
                        choices:
                            - 'disable'
                            - 'enable'
                    display-history:
                        type: str
                        description: 'Enable to display the web portal user login history widget.'
                        choices:
                            - 'disable'
                            - 'enable'
                    display-status:
                        type: str
                        description: 'Enable to display the web portal status widget.'
                        choices:
                            - 'disable'
                            - 'enable'
                    dns-server1:
                        type: str
                        description: 'IPv4 DNS server 1.'
                    dns-server2:
                        type: str
                        description: 'IPv4 DNS server 2.'
                    dns-suffix:
                        type: str
                        description: 'DNS suffix.'
                    exclusive-routing:
                        type: str
                        description: 'Enable/disable all traffic go through tunnel only.'
                        choices:
                            - 'disable'
                            - 'enable'
                    forticlient-download:
                        type: str
                        description: 'Enable/disable download option for FortiClient.'
                        choices:
                            - 'disable'
                            - 'enable'
                    forticlient-download-method:
                        type: str
                        description: 'FortiClient download method.'
                        choices:
                            - 'direct'
                            - 'ssl-vpn'
                    heading:
                        type: str
                        description: 'Web portal heading message.'
                    hide-sso-credential:
                        type: str
                        description: 'Enable to prevent SSO credential being sent to client.'
                        choices:
                            - 'disable'
                            - 'enable'
                    host-check:
                        type: str
                        description: 'Type of host checking performed on endpoints.'
                        choices:
                            - 'none'
                            - 'av'
                            - 'fw'
                            - 'av-fw'
                            - 'custom'
                    host-check-interval:
                        type: int
                        description: 'Periodic host check interval. Value of 0 means disabled and host checking only happens when the endpoint connects.'
                    host-check-policy:
                        type: str
                        description: 'One or more policies to require the endpoint to have specific security software.'
                    ip-mode:
                        type: str
                        description: 'Method by which users of this SSL-VPN tunnel obtain IP addresses.'
                        choices:
                            - 'range'
                            - 'user-group'
                    ip-pools:
                        type: str
                        description: 'IPv4 firewall source address objects reserved for SSL-VPN tunnel mode clients.'
                    ipv6-dns-server1:
                        type: str
                        description: 'IPv6 DNS server 1.'
                    ipv6-dns-server2:
                        type: str
                        description: 'IPv6 DNS server 2.'
                    ipv6-exclusive-routing:
                        type: str
                        description: 'Enable/disable all IPv6 traffic go through tunnel only.'
                        choices:
                            - 'disable'
                            - 'enable'
                    ipv6-pools:
                        type: str
                        description: 'IPv4 firewall source address objects reserved for SSL-VPN tunnel mode clients.'
                    ipv6-service-restriction:
                        type: str
                        description: 'Enable/disable IPv6 tunnel service restriction.'
                        choices:
                            - 'disable'
                            - 'enable'
                    ipv6-split-tunneling:
                        type: str
                        description: 'Enable/disable IPv6 split tunneling.'
                        choices:
                            - 'disable'
                            - 'enable'
                    ipv6-split-tunneling-routing-address:
                        type: str
                        description: 'IPv6 SSL-VPN tunnel mode firewall address objects that override firewall policy destination addresses to control split...'
                    ipv6-tunnel-mode:
                        type: str
                        description: 'Enable/disable IPv6 SSL-VPN tunnel mode.'
                        choices:
                            - 'disable'
                            - 'enable'
                    ipv6-wins-server1:
                        type: str
                        description: 'IPv6 WINS server 1.'
                    ipv6-wins-server2:
                        type: str
                        description: 'IPv6 WINS server 2.'
                    keep-alive:
                        type: str
                        description: 'Enable/disable automatic reconnect for FortiClient connections.'
                        choices:
                            - 'disable'
                            - 'enable'
                    limit-user-logins:
                        type: str
                        description: 'Enable to limit each user to one SSL-VPN session at a time.'
                        choices:
                            - 'disable'
                            - 'enable'
                    mac-addr-action:
                        type: str
                        description: 'Client MAC address action.'
                        choices:
                            - 'deny'
                            - 'allow'
                    mac-addr-check:
                        type: str
                        description: 'Enable/disable MAC address host checking.'
                        choices:
                            - 'disable'
                            - 'enable'
                    mac-addr-check-rule:
                        -
                            mac-addr-list:
                                -
                                    type: str
                            mac-addr-mask:
                                type: int
                                description: 'Client MAC address mask.'
                            name:
                                type: str
                                description: 'Client MAC address check rule name.'
                    macos-forticlient-download-url:
                        type: str
                        description: 'Download URL for Mac FortiClient.'
                    name:
                        type: str
                        description: 'Portal name.'
                    os-check:
                        type: str
                        description: 'Enable to let the FortiGate decide action based on client OS.'
                        choices:
                            - 'disable'
                            - 'enable'
                    redir-url:
                        type: str
                        description: 'Client login redirect URL.'
                    save-password:
                        type: str
                        description: 'Enable/disable FortiClient saving the users password.'
                        choices:
                            - 'disable'
                            - 'enable'
                    service-restriction:
                        type: str
                        description: 'Enable/disable tunnel service restriction.'
                        choices:
                            - 'disable'
                            - 'enable'
                    skip-check-for-unsupported-browser:
                        type: str
                        description: 'Enable to skip host check if browser does not support it.'
                        choices:
                            - 'disable'
                            - 'enable'
                    skip-check-for-unsupported-os:
                        type: str
                        description: 'Enable to skip host check if client OS does not support it.'
                        choices:
                            - 'disable'
                            - 'enable'
                    smb-ntlmv1-auth:
                        type: str
                        description: 'Enable support of NTLMv1 for Samba authentication.'
                        choices:
                            - 'disable'
                            - 'enable'
                    smbv1:
                        type: str
                        description: 'Enable/disable support of SMBv1 for Samba.'
                        choices:
                            - 'disable'
                            - 'enable'
                    split-dns:
                        -
                            dns-server1:
                                type: str
                                description: 'DNS server 1.'
                            dns-server2:
                                type: str
                                description: 'DNS server 2.'
                            domains:
                                type: str
                                description: 'Split DNS domains used for SSL-VPN clients separated by comma(,).'
                            id:
                                type: int
                                description: 'ID.'
                            ipv6-dns-server1:
                                type: str
                                description: 'IPv6 DNS server 1.'
                            ipv6-dns-server2:
                                type: str
                                description: 'IPv6 DNS server 2.'
                    split-tunneling:
                        type: str
                        description: 'Enable/disable IPv4 split tunneling.'
                        choices:
                            - 'disable'
                            - 'enable'
                    split-tunneling-routing-address:
                        type: str
                        description: 'IPv4 SSL-VPN tunnel mode firewall address objects that override firewall policy destination addresses to control split...'
                    theme:
                        type: str
                        description: 'Web portal color scheme.'
                        choices:
                            - 'gray'
                            - 'blue'
                            - 'orange'
                            - 'crimson'
                            - 'steelblue'
                            - 'darkgrey'
                            - 'green'
                            - 'melongene'
                            - 'red'
                            - 'mariner'
                    tunnel-mode:
                        type: str
                        description: 'Enable/disable IPv4 SSL-VPN tunnel mode.'
                        choices:
                            - 'disable'
                            - 'enable'
                    user-bookmark:
                        type: str
                        description: 'Enable to allow web portal users to create their own bookmarks.'
                        choices:
                            - 'disable'
                            - 'enable'
                    user-group-bookmark:
                        type: str
                        description: 'Enable to allow web portal users to create bookmarks for all users in the same user group.'
                        choices:
                            - 'disable'
                            - 'enable'
                    web-mode:
                        type: str
                        description: 'Enable/disable SSL VPN web mode.'
                        choices:
                            - 'disable'
                            - 'enable'
                    windows-forticlient-download-url:
                        type: str
                        description: 'Download URL for Windows FortiClient.'
                    wins-server1:
                        type: str
                        description: 'IPv4 WINS server 1.'
                    wins-server2:
                        type: str
                        description: 'IPv4 WINS server 1.'
    schema_object1:
        methods: [get]
        description: 'Portal.'
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
                            - 'allow-user-access'
                            - 'auto-connect'
                            - 'custom-lang'
                            - 'customize-forticlient-download-url'
                            - 'display-bookmark'
                            - 'display-connection-tools'
                            - 'display-history'
                            - 'display-status'
                            - 'dns-server1'
                            - 'dns-server2'
                            - 'dns-suffix'
                            - 'exclusive-routing'
                            - 'forticlient-download'
                            - 'forticlient-download-method'
                            - 'heading'
                            - 'hide-sso-credential'
                            - 'host-check'
                            - 'host-check-interval'
                            - 'host-check-policy'
                            - 'ip-mode'
                            - 'ip-pools'
                            - 'ipv6-dns-server1'
                            - 'ipv6-dns-server2'
                            - 'ipv6-exclusive-routing'
                            - 'ipv6-pools'
                            - 'ipv6-service-restriction'
                            - 'ipv6-split-tunneling'
                            - 'ipv6-split-tunneling-routing-address'
                            - 'ipv6-tunnel-mode'
                            - 'ipv6-wins-server1'
                            - 'ipv6-wins-server2'
                            - 'keep-alive'
                            - 'limit-user-logins'
                            - 'mac-addr-action'
                            - 'mac-addr-check'
                            - 'macos-forticlient-download-url'
                            - 'name'
                            - 'os-check'
                            - 'redir-url'
                            - 'save-password'
                            - 'service-restriction'
                            - 'skip-check-for-unsupported-browser'
                            - 'skip-check-for-unsupported-os'
                            - 'smb-ntlmv1-auth'
                            - 'smbv1'
                            - 'split-tunneling'
                            - 'split-tunneling-routing-address'
                            - 'theme'
                            - 'tunnel-mode'
                            - 'user-bookmark'
                            - 'user-group-bookmark'
                            - 'web-mode'
                            - 'windows-forticlient-download-url'
                            - 'wins-server1'
                            - 'wins-server2'
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

    - name: REQUESTING /PM/CONFIG/OBJ/VPN/SSL/WEB/PORTAL
      fmgr_vpnsslweb_portal:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     allow-user-access:
                       - <value in [web, ftp, telnet, ...]>
                     auto-connect: <value in [disable, enable]>
                     bookmark-group:
                       -
                           bookmarks:
                             -
                                 additional-params: <value of string>
                                 apptype: <value in [web, telnet, ssh, ...]>
                                 description: <value of string>
                                 folder: <value of string>
                                 form-data:
                                   -
                                       name: <value of string>
                                       value: <value of string>
                                 host: <value of string>
                                 listening-port: <value of integer>
                                 load-balancing-info: <value of string>
                                 logon-password:
                                   - <value of string>
                                 logon-user: <value of string>
                                 name: <value of string>
                                 port: <value of integer>
                                 preconnection-blob: <value of string>
                                 preconnection-id: <value of integer>
                                 remote-port: <value of integer>
                                 security: <value in [rdp, nla, tls, ...]>
                                 server-layout: <value in [en-us-qwerty, de-de-qwertz, fr-fr-azerty, ...]>
                                 show-status-window: <value in [disable, enable]>
                                 sso: <value in [disable, static, auto]>
                                 sso-credential: <value in [sslvpn-login, alternative]>
                                 sso-credential-sent-once: <value in [disable, enable]>
                                 sso-password:
                                   - <value of string>
                                 sso-username: <value of string>
                                 url: <value of string>
                           name: <value of string>
                     custom-lang: <value of string>
                     customize-forticlient-download-url: <value in [disable, enable]>
                     display-bookmark: <value in [disable, enable]>
                     display-connection-tools: <value in [disable, enable]>
                     display-history: <value in [disable, enable]>
                     display-status: <value in [disable, enable]>
                     dns-server1: <value of string>
                     dns-server2: <value of string>
                     dns-suffix: <value of string>
                     exclusive-routing: <value in [disable, enable]>
                     forticlient-download: <value in [disable, enable]>
                     forticlient-download-method: <value in [direct, ssl-vpn]>
                     heading: <value of string>
                     hide-sso-credential: <value in [disable, enable]>
                     host-check: <value in [none, av, fw, ...]>
                     host-check-interval: <value of integer>
                     host-check-policy: <value of string>
                     ip-mode: <value in [range, user-group]>
                     ip-pools: <value of string>
                     ipv6-dns-server1: <value of string>
                     ipv6-dns-server2: <value of string>
                     ipv6-exclusive-routing: <value in [disable, enable]>
                     ipv6-pools: <value of string>
                     ipv6-service-restriction: <value in [disable, enable]>
                     ipv6-split-tunneling: <value in [disable, enable]>
                     ipv6-split-tunneling-routing-address: <value of string>
                     ipv6-tunnel-mode: <value in [disable, enable]>
                     ipv6-wins-server1: <value of string>
                     ipv6-wins-server2: <value of string>
                     keep-alive: <value in [disable, enable]>
                     limit-user-logins: <value in [disable, enable]>
                     mac-addr-action: <value in [deny, allow]>
                     mac-addr-check: <value in [disable, enable]>
                     mac-addr-check-rule:
                       -
                           mac-addr-list:
                             - <value of string>
                           mac-addr-mask: <value of integer>
                           name: <value of string>
                     macos-forticlient-download-url: <value of string>
                     name: <value of string>
                     os-check: <value in [disable, enable]>
                     redir-url: <value of string>
                     save-password: <value in [disable, enable]>
                     service-restriction: <value in [disable, enable]>
                     skip-check-for-unsupported-browser: <value in [disable, enable]>
                     skip-check-for-unsupported-os: <value in [disable, enable]>
                     smb-ntlmv1-auth: <value in [disable, enable]>
                     smbv1: <value in [disable, enable]>
                     split-dns:
                       -
                           dns-server1: <value of string>
                           dns-server2: <value of string>
                           domains: <value of string>
                           id: <value of integer>
                           ipv6-dns-server1: <value of string>
                           ipv6-dns-server2: <value of string>
                     split-tunneling: <value in [disable, enable]>
                     split-tunneling-routing-address: <value of string>
                     theme: <value in [gray, blue, orange, ...]>
                     tunnel-mode: <value in [disable, enable]>
                     user-bookmark: <value in [disable, enable]>
                     user-group-bookmark: <value in [disable, enable]>
                     web-mode: <value in [disable, enable]>
                     windows-forticlient-download-url: <value of string>
                     wins-server1: <value of string>
                     wins-server2: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/VPN/SSL/WEB/PORTAL
      fmgr_vpnsslweb_portal:
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
                    - <value in [allow-user-access, auto-connect, custom-lang, ...]>
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
            example: '/pm/config/adom/{adom}/obj/vpn/ssl/web/portal'
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
               allow-user-access:
                  type: array
                  suboptions:
                     type: str
               auto-connect:
                  type: str
                  description: 'Enable/disable automatic connect by client when system is up.'
               bookmark-group:
                  type: array
                  suboptions:
                     bookmarks:
                        type: array
                        suboptions:
                           additional-params:
                              type: str
                              description: 'Additional parameters.'
                           apptype:
                              type: str
                              description: 'Application type.'
                           description:
                              type: str
                              description: 'Description.'
                           folder:
                              type: str
                              description: 'Network shared file folder parameter.'
                           form-data:
                              type: array
                              suboptions:
                                 name:
                                    type: str
                                    description: 'Name.'
                                 value:
                                    type: str
                                    description: 'Value.'
                           host:
                              type: str
                              description: 'Host name/IP parameter.'
                           listening-port:
                              type: int
                              description: 'Listening port (0 - 65535).'
                           load-balancing-info:
                              type: str
                              description: 'The load balancing information or cookie which should be provided to the connection broker.'
                           logon-password:
                              type: array
                              suboptions:
                                 type: str
                           logon-user:
                              type: str
                              description: 'Logon user.'
                           name:
                              type: str
                              description: 'Bookmark name.'
                           port:
                              type: int
                              description: 'Remote port.'
                           preconnection-blob:
                              type: str
                              description: 'An arbitrary string which identifies the RDP source.'
                           preconnection-id:
                              type: int
                              description: 'The numeric ID of the RDP source (0-2147483648).'
                           remote-port:
                              type: int
                              description: 'Remote port (0 - 65535).'
                           security:
                              type: str
                              description: 'Security mode for RDP connection.'
                           server-layout:
                              type: str
                              description: 'Server side keyboard layout.'
                           show-status-window:
                              type: str
                              description: 'Enable/disable showing of status window.'
                           sso:
                              type: str
                              description: 'Single Sign-On.'
                           sso-credential:
                              type: str
                              description: 'Single sign-on credentials.'
                           sso-credential-sent-once:
                              type: str
                              description: 'Single sign-on credentials are only sent once to remote server.'
                           sso-password:
                              type: array
                              suboptions:
                                 type: str
                           sso-username:
                              type: str
                              description: 'SSO user name.'
                           url:
                              type: str
                              description: 'URL parameter.'
                     name:
                        type: str
                        description: 'Bookmark group name.'
               custom-lang:
                  type: str
                  description: 'Change the web portal display language. Overrides config system global set language. You can use config system custom-langua...'
               customize-forticlient-download-url:
                  type: str
                  description: 'Enable support of customized download URL for FortiClient.'
               display-bookmark:
                  type: str
                  description: 'Enable to display the web portal bookmark widget.'
               display-connection-tools:
                  type: str
                  description: 'Enable to display the web portal connection tools widget.'
               display-history:
                  type: str
                  description: 'Enable to display the web portal user login history widget.'
               display-status:
                  type: str
                  description: 'Enable to display the web portal status widget.'
               dns-server1:
                  type: str
                  description: 'IPv4 DNS server 1.'
               dns-server2:
                  type: str
                  description: 'IPv4 DNS server 2.'
               dns-suffix:
                  type: str
                  description: 'DNS suffix.'
               exclusive-routing:
                  type: str
                  description: 'Enable/disable all traffic go through tunnel only.'
               forticlient-download:
                  type: str
                  description: 'Enable/disable download option for FortiClient.'
               forticlient-download-method:
                  type: str
                  description: 'FortiClient download method.'
               heading:
                  type: str
                  description: 'Web portal heading message.'
               hide-sso-credential:
                  type: str
                  description: 'Enable to prevent SSO credential being sent to client.'
               host-check:
                  type: str
                  description: 'Type of host checking performed on endpoints.'
               host-check-interval:
                  type: int
                  description: 'Periodic host check interval. Value of 0 means disabled and host checking only happens when the endpoint connects.'
               host-check-policy:
                  type: str
                  description: 'One or more policies to require the endpoint to have specific security software.'
               ip-mode:
                  type: str
                  description: 'Method by which users of this SSL-VPN tunnel obtain IP addresses.'
               ip-pools:
                  type: str
                  description: 'IPv4 firewall source address objects reserved for SSL-VPN tunnel mode clients.'
               ipv6-dns-server1:
                  type: str
                  description: 'IPv6 DNS server 1.'
               ipv6-dns-server2:
                  type: str
                  description: 'IPv6 DNS server 2.'
               ipv6-exclusive-routing:
                  type: str
                  description: 'Enable/disable all IPv6 traffic go through tunnel only.'
               ipv6-pools:
                  type: str
                  description: 'IPv4 firewall source address objects reserved for SSL-VPN tunnel mode clients.'
               ipv6-service-restriction:
                  type: str
                  description: 'Enable/disable IPv6 tunnel service restriction.'
               ipv6-split-tunneling:
                  type: str
                  description: 'Enable/disable IPv6 split tunneling.'
               ipv6-split-tunneling-routing-address:
                  type: str
                  description: 'IPv6 SSL-VPN tunnel mode firewall address objects that override firewall policy destination addresses to control split-tunne...'
               ipv6-tunnel-mode:
                  type: str
                  description: 'Enable/disable IPv6 SSL-VPN tunnel mode.'
               ipv6-wins-server1:
                  type: str
                  description: 'IPv6 WINS server 1.'
               ipv6-wins-server2:
                  type: str
                  description: 'IPv6 WINS server 2.'
               keep-alive:
                  type: str
                  description: 'Enable/disable automatic reconnect for FortiClient connections.'
               limit-user-logins:
                  type: str
                  description: 'Enable to limit each user to one SSL-VPN session at a time.'
               mac-addr-action:
                  type: str
                  description: 'Client MAC address action.'
               mac-addr-check:
                  type: str
                  description: 'Enable/disable MAC address host checking.'
               mac-addr-check-rule:
                  type: array
                  suboptions:
                     mac-addr-list:
                        type: array
                        suboptions:
                           type: str
                     mac-addr-mask:
                        type: int
                        description: 'Client MAC address mask.'
                     name:
                        type: str
                        description: 'Client MAC address check rule name.'
               macos-forticlient-download-url:
                  type: str
                  description: 'Download URL for Mac FortiClient.'
               name:
                  type: str
                  description: 'Portal name.'
               os-check:
                  type: str
                  description: 'Enable to let the FortiGate decide action based on client OS.'
               redir-url:
                  type: str
                  description: 'Client login redirect URL.'
               save-password:
                  type: str
                  description: 'Enable/disable FortiClient saving the users password.'
               service-restriction:
                  type: str
                  description: 'Enable/disable tunnel service restriction.'
               skip-check-for-unsupported-browser:
                  type: str
                  description: 'Enable to skip host check if browser does not support it.'
               skip-check-for-unsupported-os:
                  type: str
                  description: 'Enable to skip host check if client OS does not support it.'
               smb-ntlmv1-auth:
                  type: str
                  description: 'Enable support of NTLMv1 for Samba authentication.'
               smbv1:
                  type: str
                  description: 'Enable/disable support of SMBv1 for Samba.'
               split-dns:
                  type: array
                  suboptions:
                     dns-server1:
                        type: str
                        description: 'DNS server 1.'
                     dns-server2:
                        type: str
                        description: 'DNS server 2.'
                     domains:
                        type: str
                        description: 'Split DNS domains used for SSL-VPN clients separated by comma(,).'
                     id:
                        type: int
                        description: 'ID.'
                     ipv6-dns-server1:
                        type: str
                        description: 'IPv6 DNS server 1.'
                     ipv6-dns-server2:
                        type: str
                        description: 'IPv6 DNS server 2.'
               split-tunneling:
                  type: str
                  description: 'Enable/disable IPv4 split tunneling.'
               split-tunneling-routing-address:
                  type: str
                  description: 'IPv4 SSL-VPN tunnel mode firewall address objects that override firewall policy destination addresses to control split-tunne...'
               theme:
                  type: str
                  description: 'Web portal color scheme.'
               tunnel-mode:
                  type: str
                  description: 'Enable/disable IPv4 SSL-VPN tunnel mode.'
               user-bookmark:
                  type: str
                  description: 'Enable to allow web portal users to create their own bookmarks.'
               user-group-bookmark:
                  type: str
                  description: 'Enable to allow web portal users to create bookmarks for all users in the same user group.'
               web-mode:
                  type: str
                  description: 'Enable/disable SSL VPN web mode.'
               windows-forticlient-download-url:
                  type: str
                  description: 'Download URL for Windows FortiClient.'
               wins-server1:
                  type: str
                  description: 'IPv4 WINS server 1.'
               wins-server2:
                  type: str
                  description: 'IPv4 WINS server 1.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/vpn/ssl/web/portal'

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
        '/pm/config/adom/{adom}/obj/vpn/ssl/web/portal',
        '/pm/config/global/obj/vpn/ssl/web/portal'
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
                        'allow-user-access': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'web',
                                    'ftp',
                                    'telnet',
                                    'smb',
                                    'vnc',
                                    'rdp',
                                    'ssh',
                                    'ping',
                                    'citrix',
                                    'portforward',
                                    'sftp'
                                ]
                            }
                        },
                        'auto-connect': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'bookmark-group': {
                            'type': 'array',
                            'items': {
                                'bookmarks': {
                                    'type': 'array',
                                    'items': {
                                        'additional-params': {
                                            'type': 'string'
                                        },
                                        'apptype': {
                                            'type': 'string',
                                            'enum': [
                                                'web',
                                                'telnet',
                                                'ssh',
                                                'ftp',
                                                'smb',
                                                'vnc',
                                                'rdp',
                                                'citrix',
                                                'rdpnative',
                                                'portforward',
                                                'sftp'
                                            ]
                                        },
                                        'description': {
                                            'type': 'string'
                                        },
                                        'folder': {
                                            'type': 'string'
                                        },
                                        'form-data': {
                                            'type': 'array',
                                            'items': {
                                                'name': {
                                                    'type': 'string'
                                                },
                                                'value': {
                                                    'type': 'string'
                                                }
                                            }
                                        },
                                        'host': {
                                            'type': 'string'
                                        },
                                        'listening-port': {
                                            'type': 'integer'
                                        },
                                        'load-balancing-info': {
                                            'type': 'string'
                                        },
                                        'logon-password': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'string'
                                            }
                                        },
                                        'logon-user': {
                                            'type': 'string'
                                        },
                                        'name': {
                                            'type': 'string'
                                        },
                                        'port': {
                                            'type': 'integer'
                                        },
                                        'preconnection-blob': {
                                            'type': 'string'
                                        },
                                        'preconnection-id': {
                                            'type': 'integer'
                                        },
                                        'remote-port': {
                                            'type': 'integer'
                                        },
                                        'security': {
                                            'type': 'string',
                                            'enum': [
                                                'rdp',
                                                'nla',
                                                'tls',
                                                'any'
                                            ]
                                        },
                                        'server-layout': {
                                            'type': 'string',
                                            'enum': [
                                                'en-us-qwerty',
                                                'de-de-qwertz',
                                                'fr-fr-azerty',
                                                'it-it-qwerty',
                                                'sv-se-qwerty',
                                                'failsafe',
                                                'en-gb-qwerty',
                                                'es-es-qwerty',
                                                'fr-ch-qwertz',
                                                'ja-jp-qwerty',
                                                'pt-br-qwerty',
                                                'tr-tr-qwerty'
                                            ]
                                        },
                                        'show-status-window': {
                                            'type': 'string',
                                            'enum': [
                                                'disable',
                                                'enable'
                                            ]
                                        },
                                        'sso': {
                                            'type': 'string',
                                            'enum': [
                                                'disable',
                                                'static',
                                                'auto'
                                            ]
                                        },
                                        'sso-credential': {
                                            'type': 'string',
                                            'enum': [
                                                'sslvpn-login',
                                                'alternative'
                                            ]
                                        },
                                        'sso-credential-sent-once': {
                                            'type': 'string',
                                            'enum': [
                                                'disable',
                                                'enable'
                                            ]
                                        },
                                        'sso-password': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'string'
                                            }
                                        },
                                        'sso-username': {
                                            'type': 'string'
                                        },
                                        'url': {
                                            'type': 'string'
                                        }
                                    }
                                },
                                'name': {
                                    'type': 'string'
                                }
                            }
                        },
                        'custom-lang': {
                            'type': 'string'
                        },
                        'customize-forticlient-download-url': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'display-bookmark': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'display-connection-tools': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'display-history': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'display-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dns-server1': {
                            'type': 'string'
                        },
                        'dns-server2': {
                            'type': 'string'
                        },
                        'dns-suffix': {
                            'type': 'string'
                        },
                        'exclusive-routing': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'forticlient-download': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'forticlient-download-method': {
                            'type': 'string',
                            'enum': [
                                'direct',
                                'ssl-vpn'
                            ]
                        },
                        'heading': {
                            'type': 'string'
                        },
                        'hide-sso-credential': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'host-check': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'av',
                                'fw',
                                'av-fw',
                                'custom'
                            ]
                        },
                        'host-check-interval': {
                            'type': 'integer'
                        },
                        'host-check-policy': {
                            'type': 'string'
                        },
                        'ip-mode': {
                            'type': 'string',
                            'enum': [
                                'range',
                                'user-group'
                            ]
                        },
                        'ip-pools': {
                            'type': 'string'
                        },
                        'ipv6-dns-server1': {
                            'type': 'string'
                        },
                        'ipv6-dns-server2': {
                            'type': 'string'
                        },
                        'ipv6-exclusive-routing': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ipv6-pools': {
                            'type': 'string'
                        },
                        'ipv6-service-restriction': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ipv6-split-tunneling': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ipv6-split-tunneling-routing-address': {
                            'type': 'string'
                        },
                        'ipv6-tunnel-mode': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ipv6-wins-server1': {
                            'type': 'string'
                        },
                        'ipv6-wins-server2': {
                            'type': 'string'
                        },
                        'keep-alive': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'limit-user-logins': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mac-addr-action': {
                            'type': 'string',
                            'enum': [
                                'deny',
                                'allow'
                            ]
                        },
                        'mac-addr-check': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mac-addr-check-rule': {
                            'type': 'array',
                            'items': {
                                'mac-addr-list': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                },
                                'mac-addr-mask': {
                                    'type': 'integer'
                                },
                                'name': {
                                    'type': 'string'
                                }
                            }
                        },
                        'macos-forticlient-download-url': {
                            'type': 'string'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'os-check': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'redir-url': {
                            'type': 'string'
                        },
                        'save-password': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'service-restriction': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'skip-check-for-unsupported-browser': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'skip-check-for-unsupported-os': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'smb-ntlmv1-auth': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'smbv1': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'split-dns': {
                            'type': 'array',
                            'items': {
                                'dns-server1': {
                                    'type': 'string'
                                },
                                'dns-server2': {
                                    'type': 'string'
                                },
                                'domains': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'ipv6-dns-server1': {
                                    'type': 'string'
                                },
                                'ipv6-dns-server2': {
                                    'type': 'string'
                                }
                            }
                        },
                        'split-tunneling': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'split-tunneling-routing-address': {
                            'type': 'string'
                        },
                        'theme': {
                            'type': 'string',
                            'enum': [
                                'gray',
                                'blue',
                                'orange',
                                'crimson',
                                'steelblue',
                                'darkgrey',
                                'green',
                                'melongene',
                                'red',
                                'mariner'
                            ]
                        },
                        'tunnel-mode': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'user-bookmark': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'user-group-bookmark': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'web-mode': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'windows-forticlient-download-url': {
                            'type': 'string'
                        },
                        'wins-server1': {
                            'type': 'string'
                        },
                        'wins-server2': {
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
                                'allow-user-access',
                                'auto-connect',
                                'custom-lang',
                                'customize-forticlient-download-url',
                                'display-bookmark',
                                'display-connection-tools',
                                'display-history',
                                'display-status',
                                'dns-server1',
                                'dns-server2',
                                'dns-suffix',
                                'exclusive-routing',
                                'forticlient-download',
                                'forticlient-download-method',
                                'heading',
                                'hide-sso-credential',
                                'host-check',
                                'host-check-interval',
                                'host-check-policy',
                                'ip-mode',
                                'ip-pools',
                                'ipv6-dns-server1',
                                'ipv6-dns-server2',
                                'ipv6-exclusive-routing',
                                'ipv6-pools',
                                'ipv6-service-restriction',
                                'ipv6-split-tunneling',
                                'ipv6-split-tunneling-routing-address',
                                'ipv6-tunnel-mode',
                                'ipv6-wins-server1',
                                'ipv6-wins-server2',
                                'keep-alive',
                                'limit-user-logins',
                                'mac-addr-action',
                                'mac-addr-check',
                                'macos-forticlient-download-url',
                                'name',
                                'os-check',
                                'redir-url',
                                'save-password',
                                'service-restriction',
                                'skip-check-for-unsupported-browser',
                                'skip-check-for-unsupported-os',
                                'smb-ntlmv1-auth',
                                'smbv1',
                                'split-tunneling',
                                'split-tunneling-routing-address',
                                'theme',
                                'tunnel-mode',
                                'user-bookmark',
                                'user-group-bookmark',
                                'web-mode',
                                'windows-forticlient-download-url',
                                'wins-server1',
                                'wins-server2'
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
