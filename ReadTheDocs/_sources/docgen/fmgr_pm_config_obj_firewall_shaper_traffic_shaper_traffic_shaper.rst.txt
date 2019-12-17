:source: fmgr_pm_config_obj_firewall_shaper_traffic_shaper_traffic_shaper.py

:orphan:

.. _fmgr_pm_config_obj_firewall_shaper_traffic_shaper_traffic_shaper:

fmgr_pm_config_obj_firewall_shaper_traffic_shaper_traffic_shaper -- Configure shared traffic shaper.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/shaper/traffic-shaper/{traffic-shaper}`
- `/pm/config/global/obj/firewall/shaper/traffic-shaper/{traffic-shaper}`
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
 <li><span class="li-head">traffic-shaper</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure shared traffic shaper.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">bandwidth-unit</span> - Unit of measurement for guaranteed and maximum bandwidth for this shaper (Kbps, Mbps or Gbps). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [kbps, mbps, gbps]</span> </li>
 <li><span class="li-head">diffserv</span> - Enable/disable changing the DiffServ setting applied to traffic accepted by this shaper. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">diffservcode</span> - DiffServ setting to be applied to traffic accepted by this shaper. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">guaranteed-bandwidth</span> - Amount of bandwidth guaranteed for this shaper (0 - 16776000). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">maximum-bandwidth</span> - Upper bandwidth limit enforced by this shaper (0 - 16776000). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - Traffic shaper name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">per-policy</span> - Enable/disable applying a separate shaper for each policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">priority</span> - Higher priority traffic is more likely to be forwarded without delays and without compromising the guaranteed bandwidth. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [high, medium, low]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure shared traffic shaper.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure shared traffic shaper.</li>
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
    - name: send request to /pm/config/obj/firewall/shaper/traffic-shaper/{traffic-shaper}
      fmgr_pm_config_obj_firewall_shaper_traffic_shaper_traffic_shaper:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            traffic-shaper: <value of string>
         params:
            - 
               data: 
                  bandwidth-unit: <value in [kbps, mbps, gbps]>
                  diffserv: <value in [disable, enable]>
                  diffservcode: <value of string>
                  guaranteed-bandwidth: <value of integer>
                  maximum-bandwidth: <value of integer>
                  name: <value of string>
                  per-policy: <value in [disable, enable]>
                  priority: <value in [high, medium, low]>
    - name: send request to /pm/config/obj/firewall/shaper/traffic-shaper/{traffic-shaper}
      fmgr_pm_config_obj_firewall_shaper_traffic_shaper_traffic_shaper:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            traffic-shaper: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/shaper/traffic-shaper/{traffic-shaper}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> bandwidth-unit </span> - Unit of measurement for guaranteed and maximum bandwidth for this shaper (Kbps, Mbps or Gbps). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> diffserv </span> - Enable/disable changing the DiffServ setting applied to traffic accepted by this shaper. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> diffservcode </span> - DiffServ setting to be applied to traffic accepted by this shaper. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> guaranteed-bandwidth </span> - Amount of bandwidth guaranteed for this shaper (0 - 16776000). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> maximum-bandwidth </span> - Upper bandwidth limit enforced by this shaper (0 - 16776000). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> name </span> - Traffic shaper name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> per-policy </span> - Enable/disable applying a separate shaper for each policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> priority </span> - Higher priority traffic is more likely to be forwarded without delays and without compromising the guaranteed bandwidth. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/shaper/traffic-shaper/{traffic-shaper}</span>  </li>
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



