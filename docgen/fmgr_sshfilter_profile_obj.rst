:source: fmgr_sshfilter_profile_obj.py

:orphan:

.. _fmgr_sshfilter_profile_obj:

fmgr_sshfilter_profile_obj -- SSH filter profile.
+++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/ssh-filter/profile/{profile}`
- `/pm/config/global/obj/ssh-filter/profile/{profile}`
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
 <li><span class="li-head">profile</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - SSH filter profile.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">block</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [x11, shell, exec, port-forward, tun-forward, sftp, unknown]</span> </li>
 </ul>
 <li><span class="li-head">default-command-log</span> - Enable/disable logging unmatched shell commands. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">log</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [x11, shell, exec, port-forward, tun-forward, sftp, unknown]</span> </li>
 </ul>
 <li><span class="li-head">name</span> - SSH filter profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">shell-commands</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action to take for URL filter matches. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [block, allow]</span> </li>
 <li><span class="li-head">alert</span> - Enable/disable alert. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">id</span> - Id. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pattern</span> - SSH shell command pattern. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">severity</span> - Log severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high, critical]</span> </li>
 <li><span class="li-head">type</span> - Matching type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regex, simple]</span> </li>
 </ul>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - SSH filter profile.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - SSH filter profile.</li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/SSH-FILTER/PROFILE/{PROFILE}
      fmgr_sshfilter_profile_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               data:
                  block:
                    - <value in [x11, shell, exec, ...]>
                  default-command-log: <value in [disable, enable]>
                  log:
                    - <value in [x11, shell, exec, ...]>
                  name: <value of string>
                  shell-commands:
                    -
                        action: <value in [block, allow]>
                        alert: <value in [disable, enable]>
                        id: <value of integer>
                        log: <value in [disable, enable]>
                        pattern: <value of string>
                        severity: <value in [low, medium, high, ...]>
                        type: <value in [regex, simple]>

    - name: REQUESTING /PM/CONFIG/OBJ/SSH-FILTER/PROFILE/{PROFILE}
      fmgr_sshfilter_profile_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/ssh-filter/profile/{profile}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> block </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> default-command-log </span> - Enable/disable logging unmatched shell commands. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> name </span> - SSH filter profile name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> shell-commands </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - Action to take for URL filter matches. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> alert </span> - Enable/disable alert. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Id. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pattern </span> - SSH shell command pattern. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> severity </span> - Log severity. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - Matching type. <span class="li-normal">type: str</span>  </li>
 </ul>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/ssh-filter/profile/{profile}</span>  </li>
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



