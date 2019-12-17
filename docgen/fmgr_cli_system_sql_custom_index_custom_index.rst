:source: fmgr_cli_system_sql_custom_index_custom_index.py

:orphan:

.. _fmgr_cli_system_sql_custom_index_custom_index:

fmgr_cli_system_sql_custom_index_custom_index -- List of SQL index fields.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[delete, get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/sql/custom-index/{custom-index}`
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
 <li><span class="li-head">custom-index</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [delete, get]</span> - List of SQL index fields.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - List of SQL index fields.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">case-sensitive</span> - Disable/Enable case sensitive index. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">device-type</span> - Device type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [FortiGate, FortiManager, FortiClient, FortiMail, FortiWeb, FortiCache, FortiSandbox, FortiDDoS, FortiAuthenticator, FortiProxy]</span>  <span class="li-normal">default: FortiGate</span> </li>
 <li><span class="li-head">id</span> - Add or Edit log index fields. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">index-field</span> - Log field name to be indexed. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">log-type</span> - Log type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, app-ctrl, attack, content, dlp, emailfilter, event, generic, history, traffic, virus, voip, webfilter, netscan, fct-event, fct-traffic, fct-netscan, waf, gtp, dns, ssh, ssl]</span>  <span class="li-normal">default: traffic</span> </li>
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
    - name: send request to /cli/system/sql/custom-index/{custom-index}
      fmgr_cli_system_sql_custom_index_custom_index:
         method: <value in [set, update]>
         url_params:
            custom-index: <value of string>
         params:
            - 
               data: 
                  case-sensitive: <value in [disable, enable] default: disable>
                  device-type: <value in [FortiGate, FortiManager, FortiClient, ...] default: FortiGate>
                  id: <value of integer default: 0>
                  index-field: <value of string>
                  log-type: <value in [none, app-ctrl, attack, ...] default: traffic>



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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/sql/custom-index/{custom-index}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> case-sensitive </span> - Disable/Enable case sensitive index. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> device-type </span> - Device type. <span class="li-normal">type: str</span>  <span class="li-normal">example: FortiGate</span>  </li>
 <li> <span class="li-return"> id </span> - Add or Edit log index fields. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> index-field </span> - Log field name to be indexed. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log-type </span> - Log type. <span class="li-normal">type: str</span>  <span class="li-normal">example: traffic</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/sql/custom-index/{custom-index}</span>  </li>
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



