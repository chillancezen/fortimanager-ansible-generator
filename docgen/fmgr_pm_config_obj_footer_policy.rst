:source: fmgr_pm_config_obj_footer_policy.py

:orphan:

.. _fmgr_pm_config_obj_footer_policy:

fmgr_pm_config_obj_footer_policy
++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/global/footer/policy`
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
 <li><span class="li-head">parameters for method: [get]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [action, active-auth-method, anti-replay, app-category, app-group, application, application-charts, application-list, auth-cert, auth-method, auth-path, auth-portal, auth-redirect-addr, auto-asic-offload, av-profile, bandwidth, block-notification, captive-portal-exempt, capture-packet, casi-profile, central-nat, cifs-profile, client-reputation, client-reputation-mode, custom-log-fields, deep-inspection-options, delay-tcp-npu-session, delay-tcp-npu-sessoin, device-detection-portal, devices, diffserv-forward, diffserv-reverse, diffservcode-forward, diffservcode-rev, disclaimer, dlp-sensor, dnsfilter-profile, dponly, dscp-match, dscp-negate, dscp-value, dsri, dstaddr, dstaddr-negate, dstaddr6, dstintf, dynamic-profile, dynamic-profile-access, dynamic-profile-fallthrough, dynamic-profile-group, email-collect, email-collection-portal, emailfilter-profile, endpoint-check, endpoint-compliance, endpoint-keepalive-interface, endpoint-profile, failed-connection, fall-through-unauthenticated, firewall-session-dirty, fixedport, forticlient-compliance-devices, forticlient-compliance-enforcement-portal, fsae, fsae-server-for-ntlm, fsso, fsso-agent-for-ntlm, geo-location, geoip-anycast, global-label, groups, gtp-profile, http-policy-redirect, icap-profile, identity-based, identity-based-route, identity-from, inbound, inspection-mode, internet-service, internet-service-custom, internet-service-custom-group, internet-service-group, internet-service-id, internet-service-negate, internet-service-src, internet-service-src-custom, internet-service-src-custom-group, internet-service-src-group, internet-service-src-id, internet-service-src-negate, ip-based, ippool, ips-sensor, label, learning-mode, log-unmatched-traffic, logtraffic, logtraffic-app, logtraffic-start, match-vip, mms-profile, name, nat, natinbound, natip, natoutbound, np-acceleration, ntlm, ntlm-enabled-browsers, ntlm-guest, outbound, per-ip-shaper, permit-any-host, permit-stun-host, policyid, poolname, profile-group, profile-protocol-options, profile-type, radius-mac-auth-bypass, redirect-url, replacemsg-group, replacemsg-override-group, reputation-direction, reputation-minimum, require-tfa, rsso, rtp-addr, rtp-nat, scan-botnet-connections, schedule, schedule-timeout, send-deny-packet, service, service-negate, session-ttl, sessions, spamfilter-profile, srcaddr, srcaddr-negate, srcaddr6, srcintf, ssh-filter-profile, ssh-policy-redirect, ssl-mirror, ssl-mirror-intf, ssl-ssh-profile, sslvpn-auth, sslvpn-ccert, sslvpn-cipher, sso-auth-method, status, tags, tcp-mss-receiver, tcp-mss-sender, tcp-reset, tcp-session-without-syn, timeout-send-rst, tos, tos-mask, tos-negate, traffic-shaper, traffic-shaper-reverse, transaction-based, url-category, users, utm-inspection-mode, utm-status, uuid, vlan-cos-fwd, vlan-cos-rev, vlan-filter, voip-profile, vpntunnel, waf-profile, wanopt, wanopt-detection, wanopt-passive-opt, wanopt-peer, wanopt-profile, wccp, web-auth-cookie, webcache, webcache-https, webfilter-profile, webproxy-forward-server, webproxy-profile, wsso]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FOOTER/POLICY
      fmgr_pm_config_obj_footer_policy:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [action, active-auth-method, anti-replay, ...]>
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
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> active-auth-method </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> anti-replay </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> app-category </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> app-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> application </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> application-charts </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> application-list </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auth-cert </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auth-method </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auth-path </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auth-portal </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auth-redirect-addr </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auto-asic-offload </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> av-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> bandwidth </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> block-notification </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> captive-portal-exempt </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> capture-packet </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> casi-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> central-nat </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> cifs-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> client-reputation </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> client-reputation-mode </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> comments </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> custom-log-fields </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> deep-inspection-options </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> delay-tcp-npu-session </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> delay-tcp-npu-sessoin </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> device-detection-portal </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> devices </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> diffserv-forward </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> diffserv-reverse </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> diffservcode-forward </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> diffservcode-rev </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> disclaimer </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dlp-sensor </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dnsfilter-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dponly </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dscp-match </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dscp-negate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dscp-value </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dsri </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstaddr </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstaddr-negate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstaddr6 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstintf </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dynamic-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dynamic-profile-access </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> dynamic-profile-fallthrough </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dynamic-profile-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> email-collect </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> email-collection-portal </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> emailfilter-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> endpoint-check </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> endpoint-compliance </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> endpoint-keepalive-interface </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> endpoint-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> failed-connection </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fall-through-unauthenticated </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> firewall-session-dirty </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fixedport </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> forticlient-compliance-devices </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> forticlient-compliance-enforcement-portal </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fsae </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fsae-server-for-ntlm </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fsso </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fsso-agent-for-ntlm </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> geo-location </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> geoip-anycast </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> global-label </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> groups </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> gtp-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-policy-redirect </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> icap-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> identity-based </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> identity-based-policy </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> application-charts </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> application-list </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> av-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> capture-packet </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> deep-inspection-options </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> devices </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dlp-sensor </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstaddr </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstaddr-negate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> endpoint-compliance </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> groups </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> icap-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ips-sensor </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> logtraffic </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> logtraffic-app </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> logtraffic-start </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mms-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> per-ip-shaper </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> profile-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> profile-protocol-options </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> profile-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> replacemsg-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> schedule </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> send-deny-packet </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> service </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> service-negate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spamfilter-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sslvpn-portal </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sslvpn-realm </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> traffic-shaper </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> traffic-shaper-reverse </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> users </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> utm-status </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> voip-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webfilter-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> identity-based-route </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> identity-from </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> inbound </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> inspection-mode </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-custom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-custom-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-id </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-negate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-src </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-src-custom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-src-custom-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-src-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-src-id </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-src-negate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip-based </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ippool </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ips-sensor </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> label </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> learning-mode </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log-unmatched-traffic </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> logtraffic </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> logtraffic-app </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> logtraffic-start </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> match-vip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mms-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> nat </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> natinbound </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> natip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> natoutbound </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> np-acceleration </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ntlm </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ntlm-enabled-browsers </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ntlm-guest </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> outbound </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> per-ip-shaper </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> permit-any-host </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> permit-stun-host </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> policyid </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> poolname </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> profile-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> profile-protocol-options </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> profile-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> radius-mac-auth-bypass </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> redirect-url </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> replacemsg-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> replacemsg-override-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> reputation-direction </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> reputation-minimum </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> require-tfa </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rsso </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rtp-addr </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rtp-nat </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> scan-botnet-connections </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> schedule </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> schedule-timeout </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> send-deny-packet </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> service </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> service-negate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> session-ttl </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> sessions </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spamfilter-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcaddr </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcaddr-negate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcaddr6 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcintf </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssh-filter-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssh-policy-redirect </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-mirror </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-mirror-intf </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-ssh-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sslvpn-auth </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sslvpn-ccert </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sslvpn-cipher </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sso-auth-method </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tags </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tcp-mss-receiver </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> tcp-mss-sender </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> tcp-reset </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tcp-session-without-syn </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> timeout-send-rst </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tos </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tos-mask </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tos-negate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> traffic-shaper </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> traffic-shaper-reverse </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> transaction-based </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> url-category </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> users </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> utm-inspection-mode </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> utm-status </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> uuid </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vlan-cos-fwd </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> vlan-cos-rev </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> vlan-filter </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> voip-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vpntunnel </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> waf-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wanopt </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wanopt-detection </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wanopt-passive-opt </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wanopt-peer </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wanopt-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wccp </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> web-auth-cookie </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webcache </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webcache-https </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webfilter-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webproxy-forward-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webproxy-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wsso </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/global/footer/policy</span>  </li>
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



