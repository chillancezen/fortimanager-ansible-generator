:source: fmgr_pm_config_obj_firewall_identity_based_route_identity_based_route_rule_rule.py

:orphan:

.. _fmgr_pm_config_obj_firewall_identity_based_route_identity_based_route_rule_rule:

fmgr_pm_config_obj_firewall_identity_based_route_identity_based_route_rule_rule -- Rule.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/identity-based-route/{identity-based-route}/rule/{rule}`
- `/pm/config/global/obj/firewall/identity-based-route/{identity-based-route}/rule/{rule}`
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
 <li><span class="li-head">identity-based-route</span> - the object name <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rule</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Rule.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">device</span> - Outgoing interface for the rule. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gateway</span> - IPv4 address of the gateway (Format: xxx. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">groups</span> - Select one or more group(s) from available groups that are allowed to use this route. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Rule ID. <span class="li-normal">type: int</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Rule.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Rule.</li>
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
    - name: send request to /pm/config/obj/firewall/identity-based-route/{identity-based-route}/rule/{rule}
      fmgr_pm_config_obj_firewall_identity_based_route_identity_based_route_rule_rule:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            identity-based-route: <value of string>
            rule: <value of string>
         params:
            - 
               data: 
                  device: <value of string>
                  gateway: <value of string>
                  groups: <value of string>
                  id: <value of integer>
    - name: send request to /pm/config/obj/firewall/identity-based-route/{identity-based-route}/rule/{rule}
      fmgr_pm_config_obj_firewall_identity_based_route_identity_based_route_rule_rule:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            identity-based-route: <value of string>
            rule: <value of string>
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
 <li> <span class="li-return"> id </span> - Rule ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/identity-based-route/{identity-based-route}/rule/{rule}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [delete]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/identity-based-route/{identity-based-route}/rule/{rule}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> device </span> - Outgoing interface for the rule. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> gateway </span> - IPv4 address of the gateway (Format: xxx. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> groups </span> - Select one or more group(s) from available groups that are allowed to use this route. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Rule ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/identity-based-route/{identity-based-route}/rule/{rule}</span>  </li>
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



