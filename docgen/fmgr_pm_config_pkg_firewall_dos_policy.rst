:source: fmgr_pm_config_pkg_firewall_dos_policy.py

:orphan:

.. _fmgr_pm_config_pkg_firewall_dos_policy:

fmgr_pm_config_pkg_firewall_dos_policy -- Configure IPv4 DoS policies.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/pkg/{pkg}/firewall/DoS-policy`
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
 <li><span class="li-head">pkg</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure IPv4 DoS policies.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">anomaly</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action taken when the threshold is reached. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, block, proxy]</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging for this anomaly. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - Anomaly name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">quarantine</span> - Quarantine method. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, attacker, both, interface]</span> </li>
 <li><span class="li-head">quarantine-expiry</span> - Duration of quarantine, from 1 minute to 364 days, 23 hours, and 59 minutes from now. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">quarantine-log</span> - Enable/disable quarantine logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the active status of this anomaly sensor. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">threshold</span> - Number of detected instances per minute which triggers action (1 - 2147483647, default = 1000). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold(default)</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">comments</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr</span> - Destination address name from available addresses. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">interface</span> - Incoming interface name from available interfaces. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">policyid</span> - Policy ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">service</span> - Service object from available options. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr</span> - Source address name from available addresses. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable this policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure IPv4 DoS policies.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [comments, dstaddr, interface, policyid, service, srcaddr, status]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/DOS-POLICY
      fmgr_pm_config_pkg_firewall_dos_policy:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
         params:
            -
               data:
                 -
                     anomaly:
                       -
                           action: <value in [pass, block, proxy]>
                           log: <value in [disable, enable]>
                           name: <value of string>
                           quarantine: <value in [none, attacker, both, ...]>
                           quarantine-expiry: <value of string>
                           quarantine-log: <value in [disable, enable]>
                           status: <value in [disable, enable]>
                           threshold: <value of integer>
                           threshold(default): <value of integer>
                     comments: <value of string>
                     dstaddr: <value of string>
                     interface: <value of string>
                     policyid: <value of integer>
                     service: <value of string>
                     srcaddr: <value of string>
                     status: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/DOS-POLICY
      fmgr_pm_config_pkg_firewall_dos_policy:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [comments, dstaddr, interface, ...]>
               filter:
                 - <value of string>
               get used: <value of integer>
               loadsub: <value of integer>
               option: <value in [count, object member, datasrc, ...]>
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
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> policyid </span> - Policy ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/DoS-policy</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> anomaly </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - Action taken when the threshold is reached. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging for this anomaly. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Anomaly name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> quarantine </span> - Quarantine method. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> quarantine-expiry </span> - Duration of quarantine, from 1 minute to 364 days, 23 hours, and 59 minutes from now. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> quarantine-log </span> - Enable/disable quarantine logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable the active status of this anomaly sensor. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> threshold </span> - Number of detected instances per minute which triggers action (1 - 2147483647, default = 1000). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> threshold(default) </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> comments </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstaddr </span> - Destination address name from available addresses. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> interface </span> - Incoming interface name from available interfaces. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> policyid </span> - Policy ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> service </span> - Service object from available options. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcaddr </span> - Source address name from available addresses. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable this policy. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/DoS-policy</span>  </li>
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



