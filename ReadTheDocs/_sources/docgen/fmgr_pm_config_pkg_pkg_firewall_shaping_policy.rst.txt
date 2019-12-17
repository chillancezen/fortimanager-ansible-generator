:source: fmgr_pm_config_pkg_pkg_firewall_shaping_policy.py

:orphan:

.. _fmgr_pm_config_pkg_pkg_firewall_shaping_policy:

fmgr_pm_config_pkg_pkg_firewall_shaping_policy -- Configure shaping policies.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/pkg/{pkg}/firewall/shaping-policy`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure shaping policies.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">app-category</span> - IDs of one or more application categories that this shaper applies application control traffic shaping to. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">application</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">dstaddr</span> - IPv4 destination address and address group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr6</span> - IPv6 destination address and address group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstintf</span> - One or more outgoing (egress) interfaces. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">groups</span> - Apply this traffic shaping policy to user groups that have authenticated with the FortiGate. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Shaping policy ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip-version</span> - Apply this traffic shaping policy to IPv4 or IPv6 traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [4, 6]</span> </li>
 <li><span class="li-head">per-ip-shaper</span> - Per-IP traffic shaper to apply with this policy. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">schedule</span> - Schedule name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service</span> - Service and service group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr</span> - IPv4 source address and address group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr6</span> - IPv6 source address and address group names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable this traffic shaping policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">traffic-shaper</span> - Traffic shaper to apply to traffic forwarded by the firewall policy. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">traffic-shaper-reverse</span> - Traffic shaper to apply to response traffic received by the firewall policy. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">url-category</span> - IDs of one or more FortiGuard Web Filtering categories that this shaper applies traffic shaping to. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">users</span> - Apply this traffic shaping policy to individual users that have authenticated with the FortiGate. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure shaping policies.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [app-category, application, dstaddr, dstaddr6, dstintf, groups, id, ip-version, per-ip-shaper, schedule, service, srcaddr, srcaddr6, status, traffic-shaper, traffic-shaper-reverse, url-category, users]</span> </li>
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
    - name: send request to /pm/config/pkg/{pkg}/firewall/shaping-policy
      fmgr_pm_config_pkg_pkg_firewall_shaping_policy:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
         params:
            - 
               data: 
                - 
                     app-category: <value of string>
                     application: 
                      - <value of integer>
                     dstaddr: <value of string>
                     dstaddr6: <value of string>
                     dstintf: <value of string>
                     groups: <value of string>
                     id: <value of integer>
                     ip-version: <value in [4, 6]>
                     per-ip-shaper: <value of string>
                     schedule: <value of string>
                     service: <value of string>
                     srcaddr: <value of string>
                     srcaddr6: <value of string>
                     status: <value in [disable, enable]>
                     traffic-shaper: <value of string>
                     traffic-shaper-reverse: <value of string>
                     url-category: <value of string>
                     users: <value of string>
    - name: send request to /pm/config/pkg/{pkg}/firewall/shaping-policy
      fmgr_pm_config_pkg_pkg_firewall_shaping_policy:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
         params:
            - 
               attr: <value of string>
               fields: 
                - 
                   - <value in [app-category, application, dstaddr, ...]>
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
 <li> <span class="li-return"> id </span> - Shaping policy ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/shaping-policy</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> app-category </span> - IDs of one or more application categories that this shaper applies application control traffic shaping to. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> application </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> dstaddr </span> - IPv4 destination address and address group names. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstaddr6 </span> - IPv6 destination address and address group names. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstintf </span> - One or more outgoing (egress) interfaces. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> groups </span> - Apply this traffic shaping policy to user groups that have authenticated with the FortiGate. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Shaping policy ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip-version </span> - Apply this traffic shaping policy to IPv4 or IPv6 traffic. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> per-ip-shaper </span> - Per-IP traffic shaper to apply with this policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> schedule </span> - Schedule name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> service </span> - Service and service group names. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcaddr </span> - IPv4 source address and address group names. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcaddr6 </span> - IPv6 source address and address group names. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable this traffic shaping policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> traffic-shaper </span> - Traffic shaper to apply to traffic forwarded by the firewall policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> traffic-shaper-reverse </span> - Traffic shaper to apply to response traffic received by the firewall policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> url-category </span> - IDs of one or more FortiGuard Web Filtering categories that this shaper applies traffic shaping to. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> users </span> - Apply this traffic shaping policy to individual users that have authenticated with the FortiGate. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/shaping-policy</span>  </li>
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



