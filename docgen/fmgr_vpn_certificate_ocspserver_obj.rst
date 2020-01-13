:source: fmgr_vpn_certificate_ocspserver_obj.py

:orphan:

.. _fmgr_vpn_certificate_ocspserver_obj:

fmgr_vpn_certificate_ocspserver_obj -- OCSP server configuration.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/vpn/certificate/ocsp-server/{ocsp-server}`
- `/pm/config/global/obj/vpn/certificate/ocsp-server/{ocsp-server}`
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
 <li><span class="li-head">ocsp-server</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - OCSP server configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">cert</span> - OCSP server certificate. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - OCSP server entry name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">secondary-cert</span> - Secondary OCSP server certificate. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">secondary-url</span> - Secondary OCSP server URL. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-ip</span> - Source IP address for communications to the OCSP server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">unavail-action</span> - Action when server is unavailable (revoke the certificate or ignore the result of the check). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [revoke, ignore]</span> </li>
 <li><span class="li-head">url</span> - OCSP server URL. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - OCSP server configuration.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - OCSP server configuration.</li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/VPN/CERTIFICATE/OCSP-SERVER/{OCSP-SERVER}
      fmgr_vpn_certificate_ocspserver_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            ocsp-server: <value of string>
         params:
            -
               data:
                  cert: <value of string>
                  name: <value of string>
                  secondary-cert: <value of string>
                  secondary-url: <value of string>
                  source-ip: <value of string>
                  unavail-action: <value in [revoke, ignore]>
                  url: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/VPN/CERTIFICATE/OCSP-SERVER/{OCSP-SERVER}
      fmgr_vpn_certificate_ocspserver_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            ocsp-server: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/vpn/certificate/ocsp-server/{ocsp-server}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> cert </span> - OCSP server certificate. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - OCSP server entry name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> secondary-cert </span> - Secondary OCSP server certificate. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> secondary-url </span> - Secondary OCSP server URL. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-ip </span> - Source IP address for communications to the OCSP server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> unavail-action </span> - Action when server is unavailable (revoke the certificate or ignore the result of the check). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> url </span> - OCSP server URL. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/vpn/certificate/ocsp-server/{ocsp-server}</span>  </li>
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



