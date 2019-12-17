:source: fmgr_pm_config_obj_wireless_controller_hotspot20_anqp_nai_realm.py

:orphan:

.. _fmgr_pm_config_obj_wireless_controller_hotspot20_anqp_nai_realm:

fmgr_pm_config_obj_wireless_controller_hotspot20_anqp_nai_realm -- Configure network access identifier (NAI) realm.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/wireless-controller/hotspot20/anqp-nai-realm`
- `/pm/config/global/obj/wireless-controller/hotspot20/anqp-nai-realm`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure network access identifier (NAI) realm.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">nai-list</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">eap-method</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">auth-param</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - ID of authentication parameter. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [non-eap-inner-auth, inner-auth-eap, credential, tunneled-credential]</span> </li>
 <li><span class="li-head">index</span> - Param index. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">val</span> - Value of authentication parameter. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [eap-identity, eap-md5, eap-tls, eap-ttls, eap-peap, eap-sim, eap-aka, eap-aka-prime, non-eap-pap, non-eap-chap, non-eap-mschap, non-eap-mschapv2, cred-sim, cred-usim, cred-nfc, cred-hardware-token, cred-softoken, cred-certificate, cred-user-pwd, cred-none, cred-vendor-specific, tun-cred-sim, tun-cred-usim, tun-cred-nfc, tun-cred-hardware-token, tun-cred-softoken, tun-cred-certificate, tun-cred-user-pwd, tun-cred-anonymous, tun-cred-vendor-specific]</span> </li>
 </ul>
 <li><span class="li-head">index</span> - EAP method index. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">method</span> - EAP method type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [eap-identity, eap-md5, eap-tls, eap-ttls, eap-peap, eap-sim, eap-aka, eap-aka-prime]</span> </li>
 </ul>
 <li><span class="li-head">encoding</span> - Enable/disable format in accordance with IETF RFC 4282. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">nai-realm</span> - Configure NAI realms (delimited by a semi-colon character). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - NAI realm name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">name</span> - NAI realm list name. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure network access identifier (NAI) realm.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [name]</span> </li>
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
    - name: send request to /pm/config/obj/wireless-controller/hotspot20/anqp-nai-realm
      fmgr_pm_config_obj_wireless_controller_hotspot20_anqp_nai_realm:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            - 
               data: 
                - 
                     nai-list: 
                      - 
                           eap-method: 
                            - 
                                 auth-param: 
                                  - 
                                       id: <value in [non-eap-inner-auth, inner-auth-eap, credential, ...]>
                                       index: <value of integer>
                                       val: <value in [eap-identity, eap-md5, eap-tls, ...]>
                                 index: <value of integer>
                                 method: <value in [eap-identity, eap-md5, eap-tls, ...]>
                           encoding: <value in [disable, enable]>
                           nai-realm: <value of string>
                           name: <value of string>
                     name: <value of string>
    - name: send request to /pm/config/obj/wireless-controller/hotspot20/anqp-nai-realm
      fmgr_pm_config_obj_wireless_controller_hotspot20_anqp_nai_realm:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            - 
               attr: <value of string>
               fields: 
                - 
                   - <value in [name]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/hotspot20/anqp-nai-realm</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> nai-list </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> eap-method </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> auth-param </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - ID of authentication parameter. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> index </span> - Param index. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> val </span> - Value of authentication parameter. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> index </span> - EAP method index. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> method </span> - EAP method type. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> encoding </span> - Enable/disable format in accordance with IETF RFC 4282. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> nai-realm </span> - Configure NAI realms (delimited by a semi-colon character). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - NAI realm name. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> name </span> - NAI realm list name. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/hotspot20/anqp-nai-realm</span>  </li>
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



