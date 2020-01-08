:source: fmgr_pm_config_obj_firewall_ssl_ssh_profile_https.py

:orphan:

.. _fmgr_pm_config_obj_firewall_ssl_ssh_profile_https:

fmgr_pm_config_obj_firewall_ssl_ssh_profile_https -- Configure HTTPS options.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/ssl-ssh-profile/{ssl-ssh-profile}/https`
- `/pm/config/global/obj/firewall/ssl-ssh-profile/{ssl-ssh-profile}/https`
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
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure HTTPS options.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Configure HTTPS options.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">allow-invalid-server-cert</span> - When enabled, allows SSL sessions whose server certificate validation failed. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">client-cert-request</span> - Action based on client certificate request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">ports</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">status</span> - Configure protocol inspection status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, certificate-inspection, deep-inspection]</span> </li>
 <li><span class="li-head">unsupported-ssl</span> - Action based on the SSL encryption used being unsupported. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, inspect, block]</span> </li>
 <li><span class="li-head">untrusted-cert</span> - Allow, ignore, or block the untrusted SSL session server certificate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, ignore]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/SSL-SSH-PROFILE/{SSL-SSH-PROFILE}/HTTPS
      fmgr_pm_config_obj_firewall_ssl_ssh_profile_https:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            ssl-ssh-profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/SSL-SSH-PROFILE/{SSL-SSH-PROFILE}/HTTPS
      fmgr_pm_config_obj_firewall_ssl_ssh_profile_https:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            ssl-ssh-profile: <value of string>
         params:
            -
               data:
                  allow-invalid-server-cert: <value in [disable, enable]>
                  client-cert-request: <value in [bypass, inspect, block]>
                  ports:
                    - <value of integer>
                  status: <value in [disable, certificate-inspection, deep-inspection]>
                  unsupported-ssl: <value in [bypass, inspect, block]>
                  untrusted-cert: <value in [allow, block, ignore]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> allow-invalid-server-cert </span> - When enabled, allows SSL sessions whose server certificate validation failed. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> client-cert-request </span> - Action based on client certificate request. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ports </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> status </span> - Configure protocol inspection status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> unsupported-ssl </span> - Action based on the SSL encryption used being unsupported. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> untrusted-cert </span> - Allow, ignore, or block the untrusted SSL session server certificate. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/ssl-ssh-profile/{ssl-ssh-profile}/https</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/ssl-ssh-profile/{ssl-ssh-profile}/https</span>  </li>
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



