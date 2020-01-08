:source: fmgr_pm_config_obj_waf_profile_signature.py

:orphan:

.. _fmgr_pm_config_obj_waf_profile_signature:

fmgr_pm_config_obj_waf_profile_signature -- WAF signatures.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/waf/profile/{profile}/signature`
- `/pm/config/global/obj/waf/profile/{profile}/signature`
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
 <li><span class="li-head">parameters for method: [get]</span> - WAF signatures.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - WAF signatures.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">credit-card-detection-threshold</span> - The minimum number of Credit cards to detect violation. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">custom-signature</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, erase]</span> </li>
 <li><span class="li-head">case-sensitivity</span> - Case sensitivity in pattern. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">direction</span> - Traffic direction. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [request, response]</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - Signature name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">pattern</span> - Match pattern. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">target</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [arg, arg-name, req-body, req-cookie, req-cookie-name, req-filename, req-header, req-header-name, req-raw-uri, req-uri, resp-body, resp-hdr, resp-status]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">disabled-signature</span> - Disabled signatures <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">disabled-sub-class</span> - Disabled signature subclasses. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">main-class</span> <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block, erase]</span> </li>
 <li><span class="li-head">id</span> - Main signature class ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WAF/PROFILE/{PROFILE}/SIGNATURE
      fmgr_pm_config_obj_waf_profile_signature:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/WAF/PROFILE/{PROFILE}/SIGNATURE
      fmgr_pm_config_obj_waf_profile_signature:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               data:
                  credit-card-detection-threshold: <value of integer>
                  custom-signature:
                    -
                        action: <value in [allow, block, erase]>
                        case-sensitivity: <value in [disable, enable]>
                        direction: <value in [request, response]>
                        log: <value in [disable, enable]>
                        name: <value of string>
                        pattern: <value of string>
                        severity: <value in [low, medium, high]>
                        status: <value in [disable, enable]>
                        target:
                          - <value in [arg, arg-name, req-body, ...]>
                  disabled-signature: <value of string>
                  disabled-sub-class: <value of string>
                  main-class:
                     action: <value in [allow, block, erase]>
                     id: <value of integer>
                     log: <value in [disable, enable]>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> credit-card-detection-threshold </span> - The minimum number of Credit cards to detect violation. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> custom-signature </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - Action. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> case-sensitivity </span> - Case sensitivity in pattern. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> direction </span> - Traffic direction. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Signature name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pattern </span> - Match pattern. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> severity </span> - Severity. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> target </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 </ul>
 <li> <span class="li-return"> disabled-signature </span> - Disabled signatures <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> disabled-sub-class </span> - Disabled signature subclasses. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> main-class </span> <li> <span class="li-return"> action </span> - Action. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Main signature class ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> severity </span> - Severity. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Status. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/waf/profile/{profile}/signature</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/waf/profile/{profile}/signature</span>  </li>
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



