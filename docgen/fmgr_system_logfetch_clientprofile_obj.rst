:source: fmgr_system_logfetch_clientprofile_obj.py

:orphan:

.. _fmgr_system_logfetch_clientprofile_obj:

fmgr_system_logfetch_clientprofile_obj -- Log-fetch client profile settings.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[delete, get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/log-fetch/client-profile/{client-profile}`
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
 <li><span class="li-head">client-profile</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [delete, get]</span> - Log-fetch client profile settings.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Log-fetch client profile settings.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">client-adom</span> - Log-fetch client sides adom name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">data-range</span> - Data-range for fetched logs. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [custom]</span>  <span class="li-normal">default: custom</span> </li>
 <li><span class="li-head">data-range-value</span> - Last n days or hours. <span class="li-normal">type: int</span>  <span class="li-normal">default: 10</span> </li>
 <li><span class="li-head">device-filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">adom</span> - Adom name. <span class="li-normal">type: str</span>  <span class="li-normal">default: *</span> </li>
 <li><span class="li-head">device</span> - Device name or Serial number. <span class="li-normal">type: str</span>  <span class="li-normal">default: *</span> </li>
 <li><span class="li-head">id</span> - Add or edit a device filter. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">vdom</span> - Vdom filters. <span class="li-normal">type: str</span>  <span class="li-normal">default: *</span> </li>
 </ul>
 <li><span class="li-head">end-time</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">id</span> - Log-fetch client profile ID. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">index-fetch-logs</span> - Enable/Disable indexing logs automatically after fetching logs. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">log-filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">field</span> - Field name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Log filter ID. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">oper</span> - Field filter operator. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [=, !=, <, >, <=, >=, contain, not-contain, match]</span>  <span class="li-normal">default: =</span> </li>
 <li><span class="li-head">value</span> - Field filter operand or free-text matching expression. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">log-filter-logic</span> - And/Or logic for log-filters. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [and, or]</span>  <span class="li-normal">default: or</span> </li>
 <li><span class="li-head">log-filter-status</span> - Enable/Disable log-filter. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">name</span> - Name of log-fetch client profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC NzkzMDg4MDc2MTgwNjUzNhwvJBDjPF8MRvYpIukmL7G++XrKmHYTQF5zcGV+Ss3GXWsKe9F9Ie2B55rWFdty9EbQ6aAhGObDlAP7FQ7Otz0SNL49BDP1poSzSg2PuvFul8YYBSll3W/AAKoDgHm+llvtNz/qEJFyG6JzkDaGLy1ebMpO</span> </li>
 </ul>
 <li><span class="li-head">secure-connection</span> - Enable/Disable protecting log-fetch connection with TLS/SSL. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">server-adom</span> - Log-fetch server sides adom name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server-ip</span> - Log-fetch server IP address. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">start-time</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">sync-adom-config</span> - Enable/Disable sync adom related config. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">user</span> - Log-fetch server login username. <span class="li-normal">type: str</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/LOG-FETCH/CLIENT-PROFILE/{CLIENT-PROFILE}
      fmgr_system_logfetch_clientprofile_obj:
         method: <value in [set, update]>
         url_params:
            client-profile: <value of string>
         params:
            -
               data:
                  client-adom: <value of string>
                  data-range: <value in [custom] default: 'custom'>
                  data-range-value: <value of integer default: 10>
                  device-filter:
                    -
                        adom: <value of string default: '*'>
                        device: <value of string default: '*'>
                        id: <value of integer default: 0>
                        vdom: <value of string default: '*'>
                  end-time:
                    - <value of string>
                  id: <value of integer default: 0>
                  index-fetch-logs: <value in [disable, enable] default: 'enable'>
                  log-filter:
                    -
                        field: <value of string>
                        id: <value of integer default: 0>
                        oper: <value in [=, !=, <, ...] default: '='>
                        value: <value of string>
                  log-filter-logic: <value in [and, or] default: 'or'>
                  log-filter-status: <value in [disable, enable] default: 'disable'>
                  name: <value of string>
                  password:
                    - <value of string default: 'ENC NzkzMDg4MDc2MTgwNjUzNhwvJBDjPF8MRvYpIukmL7G++XrKmHYTQF5zcGV+Ss3GXWsKe9F9...'>
                  secure-connection: <value in [disable, enable] default: 'enable'>
                  server-adom: <value of string>
                  server-ip: <value of string default: '0.0.0.0'>
                  start-time:
                    - <value of string>
                  sync-adom-config: <value in [disable, enable] default: 'disable'>
                  user: <value of string>



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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/log-fetch/client-profile/{client-profile}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> client-adom </span> - Log-fetch client sides adom name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> data-range </span> - Data-range for fetched logs. <span class="li-normal">type: str</span>  <span class="li-normal">example: custom</span>  </li>
 <li> <span class="li-return"> data-range-value </span> - Last n days or hours. <span class="li-normal">type: int</span>  <span class="li-normal">example: 10</span>  </li>
 <li> <span class="li-return"> device-filter </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> adom </span> - Adom name. <span class="li-normal">type: str</span>  <span class="li-normal">example: *</span>  </li>
 <li> <span class="li-return"> device </span> - Device name or Serial number. <span class="li-normal">type: str</span>  <span class="li-normal">example: *</span>  </li>
 <li> <span class="li-return"> id </span> - Add or edit a device filter. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> vdom </span> - Vdom filters. <span class="li-normal">type: str</span>  <span class="li-normal">example: *</span>  </li>
 </ul>
 <li> <span class="li-return"> end-time </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> id </span> - Log-fetch client profile ID. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> index-fetch-logs </span> - Enable/Disable indexing logs automatically after fetching logs. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> log-filter </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> field </span> - Field name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Log filter ID. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> oper </span> - Field filter operator. <span class="li-normal">type: str</span>  <span class="li-normal">example: =</span>  </li>
 <li> <span class="li-return"> value </span> - Field filter operand or free-text matching expression. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> log-filter-logic </span> - And/Or logic for log-filters. <span class="li-normal">type: str</span>  <span class="li-normal">example: or</span>  </li>
 <li> <span class="li-return"> log-filter-status </span> - Enable/Disable log-filter. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> name </span> - Name of log-fetch client profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC NzkzMDg4MDc2MTgwNjUzNhwvJBDjPF8MRvYpIukmL7G++XrKmHYTQF5zcGV+Ss3GXWsKe9F9Ie2B55rWFdty9EbQ6aAhGObDlAP7FQ7Otz0SNL49BDP1poSzSg2PuvFul8YYBSll3W/AAKoDgHm+llvtNz/qEJFyG6JzkDaGLy1ebMpO</span>  </li>
 </ul>
 <li> <span class="li-return"> secure-connection </span> - Enable/Disable protecting log-fetch connection with TLS/SSL. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> server-adom </span> - Log-fetch server sides adom name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server-ip </span> - Log-fetch server IP address. <span class="li-normal">type: str</span>  <span class="li-normal">example: 0.0.0.0</span>  </li>
 <li> <span class="li-return"> start-time </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> sync-adom-config </span> - Enable/Disable sync adom related config. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> user </span> - Log-fetch server login username. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/log-fetch/client-profile/{client-profile}</span>  </li>
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



