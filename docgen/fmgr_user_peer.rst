:source: fmgr_user_peer.py

:orphan:

.. _fmgr_user_peer:

fmgr_user_peer -- Configure peer users.
+++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/user/peer`
- `/pm/config/global/obj/user/peer`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure peer users.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">ca</span> - Name of the CA certificate as returned by the execute vpn certificate ca list command. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cn</span> - Peer certificate common name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cn-type</span> - Peer certificate common name type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [string, email, FQDN, ipv4, ipv6]</span> </li>
 <li><span class="li-head">ldap-mode</span> - Mode for LDAP peer authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [password, principal-name]</span> </li>
 <li><span class="li-head">ldap-password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ldap-server</span> - Name of an LDAP server defined under the user ldap command. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ldap-username</span> - Username for LDAP server bind. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mandatory-ca-verify</span> - Determine what happens to the peer if the CA certificate is not installed. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - Peer name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ocsp-override-server</span> - Online Certificate Status Protocol (OCSP) server for certificate retrieval. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">passwd</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">subject</span> - Peer certificate name constraints. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">two-factor</span> - Enable/disable two-factor authentication, applying certificate and password-based authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure peer users.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ca, cn, cn-type, ldap-mode, ldap-password, ldap-server, ldap-username, mandatory-ca-verify, name, ocsp-override-server, passwd, subject, two-factor]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/USER/PEER
      fmgr_user_peer:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     ca: <value of string>
                     cn: <value of string>
                     cn-type: <value in [string, email, FQDN, ...]>
                     ldap-mode: <value in [password, principal-name]>
                     ldap-password:
                       - <value of string>
                     ldap-server: <value of string>
                     ldap-username: <value of string>
                     mandatory-ca-verify: <value in [disable, enable]>
                     name: <value of string>
                     ocsp-override-server: <value of string>
                     passwd:
                       - <value of string>
                     subject: <value of string>
                     two-factor: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/USER/PEER
      fmgr_user_peer:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [ca, cn, cn-type, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/user/peer</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> ca </span> - Name of the CA certificate as returned by the execute vpn certificate ca list command. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> cn </span> - Peer certificate common name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> cn-type </span> - Peer certificate common name type. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ldap-mode </span> - Mode for LDAP peer authentication. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ldap-password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ldap-server </span> - Name of an LDAP server defined under the user ldap command. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ldap-username </span> - Username for LDAP server bind. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mandatory-ca-verify </span> - Determine what happens to the peer if the CA certificate is not installed. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Peer name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ocsp-override-server </span> - Online Certificate Status Protocol (OCSP) server for certificate retrieval. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> passwd </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> subject </span> - Peer certificate name constraints. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> two-factor </span> - Enable/disable two-factor authentication, applying certificate and password-based authentication. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/user/peer</span>  </li>
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



