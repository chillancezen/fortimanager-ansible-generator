:source: fmgr_system_locallog_setting.py

:orphan:

.. _fmgr_system_locallog_setting:

fmgr_system_locallog_setting -- Settings for locallog logging.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/locallog/setting`
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
 <li><span class="li-head">parameters for method: [get]</span> - Settings for locallog logging.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Settings for locallog logging.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">log-interval-dev-no-logging</span> - Interval in minute for logging the event of no logs received from a device. <span class="li-normal">type: int</span>  <span class="li-normal">default: 1440</span> </li>
 <li><span class="li-head">log-interval-disk-full</span> - Interval in minute for logging the event of disk full. <span class="li-normal">type: int</span>  <span class="li-normal">default: 5</span> </li>
 <li><span class="li-head">log-interval-gbday-exceeded</span> - Interval in minute for logging the event of the GB/Day license exceeded. <span class="li-normal">type: int</span>  <span class="li-normal">default: 1440</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/LOCALLOG/SETTING
      fmgr_system_locallog_setting:
         method: <value in [set, update]>
         params:
            -
               data:
                  log-interval-dev-no-logging: <value of integer default: 1440>
                  log-interval-disk-full: <value of integer default: 5>
                  log-interval-gbday-exceeded: <value of integer default: 1440>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> log-interval-dev-no-logging </span> - Interval in minute for logging the event of no logs received from a device. <span class="li-normal">type: int</span>  <span class="li-normal">example: 1440</span>  </li>
 <li> <span class="li-return"> log-interval-disk-full </span> - Interval in minute for logging the event of disk full. <span class="li-normal">type: int</span>  <span class="li-normal">example: 5</span>  </li>
 <li> <span class="li-return"> log-interval-gbday-exceeded </span> - Interval in minute for logging the event of the GB/Day license exceeded. <span class="li-normal">type: int</span>  <span class="li-normal">example: 1440</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/locallog/setting</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/locallog/setting</span>  </li>
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



