:source: fmgr_qosprofile_obj.py

:orphan:

.. _fmgr_qosprofile_obj:

fmgr_qosprofile_obj -- Configure WiFi quality of service (QoS) profiles.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/wireless-controller/qos-profile/{qos-profile}`
- `/pm/config/global/obj/wireless-controller/qos-profile/{qos-profile}`
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
 <li><span class="li-head">qos-profile</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure WiFi quality of service (QoS) profiles.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">bandwidth-admission-control</span> - Enable/disable WMM bandwidth admission control. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">bandwidth-capacity</span> - Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">burst</span> - Enable/disable client rate burst. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">call-admission-control</span> - Enable/disable WMM call admission control. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">call-capacity</span> - Maximum number of Voice over WLAN (VoWLAN) phones allowed (0 - 60, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">downlink</span> - Maximum downlink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">downlink-sta</span> - Maximum downlink bandwidth for clients (0 - 2097152 Kbps, default = 0, 0 means no limit). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dscp-wmm-be</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">dscp-wmm-bk</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">dscp-wmm-mapping</span> - Enable/disable Differentiated Services Code Point (DSCP) mapping. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dscp-wmm-vi</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">dscp-wmm-vo</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">name</span> - WiFi QoS profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">uplink</span> - Maximum uplink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">uplink-sta</span> - Maximum uplink bandwidth for clients (0 - 2097152 Kbps, default = 0, 0 means no limit). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">wmm</span> - Enable/disable WiFi multi-media (WMM) control. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wmm-uapsd</span> - Enable/disable WMM Unscheduled Automatic Power Save Delivery (U-APSD) power save mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure WiFi quality of service (QoS) profiles.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure WiFi quality of service (QoS) profiles.</li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/QOS-PROFILE/{QOS-PROFILE}
      fmgr_qosprofile_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            qos-profile: <value of string>
         params:
            -
               data:
                  bandwidth-admission-control: <value in [disable, enable]>
                  bandwidth-capacity: <value of integer>
                  burst: <value in [disable, enable]>
                  call-admission-control: <value in [disable, enable]>
                  call-capacity: <value of integer>
                  comment: <value of string>
                  downlink: <value of integer>
                  downlink-sta: <value of integer>
                  dscp-wmm-be:
                    - <value of integer>
                  dscp-wmm-bk:
                    - <value of integer>
                  dscp-wmm-mapping: <value in [disable, enable]>
                  dscp-wmm-vi:
                    - <value of integer>
                  dscp-wmm-vo:
                    - <value of integer>
                  name: <value of string>
                  uplink: <value of integer>
                  uplink-sta: <value of integer>
                  wmm: <value in [disable, enable]>
                  wmm-uapsd: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/QOS-PROFILE/{QOS-PROFILE}
      fmgr_qosprofile_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            qos-profile: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/qos-profile/{qos-profile}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> bandwidth-admission-control </span> - Enable/disable WMM bandwidth admission control. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> bandwidth-capacity </span> - Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> burst </span> - Enable/disable client rate burst. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> call-admission-control </span> - Enable/disable WMM call admission control. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> call-capacity </span> - Maximum number of Voice over WLAN (VoWLAN) phones allowed (0 - 60, default = 10). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comment </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> downlink </span> - Maximum downlink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> downlink-sta </span> - Maximum downlink bandwidth for clients (0 - 2097152 Kbps, default = 0, 0 means no limit). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> dscp-wmm-be </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> dscp-wmm-bk </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> dscp-wmm-mapping </span> - Enable/disable Differentiated Services Code Point (DSCP) mapping. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dscp-wmm-vi </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> dscp-wmm-vo </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> name </span> - WiFi QoS profile name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> uplink </span> - Maximum uplink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> uplink-sta </span> - Maximum uplink bandwidth for clients (0 - 2097152 Kbps, default = 0, 0 means no limit). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> wmm </span> - Enable/disable WiFi multi-media (WMM) control. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wmm-uapsd </span> - Enable/disable WMM Unscheduled Automatic Power Save Delivery (U-APSD) power save mode. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/qos-profile/{qos-profile}</span>  </li>
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



