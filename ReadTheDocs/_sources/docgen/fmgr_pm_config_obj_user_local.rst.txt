:source: fmgr_pm_config_obj_user_local.py

:orphan:

.. _fmgr_pm_config_obj_user_local:

fmgr_pm_config_obj_user_local -- Configure local users.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/user/local`
- `/pm/config/global/obj/user/local`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure local users.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">auth-concurrent-override</span> - Enable/disable overriding the policy-auth-concurrent under config system global. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auth-concurrent-value</span> - Maximum number of concurrent logins permitted from the same user. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">authtimeout</span> - Time in minutes before the authentication timeout for a user is reached. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">email-to</span> - Two-factor recipient's email address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fortitoken</span> - Two-factor recipient's FortiToken serial number. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - User ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ldap-server</span> - Name of LDAP server with which the user must authenticate. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - User name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">passwd</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">passwd-policy</span> - Password policy to apply to this user, as defined in config user password-policy. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ppk-identity</span> - IKEv2 Postquantum Preshared Key Identity. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ppk-secret</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">radius-server</span> - Name of RADIUS server with which the user must authenticate. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sms-custom-server</span> - Two-factor recipient's SMS server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sms-phone</span> - Two-factor recipient's mobile phone number. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sms-server</span> - Send SMS through FortiGuard or other external server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [fortiguard, custom]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable allowing the local user to authenticate with the FortiGate unit. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tacacs+-server</span> - Name of TACACS+ server with which the user must authenticate. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">two-factor</span> - Enable/disable two-factor authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, fortitoken, email, sms, fortitoken-cloud]</span> </li>
 <li><span class="li-head">type</span> - Authentication method. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [password, radius, tacacs+, ldap]</span> </li>
 <li><span class="li-head">workstation</span> - Name of the remote user workstation, if you want to limit the user to authenticate only from a particular workstation. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure local users.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auth-concurrent-override, auth-concurrent-value, authtimeout, email-to, fortitoken, id, ldap-server, name, passwd, passwd-policy, ppk-identity, ppk-secret, radius-server, sms-custom-server, sms-phone, sms-server, status, tacacs+-server, two-factor, type, workstation]</span> </li>
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
    - name: send request to /pm/config/obj/user/local
      fmgr_pm_config_obj_user_local:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            - 
               data: 
                - 
                     auth-concurrent-override: <value in [disable, enable]>
                     auth-concurrent-value: <value of integer>
                     authtimeout: <value of integer>
                     email-to: <value of string>
                     fortitoken: <value of string>
                     id: <value of integer>
                     ldap-server: <value of string>
                     name: <value of string>
                     passwd: 
                      - <value of string>
                     passwd-policy: <value of string>
                     ppk-identity: <value of string>
                     ppk-secret: 
                      - <value of string>
                     radius-server: <value of string>
                     sms-custom-server: <value of string>
                     sms-phone: <value of string>
                     sms-server: <value in [fortiguard, custom]>
                     status: <value in [disable, enable]>
                     tacacs+-server: <value of string>
                     two-factor: <value in [disable, fortitoken, email, ...]>
                     type: <value in [password, radius, tacacs+, ...]>
                     workstation: <value of string>
    - name: send request to /pm/config/obj/user/local
      fmgr_pm_config_obj_user_local:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            - 
               attr: <value of string>
               fields: 
                - 
                   - <value in [auth-concurrent-override, auth-concurrent-value, authtimeout, ...]>
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
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/user/local</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> auth-concurrent-override </span> - Enable/disable overriding the policy-auth-concurrent under config system global. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auth-concurrent-value </span> - Maximum number of concurrent logins permitted from the same user. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> authtimeout </span> - Time in minutes before the authentication timeout for a user is reached. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> email-to </span> - Two-factor recipient's email address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fortitoken </span> - Two-factor recipient's FortiToken serial number. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - User ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ldap-server </span> - Name of LDAP server with which the user must authenticate. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - User name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> passwd </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> passwd-policy </span> - Password policy to apply to this user, as defined in config user password-policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ppk-identity </span> - IKEv2 Postquantum Preshared Key Identity. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ppk-secret </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> radius-server </span> - Name of RADIUS server with which the user must authenticate. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sms-custom-server </span> - Two-factor recipient's SMS server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sms-phone </span> - Two-factor recipient's mobile phone number. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sms-server </span> - Send SMS through FortiGuard or other external server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable allowing the local user to authenticate with the FortiGate unit. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tacacs+-server </span> - Name of TACACS+ server with which the user must authenticate. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> two-factor </span> - Enable/disable two-factor authentication. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - Authentication method. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> workstation </span> - Name of the remote user workstation, if you want to limit the user to authenticate only from a particular workstation. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/user/local</span>  </li>
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



