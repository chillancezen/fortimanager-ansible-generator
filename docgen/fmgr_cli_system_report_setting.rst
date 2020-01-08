:source: fmgr_cli_system_report_setting.py

:orphan:

.. _fmgr_cli_system_report_setting:

fmgr_cli_system_report_setting -- Report settings.
++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/report/setting`
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
 <li><span class="li-head">parameters for method: [get]</span> - Report settings.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Report settings.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">aggregate-report</span> - Enable/disable including a group report along with the per-device reports. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">hcache-lossless</span> - Usableness of ready-with-loss hcaches. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">ldap-cache-timeout</span> - LDAP cache timeout in minutes, default 60, 0 means not use cache. <span class="li-normal">type: int</span>  <span class="li-normal">default: 60</span> </li>
 <li><span class="li-head">max-table-rows</span> - Maximum number of rows can be generated in a single table. <span class="li-normal">type: int</span>  <span class="li-normal">default: 10000</span> </li>
 <li><span class="li-head">report-priority</span> - Priority of sql report. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [high, low, auto]</span>  <span class="li-normal">default: auto</span> </li>
 <li><span class="li-head">template-auto-install</span> - The language used for new ADOMs (default = default). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, english]</span>  <span class="li-normal">default: default</span> </li>
 <li><span class="li-head">week-start</span> - Day of the week on which the week starts. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sun, mon]</span>  <span class="li-normal">default: sun</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/REPORT/SETTING
      fmgr_cli_system_report_setting:
         method: <value in [set, update]>
         params:
            -
               data:
                  aggregate-report: <value in [disable, enable] default: 'disable'>
                  hcache-lossless: <value in [disable, enable] default: 'disable'>
                  ldap-cache-timeout: <value of integer default: 60>
                  max-table-rows: <value of integer default: 10000>
                  report-priority: <value in [high, low, auto] default: 'auto'>
                  template-auto-install: <value in [default, english] default: 'default'>
                  week-start: <value in [sun, mon] default: 'sun'>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> aggregate-report </span> - Enable/disable including a group report along with the per-device reports. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> hcache-lossless </span> - Usableness of ready-with-loss hcaches. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> ldap-cache-timeout </span> - LDAP cache timeout in minutes, default 60, 0 means not use cache. <span class="li-normal">type: int</span>  <span class="li-normal">example: 60</span>  </li>
 <li> <span class="li-return"> max-table-rows </span> - Maximum number of rows can be generated in a single table. <span class="li-normal">type: int</span>  <span class="li-normal">example: 10000</span>  </li>
 <li> <span class="li-return"> report-priority </span> - Priority of sql report. <span class="li-normal">type: str</span>  <span class="li-normal">example: auto</span>  </li>
 <li> <span class="li-return"> template-auto-install </span> - The language used for new ADOMs (default = default). <span class="li-normal">type: str</span>  <span class="li-normal">example: default</span>  </li>
 <li> <span class="li-return"> week-start </span> - Day of the week on which the week starts. <span class="li-normal">type: str</span>  <span class="li-normal">example: sun</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/report/setting</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/report/setting</span>  </li>
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



