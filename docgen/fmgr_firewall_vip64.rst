:source: fmgr_firewall_vip64.py

:orphan:

.. _fmgr_firewall_vip64:

fmgr_firewall_vip64 -- Configure IPv6 to IPv4 virtual IPs.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/vip64`
- `/pm/config/global/obj/firewall/vip64`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure IPv6 to IPv4 virtual IPs.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">arp-reply</span> - Enable ARP reply. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">color</span> - Color of icon on the GUI. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dynamic_mapping</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">arp-reply</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">color</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extport</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ldb-method</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, round-robin, weighted, least-session, least-rtt, first-alive]</span> </li>
 <li><span class="li-head">mappedip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mappedport</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">monitor</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">portforward</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">protocol</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [tcp, udp]</span> </li>
 <li><span class="li-head">server-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [http, tcp, udp, ip]</span> </li>
 <li><span class="li-head">src-filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static-nat, server-load-balance]</span> </li>
 <li><span class="li-head">uuid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">extip</span> - Start-external-IP [-end-external-IP]. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extport</span> - External service port. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Custom defined id. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ldb-method</span> - Load balance method. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, round-robin, weighted, least-session, least-rtt, first-alive]</span> </li>
 <li><span class="li-head">mappedip</span> - Start-mapped-IP [-end-mapped-IP]. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mappedport</span> - Mapped service port. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">monitor</span> - Health monitors. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - VIP64 name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">portforward</span> - Enable port forwarding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">protocol</span> - Mapped port protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [tcp, udp]</span> </li>
 <li><span class="li-head">realservers</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">client-ip</span> - Restrict server to a client IP in this range. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">healthcheck</span> - Per server health check. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, vip]</span> </li>
 <li><span class="li-head">holddown-interval</span> - Hold down interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">id</span> - Real server ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - Mapped server IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-connections</span> - Maximum number of connections allowed to server. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">monitor</span> - Health monitors. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port</span> - Mapped server port. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Server administrative status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [active, standby, disable]</span> </li>
 <li><span class="li-head">weight</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">server-type</span> - Server type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [http, tcp, udp, ip]</span> </li>
 <li><span class="li-head">src-filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">type</span> - VIP type: static NAT. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static-nat, server-load-balance]</span> </li>
 <li><span class="li-head">uuid</span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure IPv6 to IPv4 virtual IPs.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [arp-reply, color, comment, extip, extport, id, ldb-method, mappedip, mappedport, monitor, name, portforward, protocol, server-type, src-filter, type, uuid]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/VIP64
      fmgr_firewall_vip64:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     arp-reply: <value in [disable, enable]>
                     color: <value of integer>
                     comment: <value of string>
                     dynamic_mapping:
                       -
                           _scope:
                             -
                                 name: <value of string>
                                 vdom: <value of string>
                           arp-reply: <value in [disable, enable]>
                           color: <value of integer>
                           comment: <value of string>
                           extip: <value of string>
                           extport: <value of string>
                           id: <value of integer>
                           ldb-method: <value in [static, round-robin, weighted, ...]>
                           mappedip: <value of string>
                           mappedport: <value of string>
                           monitor: <value of string>
                           portforward: <value in [disable, enable]>
                           protocol: <value in [tcp, udp]>
                           server-type: <value in [http, tcp, udp, ...]>
                           src-filter:
                             - <value of string>
                           type: <value in [static-nat, server-load-balance]>
                           uuid: <value of string>
                     extip: <value of string>
                     extport: <value of string>
                     id: <value of integer>
                     ldb-method: <value in [static, round-robin, weighted, ...]>
                     mappedip: <value of string>
                     mappedport: <value of string>
                     monitor: <value of string>
                     name: <value of string>
                     portforward: <value in [disable, enable]>
                     protocol: <value in [tcp, udp]>
                     realservers:
                       -
                           client-ip: <value of string>
                           healthcheck: <value in [disable, enable, vip]>
                           holddown-interval: <value of integer>
                           id: <value of integer>
                           ip: <value of string>
                           max-connections: <value of integer>
                           monitor: <value of string>
                           port: <value of integer>
                           status: <value in [active, standby, disable]>
                           weight: <value of integer>
                     server-type: <value in [http, tcp, udp, ...]>
                     src-filter:
                       - <value of string>
                     type: <value in [static-nat, server-load-balance]>
                     uuid: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/VIP64
      fmgr_firewall_vip64:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [arp-reply, color, comment, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/vip64</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> arp-reply </span> - Enable ARP reply. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> color </span> - Color of icon on the GUI. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comment </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dynamic_mapping </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> _scope </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> arp-reply </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> color </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comment </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> extip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> extport </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ldb-method </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mappedip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mappedport </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> monitor </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> portforward </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> protocol </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> src-filter </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> uuid </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> extip </span> - Start-external-IP [-end-external-IP]. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> extport </span> - External service port. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Custom defined id. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ldb-method </span> - Load balance method. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mappedip </span> - Start-mapped-IP [-end-mapped-IP]. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mappedport </span> - Mapped service port. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> monitor </span> - Health monitors. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - VIP64 name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> portforward </span> - Enable port forwarding. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> protocol </span> - Mapped port protocol. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> realservers </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> client-ip </span> - Restrict server to a client IP in this range. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> healthcheck </span> - Per server health check. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> holddown-interval </span> - Hold down interval. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> id </span> - Real server ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip </span> - Mapped server IP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-connections </span> - Maximum number of connections allowed to server. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> monitor </span> - Health monitors. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port </span> - Mapped server port. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> status </span> - Server administrative status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> weight </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> server-type </span> - Server type. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> src-filter </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> type </span> - VIP type: static NAT. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> uuid </span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/vip64</span>  </li>
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



