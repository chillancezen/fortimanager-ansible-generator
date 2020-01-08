:source: fmgr_pm_config_wanprof_system_virtual_wan_link_health_check_sla_per_object.py

:orphan:

.. _fmgr_pm_config_wanprof_system_virtual_wan_link_health_check_sla_per_object:

fmgr_pm_config_wanprof_system_virtual_wan_link_health_check_sla_per_object -- Service level agreement (SLA).
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/health-check/{health-check}/sla/{sla}`
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
 <li><span class="li-head">health-check</span> - the object name <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sla</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Service level agreement (SLA).</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - SLA ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">jitter-threshold</span> - Jitter for SLA to make decision in milliseconds. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">latency-threshold</span> - Latency for SLA to make decision in milliseconds. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">link-cost-factor</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [latency, jitter, packet-loss]</span> </li>
 </ul>
 <li><span class="li-head">packetloss-threshold</span> - Packet loss for SLA to make decision in percentage. <span class="li-normal">type: int</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Service level agreement (SLA).</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Service level agreement (SLA).</li>
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

    - name: REQUESTING /PM/CONFIG/WANPROF/{WANPROF}/SYSTEM/VIRTUAL-WAN-LINK/HEALTH-CHECK/{HEALTH-CHECK}/SLA/{SLA}
      fmgr_pm_config_wanprof_system_virtual_wan_link_health_check_sla_per_object:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wanprof: <value of string>
            health-check: <value of string>
            sla: <value of string>
         params:
            -
               data:
                  id: <value of integer>
                  jitter-threshold: <value of integer>
                  latency-threshold: <value of integer>
                  link-cost-factor:
                    - <value in [latency, jitter, packet-loss]>
                  packetloss-threshold: <value of integer>

    - name: REQUESTING /PM/CONFIG/WANPROF/{WANPROF}/SYSTEM/VIRTUAL-WAN-LINK/HEALTH-CHECK/{HEALTH-CHECK}/SLA/{SLA}
      fmgr_pm_config_wanprof_system_virtual_wan_link_health_check_sla_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wanprof: <value of string>
            health-check: <value of string>
            sla: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/health-check/{health-check}/sla/{sla}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - SLA ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> jitter-threshold </span> - Jitter for SLA to make decision in milliseconds. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> latency-threshold </span> - Latency for SLA to make decision in milliseconds. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> link-cost-factor </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> packetloss-threshold </span> - Packet loss for SLA to make decision in percentage. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/health-check/{health-check}/sla/{sla}</span>  </li>
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



