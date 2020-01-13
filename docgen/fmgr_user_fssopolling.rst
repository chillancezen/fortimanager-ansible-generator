:source: fmgr_user_fssopolling.py

:orphan:

.. _fmgr_user_fssopolling:

fmgr_user_fssopolling -- Configure FSSO active directory servers for polling mode.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/user/fsso-polling`
- `/pm/config/global/obj/user/fsso-polling`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure FSSO active directory servers for polling mode.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_gui_meta</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">adgrp</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - Name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">default-domain</span> - Default domain managed by this Active Directory server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Active Directory server ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ldap-server</span> - LDAP server name used in LDAP connection strings. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">logon-history</span> - Number of hours of logon history to keep, 0 means keep all history. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">polling-frequency</span> - Polling frequency (every 1 to 30 seconds). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">port</span> - Port to communicate with this Active Directory server. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">server</span> - Host name or IP address of the Active Directory server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable polling for the status of this Active Directory server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">user</span> - User name required to log into this Active Directory server. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure FSSO active directory servers for polling mode.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [_gui_meta, default-domain, id, ldap-server, logon-history, password, polling-frequency, port, server, status, user]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/USER/FSSO-POLLING
      fmgr_user_fssopolling:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     _gui_meta: <value of string>
                     adgrp:
                       -
                           name: <value of string>
                     default-domain: <value of string>
                     id: <value of integer>
                     ldap-server: <value of string>
                     logon-history: <value of integer>
                     password:
                       - <value of string>
                     polling-frequency: <value of integer>
                     port: <value of integer>
                     server: <value of string>
                     status: <value in [disable, enable]>
                     user: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/USER/FSSO-POLLING
      fmgr_user_fssopolling:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [_gui_meta, default-domain, id, ...]>
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
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - Active Directory server ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/user/fsso-polling</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> _gui_meta </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> adgrp </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - Name. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> default-domain </span> - Default domain managed by this Active Directory server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Active Directory server ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ldap-server </span> - LDAP server name used in LDAP connection strings. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> logon-history </span> - Number of hours of logon history to keep, 0 means keep all history. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> polling-frequency </span> - Polling frequency (every 1 to 30 seconds). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> port </span> - Port to communicate with this Active Directory server. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> server </span> - Host name or IP address of the Active Directory server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable polling for the status of this Active Directory server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> user </span> - User name required to log into this Active Directory server. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/user/fsso-polling</span>  </li>
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



