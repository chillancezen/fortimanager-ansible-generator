:source: fmgr_pm_config_obj_vpnmgr_node.py

:orphan:

.. _fmgr_pm_config_obj_vpnmgr_node:

fmgr_pm_config_obj_vpnmgr_node -- VPN node for VPN Manager.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/vpnmgr/node`
- `/pm/config/global/obj/vpnmgr/node`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - VPN node for VPN Manager. Must specify vpntable and scope member.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">add-route</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">assign-ip</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">assign-ip-from</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [range, usrgrp, dhcp, name]</span> </li>
 <li><span class="li-head">authpasswd</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">authusr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">authusrgrp</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">auto-configuration</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">automatic_routing</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">banner</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">default-gateway</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dhcp-server</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dns-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, manual]</span> </li>
 <li><span class="li-head">dns-service</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, specify, local]</span> </li>
 <li><span class="li-head">domain</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extgw</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extgw_hubip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extgw_p2_per_net</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">extgwip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">hub_iface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">iface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip-range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">end-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">start-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ipsec-lease-hold</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ipv4-dns-server1</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv4-dns-server2</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv4-dns-server3</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv4-end-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv4-exclude-range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">end-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">start-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ipv4-netmask</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv4-split-include</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv4-start-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv4-wins-server1</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ipv4-wins-server2</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">local-gw</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">localid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mode-cfg</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mode-cfg-ip-version</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [4, 6]</span> </li>
 <li><span class="li-head">net-device</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">peer</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">peergrp</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">peerid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">peertype</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [any, one, dialup, peer, peergrp]</span> </li>
 <li><span class="li-head">protected_subnet</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">addr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">seq</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">public-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">role</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hub, spoke]</span> </li>
 <li><span class="li-head">route-overlap</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [use-old, use-new, allow]</span> </li>
 <li><span class="li-head">spoke-zone</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">summary_addr</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">addr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priority</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">seq</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">tunnel-search</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [selectors, nexthop]</span> </li>
 <li><span class="li-head">unity-support</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">usrgrp</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vpn-interface-priority</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vpn-zone</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vpntable</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">xauthtype</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, client, pap, chap, auto]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - VPN node for VPN Manager. Must specify vpntable and scope member.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [add-route, assign-ip, assign-ip-from, authpasswd, authusr, authusrgrp, auto-configuration, automatic_routing, banner, default-gateway, dhcp-server, dns-mode, dns-service, domain, extgw, extgw_hubip, extgw_p2_per_net, extgwip, hub_iface, id, iface, ipsec-lease-hold, ipv4-dns-server1, ipv4-dns-server2, ipv4-dns-server3, ipv4-end-ip, ipv4-netmask, ipv4-split-include, ipv4-start-ip, ipv4-wins-server1, ipv4-wins-server2, local-gw, localid, mode-cfg, mode-cfg-ip-version, net-device, peer, peergrp, peerid, peertype, public-ip, role, route-overlap, spoke-zone, tunnel-search, unity-support, usrgrp, vpn-interface-priority, vpn-zone, vpntable, xauthtype]</span> </li>
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
    - name: send request to /pm/config/obj/vpnmgr/node
      fmgr_pm_config_obj_vpnmgr_node:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            - 
               data: 
                - 
                     add-route: <value in [disable, enable]>
                     assign-ip: <value in [disable, enable]>
                     assign-ip-from: <value in [range, usrgrp, dhcp, ...]>
                     authpasswd: 
                      - <value of string>
                     authusr: <value of string>
                     authusrgrp: <value of string>
                     auto-configuration: <value in [disable, enable]>
                     automatic_routing: <value in [disable, enable]>
                     banner: <value of string>
                     default-gateway: <value of string>
                     dhcp-server: <value in [disable, enable]>
                     dns-mode: <value in [auto, manual]>
                     dns-service: <value in [default, specify, local]>
                     domain: <value of string>
                     extgw: <value of string>
                     extgw_hubip: <value of string>
                     extgw_p2_per_net: <value in [disable, enable]>
                     extgwip: <value of string>
                     hub_iface: <value of string>
                     id: <value of integer>
                     iface: <value of string>
                     ip-range: 
                      - 
                           end-ip: <value of string>
                           id: <value of integer>
                           start-ip: <value of string>
                     ipsec-lease-hold: <value of integer>
                     ipv4-dns-server1: <value of string>
                     ipv4-dns-server2: <value of string>
                     ipv4-dns-server3: <value of string>
                     ipv4-end-ip: <value of string>
                     ipv4-exclude-range: 
                      - 
                           end-ip: <value of string>
                           id: <value of integer>
                           start-ip: <value of string>
                     ipv4-netmask: <value of string>
                     ipv4-split-include: <value of string>
                     ipv4-start-ip: <value of string>
                     ipv4-wins-server1: <value of string>
                     ipv4-wins-server2: <value of string>
                     local-gw: <value of string>
                     localid: <value of string>
                     mode-cfg: <value in [disable, enable]>
                     mode-cfg-ip-version: <value in [4, 6]>
                     net-device: <value in [disable, enable]>
                     peer: <value of string>
                     peergrp: <value of string>
                     peerid: <value of string>
                     peertype: <value in [any, one, dialup, ...]>
                     protected_subnet: 
                      - 
                           addr: <value of string>
                           seq: <value of integer>
                     public-ip: <value of string>
                     role: <value in [hub, spoke]>
                     route-overlap: <value in [use-old, use-new, allow]>
                     spoke-zone: <value of string>
                     summary_addr: 
                      - 
                           addr: <value of string>
                           priority: <value of integer>
                           seq: <value of integer>
                     tunnel-search: <value in [selectors, nexthop]>
                     unity-support: <value in [disable, enable]>
                     usrgrp: <value of string>
                     vpn-interface-priority: <value of integer>
                     vpn-zone: <value of string>
                     vpntable: <value of string>
                     xauthtype: <value in [disable, client, pap, ...]>
    - name: send request to /pm/config/obj/vpnmgr/node
      fmgr_pm_config_obj_vpnmgr_node:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            - 
               attr: <value of string>
               fields: 
                - 
                   - <value in [add-route, assign-ip, assign-ip-from, ...]>
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
 <li> <span class="li-return"> id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/vpnmgr/node</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> add-route </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> assign-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> assign-ip-from </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> authpasswd </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> authusr </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> authusrgrp </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auto-configuration </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> automatic_routing </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> banner </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> default-gateway </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dhcp-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dns-mode </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dns-service </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> domain </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> extgw </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> extgw_hubip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> extgw_p2_per_net </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> extgwip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> hub_iface </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> iface </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip-range </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> end-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> start-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ipsec-lease-hold </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ipv4-dns-server1 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ipv4-dns-server2 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ipv4-dns-server3 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ipv4-end-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ipv4-exclude-range </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> end-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> start-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ipv4-netmask </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ipv4-split-include </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ipv4-start-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ipv4-wins-server1 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ipv4-wins-server2 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> local-gw </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> localid </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mode-cfg </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mode-cfg-ip-version </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> net-device </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> peer </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> peergrp </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> peerid </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> peertype </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> protected_subnet </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> addr </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> seq </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> public-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> role </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> route-overlap </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spoke-zone </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> summary_addr </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> addr </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> priority </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> seq </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> tunnel-search </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> unity-support </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> usrgrp </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vpn-interface-priority </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> vpn-zone </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vpntable </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> xauthtype </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/vpnmgr/node</span>  </li>
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



