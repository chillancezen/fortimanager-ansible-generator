:source: fmgr_pm_config_obj_webfilter_profile_ftgd_wf.py

:orphan:

.. _fmgr_pm_config_obj_webfilter_profile_ftgd_wf:

fmgr_pm_config_obj_webfilter_profile_ftgd_wf -- FortiGuard Web Filter settings.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/webfilter/profile/{profile}/ftgd-wf`
- `/pm/config/global/obj/webfilter/profile/{profile}/ftgd-wf`
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
 <li><span class="li-head">parameters for method: [get]</span> - FortiGuard Web Filter settings.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - FortiGuard Web Filter settings.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">exempt-quota</span> - Do not stop quota for these categories. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">filters</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action to take for matches. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [block, monitor, warning, authenticate]</span> </li>
 <li><span class="li-head">auth-usr-grp</span> - Groups with permission to authenticate. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">category</span> - Categories and groups the filter examines. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">log</span> - Enable/disable logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">override-replacemsg</span> - Override replacement message. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">warn-duration</span> - Duration of warnings. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">warning-duration-type</span> - Re-display warning after closing browser or after a timeout. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [session, timeout]</span> </li>
 <li><span class="li-head">warning-prompt</span> - Warning prompts in each category or each domain. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [per-domain, per-category]</span> </li>
 </ul>
 <li><span class="li-head">max-quota-timeout</span> - Maximum FortiGuard quota used by single page view in seconds (excludes streams). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [error-allow, http-err-detail, rate-image-urls, strict-blocking, rate-server-ip, redir-block, connect-request-bypass, log-all-url, ftgd-disable]</span> </li>
 </ul>
 <li><span class="li-head">ovrd</span> - Allow web filter profile overrides. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">quota</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">category</span> - FortiGuard categories to apply quota to (category action must be set to monitor). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">duration</span> - Duration of quota. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">override-replacemsg</span> - Override replacement message. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - Quota type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [time, traffic]</span> </li>
 <li><span class="li-head">unit</span> - Traffic quota unit of measurement. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [B, KB, MB, GB]</span> </li>
 <li><span class="li-head">value</span> - Traffic quota value. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">rate-crl-urls</span> - Enable/disable rating CRL by URL. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rate-css-urls</span> - Enable/disable rating CSS by URL. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rate-image-urls</span> - Enable/disable rating images by URL. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rate-javascript-urls</span> - Enable/disable rating JavaScript by URL. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WEBFILTER/PROFILE/{PROFILE}/FTGD-WF
      fmgr_pm_config_obj_webfilter_profile_ftgd_wf:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/WEBFILTER/PROFILE/{PROFILE}/FTGD-WF
      fmgr_pm_config_obj_webfilter_profile_ftgd_wf:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               data:
                  exempt-quota: <value of string>
                  filters:
                    -
                        action: <value in [block, monitor, warning, ...]>
                        auth-usr-grp: <value of string>
                        category: <value of string>
                        id: <value of integer>
                        log: <value in [disable, enable]>
                        override-replacemsg: <value of string>
                        warn-duration: <value of string>
                        warning-duration-type: <value in [session, timeout]>
                        warning-prompt: <value in [per-domain, per-category]>
                  max-quota-timeout: <value of integer>
                  options:
                    - <value in [error-allow, http-err-detail, rate-image-urls, ...]>
                  ovrd: <value of string>
                  quota:
                    -
                        category: <value of string>
                        duration: <value of string>
                        id: <value of integer>
                        override-replacemsg: <value of string>
                        type: <value in [time, traffic]>
                        unit: <value in [B, KB, MB, ...]>
                        value: <value of integer>
                  rate-crl-urls: <value in [disable, enable]>
                  rate-css-urls: <value in [disable, enable]>
                  rate-image-urls: <value in [disable, enable]>
                  rate-javascript-urls: <value in [disable, enable]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> exempt-quota </span> - Do not stop quota for these categories. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> filters </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - Action to take for matches. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auth-usr-grp </span> - Groups with permission to authenticate. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> category </span> - Categories and groups the filter examines. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - ID number. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> log </span> - Enable/disable logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> override-replacemsg </span> - Override replacement message. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> warn-duration </span> - Duration of warnings. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> warning-duration-type </span> - Re-display warning after closing browser or after a timeout. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> warning-prompt </span> - Warning prompts in each category or each domain. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> max-quota-timeout </span> - Maximum FortiGuard quota used by single page view in seconds (excludes streams). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> options </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ovrd </span> - Allow web filter profile overrides. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> quota </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> category </span> - FortiGuard categories to apply quota to (category action must be set to monitor). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> duration </span> - Duration of quota. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - ID number. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> override-replacemsg </span> - Override replacement message. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - Quota type. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> unit </span> - Traffic quota unit of measurement. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> value </span> - Traffic quota value. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> rate-crl-urls </span> - Enable/disable rating CRL by URL. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rate-css-urls </span> - Enable/disable rating CSS by URL. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rate-image-urls </span> - Enable/disable rating images by URL. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rate-javascript-urls </span> - Enable/disable rating JavaScript by URL. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/webfilter/profile/{profile}/ftgd-wf</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/webfilter/profile/{profile}/ftgd-wf</span>  </li>
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



