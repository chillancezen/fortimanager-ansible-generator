:source: fmgr_pm_config_wanprof_system_virtual_wan_link_members.py

:orphan:

.. _fmgr_pm_config_wanprof_system_virtual_wan_link_members:

fmgr_pm_config_wanprof_system_virtual_wan_link_members -- Physical FortiGate interfaces added to the virtual-wan-link.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/members`
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
 <li><span class="li-head">wanprof</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Physical FortiGate interfaces added to the virtual-wan-link.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_dynamic-member</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">comment</span> - Comments. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gateway</span> - The default gateway for this interface. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gateway6</span> - IPv6 gateway. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ingress-spillover-threshold</span> - Ingress spillover threshold for this interface (0 - 16776000 kbit/s). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">interface</span> - Interface name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priority</span> - Priority of the interface (0 - 4294967295). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">seq-num</span> - Sequence number(1-255). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">source</span> - Source IP address used in the health-check packet to the server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source6</span> - Source IPv6 address used in the health-check packet to the server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spillover-threshold</span> - Egress spillover threshold for this interface (0 - 16776000 kbit/s). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Enable/disable this interface in the SD-WAN. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">volume-ratio</span> - Measured volume ratio (this value / sum of all values = percentage of link volume, 0 - 255). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">weight</span> - Weight of this interface for weighted load balancing. <span class="li-normal">type: int</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Physical FortiGate interfaces added to the virtual-wan-link.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [_dynamic-member, comment, gateway, gateway6, ingress-spillover-threshold, interface, priority, seq-num, source, source6, spillover-threshold, status, volume-ratio, weight]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/WANPROF/{WANPROF}/SYSTEM/VIRTUAL-WAN-LINK/MEMBERS
      fmgr_pm_config_wanprof_system_virtual_wan_link_members:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wanprof: <value of string>
         params:
            -
               data:
                 -
                     _dynamic-member: <value of string>
                     comment: <value of string>
                     gateway: <value of string>
                     gateway6: <value of string>
                     ingress-spillover-threshold: <value of integer>
                     interface: <value of string>
                     priority: <value of integer>
                     seq-num: <value of integer>
                     source: <value of string>
                     source6: <value of string>
                     spillover-threshold: <value of integer>
                     status: <value in [disable, enable]>
                     volume-ratio: <value of integer>
                     weight: <value of integer>

    - name: REQUESTING /PM/CONFIG/WANPROF/{WANPROF}/SYSTEM/VIRTUAL-WAN-LINK/MEMBERS
      fmgr_pm_config_wanprof_system_virtual_wan_link_members:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wanprof: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [_dynamic-member, comment, gateway, ...]>
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
 <li> <span class="li-return"> seq-num </span> - Sequence number(1-255). <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/members</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> _dynamic-member </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> comment </span> - Comments. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> gateway </span> - The default gateway for this interface. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> gateway6 </span> - IPv6 gateway. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ingress-spillover-threshold </span> - Ingress spillover threshold for this interface (0 - 16776000 kbit/s). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> interface </span> - Interface name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> priority </span> - Priority of the interface (0 - 4294967295). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> seq-num </span> - Sequence number(1-255). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> source </span> - Source IP address used in the health-check packet to the server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source6 </span> - Source IPv6 address used in the health-check packet to the server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spillover-threshold </span> - Egress spillover threshold for this interface (0 - 16776000 kbit/s). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable this interface in the SD-WAN. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> volume-ratio </span> - Measured volume ratio (this value / sum of all values = percentage of link volume, 0 - 255). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> weight </span> - Weight of this interface for weighted load balancing. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/members</span>  </li>
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



