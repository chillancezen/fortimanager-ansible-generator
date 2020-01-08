:source: fmgr_pm_config_obj_wireless_controller_hotspot20_h2qp_conn_capability.py

:orphan:

.. _fmgr_pm_config_obj_wireless_controller_hotspot20_h2qp_conn_capability:

fmgr_pm_config_obj_wireless_controller_hotspot20_h2qp_conn_capability -- Configure connection capability.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/wireless-controller/hotspot20/h2qp-conn-capability`
- `/pm/config/global/obj/wireless-controller/hotspot20/h2qp-conn-capability`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure connection capability.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">esp-port</span> - Set ESP port service (used by IPsec VPNs) status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [closed, open, unknown]</span> </li>
 <li><span class="li-head">ftp-port</span> - Set FTP port service status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [closed, open, unknown]</span> </li>
 <li><span class="li-head">http-port</span> - Set HTTP port service status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [closed, open, unknown]</span> </li>
 <li><span class="li-head">icmp-port</span> - Set ICMP port service status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [closed, open, unknown]</span> </li>
 <li><span class="li-head">ikev2-port</span> - Set IKEv2 port service for IPsec VPN status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [closed, open, unknown]</span> </li>
 <li><span class="li-head">ikev2-xx-port</span> - Set UDP port 4500 (which may be used by IKEv2 for IPsec VPN) service status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [closed, open, unknown]</span> </li>
 <li><span class="li-head">name</span> - Connection capability name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">pptp-vpn-port</span> - Set Point to Point Tunneling Protocol (PPTP) VPN port service status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [closed, open, unknown]</span> </li>
 <li><span class="li-head">ssh-port</span> - Set SSH port service status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [closed, open, unknown]</span> </li>
 <li><span class="li-head">tls-port</span> - Set TLS VPN (HTTPS) port service status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [closed, open, unknown]</span> </li>
 <li><span class="li-head">voip-tcp-port</span> - Set VoIP TCP port service status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [closed, open, unknown]</span> </li>
 <li><span class="li-head">voip-udp-port</span> - Set VoIP UDP port service status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [closed, open, unknown]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure connection capability.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [esp-port, ftp-port, http-port, icmp-port, ikev2-port, ikev2-xx-port, name, pptp-vpn-port, ssh-port, tls-port, voip-tcp-port, voip-udp-port]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/HOTSPOT20/H2QP-CONN-CAPABILITY
      fmgr_pm_config_obj_wireless_controller_hotspot20_h2qp_conn_capability:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     esp-port: <value in [closed, open, unknown]>
                     ftp-port: <value in [closed, open, unknown]>
                     http-port: <value in [closed, open, unknown]>
                     icmp-port: <value in [closed, open, unknown]>
                     ikev2-port: <value in [closed, open, unknown]>
                     ikev2-xx-port: <value in [closed, open, unknown]>
                     name: <value of string>
                     pptp-vpn-port: <value in [closed, open, unknown]>
                     ssh-port: <value in [closed, open, unknown]>
                     tls-port: <value in [closed, open, unknown]>
                     voip-tcp-port: <value in [closed, open, unknown]>
                     voip-udp-port: <value in [closed, open, unknown]>

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/HOTSPOT20/H2QP-CONN-CAPABILITY
      fmgr_pm_config_obj_wireless_controller_hotspot20_h2qp_conn_capability:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [esp-port, ftp-port, http-port, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/hotspot20/h2qp-conn-capability</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> esp-port </span> - Set ESP port service (used by IPsec VPNs) status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ftp-port </span> - Set FTP port service status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-port </span> - Set HTTP port service status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> icmp-port </span> - Set ICMP port service status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ikev2-port </span> - Set IKEv2 port service for IPsec VPN status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ikev2-xx-port </span> - Set UDP port 4500 (which may be used by IKEv2 for IPsec VPN) service status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Connection capability name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pptp-vpn-port </span> - Set Point to Point Tunneling Protocol (PPTP) VPN port service status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssh-port </span> - Set SSH port service status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tls-port </span> - Set TLS VPN (HTTPS) port service status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> voip-tcp-port </span> - Set VoIP TCP port service status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> voip-udp-port </span> - Set VoIP UDP port service status. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/hotspot20/h2qp-conn-capability</span>  </li>
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



