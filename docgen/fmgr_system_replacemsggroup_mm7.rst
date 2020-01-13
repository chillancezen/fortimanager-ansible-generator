:source: fmgr_system_replacemsggroup_mm7.py

:orphan:

.. _fmgr_system_replacemsggroup_mm7:

fmgr_system_replacemsggroup_mm7 -- Replacement message table entries.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/system/replacemsg-group/{replacemsg-group}/mm7`
- `/pm/config/global/obj/system/replacemsg-group/{replacemsg-group}/mm7`
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
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Replacement message table entries.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">add-smil</span> - add message encapsulation <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">addr-type</span> - from address type <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rfc2822-addr, number, short-code]</span> </li>
 <li><span class="li-head">allow-content-adaptation</span> - allow content adaptations <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">charset</span> - character encoding used for replacement message <span class="li-normal">type: str</span>  <span class="li-normal">choices: [us-ascii, utf-8]</span> </li>
 <li><span class="li-head">class</span> - message class <span class="li-normal">type: str</span>  <span class="li-normal">choices: [personal, advertisement, informational, auto, not-included]</span> </li>
 <li><span class="li-head">format</span> - Format flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">from</span> - from address <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">from-sender</span> - notification message sent from recipient <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">header</span> - Header flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">image</span> - Message string. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">message</span> - message text <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">msg-type</span> - Message type. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priority</span> - message priority <span class="li-normal">type: str</span>  <span class="li-normal">choices: [low, normal, high, not-included]</span> </li>
 <li><span class="li-head">rsp-status</span> - response status <span class="li-normal">type: str</span>  <span class="li-normal">choices: [success, partial-success, client-err, oper-restrict, addr-err, addr-not-found, content-refused, msg-id-not-found, link-id-not-found, msg-fmt-corrupt, app-id-not-found, repl-app-id-not-found, srv-err, not-possible, msg-rejected, multiple-addr-not-supp, app-addr-not-supp, gen-service-err, improper-ident, unsupp-ver, unsupp-oper, validation-err, service-err, service-unavail, service-denied, app-denied]</span> </li>
 <li><span class="li-head">smil-part</span> - message encapsulation text <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">subject</span> - subject text string <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Replacement message table entries.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [add-smil, addr-type, allow-content-adaptation, charset, class, format, from, from-sender, header, image, message, msg-type, priority, rsp-status, smil-part, subject]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/SYSTEM/REPLACEMSG-GROUP/{REPLACEMSG-GROUP}/MM7
      fmgr_system_replacemsggroup_mm7:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            replacemsg-group: <value of string>
         params:
            -
               data:
                 -
                     add-smil: <value in [disable, enable]>
                     addr-type: <value in [rfc2822-addr, number, short-code]>
                     allow-content-adaptation: <value in [disable, enable]>
                     charset: <value in [us-ascii, utf-8]>
                     class: <value in [personal, advertisement, informational, ...]>
                     format: <value in [none, text, html, ...]>
                     from: <value of string>
                     from-sender: <value in [disable, enable]>
                     header: <value in [none, http, 8bit]>
                     image: <value of string>
                     message: <value of string>
                     msg-type: <value of string>
                     priority: <value in [low, normal, high, ...]>
                     rsp-status: <value in [success, partial-success, client-err, ...]>
                     smil-part: <value of string>
                     subject: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/SYSTEM/REPLACEMSG-GROUP/{REPLACEMSG-GROUP}/MM7
      fmgr_system_replacemsggroup_mm7:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            replacemsg-group: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [add-smil, addr-type, allow-content-adaptation, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/system/replacemsg-group/{replacemsg-group}/mm7</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> add-smil </span> - add message encapsulation <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> addr-type </span> - from address type <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> allow-content-adaptation </span> - allow content adaptations <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> charset </span> - character encoding used for replacement message <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> class </span> - message class <span class="li-normal">type: str</span>  </li>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/system/replacemsg-group/{replacemsg-group}/mm7</span>  </li>
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



