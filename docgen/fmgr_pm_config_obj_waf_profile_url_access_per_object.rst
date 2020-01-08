:source: fmgr_pm_config_obj_waf_profile_url_access_per_object.py

:orphan:

.. _fmgr_pm_config_obj_waf_profile_url_access_per_object:

fmgr_pm_config_obj_waf_profile_url_access_per_object -- URL access list
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/waf/profile/{profile}/url-access/{url-access}`
- `/pm/config/global/obj/waf/profile/{profile}/url-access/{url-access}`
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
 <li><span class="li-head">url-access</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - URL access list</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">access-pattern</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - URL access pattern ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">negate</span> - Enable/disable match negation. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pattern</span> - URL pattern. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">regex</span> - Enable/disable regular expression based pattern match. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">srcaddr</span> - Source address. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, permit, block]</span> </li>
 <li><span class="li-head">address</span> - Host address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - URL access ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - URL access list</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - URL access list</li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WAF/PROFILE/{PROFILE}/URL-ACCESS/{URL-ACCESS}
      fmgr_pm_config_obj_waf_profile_url_access_per_object:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
            url-access: <value of string>
         params:
            -
               data:
                  access-pattern:
                    -
                        id: <value of integer>
                        negate: <value in [disable, enable]>
                        pattern: <value of string>
                        regex: <value in [disable, enable]>
                        srcaddr: <value of string>
                  action: <value in [bypass, permit, block]>
                  address: <value of string>
                  id: <value of integer>
                  log: <value in [disable, enable]>
                  severity: <value in [low, medium, high]>

    - name: REQUESTING /PM/CONFIG/OBJ/WAF/PROFILE/{PROFILE}/URL-ACCESS/{URL-ACCESS}
      fmgr_pm_config_obj_waf_profile_url_access_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
            url-access: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [clone, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - URL access ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/waf/profile/{profile}/url-access/{url-access}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [delete]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/waf/profile/{profile}/url-access/{url-access}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> access-pattern </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - URL access pattern ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> negate </span> - Enable/disable match negation. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pattern </span> - URL pattern. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> regex </span> - Enable/disable regular expression based pattern match. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcaddr </span> - Source address. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> action </span> - Action. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> address </span> - Host address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - URL access ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> severity </span> - Severity. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/waf/profile/{profile}/url-access/{url-access}</span>  </li>
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



