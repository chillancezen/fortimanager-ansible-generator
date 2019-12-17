:source: fmgr_pm_config_obj_firewall_ssl_ssh_profile_ssl_ssh_profile_ssl_server_ssl_server.py

:orphan:

.. _fmgr_pm_config_obj_firewall_ssl_ssh_profile_ssl_ssh_profile_ssl_server_ssl_server:

fmgr_pm_config_obj_firewall_ssl_ssh_profile_ssl_ssh_profile_ssl_server_ssl_server -- SSL servers.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/ssl-ssh-profile/{ssl-ssh-profile}/ssl-server/{ssl-server}`
- `/pm/config/global/obj/firewall/ssl-ssh-profile/{ssl-ssh-profile}/ssl-server/{ssl-server}`
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
 <li><span class="li-head">ssl-ssh-profile</span> - the object name <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-server</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - SSL servers.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">ftps-client-cert-request</span> - Action based on client certificate request during the FTPS handshake. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">https-client-cert-request</span> - Action based on client certificate request during the HTTPS handshake. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">id</span> - SSL server ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">imaps-client-cert-request</span> - Action based on client certificate request during the IMAPS handshake. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">ip</span> - IPv4 address of the SSL server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">pop3s-client-cert-request</span> - Action based on client certificate request during the POP3S handshake. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">smtps-client-cert-request</span> - Action based on client certificate request during the SMTPS handshake. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">ssl-other-client-cert-request</span> - Action based on client certificate request during an SSL protocol handshake. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - SSL servers.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - SSL servers.</li>
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
    - name: send request to /pm/config/obj/firewall/ssl-ssh-profile/{ssl-ssh-profile}/ssl-server/{ssl-server}
      fmgr_pm_config_obj_firewall_ssl_ssh_profile_ssl_ssh_profile_ssl_server_ssl_server:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            ssl-ssh-profile: <value of string>
            ssl-server: <value of string>
         params:
            - 
               data: 
                  ftps-client-cert-request: <value in [bypass, inspect, block]>
                  https-client-cert-request: <value in [bypass, inspect, block]>
                  id: <value of integer>
                  imaps-client-cert-request: <value in [bypass, inspect, block]>
                  ip: <value of string>
                  pop3s-client-cert-request: <value in [bypass, inspect, block]>
                  smtps-client-cert-request: <value in [bypass, inspect, block]>
                  ssl-other-client-cert-request: <value in [bypass, inspect, block]>
    - name: send request to /pm/config/obj/firewall/ssl-ssh-profile/{ssl-ssh-profile}/ssl-server/{ssl-server}
      fmgr_pm_config_obj_firewall_ssl_ssh_profile_ssl_ssh_profile_ssl_server_ssl_server:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            ssl-ssh-profile: <value of string>
            ssl-server: <value of string>
         params:
            - 
               option: <value in [object member, chksum, datasrc]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [clone, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - SSL server ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/ssl-ssh-profile/{ssl-ssh-profile}/ssl-server/{ssl-server}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [delete]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/ssl-ssh-profile/{ssl-ssh-profile}/ssl-server/{ssl-server}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> ftps-client-cert-request </span> - Action based on client certificate request during the FTPS handshake. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> https-client-cert-request </span> - Action based on client certificate request during the HTTPS handshake. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - SSL server ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> imaps-client-cert-request </span> - Action based on client certificate request during the IMAPS handshake. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip </span> - IPv4 address of the SSL server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pop3s-client-cert-request </span> - Action based on client certificate request during the POP3S handshake. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> smtps-client-cert-request </span> - Action based on client certificate request during the SMTPS handshake. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-other-client-cert-request </span> - Action based on client certificate request during an SSL protocol handshake. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/ssl-ssh-profile/{ssl-ssh-profile}/ssl-server/{ssl-server}</span>  </li>
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



