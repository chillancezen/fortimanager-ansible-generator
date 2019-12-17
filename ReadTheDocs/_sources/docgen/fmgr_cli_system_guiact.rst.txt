:source: fmgr_cli_system_guiact.py

:orphan:

.. _fmgr_cli_system_guiact:

fmgr_cli_system_guiact -- System settings through GUI.
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/guiact`
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
 <li><span class="li-head">parameters for method: [get]</span> - System settings through GUI.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - System settings through GUI.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">backup_all</span> - Backup all settings. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">backup_conf</span> - Backup config file. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">eventlog_msg</span> - Write event log. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">eventlog_path</span> - Event log path. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">reboot</span> - Reboot system. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">reset2default</span> - Reset to factory default. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">restore_all</span> - Restore all settings. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">restore_conf</span> - Restore config file. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">time</span> - Time. <span class="li-normal">type: str</span> </li>
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
    - name: send request to /cli/system/guiact
      fmgr_cli_system_guiact:
         method: <value in [set, update]>
         params:
            - 
               data: 
                  backup_all: <value of string>
                  backup_conf: <value of string>
                  eventlog_msg: <value of string>
                  eventlog_path: <value of string>
                  reboot: <value of integer default: 0>
                  reset2default: <value of integer default: 0>
                  restore_all: <value of string>
                  restore_conf: <value of string>
                  time: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> backup_all </span> - Backup all settings. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> backup_conf </span> - Backup config file. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> eventlog_msg </span> - Write event log. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> eventlog_path </span> - Event log path. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> reboot </span> - Reboot system. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> reset2default </span> - Reset to factory default. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> restore_all </span> - Restore all settings. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> restore_conf </span> - Restore config file. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> time </span> - Time. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/guiact</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/guiact</span>  </li>
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



