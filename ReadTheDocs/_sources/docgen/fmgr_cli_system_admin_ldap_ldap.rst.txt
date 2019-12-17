:source: fmgr_cli_system_admin_ldap_ldap.py

:orphan:

.. _fmgr_cli_system_admin_ldap_ldap:

fmgr_cli_system_admin_ldap_ldap -- LDAP server entry configuration.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[delete, get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/admin/ldap/{ldap}`
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
 <li><span class="li-head">ldap</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [delete, get]</span> - LDAP server entry configuration.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - LDAP server entry configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">adom</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">adom-name</span> - Admin domain names. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">adom-attr</span> - Attribute used to retrieve adom <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">attributes</span> - Attributes used for group searching. <span class="li-normal">type: str</span>  <span class="li-normal">default: member,uniquemember,memberuid</span> </li>
 <li><span class="li-head">ca-cert</span> - CA certificate name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cnid</span> - Common Name Identifier (default = CN). <span class="li-normal">type: str</span>  <span class="li-normal">default: cn</span> </li>
 <li><span class="li-head">connect-timeout</span> - LDAP connection timeout (msec). <span class="li-normal">type: int</span>  <span class="li-normal">default: 500</span> </li>
 <li><span class="li-head">dn</span> - Distinguished Name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">filter</span> - Filter used for group searching. <span class="li-normal">type: str</span>  <span class="li-normal">default: (objectclass=*)</span> </li>
 <li><span class="li-head">group</span> - Full base DN used for group searching. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">memberof-attr</span> - Attribute used to retrieve memeberof. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - LDAP server entry name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC MTEyODQwMzUzNTU5OTkxNiMZsnjCaX8v5NaNPmglZ1pwQh+wPb8bwCFjVP5hUgQnOleEpUJ7ARHGG9tpPDKAZE74Ep4RHCgPsKLw3wtuNG0kB3r6RBqrFQcvA/t/txyxY2LlhN4+ewvQsITXDVyOmmyE1tqgG/9GpJNNqPCgZsW36+Oo</span> </li>
 </ul>
 <li><span class="li-head">port</span> - Port number of LDAP server (default = 389). <span class="li-normal">type: int</span>  <span class="li-normal">default: 389</span> </li>
 <li><span class="li-head">profile-attr</span> - Attribute used to retrieve admin profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">secondary-server</span> - {<name_str|ip_str>} secondary LDAP server domain name or IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">secure</span> - SSL connection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, starttls, ldaps]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">server</span> - {<name_str|ip_str>} LDAP server domain name or IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tertiary-server</span> - {<name_str|ip_str>} tertiary LDAP server domain name or IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - Type of LDAP binding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [simple, anonymous, regular]</span>  <span class="li-normal">default: simple</span> </li>
 <li><span class="li-head">username</span> - Username (full DN) for initial binding. <span class="li-normal">type: str</span> </li>
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
    - name: send request to /cli/system/admin/ldap/{ldap}
      fmgr_cli_system_admin_ldap_ldap:
         method: <value in [set, update]>
         url_params:
            ldap: <value of string>
         params:
            - 
               data: 
                  adom: 
                   - 
                        adom-name: <value of string>
                  adom-attr: <value of string>
                  attributes: <value of string default: member,uniquemember,memberuid>
                  ca-cert: <value of string>
                  cnid: <value of string default: cn>
                  connect-timeout: <value of integer default: 500>
                  dn: <value of string>
                  filter: <value of string default: (objectclass=*)>
                  group: <value of string>
                  memberof-attr: <value of string>
                  name: <value of string>
                  password: 
                   - <value of string default: ENC MTEyODQwMzUzNTU5OTkxNiMZsnjCaX8v5NaNPmglZ1pwQh+wPb8bwCFjVP5hUgQnOleEpUJ7ARHGG9tpPDKAZE74Ep4RHCgPsKLw3wtuNG0kB3r6RBqrFQcvA/t/txyxY2LlhN4+ewvQsITXDVyOmmyE1tqgG/9GpJNNqPCgZsW36+Oo>
                  port: <value of integer default: 389>
                  profile-attr: <value of string>
                  secondary-server: <value of string>
                  secure: <value in [disable, starttls, ldaps] default: disable>
                  server: <value of string>
                  tertiary-server: <value of string>
                  type: <value in [simple, anonymous, regular] default: simple>
                  username: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [delete, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/admin/ldap/{ldap}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> adom </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> adom-name </span> - Admin domain names. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> adom-attr </span> - Attribute used to retrieve adom <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> attributes </span> - Attributes used for group searching. <span class="li-normal">type: str</span>  <span class="li-normal">example: member,uniquemember,memberuid</span>  </li>
 <li> <span class="li-return"> ca-cert </span> - CA certificate name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> cnid </span> - Common Name Identifier (default = CN). <span class="li-normal">type: str</span>  <span class="li-normal">example: cn</span>  </li>
 <li> <span class="li-return"> connect-timeout </span> - LDAP connection timeout (msec). <span class="li-normal">type: int</span>  <span class="li-normal">example: 500</span>  </li>
 <li> <span class="li-return"> dn </span> - Distinguished Name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> filter </span> - Filter used for group searching. <span class="li-normal">type: str</span>  <span class="li-normal">example: (objectclass=*)</span>  </li>
 <li> <span class="li-return"> group </span> - Full base DN used for group searching. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> memberof-attr </span> - Attribute used to retrieve memeberof. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - LDAP server entry name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC MTEyODQwMzUzNTU5OTkxNiMZsnjCaX8v5NaNPmglZ1pwQh+wPb8bwCFjVP5hUgQnOleEpUJ7ARHGG9tpPDKAZE74Ep4RHCgPsKLw3wtuNG0kB3r6RBqrFQcvA/t/txyxY2LlhN4+ewvQsITXDVyOmmyE1tqgG/9GpJNNqPCgZsW36+Oo</span>  </li>
 </ul>
 <li> <span class="li-return"> port </span> - Port number of LDAP server (default = 389). <span class="li-normal">type: int</span>  <span class="li-normal">example: 389</span>  </li>
 <li> <span class="li-return"> profile-attr </span> - Attribute used to retrieve admin profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> secondary-server </span> - {<name_str|ip_str>} secondary LDAP server domain name or IP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> secure </span> - SSL connection. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> server </span> - {<name_str|ip_str>} LDAP server domain name or IP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tertiary-server </span> - {<name_str|ip_str>} tertiary LDAP server domain name or IP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - Type of LDAP binding. <span class="li-normal">type: str</span>  <span class="li-normal">example: simple</span>  </li>
 <li> <span class="li-return"> username </span> - Username (full DN) for initial binding. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/admin/ldap/{ldap}</span>  </li>
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



