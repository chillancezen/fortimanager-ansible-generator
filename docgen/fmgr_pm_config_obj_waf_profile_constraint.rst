:source: fmgr_pm_config_obj_waf_profile_constraint.py

:orphan:

.. _fmgr_pm_config_obj_waf_profile_constraint:

fmgr_pm_config_obj_waf_profile_constraint -- WAF HTTP protocol restrictions.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/waf/profile/{profile}/constraint`
- `/pm/config/global/obj/waf/profile/{profile}/constraint`
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
 <li><span class="li-head">parameters for method: [get]</span> - WAF HTTP protocol restrictions.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - WAF HTTP protocol restrictions.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">content-length</span> <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">length</span> - Length of HTTP content in bytes (0 to 2147483647). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">exception</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">address</span> - Host address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">content-length</span> - HTTP content length in request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">header-length</span> - HTTP header length in request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">hostname</span> - Enable/disable hostname check. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">id</span> - Exception ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">line-length</span> - HTTP line length in request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">malformed</span> - Enable/disable malformed HTTP request check. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-cookie</span> - Maximum number of cookies in HTTP request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-header-line</span> - Maximum number of HTTP header line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-range-segment</span> - Maximum number of range segments in HTTP range line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-url-param</span> - Maximum number of parameters in URL. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">method</span> - Enable/disable HTTP method check. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">param-length</span> - Maximum length of parameter in URL, HTTP POST request or HTTP body. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pattern</span> - URL pattern. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">regex</span> - Enable/disable regular expression based pattern match. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">url-param-length</span> - Maximum length of parameter in URL. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">version</span> - Enable/disable HTTP version check. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">header-length</span> <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">length</span> - Length of HTTP header in bytes (0 to 2147483647). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">hostname</span> <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">line-length</span> <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">length</span> - Length of HTTP line in bytes (0 to 2147483647). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">malformed</span> <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-cookie</span> <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-cookie</span> - Maximum number of cookies in HTTP request (0 to 2147483647). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-header-line</span> <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-header-line</span> - Maximum number HTTP header lines (0 to 2147483647). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-range-segment</span> <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-range-segment</span> - Maximum number of range segments in HTTP range line (0 to 2147483647). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-url-param</span> <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">max-url-param</span> - Maximum number of parameters in URL (0 to 2147483647). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">method</span> <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">param-length</span> <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">length</span> - Maximum length of parameter in URL, HTTP POST request or HTTP body in bytes (0 to 2147483647). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">url-param-length</span> <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">length</span> - Maximum length of URL parameter in bytes (0 to 2147483647). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">version</span> <li><span class="li-head">action</span> - Action. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, block]</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">severity</span> - Severity. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, medium, high]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WAF/PROFILE/{PROFILE}/CONSTRAINT
      fmgr_pm_config_obj_waf_profile_constraint:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/WAF/PROFILE/{PROFILE}/CONSTRAINT
      fmgr_pm_config_obj_waf_profile_constraint:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               data:
                  content-length:
                     action: <value in [allow, block]>
                     length: <value of integer>
                     log: <value in [disable, enable]>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  exception:
                    -
                        address: <value of string>
                        content-length: <value in [disable, enable]>
                        header-length: <value in [disable, enable]>
                        hostname: <value in [disable, enable]>
                        id: <value of integer>
                        line-length: <value in [disable, enable]>
                        malformed: <value in [disable, enable]>
                        max-cookie: <value in [disable, enable]>
                        max-header-line: <value in [disable, enable]>
                        max-range-segment: <value in [disable, enable]>
                        max-url-param: <value in [disable, enable]>
                        method: <value in [disable, enable]>
                        param-length: <value in [disable, enable]>
                        pattern: <value of string>
                        regex: <value in [disable, enable]>
                        url-param-length: <value in [disable, enable]>
                        version: <value in [disable, enable]>
                  header-length:
                     action: <value in [allow, block]>
                     length: <value of integer>
                     log: <value in [disable, enable]>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  hostname:
                     action: <value in [allow, block]>
                     log: <value in [disable, enable]>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  line-length:
                     action: <value in [allow, block]>
                     length: <value of integer>
                     log: <value in [disable, enable]>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  malformed:
                     action: <value in [allow, block]>
                     log: <value in [disable, enable]>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  max-cookie:
                     action: <value in [allow, block]>
                     log: <value in [disable, enable]>
                     max-cookie: <value of integer>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  max-header-line:
                     action: <value in [allow, block]>
                     log: <value in [disable, enable]>
                     max-header-line: <value of integer>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  max-range-segment:
                     action: <value in [allow, block]>
                     log: <value in [disable, enable]>
                     max-range-segment: <value of integer>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  max-url-param:
                     action: <value in [allow, block]>
                     log: <value in [disable, enable]>
                     max-url-param: <value of integer>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  method:
                     action: <value in [allow, block]>
                     log: <value in [disable, enable]>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  param-length:
                     action: <value in [allow, block]>
                     length: <value of integer>
                     log: <value in [disable, enable]>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  url-param-length:
                     action: <value in [allow, block]>
                     length: <value of integer>
                     log: <value in [disable, enable]>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  version:
                     action: <value in [allow, block]>
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
 <li> <span class="li-return"> content-length </span> <li> <span class="li-return"> action </span> - Action. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> length </span> - Length of HTTP content in bytes (0 to 2147483647). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> severity </span> - Severity. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> exception </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> address </span> - Host address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> content-length </span> - HTTP content length in request. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> header-length </span> - HTTP header length in request. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> hostname </span> - Enable/disable hostname check. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Exception ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> line-length </span> - HTTP line length in request. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed </span> - Enable/disable malformed HTTP request check. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-cookie </span> - Maximum number of cookies in HTTP request. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-header-line </span> - Maximum number of HTTP header line. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-range-segment </span> - Maximum number of range segments in HTTP range line. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-url-param </span> - Maximum number of parameters in URL. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> method </span> - Enable/disable HTTP method check. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> param-length </span> - Maximum length of parameter in URL, HTTP POST request or HTTP body. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pattern </span> - URL pattern. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> regex </span> - Enable/disable regular expression based pattern match. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> url-param-length </span> - Maximum length of parameter in URL. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> version </span> - Enable/disable HTTP version check. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> header-length </span> <li> <span class="li-return"> action </span> - Action. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> length </span> - Length of HTTP header in bytes (0 to 2147483647). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> severity </span> - Severity. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> hostname </span> <li> <span class="li-return"> action </span> - Action. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> severity </span> - Severity. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> line-length </span> <li> <span class="li-return"> action </span> - Action. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> length </span> - Length of HTTP line in bytes (0 to 2147483647). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> severity </span> - Severity. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed </span> <li> <span class="li-return"> action </span> - Action. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> severity </span> - Severity. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-cookie </span> <li> <span class="li-return"> action </span> - Action. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-cookie </span> - Maximum number of cookies in HTTP request (0 to 2147483647). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> severity </span> - Severity. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-header-line </span> <li> <span class="li-return"> action </span> - Action. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-header-line </span> - Maximum number HTTP header lines (0 to 2147483647). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> severity </span> - Severity. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-range-segment </span> <li> <span class="li-return"> action </span> - Action. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-range-segment </span> - Maximum number of range segments in HTTP range line (0 to 2147483647). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> severity </span> - Severity. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-url-param </span> <li> <span class="li-return"> action </span> - Action. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-url-param </span> - Maximum number of parameters in URL (0 to 2147483647). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> severity </span> - Severity. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> method </span> <li> <span class="li-return"> action </span> - Action. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> severity </span> - Severity. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> param-length </span> <li> <span class="li-return"> action </span> - Action. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> length </span> - Maximum length of parameter in URL, HTTP POST request or HTTP body in bytes (0 to 2147483647). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> severity </span> - Severity. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> url-param-length </span> <li> <span class="li-return"> action </span> - Action. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> length </span> - Maximum length of URL parameter in bytes (0 to 2147483647). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> severity </span> - Severity. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> version </span> <li> <span class="li-return"> action </span> - Action. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> severity </span> - Severity. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable the constraint. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/waf/profile/{profile}/constraint</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/waf/profile/{profile}/constraint</span>  </li>
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



