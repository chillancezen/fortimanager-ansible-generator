:source: fmgr_hotspot20_h2qpconncapability_obj.py

:orphan:

.. _fmgr_hotspot20_h2qpconncapability_obj:

fmgr_hotspot20_h2qpconncapability_obj -- Configure connection capability.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/wireless-controller/hotspot20/h2qp-conn-capability/{h2qp-conn-capability}`
- `/pm/config/global/obj/wireless-controller/hotspot20/h2qp-conn-capability/{h2qp-conn-capability}`
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
 <li><span class="li-head">h2qp-conn-capability</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure connection capability.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
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
 <li><span class="li-head">parameters for method: [delete]</span> - Configure connection capability.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure connection capability.</li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/HOTSPOT20/H2QP-CONN-CAPABILITY/{H2QP-CONN-CAPABILITY}
      fmgr_hotspot20_h2qpconncapability_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            h2qp-conn-capability: <value of string>
         params:
            -
               data:
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

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/HOTSPOT20/H2QP-CONN-CAPABILITY/{H2QP-CONN-CAPABILITY}
      fmgr_hotspot20_h2qpconncapability_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            h2qp-conn-capability: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/hotspot20/h2qp-conn-capability/{h2qp-conn-capability}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/hotspot20/h2qp-conn-capability/{h2qp-conn-capability}</span>  </li>
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



