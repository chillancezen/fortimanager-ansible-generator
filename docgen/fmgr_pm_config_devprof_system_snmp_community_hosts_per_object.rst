:source: fmgr_pm_config_devprof_system_snmp_community_hosts_per_object.py

:orphan:

.. _fmgr_pm_config_devprof_system_snmp_community_hosts_per_object:

fmgr_pm_config_devprof_system_snmp_community_hosts_per_object -- Configure IPv4 SNMP managers (hosts).
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/devprof/{devprof}/system/snmp/community/{community}/hosts/{hosts}`
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
 <li><span class="li-head">adom</span> - the domain prefix <span class="li-normal">type: str</span> <span class="li-normal"> choices: none, global, custom dom</span></li>
 <li><span class="li-head">devprof</span> - the object name <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">community</span> - the object name <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">hosts</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure IPv4 SNMP managers (hosts).</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">ha-direct</span> - Enable/disable direct management of HA cluster members. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">host-type</span> - Control whether the SNMP manager sends SNMP queries, receives SNMP traps, or both. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [any, query, trap]</span> </li>
 <li><span class="li-head">id</span> - Host entry ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - IPv4 address of the SNMP manager (host). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-ip</span> - Source IPv4 address for SNMP traps. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure IPv4 SNMP managers (hosts).</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure IPv4 SNMP managers (hosts).</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/DEVPROF/{DEVPROF}/SYSTEM/SNMP/COMMUNITY/{COMMUNITY}/HOSTS/{HOSTS}
      fmgr_pm_config_devprof_system_snmp_community_hosts_per_object:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            devprof: <value of string>
            community: <value of string>
            hosts: <value of string>
         params:
            -
               data:
                  ha-direct: <value in [disable, enable]>
                  host-type: <value in [any, query, trap]>
                  id: <value of integer>
                  ip: <value of string>
                  source-ip: <value of string>

    - name: REQUESTING /PM/CONFIG/DEVPROF/{DEVPROF}/SYSTEM/SNMP/COMMUNITY/{COMMUNITY}/HOSTS/{HOSTS}
      fmgr_pm_config_devprof_system_snmp_community_hosts_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            devprof: <value of string>
            community: <value of string>
            hosts: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [clone, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - Host entry ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/devprof/{devprof}/system/snmp/community/{community}/hosts/{hosts}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [delete]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/devprof/{devprof}/system/snmp/community/{community}/hosts/{hosts}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> ha-direct </span> - Enable/disable direct management of HA cluster members. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> host-type </span> - Control whether the SNMP manager sends SNMP queries, receives SNMP traps, or both. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Host entry ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip </span> - IPv4 address of the SNMP manager (host). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-ip </span> - Source IPv4 address for SNMP traps. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/devprof/{devprof}/system/snmp/community/{community}/hosts/{hosts}</span>  </li>
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



