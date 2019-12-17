:source: fmgr_pm_config_device_device_vdom_vdom_switch_controller_managed_switch_managed_switch_switch_log.py

:orphan:

.. _fmgr_pm_config_device_device_vdom_vdom_switch_controller_managed_switch_managed_switch_switch_log:

fmgr_pm_config_device_device_vdom_vdom_switch_controller_managed_switch_managed_switch_switch_log -- Configuration method to edit FortiSwitch logging settings (logs are transferred to and inserted into the FortiGate event log).
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/device/{device}/vdom/{vdom}/switch-controller/managed-switch/{managed-switch}/switch-log`
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
 <li><span class="li-head">device</span> - the object name <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - the object name <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">managed-switch</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configuration method to edit FortiSwitch logging settings (logs are transferred to and inserted into the FortiGate event log).</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Configuration method to edit FortiSwitch logging settings (logs are transferred to and inserted into the FortiGate event log).</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
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
    - name: send request to /pm/config/device/{device}/vdom/{vdom}/switch-controller/managed-switch/{managed-switch}/switch-log
      fmgr_pm_config_device_device_vdom_vdom_switch_controller_managed_switch_managed_switch_switch_log:
         method: <value in [get]>
         url_params:
            device: <value of string>
            vdom: <value of string>
            managed-switch: <value of string>
         params:
            - 
               option: <value in [object member, chksum, datasrc]>
    - name: send request to /pm/config/device/{device}/vdom/{vdom}/switch-controller/managed-switch/{managed-switch}/switch-log
      fmgr_pm_config_device_device_vdom_vdom_switch_controller_managed_switch_managed_switch_switch_log:
         method: <value in [set, update]>
         url_params:
            device: <value of string>
            vdom: <value of string>
            managed-switch: <value of string>
         params:
            - 
               data: 


Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/device/{device}/vdom/{vdom}/switch-controller/managed-switch/{managed-switch}/switch-log</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/device/{device}/vdom/{vdom}/switch-controller/managed-switch/{managed-switch}/switch-log</span>  </li>
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



