:source: fmgr_pm_config_obj_ips_sensor_sensor_override.py

:orphan:

.. _fmgr_pm_config_obj_ips_sensor_sensor_override:

fmgr_pm_config_obj_ips_sensor_sensor_override -- IPS override rule.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/ips/sensor/{sensor}/override`
- `/pm/config/global/obj/ips/sensor/{sensor}/override`
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
 <li><span class="li-head">sensor</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - IPS override rule.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action of override rule. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, block, reset]</span> </li>
 <li><span class="li-head">exempt-ip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">dst-ip</span> - Destination IP address and netmask. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Exempt IP ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">src-ip</span> - Source IP address and netmask. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">log-packet</span> - Enable/disable packet logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">quarantine</span> - Quarantine IP or interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, attacker, both, interface]</span> </li>
 <li><span class="li-head">quarantine-expiry</span> - Duration of quarantine in minute. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">quarantine-log</span> - Enable/disable logging of selected quarantine. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rule-id</span> - Override rule ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Enable/disable status of override rule. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - IPS override rule.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [action, log, log-packet, quarantine, quarantine-expiry, quarantine-log, rule-id, status]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">get used</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">loadsub</span> - Enable or disable the return of any sub-objects. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [count, object member, datasrc, get reserved, syntax]</span> </li>
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
    - name: send request to /pm/config/obj/ips/sensor/{sensor}/override
      fmgr_pm_config_obj_ips_sensor_sensor_override:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            sensor: <value of string>
         params:
            - 
               data: 
                - 
                     action: <value in [pass, block, reset]>
                     exempt-ip: 
                      - 
                           dst-ip: <value of string>
                           id: <value of integer>
                           src-ip: <value of string>
                     log: <value in [disable, enable]>
                     log-packet: <value in [disable, enable]>
                     quarantine: <value in [none, attacker, both, ...]>
                     quarantine-expiry: <value of integer>
                     quarantine-log: <value in [disable, enable]>
                     rule-id: <value of integer>
                     status: <value in [disable, enable]>
    - name: send request to /pm/config/obj/ips/sensor/{sensor}/override
      fmgr_pm_config_obj_ips_sensor_sensor_override:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            sensor: <value of string>
         params:
            - 
               attr: <value of string>
               fields: 
                - 
                   - <value in [action, log, log-packet, ...]>
               filter: 
                - <value of string>
               get used: <value of integer>
               loadsub: <value of integer>
               option: <value in [count, object member, datasrc, ...]>
               range: 
                - <value of integer>
               sortings: 
                - 
                     \{attr_name\}: <value in [1, -1]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [add, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> rule-id </span> - Override rule ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/ips/sensor/{sensor}/override</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - Action of override rule. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> exempt-ip </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> dst-ip </span> - Destination IP address and netmask. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Exempt IP ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> src-ip </span> - Source IP address and netmask. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log-packet </span> - Enable/disable packet logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> quarantine </span> - Quarantine IP or interface. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> quarantine-expiry </span> - Duration of quarantine in minute. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> quarantine-log </span> - Enable/disable logging of selected quarantine. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rule-id </span> - Override rule ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable status of override rule. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/ips/sensor/{sensor}/override</span>  </li>
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



