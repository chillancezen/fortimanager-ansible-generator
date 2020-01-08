:source: fmgr_cli_system_snmp_community.py

:orphan:

.. _fmgr_cli_system_snmp_community:

fmgr_cli_system_snmp_community -- SNMP community configuration.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/snmp/community`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - SNMP community configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">events</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disk_low, ha_switch, intf_ip_chg, sys_reboot, cpu_high, mem_low, log-alert, log-rate, log-data-rate, lic-gbday, lic-dev-quota, cpu-high-exclude-nice]</span> </li>
 </ul>
 <li><span class="li-head">hosts</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - Host entry ID. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">interface</span> - Allow interface name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip</span> - Allow host IP address. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0 0.0.0.0</span> </li>
 </ul>
 <li><span class="li-head">hosts6</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - Host entry ID. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">interface</span> - Allow interface name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip</span> - Allow host IP address. <span class="li-normal">type: str</span>  <span class="li-normal">default: ::/0</span> </li>
 </ul>
 <li><span class="li-head">id</span> - Community ID. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">name</span> - Community name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">query_v1_port</span> - SNMP v1 query port. <span class="li-normal">type: int</span>  <span class="li-normal">default: 161</span> </li>
 <li><span class="li-head">query_v1_status</span> - Enable/disable SNMP v1 query. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">query_v2c_port</span> - SNMP v2c query port. <span class="li-normal">type: int</span>  <span class="li-normal">default: 161</span> </li>
 <li><span class="li-head">query_v2c_status</span> - Enable/disable SNMP v2c query. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">status</span> - Enable/disable community. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">trap_v1_rport</span> - SNMP v1 trap remote port. <span class="li-normal">type: int</span>  <span class="li-normal">default: 162</span> </li>
 <li><span class="li-head">trap_v1_status</span> - Enable/disable SNMP v1 trap. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">trap_v2c_rport</span> - SNMP v2c trap remote port. <span class="li-normal">type: int</span>  <span class="li-normal">default: 162</span> </li>
 <li><span class="li-head">trap_v2c_status</span> - Enable/disable SNMP v2c trap. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - SNMP community configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [events, id, name, query_v1_port, query_v1_status, query_v2c_port, query_v2c_status, status, trap_v1_rport, trap_v1_status, trap_v2c_rport, trap_v2c_status]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">loadsub</span> - Enable or disable the return of any sub-objects. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [count, syntax]</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/SNMP/COMMUNITY
      fmgr_cli_system_snmp_community:
         method: <value in [add, set, update]>
         params:
            -
               data:
                 -
                     events:
                       - <value in [disk_low, ha_switch, intf_ip_chg, ...]>
                     hosts:
                       -
                           id: <value of integer default: 0>
                           interface: <value of string>
                           ip: <value of string default: '0.0.0.0 0.0.0.0'>
                     hosts6:
                       -
                           id: <value of integer default: 0>
                           interface: <value of string>
                           ip: <value of string default: '::/0'>
                     id: <value of integer default: 0>
                     name: <value of string>
                     query_v1_port: <value of integer default: 161>
                     query_v1_status: <value in [disable, enable] default: 'enable'>
                     query_v2c_port: <value of integer default: 161>
                     query_v2c_status: <value in [disable, enable] default: 'enable'>
                     status: <value in [disable, enable] default: 'enable'>
                     trap_v1_rport: <value of integer default: 162>
                     trap_v1_status: <value in [disable, enable] default: 'enable'>
                     trap_v2c_rport: <value of integer default: 162>
                     trap_v2c_status: <value in [disable, enable] default: 'enable'>

    - name: REQUESTING /CLI/SYSTEM/SNMP/COMMUNITY
      fmgr_cli_system_snmp_community:
         method: <value in [get]>
         params:
            -
               fields:
                 -
                    - <value in [events, id, name, ...]>
               filter:
                 - <value of string>
               loadsub: <value of integer>
               option: <value in [count, syntax]>



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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/snmp/community</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> events </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> hosts </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - Host entry ID. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> interface </span> - Allow interface name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip </span> - Allow host IP address. <span class="li-normal">type: str</span>  <span class="li-normal">example: 0.0.0.0 0.0.0.0</span>  </li>
 </ul>
 <li> <span class="li-return"> hosts6 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - Host entry ID. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> interface </span> - Allow interface name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip </span> - Allow host IP address. <span class="li-normal">type: str</span>  <span class="li-normal">example: ::/0</span>  </li>
 </ul>
 <li> <span class="li-return"> id </span> - Community ID. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> name </span> - Community name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> query_v1_port </span> - SNMP v1 query port. <span class="li-normal">type: int</span>  <span class="li-normal">example: 161</span>  </li>
 <li> <span class="li-return"> query_v1_status </span> - Enable/disable SNMP v1 query. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> query_v2c_port </span> - SNMP v2c query port. <span class="li-normal">type: int</span>  <span class="li-normal">example: 161</span>  </li>
 <li> <span class="li-return"> query_v2c_status </span> - Enable/disable SNMP v2c query. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable community. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> trap_v1_rport </span> - SNMP v1 trap remote port. <span class="li-normal">type: int</span>  <span class="li-normal">example: 162</span>  </li>
 <li> <span class="li-return"> trap_v1_status </span> - Enable/disable SNMP v1 trap. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> trap_v2c_rport </span> - SNMP v2c trap remote port. <span class="li-normal">type: int</span>  <span class="li-normal">example: 162</span>  </li>
 <li> <span class="li-return"> trap_v2c_status </span> - Enable/disable SNMP v2c trap. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/snmp/community</span>  </li>
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



