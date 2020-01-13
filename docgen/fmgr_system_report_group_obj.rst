:source: fmgr_system_report_group_obj.py

:orphan:

.. _fmgr_system_report_group_obj:

fmgr_system_report_group_obj -- Report group.
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[delete, get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/report/group/{group}`
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
 <li><span class="li-head">group</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [delete, get]</span> - Report group.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Report group.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">adom</span> - Admin domain name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">case-insensitive</span> - Case insensitive. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">chart-alternative</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">chart-name</span> - Chart name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">chart-replace</span> - Chart replacement. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">group-by</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">var-expression</span> - Variable expression. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">var-name</span> - Variable name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">var-type</span> - Variable type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [integer, string, enum, ip]</span>  <span class="li-normal">default: string</span> </li>
 </ul>
 <li><span class="li-head">group-id</span> - Group ID. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">report-like</span> - Report pattern. <span class="li-normal">type: str</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/REPORT/GROUP/{GROUP}
      fmgr_system_report_group_obj:
         method: <value in [set, update]>
         url_params:
            group: <value of string>
         params:
            -
               data:
                  adom: <value of string>
                  case-insensitive: <value in [disable, enable] default: 'enable'>
                  chart-alternative:
                    -
                        chart-name: <value of string>
                        chart-replace: <value of string>
                  group-by:
                    -
                        var-expression: <value of string>
                        var-name: <value of string>
                        var-type: <value in [integer, string, enum, ...] default: 'string'>
                  group-id: <value of integer default: 0>
                  report-like: <value of string>



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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/report/group/{group}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> adom </span> - Admin domain name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> case-insensitive </span> - Case insensitive. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> chart-alternative </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> chart-name </span> - Chart name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> chart-replace </span> - Chart replacement. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> group-by </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> var-expression </span> - Variable expression. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> var-name </span> - Variable name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> var-type </span> - Variable type. <span class="li-normal">type: str</span>  <span class="li-normal">example: string</span>  </li>
 </ul>
 <li> <span class="li-return"> group-id </span> - Group ID. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> report-like </span> - Report pattern. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/report/group/{group}</span>  </li>
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



