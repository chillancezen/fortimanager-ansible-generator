:source: fmgr_pm_config_obj_wireless_controller_hotspot20_h2qp_wan_metric_h2qp_wan_metric.py

:orphan:

.. _fmgr_pm_config_obj_wireless_controller_hotspot20_h2qp_wan_metric_h2qp_wan_metric:

fmgr_pm_config_obj_wireless_controller_hotspot20_h2qp_wan_metric_h2qp_wan_metric -- Configure WAN metrics.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/wireless-controller/hotspot20/h2qp-wan-metric/{h2qp-wan-metric}`
- `/pm/config/global/obj/wireless-controller/hotspot20/h2qp-wan-metric/{h2qp-wan-metric}`
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
 <li><span class="li-head">h2qp-wan-metric</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure WAN metrics.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">downlink-load</span> - Downlink load. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">downlink-speed</span> - Downlink speed (in kilobits/s). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">link-at-capacity</span> - Link at capacity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">link-status</span> - Link status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [down, up, in-test]</span> </li>
 <li><span class="li-head">load-measurement-duration</span> - Load measurement duration (in tenths of a second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - WAN metric name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">symmetric-wan-link</span> - WAN link symmetry. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [asymmetric, symmetric]</span> </li>
 <li><span class="li-head">uplink-load</span> - Uplink load. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">uplink-speed</span> - Uplink speed (in kilobits/s). <span class="li-normal">type: int</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure WAN metrics.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure WAN metrics.</li>
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
    - name: send request to /pm/config/obj/wireless-controller/hotspot20/h2qp-wan-metric/{h2qp-wan-metric}
      fmgr_pm_config_obj_wireless_controller_hotspot20_h2qp_wan_metric_h2qp_wan_metric:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            h2qp-wan-metric: <value of string>
         params:
            - 
               data: 
                  downlink-load: <value of integer>
                  downlink-speed: <value of integer>
                  link-at-capacity: <value in [disable, enable]>
                  link-status: <value in [down, up, in-test]>
                  load-measurement-duration: <value of integer>
                  name: <value of string>
                  symmetric-wan-link: <value in [asymmetric, symmetric]>
                  uplink-load: <value of integer>
                  uplink-speed: <value of integer>
    - name: send request to /pm/config/obj/wireless-controller/hotspot20/h2qp-wan-metric/{h2qp-wan-metric}
      fmgr_pm_config_obj_wireless_controller_hotspot20_h2qp_wan_metric_h2qp_wan_metric:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            h2qp-wan-metric: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/hotspot20/h2qp-wan-metric/{h2qp-wan-metric}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> downlink-load </span> - Downlink load. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> downlink-speed </span> - Downlink speed (in kilobits/s). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> link-at-capacity </span> - Link at capacity. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> link-status </span> - Link status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> load-measurement-duration </span> - Load measurement duration (in tenths of a second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> name </span> - WAN metric name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> symmetric-wan-link </span> - WAN link symmetry. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> uplink-load </span> - Uplink load. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> uplink-speed </span> - Uplink speed (in kilobits/s). <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/hotspot20/h2qp-wan-metric/{h2qp-wan-metric}</span>  </li>
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



