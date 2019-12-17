:source: fmgr_pm_config_obj_gtp_message_filter_v2.py

:orphan:

.. _fmgr_pm_config_obj_gtp_message_filter_v2:

fmgr_pm_config_obj_gtp_message_filter_v2 -- Message filter for GTPv2 messages.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/gtp/message-filter-v2`
- `/pm/config/global/obj/gtp/message-filter-v2`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Message filter for GTPv2 messages.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">bearer-resource-cmd-fail</span> - Bearer resource (command 68, failure indication 69). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">change-notification</span> - Change notification (req 38, resp 39). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">create-bearer</span> - Create bearer (req 95, resp 96). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">create-session</span> - Create session (req 32, resp 33). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">delete-bearer-cmd-fail</span> - Delete bearer (command 66, failure indication 67). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">delete-bearer-req-resp</span> - Delete bearer (req 99, resp 100). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">delete-pdn-connection-set</span> - Delete PDN connection set (req 101, resp 102). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">delete-session</span> - Delete session (req 36, resp 37). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">echo</span> - Echo (req 1, resp 2). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">modify-bearer-cmd-fail</span> - Modify bearer (command 64 , failure indication 65). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">modify-bearer-req-resp</span> - Modify bearer (req 34, resp 35). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">name</span> - Message filter name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">resume</span> - Resume (notify 164 , ack 165). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">suspend</span> - Suspend (notify 162, ack 163). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">trace-session</span> - Trace session (activation 71, deactivation 72). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">unknown-message</span> - Allow or Deny unknown messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">unknown-message-white-list</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">update-bearer</span> - Update bearer (req 97, resp 98). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">update-pdn-connection-set</span> - Update PDN connection set (req 200, resp 201). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">version-not-support</span> - Version not supported (3). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Message filter for GTPv2 messages.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bearer-resource-cmd-fail, change-notification, create-bearer, create-session, delete-bearer-cmd-fail, delete-bearer-req-resp, delete-pdn-connection-set, delete-session, echo, modify-bearer-cmd-fail, modify-bearer-req-resp, name, resume, suspend, trace-session, unknown-message, unknown-message-white-list, update-bearer, update-pdn-connection-set, version-not-support]</span> </li>
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
    - name: send request to /pm/config/obj/gtp/message-filter-v2
      fmgr_pm_config_obj_gtp_message_filter_v2:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            - 
               data: 
                - 
                     bearer-resource-cmd-fail: <value in [allow, deny]>
                     change-notification: <value in [allow, deny]>
                     create-bearer: <value in [allow, deny]>
                     create-session: <value in [allow, deny]>
                     delete-bearer-cmd-fail: <value in [allow, deny]>
                     delete-bearer-req-resp: <value in [allow, deny]>
                     delete-pdn-connection-set: <value in [allow, deny]>
                     delete-session: <value in [allow, deny]>
                     echo: <value in [allow, deny]>
                     modify-bearer-cmd-fail: <value in [allow, deny]>
                     modify-bearer-req-resp: <value in [allow, deny]>
                     name: <value of string>
                     resume: <value in [allow, deny]>
                     suspend: <value in [allow, deny]>
                     trace-session: <value in [allow, deny]>
                     unknown-message: <value in [allow, deny]>
                     unknown-message-white-list: 
                      - <value of integer>
                     update-bearer: <value in [allow, deny]>
                     update-pdn-connection-set: <value in [allow, deny]>
                     version-not-support: <value in [allow, deny]>
    - name: send request to /pm/config/obj/gtp/message-filter-v2
      fmgr_pm_config_obj_gtp_message_filter_v2:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            - 
               attr: <value of string>
               fields: 
                - 
                   - <value in [bearer-resource-cmd-fail, change-notification, create-bearer, ...]>
               filter: 
                - <value of string>
               get used: <value of integer>
               loadsub: <value of integer>
               option: <value in [count, object member, datasrc, ...]>
               range: 
                - <value of integer>
               sortings: 
                - 
                     \{attr_name\}: <value in [1, -1]>



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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/gtp/message-filter-v2</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> bearer-resource-cmd-fail </span> - Bearer resource (command 68, failure indication 69). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> change-notification </span> - Change notification (req 38, resp 39). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> create-bearer </span> - Create bearer (req 95, resp 96). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> create-session </span> - Create session (req 32, resp 33). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> delete-bearer-cmd-fail </span> - Delete bearer (command 66, failure indication 67). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> delete-bearer-req-resp </span> - Delete bearer (req 99, resp 100). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> delete-pdn-connection-set </span> - Delete PDN connection set (req 101, resp 102). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> delete-session </span> - Delete session (req 36, resp 37). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> echo </span> - Echo (req 1, resp 2). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> modify-bearer-cmd-fail </span> - Modify bearer (command 64 , failure indication 65). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> modify-bearer-req-resp </span> - Modify bearer (req 34, resp 35). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Message filter name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> resume </span> - Resume (notify 164 , ack 165). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> suspend </span> - Suspend (notify 162, ack 163). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> trace-session </span> - Trace session (activation 71, deactivation 72). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> unknown-message </span> - Allow or Deny unknown messages. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> unknown-message-white-list </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> update-bearer </span> - Update bearer (req 97, resp 98). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> update-pdn-connection-set </span> - Update PDN connection set (req 200, resp 201). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> version-not-support </span> - Version not supported (3). <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/gtp/message-filter-v2</span>  </li>
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



