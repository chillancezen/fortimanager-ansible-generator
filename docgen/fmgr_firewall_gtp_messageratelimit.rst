:source: fmgr_firewall_gtp_messageratelimit.py

:orphan:

.. _fmgr_firewall_gtp_messageratelimit:

fmgr_firewall_gtp_messageratelimit -- Message rate limiting.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/gtp/{gtp}/message-rate-limit`
- `/pm/config/global/obj/firewall/gtp/{gtp}/message-rate-limit`
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
 <li><span class="li-head">gtp</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Message rate limiting.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Message rate limiting.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">create-aa-pdp-request</span> - Rate limit for create AA PDP context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">create-aa-pdp-response</span> - Rate limit for create AA PDP context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">create-mbms-request</span> - Rate limit for create MBMS context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">create-mbms-response</span> - Rate limit for create MBMS context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">create-pdp-request</span> - Rate limit for create PDP context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">create-pdp-response</span> - Rate limit for create PDP context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-aa-pdp-request</span> - Rate limit for delete AA PDP context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-aa-pdp-response</span> - Rate limit for delete AA PDP context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-mbms-request</span> - Rate limit for delete MBMS context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-mbms-response</span> - Rate limit for delete MBMS context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-pdp-request</span> - Rate limit for delete PDP context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">delete-pdp-response</span> - Rate limit for delete PDP context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">echo-reponse</span> - Rate limit for echo response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">echo-request</span> - Rate limit for echo requests (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">error-indication</span> - Rate limit for error indication (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">failure-report-request</span> - Rate limit for failure report request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">failure-report-response</span> - Rate limit for failure report response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fwd-reloc-complete-ack</span> - Rate limit for forward relocation complete acknowledge (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fwd-relocation-complete</span> - Rate limit for forward relocation complete (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fwd-relocation-request</span> - Rate limit for forward relocation request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fwd-relocation-response</span> - Rate limit for forward relocation response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fwd-srns-context</span> - Rate limit for forward SRNS context (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fwd-srns-context-ack</span> - Rate limit for forward SRNS context acknowledge (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">g-pdu</span> - Rate limit for G-PDU (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">identification-request</span> - Rate limit for identification request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">identification-response</span> - Rate limit for identification response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-de-reg-request</span> - Rate limit for MBMS de-registration request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-de-reg-response</span> - Rate limit for MBMS de-registration response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-notify-rej-request</span> - Rate limit for MBMS notification reject request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-notify-rej-response</span> - Rate limit for MBMS notification reject response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-notify-request</span> - Rate limit for MBMS notification request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-notify-response</span> - Rate limit for MBMS notification response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-reg-request</span> - Rate limit for MBMS registration request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-reg-response</span> - Rate limit for MBMS registration response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-ses-start-request</span> - Rate limit for MBMS session start request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-ses-start-response</span> - Rate limit for MBMS session start response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-ses-stop-request</span> - Rate limit for MBMS session stop request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mbms-ses-stop-response</span> - Rate limit for MBMS session stop response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">note-ms-request</span> - Rate limit for note MS GPRS present request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">note-ms-response</span> - Rate limit for note MS GPRS present response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pdu-notify-rej-request</span> - Rate limit for PDU notify reject request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pdu-notify-rej-response</span> - Rate limit for PDU notify reject response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pdu-notify-request</span> - Rate limit for PDU notify request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pdu-notify-response</span> - Rate limit for PDU notify response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ran-info</span> - Rate limit for RAN information relay (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">relocation-cancel-request</span> - Rate limit for relocation cancel request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">relocation-cancel-response</span> - Rate limit for relocation cancel response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">send-route-request</span> - Rate limit for send routing information for GPRS request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">send-route-response</span> - Rate limit for send routing information for GPRS response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sgsn-context-ack</span> - Rate limit for SGSN context acknowledgement (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sgsn-context-request</span> - Rate limit for SGSN context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sgsn-context-response</span> - Rate limit for SGSN context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">support-ext-hdr-notify</span> - Rate limit for support extension headers notification (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">update-mbms-request</span> - Rate limit for update MBMS context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">update-mbms-response</span> - Rate limit for update MBMS context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">update-pdp-request</span> - Rate limit for update PDP context request (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">update-pdp-response</span> - Rate limit for update PDP context response (packets per second). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">version-not-support</span> - Rate limit for version not supported (packets per second). <span class="li-normal">type: int</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/GTP/{GTP}/MESSAGE-RATE-LIMIT
      fmgr_firewall_gtp_messageratelimit:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            gtp: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/GTP/{GTP}/MESSAGE-RATE-LIMIT
      fmgr_firewall_gtp_messageratelimit:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            gtp: <value of string>
         params:
            -
               data:
                  create-aa-pdp-request: <value of integer>
                  create-aa-pdp-response: <value of integer>
                  create-mbms-request: <value of integer>
                  create-mbms-response: <value of integer>
                  create-pdp-request: <value of integer>
                  create-pdp-response: <value of integer>
                  delete-aa-pdp-request: <value of integer>
                  delete-aa-pdp-response: <value of integer>
                  delete-mbms-request: <value of integer>
                  delete-mbms-response: <value of integer>
                  delete-pdp-request: <value of integer>
                  delete-pdp-response: <value of integer>
                  echo-reponse: <value of integer>
                  echo-request: <value of integer>
                  error-indication: <value of integer>
                  failure-report-request: <value of integer>
                  failure-report-response: <value of integer>
                  fwd-reloc-complete-ack: <value of integer>
                  fwd-relocation-complete: <value of integer>
                  fwd-relocation-request: <value of integer>
                  fwd-relocation-response: <value of integer>
                  fwd-srns-context: <value of integer>
                  fwd-srns-context-ack: <value of integer>
                  g-pdu: <value of integer>
                  identification-request: <value of integer>
                  identification-response: <value of integer>
                  mbms-de-reg-request: <value of integer>
                  mbms-de-reg-response: <value of integer>
                  mbms-notify-rej-request: <value of integer>
                  mbms-notify-rej-response: <value of integer>
                  mbms-notify-request: <value of integer>
                  mbms-notify-response: <value of integer>
                  mbms-reg-request: <value of integer>
                  mbms-reg-response: <value of integer>
                  mbms-ses-start-request: <value of integer>
                  mbms-ses-start-response: <value of integer>
                  mbms-ses-stop-request: <value of integer>
                  mbms-ses-stop-response: <value of integer>
                  note-ms-request: <value of integer>
                  note-ms-response: <value of integer>
                  pdu-notify-rej-request: <value of integer>
                  pdu-notify-rej-response: <value of integer>
                  pdu-notify-request: <value of integer>
                  pdu-notify-response: <value of integer>
                  ran-info: <value of integer>
                  relocation-cancel-request: <value of integer>
                  relocation-cancel-response: <value of integer>
                  send-route-request: <value of integer>
                  send-route-response: <value of integer>
                  sgsn-context-ack: <value of integer>
                  sgsn-context-request: <value of integer>
                  sgsn-context-response: <value of integer>
                  support-ext-hdr-notify: <value of integer>
                  update-mbms-request: <value of integer>
                  update-mbms-response: <value of integer>
                  update-pdp-request: <value of integer>
                  update-pdp-response: <value of integer>
                  version-not-support: <value of integer>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> create-aa-pdp-request </span> - Rate limit for create AA PDP context request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> create-aa-pdp-response </span> - Rate limit for create AA PDP context response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> create-mbms-request </span> - Rate limit for create MBMS context request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> create-mbms-response </span> - Rate limit for create MBMS context response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> create-pdp-request </span> - Rate limit for create PDP context request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> create-pdp-response </span> - Rate limit for create PDP context response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> delete-aa-pdp-request </span> - Rate limit for delete AA PDP context request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> delete-aa-pdp-response </span> - Rate limit for delete AA PDP context response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> delete-mbms-request </span> - Rate limit for delete MBMS context request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> delete-mbms-response </span> - Rate limit for delete MBMS context response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> delete-pdp-request </span> - Rate limit for delete PDP context request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> delete-pdp-response </span> - Rate limit for delete PDP context response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> echo-reponse </span> - Rate limit for echo response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> echo-request </span> - Rate limit for echo requests (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> error-indication </span> - Rate limit for error indication (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> failure-report-request </span> - Rate limit for failure report request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> failure-report-response </span> - Rate limit for failure report response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> fwd-reloc-complete-ack </span> - Rate limit for forward relocation complete acknowledge (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> fwd-relocation-complete </span> - Rate limit for forward relocation complete (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> fwd-relocation-request </span> - Rate limit for forward relocation request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> fwd-relocation-response </span> - Rate limit for forward relocation response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> fwd-srns-context </span> - Rate limit for forward SRNS context (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> fwd-srns-context-ack </span> - Rate limit for forward SRNS context acknowledge (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> g-pdu </span> - Rate limit for G-PDU (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> identification-request </span> - Rate limit for identification request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> identification-response </span> - Rate limit for identification response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mbms-de-reg-request </span> - Rate limit for MBMS de-registration request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mbms-de-reg-response </span> - Rate limit for MBMS de-registration response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mbms-notify-rej-request </span> - Rate limit for MBMS notification reject request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mbms-notify-rej-response </span> - Rate limit for MBMS notification reject response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mbms-notify-request </span> - Rate limit for MBMS notification request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mbms-notify-response </span> - Rate limit for MBMS notification response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mbms-reg-request </span> - Rate limit for MBMS registration request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mbms-reg-response </span> - Rate limit for MBMS registration response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mbms-ses-start-request </span> - Rate limit for MBMS session start request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mbms-ses-start-response </span> - Rate limit for MBMS session start response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mbms-ses-stop-request </span> - Rate limit for MBMS session stop request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mbms-ses-stop-response </span> - Rate limit for MBMS session stop response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> note-ms-request </span> - Rate limit for note MS GPRS present request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> note-ms-response </span> - Rate limit for note MS GPRS present response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> pdu-notify-rej-request </span> - Rate limit for PDU notify reject request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> pdu-notify-rej-response </span> - Rate limit for PDU notify reject response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> pdu-notify-request </span> - Rate limit for PDU notify request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> pdu-notify-response </span> - Rate limit for PDU notify response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ran-info </span> - Rate limit for RAN information relay (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> relocation-cancel-request </span> - Rate limit for relocation cancel request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> relocation-cancel-response </span> - Rate limit for relocation cancel response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> send-route-request </span> - Rate limit for send routing information for GPRS request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> send-route-response </span> - Rate limit for send routing information for GPRS response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> sgsn-context-ack </span> - Rate limit for SGSN context acknowledgement (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> sgsn-context-request </span> - Rate limit for SGSN context request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> sgsn-context-response </span> - Rate limit for SGSN context response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> support-ext-hdr-notify </span> - Rate limit for support extension headers notification (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> update-mbms-request </span> - Rate limit for update MBMS context request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> update-mbms-response </span> - Rate limit for update MBMS context response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> update-pdp-request </span> - Rate limit for update PDP context request (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> update-pdp-response </span> - Rate limit for update PDP context response (packets per second). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> version-not-support </span> - Rate limit for version not supported (packets per second). <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/gtp/{gtp}/message-rate-limit</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/gtp/{gtp}/message-rate-limit</span>  </li>
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



