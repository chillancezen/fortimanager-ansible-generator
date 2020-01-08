:source: fmgr_pm_config_obj_firewall_vip6_realservers.py

:orphan:

.. _fmgr_pm_config_obj_firewall_vip6_realservers:

fmgr_pm_config_obj_firewall_vip6_realservers -- Select the real servers that this server load balancing VIP will distribute traffic to.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/vip6/{vip6}/realservers`
- `/pm/config/global/obj/firewall/vip6/{vip6}/realservers`
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
 <li><span class="li-head">vip6</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Select the real servers that this server load balancing VIP will distribute traffic to.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">client-ip</span> - Only clients in this IP range can connect to this real server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">healthcheck</span> - Enable to check the responsiveness of the real server before forwarding traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, vip]</span> </li>
 <li><span class="li-head">holddown-interval</span> - Time in seconds that the health check monitor continues to monitor an unresponsive server that should be active. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">http-host</span> - HTTP server domain name in HTTP header. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Real server ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - IPv6 address of the real server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-connections</span> - Max number of active connections that can directed to the real server. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">monitor</span> - Name of the health check monitor to use when polling to determine a virtual servers connectivity status. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port</span> - Port for communicating with the real server. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traffic is sent. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [active, standby, disable]</span> </li>
 <li><span class="li-head">weight</span> - Weight of the real server. <span class="li-normal">type: int</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Select the real servers that this server load balancing VIP will distribute traffic to.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [client-ip, healthcheck, holddown-interval, http-host, id, ip, max-connections, monitor, port, status, weight]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/VIP6/{VIP6}/REALSERVERS
      fmgr_pm_config_obj_firewall_vip6_realservers:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vip6: <value of string>
         params:
            -
               data:
                 -
                     client-ip: <value of string>
                     healthcheck: <value in [disable, enable, vip]>
                     holddown-interval: <value of integer>
                     http-host: <value of string>
                     id: <value of integer>
                     ip: <value of string>
                     max-connections: <value of integer>
                     monitor: <value of string>
                     port: <value of integer>
                     status: <value in [active, standby, disable]>
                     weight: <value of integer>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/VIP6/{VIP6}/REALSERVERS
      fmgr_pm_config_obj_firewall_vip6_realservers:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vip6: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [client-ip, healthcheck, holddown-interval, ...]>
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
 <li> <span class="li-return"> id </span> - Real server ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/vip6/{vip6}/realservers</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> client-ip </span> - Only clients in this IP range can connect to this real server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> healthcheck </span> - Enable to check the responsiveness of the real server before forwarding traffic. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> holddown-interval </span> - Time in seconds that the health check monitor continues to monitor an unresponsive server that should be active. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> http-host </span> - HTTP server domain name in HTTP header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Real server ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip </span> - IPv6 address of the real server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-connections </span> - Max number of active connections that can directed to the real server. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> monitor </span> - Name of the health check monitor to use when polling to determine a virtual servers connectivity status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port </span> - Port for communicating with the real server. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> status </span> - Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traffic is sent. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> weight </span> - Weight of the real server. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/vip6/{vip6}/realservers</span>  </li>
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



