:source: fmgr_pm_config_obj_firewall_ldb_monitor.py

:orphan:

.. _fmgr_pm_config_obj_firewall_ldb_monitor:

fmgr_pm_config_obj_firewall_ldb_monitor -- Configure server load balancing health monitors.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/ldb-monitor`
- `/pm/config/global/obj/firewall/ldb-monitor`
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
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure server load balancing health monitors.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">http-get</span> - URL used to send a GET request to check the health of an HTTP server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-match</span> - String to match the value expected in response to an HTTP-GET request. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-max-redirects</span> - The maximum number of HTTP redirects to be allowed (0 - 5, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">interval</span> - Time between health checks (5 - 65635 sec, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - Monitor name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port</span> - Service port used to perform the health check. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">retry</span> - Number health check attempts before the server is considered down (1 - 255, default = 3). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">timeout</span> - Time to wait to receive response to a health check from a server. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">type</span> - Select the Monitor type used by the health check monitor to check the health of the server (PING | TCP | HTTP). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ping, tcp, http, passive-sip]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure server load balancing health monitors.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [http-get, http-match, http-max-redirects, interval, name, port, retry, timeout, type]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/LDB-MONITOR
      fmgr_pm_config_obj_firewall_ldb_monitor:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     http-get: <value of string>
                     http-match: <value of string>
                     http-max-redirects: <value of integer>
                     interval: <value of integer>
                     name: <value of string>
                     port: <value of integer>
                     retry: <value of integer>
                     timeout: <value of integer>
                     type: <value in [ping, tcp, http, ...]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/LDB-MONITOR
      fmgr_pm_config_obj_firewall_ldb_monitor:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [http-get, http-match, http-max-redirects, ...]>
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
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/ldb-monitor</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> http-get </span> - URL used to send a GET request to check the health of an HTTP server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-match </span> - String to match the value expected in response to an HTTP-GET request. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-max-redirects </span> - The maximum number of HTTP redirects to be allowed (0 - 5, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> interval </span> - Time between health checks (5 - 65635 sec, default = 10). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> name </span> - Monitor name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port </span> - Service port used to perform the health check. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> retry </span> - Number health check attempts before the server is considered down (1 - 255, default = 3). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> timeout </span> - Time to wait to receive response to a health check from a server. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> type </span> - Select the Monitor type used by the health check monitor to check the health of the server (PING | TCP | HTTP). <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/ldb-monitor</span>  </li>
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



