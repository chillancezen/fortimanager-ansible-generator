:source: fmgr_cli_system_locallog_fortianalyzer2_setting.py

:orphan:

.. _fmgr_cli_system_locallog_fortianalyzer2_setting:

fmgr_cli_system_locallog_fortianalyzer2_setting -- Settings for locallog to fortianalyzer.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/locallog/fortianalyzer2/setting`
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
 <li><span class="li-head">parameters for method: [get]</span> - Settings for locallog to fortianalyzer.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Settings for locallog to fortianalyzer.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">reliable</span> - Enable/disable reliable realtime logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">secure-connection</span> - Enable/disable connection secured by TLS/SSL. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">server-ip</span> - Remote FortiAnalyzer server IP address. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">severity</span> - Least severity level to log. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [emergency, alert, critical, error, warning, notification, information, debug]</span>  <span class="li-normal">default: notification</span> </li>
 <li><span class="li-head">status</span> - Log to FortiAnalyzer status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, realtime, upload]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">upload-time</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
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

    - name: REQUESTING /CLI/SYSTEM/LOCALLOG/FORTIANALYZER2/SETTING
      fmgr_cli_system_locallog_fortianalyzer2_setting:
         method: <value in [set, update]>
         params:
            -
               data:
                  reliable: <value in [disable, enable] default: 'disable'>
                  secure-connection: <value in [disable, enable] default: 'disable'>
                  server-ip: <value of string default: '0.0.0.0'>
                  severity: <value in [emergency, alert, critical, ...] default: 'notification'>
                  status: <value in [disable, realtime, upload] default: 'disable'>
                  upload-time:
                    - <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> reliable </span> - Enable/disable reliable realtime logging. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> secure-connection </span> - Enable/disable connection secured by TLS/SSL. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> server-ip </span> - Remote FortiAnalyzer server IP address. <span class="li-normal">type: str</span>  <span class="li-normal">example: 0.0.0.0</span>  </li>
 <li> <span class="li-return"> severity </span> - Least severity level to log. <span class="li-normal">type: str</span>  <span class="li-normal">example: notification</span>  </li>
 <li> <span class="li-return"> status </span> - Log to FortiAnalyzer status. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> upload-time </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/locallog/fortianalyzer2/setting</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/locallog/fortianalyzer2/setting</span>  </li>
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



