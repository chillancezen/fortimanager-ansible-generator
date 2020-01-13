:source: fmgr_fsp_vlan_interface_ipv6.py

:orphan:

.. _fmgr_fsp_vlan_interface_ipv6:

fmgr_fsp_vlan_interface_ipv6
++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/interface/ipv6`
- `/pm/config/global/obj/fsp/vlan/{vlan}/interface/ipv6`
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
 <li><span class="li-head">vlan</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">autoconf</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp6-client-options</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rapid, iapd, iana, dns, dnsname]</span> </li>
 </ul>
 <li><span class="li-head">dhcp6-information-request</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp6-prefix-delegation</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp6-prefix-hint</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dhcp6-prefix-hint-plt</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dhcp6-prefix-hint-vlt</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dhcp6-relay-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dhcp6-relay-service</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp6-relay-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular]</span> </li>
 <li><span class="li-head">ip6-address</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip6-allowaccess</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, capwap]</span> </li>
 </ul>
 <li><span class="li-head">ip6-default-life</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-dns-server-override</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip6-hop-limit</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-link-mtu</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-manage-flag</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip6-max-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-min-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, dhcp, pppoe, delegated]</span> </li>
 <li><span class="li-head">ip6-other-flag</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip6-reachable-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-retrans-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip6-send-adv</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip6-subnet</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip6-upstream-interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nd-cert</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nd-cga-modifier</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nd-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [basic, SEND-compatible]</span> </li>
 <li><span class="li-head">nd-security-level</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">nd-timestamp-delta</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">nd-timestamp-fuzz</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vrip6_link_local</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vrrp-virtual-mac6</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FSP/VLAN/{VLAN}/INTERFACE/IPV6
      fmgr_fsp_vlan_interface_ipv6:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vlan: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/FSP/VLAN/{VLAN}/INTERFACE/IPV6
      fmgr_fsp_vlan_interface_ipv6:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vlan: <value of string>
         params:
            -
               data:
                  autoconf: <value in [disable, enable]>
                  dhcp6-client-options:
                    - <value in [rapid, iapd, iana, ...]>
                  dhcp6-information-request: <value in [disable, enable]>
                  dhcp6-prefix-delegation: <value in [disable, enable]>
                  dhcp6-prefix-hint: <value of string>
                  dhcp6-prefix-hint-plt: <value of integer>
                  dhcp6-prefix-hint-vlt: <value of integer>
                  dhcp6-relay-ip: <value of string>
                  dhcp6-relay-service: <value in [disable, enable]>
                  dhcp6-relay-type: <value in [regular]>
                  ip6-address: <value of string>
                  ip6-allowaccess:
                    - <value in [https, ping, ssh, ...]>
                  ip6-default-life: <value of integer>
                  ip6-dns-server-override: <value in [disable, enable]>
                  ip6-hop-limit: <value of integer>
                  ip6-link-mtu: <value of integer>
                  ip6-manage-flag: <value in [disable, enable]>
                  ip6-max-interval: <value of integer>
                  ip6-min-interval: <value of integer>
                  ip6-mode: <value in [static, dhcp, pppoe, ...]>
                  ip6-other-flag: <value in [disable, enable]>
                  ip6-reachable-time: <value of integer>
                  ip6-retrans-time: <value of integer>
                  ip6-send-adv: <value in [disable, enable]>
                  ip6-subnet: <value of string>
                  ip6-upstream-interface: <value of string>
                  nd-cert: <value of string>
                  nd-cga-modifier: <value of string>
                  nd-mode: <value in [basic, SEND-compatible]>
                  nd-security-level: <value of integer>
                  nd-timestamp-delta: <value of integer>
                  nd-timestamp-fuzz: <value of integer>
                  vrip6_link_local: <value of string>
                  vrrp-virtual-mac6: <value in [disable, enable]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> autoconf </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dhcp6-client-options </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> dhcp6-information-request </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dhcp6-prefix-delegation </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dhcp6-prefix-hint </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dhcp6-prefix-hint-plt </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> dhcp6-prefix-hint-vlt </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> dhcp6-relay-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dhcp6-relay-service </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dhcp6-relay-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip6-address </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip6-allowaccess </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ip6-default-life </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip6-dns-server-override </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip6-hop-limit </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip6-link-mtu </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip6-manage-flag </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip6-max-interval </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip6-min-interval </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip6-mode </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip6-other-flag </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip6-reachable-time </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip6-retrans-time </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip6-send-adv </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip6-subnet </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip6-upstream-interface </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> nd-cert </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> nd-cga-modifier </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> nd-mode </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> nd-security-level </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> nd-timestamp-delta </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> nd-timestamp-fuzz </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> vrip6_link_local </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vrrp-virtual-mac6 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/interface/ipv6</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/interface/ipv6</span>  </li>
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



