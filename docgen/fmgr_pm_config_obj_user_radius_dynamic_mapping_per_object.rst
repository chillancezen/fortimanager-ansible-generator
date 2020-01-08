:source: fmgr_pm_config_obj_user_radius_dynamic_mapping_per_object.py

:orphan:

.. _fmgr_pm_config_obj_user_radius_dynamic_mapping_per_object:

fmgr_pm_config_obj_user_radius_dynamic_mapping_per_object
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/user/radius/{radius}/dynamic_mapping/{dynamic_mapping}`
- `/pm/config/global/obj/user/radius/{radius}/dynamic_mapping/{dynamic_mapping}`
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
 <li><span class="li-head">radius</span> - the object name <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dynamic_mapping</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">acct-all-servers</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">acct-interim-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">all-usergroup</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auth-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pap, chap, ms_chap, ms_chap_v2, auto]</span> </li>
 <li><span class="li-head">class</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">dp-carrier-endpoint-attribute</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Vendor-Specific, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span> </li>
 <li><span class="li-head">dp-carrier-endpoint-block-attribute</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Vendor-Specific, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span> </li>
 <li><span class="li-head">dp-context-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dp-flush-ip-session</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dp-hold-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dp-http-header</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dp-http-header-fallback</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ip-header-address, default-profile]</span> </li>
 <li><span class="li-head">dp-http-header-status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dp-http-header-suppress</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dp-log-dyn_flags</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, protocol-error, profile-missing, context-missing, accounting-stop-missed, accounting-event, radiusd-other, endpoint-block]</span> </li>
 </ul>
 <li><span class="li-head">dp-log-period</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dp-mem-percent</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dp-profile-attribute</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Vendor-Specific, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span> </li>
 <li><span class="li-head">dp-profile-attribute-key</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dp-radius-response</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dp-radius-server-port</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dp-secret</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">dp-validate-request-secret</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dynamic-profile</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">endpoint-translation</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ep-carrier-endpoint-convert-hex</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ep-carrier-endpoint-header</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ep-carrier-endpoint-header-suppress</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ep-carrier-endpoint-prefix</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ep-carrier-endpoint-prefix-range-max</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ep-carrier-endpoint-prefix-range-min</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ep-carrier-endpoint-prefix-string</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ep-carrier-endpoint-source</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [http-header, cookie]</span> </li>
 <li><span class="li-head">ep-ip-header</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ep-ip-header-suppress</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ep-missing-header-fallback</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [session-ip, policy-profile]</span> </li>
 <li><span class="li-head">ep-profile-query-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [session-ip, extract-ip, extract-carrier-endpoint]</span> </li>
 <li><span class="li-head">h3c-compatibility</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">nas-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">password-encoding</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ISO-8859-1, auto]</span> </li>
 <li><span class="li-head">password-renewal</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">radius-coa</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">radius-port</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rsso</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rsso-context-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rsso-endpoint-attribute</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span> </li>
 <li><span class="li-head">rsso-endpoint-block-attribute</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span> </li>
 <li><span class="li-head">rsso-ep-one-ip-only</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rsso-flush-ip-session</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rsso-log-flags</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, protocol-error, profile-missing, context-missing, accounting-stop-missed, accounting-event, radiusd-other, endpoint-block]</span> </li>
 </ul>
 <li><span class="li-head">rsso-log-period</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rsso-radius-response</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rsso-radius-server-port</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rsso-secret</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">rsso-validate-request-secret</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">secondary-secret</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">secondary-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">secret</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sso-attribute</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span> </li>
 <li><span class="li-head">sso-attribute-key</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sso-attribute-value-override</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tertiary-secret</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">tertiary-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">use-group-for-profile</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">use-management-vdom</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">username-case-sensitive</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - </li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/USER/RADIUS/{RADIUS}/DYNAMIC_MAPPING/{DYNAMIC_MAPPING}
      fmgr_pm_config_obj_user_radius_dynamic_mapping_per_object:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            radius: <value of string>
            dynamic_mapping: <value of string>
         params:
            -
               data:
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

    - name: REQUESTING /PM/CONFIG/OBJ/USER/RADIUS/{RADIUS}/DYNAMIC_MAPPING/{DYNAMIC_MAPPING}
      fmgr_pm_config_obj_user_radius_dynamic_mapping_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            radius: <value of string>
            dynamic_mapping: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [clone, delete, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/user/radius/{radius}/dynamic_mapping/{dynamic_mapping}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> _scope </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> acct-all-servers </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> acct-interim-interval </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> all-usergroup </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auth-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> class </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> dp-carrier-endpoint-attribute </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dp-carrier-endpoint-block-attribute </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dp-context-timeout </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> dp-flush-ip-session </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dp-hold-time </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> dp-http-header </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dp-http-header-fallback </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dp-http-header-status </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dp-http-header-suppress </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dp-log-dyn_flags </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> dp-log-period </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> dp-mem-percent </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> dp-profile-attribute </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dp-profile-attribute-key </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dp-radius-response </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dp-radius-server-port </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> dp-secret </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> dp-validate-request-secret </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dynamic-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> endpoint-translation </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ep-carrier-endpoint-convert-hex </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ep-carrier-endpoint-header </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ep-carrier-endpoint-header-suppress </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ep-carrier-endpoint-prefix </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ep-carrier-endpoint-prefix-range-max </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ep-carrier-endpoint-prefix-range-min </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ep-carrier-endpoint-prefix-string </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ep-carrier-endpoint-source </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ep-ip-header </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ep-ip-header-suppress </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ep-missing-header-fallback </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ep-profile-query-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> h3c-compatibility </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> nas-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> password-encoding </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> password-renewal </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> radius-coa </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> radius-port </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> rsso </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rsso-context-timeout </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> rsso-endpoint-attribute </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rsso-endpoint-block-attribute </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rsso-ep-one-ip-only </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rsso-flush-ip-session </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rsso-log-flags </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> rsso-log-period </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> rsso-radius-response </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rsso-radius-server-port </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> rsso-secret </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> rsso-validate-request-secret </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> secondary-secret </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> secondary-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> secret </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sso-attribute </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sso-attribute-key </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sso-attribute-value-override </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tertiary-secret </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> tertiary-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> timeout </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> use-group-for-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> use-management-vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> username-case-sensitive </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/user/radius/{radius}/dynamic_mapping/{dynamic_mapping}</span>  </li>
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



