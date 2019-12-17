:source: fmgr_pm_config_obj_firewall_schedule_onetime_onetime.py

:orphan:

.. _fmgr_pm_config_obj_firewall_schedule_onetime_onetime:

fmgr_pm_config_obj_firewall_schedule_onetime_onetime -- Onetime schedule configuration.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/schedule/onetime/{onetime}`
- `/pm/config/global/obj/firewall/schedule/onetime/{onetime}`
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
 <li><span class="li-head">onetime</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Onetime schedule configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">color</span> - Color of icon on the GUI. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">end</span> - Schedule end date and time, format hh:mm yyyy/mm/dd. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">expiration-days</span> - Write an event log message this many days before the schedule expires. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - Onetime schedule name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">start</span> - Schedule start date and time, format hh:mm yyyy/mm/dd. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Onetime schedule configuration.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Onetime schedule configuration.</li>
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
    - name: send request to /pm/config/obj/firewall/schedule/onetime/{onetime}
      fmgr_pm_config_obj_firewall_schedule_onetime_onetime:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            onetime: <value of string>
         params:
            - 
               data: 
                  color: <value of integer>
                  end: <value of string>
                  expiration-days: <value of integer>
                  name: <value of string>
                  start: <value of string>
    - name: send request to /pm/config/obj/firewall/schedule/onetime/{onetime}
      fmgr_pm_config_obj_firewall_schedule_onetime_onetime:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            onetime: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/schedule/onetime/{onetime}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> color </span> - Color of icon on the GUI. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> end </span> - Schedule end date and time, format hh:mm yyyy/mm/dd. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> expiration-days </span> - Write an event log message this many days before the schedule expires. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> name </span> - Onetime schedule name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> start </span> - Schedule start date and time, format hh:mm yyyy/mm/dd. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/schedule/onetime/{onetime}</span>  </li>
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



