:source: fmgr_pm_config_pkg_footer_policy6.py

:orphan:

.. _fmgr_pm_config_pkg_footer_policy6:

fmgr_pm_config_pkg_footer_policy6
+++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/global/pkg/{pkg}/global/footer/policy6`
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
 <li><span class="li-head">pkg</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, accept, ipsec, ssl-vpn]</span> </li>
 <li><span class="li-head">anti-replay</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">app-category</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">app-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">application</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">application-charts</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [top10-app, top10-p2p-user, top10-media-user]</span> </li>
 </ul>
 <li><span class="li-head">application-list</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">auto-asic-offload</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">av-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">casi-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cifs-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">comments</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">custom-log-fields</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">deep-inspection-options</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">device-detection-portal</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">devices</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">diffserv-forward</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">diffserv-reverse</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">diffservcode-forward</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">diffservcode-rev</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dlp-sensor</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dnsfilter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dscp-match</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dscp-negate</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dscp-value</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dsri</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dstaddr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr-negate</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dstintf</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dynamic-profile</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dynamic-profile-access</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [imap, smtp, pop3, http, ftp, im, nntp, imaps, smtps, pop3s, https, ftps]</span> </li>
 </ul>
 <li><span class="li-head">dynamic-profile-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">email-collection-portal</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">emailfilter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">firewall-session-dirty</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [check-all, check-new]</span> </li>
 <li><span class="li-head">fixedport</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fsae</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">global-label</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">groups</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-policy-redirect</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">icap-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">identity-based</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">identity-based-policy6</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, accept]</span> </li>
 <li><span class="li-head">application-list</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">av-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">deep-inspection-options</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">devices</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dlp-sensor</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">endpoint-compliance</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">groups</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">icap-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ips-sensor</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">logtraffic</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, all, utm]</span> </li>
 <li><span class="li-head">mms-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">per-ip-shaper</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-protocol-options</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [single, group]</span> </li>
 <li><span class="li-head">replacemsg-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">schedule</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">send-deny-packet</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">service</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service-negate</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">spamfilter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sslvpn-portal</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sslvpn-realm</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">traffic-shaper</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">traffic-shaper-reverse</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">utm-status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">voip-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">webfilter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">identity-from</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auth, device]</span> </li>
 <li><span class="li-head">inbound</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">inspection-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [proxy, flow]</span> </li>
 <li><span class="li-head">ippool</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ips-sensor</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">label</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">logtraffic</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, all, utm]</span> </li>
 <li><span class="li-head">logtraffic-start</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nat</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">natinbound</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">natoutbound</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">np-accelation</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">np-acceleration</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">outbound</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">per-ip-shaper</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">policyid</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">poolname</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-protocol-options</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [single, group]</span> </li>
 <li><span class="li-head">replacemsg-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">replacemsg-override-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rsso</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">schedule</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">send-deny-packet</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">service</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service-negate</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">session-ttl</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">spamfilter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr-negate</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">srcintf</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssh-filter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssh-policy-redirect</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-mirror</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-mirror-intf</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-ssh-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sslvpn-auth</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [any, local, radius, ldap, tacacs+]</span> </li>
 <li><span class="li-head">sslvpn-ccert</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sslvpn-cipher</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [any, high, medium]</span> </li>
 <li><span class="li-head">status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tags</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tcp-mss-receiver</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-mss-sender</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tcp-session-without-syn</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [all, data-only, disable]</span> </li>
 <li><span class="li-head">timeout-send-rst</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tos</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tos-mask</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tos-negate</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">traffic-shaper</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">traffic-shaper-reverse</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">url-category</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">users</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">utm-inspection-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [proxy, flow]</span> </li>
 <li><span class="li-head">utm-status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">uuid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vlan-cos-fwd</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vlan-cos-rev</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">vlan-filter</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">voip-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vpntunnel</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">webfilter-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [action, anti-replay, app-category, app-group, application, application-charts, application-list, auto-asic-offload, av-profile, casi-profile, cifs-profile, comments, custom-log-fields, deep-inspection-options, device-detection-portal, devices, diffserv-forward, diffserv-reverse, diffservcode-forward, diffservcode-rev, dlp-sensor, dnsfilter-profile, dscp-match, dscp-negate, dscp-value, dsri, dstaddr, dstaddr-negate, dstintf, dynamic-profile, dynamic-profile-access, dynamic-profile-group, email-collection-portal, emailfilter-profile, firewall-session-dirty, fixedport, fsae, global-label, groups, http-policy-redirect, icap-profile, identity-based, identity-from, inbound, inspection-mode, ippool, ips-sensor, label, logtraffic, logtraffic-start, mms-profile, name, nat, natinbound, natoutbound, np-accelation, np-acceleration, outbound, per-ip-shaper, policyid, poolname, profile-group, profile-protocol-options, profile-type, replacemsg-group, replacemsg-override-group, rsso, schedule, send-deny-packet, service, service-negate, session-ttl, spamfilter-profile, srcaddr, srcaddr-negate, srcintf, ssh-filter-profile, ssh-policy-redirect, ssl-mirror, ssl-mirror-intf, ssl-ssh-profile, sslvpn-auth, sslvpn-ccert, sslvpn-cipher, status, tags, tcp-mss-receiver, tcp-mss-sender, tcp-session-without-syn, timeout-send-rst, tos, tos-mask, tos-negate, traffic-shaper, traffic-shaper-reverse, url-category, users, utm-inspection-mode, utm-status, uuid, vlan-cos-fwd, vlan-cos-rev, vlan-filter, voip-profile, vpntunnel, webfilter-profile]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FOOTER/POLICY6
      fmgr_pm_config_pkg_footer_policy6:
         method: <value in [add, set, update]>
         url_params:
            pkg: <value of string>
         params:
            -
               data:
                 -
                     action: <value in [deny, accept, ipsec, ...]>
                     anti-replay: <value in [disable, enable]>
                     app-category: <value of string>
                     app-group: <value of string>
                     application:
                       - <value of integer>
                     application-charts:
                       - <value in [top10-app, top10-p2p-user, top10-media-user]>
                     application-list: <value of string>
                     auto-asic-offload: <value in [disable, enable]>
                     av-profile: <value of string>
                     casi-profile: <value of string>
                     cifs-profile: <value of string>
                     comments: <value of string>
                     custom-log-fields: <value of string>
                     deep-inspection-options: <value of string>
                     device-detection-portal: <value in [disable, enable]>
                     devices: <value of string>
                     diffserv-forward: <value in [disable, enable]>
                     diffserv-reverse: <value in [disable, enable]>
                     diffservcode-forward: <value of string>
                     diffservcode-rev: <value of string>
                     dlp-sensor: <value of string>
                     dnsfilter-profile: <value of string>
                     dscp-match: <value in [disable, enable]>
                     dscp-negate: <value in [disable, enable]>
                     dscp-value: <value of string>
                     dsri: <value in [disable, enable]>
                     dstaddr: <value of string>
                     dstaddr-negate: <value in [disable, enable]>
                     dstintf: <value of string>
                     dynamic-profile: <value in [disable, enable]>
                     dynamic-profile-access:
                       - <value in [imap, smtp, pop3, ...]>
                     dynamic-profile-group: <value of string>
                     email-collection-portal: <value in [disable, enable]>
                     emailfilter-profile: <value of string>
                     firewall-session-dirty: <value in [check-all, check-new]>
                     fixedport: <value in [disable, enable]>
                     fsae: <value in [disable, enable]>
                     global-label: <value of string>
                     groups: <value of string>
                     http-policy-redirect: <value in [disable, enable]>
                     icap-profile: <value of string>
                     identity-based: <value in [disable, enable]>
                     identity-based-policy6:
                       -
                           action: <value in [deny, accept]>
                           application-list: <value of string>
                           av-profile: <value of string>
                           deep-inspection-options: <value of string>
                           devices: <value of string>
                           dlp-sensor: <value of string>
                           endpoint-compliance: <value in [disable, enable]>
                           groups: <value of string>
                           icap-profile: <value of string>
                           id: <value of integer>
                           ips-sensor: <value of string>
                           logtraffic: <value in [disable, enable, all, ...]>
                           mms-profile: <value of string>
                           per-ip-shaper: <value of string>
                           profile-group: <value of string>
                           profile-protocol-options: <value of string>
                           profile-type: <value in [single, group]>
                           replacemsg-group: <value of string>
                           schedule: <value of string>
                           send-deny-packet: <value in [disable, enable]>
                           service: <value of string>
                           service-negate: <value in [disable, enable]>
                           spamfilter-profile: <value of string>
                           sslvpn-portal: <value of string>
                           sslvpn-realm: <value of string>
                           traffic-shaper: <value of string>
                           traffic-shaper-reverse: <value of string>
                           utm-status: <value in [disable, enable]>
                           voip-profile: <value of string>
                           webfilter-profile: <value of string>
                     identity-from: <value in [auth, device]>
                     inbound: <value in [disable, enable]>
                     inspection-mode: <value in [proxy, flow]>
                     ippool: <value in [disable, enable]>
                     ips-sensor: <value of string>
                     label: <value of string>
                     logtraffic: <value in [disable, enable, all, ...]>
                     logtraffic-start: <value in [disable, enable]>
                     mms-profile: <value of string>
                     name: <value of string>
                     nat: <value in [disable, enable]>
                     natinbound: <value in [disable, enable]>
                     natoutbound: <value in [disable, enable]>
                     np-accelation: <value in [disable, enable]>
                     np-acceleration: <value in [disable, enable]>
                     outbound: <value in [disable, enable]>
                     per-ip-shaper: <value of string>
                     policyid: <value of integer>
                     poolname: <value of string>
                     profile-group: <value of string>
                     profile-protocol-options: <value of string>
                     profile-type: <value in [single, group]>
                     replacemsg-group: <value of string>
                     replacemsg-override-group: <value of string>
                     rsso: <value in [disable, enable]>
                     schedule: <value of string>
                     send-deny-packet: <value in [disable, enable]>
                     service: <value of string>
                     service-negate: <value in [disable, enable]>
                     session-ttl: <value of integer>
                     spamfilter-profile: <value of string>
                     srcaddr: <value of string>
                     srcaddr-negate: <value in [disable, enable]>
                     srcintf: <value of string>
                     ssh-filter-profile: <value of string>
                     ssh-policy-redirect: <value in [disable, enable]>
                     ssl-mirror: <value in [disable, enable]>
                     ssl-mirror-intf: <value of string>
                     ssl-ssh-profile: <value of string>
                     sslvpn-auth: <value in [any, local, radius, ...]>
                     sslvpn-ccert: <value in [disable, enable]>
                     sslvpn-cipher: <value in [any, high, medium]>
                     status: <value in [disable, enable]>
                     tags: <value of string>
                     tcp-mss-receiver: <value of integer>
                     tcp-mss-sender: <value of integer>
                     tcp-session-without-syn: <value in [all, data-only, disable]>
                     timeout-send-rst: <value in [disable, enable]>
                     tos: <value of string>
                     tos-mask: <value of string>
                     tos-negate: <value in [disable, enable]>
                     traffic-shaper: <value of string>
                     traffic-shaper-reverse: <value of string>
                     url-category: <value of string>
                     users: <value of string>
                     utm-inspection-mode: <value in [proxy, flow]>
                     utm-status: <value in [disable, enable]>
                     uuid: <value of string>
                     vlan-cos-fwd: <value of integer>
                     vlan-cos-rev: <value of integer>
                     vlan-filter: <value of string>
                     voip-profile: <value of string>
                     vpntunnel: <value of string>
                     webfilter-profile: <value of string>

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FOOTER/POLICY6
      fmgr_pm_config_pkg_footer_policy6:
         method: <value in [get]>
         url_params:
            pkg: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [action, anti-replay, app-category, ...]>
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
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> policyid </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/global/pkg/{pkg}/global/footer/policy6</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
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
 <li> <span class="li-return"> auto-asic-offload </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> av-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> casi-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> cifs-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> comments </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> custom-log-fields </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> deep-inspection-options </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> device-detection-portal </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> devices </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> diffserv-forward </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> diffserv-reverse </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> diffservcode-forward </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> diffservcode-rev </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dlp-sensor </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dnsfilter-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dscp-match </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dscp-negate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dscp-value </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dsri </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstaddr </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstaddr-negate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstintf </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dynamic-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dynamic-profile-access </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> dynamic-profile-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> email-collection-portal </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> emailfilter-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> firewall-session-dirty </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fixedport </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fsae </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> global-label </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> groups </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-policy-redirect </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> icap-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> identity-based </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> identity-based-policy6 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> application-list </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> av-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> deep-inspection-options </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> devices </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dlp-sensor </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> endpoint-compliance </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> groups </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> icap-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ips-sensor </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> logtraffic </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
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
 <li> <span class="li-return"> utm-status </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> voip-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webfilter-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> identity-from </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> inbound </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> inspection-mode </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ippool </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ips-sensor </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> label </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> logtraffic </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> logtraffic-start </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mms-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> nat </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> natinbound </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> natoutbound </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> np-accelation </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> np-acceleration </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> outbound </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> per-ip-shaper </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> policyid </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> poolname </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> profile-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> profile-protocol-options </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> profile-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> replacemsg-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> replacemsg-override-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rsso </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> schedule </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> send-deny-packet </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> service </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> service-negate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> session-ttl </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> spamfilter-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcaddr </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcaddr-negate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcintf </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssh-filter-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssh-policy-redirect </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-mirror </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-mirror-intf </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-ssh-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sslvpn-auth </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sslvpn-ccert </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sslvpn-cipher </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tags </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tcp-mss-receiver </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> tcp-mss-sender </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> tcp-session-without-syn </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> timeout-send-rst </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tos </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tos-mask </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tos-negate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> traffic-shaper </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> traffic-shaper-reverse </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
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
 <li> <span class="li-return"> webfilter-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/global/pkg/{pkg}/global/footer/policy6</span>  </li>
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



