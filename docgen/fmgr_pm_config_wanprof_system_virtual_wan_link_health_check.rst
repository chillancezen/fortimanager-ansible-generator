:source: fmgr_pm_config_wanprof_system_virtual_wan_link_health_check.py

:orphan:

.. _fmgr_pm_config_wanprof_system_virtual_wan_link_health_check:

fmgr_pm_config_wanprof_system_virtual_wan_link_health_check -- SD-WAN status checking or health checking.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/health-check`
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
 <li><span class="li-head">wanprof</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - SD-WAN status checking or health checking. Identify a server on the Internet and determine how SD-WAN verifies that the FortiGate can communicate with it.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_dynamic-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">addr-mode</span> - Address mode (IPv4 or IPv6). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipv4, ipv6]</span> </li>
 <li><span class="li-head">failtime</span> - Number of failures before server is considered lost (1 - 3600, default = 5). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">http-agent</span> - String in the http-agent field in the HTTP header. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-get</span> - URL used to communicate with the server if the protocol if the protocol is HTTP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-match</span> - Response string expected from the server if the protocol is HTTP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">interval</span> - Status check interval, or the time between attempting to connect to the server (1 - 3600 sec, default = 5). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">members</span> - Member sequence number list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Status check or health check name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">packet-size</span> - Packet size of a twamp test session, <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">port</span> - Port number used to communicate with the server over the selected protocol. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">protocol</span> - Protocol used to determine if the FortiGate can communicate with the server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ping, tcp-echo, udp-echo, http, twamp, ping6]</span> </li>
 <li><span class="li-head">recoverytime</span> - Number of successful responses received before server is considered recovered (1 - 3600, default = 5). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">security-mode</span> - Twamp controller security mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, authentication]</span> </li>
 <li><span class="li-head">server</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">sla</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - SLA ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">jitter-threshold</span> - Jitter for SLA to make decision in milliseconds. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">latency-threshold</span> - Latency for SLA to make decision in milliseconds. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">link-cost-factor</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [latency, jitter, packet-loss]</span> </li>
 </ul>
 <li><span class="li-head">packetloss-threshold</span> - Packet loss for SLA to make decision in percentage. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">threshold-alert-jitter</span> - Alert threshold for jitter (ms, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold-alert-latency</span> - Alert threshold for latency (ms, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold-alert-packetloss</span> - Alert threshold for packet loss (percentage, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold-warning-jitter</span> - Warning threshold for jitter (ms, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold-warning-latency</span> - Warning threshold for latency (ms, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold-warning-packetloss</span> - Warning threshold for packet loss (percentage, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">update-cascade-interface</span> - Enable/disable update cascade interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">update-static-route</span> - Enable/disable updating the static route. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - SD-WAN status checking or health checking. Identify a server on the Internet and determine how SD-WAN verifies that the FortiGate can communicate with it.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [_dynamic-server, addr-mode, failtime, http-agent, http-get, http-match, interval, members, name, packet-size, password, port, protocol, recoverytime, security-mode, server, threshold-alert-jitter, threshold-alert-latency, threshold-alert-packetloss, threshold-warning-jitter, threshold-warning-latency, threshold-warning-packetloss, update-cascade-interface, update-static-route]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/WANPROF/{WANPROF}/SYSTEM/VIRTUAL-WAN-LINK/HEALTH-CHECK
      fmgr_pm_config_wanprof_system_virtual_wan_link_health_check:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wanprof: <value of string>
         params:
            -
               data:
                 -
                     _dynamic-server: <value of string>
                     addr-mode: <value in [ipv4, ipv6]>
                     failtime: <value of integer>
                     http-agent: <value of string>
                     http-get: <value of string>
                     http-match: <value of string>
                     interval: <value of integer>
                     members: <value of string>
                     name: <value of string>
                     packet-size: <value of integer>
                     password:
                       - <value of string>
                     port: <value of integer>
                     protocol: <value in [ping, tcp-echo, udp-echo, ...]>
                     recoverytime: <value of integer>
                     security-mode: <value in [none, authentication]>
                     server:
                       - <value of string>
                     sla:
                       -
                           id: <value of integer>
                           jitter-threshold: <value of integer>
                           latency-threshold: <value of integer>
                           link-cost-factor:
                             - <value in [latency, jitter, packet-loss]>
                           packetloss-threshold: <value of integer>
                     threshold-alert-jitter: <value of integer>
                     threshold-alert-latency: <value of integer>
                     threshold-alert-packetloss: <value of integer>
                     threshold-warning-jitter: <value of integer>
                     threshold-warning-latency: <value of integer>
                     threshold-warning-packetloss: <value of integer>
                     update-cascade-interface: <value in [disable, enable]>
                     update-static-route: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/WANPROF/{WANPROF}/SYSTEM/VIRTUAL-WAN-LINK/HEALTH-CHECK
      fmgr_pm_config_wanprof_system_virtual_wan_link_health_check:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wanprof: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [_dynamic-server, addr-mode, failtime, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/health-check</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> _dynamic-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> addr-mode </span> - Address mode (IPv4 or IPv6). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> failtime </span> - Number of failures before server is considered lost (1 - 3600, default = 5). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> http-agent </span> - String in the http-agent field in the HTTP header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-get </span> - URL used to communicate with the server if the protocol if the protocol is HTTP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-match </span> - Response string expected from the server if the protocol is HTTP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> interval </span> - Status check interval, or the time between attempting to connect to the server (1 - 3600 sec, default = 5). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> members </span> - Member sequence number list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Status check or health check name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> packet-size </span> - Packet size of a twamp test session, <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> port </span> - Port number used to communicate with the server over the selected protocol. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> protocol </span> - Protocol used to determine if the FortiGate can communicate with the server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> recoverytime </span> - Number of successful responses received before server is considered recovered (1 - 3600, default = 5). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> security-mode </span> - Twamp controller security mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> sla </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - SLA ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> jitter-threshold </span> - Jitter for SLA to make decision in milliseconds. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> latency-threshold </span> - Latency for SLA to make decision in milliseconds. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> link-cost-factor </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> packetloss-threshold </span> - Packet loss for SLA to make decision in percentage. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> threshold-alert-jitter </span> - Alert threshold for jitter (ms, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> threshold-alert-latency </span> - Alert threshold for latency (ms, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> threshold-alert-packetloss </span> - Alert threshold for packet loss (percentage, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> threshold-warning-jitter </span> - Warning threshold for jitter (ms, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> threshold-warning-latency </span> - Warning threshold for latency (ms, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> threshold-warning-packetloss </span> - Warning threshold for packet loss (percentage, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> update-cascade-interface </span> - Enable/disable update cascade interface. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> update-static-route </span> - Enable/disable updating the static route. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/health-check</span>  </li>
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



