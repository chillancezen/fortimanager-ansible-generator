:source: fmgr_cli_system_snmp_sysinfo.py

:orphan:

.. _fmgr_cli_system_snmp_sysinfo:

fmgr_cli_system_snmp_sysinfo -- SNMP configuration.
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/snmp/sysinfo`
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
 <li><span class="li-head">parameters for method: [get]</span> - SNMP configuration.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - SNMP configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">contact_info</span> - Contact information. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">description</span> - System description. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">engine-id</span> - Local SNMP engineID string (maximum 24 characters). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">location</span> - System location. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable SNMP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">trap-cpu-high-exclude-nice-threshold</span> - SNMP trap for CPU usage threshold (exclude NICE processes). <span class="li-normal">type: int</span>  <span class="li-normal">default: 80</span> </li>
 <li><span class="li-head">trap-high-cpu-threshold</span> - SNMP trap for CPU usage threshold. <span class="li-normal">type: int</span>  <span class="li-normal">default: 80</span> </li>
 <li><span class="li-head">trap-low-memory-threshold</span> - SNMP trap for memory usage threshold. <span class="li-normal">type: int</span>  <span class="li-normal">default: 80</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/SNMP/SYSINFO
      fmgr_cli_system_snmp_sysinfo:
         method: <value in [set, update]>
         params:
            -
               data:
                  contact_info: <value of string>
                  description: <value of string>
                  engine-id: <value of string>
                  location: <value of string>
                  status: <value in [disable, enable] default: 'disable'>
                  trap-cpu-high-exclude-nice-threshold: <value of integer default: 80>
                  trap-high-cpu-threshold: <value of integer default: 80>
                  trap-low-memory-threshold: <value of integer default: 80>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> contact_info </span> - Contact information. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> description </span> - System description. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> engine-id </span> - Local SNMP engineID string (maximum 24 characters). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> location </span> - System location. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable SNMP. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> trap-cpu-high-exclude-nice-threshold </span> - SNMP trap for CPU usage threshold (exclude NICE processes). <span class="li-normal">type: int</span>  <span class="li-normal">example: 80</span>  </li>
 <li> <span class="li-return"> trap-high-cpu-threshold </span> - SNMP trap for CPU usage threshold. <span class="li-normal">type: int</span>  <span class="li-normal">example: 80</span>  </li>
 <li> <span class="li-return"> trap-low-memory-threshold </span> - SNMP trap for memory usage threshold. <span class="li-normal">type: int</span>  <span class="li-normal">example: 80</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/snmp/sysinfo</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/snmp/sysinfo</span>  </li>
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



