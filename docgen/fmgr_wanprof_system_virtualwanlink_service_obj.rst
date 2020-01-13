:source: fmgr_wanprof_system_virtualwanlink_service_obj.py

:orphan:

.. _fmgr_wanprof_system_virtualwanlink_service_obj:

fmgr_wanprof_system_virtualwanlink_service_obj -- Create SD-WAN rules or priority rules (also called services) to control how sessions are distributed to physical interfaces in the SD-WAN.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, move, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/service/{service}`
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
 <li><span class="li-head">service</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Create SD-WAN rules or priority rules (also called services) to control how sessions are distributed to physical interfaces in the SD-WAN.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">addr-mode</span> - Address mode (IPv4 or IPv6). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipv4, ipv6]</span> </li>
 <li><span class="li-head">bandwidth-weight</span> - Coefficient of reciprocal of available bidirectional bandwidth in the formula of custom-profile-1. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">default</span> - Enable/disable use of SD-WAN as default service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dscp-forward</span> - Enable/disable forward traffic DSCP tag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dscp-forward-tag</span> - Forward traffic DSCP tag. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dscp-reverse</span> - Enable/disable reverse traffic DSCP tag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dscp-reverse-tag</span> - Reverse traffic DSCP tag. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dst</span> - Destination address name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dst-negate</span> - Enable/disable negation of destination address match. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dst6</span> - Destination address6 name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">end-port</span> - End destination port number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">gateway</span> - Enable/disable SD-WAN service gateway. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">groups</span> - User groups. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">health-check</span> - Health check. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">hold-down-time</span> - Waiting period in seconds when switching from the back-up member to the primary member (0 - 10000000, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">id</span> - Priority rule ID (1 - 4000). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">internet-service</span> - Enable/disable use of Internet service for application-based load balancing. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">internet-service-ctrl</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">internet-service-ctrl-group</span> - Control-based Internet Service group list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-custom</span> - Custom Internet service name list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-custom-group</span> - Custom Internet Service group list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-group</span> - Internet Service group list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-id</span> - Internet service ID list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">jitter-weight</span> - Coefficient of jitter in the formula of custom-profile-1. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">latency-weight</span> - Coefficient of latency in the formula of custom-profile-1. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">link-cost-factor</span> - Link cost factor. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [latency, jitter, packet-loss, inbandwidth, outbandwidth, bibandwidth, custom-profile-1]</span> </li>
 <li><span class="li-head">link-cost-threshold</span> - Percentage threshold change of link cost values that will result in policy route regeneration (0 - 10000000, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">member</span> - Member sequence number. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mode</span> - Control how the priority rule sets the priority of interfaces in the SD-WAN. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, manual, priority, sla, load-balance]</span> </li>
 <li><span class="li-head">name</span> - Priority rule name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">packet-loss-weight</span> - Coefficient of packet-loss in the formula of custom-profile-1. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">priority-members</span> - Member sequence number list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">protocol</span> - Protocol number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">quality-link</span> - Quality grade. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">route-tag</span> - IPv4 route map route-tag. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sla</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">health-check</span> - Virtual WAN Link health-check. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - SLA ID. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">src</span> - Source address name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">src-negate</span> - Enable/disable negation of source address match. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">src6</span> - Source address6 name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">start-port</span> - Start destination port number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Enable/disable SD-WAN service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tos</span> - Type of service bit pattern. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tos-mask</span> - Type of service evaluated bits. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">users</span> - User name. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Create SD-WAN rules or priority rules (also called services) to control how sessions are distributed to physical interfaces in the SD-WAN.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Create SD-WAN rules or priority rules (also called services) to control how sessions are distributed to physical interfaces in the SD-WAN.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [move]</span> - Create SD-WAN rules or priority rules (also called services) to control how sessions are distributed to physical interfaces in the SD-WAN.</li>
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

    - name: REQUESTING /PM/CONFIG/WANPROF/{WANPROF}/SYSTEM/VIRTUAL-WAN-LINK/SERVICE/{SERVICE}
      fmgr_wanprof_system_virtualwanlink_service_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wanprof: <value of string>
            service: <value of string>
         params:
            -
               data:
                  addr-mode: <value in [ipv4, ipv6]>
                  bandwidth-weight: <value of integer>
                  default: <value in [disable, enable]>
                  dscp-forward: <value in [disable, enable]>
                  dscp-forward-tag: <value of string>
                  dscp-reverse: <value in [disable, enable]>
                  dscp-reverse-tag: <value of string>
                  dst: <value of string>
                  dst-negate: <value in [disable, enable]>
                  dst6: <value of string>
                  end-port: <value of integer>
                  gateway: <value in [disable, enable]>
                  groups: <value of string>
                  health-check: <value of string>
                  hold-down-time: <value of integer>
                  id: <value of integer>
                  internet-service: <value in [disable, enable]>
                  internet-service-ctrl:
                    - <value of integer>
                  internet-service-ctrl-group: <value of string>
                  internet-service-custom: <value of string>
                  internet-service-custom-group: <value of string>
                  internet-service-group: <value of string>
                  internet-service-id: <value of string>
                  jitter-weight: <value of integer>
                  latency-weight: <value of integer>
                  link-cost-factor: <value in [latency, jitter, packet-loss, ...]>
                  link-cost-threshold: <value of integer>
                  member: <value of string>
                  mode: <value in [auto, manual, priority, ...]>
                  name: <value of string>
                  packet-loss-weight: <value of integer>
                  priority-members: <value of string>
                  protocol: <value of integer>
                  quality-link: <value of integer>
                  route-tag: <value of integer>
                  sla:
                    -
                        health-check: <value of string>
                        id: <value of integer>
                  src: <value of string>
                  src-negate: <value in [disable, enable]>
                  src6: <value of string>
                  start-port: <value of integer>
                  status: <value in [disable, enable]>
                  tos: <value of string>
                  tos-mask: <value of string>
                  users: <value of string>

    - name: REQUESTING /PM/CONFIG/WANPROF/{WANPROF}/SYSTEM/VIRTUAL-WAN-LINK/SERVICE/{SERVICE}
      fmgr_wanprof_system_virtualwanlink_service_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wanprof: <value of string>
            service: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/WANPROF/{WANPROF}/SYSTEM/VIRTUAL-WAN-LINK/SERVICE/{SERVICE}
      fmgr_wanprof_system_virtualwanlink_service_obj:
         method: <value in [move]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wanprof: <value of string>
            service: <value of string>
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
 <li> <span class="li-return"> id </span> - Priority rule ID (1 - 4000). <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/service/{service}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [delete]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/service/{service}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> addr-mode </span> - Address mode (IPv4 or IPv6). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> bandwidth-weight </span> - Coefficient of reciprocal of available bidirectional bandwidth in the formula of custom-profile-1. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> default </span> - Enable/disable use of SD-WAN as default service. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dscp-forward </span> - Enable/disable forward traffic DSCP tag. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dscp-forward-tag </span> - Forward traffic DSCP tag. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dscp-reverse </span> - Enable/disable reverse traffic DSCP tag. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dscp-reverse-tag </span> - Reverse traffic DSCP tag. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dst </span> - Destination address name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dst-negate </span> - Enable/disable negation of destination address match. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dst6 </span> - Destination address6 name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> end-port </span> - End destination port number. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> gateway </span> - Enable/disable SD-WAN service gateway. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> groups </span> - User groups. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> health-check </span> - Health check. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> hold-down-time </span> - Waiting period in seconds when switching from the back-up member to the primary member (0 - 10000000, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> id </span> - Priority rule ID (1 - 4000). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> internet-service </span> - Enable/disable use of Internet service for application-based load balancing. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-ctrl </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> internet-service-ctrl-group </span> - Control-based Internet Service group list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-custom </span> - Custom Internet service name list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-custom-group </span> - Custom Internet Service group list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-group </span> - Internet Service group list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-id </span> - Internet service ID list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> jitter-weight </span> - Coefficient of jitter in the formula of custom-profile-1. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> latency-weight </span> - Coefficient of latency in the formula of custom-profile-1. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> link-cost-factor </span> - Link cost factor. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> link-cost-threshold </span> - Percentage threshold change of link cost values that will result in policy route regeneration (0 - 10000000, default = 10). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> member </span> - Member sequence number. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mode </span> - Control how the priority rule sets the priority of interfaces in the SD-WAN. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Priority rule name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> packet-loss-weight </span> - Coefficient of packet-loss in the formula of custom-profile-1. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> priority-members </span> - Member sequence number list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> protocol </span> - Protocol number. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> quality-link </span> - Quality grade. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> route-tag </span> - IPv4 route map route-tag. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> sla </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> health-check </span> - Virtual WAN Link health-check. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - SLA ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> src </span> - Source address name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> src-negate </span> - Enable/disable negation of source address match. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> src6 </span> - Source address6 name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> start-port </span> - Start destination port number. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable SD-WAN service. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tos </span> - Type of service bit pattern. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tos-mask </span> - Type of service evaluated bits. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> users </span> - User name. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/service/{service}</span>  </li>
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



