:source: fmgr_cli_system_log_fetch_client_profile_client_profile_device_filter_device_filter.py

:orphan:

.. _fmgr_cli_system_log_fetch_client_profile_client_profile_device_filter_device_filter:

fmgr_cli_system_log_fetch_client_profile_client_profile_device_filter_device_filter -- List of device filter.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[delete, get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/log-fetch/client-profile/{client-profile}/device-filter/{device-filter}`
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
 <li><span class="li-head">device-filter</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [delete, get]</span> - List of device filter.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - List of device filter.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">adom</span> - Adom name. <span class="li-normal">type: str</span>  <span class="li-normal">default: *</span> </li>
 <li><span class="li-head">device</span> - Device name or Serial number. <span class="li-normal">type: str</span>  <span class="li-normal">default: *</span> </li>
 <li><span class="li-head">id</span> - Add or edit a device filter. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">vdom</span> - Vdom filters. <span class="li-normal">type: str</span>  <span class="li-normal">default: *</span> </li>
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
    - name: send request to /cli/system/log-fetch/client-profile/{client-profile}/device-filter/{device-filter}
      fmgr_cli_system_log_fetch_client_profile_client_profile_device_filter_device_filter:
         method: <value in [set, update]>
         url_params:
            client-profile: <value of string>
            device-filter: <value of string>
         params:
            - 
               data: 
                  adom: <value of string default: *>
                  device: <value of string default: *>
                  id: <value of integer default: 0>
                  vdom: <value of string default: *>



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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/log-fetch/client-profile/{client-profile}/device-filter/{device-filter}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> adom </span> - Adom name. <span class="li-normal">type: str</span>  <span class="li-normal">example: *</span>  </li>
 <li> <span class="li-return"> device </span> - Device name or Serial number. <span class="li-normal">type: str</span>  <span class="li-normal">example: *</span>  </li>
 <li> <span class="li-return"> id </span> - Add or edit a device filter. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> vdom </span> - Vdom filters. <span class="li-normal">type: str</span>  <span class="li-normal">example: *</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/log-fetch/client-profile/{client-profile}/device-filter/{device-filter}</span>  </li>
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



