:source: fmgr_pm_config_obj_waf_profile_constraint_exception.py

:orphan:

.. _fmgr_pm_config_obj_waf_profile_constraint_exception:

fmgr_pm_config_obj_waf_profile_constraint_exception -- HTTP constraint exception.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/waf/profile/{profile}/constraint/exception`
- `/pm/config/global/obj/waf/profile/{profile}/constraint/exception`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - HTTP constraint exception.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
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
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - HTTP constraint exception.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [address, content-length, header-length, hostname, id, line-length, malformed, max-cookie, max-header-line, max-range-segment, max-url-param, method, param-length, pattern, regex, url-param-length, version]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WAF/PROFILE/{PROFILE}/CONSTRAINT/EXCEPTION
      fmgr_pm_config_obj_waf_profile_constraint_exception:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               data:
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

    - name: REQUESTING /PM/CONFIG/OBJ/WAF/PROFILE/{PROFILE}/CONSTRAINT/EXCEPTION
      fmgr_pm_config_obj_waf_profile_constraint_exception:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [address, content-length, header-length, ...]>
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
 <li> <span class="li-return"> id </span> - Exception ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/waf/profile/{profile}/constraint/exception</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
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
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/waf/profile/{profile}/constraint/exception</span>  </li>
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



