:source: fmgr_pm_config_obj_system_replacemsg_group_replacemsg_group_custom_message_custom_message.py

:orphan:

.. _fmgr_pm_config_obj_system_replacemsg_group_replacemsg_group_custom_message_custom_message:

fmgr_pm_config_obj_system_replacemsg_group_replacemsg_group_custom_message_custom_message -- Replacement message table entries.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/system/replacemsg-group/{replacemsg-group}/custom-message/{custom-message}`
- `/pm/config/global/obj/system/replacemsg-group/{replacemsg-group}/custom-message/{custom-message}`
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
 <li><span class="li-head">custom-message</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Replacement message table entries.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">buffer</span> - Message string. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">format</span> - Format flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, text, html, wml]</span> </li>
 <li><span class="li-head">header</span> - Header flag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http, 8bit]</span> </li>
 <li><span class="li-head">msg-type</span> - Message type. <span class="li-normal">type: str</span> </li>
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
    - name: send request to /pm/config/obj/system/replacemsg-group/{replacemsg-group}/custom-message/{custom-message}
      fmgr_pm_config_obj_system_replacemsg_group_replacemsg_group_custom_message_custom_message:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            replacemsg-group: <value of string>
            custom-message: <value of string>
         params:
            - 
               data: 
                  buffer: <value of string>
                  format: <value in [none, text, html, ...]>
                  header: <value in [none, http, 8bit]>
                  msg-type: <value of string>
    - name: send request to /pm/config/obj/system/replacemsg-group/{replacemsg-group}/custom-message/{custom-message}
      fmgr_pm_config_obj_system_replacemsg_group_replacemsg_group_custom_message_custom_message:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            replacemsg-group: <value of string>
            custom-message: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/system/replacemsg-group/{replacemsg-group}/custom-message/{custom-message}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> buffer </span> - Message string. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> format </span> - Format flag. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> header </span> - Header flag. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> msg-type </span> - Message type. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/system/replacemsg-group/{replacemsg-group}/custom-message/{custom-message}</span>  </li>
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



