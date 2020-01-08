:source: fmgr_pm_config_pkg_firewall_policy46_per_object.py

:orphan:

.. _fmgr_pm_config_pkg_firewall_policy46_per_object:

fmgr_pm_config_pkg_firewall_policy46_per_object -- Configure IPv4 to IPv6 policies.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, move, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/pkg/{pkg}/firewall/policy46/{policy46}`
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
 <li><span class="li-head">policy46</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure IPv4 to IPv6 policies.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Accept or deny traffic matching the policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, accept]</span> </li>
 <li><span class="li-head">comments</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr</span> - Destination address objects. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstintf</span> - Destination interface name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fixedport</span> - Enable/disable fixed port for this policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">logtraffic</span> - Enable/disable traffic logging for this policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">per-ip-shaper</span> - Per IP traffic shaper. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">permit-any-host</span> - Enable/disable allowing any host. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">policyid</span> - Policy ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">schedule</span> - Schedule name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service</span> - Service name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr</span> - Source address objects. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcintf</span> - Source interface name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable this policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tags</span> - Applied object tags. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tcp-mss-receiver</span> - TCP Maximum Segment Size value of receiver (0 - 65535, default = 0) <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-mss-sender</span> - TCP Maximum Segment Size value of sender (0 - 65535, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">traffic-shaper</span> - Traffic shaper. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">traffic-shaper-reverse</span> - Reverse traffic shaper. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">uuid</span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure IPv4 to IPv6 policies.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure IPv4 to IPv6 policies.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [move]</span> - Configure IPv4 to IPv6 policies.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [before, after]</span> </li>
 <li><span class="li-head">target</span> - Key to the target entry. <span class="li-normal">type: str</span> </li>
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

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/POLICY46/{POLICY46}
      fmgr_pm_config_pkg_firewall_policy46_per_object:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            policy46: <value of string>
         params:
            -
               data:
                  action: <value in [deny, accept]>
                  comments: <value of string>
                  dstaddr: <value of string>
                  dstintf: <value of string>
                  fixedport: <value in [disable, enable]>
                  logtraffic: <value in [disable, enable]>
                  per-ip-shaper: <value of string>
                  permit-any-host: <value in [disable, enable]>
                  policyid: <value of integer>
                  schedule: <value of string>
                  service: <value of string>
                  srcaddr: <value of string>
                  srcintf: <value of string>
                  status: <value in [disable, enable]>
                  tags: <value of string>
                  tcp-mss-receiver: <value of integer>
                  tcp-mss-sender: <value of integer>
                  traffic-shaper: <value of string>
                  traffic-shaper-reverse: <value of string>
                  uuid: <value of string>

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/POLICY46/{POLICY46}
      fmgr_pm_config_pkg_firewall_policy46_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            policy46: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/POLICY46/{POLICY46}
      fmgr_pm_config_pkg_firewall_policy46_per_object:
         method: <value in [move]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            policy46: <value of string>
         params:
            -
               option: <value in [before, after]>
               target: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [clone, move, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> policyid </span> - Policy ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/policy46/{policy46}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [delete]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/policy46/{policy46}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - Accept or deny traffic matching the policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> comments </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstaddr </span> - Destination address objects. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstintf </span> - Destination interface name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fixedport </span> - Enable/disable fixed port for this policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> logtraffic </span> - Enable/disable traffic logging for this policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> per-ip-shaper </span> - Per IP traffic shaper. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> permit-any-host </span> - Enable/disable allowing any host. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> policyid </span> - Policy ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> schedule </span> - Schedule name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> service </span> - Service name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcaddr </span> - Source address objects. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcintf </span> - Source interface name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable this policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tags </span> - Applied object tags. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tcp-mss-receiver </span> - TCP Maximum Segment Size value of receiver (0 - 65535, default = 0) <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> tcp-mss-sender </span> - TCP Maximum Segment Size value of sender (0 - 65535, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> traffic-shaper </span> - Traffic shaper. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> traffic-shaper-reverse </span> - Reverse traffic shaper. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> uuid </span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/policy46/{policy46}</span>  </li>
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



