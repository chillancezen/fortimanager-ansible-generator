:source: fmgr_pm_config_obj_voip_profile_profile_sip.py

:orphan:

.. _fmgr_pm_config_obj_voip_profile_profile_sip:

fmgr_pm_config_obj_voip_profile_profile_sip -- SIP.
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/voip/profile/{profile}/sip`
- `/pm/config/global/obj/voip/profile/{profile}/sip`
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
 <li><span class="li-head">parameters for method: [get]</span> - SIP.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - SIP.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">ack-rate</span> - ACK request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">block-ack</span> - Enable/disable block ACK requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-bye</span> - Enable/disable block BYE requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-cancel</span> - Enable/disable block CANCEL requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-geo-red-options</span> - Enable/disable block OPTIONS requests, but OPTIONS requests still notify for redundancy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-info</span> - Enable/disable block INFO requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-invite</span> - Enable/disable block INVITE requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-long-lines</span> - Enable/disable block requests with headers exceeding max-line-length. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-message</span> - Enable/disable block MESSAGE requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-notify</span> - Enable/disable block NOTIFY requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-options</span> - Enable/disable block OPTIONS requests and no OPTIONS as notifying message for redundancy either. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-prack</span> - Enable/disable block prack requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-publish</span> - Enable/disable block PUBLISH requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-refer</span> - Enable/disable block REFER requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-register</span> - Enable/disable block REGISTER requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-subscribe</span> - Enable/disable block SUBSCRIBE requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-unknown</span> - Block unrecognized SIP requests (enabled by default). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">block-update</span> - Enable/disable block UPDATE requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">bye-rate</span> - BYE request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">call-keepalive</span> - Continue tracking calls with no RTP for this many minutes. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">cancel-rate</span> - CANCEL request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">contact-fixup</span> - Fixup contact anyway even if contact's IP:port doesn't match session's IP:port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">hnt-restrict-source-ip</span> - Enable/disable restrict RTP source IP to be the same as SIP source IP when HNT is enabled. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">hosted-nat-traversal</span> - Hosted NAT Traversal (HNT). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">info-rate</span> - INFO request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">invite-rate</span> - INVITE request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ips-rtp</span> - Enable/disable allow IPS on RTP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">log-call-summary</span> - Enable/disable logging of SIP call summary. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">log-violations</span> - Enable/disable logging of SIP violations. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">malformed-header-allow</span> - Action for malformed Allow header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-call-id</span> - Action for malformed Call-ID header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-contact</span> - Action for malformed Contact header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-content-length</span> - Action for malformed Content-Length header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-content-type</span> - Action for malformed Content-Type header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-cseq</span> - Action for malformed CSeq header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-expires</span> - Action for malformed Expires header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-from</span> - Action for malformed From header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-max-forwards</span> - Action for malformed Max-Forwards header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-p-asserted-identity</span> - Action for malformed P-Asserted-Identity header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-rack</span> - Action for malformed RAck header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-record-route</span> - Action for malformed Record-Route header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-route</span> - Action for malformed Route header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-rseq</span> - Action for malformed RSeq header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-a</span> - Action for malformed SDP a line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-b</span> - Action for malformed SDP b line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-c</span> - Action for malformed SDP c line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-i</span> - Action for malformed SDP i line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-k</span> - Action for malformed SDP k line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-m</span> - Action for malformed SDP m line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-o</span> - Action for malformed SDP o line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-r</span> - Action for malformed SDP r line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-s</span> - Action for malformed SDP s line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-t</span> - Action for malformed SDP t line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-v</span> - Action for malformed SDP v line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-sdp-z</span> - Action for malformed SDP z line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-to</span> - Action for malformed To header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-header-via</span> - Action for malformed VIA header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">malformed-request-line</span> - Action for malformed request line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">max-body-length</span> - Maximum SIP message body length (0 meaning no limit). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-dialogs</span> - Maximum number of concurrent calls/dialogs (per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-idle-dialogs</span> - Maximum number established but idle dialogs to retain (per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-line-length</span> - Maximum SIP header line length (78-4096). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">message-rate</span> - MESSAGE request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">nat-trace</span> - Enable/disable preservation of original IP in SDP i line. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">no-sdp-fixup</span> - Enable/disable no SDP fix-up. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">notify-rate</span> - NOTIFY request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">open-contact-pinhole</span> - Enable/disable open pinhole for non-REGISTER Contact port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">open-record-route-pinhole</span> - Enable/disable open pinhole for Record-Route port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">open-register-pinhole</span> - Enable/disable open pinhole for REGISTER Contact port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">open-via-pinhole</span> - Enable/disable open pinhole for Via port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">options-rate</span> - OPTIONS request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">prack-rate</span> - PRACK request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">preserve-override</span> - Override i line to preserve original IPS (default: append). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">provisional-invite-expiry-time</span> - Expiry time for provisional INVITE (10 - 3600 sec). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">publish-rate</span> - PUBLISH request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">refer-rate</span> - REFER request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">register-contact-trace</span> - Enable/disable trace original IP/port within the contact header of REGISTER requests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">register-rate</span> - REGISTER request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rfc2543-branch</span> - Enable/disable support via branch compliant with RFC 2543. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">rtp</span> - Enable/disable create pinholes for RTP traffic to traverse firewall. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-algorithm</span> - Relative strength of encryption algorithms accepted in negotiation. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [high, medium, low]</span> </li>
 <li><span class="li-head">ssl-auth-client</span> - Require a client certificate and authenticate it with the peer/peergrp. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-auth-server</span> - Authenticate the server's certificate with the peer/peergrp. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-client-certificate</span> - Name of Certificate to offer to server if requested. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-client-renegotiation</span> - Allow/block client renegotiation by server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [allow, deny, secure]</span> </li>
 <li><span class="li-head">ssl-max-version</span> - Highest SSL/TLS version to negotiate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2]</span> </li>
 <li><span class="li-head">ssl-min-version</span> - Lowest SSL/TLS version to negotiate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2]</span> </li>
 <li><span class="li-head">ssl-mode</span> - SSL/TLS mode for encryption & decryption of traffic. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [off, full]</span> </li>
 <li><span class="li-head">ssl-pfs</span> - SSL Perfect Forward Secrecy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [require, deny, allow]</span> </li>
 <li><span class="li-head">ssl-send-empty-frags</span> - Send empty fragments to avoid attack on CBC IV (SSL 3. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-server-certificate</span> - Name of Certificate return to the client in every SSL connection. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable SIP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">strict-register</span> - Enable/disable only allow the registrar to connect. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">subscribe-rate</span> - SUBSCRIBE request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">unknown-header</span> - Action for unknown SIP header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pass, discard, respond]</span> </li>
 <li><span class="li-head">update-rate</span> - UPDATE request rate limit (per second, per policy). <span class="li-normal">type: int</span> </li>
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
    - name: send request to /pm/config/obj/voip/profile/{profile}/sip
      fmgr_pm_config_obj_voip_profile_profile_sip:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            - 
               option: <value in [object member, chksum, datasrc]>
    - name: send request to /pm/config/obj/voip/profile/{profile}/sip
      fmgr_pm_config_obj_voip_profile_profile_sip:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            - 
               data: 
                  ack-rate: <value of integer>
                  block-ack: <value in [disable, enable]>
                  block-bye: <value in [disable, enable]>
                  block-cancel: <value in [disable, enable]>
                  block-geo-red-options: <value in [disable, enable]>
                  block-info: <value in [disable, enable]>
                  block-invite: <value in [disable, enable]>
                  block-long-lines: <value in [disable, enable]>
                  block-message: <value in [disable, enable]>
                  block-notify: <value in [disable, enable]>
                  block-options: <value in [disable, enable]>
                  block-prack: <value in [disable, enable]>
                  block-publish: <value in [disable, enable]>
                  block-refer: <value in [disable, enable]>
                  block-register: <value in [disable, enable]>
                  block-subscribe: <value in [disable, enable]>
                  block-unknown: <value in [disable, enable]>
                  block-update: <value in [disable, enable]>
                  bye-rate: <value of integer>
                  call-keepalive: <value of integer>
                  cancel-rate: <value of integer>
                  contact-fixup: <value in [disable, enable]>
                  hnt-restrict-source-ip: <value in [disable, enable]>
                  hosted-nat-traversal: <value in [disable, enable]>
                  info-rate: <value of integer>
                  invite-rate: <value of integer>
                  ips-rtp: <value in [disable, enable]>
                  log-call-summary: <value in [disable, enable]>
                  log-violations: <value in [disable, enable]>
                  malformed-header-allow: <value in [pass, discard, respond]>
                  malformed-header-call-id: <value in [pass, discard, respond]>
                  malformed-header-contact: <value in [pass, discard, respond]>
                  malformed-header-content-length: <value in [pass, discard, respond]>
                  malformed-header-content-type: <value in [pass, discard, respond]>
                  malformed-header-cseq: <value in [pass, discard, respond]>
                  malformed-header-expires: <value in [pass, discard, respond]>
                  malformed-header-from: <value in [pass, discard, respond]>
                  malformed-header-max-forwards: <value in [pass, discard, respond]>
                  malformed-header-p-asserted-identity: <value in [pass, discard, respond]>
                  malformed-header-rack: <value in [pass, discard, respond]>
                  malformed-header-record-route: <value in [pass, discard, respond]>
                  malformed-header-route: <value in [pass, discard, respond]>
                  malformed-header-rseq: <value in [pass, discard, respond]>
                  malformed-header-sdp-a: <value in [pass, discard, respond]>
                  malformed-header-sdp-b: <value in [pass, discard, respond]>
                  malformed-header-sdp-c: <value in [pass, discard, respond]>
                  malformed-header-sdp-i: <value in [pass, discard, respond]>
                  malformed-header-sdp-k: <value in [pass, discard, respond]>
                  malformed-header-sdp-m: <value in [pass, discard, respond]>
                  malformed-header-sdp-o: <value in [pass, discard, respond]>
                  malformed-header-sdp-r: <value in [pass, discard, respond]>
                  malformed-header-sdp-s: <value in [pass, discard, respond]>
                  malformed-header-sdp-t: <value in [pass, discard, respond]>
                  malformed-header-sdp-v: <value in [pass, discard, respond]>
                  malformed-header-sdp-z: <value in [pass, discard, respond]>
                  malformed-header-to: <value in [pass, discard, respond]>
                  malformed-header-via: <value in [pass, discard, respond]>
                  malformed-request-line: <value in [pass, discard, respond]>
                  max-body-length: <value of integer>
                  max-dialogs: <value of integer>
                  max-idle-dialogs: <value of integer>
                  max-line-length: <value of integer>
                  message-rate: <value of integer>
                  nat-trace: <value in [disable, enable]>
                  no-sdp-fixup: <value in [disable, enable]>
                  notify-rate: <value of integer>
                  open-contact-pinhole: <value in [disable, enable]>
                  open-record-route-pinhole: <value in [disable, enable]>
                  open-register-pinhole: <value in [disable, enable]>
                  open-via-pinhole: <value in [disable, enable]>
                  options-rate: <value of integer>
                  prack-rate: <value of integer>
                  preserve-override: <value in [disable, enable]>
                  provisional-invite-expiry-time: <value of integer>
                  publish-rate: <value of integer>
                  refer-rate: <value of integer>
                  register-contact-trace: <value in [disable, enable]>
                  register-rate: <value of integer>
                  rfc2543-branch: <value in [disable, enable]>
                  rtp: <value in [disable, enable]>
                  ssl-algorithm: <value in [high, medium, low]>
                  ssl-auth-client: <value of string>
                  ssl-auth-server: <value of string>
                  ssl-client-certificate: <value of string>
                  ssl-client-renegotiation: <value in [allow, deny, secure]>
                  ssl-max-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
                  ssl-min-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
                  ssl-mode: <value in [off, full]>
                  ssl-pfs: <value in [require, deny, allow]>
                  ssl-send-empty-frags: <value in [disable, enable]>
                  ssl-server-certificate: <value of string>
                  status: <value in [disable, enable]>
                  strict-register: <value in [disable, enable]>
                  subscribe-rate: <value of integer>
                  unknown-header: <value in [pass, discard, respond]>
                  update-rate: <value of integer>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> ack-rate </span> - ACK request rate limit (per second, per policy). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> block-ack </span> - Enable/disable block ACK requests. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-bye </span> - Enable/disable block BYE requests. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-cancel </span> - Enable/disable block CANCEL requests. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-geo-red-options </span> - Enable/disable block OPTIONS requests, but OPTIONS requests still notify for redundancy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-info </span> - Enable/disable block INFO requests. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-invite </span> - Enable/disable block INVITE requests. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-long-lines </span> - Enable/disable block requests with headers exceeding max-line-length. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-message </span> - Enable/disable block MESSAGE requests. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-notify </span> - Enable/disable block NOTIFY requests. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-options </span> - Enable/disable block OPTIONS requests and no OPTIONS as notifying message for redundancy either. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-prack </span> - Enable/disable block prack requests. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-publish </span> - Enable/disable block PUBLISH requests. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-refer </span> - Enable/disable block REFER requests. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-register </span> - Enable/disable block REGISTER requests. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-subscribe </span> - Enable/disable block SUBSCRIBE requests. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-unknown </span> - Block unrecognized SIP requests (enabled by default). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-update </span> - Enable/disable block UPDATE requests. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> bye-rate </span> - BYE request rate limit (per second, per policy). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> call-keepalive </span> - Continue tracking calls with no RTP for this many minutes. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> cancel-rate </span> - CANCEL request rate limit (per second, per policy). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> contact-fixup </span> - Fixup contact anyway even if contact's IP:port doesn't match session's IP:port. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> hnt-restrict-source-ip </span> - Enable/disable restrict RTP source IP to be the same as SIP source IP when HNT is enabled. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> hosted-nat-traversal </span> - Hosted NAT Traversal (HNT). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> info-rate </span> - INFO request rate limit (per second, per policy). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> invite-rate </span> - INVITE request rate limit (per second, per policy). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ips-rtp </span> - Enable/disable allow IPS on RTP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log-call-summary </span> - Enable/disable logging of SIP call summary. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log-violations </span> - Enable/disable logging of SIP violations. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-allow </span> - Action for malformed Allow header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-call-id </span> - Action for malformed Call-ID header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-contact </span> - Action for malformed Contact header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-content-length </span> - Action for malformed Content-Length header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-content-type </span> - Action for malformed Content-Type header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-cseq </span> - Action for malformed CSeq header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-expires </span> - Action for malformed Expires header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-from </span> - Action for malformed From header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-max-forwards </span> - Action for malformed Max-Forwards header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-p-asserted-identity </span> - Action for malformed P-Asserted-Identity header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-rack </span> - Action for malformed RAck header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-record-route </span> - Action for malformed Record-Route header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-route </span> - Action for malformed Route header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-rseq </span> - Action for malformed RSeq header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-sdp-a </span> - Action for malformed SDP a line. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-sdp-b </span> - Action for malformed SDP b line. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-sdp-c </span> - Action for malformed SDP c line. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-sdp-i </span> - Action for malformed SDP i line. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-sdp-k </span> - Action for malformed SDP k line. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-sdp-m </span> - Action for malformed SDP m line. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-sdp-o </span> - Action for malformed SDP o line. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-sdp-r </span> - Action for malformed SDP r line. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-sdp-s </span> - Action for malformed SDP s line. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-sdp-t </span> - Action for malformed SDP t line. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-sdp-v </span> - Action for malformed SDP v line. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-sdp-z </span> - Action for malformed SDP z line. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-to </span> - Action for malformed To header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-header-via </span> - Action for malformed VIA header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> malformed-request-line </span> - Action for malformed request line. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-body-length </span> - Maximum SIP message body length (0 meaning no limit). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> max-dialogs </span> - Maximum number of concurrent calls/dialogs (per policy). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> max-idle-dialogs </span> - Maximum number established but idle dialogs to retain (per policy). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> max-line-length </span> - Maximum SIP header line length (78-4096). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message-rate </span> - MESSAGE request rate limit (per second, per policy). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> nat-trace </span> - Enable/disable preservation of original IP in SDP i line. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> no-sdp-fixup </span> - Enable/disable no SDP fix-up. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> notify-rate </span> - NOTIFY request rate limit (per second, per policy). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> open-contact-pinhole </span> - Enable/disable open pinhole for non-REGISTER Contact port. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> open-record-route-pinhole </span> - Enable/disable open pinhole for Record-Route port. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> open-register-pinhole </span> - Enable/disable open pinhole for REGISTER Contact port. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> open-via-pinhole </span> - Enable/disable open pinhole for Via port. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> options-rate </span> - OPTIONS request rate limit (per second, per policy). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> prack-rate </span> - PRACK request rate limit (per second, per policy). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> preserve-override </span> - Override i line to preserve original IPS (default: append). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> provisional-invite-expiry-time </span> - Expiry time for provisional INVITE (10 - 3600 sec). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> publish-rate </span> - PUBLISH request rate limit (per second, per policy). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> refer-rate </span> - REFER request rate limit (per second, per policy). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> register-contact-trace </span> - Enable/disable trace original IP/port within the contact header of REGISTER requests. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> register-rate </span> - REGISTER request rate limit (per second, per policy). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> rfc2543-branch </span> - Enable/disable support via branch compliant with RFC 2543. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rtp </span> - Enable/disable create pinholes for RTP traffic to traverse firewall. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-algorithm </span> - Relative strength of encryption algorithms accepted in negotiation. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-auth-client </span> - Require a client certificate and authenticate it with the peer/peergrp. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-auth-server </span> - Authenticate the server's certificate with the peer/peergrp. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-client-certificate </span> - Name of Certificate to offer to server if requested. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-client-renegotiation </span> - Allow/block client renegotiation by server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-max-version </span> - Highest SSL/TLS version to negotiate. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-min-version </span> - Lowest SSL/TLS version to negotiate. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-mode </span> - SSL/TLS mode for encryption & decryption of traffic. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-pfs </span> - SSL Perfect Forward Secrecy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-send-empty-frags </span> - Send empty fragments to avoid attack on CBC IV (SSL 3. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-server-certificate </span> - Name of Certificate return to the client in every SSL connection. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable SIP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> strict-register </span> - Enable/disable only allow the registrar to connect. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> subscribe-rate </span> - SUBSCRIBE request rate limit (per second, per policy). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> unknown-header </span> - Action for unknown SIP header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> update-rate </span> - UPDATE request rate limit (per second, per policy). <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/voip/profile/{profile}/sip</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/voip/profile/{profile}/sip</span>  </li>
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



