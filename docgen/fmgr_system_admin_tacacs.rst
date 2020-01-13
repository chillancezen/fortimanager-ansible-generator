:source: fmgr_system_admin_tacacs.py

:orphan:

.. _fmgr_system_admin_tacacs:

fmgr_system_admin_tacacs -- TACACS+ server entry configuration.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/admin/tacacs`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - TACACS+ server entry configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">authen-type</span> - Authentication type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, ascii, pap, chap, mschap]</span>  <span class="li-normal">default: auto</span> </li>
 <li><span class="li-head">authorization</span> - Enable/disable TACACS+ authorization. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">key</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC MTM1NzgxNTEwMTQ3MzkyN6Bf+SUc1DH38ALtjfXS+4tsPEStofpzICCe9zH2nI/U1uDRuS4ysXoRMhkM/i6ypV7BvpqVqu3wnaI3lWsFOh6+06ydV9EyGZ+z+v4JkMDSSJ5UHQdPh8DxRdsVvWS3WpWWGFXk4064PiT2A1zTZuT+ZqDM</span> </li>
 </ul>
 <li><span class="li-head">name</span> - TACACS+ server entry name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port</span> - Port number of TACACS+ server. <span class="li-normal">type: int</span>  <span class="li-normal">default: 49</span> </li>
 <li><span class="li-head">secondary-key</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC MTM3MzM0NTI4MzQ3MTQ4OftOEtzg8U8bz+L2zW2yOkzO1vkOesoOkTy2j02IrPnwTVEVz7aOODvx+zGMUtELHdsY22GW20r4Q0OasjCqkmZgjt9PbfLA2Np3vyJ5ZPtz0IUohnN5frAIVPy7p2VtSHJmvOK3PrMoiwLcSesT0RKSn//Q</span> </li>
 </ul>
 <li><span class="li-head">secondary-server</span> - {<name_str|ip_str>} secondary server domain name or IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server</span> - {<name_str|ip_str>} server domain name or IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tertiary-key</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC MjAzNTE3MDIwNDI1OTEwMgAtMeOT5CzyMlsFCmOGJ8cTlQYpjv7BJI+uC5QN2LxVGteUJ87W++EYhPaChx42doThcM3Gtb7w8PfrihahuU7S+qoi9weI6eVMq6AUQ7Zw0AomShHbqS8QLEsNf1a59nYX+Lp2wFPwgSYT4xlLOXCNX18h</span> </li>
 </ul>
 <li><span class="li-head">tertiary-server</span> - {<name_str|ip_str>} tertiary server domain name or IP. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - TACACS+ server entry configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [authen-type, authorization, key, name, port, secondary-key, secondary-server, server, tertiary-key, tertiary-server]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">loadsub</span> - Enable or disable the return of any sub-objects. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [count, syntax]</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/ADMIN/TACACS
      fmgr_system_admin_tacacs:
         method: <value in [add, set, update]>
         params:
            -
               data:
                 -
                     authen-type: <value in [auto, ascii, pap, ...] default: 'auto'>
                     authorization: <value in [disable, enable] default: 'disable'>
                     key:
                       - <value of string default: 'ENC MTM1NzgxNTEwMTQ3MzkyN6Bf+SUc1DH38ALtjfXS+4tsPEStofpzICCe9zH2nI/U1uDRuS4y...'>
                     name: <value of string>
                     port: <value of integer default: 49>
                     secondary-key:
                       - <value of string default: 'ENC MTM3MzM0NTI4MzQ3MTQ4OftOEtzg8U8bz+L2zW2yOkzO1vkOesoOkTy2j02IrPnwTVEVz7aO...'>
                     secondary-server: <value of string>
                     server: <value of string>
                     tertiary-key:
                       - <value of string default: 'ENC MjAzNTE3MDIwNDI1OTEwMgAtMeOT5CzyMlsFCmOGJ8cTlQYpjv7BJI+uC5QN2LxVGteUJ87W...'>
                     tertiary-server: <value of string>

    - name: REQUESTING /CLI/SYSTEM/ADMIN/TACACS
      fmgr_system_admin_tacacs:
         method: <value in [get]>
         params:
            -
               fields:
                 -
                    - <value in [authen-type, authorization, key, ...]>
               filter:
                 - <value of string>
               loadsub: <value of integer>
               option: <value in [count, syntax]>



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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/admin/tacacs</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> authen-type </span> - Authentication type. <span class="li-normal">type: str</span>  <span class="li-normal">example: auto</span>  </li>
 <li> <span class="li-return"> authorization </span> - Enable/disable TACACS+ authorization. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> key </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC MTM1NzgxNTEwMTQ3MzkyN6Bf+SUc1DH38ALtjfXS+4tsPEStofpzICCe9zH2nI/U1uDRuS4ysXoRMhkM/i6ypV7BvpqVqu3wnaI3lWsFOh6+06ydV9EyGZ+z+v4JkMDSSJ5UHQdPh8DxRdsVvWS3WpWWGFXk4064PiT2A1zTZuT+ZqDM</span>  </li>
 </ul>
 <li> <span class="li-return"> name </span> - TACACS+ server entry name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port </span> - Port number of TACACS+ server. <span class="li-normal">type: int</span>  <span class="li-normal">example: 49</span>  </li>
 <li> <span class="li-return"> secondary-key </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC MTM3MzM0NTI4MzQ3MTQ4OftOEtzg8U8bz+L2zW2yOkzO1vkOesoOkTy2j02IrPnwTVEVz7aOODvx+zGMUtELHdsY22GW20r4Q0OasjCqkmZgjt9PbfLA2Np3vyJ5ZPtz0IUohnN5frAIVPy7p2VtSHJmvOK3PrMoiwLcSesT0RKSn//Q</span>  </li>
 </ul>
 <li> <span class="li-return"> secondary-server </span> - {<name_str|ip_str>} secondary server domain name or IP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server </span> - {<name_str|ip_str>} server domain name or IP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tertiary-key </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC MjAzNTE3MDIwNDI1OTEwMgAtMeOT5CzyMlsFCmOGJ8cTlQYpjv7BJI+uC5QN2LxVGteUJ87W++EYhPaChx42doThcM3Gtb7w8PfrihahuU7S+qoi9weI6eVMq6AUQ7Zw0AomShHbqS8QLEsNf1a59nYX+Lp2wFPwgSYT4xlLOXCNX18h</span>  </li>
 </ul>
 <li> <span class="li-return"> tertiary-server </span> - {<name_str|ip_str>} tertiary server domain name or IP. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/admin/tacacs</span>  </li>
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



