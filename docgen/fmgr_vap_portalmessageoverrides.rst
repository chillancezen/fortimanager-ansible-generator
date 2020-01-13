:source: fmgr_vap_portalmessageoverrides.py

:orphan:

.. _fmgr_vap_portalmessageoverrides:

fmgr_vap_portalmessageoverrides -- Individual message overrides.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/wireless-controller/vap/{vap}/portal-message-overrides`
- `/pm/config/global/obj/wireless-controller/vap/{vap}/portal-message-overrides`
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
 <li><span class="li-head">vap</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Individual message overrides.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Individual message overrides.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">auth-disclaimer-page</span> - Override auth-disclaimer-page message with message from portal-message-overrides group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">auth-login-failed-page</span> - Override auth-login-failed-page message with message from portal-message-overrides group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">auth-login-page</span> - Override auth-login-page message with message from portal-message-overrides group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">auth-reject-page</span> - Override auth-reject-page message with message from portal-message-overrides group. <span class="li-normal">type: str</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/VAP/{VAP}/PORTAL-MESSAGE-OVERRIDES
      fmgr_vap_portalmessageoverrides:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vap: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/VAP/{VAP}/PORTAL-MESSAGE-OVERRIDES
      fmgr_vap_portalmessageoverrides:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vap: <value of string>
         params:
            -
               data:
                  auth-disclaimer-page: <value of string>
                  auth-login-failed-page: <value of string>
                  auth-login-page: <value of string>
                  auth-reject-page: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> auth-disclaimer-page </span> - Override auth-disclaimer-page message with message from portal-message-overrides group. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auth-login-failed-page </span> - Override auth-login-failed-page message with message from portal-message-overrides group. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auth-login-page </span> - Override auth-login-page message with message from portal-message-overrides group. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auth-reject-page </span> - Override auth-reject-page message with message from portal-message-overrides group. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/vap/{vap}/portal-message-overrides</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/vap/{vap}/portal-message-overrides</span>  </li>
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



