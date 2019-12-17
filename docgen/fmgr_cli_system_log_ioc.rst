:source: fmgr_cli_system_log_ioc.py

:orphan:

.. _fmgr_cli_system_log_ioc:

fmgr_cli_system_log_ioc -- IoC settings.
++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/log/ioc`
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
 <li><span class="li-head">parameters for method: [get]</span> - IoC settings.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - IoC settings.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">notification</span> - Disable/Enable IoC notification. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">notification-throttle</span> - Minute value for throttling the rate of IoC notifications. <span class="li-normal">type: int</span>  <span class="li-normal">default: 1440</span> </li>
 <li><span class="li-head">rescan-max-runner</span> - Max count of cocurrent runner of IoC rescan. <span class="li-normal">type: int</span>  <span class="li-normal">default: 8</span> </li>
 <li><span class="li-head">rescan-run-at</span> - When to run IoC rescan. <span class="li-normal">type: int</span>  <span class="li-normal">default: 24</span> </li>
 <li><span class="li-head">rescan-status</span> - Disable/Enable IoC rescan. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">status</span> - Disable/Enable IoC feature. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
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
    - name: send request to /cli/system/log/ioc
      fmgr_cli_system_log_ioc:
         method: <value in [set, update]>
         params:
            - 
               data: 
                  notification: <value in [disable, enable] default: enable>
                  notification-throttle: <value of integer default: 1440>
                  rescan-max-runner: <value of integer default: 8>
                  rescan-run-at: <value of integer default: 24>
                  rescan-status: <value in [disable, enable] default: enable>
                  status: <value in [disable, enable] default: enable>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> notification </span> - Disable/Enable IoC notification. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> notification-throttle </span> - Minute value for throttling the rate of IoC notifications. <span class="li-normal">type: int</span>  <span class="li-normal">example: 1440</span>  </li>
 <li> <span class="li-return"> rescan-max-runner </span> - Max count of cocurrent runner of IoC rescan. <span class="li-normal">type: int</span>  <span class="li-normal">example: 8</span>  </li>
 <li> <span class="li-return"> rescan-run-at </span> - When to run IoC rescan. <span class="li-normal">type: int</span>  <span class="li-normal">example: 24</span>  </li>
 <li> <span class="li-return"> rescan-status </span> - Disable/Enable IoC rescan. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> status </span> - Disable/Enable IoC feature. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/log/ioc</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/log/ioc</span>  </li>
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



