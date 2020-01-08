:source: fmgr_pm_config_obj_user_ldap_dynamic_mapping_per_object.py

:orphan:

.. _fmgr_pm_config_obj_user_ldap_dynamic_mapping_per_object:

fmgr_pm_config_obj_user_ldap_dynamic_mapping_per_object
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/user/ldap/{ldap}/dynamic_mapping/{dynamic_mapping}`
- `/pm/config/global/obj/user/ldap/{ldap}/dynamic_mapping/{dynamic_mapping}`
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
 <li><span class="li-head">ldap</span> - the object name <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dynamic_mapping</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">account-key-filter</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">account-key-name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">account-key-processing</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [same, strip]</span> </li>
 <li><span class="li-head">ca-cert</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cnid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dn</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">group-filter</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">group-member-check</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [user-attr, group-object, posix-group-object]</span> </li>
 <li><span class="li-head">group-object-filter</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">group-object-search-base</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">group-search-base</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">member-attr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">obtain-user-info</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">password-expiry-warning</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">password-renewal</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">port</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">retrieve-protection-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">search-type</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [nested, recursive]</span> </li>
 </ul>
 <li><span class="li-head">secondary-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">secure</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, starttls, ldaps]</span> </li>
 <li><span class="li-head">server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server-identity-check</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">source-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-min-proto-version</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, TLSv1, TLSv1-1, TLSv1-2, SSLv3]</span> </li>
 <li><span class="li-head">tertiary-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [simple, anonymous, regular]</span> </li>
 <li><span class="li-head">user-info-exchange-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">username</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - </li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/USER/LDAP/{LDAP}/DYNAMIC_MAPPING/{DYNAMIC_MAPPING}
      fmgr_pm_config_obj_user_ldap_dynamic_mapping_per_object:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            ldap: <value of string>
            dynamic_mapping: <value of string>
         params:
            -
               data:
                  _scope:
                    -
                        name: <value of string>
                        vdom: <value of string>
                  account-key-filter: <value of string>
                  account-key-name: <value of string>
                  account-key-processing: <value in [same, strip]>
                  ca-cert: <value of string>
                  cnid: <value of string>
                  dn: <value of string>
                  filter: <value of string>
                  group: <value of string>
                  group-filter: <value of string>
                  group-member-check: <value in [user-attr, group-object, posix-group-object]>
                  group-object-filter: <value of string>
                  group-object-search-base: <value of string>
                  group-search-base: <value of string>
                  member-attr: <value of string>
                  obtain-user-info: <value in [disable, enable]>
                  password:
                    - <value of string>
                  password-expiry-warning: <value in [disable, enable]>
                  password-renewal: <value in [disable, enable]>
                  port: <value of integer>
                  retrieve-protection-profile: <value of string>
                  search-type:
                    - <value in [nested, recursive]>
                  secondary-server: <value of string>
                  secure: <value in [disable, starttls, ldaps]>
                  server: <value of string>
                  server-identity-check: <value in [disable, enable]>
                  source-ip: <value of string>
                  ssl-min-proto-version: <value in [default, TLSv1, TLSv1-1, ...]>
                  tertiary-server: <value of string>
                  type: <value in [simple, anonymous, regular]>
                  user-info-exchange-server: <value of string>
                  username: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/USER/LDAP/{LDAP}/DYNAMIC_MAPPING/{DYNAMIC_MAPPING}
      fmgr_pm_config_obj_user_ldap_dynamic_mapping_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            ldap: <value of string>
            dynamic_mapping: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/user/ldap/{ldap}/dynamic_mapping/{dynamic_mapping}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> _scope </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> account-key-filter </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> account-key-name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> account-key-processing </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ca-cert </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> cnid </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dn </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> filter </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> group-filter </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> group-member-check </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> group-object-filter </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> group-object-search-base </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> group-search-base </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> member-attr </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> obtain-user-info </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> password-expiry-warning </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> password-renewal </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> retrieve-protection-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> search-type </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> secondary-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> secure </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server-identity-check </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-min-proto-version </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tertiary-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> user-info-exchange-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> username </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/user/ldap/{ldap}/dynamic_mapping/{dynamic_mapping}</span>  </li>
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



