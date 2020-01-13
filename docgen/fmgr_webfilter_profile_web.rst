:source: fmgr_webfilter_profile_web.py

:orphan:

.. _fmgr_webfilter_profile_web:

fmgr_webfilter_profile_web -- Web content filtering settings.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/webfilter/profile/{profile}/web`
- `/pm/config/global/obj/webfilter/profile/{profile}/web`
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
 <li><span class="li-head">parameters for method: [get]</span> - Web content filtering settings.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Web content filtering settings.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">blacklist</span> - Enable/disable automatic addition of URLs detected by FortiSandbox to blacklist. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">bword-table</span> - Banned word table ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">bword-threshold</span> - Banned word score threshold. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">content-header-list</span> - Content header list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">keyword-match</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">log-search</span> - Enable/disable logging all search phrases. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">safe-search</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [google, yahoo, bing, url, header]</span> </li>
 </ul>
 <li><span class="li-head">urlfilter-table</span> - URL filter table ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">whitelist</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [exempt-av, exempt-webcontent, exempt-activex-java-cookie, exempt-dlp, exempt-rangeblock, extended-log-others]</span> </li>
 </ul>
 <li><span class="li-head">youtube-restrict</span> - YouTube EDU filter level. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [strict, none, moderate]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WEBFILTER/PROFILE/{PROFILE}/WEB
      fmgr_webfilter_profile_web:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/WEBFILTER/PROFILE/{PROFILE}/WEB
      fmgr_webfilter_profile_web:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               data:
                  blacklist: <value in [disable, enable]>
                  bword-table: <value of string>
                  bword-threshold: <value of integer>
                  content-header-list: <value of string>
                  keyword-match:
                    - <value of string>
                  log-search: <value in [disable, enable]>
                  safe-search:
                    - <value in [google, yahoo, bing, ...]>
                  urlfilter-table: <value of string>
                  whitelist:
                    - <value in [exempt-av, exempt-webcontent, exempt-activex-java-cookie, ...]>
                  youtube-restrict: <value in [strict, none, moderate]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> blacklist </span> - Enable/disable automatic addition of URLs detected by FortiSandbox to blacklist. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> bword-table </span> - Banned word table ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> bword-threshold </span> - Banned word score threshold. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> content-header-list </span> - Content header list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> keyword-match </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> log-search </span> - Enable/disable logging all search phrases. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> safe-search </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> urlfilter-table </span> - URL filter table ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> whitelist </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> youtube-restrict </span> - YouTube EDU filter level. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/webfilter/profile/{profile}/web</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/webfilter/profile/{profile}/web</span>  </li>
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



