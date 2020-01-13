:source: fmgr_user_fsso_obj.py

:orphan:

.. _fmgr_user_fsso_obj:

fmgr_user_fsso_obj -- Configure Fortinet Single Sign On (FSSO) agents.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/user/fsso/{fsso}`
- `/pm/config/global/obj/user/fsso/{fsso}`
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
 <li><span class="li-head">fsso</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure Fortinet Single Sign On (FSSO) agents.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">_gui_meta</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dynamic_mapping</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_gui_meta</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ldap-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">password2</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">password3</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">password4</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">password5</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">port</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">port2</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">port3</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">port4</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">port5</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server2</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server3</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server4</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server5</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-ip6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-trusted-cert</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, fortiems, fortinac]</span> </li>
 <li><span class="li-head">user-info-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ldap-server</span> - LDAP server to get group information. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">password2</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">password3</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">password4</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">password5</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">port</span> - Port of the first FSSO collector agent. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">port2</span> - Port of the second FSSO collector agent. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">port3</span> - Port of the third FSSO collector agent. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">port4</span> - Port of the fourth FSSO collector agent. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">port5</span> - Port of the fifth FSSO collector agent. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">server</span> - Domain name or IP address of the first FSSO collector agent. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server2</span> - Domain name or IP address of the second FSSO collector agent. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server3</span> - Domain name or IP address of the third FSSO collector agent. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server4</span> - Domain name or IP address of the fourth FSSO collector agent. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server5</span> - Domain name or IP address of the fifth FSSO collector agent. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-ip</span> - Source IP for communications to FSSO agent. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-ip6</span> - IPv6 source for communications to FSSO agent. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure Fortinet Single Sign On (FSSO) agents.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure Fortinet Single Sign On (FSSO) agents.</li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/USER/FSSO/{FSSO}
      fmgr_user_fsso_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            fsso: <value of string>
         params:
            -
               data:
                  _gui_meta: <value of string>
                  dynamic_mapping:
                    -
                        _gui_meta: <value of string>
                        _scope:
                          -
                              name: <value of string>
                              vdom: <value of string>
                        ldap-server: <value of string>
                        password:
                          - <value of string>
                        password2:
                          - <value of string>
                        password3:
                          - <value of string>
                        password4:
                          - <value of string>
                        password5:
                          - <value of string>
                        port: <value of integer>
                        port2: <value of integer>
                        port3: <value of integer>
                        port4: <value of integer>
                        port5: <value of integer>
                        server: <value of string>
                        server2: <value of string>
                        server3: <value of string>
                        server4: <value of string>
                        server5: <value of string>
                        source-ip: <value of string>
                        source-ip6: <value of string>
                        ssl: <value in [disable, enable]>
                        ssl-trusted-cert: <value of string>
                        type: <value in [default, fortiems, fortinac]>
                        user-info-server: <value of string>
                  ldap-server: <value of string>
                  name: <value of string>
                  password:
                    - <value of string>
                  password2:
                    - <value of string>
                  password3:
                    - <value of string>
                  password4:
                    - <value of string>
                  password5:
                    - <value of string>
                  port: <value of integer>
                  port2: <value of integer>
                  port3: <value of integer>
                  port4: <value of integer>
                  port5: <value of integer>
                  server: <value of string>
                  server2: <value of string>
                  server3: <value of string>
                  server4: <value of string>
                  server5: <value of string>
                  source-ip: <value of string>
                  source-ip6: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/USER/FSSO/{FSSO}
      fmgr_user_fsso_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            fsso: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/user/fsso/{fsso}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> _gui_meta </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dynamic_mapping </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> _gui_meta </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> _scope </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ldap-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> password2 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> password3 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> password4 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> password5 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> port </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> port2 </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> port3 </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> port4 </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> port5 </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server2 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server3 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server4 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server5 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-ip6 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-trusted-cert </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> user-info-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ldap-server </span> - LDAP server to get group information. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> password2 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> password3 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> password4 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> password5 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> port </span> - Port of the first FSSO collector agent. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> port2 </span> - Port of the second FSSO collector agent. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> port3 </span> - Port of the third FSSO collector agent. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> port4 </span> - Port of the fourth FSSO collector agent. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> port5 </span> - Port of the fifth FSSO collector agent. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> server </span> - Domain name or IP address of the first FSSO collector agent. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server2 </span> - Domain name or IP address of the second FSSO collector agent. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server3 </span> - Domain name or IP address of the third FSSO collector agent. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server4 </span> - Domain name or IP address of the fourth FSSO collector agent. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server5 </span> - Domain name or IP address of the fifth FSSO collector agent. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-ip </span> - Source IP for communications to FSSO agent. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-ip6 </span> - IPv6 source for communications to FSSO agent. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/user/fsso/{fsso}</span>  </li>
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



