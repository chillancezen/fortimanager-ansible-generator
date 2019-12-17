:source: fmgr_pm_config_obj_icap_profile_profile.py

:orphan:

.. _fmgr_pm_config_obj_icap_profile_profile:

fmgr_pm_config_obj_icap_profile_profile -- Configure ICAP profiles.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/icap/profile/{profile}`
- `/pm/config/global/obj/icap/profile/{profile}`
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
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure ICAP profiles.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">methods</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [delete, get, head, options, post, put, trace, other]</span> </li>
 </ul>
 <li><span class="li-head">name</span> - ICAP profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">replacemsg-group</span> - Replacement message group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">request</span> - Enable/disable whether an HTTP request is passed to an ICAP server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">request-failure</span> - Action to take if the ICAP server cannot be contacted when processing an HTTP request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [error, bypass]</span> </li>
 <li><span class="li-head">request-path</span> - Path component of the ICAP URI that identifies the HTTP request processing service. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">request-server</span> - ICAP server to use for an HTTP request. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">response</span> - Enable/disable whether an HTTP response is passed to an ICAP server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">response-failure</span> - Action to take if the ICAP server cannot be contacted when processing an HTTP response. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [error, bypass]</span> </li>
 <li><span class="li-head">response-path</span> - Path component of the ICAP URI that identifies the HTTP response processing service. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">response-server</span> - ICAP server to use for an HTTP response. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">streaming-content-bypass</span> - Enable/disable bypassing of ICAP server for streaming content. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure ICAP profiles.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure ICAP profiles.</li>
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
    - name: send request to /pm/config/obj/icap/profile/{profile}
      fmgr_pm_config_obj_icap_profile_profile:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            - 
               data: 
                  methods: 
                   - <value in [delete, get, head, ...]>
                  name: <value of string>
                  replacemsg-group: <value of string>
                  request: <value in [disable, enable]>
                  request-failure: <value in [error, bypass]>
                  request-path: <value of string>
                  request-server: <value of string>
                  response: <value in [disable, enable]>
                  response-failure: <value in [error, bypass]>
                  response-path: <value of string>
                  response-server: <value of string>
                  streaming-content-bypass: <value in [disable, enable]>
    - name: send request to /pm/config/obj/icap/profile/{profile}
      fmgr_pm_config_obj_icap_profile_profile:
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/icap/profile/{profile}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> methods </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> name </span> - ICAP profile name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> replacemsg-group </span> - Replacement message group. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> request </span> - Enable/disable whether an HTTP request is passed to an ICAP server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> request-failure </span> - Action to take if the ICAP server cannot be contacted when processing an HTTP request. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> request-path </span> - Path component of the ICAP URI that identifies the HTTP request processing service. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> request-server </span> - ICAP server to use for an HTTP request. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> response </span> - Enable/disable whether an HTTP response is passed to an ICAP server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> response-failure </span> - Action to take if the ICAP server cannot be contacted when processing an HTTP response. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> response-path </span> - Path component of the ICAP URI that identifies the HTTP response processing service. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> response-server </span> - ICAP server to use for an HTTP response. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> streaming-content-bypass </span> - Enable/disable bypassing of ICAP server for streaming content. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/icap/profile/{profile}</span>  </li>
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



