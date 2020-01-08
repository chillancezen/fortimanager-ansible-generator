:source: fmgr_dvmdb_adom.py

:orphan:

.. _fmgr_dvmdb_adom:

fmgr_dvmdb_adom -- ADOM table, most attributes are read-only and can only be changed internally.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/dvmdb/adom`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - ADOM table, most attributes are read-only and can only be changed internally.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">desc</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">flags</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [migration, db_export, no_vpn_console, backup, other_devices, central_sdwan, is_autosync, per_device_wtp, policy_check_on_install, install_on_policy_check_fail, auto_push_cfg]</span> </li>
 </ul>
 <li><span class="li-head">log_db_retention_hours</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 1440</span> </li>
 <li><span class="li-head">log_disk_quota</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log_disk_quota_alert_thres</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 90</span> </li>
 <li><span class="li-head">log_disk_quota_split_ratio</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 70</span> </li>
 <li><span class="li-head">log_file_retention_hours</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 8760</span> </li>
 <li><span class="li-head">meta fields</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mig_mr</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 2</span> </li>
 <li><span class="li-head">mig_os_ver</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]</span>  <span class="li-normal">default: 6.0</span> </li>
 <li><span class="li-head">mode</span> - ems - (Value no longer used as of 4. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ems, gms, provider]</span>  <span class="li-normal">default: gms</span> </li>
 <li><span class="li-head">mr</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 2</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">os_ver</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0]</span>  <span class="li-normal">default: 6.0</span> </li>
 <li><span class="li-head">restricted_prds</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [fos, foc, fml, fch, fwb, log, fct, faz, fsa, fsw, fmg, fdd, fac, fpx]</span> </li>
 </ul>
 <li><span class="li-head">state</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 1</span> </li>
 <li><span class="li-head">uuid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - ADOM table, most attributes are read-only and can only be changed internally.</li>
 <ul class="ul-self">
 <li><span class="li-head">expand member</span> - Fetch all or selected attributes of object members. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [desc, flags, log_db_retention_hours, log_disk_quota, log_disk_quota_alert_thres, log_disk_quota_split_ratio, log_file_retention_hours, mig_mr, mig_os_ver, mode, mr, name, os_ver, restricted_prds, state, uuid]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">loadsub</span> - Enable or disable the return of any sub-objects. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">meta fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [count, object member, syntax]</span> </li>
 <li><span class="li-head">range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">sortings</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{attr_name}</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">choices: [1, -1]</span> </li>
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

    - name: REQUESTING /DVMDB/ADOM
      fmgr_dvmdb_adom:
         method: <value in [add, set, update]>
         params:
            -
               data:
                 -
                     desc: <value of string>
                     flags:
                       - <value in [migration, db_export, no_vpn_console, ...]>
                     log_db_retention_hours: <value of integer default: 1440>
                     log_disk_quota: <value of integer>
                     log_disk_quota_alert_thres: <value of integer default: 90>
                     log_disk_quota_split_ratio: <value of integer default: 70>
                     log_file_retention_hours: <value of integer default: 8760>
                     meta fields: <value of string>
                     mig_mr: <value of integer default: 2>
                     mig_os_ver: <value in [unknown, 0.0, 1.0, ...] default: '6.0'>
                     mode: <value in [ems, gms, provider] default: 'gms'>
                     mr: <value of integer default: 2>
                     name: <value of string>
                     os_ver: <value in [unknown, 0.0, 1.0, ...] default: '6.0'>
                     restricted_prds:
                       - <value in [fos, foc, fml, ...]>
                     state: <value of integer default: 1>
                     uuid: <value of string>

    - name: REQUESTING /DVMDB/ADOM
      fmgr_dvmdb_adom:
         method: <value in [get]>
         params:
            -
               expand member: <value of string>
               fields:
                 -
                    - <value in [desc, flags, log_db_retention_hours, ...]>
               filter:
                 - <value of string>
               loadsub: <value of integer>
               meta fields:
                 - <value of string>
               option: <value in [count, object member, syntax]>
               range:
                 - <value of integer>
               sortings:
                 -
                     varidic.attr_name: <value in [1, -1]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [add, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /dvmdb/adom</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> desc </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> flags </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> log_db_retention_hours </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 1440</span>  </li>
 <li> <span class="li-return"> log_disk_quota </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> log_disk_quota_alert_thres </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 90</span>  </li>
 <li> <span class="li-return"> log_disk_quota_split_ratio </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 70</span>  </li>
 <li> <span class="li-return"> log_file_retention_hours </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 8760</span>  </li>
 <li> <span class="li-return"> meta fields </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mig_mr </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 2</span>  </li>
 <li> <span class="li-return"> mig_os_ver </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: 6.0</span>  </li>
 <li> <span class="li-return"> mode </span> - ems - (Value no longer used as of 4. <span class="li-normal">type: str</span>  <span class="li-normal">example: gms</span>  </li>
 <li> <span class="li-return"> mr </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 2</span>  </li>
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> os_ver </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: 6.0</span>  </li>
 <li> <span class="li-return"> restricted_prds </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> state </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 1</span>  </li>
 <li> <span class="li-return"> uuid </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /dvmdb/adom</span>  </li>
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



