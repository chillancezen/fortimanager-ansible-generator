:source: fmgr_pm_config_obj_dynamic_virtual_wan_link_members_members.py

:orphan:

.. _fmgr_pm_config_obj_dynamic_virtual_wan_link_members_members:

fmgr_pm_config_obj_dynamic_virtual_wan_link_members_members
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/dynamic/virtual-wan-link/members/{members}`
- `/pm/config/global/obj/dynamic/virtual-wan-link/members/{members}`
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
 <li><span class="li-head">members</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cost</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detect-failtime</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detect-http-get</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">detect-http-match</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">detect-http-port</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detect-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detect-protocol</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ping, tcp-echo, udp-echo, http]</span> </li>
 <li><span class="li-head">detect-recoverytime</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detect-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">detect-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dynamic_mapping</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cost</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detect-failtime</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detect-http-get</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">detect-http-match</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">detect-http-port</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detect-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detect-protocol</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ping, tcp-echo, udp-echo, http]</span> </li>
 <li><span class="li-head">detect-recoverytime</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">detect-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">detect-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">gateway</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gateway6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ingress-spillover-threshold</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priority</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">source</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spillover-threshold</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">volume-ratio</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">weight</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">gateway</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gateway6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ingress-spillover-threshold</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priority</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">source</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spillover-threshold</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">volume-ratio</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">weight</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - </li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - </li>
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
    - name: send request to /pm/config/obj/dynamic/virtual-wan-link/members/{members}
      fmgr_pm_config_obj_dynamic_virtual_wan_link_members_members:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            members: <value of string>
         params:
            - 
               data: 
                  comment: <value of string>
                  cost: <value of integer>
                  detect-failtime: <value of integer>
                  detect-http-get: <value of string>
                  detect-http-match: <value of string>
                  detect-http-port: <value of integer>
                  detect-interval: <value of integer>
                  detect-protocol: <value in [ping, tcp-echo, udp-echo, ...]>
                  detect-recoverytime: <value of integer>
                  detect-server: <value of string>
                  detect-timeout: <value of integer>
                  dynamic_mapping: 
                   - 
                        _scope: 
                         - 
                              name: <value of string>
                              vdom: <value of string>
                        comment: <value of string>
                        cost: <value of integer>
                        detect-failtime: <value of integer>
                        detect-http-get: <value of string>
                        detect-http-match: <value of string>
                        detect-http-port: <value of integer>
                        detect-interval: <value of integer>
                        detect-protocol: <value in [ping, tcp-echo, udp-echo, ...]>
                        detect-recoverytime: <value of integer>
                        detect-server: <value of string>
                        detect-timeout: <value of integer>
                        gateway: <value of string>
                        gateway6: <value of string>
                        ingress-spillover-threshold: <value of integer>
                        interface: <value of string>
                        priority: <value of integer>
                        source: <value of string>
                        source6: <value of string>
                        spillover-threshold: <value of integer>
                        status: <value in [disable, enable]>
                        volume-ratio: <value of integer>
                        weight: <value of integer>
                  gateway: <value of string>
                  gateway6: <value of string>
                  ingress-spillover-threshold: <value of integer>
                  interface: <value of string>
                  name: <value of string>
                  priority: <value of integer>
                  source: <value of string>
                  source6: <value of string>
                  spillover-threshold: <value of integer>
                  status: <value in [disable, enable]>
                  volume-ratio: <value of integer>
                  weight: <value of integer>
    - name: send request to /pm/config/obj/dynamic/virtual-wan-link/members/{members}
      fmgr_pm_config_obj_dynamic_virtual_wan_link_members_members:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            members: <value of string>
         params:
            - 
               option: <value in [object member, chksum, datasrc]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [clone, delete, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/dynamic/virtual-wan-link/members/{members}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> comment </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> cost </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> detect-failtime </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> detect-http-get </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> detect-http-match </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> detect-http-port </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> detect-interval </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> detect-protocol </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> detect-recoverytime </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> detect-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> detect-timeout </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> dynamic_mapping </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> _scope </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> comment </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> cost </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> detect-failtime </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> detect-http-get </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> detect-http-match </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> detect-http-port </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> detect-interval </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> detect-protocol </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> detect-recoverytime </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> detect-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> detect-timeout </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> gateway </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> gateway6 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ingress-spillover-threshold </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> interface </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> priority </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> source </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source6 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spillover-threshold </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> status </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> volume-ratio </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> weight </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> gateway </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> gateway6 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ingress-spillover-threshold </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> interface </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> priority </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> source </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source6 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spillover-threshold </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> status </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> volume-ratio </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> weight </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/dynamic/virtual-wan-link/members/{members}</span>  </li>
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



