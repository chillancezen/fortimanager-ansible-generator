:source: fmgr_wtpprofile_lan.py

:orphan:

.. _fmgr_wtpprofile_lan:

fmgr_wtpprofile_lan -- WTP LAN port mapping.
++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/lan`
- `/pm/config/global/obj/wireless-controller/wtp-profile/{wtp-profile}/lan`
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
 <li><span class="li-head">parameters for method: [get]</span> - WTP LAN port mapping.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - WTP LAN port mapping.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">port-mode</span> - LAN port mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port-ssid</span> - Bridge LAN port to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port1-mode</span> - LAN port 1 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port1-ssid</span> - Bridge LAN port 1 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port2-mode</span> - LAN port 2 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port2-ssid</span> - Bridge LAN port 2 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port3-mode</span> - LAN port 3 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port3-ssid</span> - Bridge LAN port 3 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port4-mode</span> - LAN port 4 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port4-ssid</span> - Bridge LAN port 4 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port5-mode</span> - LAN port 5 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port5-ssid</span> - Bridge LAN port 5 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port6-mode</span> - LAN port 6 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port6-ssid</span> - Bridge LAN port 6 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port7-mode</span> - LAN port 7 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port7-ssid</span> - Bridge LAN port 7 to SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port8-mode</span> - LAN port 8 mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [offline, bridge-to-wan, bridge-to-ssid, nat-to-wan]</span> </li>
 <li><span class="li-head">port8-ssid</span> - Bridge LAN port 8 to SSID. <span class="li-normal">type: str</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WTP-PROFILE/{WTP-PROFILE}/LAN
      fmgr_wtpprofile_lan:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wtp-profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WTP-PROFILE/{WTP-PROFILE}/LAN
      fmgr_wtpprofile_lan:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wtp-profile: <value of string>
         params:
            -
               data:
                  port-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
                  port-ssid: <value of string>
                  port1-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
                  port1-ssid: <value of string>
                  port2-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
                  port2-ssid: <value of string>
                  port3-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
                  port3-ssid: <value of string>
                  port4-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
                  port4-ssid: <value of string>
                  port5-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
                  port5-ssid: <value of string>
                  port6-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
                  port6-ssid: <value of string>
                  port7-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
                  port7-ssid: <value of string>
                  port8-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
                  port8-ssid: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> port-mode </span> - LAN port mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port-ssid </span> - Bridge LAN port to SSID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port1-mode </span> - LAN port 1 mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port1-ssid </span> - Bridge LAN port 1 to SSID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port2-mode </span> - LAN port 2 mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port2-ssid </span> - Bridge LAN port 2 to SSID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port3-mode </span> - LAN port 3 mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port3-ssid </span> - Bridge LAN port 3 to SSID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port4-mode </span> - LAN port 4 mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port4-ssid </span> - Bridge LAN port 4 to SSID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port5-mode </span> - LAN port 5 mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port5-ssid </span> - Bridge LAN port 5 to SSID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port6-mode </span> - LAN port 6 mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port6-ssid </span> - Bridge LAN port 6 to SSID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port7-mode </span> - LAN port 7 mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port7-ssid </span> - Bridge LAN port 7 to SSID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port8-mode </span> - LAN port 8 mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port8-ssid </span> - Bridge LAN port 8 to SSID. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/lan</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/lan</span>  </li>
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



