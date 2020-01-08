:source: fmgr_pm_config_obj_wireless_controller_wtp_profile_radio_1.py

:orphan:

.. _fmgr_pm_config_obj_wireless_controller_wtp_profile_radio_1:

fmgr_pm_config_obj_wireless_controller_wtp_profile_radio_1 -- Configuration options for radio 1.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/radio-1`
- `/pm/config/global/obj/wireless-controller/wtp-profile/{wtp-profile}/radio-1`
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
 <li><span class="li-head">parameters for method: [get]</span> - Configuration options for radio 1.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Configuration options for radio 1.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">amsdu</span> - Enable/disable 802. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-handoff</span> - Enable/disable AP handoff of clients to other APs (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-addr</span> - MAC address to monitor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ap-sniffer-bufsize</span> - Sniffer buffer size (1 - 32 MB, default = 16). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-sniffer-chan</span> - Channel on which to operate the sniffer (default = 6). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-sniffer-ctl</span> - Enable/disable sniffer on WiFi control frame (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-data</span> - Enable/disable sniffer on WiFi data frame (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-mgmt-beacon</span> - Enable/disable sniffer on WiFi management Beacon frames (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-mgmt-other</span> - Enable/disable sniffer on WiFi management other frames  (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-sniffer-mgmt-probe</span> - Enable/disable sniffer on WiFi management probe frames (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auto-power-high</span> - Automatic transmit power high limit in dBm (the actual range of transmit power depends on the AP platform type). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">auto-power-level</span> - Enable/disable automatic power-level adjustment to prevent co-channel interference (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auto-power-low</span> - Automatic transmission power low limit in dBm (the actual range of transmit power depends on the AP platform type). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">band</span> - WiFi band that Radio 1 operates on. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [802.11b, 802.11a, 802.11g, 802.11n, 802.11ac, 802.11n-5G, 802.11g-only, 802.11n-only, 802.11n,g-only, 802.11ac-only, 802.11ac,n-only, 802.11n-5G-only]</span> </li>
 <li><span class="li-head">bandwidth-admission-control</span> - Enable/disable WiFi multimedia (WMM) bandwidth admission control to optimize WiFi bandwidth use. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">bandwidth-capacity</span> - Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">beacon-interval</span> - Beacon interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">call-admission-control</span> - Enable/disable WiFi multimedia (WMM) call admission control to optimize WiFi bandwidth use for VoIP calls. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">call-capacity</span> - Maximum number of Voice over WLAN (VoWLAN) phones supported by the radio (0 - 60, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">channel</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">channel-bonding</span> - Channel bandwidth: 80, 40, or 20MHz. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, 80MHz, 40MHz, 20MHz]</span> </li>
 <li><span class="li-head">channel-utilization</span> - Enable/disable measuring channel utilization. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">coexistence</span> - Enable/disable allowing both HT20 and HT40 on the same radio (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">darrp</span> - Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optimal channel (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dtim</span> - DTIM interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">frag-threshold</span> - Maximum packet size that can be sent without fragmentation (800 - 2346 bytes, default = 2346). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">frequency-handoff</span> - Enable/disable frequency handoff of clients to other channels (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-clients</span> - Maximum number of stations (STAs) or WiFi clients supported by the radio. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-distance</span> - Maximum expected distance between the AP and clients (0 - 54000 m, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mode</span> - Mode of radio 1. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, ap, monitor, sniffer]</span> </li>
 <li><span class="li-head">power-level</span> - Radio power level as a percentage of the maximum transmit power (0 - 100, default = 100). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">powersave-optimize</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [tim, ac-vo, no-obss-scan, no-11b-rate, client-rate-follow]</span> </li>
 </ul>
 <li><span class="li-head">protection-mode</span> - Enable/disable 802. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rtscts, ctsonly, disable]</span> </li>
 <li><span class="li-head">radio-id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rts-threshold</span> - Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS (256 - 2346 bytes, default = 2346). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">short-guard-interval</span> - Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">spectrum-analysis</span> - Enable/disable spectrum analysis to find interference that would negatively impact wireless performance. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">transmit-optimize</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, power-save, aggr-limit, retry-limit, send-bar]</span> </li>
 </ul>
 <li><span class="li-head">vap-all</span> - Enable/disable the automatic inheritance of all Virtual Access Points (VAPs) (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">vaps</span> - Manually selected list of Virtual Access Points (VAPs). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wids-profile</span> - Wireless Intrusion Detection System (WIDS) profile name to assign to the radio. <span class="li-normal">type: str</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WTP-PROFILE/{WTP-PROFILE}/RADIO-1
      fmgr_pm_config_obj_wireless_controller_wtp_profile_radio_1:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wtp-profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WTP-PROFILE/{WTP-PROFILE}/RADIO-1
      fmgr_pm_config_obj_wireless_controller_wtp_profile_radio_1:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wtp-profile: <value of string>
         params:
            -
               data:
                  amsdu: <value in [disable, enable]>
                  ap-handoff: <value in [disable, enable]>
                  ap-sniffer-addr: <value of string>
                  ap-sniffer-bufsize: <value of integer>
                  ap-sniffer-chan: <value of integer>
                  ap-sniffer-ctl: <value in [disable, enable]>
                  ap-sniffer-data: <value in [disable, enable]>
                  ap-sniffer-mgmt-beacon: <value in [disable, enable]>
                  ap-sniffer-mgmt-other: <value in [disable, enable]>
                  ap-sniffer-mgmt-probe: <value in [disable, enable]>
                  auto-power-high: <value of integer>
                  auto-power-level: <value in [disable, enable]>
                  auto-power-low: <value of integer>
                  band: <value in [802.11b, 802.11a, 802.11g, ...]>
                  bandwidth-admission-control: <value in [disable, enable]>
                  bandwidth-capacity: <value of integer>
                  beacon-interval: <value of integer>
                  call-admission-control: <value in [disable, enable]>
                  call-capacity: <value of integer>
                  channel:
                    - <value of string>
                  channel-bonding: <value in [disable, enable, 80MHz, ...]>
                  channel-utilization: <value in [disable, enable]>
                  coexistence: <value in [disable, enable]>
                  darrp: <value in [disable, enable]>
                  dtim: <value of integer>
                  frag-threshold: <value of integer>
                  frequency-handoff: <value in [disable, enable]>
                  max-clients: <value of integer>
                  max-distance: <value of integer>
                  mode: <value in [disabled, ap, monitor, ...]>
                  power-level: <value of integer>
                  powersave-optimize:
                    - <value in [tim, ac-vo, no-obss-scan, ...]>
                  protection-mode: <value in [rtscts, ctsonly, disable]>
                  radio-id: <value of integer>
                  rts-threshold: <value of integer>
                  short-guard-interval: <value in [disable, enable]>
                  spectrum-analysis: <value in [disable, enable]>
                  transmit-optimize:
                    - <value in [disable, power-save, aggr-limit, ...]>
                  vap-all: <value in [disable, enable]>
                  vaps: <value of string>
                  wids-profile: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> amsdu </span> - Enable/disable 802. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ap-handoff </span> - Enable/disable AP handoff of clients to other APs (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ap-sniffer-addr </span> - MAC address to monitor. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ap-sniffer-bufsize </span> - Sniffer buffer size (1 - 32 MB, default = 16). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ap-sniffer-chan </span> - Channel on which to operate the sniffer (default = 6). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ap-sniffer-ctl </span> - Enable/disable sniffer on WiFi control frame (default = enable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ap-sniffer-data </span> - Enable/disable sniffer on WiFi data frame (default = enable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ap-sniffer-mgmt-beacon </span> - Enable/disable sniffer on WiFi management Beacon frames (default = enable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ap-sniffer-mgmt-other </span> - Enable/disable sniffer on WiFi management other frames  (default = enable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ap-sniffer-mgmt-probe </span> - Enable/disable sniffer on WiFi management probe frames (default = enable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auto-power-high </span> - Automatic transmit power high limit in dBm (the actual range of transmit power depends on the AP platform type). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> auto-power-level </span> - Enable/disable automatic power-level adjustment to prevent co-channel interference (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auto-power-low </span> - Automatic transmission power low limit in dBm (the actual range of transmit power depends on the AP platform type). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> band </span> - WiFi band that Radio 1 operates on. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> bandwidth-admission-control </span> - Enable/disable WiFi multimedia (WMM) bandwidth admission control to optimize WiFi bandwidth use. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> bandwidth-capacity </span> - Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> beacon-interval </span> - Beacon interval. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> call-admission-control </span> - Enable/disable WiFi multimedia (WMM) call admission control to optimize WiFi bandwidth use for VoIP calls. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> call-capacity </span> - Maximum number of Voice over WLAN (VoWLAN) phones supported by the radio (0 - 60, default = 10). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> channel </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> channel-bonding </span> - Channel bandwidth: 80, 40, or 20MHz. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> channel-utilization </span> - Enable/disable measuring channel utilization. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> coexistence </span> - Enable/disable allowing both HT20 and HT40 on the same radio (default = enable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> darrp </span> - Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optimal channel (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dtim </span> - DTIM interval. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> frag-threshold </span> - Maximum packet size that can be sent without fragmentation (800 - 2346 bytes, default = 2346). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> frequency-handoff </span> - Enable/disable frequency handoff of clients to other channels (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-clients </span> - Maximum number of stations (STAs) or WiFi clients supported by the radio. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> max-distance </span> - Maximum expected distance between the AP and clients (0 - 54000 m, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mode </span> - Mode of radio 1. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> power-level </span> - Radio power level as a percentage of the maximum transmit power (0 - 100, default = 100). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> powersave-optimize </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> protection-mode </span> - Enable/disable 802. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> radio-id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> rts-threshold </span> - Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS (256 - 2346 bytes, default = 2346). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> short-guard-interval </span> - Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spectrum-analysis </span> - Enable/disable spectrum analysis to find interference that would negatively impact wireless performance. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> transmit-optimize </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> vap-all </span> - Enable/disable the automatic inheritance of all Virtual Access Points (VAPs) (default = enable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vaps </span> - Manually selected list of Virtual Access Points (VAPs). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wids-profile </span> - Wireless Intrusion Detection System (WIDS) profile name to assign to the radio. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/radio-1</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/radio-1</span>  </li>
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



