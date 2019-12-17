:source: fmgr_pm_config_obj_wanopt_profile_profile_http.py

:orphan:

.. _fmgr_pm_config_obj_wanopt_profile_profile_http:

fmgr_pm_config_obj_wanopt_profile_profile_http -- Enable/disable HTTP WAN Optimization and configure HTTP WAN Optimization features.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/wanopt/profile/{profile}/http`
- `/pm/config/global/obj/wanopt/profile/{profile}/http`
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
 <li><span class="li-head">profile</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Enable/disable HTTP WAN Optimization and configure HTTP WAN Optimization features.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Enable/disable HTTP WAN Optimization and configure HTTP WAN Optimization features.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">byte-caching</span> - Enable/disable byte-caching for HTTP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">log-traffic</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">port</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">prefer-chunking</span> - Select dynamic or fixed-size data chunking for HTTP WAN Optimization. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [dynamic, fix]</span> </li>
 <li><span class="li-head">secure-tunnel</span> - Enable/disable securing the WAN Opt tunnel using SSL. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl</span> - Enable/disable SSL/TLS offloading (hardware acceleration) for HTTPS traffic in this tunnel. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-port</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">status</span> - Enable/disable HTTP WAN Optimization. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tunnel-non-http</span> - Configure how to process non-HTTP traffic when a profile configured for HTTP traffic accepts a non-HTTP session. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tunnel-sharing</span> - Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive protocols. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [private, shared, express-shared]</span> </li>
 <li><span class="li-head">unknown-http-version</span> - How to handle HTTP sessions that do not comply with HTTP 0. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [best-effort, reject, tunnel]</span> </li>
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
    - name: send request to /pm/config/obj/wanopt/profile/{profile}/http
      fmgr_pm_config_obj_wanopt_profile_profile_http:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            - 
               option: <value in [object member, chksum, datasrc]>
    - name: send request to /pm/config/obj/wanopt/profile/{profile}/http
      fmgr_pm_config_obj_wanopt_profile_profile_http:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            - 
               data: 
                  byte-caching: <value in [disable, enable]>
                  log-traffic: <value in [disable, enable]>
                  port: 
                   - <value of integer>
                  prefer-chunking: <value in [dynamic, fix]>
                  secure-tunnel: <value in [disable, enable]>
                  ssl: <value in [disable, enable]>
                  ssl-port: 
                   - <value of integer>
                  status: <value in [disable, enable]>
                  tunnel-non-http: <value in [disable, enable]>
                  tunnel-sharing: <value in [private, shared, express-shared]>
                  unknown-http-version: <value in [best-effort, reject, tunnel]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> byte-caching </span> - Enable/disable byte-caching for HTTP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log-traffic </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> prefer-chunking </span> - Select dynamic or fixed-size data chunking for HTTP WAN Optimization. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> secure-tunnel </span> - Enable/disable securing the WAN Opt tunnel using SSL. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl </span> - Enable/disable SSL/TLS offloading (hardware acceleration) for HTTPS traffic in this tunnel. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-port </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> status </span> - Enable/disable HTTP WAN Optimization. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tunnel-non-http </span> - Configure how to process non-HTTP traffic when a profile configured for HTTP traffic accepts a non-HTTP session. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tunnel-sharing </span> - Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive protocols. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> unknown-http-version </span> - How to handle HTTP sessions that do not comply with HTTP 0. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wanopt/profile/{profile}/http</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wanopt/profile/{profile}/http</span>  </li>
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



