:source: fmgr_pm_config_obj_wireless_controller_wtp_profile.py

:orphan:

.. _fmgr_pm_config_obj_wireless_controller_wtp_profile:

fmgr_pm_config_obj_wireless_controller_wtp_profile -- Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile`
- `/pm/config/global/obj/wireless-controller/wtp-profile`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">allowaccess</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [https, ssh, snmp, http, telnet]</span> </li>
 </ul>
 <li><span class="li-head">ap-country</span> - Country in which this WTP, FortiAP or AP will operate (default = NA, automatically use the country configured for the current VDOM). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [AL, DZ, AR, AM, AU, AT, AZ, BH, BD, BY, BE, BZ, BO, BA, BR, BN, BG, CA, CL, CN, CO, CR, HR, CY, CZ, DK, DO, EC, EG, SV, EE, FI, FR, GE, DE, GR, GT, HN, HK, HU, IS, IN, ID, IR, IE, IL, IT, JM, JP, JO, KZ, KE, KP, KR, KW, LV, LB, LI, LT, LU, MO, MK, MY, MT, MX, MC, MA, NP, NL, AN, NZ, NO, OM, PK, PA, PG, PE, PH, PL, PT, PR, QA, RO, RU, SA, SG, SK, SI, ZA, ES, LK, SE, CH, SY, TW, TH, TT, TN, TR, AE, UA, GB, US, PS, UY, UZ, VE, VN, YE, ZW, NA, KH, TZ, SD, AO, RW, MZ, RS, ME, BB, GD, GL, GU, PY, HT, AW, MM, ZB]</span> </li>
 <li><span class="li-head">ble-profile</span> - Bluetooth Low Energy profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">control-message-offload</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ebp-frame, aeroscout-tag, ap-list, sta-list, sta-cap-list, stats, aeroscout-mu, sta-health]</span> </li>
 </ul>
 <li><span class="li-head">deny-mac-list</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mac</span> - A WiFi device with this MAC address is denied access to this WTP, FortiAP or AP. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">dtls-in-kernel</span> - Enable/disable data channel DTLS in kernel. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dtls-policy</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [clear-text, dtls-enabled, ipsec-vpn]</span> </li>
 </ul>
 <li><span class="li-head">energy-efficient-ethernet</span> - Enable/disable use of energy efficient Ethernet on WTP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ext-info-enable</span> - Enable/disable station/VAP/radio extension information. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">handoff-roaming</span> - Enable/disable client load balancing during roaming to avoid roaming delay (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">handoff-rssi</span> - Minimum received signal strength indicator (RSSI) value for handoff (20 - 30, default = 25). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">handoff-sta-thresh</span> - Threshold value for AP handoff. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip-fragment-preventing</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [tcp-mss-adjust, icmp-unreachable]</span> </li>
 </ul>
 <li><span class="li-head">led-schedules</span> - Recurring firewall schedules for illuminating LEDs on the FortiAP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">led-state</span> - Enable/disable use of LEDs on WTP (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">lldp</span> - Enable/disable Link Layer Discovery Protocol (LLDP) for the WTP, FortiAP, or AP (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">login-passwd</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">login-passwd-change</span> - Change or reset the administrator password of a managed WTP, FortiAP or AP (yes, default, or no, default = no). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [no, yes, default]</span> </li>
 <li><span class="li-head">max-clients</span> - Maximum number of stations (STAs) supported by the WTP (default = 0, meaning no client limitation). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - WTP (or FortiAP or AP) profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">poe-mode</span> - Set the WTP, FortiAP, or APs PoE mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, 8023af, 8023at, power-adapter]</span> </li>
 <li><span class="li-head">split-tunneling-acl</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">dest-ip</span> - Destination IP and mask for the split-tunneling subnet. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">split-tunneling-acl-local-ap-subnet</span> - Enable/disable automatically adding local subnetwork of FortiAP to split-tunneling ACL (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">split-tunneling-acl-path</span> - Split tunneling ACL path is local/tunnel. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [tunnel, local]</span> </li>
 <li><span class="li-head">tun-mtu-downlink</span> - Downlink CAPWAP tunnel MTU (0, 576, or 1500 bytes, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tun-mtu-uplink</span> - Uplink CAPWAP tunnel MTU (0, 576, or 1500 bytes, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">wan-port-mode</span> - Enable/disable using a WAN port as a LAN port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [wan-lan, wan-only]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allowaccess, ap-country, ble-profile, comment, control-message-offload, dtls-in-kernel, dtls-policy, energy-efficient-ethernet, ext-info-enable, handoff-roaming, handoff-rssi, handoff-sta-thresh, ip-fragment-preventing, led-schedules, led-state, lldp, login-passwd, login-passwd-change, max-clients, name, poe-mode, split-tunneling-acl-local-ap-subnet, split-tunneling-acl-path, tun-mtu-downlink, tun-mtu-uplink, wan-port-mode]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WTP-PROFILE
      fmgr_pm_config_obj_wireless_controller_wtp_profile:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     allowaccess:
                       - <value in [https, ssh, snmp, ...]>
                     ap-country: <value in [AL, DZ, AR, ...]>
                     ble-profile: <value of string>
                     comment: <value of string>
                     control-message-offload:
                       - <value in [ebp-frame, aeroscout-tag, ap-list, ...]>
                     deny-mac-list:
                       -
                           id: <value of integer>
                           mac: <value of string>
                     dtls-in-kernel: <value in [disable, enable]>
                     dtls-policy:
                       - <value in [clear-text, dtls-enabled, ipsec-vpn]>
                     energy-efficient-ethernet: <value in [disable, enable]>
                     ext-info-enable: <value in [disable, enable]>
                     handoff-roaming: <value in [disable, enable]>
                     handoff-rssi: <value of integer>
                     handoff-sta-thresh: <value of integer>
                     ip-fragment-preventing:
                       - <value in [tcp-mss-adjust, icmp-unreachable]>
                     led-schedules: <value of string>
                     led-state: <value in [disable, enable]>
                     lldp: <value in [disable, enable]>
                     login-passwd:
                       - <value of string>
                     login-passwd-change: <value in [no, yes, default]>
                     max-clients: <value of integer>
                     name: <value of string>
                     poe-mode: <value in [auto, 8023af, 8023at, ...]>
                     split-tunneling-acl:
                       -
                           dest-ip: <value of string>
                           id: <value of integer>
                     split-tunneling-acl-local-ap-subnet: <value in [disable, enable]>
                     split-tunneling-acl-path: <value in [tunnel, local]>
                     tun-mtu-downlink: <value of integer>
                     tun-mtu-uplink: <value of integer>
                     wan-port-mode: <value in [wan-lan, wan-only]>

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WTP-PROFILE
      fmgr_pm_config_obj_wireless_controller_wtp_profile:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [allowaccess, ap-country, ble-profile, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/wtp-profile</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> allowaccess </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ap-country </span> - Country in which this WTP, FortiAP or AP will operate (default = NA, automatically use the country configured for the current VDOM). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ble-profile </span> - Bluetooth Low Energy profile name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> comment </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> control-message-offload </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> deny-mac-list </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mac </span> - A WiFi device with this MAC address is denied access to this WTP, FortiAP or AP. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> dtls-in-kernel </span> - Enable/disable data channel DTLS in kernel. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dtls-policy </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> energy-efficient-ethernet </span> - Enable/disable use of energy efficient Ethernet on WTP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ext-info-enable </span> - Enable/disable station/VAP/radio extension information. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> handoff-roaming </span> - Enable/disable client load balancing during roaming to avoid roaming delay (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> handoff-rssi </span> - Minimum received signal strength indicator (RSSI) value for handoff (20 - 30, default = 25). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> handoff-sta-thresh </span> - Threshold value for AP handoff. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip-fragment-preventing </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> led-schedules </span> - Recurring firewall schedules for illuminating LEDs on the FortiAP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> led-state </span> - Enable/disable use of LEDs on WTP (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> lldp </span> - Enable/disable Link Layer Discovery Protocol (LLDP) for the WTP, FortiAP, or AP (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> login-passwd </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> login-passwd-change </span> - Change or reset the administrator password of a managed WTP, FortiAP or AP (yes, default, or no, default = no). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-clients </span> - Maximum number of stations (STAs) supported by the WTP (default = 0, meaning no client limitation). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> name </span> - WTP (or FortiAP or AP) profile name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> poe-mode </span> - Set the WTP, FortiAP, or APs PoE mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> split-tunneling-acl </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> dest-ip </span> - Destination IP and mask for the split-tunneling subnet. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> split-tunneling-acl-local-ap-subnet </span> - Enable/disable automatically adding local subnetwork of FortiAP to split-tunneling ACL (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> split-tunneling-acl-path </span> - Split tunneling ACL path is local/tunnel. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tun-mtu-downlink </span> - Downlink CAPWAP tunnel MTU (0, 576, or 1500 bytes, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> tun-mtu-uplink </span> - Uplink CAPWAP tunnel MTU (0, 576, or 1500 bytes, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> wan-port-mode </span> - Enable/disable using a WAN port as a LAN port. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/wtp-profile</span>  </li>
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



