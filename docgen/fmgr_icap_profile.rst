:source: fmgr_icap_profile.py

:orphan:

.. _fmgr_icap_profile:

fmgr_icap_profile -- Configure ICAP profiles.
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/icap/profile`
- `/pm/config/global/obj/icap/profile`
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
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure ICAP profiles.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
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
 <li><span class="li-head">parameters for method: [get]</span> - Configure ICAP profiles.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [methods, name, replacemsg-group, request, request-failure, request-path, request-server, response, response-failure, response-path, response-server, streaming-content-bypass]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/ICAP/PROFILE
      fmgr_icap_profile:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
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

    - name: REQUESTING /PM/CONFIG/OBJ/ICAP/PROFILE
      fmgr_icap_profile:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [methods, name, replacemsg-group, ...]>
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
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/icap/profile</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/icap/profile</span>  </li>
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



