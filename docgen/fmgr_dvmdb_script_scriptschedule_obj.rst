:source: fmgr_dvmdb_script_scriptschedule_obj.py

:orphan:

.. _fmgr_dvmdb_script_scriptschedule_obj:

fmgr_dvmdb_script_scriptschedule_obj -- Script schedule table.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[delete, get, set, update]** the following FortiManager json-rpc urls.
- `/dvmdb/adom/{adom}/script/{script}/script_schedule/{script_schedule}`
- `/dvmdb/global/script/{script}/script_schedule/{script_schedule}`
- `/dvmdb/script/{script}/script_schedule/{script_schedule}`
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
 <li><span class="li-head">script</span> - the object name <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">script_schedule</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Script schedule table.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Script schedule table.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Script schedule table.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">datetime</span> - Indicates the date and time of the schedule. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">day_of_week</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, sun, mon, tue, wed, thu, fri, sat]</span>  <span class="li-normal">default: sun</span> </li>
 <li><span class="li-head">device</span> - Name or id of an existing device in the database. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">run_on_db</span> - Indicates if the scheduled script should be executed on device database. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, onetime, daily, weekly, monthly]</span> </li>
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

    - name: REQUESTING /DVMDB/SCRIPT/{SCRIPT}/SCRIPT_SCHEDULE/{SCRIPT_SCHEDULE}
      fmgr_dvmdb_script_scriptschedule_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            script: <value of string>
            script_schedule: <value of string>
         params:
            -
               option: <value in [object member, chksum]>

    - name: REQUESTING /DVMDB/SCRIPT/{SCRIPT}/SCRIPT_SCHEDULE/{SCRIPT_SCHEDULE}
      fmgr_dvmdb_script_scriptschedule_obj:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            script: <value of string>
            script_schedule: <value of string>
         params:
            -
               data:
                  datetime: <value of string>
                  day_of_week: <value in [unknown, sun, mon, ...] default: 'sun'>
                  device: <value of integer>
                  name: <value of string>
                  run_on_db: <value in [disable, enable] default: 'disable'>
                  type: <value in [auto, onetime, daily, ...]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [delete, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /dvmdb/adom/{adom}/script/{script}/script_schedule/{script_schedule}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> datetime </span> - Indicates the date and time of the schedule. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> day_of_week </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: sun</span>  </li>
 <li> <span class="li-return"> device </span> - Name or id of an existing device in the database. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> run_on_db </span> - Indicates if the scheduled script should be executed on device database. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /dvmdb/adom/{adom}/script/{script}/script_schedule/{script_schedule}</span>  </li>
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



