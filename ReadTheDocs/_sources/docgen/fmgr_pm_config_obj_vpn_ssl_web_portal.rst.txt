:source: fmgr_pm_config_obj_vpn_ssl_web_portal.py

:orphan:

.. _fmgr_pm_config_obj_vpn_ssl_web_portal:

fmgr_pm_config_obj_vpn_ssl_web_portal -- Portal.
++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/vpn/ssl/web/portal`
- `/pm/config/global/obj/vpn/ssl/web/portal`
- Examples include all parameters and values need to be adjusted to data sources before usage.
- Tested with FortiManager v6.0.0


Requirements
------------
The below requirements are needed on the host that executes this module.

- ansible>=2.10.0



Parameters
----------

.. raw:: html

 <ul>
 <li><span class="li-head">url_params</span> - parameters in url path <span class="li-normal">type: dict</span> <span class="li-required">required: true</span></li>
 <ul class="ul-self">
 <li><span class="li-head">adom</span> - the domain prefix <span class="li-normal">type: str</span> <span class="li-normal"> choices: none, global, custom dom</span></li>
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Portal.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">allow-user-access</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [web, ftp, telnet, smb, vnc, rdp, ssh, ping, citrix, portforward, sftp]</span> </li>
 </ul>
 <li><span class="li-head">auto-connect</span> - Enable/disable automatic connect by client when system is up. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">bookmark-group</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">bookmarks</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">additional-params</span> - Additional parameters. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">apptype</span> - Application type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [web, telnet, ssh, ftp, smb, vnc, rdp, citrix, rdpnative, portforward, sftp]</span> </li>
 <li><span class="li-head">description</span> - Description. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">folder</span> - Network shared file folder parameter. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">form-data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - Name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">value</span> - Value. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">host</span> - Host name/IP parameter. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">listening-port</span> - Listening port (0 - 65535). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">load-balancing-info</span> - The load balancing information or cookie which should be provided to the connection broker. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">logon-password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">logon-user</span> - Logon user. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Bookmark name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port</span> - Remote port. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">preconnection-blob</span> - An arbitrary string which identifies the RDP source. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">preconnection-id</span> - The numeric ID of the RDP source (0-2147483648). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">remote-port</span> - Remote port (0 - 65535). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">security</span> - Security mode for RDP connection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rdp, nla, tls, any]</span> </li>
 <li><span class="li-head">server-layout</span> - Server side keyboard layout. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [en-us-qwerty, de-de-qwertz, fr-fr-azerty, it-it-qwerty, sv-se-qwerty, failsafe, en-gb-qwerty, es-es-qwerty, fr-ch-qwertz, ja-jp-qwerty, pt-br-qwerty, tr-tr-qwerty]</span> </li>
 <li><span class="li-head">show-status-window</span> - Enable/disable showing of status window. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sso</span> - Single Sign-On. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, static, auto]</span> </li>
 <li><span class="li-head">sso-credential</span> - Single sign-on credentials. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sslvpn-login, alternative]</span> </li>
 <li><span class="li-head">sso-credential-sent-once</span> - Single sign-on credentials are only sent once to remote server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sso-password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">sso-username</span> - SSO user name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">url</span> - URL parameter. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">name</span> - Bookmark group name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">custom-lang</span> - Change the web portal display language. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">customize-forticlient-download-url</span> - Enable support of customized download URL for FortiClient. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">display-bookmark</span> - Enable to display the web portal bookmark widget. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">display-connection-tools</span> - Enable to display the web portal connection tools widget. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">display-history</span> - Enable to display the web portal user login history widget. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">display-status</span> - Enable to display the web portal status widget. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dns-server1</span> - IPv4 DNS server 1. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-server2</span> - IPv4 DNS server 2. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-suffix</span> - DNS suffix. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">exclusive-routing</span> - Enable/disable all traffic go through tunnel only. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">forticlient-download</span> - Enable/disable download option for FortiClient. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">forticlient-download-method</span> - FortiClient download method. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [direct, ssl-vpn]</span> </li>
 <li><span class="li-head">heading</span> - Web portal heading message. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">hide-sso-credential</span> - Enable to prevent SSO credential being sent to client. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">host-check</span> - Type of host checking performed on endpoints. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, av, fw, av-fw, custom]</span> </li>
 <li><span class="li-head">host-check-interval</span> - Periodic host check interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">host-check-policy</span> - One or more policies to require the endpoint to have specific security software. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip-mode</span> - Method by which users of this SSL-VPN tunnel obtain IP addresses. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [range, user-group]</span> </li>
 <li><span class="li-head">ip-pools</span> - IPv4 firewall source address objects reserved for SSL-VPN tunnel mode clients. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6-dns-server1</span> - IPv6 DNS server 1. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6-dns-server2</span> - IPv6 DNS server 2. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6-exclusive-routing</span> - Enable/disable all IPv6 traffic go through tunnel only. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ipv6-pools</span> - IPv4 firewall source address objects reserved for SSL-VPN tunnel mode clients. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6-service-restriction</span> - Enable/disable IPv6 tunnel service restriction. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ipv6-split-tunneling</span> - Enable/disable IPv6 split tunneling. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ipv6-split-tunneling-routing-address</span> - IPv6 SSL-VPN tunnel mode firewall address objects that override firewall policy destination addresses to control split-tunneling access. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6-tunnel-mode</span> - Enable/disable IPv6 SSL-VPN tunnel mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ipv6-wins-server1</span> - IPv6 WINS server 1. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6-wins-server2</span> - IPv6 WINS server 2. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">keep-alive</span> - Enable/disable automatic reconnect for FortiClient connections. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">limit-user-logins</span> - Enable to limit each user to one SSL-VPN session at a time. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mac-addr-action</span> - Client MAC address action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, allow]</span> </li>
 <li><span class="li-head">mac-addr-check</span> - Enable/disable MAC address host checking. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mac-addr-check-rule</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">mac-addr-list</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">mac-addr-mask</span> - Client MAC address mask. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - Client MAC address check rule name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">macos-forticlient-download-url</span> - Download URL for Mac FortiClient. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Portal name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">os-check</span> - Enable to let the FortiGate decide action based on client OS. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">redir-url</span> - Client login redirect URL. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">save-password</span> - Enable/disable FortiClient saving the user's password. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">service-restriction</span> - Enable/disable tunnel service restriction. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">skip-check-for-unsupported-browser</span> - Enable to skip host check if browser does not support it. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">skip-check-for-unsupported-os</span> - Enable to skip host check if client OS does not support it. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">smb-ntlmv1-auth</span> - Enable support of NTLMv1 for Samba authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">smbv1</span> - Enable/disable support of SMBv1 for Samba. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">split-dns</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">dns-server1</span> - DNS server 1. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-server2</span> - DNS server 2. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">domains</span> - Split DNS domains used for SSL-VPN clients separated by comma(,). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ipv6-dns-server1</span> - IPv6 DNS server 1. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv6-dns-server2</span> - IPv6 DNS server 2. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">split-tunneling</span> - Enable/disable IPv4 split tunneling. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">split-tunneling-routing-address</span> - IPv4 SSL-VPN tunnel mode firewall address objects that override firewall policy destination addresses to control split-tunneling access. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">theme</span> - Web portal color scheme. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [gray, blue, orange, crimson, steelblue, darkgrey, green, melongene, red, mariner]</span> </li>
 <li><span class="li-head">tunnel-mode</span> - Enable/disable IPv4 SSL-VPN tunnel mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">user-bookmark</span> - Enable to allow web portal users to create their own bookmarks. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">user-group-bookmark</span> - Enable to allow web portal users to create bookmarks for all users in the same user group. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">web-mode</span> - Enable/disable SSL VPN web mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">windows-forticlient-download-url</span> - Download URL for Windows FortiClient. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wins-server1</span> - IPv4 WINS server 1. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wins-server2</span> - IPv4 WINS server 1. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Portal.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow-user-access, auto-connect, custom-lang, customize-forticlient-download-url, display-bookmark, display-connection-tools, display-history, display-status, dns-server1, dns-server2, dns-suffix, exclusive-routing, forticlient-download, forticlient-download-method, heading, hide-sso-credential, host-check, host-check-interval, host-check-policy, ip-mode, ip-pools, ipv6-dns-server1, ipv6-dns-server2, ipv6-exclusive-routing, ipv6-pools, ipv6-service-restriction, ipv6-split-tunneling, ipv6-split-tunneling-routing-address, ipv6-tunnel-mode, ipv6-wins-server1, ipv6-wins-server2, keep-alive, limit-user-logins, mac-addr-action, mac-addr-check, macos-forticlient-download-url, name, os-check, redir-url, save-password, service-restriction, skip-check-for-unsupported-browser, skip-check-for-unsupported-os, smb-ntlmv1-auth, smbv1, split-tunneling, split-tunneling-routing-address, theme, tunnel-mode, user-bookmark, user-group-bookmark, web-mode, windows-forticlient-download-url, wins-server1, wins-server2]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">get used</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">loadsub</span> - Enable or disable the return of any sub-objects. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [count, object member, datasrc, get reserved, syntax]</span> </li>
 <li><span class="li-head">range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">sortings</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{attr_name}</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">choices: [1, -1]</span> </li>
 </ul>
 </ul>
 </ul>






Notes
-----
.. note::

   - The module may supports multiple method, every method has different parameters definition

   - One method may also have more than one parameter definition collection, each collection is dedicated to one API endpoint

   - The module may include domain dependent urls, the domain can be specified in url_params as adom

Examples
--------

.. code-block:: yaml+jinja

 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /pm/config/obj/vpn/ssl/web/portal
      fmgr_pm_config_obj_vpn_ssl_web_portal:
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
    - name: send request to /pm/config/obj/vpn/ssl/web/portal
      fmgr_pm_config_obj_vpn_ssl_web_portal:
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
                     \{attr_name\}: <value in [1, -1]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [add, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/vpn/ssl/web/portal</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> allow-user-access </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> auto-connect </span> - Enable/disable automatic connect by client when system is up. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> bookmark-group </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> bookmarks </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> additional-params </span> - Additional parameters. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> apptype </span> - Application type. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> description </span> - Description. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> folder </span> - Network shared file folder parameter. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> form-data </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - Name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> value </span> - Value. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> host </span> - Host name/IP parameter. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> listening-port </span> - Listening port (0 - 65535). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> load-balancing-info </span> - The load balancing information or cookie which should be provided to the connection broker. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> logon-password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> logon-user </span> - Logon user. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Bookmark name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port </span> - Remote port. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> preconnection-blob </span> - An arbitrary string which identifies the RDP source. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> preconnection-id </span> - The numeric ID of the RDP source (0-2147483648). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> remote-port </span> - Remote port (0 - 65535). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> security </span> - Security mode for RDP connection. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server-layout </span> - Server side keyboard layout. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> show-status-window </span> - Enable/disable showing of status window. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sso </span> - Single Sign-On. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sso-credential </span> - Single sign-on credentials. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sso-credential-sent-once </span> - Single sign-on credentials are only sent once to remote server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sso-password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> sso-username </span> - SSO user name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> url </span> - URL parameter. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> name </span> - Bookmark group name. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> custom-lang </span> - Change the web portal display language. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> customize-forticlient-download-url </span> - Enable support of customized download URL for FortiClient. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> display-bookmark </span> - Enable to display the web portal bookmark widget. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> display-connection-tools </span> - Enable to display the web portal connection tools widget. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> display-history </span> - Enable to display the web portal user login history widget. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> display-status </span> - Enable to display the web portal status widget. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dns-server1 </span> - IPv4 DNS server 1. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dns-server2 </span> - IPv4 DNS server 2. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dns-suffix </span> - DNS suffix. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> exclusive-routing </span> - Enable/disable all traffic go through tunnel only. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> forticlient-download </span> - Enable/disable download option for FortiClient. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> forticlient-download-method </span> - FortiClient download method. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> heading </span> - Web portal heading message. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> hide-sso-credential </span> - Enable to prevent SSO credential being sent to client. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> host-check </span> - Type of host checking performed on endpoints. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> host-check-interval </span> - Periodic host check interval. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> host-check-policy </span> - One or more policies to require the endpoint to have specific security software. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip-mode </span> - Method by which users of this SSL-VPN tunnel obtain IP addresses. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip-pools </span> - IPv4 firewall source address objects reserved for SSL-VPN tunnel mode clients. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ipv6-dns-server1 </span> - IPv6 DNS server 1. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ipv6-dns-server2 </span> - IPv6 DNS server 2. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ipv6-exclusive-routing </span> - Enable/disable all IPv6 traffic go through tunnel only. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ipv6-pools </span> - IPv4 firewall source address objects reserved for SSL-VPN tunnel mode clients. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ipv6-service-restriction </span> - Enable/disable IPv6 tunnel service restriction. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ipv6-split-tunneling </span> - Enable/disable IPv6 split tunneling. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ipv6-split-tunneling-routing-address </span> - IPv6 SSL-VPN tunnel mode firewall address objects that override firewall policy destination addresses to control split-tunneling access. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ipv6-tunnel-mode </span> - Enable/disable IPv6 SSL-VPN tunnel mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ipv6-wins-server1 </span> - IPv6 WINS server 1. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ipv6-wins-server2 </span> - IPv6 WINS server 2. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> keep-alive </span> - Enable/disable automatic reconnect for FortiClient connections. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> limit-user-logins </span> - Enable to limit each user to one SSL-VPN session at a time. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mac-addr-action </span> - Client MAC address action. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mac-addr-check </span> - Enable/disable MAC address host checking. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mac-addr-check-rule </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> mac-addr-list </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> mac-addr-mask </span> - Client MAC address mask. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> name </span> - Client MAC address check rule name. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> macos-forticlient-download-url </span> - Download URL for Mac FortiClient. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Portal name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> os-check </span> - Enable to let the FortiGate decide action based on client OS. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> redir-url </span> - Client login redirect URL. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> save-password </span> - Enable/disable FortiClient saving the user's password. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> service-restriction </span> - Enable/disable tunnel service restriction. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> skip-check-for-unsupported-browser </span> - Enable to skip host check if browser does not support it. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> skip-check-for-unsupported-os </span> - Enable to skip host check if client OS does not support it. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> smb-ntlmv1-auth </span> - Enable support of NTLMv1 for Samba authentication. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> smbv1 </span> - Enable/disable support of SMBv1 for Samba. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> split-dns </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> dns-server1 </span> - DNS server 1. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dns-server2 </span> - DNS server 2. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> domains </span> - Split DNS domains used for SSL-VPN clients separated by comma(,). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ipv6-dns-server1 </span> - IPv6 DNS server 1. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ipv6-dns-server2 </span> - IPv6 DNS server 2. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> split-tunneling </span> - Enable/disable IPv4 split tunneling. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> split-tunneling-routing-address </span> - IPv4 SSL-VPN tunnel mode firewall address objects that override firewall policy destination addresses to control split-tunneling access. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> theme </span> - Web portal color scheme. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tunnel-mode </span> - Enable/disable IPv4 SSL-VPN tunnel mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> user-bookmark </span> - Enable to allow web portal users to create their own bookmarks. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> user-group-bookmark </span> - Enable to allow web portal users to create bookmarks for all users in the same user group. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> web-mode </span> - Enable/disable SSL VPN web mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> windows-forticlient-download-url </span> - Download URL for Windows FortiClient. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wins-server1 </span> - IPv4 WINS server 1. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wins-server2 </span> - IPv4 WINS server 1. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/vpn/ssl/web/portal</span>  </li>
 </ul>
 </ul>





Status
------

- This module is not guaranteed to have a backwards compatible interface.


Authors
-------

- Frank Shen (@fshen01)
- Link Zheng (@zhengl)


.. hint::

    If you notice any issues in this documentation, you can create a pull request to improve it.



