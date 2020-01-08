:source: fmgr_pm_config_obj_vpnmgr_vpntable.py

:orphan:

.. _fmgr_pm_config_obj_vpnmgr_vpntable:

fmgr_pm_config_obj_vpnmgr_vpntable
++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/vpnmgr/vpntable`
- `/pm/config/global/obj/vpnmgr/vpntable`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">authmethod</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [psk, rsa-signature, signature]</span> </li>
 <li><span class="li-head">auto-zone-policy</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">certificate</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">description</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dpd</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, on-idle, on-demand]</span> </li>
 <li><span class="li-head">dpd-retrycount</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dpd-retryinterval</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">fcc-enforcement</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">hub2spoke-zone</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ike-version</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1, 2]</span> </li>
 <li><span class="li-head">ike1dhgroup</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1, 2, 5, 14, 15, 16, 17, 18, 19, 20, 21, 27, 28, 29, 30, 31, 32]</span> </li>
 </ul>
 <li><span class="li-head">ike1dpd</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ike1keylifesec</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ike1localid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ike1mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [main, aggressive]</span> </li>
 <li><span class="li-head">ike1natkeepalive</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ike1nattraversal</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, forced]</span> </li>
 <li><span class="li-head">ike1proposal</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [des-md5, des-sha1, 3des-md5, 3des-sha1, aes128-md5, aes128-sha1, aes192-md5, aes192-sha1, aes256-md5, aes256-sha1, des-sha256, 3des-sha256, aes128-sha256, aes192-sha256, aes256-sha256, des-sha384, des-sha512, 3des-sha384, 3des-sha512, aes128-sha384, aes128-sha512, aes192-sha384, aes192-sha512, aes256-sha384, aes256-sha512, aria128-md5, aria128-sha1, aria128-sha256, aria128-sha384, aria128-sha512, aria192-md5, aria192-sha1, aria192-sha256, aria192-sha384, aria192-sha512, aria256-md5, aria256-sha1, aria256-sha256, aria256-sha384, aria256-sha512, seed-md5, seed-sha1, seed-sha256, seed-sha384, seed-sha512, aes128gcm-prfsha1, aes128gcm-prfsha256, aes128gcm-prfsha384, aes128gcm-prfsha512, aes256gcm-prfsha1, aes256gcm-prfsha256, aes256gcm-prfsha384, aes256gcm-prfsha512, chacha20poly1305-prfsha1, chacha20poly1305-prfsha256, chacha20poly1305-prfsha384, chacha20poly1305-prfsha512]</span> </li>
 <li><span class="li-head">ike2autonego</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ike2dhgroup</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1, 2, 5, 14, 15, 16, 17, 18, 19, 20, 21, 27, 28, 29, 30, 31, 32]</span> </li>
 </ul>
 <li><span class="li-head">ike2keepalive</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ike2keylifekbs</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ike2keylifesec</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ike2keylifetype</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [seconds, kbs, both]</span> </li>
 <li><span class="li-head">ike2proposal</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [null-md5, null-sha1, des-null, 3des-null, des-md5, des-sha1, 3des-md5, 3des-sha1, aes128-md5, aes128-sha1, aes192-md5, aes192-sha1, aes256-md5, aes256-sha1, aes128-null, aes192-null, aes256-null, null-sha256, des-sha256, 3des-sha256, aes128-sha256, aes192-sha256, aes256-sha256, des-sha384, des-sha512, 3des-sha384, 3des-sha512, aes128-sha384, aes128-sha512, aes192-sha384, aes192-sha512, aes256-sha384, aes256-sha512, null-sha384, null-sha512, aria128-null, aria128-md5, aria128-sha1, aria128-sha256, aria128-sha384, aria128-sha512, aria192-null, aria192-md5, aria192-sha1, aria192-sha256, aria192-sha384, aria192-sha512, aria256-null, aria256-md5, aria256-sha1, aria256-sha256, aria256-sha384, aria256-sha512, seed-null, seed-md5, seed-sha1, seed-sha256, seed-sha384, seed-sha512, aes128gcm, aes256gcm, chacha20poly1305]</span> </li>
 <li><span class="li-head">inter-vdom</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">intf-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [off, on]</span> </li>
 <li><span class="li-head">localid-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, fqdn, user-fqdn, keyid, address, asn1dn]</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">negotiate-timeout</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">default: 30</span> </li>
 <li><span class="li-head">npu-offload</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">pfs</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">psk-auto-generate</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">psksecret</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">replay</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rsa-certificate</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spoke2hub-zone</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">topology</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [meshed, star, dialup]</span> </li>
 <li><span class="li-head">vpn-zone</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [authmethod, auto-zone-policy, certificate, description, dpd, dpd-retrycount, dpd-retryinterval, fcc-enforcement, hub2spoke-zone, ike-version, ike1dhgroup, ike1dpd, ike1keylifesec, ike1localid, ike1mode, ike1natkeepalive, ike1nattraversal, ike1proposal, ike2autonego, ike2dhgroup, ike2keepalive, ike2keylifekbs, ike2keylifesec, ike2keylifetype, ike2proposal, inter-vdom, intf-mode, localid-type, name, negotiate-timeout, npu-offload, pfs, psk-auto-generate, psksecret, replay, rsa-certificate, spoke2hub-zone, topology, vpn-zone]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/VPNMGR/VPNTABLE
      fmgr_pm_config_obj_vpnmgr_vpntable:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     authmethod: <value in [psk, rsa-signature, signature]>
                     auto-zone-policy: <value in [disable, enable] default: 'enable'>
                     certificate: <value of string>
                     description: <value of string>
                     dpd: <value in [disable, enable, on-idle, ...]>
                     dpd-retrycount: <value of integer>
                     dpd-retryinterval:
                       - <value of integer>
                     fcc-enforcement: <value in [disable, enable]>
                     hub2spoke-zone: <value of string>
                     ike-version: <value in [1, 2]>
                     ike1dhgroup:
                       - <value in [1, 2, 5, ...]>
                     ike1dpd: <value in [disable, enable]>
                     ike1keylifesec: <value of integer>
                     ike1localid: <value of string>
                     ike1mode: <value in [main, aggressive]>
                     ike1natkeepalive: <value of integer>
                     ike1nattraversal: <value in [disable, enable, forced]>
                     ike1proposal: <value in [des-md5, des-sha1, 3des-md5, ...]>
                     ike2autonego: <value in [disable, enable]>
                     ike2dhgroup:
                       - <value in [1, 2, 5, ...]>
                     ike2keepalive: <value in [disable, enable]>
                     ike2keylifekbs: <value of integer>
                     ike2keylifesec: <value of integer>
                     ike2keylifetype: <value in [seconds, kbs, both]>
                     ike2proposal: <value in [null-md5, null-sha1, des-null, ...]>
                     inter-vdom: <value in [disable, enable]>
                     intf-mode: <value in [off, on]>
                     localid-type: <value in [auto, fqdn, user-fqdn, ...]>
                     name: <value of string>
                     negotiate-timeout: <value of integer default: 30>
                     npu-offload: <value in [disable, enable] default: 'enable'>
                     pfs: <value in [disable, enable]>
                     psk-auto-generate: <value in [disable, enable]>
                     psksecret:
                       - <value of string>
                     replay: <value in [disable, enable]>
                     rsa-certificate: <value of string>
                     spoke2hub-zone: <value of string>
                     topology: <value in [meshed, star, dialup]>
                     vpn-zone: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/VPNMGR/VPNTABLE
      fmgr_pm_config_obj_vpnmgr_vpntable:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [authmethod, auto-zone-policy, certificate, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/vpnmgr/vpntable</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> authmethod </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auto-zone-policy </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> certificate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> description </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dpd </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dpd-retrycount </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> dpd-retryinterval </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> fcc-enforcement </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> hub2spoke-zone </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ike-version </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ike1dhgroup </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ike1dpd </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ike1keylifesec </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ike1localid </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ike1mode </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ike1natkeepalive </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ike1nattraversal </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ike1proposal </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ike2autonego </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ike2dhgroup </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ike2keepalive </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ike2keylifekbs </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ike2keylifesec </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ike2keylifetype </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ike2proposal </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> inter-vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> intf-mode </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> localid-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> negotiate-timeout </span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">example: 30</span>  </li>
 <li> <span class="li-return"> npu-offload </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> pfs </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> psk-auto-generate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> psksecret </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> replay </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rsa-certificate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spoke2hub-zone </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> topology </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vpn-zone </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/vpnmgr/vpntable</span>  </li>
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



