:source: fmgr_pm_config_obj_wireless_controller_wids_profile.py

:orphan:

.. _fmgr_pm_config_obj_wireless_controller_wids_profile:

fmgr_pm_config_obj_wireless_controller_wids_profile -- Configure wireless intrusion detection system (WIDS) profiles.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/wireless-controller/wids-profile`
- `/pm/config/global/obj/wireless-controller/wids-profile`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure wireless intrusion detection system (WIDS) profiles.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">ap-auto-suppress</span> - Enable/disable on-wire rogue AP auto-suppression (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-bgscan-disable-day</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sunday, monday, tuesday, wednesday, thursday, friday, saturday]</span> </li>
 </ul>
 <li><span class="li-head">ap-bgscan-disable-end</span> - End time, using a 24-hour clock in the format of hh:mm, for disabling background scanning (default = 00:00). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ap-bgscan-disable-start</span> - Start time, using a 24-hour clock in the format of hh:mm, for disabling background scanning (default = 00:00). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ap-bgscan-duration</span> - Listening time on a scanning channel (10 - 1000 msec, default = 20). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-bgscan-idle</span> - Waiting time for channel inactivity before scanning this channel (0 - 1000 msec, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-bgscan-intv</span> - Period of time between scanning two channels (1 - 600 sec, default = 1). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-bgscan-period</span> - Period of time between background scans (60 - 3600 sec, default = 600). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-bgscan-report-intv</span> - Period of time between background scan reports (15 - 600 sec, default = 30). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-fgscan-report-intv</span> - Period of time between foreground scan reports (15 - 600 sec, default = 15). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ap-scan</span> - Enable/disable rogue AP detection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ap-scan-passive</span> - Enable/disable passive scanning. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">asleap-attack</span> - Enable/disable asleap attack detection (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">assoc-flood-thresh</span> - The threshold value for association frame flooding. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">assoc-flood-time</span> - Number of seconds after which a station is considered not connected. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">assoc-frame-flood</span> - Enable/disable association frame flooding detection (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auth-flood-thresh</span> - The threshold value for authentication frame flooding. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">auth-flood-time</span> - Number of seconds after which a station is considered not connected. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">auth-frame-flood</span> - Enable/disable authentication frame flooding detection (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">deauth-broadcast</span> - Enable/disable broadcasting de-authentication detection (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">deauth-unknown-src-thresh</span> - Threshold value per second to deauth unknown src for DoS attack (0: no limit). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-fail-flood</span> - Enable/disable EAPOL-Failure flooding (to AP) detection (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">eapol-fail-intv</span> - The detection interval for EAPOL-Failure flooding (1 - 3600 sec). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-fail-thresh</span> - The threshold value for EAPOL-Failure flooding in specified interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-logoff-flood</span> - Enable/disable EAPOL-Logoff flooding (to AP) detection (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">eapol-logoff-intv</span> - The detection interval for EAPOL-Logoff flooding (1 - 3600 sec). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-logoff-thresh</span> - The threshold value for EAPOL-Logoff flooding in specified interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-pre-fail-flood</span> - Enable/disable premature EAPOL-Failure flooding (to STA) detection (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">eapol-pre-fail-intv</span> - The detection interval for premature EAPOL-Failure flooding (1 - 3600 sec). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-pre-fail-thresh</span> - The threshold value for premature EAPOL-Failure flooding in specified interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-pre-succ-flood</span> - Enable/disable premature EAPOL-Success flooding (to STA) detection (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">eapol-pre-succ-intv</span> - The detection interval for premature EAPOL-Success flooding (1 - 3600 sec). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-pre-succ-thresh</span> - The threshold value for premature EAPOL-Success flooding in specified interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-start-flood</span> - Enable/disable EAPOL-Start flooding (to AP) detection (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">eapol-start-intv</span> - The detection interval for EAPOL-Start flooding (1 - 3600 sec). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-start-thresh</span> - The threshold value for EAPOL-Start flooding in specified interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-succ-flood</span> - Enable/disable EAPOL-Success flooding (to AP) detection (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">eapol-succ-intv</span> - The detection interval for EAPOL-Success flooding (1 - 3600 sec). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-succ-thresh</span> - The threshold value for EAPOL-Success flooding in specified interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">invalid-mac-oui</span> - Enable/disable invalid MAC OUI detection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">long-duration-attack</span> - Enable/disable long duration attack detection based on user configured threshold (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">long-duration-thresh</span> - Threshold value for long duration attack detection (1000 - 32767 usec, default = 8200). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - WIDS profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">null-ssid-probe-resp</span> - Enable/disable null SSID probe response detection (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sensor-mode</span> - Scan WiFi nearby stations (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, foreign, both]</span> </li>
 <li><span class="li-head">spoofed-deauth</span> - Enable/disable spoofed de-authentication attack detection (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">weak-wep-iv</span> - Enable/disable weak WEP IV (Initialization Vector) detection (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wireless-bridge</span> - Enable/disable wireless bridge detection (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure wireless intrusion detection system (WIDS) profiles.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ap-auto-suppress, ap-bgscan-disable-day, ap-bgscan-disable-end, ap-bgscan-disable-start, ap-bgscan-duration, ap-bgscan-idle, ap-bgscan-intv, ap-bgscan-period, ap-bgscan-report-intv, ap-fgscan-report-intv, ap-scan, ap-scan-passive, asleap-attack, assoc-flood-thresh, assoc-flood-time, assoc-frame-flood, auth-flood-thresh, auth-flood-time, auth-frame-flood, comment, deauth-broadcast, deauth-unknown-src-thresh, eapol-fail-flood, eapol-fail-intv, eapol-fail-thresh, eapol-logoff-flood, eapol-logoff-intv, eapol-logoff-thresh, eapol-pre-fail-flood, eapol-pre-fail-intv, eapol-pre-fail-thresh, eapol-pre-succ-flood, eapol-pre-succ-intv, eapol-pre-succ-thresh, eapol-start-flood, eapol-start-intv, eapol-start-thresh, eapol-succ-flood, eapol-succ-intv, eapol-succ-thresh, invalid-mac-oui, long-duration-attack, long-duration-thresh, name, null-ssid-probe-resp, sensor-mode, spoofed-deauth, weak-wep-iv, wireless-bridge]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WIDS-PROFILE
      fmgr_pm_config_obj_wireless_controller_wids_profile:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     ap-auto-suppress: <value in [disable, enable]>
                     ap-bgscan-disable-day:
                       - <value in [sunday, monday, tuesday, ...]>
                     ap-bgscan-disable-end: <value of string>
                     ap-bgscan-disable-start: <value of string>
                     ap-bgscan-duration: <value of integer>
                     ap-bgscan-idle: <value of integer>
                     ap-bgscan-intv: <value of integer>
                     ap-bgscan-period: <value of integer>
                     ap-bgscan-report-intv: <value of integer>
                     ap-fgscan-report-intv: <value of integer>
                     ap-scan: <value in [disable, enable]>
                     ap-scan-passive: <value in [disable, enable]>
                     asleap-attack: <value in [disable, enable]>
                     assoc-flood-thresh: <value of integer>
                     assoc-flood-time: <value of integer>
                     assoc-frame-flood: <value in [disable, enable]>
                     auth-flood-thresh: <value of integer>
                     auth-flood-time: <value of integer>
                     auth-frame-flood: <value in [disable, enable]>
                     comment: <value of string>
                     deauth-broadcast: <value in [disable, enable]>
                     deauth-unknown-src-thresh: <value of integer>
                     eapol-fail-flood: <value in [disable, enable]>
                     eapol-fail-intv: <value of integer>
                     eapol-fail-thresh: <value of integer>
                     eapol-logoff-flood: <value in [disable, enable]>
                     eapol-logoff-intv: <value of integer>
                     eapol-logoff-thresh: <value of integer>
                     eapol-pre-fail-flood: <value in [disable, enable]>
                     eapol-pre-fail-intv: <value of integer>
                     eapol-pre-fail-thresh: <value of integer>
                     eapol-pre-succ-flood: <value in [disable, enable]>
                     eapol-pre-succ-intv: <value of integer>
                     eapol-pre-succ-thresh: <value of integer>
                     eapol-start-flood: <value in [disable, enable]>
                     eapol-start-intv: <value of integer>
                     eapol-start-thresh: <value of integer>
                     eapol-succ-flood: <value in [disable, enable]>
                     eapol-succ-intv: <value of integer>
                     eapol-succ-thresh: <value of integer>
                     invalid-mac-oui: <value in [disable, enable]>
                     long-duration-attack: <value in [disable, enable]>
                     long-duration-thresh: <value of integer>
                     name: <value of string>
                     null-ssid-probe-resp: <value in [disable, enable]>
                     sensor-mode: <value in [disable, foreign, both]>
                     spoofed-deauth: <value in [disable, enable]>
                     weak-wep-iv: <value in [disable, enable]>
                     wireless-bridge: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WIDS-PROFILE
      fmgr_pm_config_obj_wireless_controller_wids_profile:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [ap-auto-suppress, ap-bgscan-disable-day, ap-bgscan-disable-end, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/wids-profile</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> ap-auto-suppress </span> - Enable/disable on-wire rogue AP auto-suppression (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ap-bgscan-disable-day </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ap-bgscan-disable-end </span> - End time, using a 24-hour clock in the format of hh:mm, for disabling background scanning (default = 00:00). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ap-bgscan-disable-start </span> - Start time, using a 24-hour clock in the format of hh:mm, for disabling background scanning (default = 00:00). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ap-bgscan-duration </span> - Listening time on a scanning channel (10 - 1000 msec, default = 20). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ap-bgscan-idle </span> - Waiting time for channel inactivity before scanning this channel (0 - 1000 msec, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ap-bgscan-intv </span> - Period of time between scanning two channels (1 - 600 sec, default = 1). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ap-bgscan-period </span> - Period of time between background scans (60 - 3600 sec, default = 600). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ap-bgscan-report-intv </span> - Period of time between background scan reports (15 - 600 sec, default = 30). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ap-fgscan-report-intv </span> - Period of time between foreground scan reports (15 - 600 sec, default = 15). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ap-scan </span> - Enable/disable rogue AP detection. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ap-scan-passive </span> - Enable/disable passive scanning. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> asleap-attack </span> - Enable/disable asleap attack detection (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> assoc-flood-thresh </span> - The threshold value for association frame flooding. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> assoc-flood-time </span> - Number of seconds after which a station is considered not connected. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> assoc-frame-flood </span> - Enable/disable association frame flooding detection (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auth-flood-thresh </span> - The threshold value for authentication frame flooding. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> auth-flood-time </span> - Number of seconds after which a station is considered not connected. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> auth-frame-flood </span> - Enable/disable authentication frame flooding detection (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> comment </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> deauth-broadcast </span> - Enable/disable broadcasting de-authentication detection (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> deauth-unknown-src-thresh </span> - Threshold value per second to deauth unknown src for DoS attack (0: no limit). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> eapol-fail-flood </span> - Enable/disable EAPOL-Failure flooding (to AP) detection (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> eapol-fail-intv </span> - The detection interval for EAPOL-Failure flooding (1 - 3600 sec). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> eapol-fail-thresh </span> - The threshold value for EAPOL-Failure flooding in specified interval. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> eapol-logoff-flood </span> - Enable/disable EAPOL-Logoff flooding (to AP) detection (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> eapol-logoff-intv </span> - The detection interval for EAPOL-Logoff flooding (1 - 3600 sec). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> eapol-logoff-thresh </span> - The threshold value for EAPOL-Logoff flooding in specified interval. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> eapol-pre-fail-flood </span> - Enable/disable premature EAPOL-Failure flooding (to STA) detection (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> eapol-pre-fail-intv </span> - The detection interval for premature EAPOL-Failure flooding (1 - 3600 sec). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> eapol-pre-fail-thresh </span> - The threshold value for premature EAPOL-Failure flooding in specified interval. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> eapol-pre-succ-flood </span> - Enable/disable premature EAPOL-Success flooding (to STA) detection (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> eapol-pre-succ-intv </span> - The detection interval for premature EAPOL-Success flooding (1 - 3600 sec). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> eapol-pre-succ-thresh </span> - The threshold value for premature EAPOL-Success flooding in specified interval. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> eapol-start-flood </span> - Enable/disable EAPOL-Start flooding (to AP) detection (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> eapol-start-intv </span> - The detection interval for EAPOL-Start flooding (1 - 3600 sec). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> eapol-start-thresh </span> - The threshold value for EAPOL-Start flooding in specified interval. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> eapol-succ-flood </span> - Enable/disable EAPOL-Success flooding (to AP) detection (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> eapol-succ-intv </span> - The detection interval for EAPOL-Success flooding (1 - 3600 sec). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> eapol-succ-thresh </span> - The threshold value for EAPOL-Success flooding in specified interval. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> invalid-mac-oui </span> - Enable/disable invalid MAC OUI detection. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> long-duration-attack </span> - Enable/disable long duration attack detection based on user configured threshold (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> long-duration-thresh </span> - Threshold value for long duration attack detection (1000 - 32767 usec, default = 8200). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> name </span> - WIDS profile name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> null-ssid-probe-resp </span> - Enable/disable null SSID probe response detection (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sensor-mode </span> - Scan WiFi nearby stations (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spoofed-deauth </span> - Enable/disable spoofed de-authentication attack detection (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> weak-wep-iv </span> - Enable/disable weak WEP IV (Initialization Vector) detection (default = disable). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wireless-bridge </span> - Enable/disable wireless bridge detection (default = disable). <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/wids-profile</span>  </li>
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



