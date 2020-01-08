:source: fmgr_pm_config_obj_system_replacemsg_group_mm4_per_object.py

:orphan:

.. _fmgr_pm_config_obj_system_replacemsg_group_mm4_per_object:

fmgr_pm_config_obj_system_replacemsg_group_mm4_per_object -- Replacement message table entries.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/system/replacemsg-group/{replacemsg-group}/mm4/{mm4}`
- `/pm/config/global/obj/system/replacemsg-group/{replacemsg-group}/mm4/{mm4}`
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
 <li><span class="li-head">replacemsg-group</span> - the object name <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mm4</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Replacement message table entries.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">add-smil</span> - add message encapsulation <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">charset</span> - character encoding used for replacement message <span class="li-normal">type: str</span>  <span class="li-normal">choices: [us-ascii, utf-8]</span> </li>
 <li><span class="li-head">class</span> - message class <span class="li-normal">type: str</span>  <span class="li-normal">choices: [personal, advertisement, informational, auto, not-included]</span> </li>
 <li><span class="li-head">domain</span> - from address domain <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - Format flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">from</span> - from address <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">from-sender</span> - notification message sent from recipient <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">header</span> - Header flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">image</span> - Message string. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">message</span> - message text <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">msg-type</span> - Message type. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priority</span> - message priority <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, normal, high, not-included]</span> </li>
 <li><span class="li-head">rsp-status</span> - response status <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ok, err-unspecified, err-srv-denied, err-msg-fmt-corrupt, err-snd-addr-unresolv, err-net-prob, err-content-not-accept, err-unsupp-msg]</span> </li>
 <li><span class="li-head">smil-part</span> - message encapsulation text <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">subject</span> - subject text string <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Replacement message table entries.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Replacement message table entries.</li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/SYSTEM/REPLACEMSG-GROUP/{REPLACEMSG-GROUP}/MM4/{MM4}
      fmgr_pm_config_obj_system_replacemsg_group_mm4_per_object:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            replacemsg-group: <value of string>
            mm4: <value of string>
         params:
            -
               data:
                  add-smil: <value in [disable, enable]>
                  charset: <value in [us-ascii, utf-8]>
                  class: <value in [personal, advertisement, informational, ...]>
                  domain: <value of string>
                  format: <value in [none, text, html, ...]>
                  from: <value of string>
                  from-sender: <value in [disable, enable]>
                  header: <value in [none, http, 8bit]>
                  image: <value of string>
                  message: <value of string>
                  msg-type: <value of string>
                  priority: <value in [low, normal, high, ...]>
                  rsp-status: <value in [ok, err-unspecified, err-srv-denied, ...]>
                  smil-part: <value of string>
                  subject: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/SYSTEM/REPLACEMSG-GROUP/{REPLACEMSG-GROUP}/MM4/{MM4}
      fmgr_pm_config_obj_system_replacemsg_group_mm4_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            replacemsg-group: <value of string>
            mm4: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/system/replacemsg-group/{replacemsg-group}/mm4/{mm4}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> add-smil </span> - add message encapsulation <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> charset </span> - character encoding used for replacement message <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> class </span> - message class <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> domain </span> - from address domain <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> format </span> - Format flag. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> from </span> - from address <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> from-sender </span> - notification message sent from recipient <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> header </span> - Header flag. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> image </span> - Message string. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> message </span> - message text <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> msg-type </span> - Message type. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> priority </span> - message priority <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rsp-status </span> - response status <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> smil-part </span> - message encapsulation text <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> subject </span> - subject text string <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/system/replacemsg-group/{replacemsg-group}/mm4/{mm4}</span>  </li>
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



