:source: fmgr_pm_config_obj_wireless_controller_wtp_profile_lbs.py

:orphan:

.. _fmgr_pm_config_obj_wireless_controller_wtp_profile_lbs:

fmgr_pm_config_obj_wireless_controller_wtp_profile_lbs -- Set various location based service (LBS) options.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/lbs`
- `/pm/config/global/obj/wireless-controller/wtp-profile/{wtp-profile}/lbs`
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
 <li><span class="li-head">wtp-profile</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Set various location based service (LBS) options.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Set various location based service (LBS) options.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">aeroscout</span> - Enable/disable AeroScout Real Time Location Service (RTLS) support. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">aeroscout-ap-mac</span> - Use BSSID or board MAC address as AP MAC address in the Aeroscout AP message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bssid, board-mac]</span> </li>
 <li><span class="li-head">aeroscout-mmu-report</span> - Enable/disable MU compounded report. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">aeroscout-mu</span> - Enable/disable AeroScout support. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">aeroscout-mu-factor</span> - AeroScout Mobile Unit (MU) mode dilution factor (default = 20). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">aeroscout-mu-timeout</span> - AeroScout MU mode timeout (0 - 65535 sec, default = 5). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">aeroscout-server-ip</span> - IP address of AeroScout server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">aeroscout-server-port</span> - AeroScout server UDP listening port. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ekahau-blink-mode</span> - Enable/disable Ekahua blink mode (also called AiRISTA Flow Blink Mode) to find the location of devices connected to a wireless LAN (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ekahau-tag</span> - WiFi frame MAC address or WiFi Tag. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">erc-server-ip</span> - IP address of Ekahua RTLS Controller (ERC). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">erc-server-port</span> - Ekahua RTLS Controller (ERC) UDP listening port. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fortipresence</span> - Enable/disable FortiPresence to monitor the location and activity of WiFi clients even if they dont connect to this WiFi network (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, enable2, foreign, both]</span> </li>
 <li><span class="li-head">fortipresence-frequency</span> - FortiPresence report transmit frequency (5 - 65535 sec, default = 30). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fortipresence-port</span> - FortiPresence server UDP listening port (default = 3000). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fortipresence-project</span> - FortiPresence project name (max. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fortipresence-rogue</span> - Enable/disable FortiPresence finding and reporting rogue APs. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fortipresence-secret</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">fortipresence-server</span> - FortiPresence server IP address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fortipresence-unassoc</span> - Enable/disable FortiPresence finding and reporting unassociated stations. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">station-locate</span> - Enable/disable client station locating services for all clients, whether associated or not (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WTP-PROFILE/{WTP-PROFILE}/LBS
      fmgr_pm_config_obj_wireless_controller_wtp_profile_lbs:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wtp-profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WTP-PROFILE/{WTP-PROFILE}/LBS
      fmgr_pm_config_obj_wireless_controller_wtp_profile_lbs:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wtp-profile: <value of string>
         params:
            -
               data:
                  aeroscout: <value in [disable, enable]>
                  aeroscout-ap-mac: <value in [bssid, board-mac]>
                  aeroscout-mmu-report: <value in [disable, enable]>
                  aeroscout-mu: <value in [disable, enable]>
                  aeroscout-mu-factor: <value of integer>
                  aeroscout-mu-timeout: <value of integer>
                  aeroscout-server-ip: <value of string>
                  aeroscout-server-port: <value of integer>
                  ekahau-blink-mode: <value in [disable, enable]>
                  ekahau-tag: <value of string>
                  erc-server-ip: <value of string>
                  erc-server-port: <value of integer>
                  fortipresence: <value in [disable, enable, enable2, ...]>
                  fortipresence-frequency: <value of integer>
                  fortipresence-port: <value of integer>
                  fortipresence-project: <value of string>
                  fortipresence-rogue: <value in [disable, enable]>
                  fortipresence-secret:
                    - <value of string>
                  fortipresence-server: <value of string>
                  fortipresence-unassoc: <value in [disable, enable]>
                  station-locate: <value in [disable, enable]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> aeroscout </span> - Enable/disable AeroScout Real Time Location Service (RTLS) support. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> aeroscout-ap-mac </span> - Use BSSID or board MAC address as AP MAC address in the Aeroscout AP message. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> aeroscout-mmu-report </span> - Enable/disable MU compounded report. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> aeroscout-mu </span> - Enable/disable AeroScout support. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> aeroscout-mu-factor </span> - AeroScout Mobile Unit (MU) mode dilution factor (default = 20). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> aeroscout-mu-timeout </span> - AeroScout MU mode timeout (0 - 65535 sec, default = 5). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> aeroscout-server-ip </span> - IP address of AeroScout server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> aeroscout-server-port </span> - AeroScout server UDP listening port. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ekahau-blink-mode </span> - Enable/disable Ekahua blink mode (also called AiRISTA Flow Blink Mode) to find the location of devices connected to a wireless LAN (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ekahau-tag </span> - WiFi frame MAC address or WiFi Tag. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> erc-server-ip </span> - IP address of Ekahua RTLS Controller (ERC). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> erc-server-port </span> - Ekahua RTLS Controller (ERC) UDP listening port. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> fortipresence </span> - Enable/disable FortiPresence to monitor the location and activity of WiFi clients even if they dont connect to this WiFi network (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fortipresence-frequency </span> - FortiPresence report transmit frequency (5 - 65535 sec, default = 30). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> fortipresence-port </span> - FortiPresence server UDP listening port (default = 3000). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> fortipresence-project </span> - FortiPresence project name (max. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fortipresence-rogue </span> - Enable/disable FortiPresence finding and reporting rogue APs. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fortipresence-secret </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> fortipresence-server </span> - FortiPresence server IP address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fortipresence-unassoc </span> - Enable/disable FortiPresence finding and reporting unassociated stations. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> station-locate </span> - Enable/disable client station locating services for all clients, whether associated or not (default = disable). <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/lbs</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/lbs</span>  </li>
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



