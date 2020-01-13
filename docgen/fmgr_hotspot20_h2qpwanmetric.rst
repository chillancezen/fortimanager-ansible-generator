:source: fmgr_hotspot20_h2qpwanmetric.py

:orphan:

.. _fmgr_hotspot20_h2qpwanmetric:

fmgr_hotspot20_h2qpwanmetric -- Configure WAN metrics.
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/wireless-controller/hotspot20/h2qp-wan-metric`
- `/pm/config/global/obj/wireless-controller/hotspot20/h2qp-wan-metric`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure WAN metrics.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
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
 <li><span class="li-head">parameters for method: [get]</span> - Configure WAN metrics.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [downlink-load, downlink-speed, link-at-capacity, link-status, load-measurement-duration, name, symmetric-wan-link, uplink-load, uplink-speed]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/HOTSPOT20/H2QP-WAN-METRIC
      fmgr_hotspot20_h2qpwanmetric:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     downlink-load: <value of integer>
                     downlink-speed: <value of integer>
                     link-at-capacity: <value in [disable, enable]>
                     link-status: <value in [down, up, in-test]>
                     load-measurement-duration: <value of integer>
                     name: <value of string>
                     symmetric-wan-link: <value in [asymmetric, symmetric]>
                     uplink-load: <value of integer>
                     uplink-speed: <value of integer>

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/HOTSPOT20/H2QP-WAN-METRIC
      fmgr_hotspot20_h2qpwanmetric:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [downlink-load, downlink-speed, link-at-capacity, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/hotspot20/h2qp-wan-metric</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/hotspot20/h2qp-wan-metric</span>  </li>
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



