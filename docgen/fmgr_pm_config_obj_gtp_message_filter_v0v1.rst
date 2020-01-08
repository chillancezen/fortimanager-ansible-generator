:source: fmgr_pm_config_obj_gtp_message_filter_v0v1.py

:orphan:

.. _fmgr_pm_config_obj_gtp_message_filter_v0v1:

fmgr_pm_config_obj_gtp_message_filter_v0v1 -- Message filter for GTPv0/v1 messages.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/gtp/message-filter-v0v1`
- `/pm/config/global/obj/gtp/message-filter-v0v1`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Message filter for GTPv0/v1 messages.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">create-mbms</span> - GTPv1 create MBMS context (req 100, resp 101). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">create-pdp</span> - Create PDP context (req 16, resp 17). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">data-record</span> - Data record transfer (req 240, resp 241). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">delete-aa-pdp</span> - GTPv0 delete AA PDP context (req 24, resp 25). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">delete-mbms</span> - GTPv1 delete MBMS context (req 104, resp 105). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">delete-pdp</span> - Delete PDP context (req 20, resp 21). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">echo</span> - Echo (req 1, resp 2). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">end-marker</span> - GTPv1 End marker (254). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">error-indication</span> - Error indication (26). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">failure-report</span> - Failure report (req 34, resp 35). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">fwd-relocation</span> - GTPv1 forward relocation (req 53, resp 54, complete 55, complete ack 59). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">fwd-srns-context</span> - GTPv1 forward SRNS (context 58, context ack 60). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">gtp-pdu</span> - PDU (255). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">identification</span> - Identification (req 48, resp 49). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">mbms-de-registration</span> - GTPv1 MBMS de-registration (req 114, resp 115). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">mbms-notification</span> - GTPv1 MBMS notification (req 96, resp 97, reject req 98. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">mbms-registration</span> - GTPv1 MBMS registration (req 112, resp 113). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">mbms-session-start</span> - GTPv1 MBMS session start (req 116, resp 117). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">mbms-session-stop</span> - GTPv1 MBMS session stop (req 118, resp 119). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">mbms-session-update</span> - GTPv1 MBMS session update (req 120, resp 121). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">ms-info-change-notif</span> - GTPv1 MS info change notification (req 128, resp 129). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">name</span> - Message filter name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">node-alive</span> - Node alive (req 4, resp 5). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">note-ms-present</span> - Note MS GPRS present (req 36, resp 37). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">pdu-notification</span> - PDU notification (req 27, resp 28, reject req 29, reject resp 30). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">ran-info</span> - GTPv1 RAN information relay (70). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">redirection</span> - Redirection (req 6, resp 7). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">relocation-cancel</span> - GTPv1 relocation cancel (req 56, resp 57). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">send-route</span> - Send routing information for GPRS (req 32, resp 33). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">sgsn-context</span> - SGSN context (req 50, resp 51, ack 52). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">support-extension</span> - GTPv1 supported extension headers notify (31). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">unknown-message</span> - Allow or Deny unknown messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">unknown-message-white-list</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">update-mbms</span> - GTPv1 update MBMS context (req 102, resp 103). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">update-pdp</span> - Update PDP context (req 18, resp 19). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 <li><span class="li-head">v0-create-aa-pdp--v1-init-pdp-ctx</span> - GTPv0 create AA PDP context (req 22, resp 23); Or GTPv1 initiate PDP context (req 22, resp 23). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, allow]</span> </li>
 <li><span class="li-head">version-not-support</span> - Version not supported (3). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Message filter for GTPv0/v1 messages.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [create-mbms, create-pdp, data-record, delete-aa-pdp, delete-mbms, delete-pdp, echo, end-marker, error-indication, failure-report, fwd-relocation, fwd-srns-context, gtp-pdu, identification, mbms-de-registration, mbms-notification, mbms-registration, mbms-session-start, mbms-session-stop, mbms-session-update, ms-info-change-notif, name, node-alive, note-ms-present, pdu-notification, ran-info, redirection, relocation-cancel, send-route, sgsn-context, support-extension, unknown-message, unknown-message-white-list, update-mbms, update-pdp, v0-create-aa-pdp--v1-init-pdp-ctx, version-not-support]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/GTP/MESSAGE-FILTER-V0V1
      fmgr_pm_config_obj_gtp_message_filter_v0v1:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     create-mbms: <value in [allow, deny]>
                     create-pdp: <value in [allow, deny]>
                     data-record: <value in [allow, deny]>
                     delete-aa-pdp: <value in [allow, deny]>
                     delete-mbms: <value in [allow, deny]>
                     delete-pdp: <value in [allow, deny]>
                     echo: <value in [allow, deny]>
                     end-marker: <value in [allow, deny]>
                     error-indication: <value in [allow, deny]>
                     failure-report: <value in [allow, deny]>
                     fwd-relocation: <value in [allow, deny]>
                     fwd-srns-context: <value in [allow, deny]>
                     gtp-pdu: <value in [allow, deny]>
                     identification: <value in [allow, deny]>
                     mbms-de-registration: <value in [allow, deny]>
                     mbms-notification: <value in [allow, deny]>
                     mbms-registration: <value in [allow, deny]>
                     mbms-session-start: <value in [allow, deny]>
                     mbms-session-stop: <value in [allow, deny]>
                     mbms-session-update: <value in [allow, deny]>
                     ms-info-change-notif: <value in [allow, deny]>
                     name: <value of string>
                     node-alive: <value in [allow, deny]>
                     note-ms-present: <value in [allow, deny]>
                     pdu-notification: <value in [allow, deny]>
                     ran-info: <value in [allow, deny]>
                     redirection: <value in [allow, deny]>
                     relocation-cancel: <value in [allow, deny]>
                     send-route: <value in [allow, deny]>
                     sgsn-context: <value in [allow, deny]>
                     support-extension: <value in [allow, deny]>
                     unknown-message: <value in [allow, deny]>
                     unknown-message-white-list:
                       - <value of integer>
                     update-mbms: <value in [allow, deny]>
                     update-pdp: <value in [allow, deny]>
                     v0-create-aa-pdp--v1-init-pdp-ctx: <value in [deny, allow]>
                     version-not-support: <value in [allow, deny]>

    - name: REQUESTING /PM/CONFIG/OBJ/GTP/MESSAGE-FILTER-V0V1
      fmgr_pm_config_obj_gtp_message_filter_v0v1:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [create-mbms, create-pdp, data-record, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/gtp/message-filter-v0v1</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> create-mbms </span> - GTPv1 create MBMS context (req 100, resp 101). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> create-pdp </span> - Create PDP context (req 16, resp 17). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> data-record </span> - Data record transfer (req 240, resp 241). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> delete-aa-pdp </span> - GTPv0 delete AA PDP context (req 24, resp 25). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> delete-mbms </span> - GTPv1 delete MBMS context (req 104, resp 105). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> delete-pdp </span> - Delete PDP context (req 20, resp 21). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> echo </span> - Echo (req 1, resp 2). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> end-marker </span> - GTPv1 End marker (254). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> error-indication </span> - Error indication (26). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> failure-report </span> - Failure report (req 34, resp 35). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fwd-relocation </span> - GTPv1 forward relocation (req 53, resp 54, complete 55, complete ack 59). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fwd-srns-context </span> - GTPv1 forward SRNS (context 58, context ack 60). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> gtp-pdu </span> - PDU (255). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> identification </span> - Identification (req 48, resp 49). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mbms-de-registration </span> - GTPv1 MBMS de-registration (req 114, resp 115). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mbms-notification </span> - GTPv1 MBMS notification (req 96, resp 97, reject req 98. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mbms-registration </span> - GTPv1 MBMS registration (req 112, resp 113). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mbms-session-start </span> - GTPv1 MBMS session start (req 116, resp 117). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mbms-session-stop </span> - GTPv1 MBMS session stop (req 118, resp 119). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mbms-session-update </span> - GTPv1 MBMS session update (req 120, resp 121). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ms-info-change-notif </span> - GTPv1 MS info change notification (req 128, resp 129). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Message filter name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> node-alive </span> - Node alive (req 4, resp 5). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> note-ms-present </span> - Note MS GPRS present (req 36, resp 37). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pdu-notification </span> - PDU notification (req 27, resp 28, reject req 29, reject resp 30). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ran-info </span> - GTPv1 RAN information relay (70). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> redirection </span> - Redirection (req 6, resp 7). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> relocation-cancel </span> - GTPv1 relocation cancel (req 56, resp 57). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> send-route </span> - Send routing information for GPRS (req 32, resp 33). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sgsn-context </span> - SGSN context (req 50, resp 51, ack 52). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> support-extension </span> - GTPv1 supported extension headers notify (31). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> unknown-message </span> - Allow or Deny unknown messages. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> unknown-message-white-list </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> update-mbms </span> - GTPv1 update MBMS context (req 102, resp 103). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> update-pdp </span> - Update PDP context (req 18, resp 19). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> v0-create-aa-pdp--v1-init-pdp-ctx </span> - GTPv0 create AA PDP context (req 22, resp 23); Or GTPv1 initiate PDP context (req 22, resp 23). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> version-not-support </span> - Version not supported (3). <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/gtp/message-filter-v0v1</span>  </li>
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



