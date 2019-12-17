:source: fmgr_pm_config_obj_wireless_controller_vap_vap_dynamic_mapping.py

:orphan:

.. _fmgr_pm_config_obj_wireless_controller_vap_vap_dynamic_mapping:

fmgr_pm_config_obj_wireless_controller_vap_vap_dynamic_mapping
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/wireless-controller/vap/{vap}/dynamic_mapping`
- `/pm/config/global/obj/wireless-controller/vap/{vap}/dynamic_mapping`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_centmgmt</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">_dhcp_svr_id</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">_intf_allowaccess</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, fgfm, auto-ipsec, radius-acct, probe-response, capwap]</span> </li>
 </ul>
 <li><span class="li-head">_intf_device-identification</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">_intf_device-netscan</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">_intf_dhcp-relay-ip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">_intf_dhcp-relay-service</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">_intf_dhcp-relay-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular, ipsec]</span>  <span class="li-normal">default: regular</span> </li>
 <li><span class="li-head">_intf_dhcp6-relay-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">_intf_dhcp6-relay-service</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">_intf_dhcp6-relay-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular]</span>  <span class="li-normal">default: regular</span> </li>
 <li><span class="li-head">_intf_ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">_intf_ip6-address</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">_intf_ip6-allowaccess</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [https, ping, ssh, snmp, http, telnet, any, fgfm, capwap]</span> </li>
 </ul>
 <li><span class="li-head">_intf_listen-forticlient-connection</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">acct-interim-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">address-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">alias</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">atf-weight</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">auth</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [PSK, psk, RADIUS, radius, usergroup]</span> </li>
 <li><span class="li-head">broadcast-ssid</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">broadcast-suppression</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [dhcp, arp, dhcp2, arp2, netbios-ns, netbios-ds, arp3, dhcp-up, dhcp-down, arp-known, arp-unknown, arp-reply, ipv6, dhcp-starvation, arp-poison, all-other-mc, all-other-bc, arp-proxy, dhcp-ucast]</span> </li>
 </ul>
 <li><span class="li-head">captive-portal-ac-name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">captive-portal-macauth-radius-secret</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">captive-portal-macauth-radius-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">captive-portal-radius-secret</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">captive-portal-radius-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">captive-portal-session-timeout-interval</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">client-count</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dhcp-lease-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dhcp-option82-circuit-id-insertion</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, style-1, style-2]</span> </li>
 <li><span class="li-head">dhcp-option82-insertion</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp-option82-remote-id-insertion</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, style-1]</span> </li>
 <li><span class="li-head">dynamic-vlan</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">eap-reauth</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">eap-reauth-intv</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eapol-key-retries</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">encrypt</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [TKIP, AES, TKIP-AES]</span> </li>
 <li><span class="li-head">external-fast-roaming</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">external-logout</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">external-web</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fast-bss-transition</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fast-roaming</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ft-mobility-domain</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ft-over-ds</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ft-r0-key-lifetime</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">gtk-rekey</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">gtk-rekey-intv</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">hotspot20-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">intra-vap-privacy</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">key</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">keyindex</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ldpc</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, tx, rx, rxtx]</span> </li>
 <li><span class="li-head">local-authentication</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">local-bridging</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">local-lan</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, allow]</span> </li>
 <li><span class="li-head">local-standalone</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">local-standalone-nat</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">local-switching</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mac-auth-bypass</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mac-filter</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mac-filter-policy-other</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, allow]</span> </li>
 <li><span class="li-head">max-clients</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-clients-ap</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">me-disable-thresh</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mesh-backhaul</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mpsk</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mpsk-concurrent-clients</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">multicast-enhance</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">multicast-rate</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [0, 6000, 12000, 24000]</span> </li>
 <li><span class="li-head">okc</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">owe-groups</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [19, 20, 21]</span> </li>
 </ul>
 <li><span class="li-head">owe-transition</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">owe-transition-ssid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">passphrase</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">pmf</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, optional]</span> </li>
 <li><span class="li-head">pmf-assoc-comeback-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">pmf-sa-query-retry-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">portal-message-override-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">portal-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auth, auth+disclaimer, disclaimer, email-collect, cmcc, cmcc-macauth, auth-mac]</span> </li>
 <li><span class="li-head">probe-resp-suppression</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">probe-resp-threshold</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ptk-rekey</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ptk-rekey-intv</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">qos-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">quarantine</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">radio-2g-threshold</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">radio-5g-threshold</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">radio-sensitivity</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">radius-mac-auth</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">radius-mac-auth-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">radius-mac-auth-usergroups</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">radius-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rates-11a</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1, 1-basic, 2, 2-basic, 5.5, 5.5-basic, 6, 6-basic, 9, 9-basic, 12, 12-basic, 18, 18-basic, 24, 24-basic, 36, 36-basic, 48, 48-basic, 54, 54-basic, 11, 11-basic]</span> </li>
 </ul>
 <li><span class="li-head">rates-11ac-ss12</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [mcs0/1, mcs1/1, mcs2/1, mcs3/1, mcs4/1, mcs5/1, mcs6/1, mcs7/1, mcs8/1, mcs9/1, mcs0/2, mcs1/2, mcs2/2, mcs3/2, mcs4/2, mcs5/2, mcs6/2, mcs7/2, mcs8/2, mcs9/2, mcs10/1, mcs11/1, mcs10/2, mcs11/2]</span> </li>
 </ul>
 <li><span class="li-head">rates-11ac-ss34</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [mcs0/3, mcs1/3, mcs2/3, mcs3/3, mcs4/3, mcs5/3, mcs6/3, mcs7/3, mcs8/3, mcs9/3, mcs0/4, mcs1/4, mcs2/4, mcs3/4, mcs4/4, mcs5/4, mcs6/4, mcs7/4, mcs8/4, mcs9/4, mcs10/3, mcs11/3, mcs10/4, mcs11/4]</span> </li>
 </ul>
 <li><span class="li-head">rates-11bg</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1, 1-basic, 2, 2-basic, 5.5, 5.5-basic, 6, 6-basic, 9, 9-basic, 12, 12-basic, 18, 18-basic, 24, 24-basic, 36, 36-basic, 48, 48-basic, 54, 54-basic, 11, 11-basic]</span> </li>
 </ul>
 <li><span class="li-head">rates-11n-ss12</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [mcs0/1, mcs1/1, mcs2/1, mcs3/1, mcs4/1, mcs5/1, mcs6/1, mcs7/1, mcs8/2, mcs9/2, mcs10/2, mcs11/2, mcs12/2, mcs13/2, mcs14/2, mcs15/2]</span> </li>
 </ul>
 <li><span class="li-head">rates-11n-ss34</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [mcs16/3, mcs17/3, mcs18/3, mcs19/3, mcs20/3, mcs21/3, mcs22/3, mcs23/3, mcs24/4, mcs25/4, mcs26/4, mcs27/4, mcs28/4, mcs29/4, mcs30/4, mcs31/4]</span> </li>
 </ul>
 <li><span class="li-head">sae-groups</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1, 2, 5, 14, 15, 16, 17, 18, 19, 20, 21, 27, 28, 29, 30, 31]</span> </li>
 </ul>
 <li><span class="li-head">sae-password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">schedule</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">security</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [None, WEP64, wep64, WEP128, wep128, WPA_PSK, WPA_RADIUS, WPA, WPA2, WPA2_AUTO, open, wpa-personal, wpa-enterprise, captive-portal, wpa-only-personal, wpa-only-enterprise, wpa2-only-personal, wpa2-only-enterprise, wpa-personal+captive-portal, wpa-only-personal+captive-portal, wpa2-only-personal+captive-portal, osen, wpa3-enterprise, sae, sae-transition, owe, wpa3-sae, wpa3-sae-transition]</span> </li>
 <li><span class="li-head">security-exempt-list</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">security-obsolete-option</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">security-redirect-url</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">selected-usergroups</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">split-tunneling</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tkip-counter-measure</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">usergroup</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">utm-profile</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vlan-auto</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">vlan-pooling</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [wtp-group, round-robin, hash, disable]</span> </li>
 <li><span class="li-head">vlanid</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">voice-enterprise</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [_centmgmt, _dhcp_svr_id, _intf_allowaccess, _intf_device-identification, _intf_device-netscan, _intf_dhcp-relay-ip, _intf_dhcp-relay-service, _intf_dhcp-relay-type, _intf_dhcp6-relay-ip, _intf_dhcp6-relay-service, _intf_dhcp6-relay-type, _intf_ip, _intf_ip6-address, _intf_ip6-allowaccess, _intf_listen-forticlient-connection, _scope, acct-interim-interval, address-group, alias, atf-weight, auth, broadcast-ssid, broadcast-suppression, captive-portal-ac-name, captive-portal-macauth-radius-secret, captive-portal-macauth-radius-server, captive-portal-radius-secret, captive-portal-radius-server, captive-portal-session-timeout-interval, client-count, dhcp-lease-time, dhcp-option82-circuit-id-insertion, dhcp-option82-insertion, dhcp-option82-remote-id-insertion, dynamic-vlan, eap-reauth, eap-reauth-intv, eapol-key-retries, encrypt, external-fast-roaming, external-logout, external-web, fast-bss-transition, fast-roaming, ft-mobility-domain, ft-over-ds, ft-r0-key-lifetime, gtk-rekey, gtk-rekey-intv, hotspot20-profile, intra-vap-privacy, ip, key, keyindex, ldpc, local-authentication, local-bridging, local-lan, local-standalone, local-standalone-nat, local-switching, mac-auth-bypass, mac-filter, mac-filter-policy-other, max-clients, max-clients-ap, me-disable-thresh, mesh-backhaul, mpsk, mpsk-concurrent-clients, multicast-enhance, multicast-rate, okc, owe-groups, owe-transition, owe-transition-ssid, passphrase, pmf, pmf-assoc-comeback-timeout, pmf-sa-query-retry-timeout, portal-message-override-group, portal-type, probe-resp-suppression, probe-resp-threshold, ptk-rekey, ptk-rekey-intv, qos-profile, quarantine, radio-2g-threshold, radio-5g-threshold, radio-sensitivity, radius-mac-auth, radius-mac-auth-server, radius-mac-auth-usergroups, radius-server, rates-11a, rates-11ac-ss12, rates-11ac-ss34, rates-11bg, rates-11n-ss12, rates-11n-ss34, sae-groups, sae-password, schedule, security, security-exempt-list, security-obsolete-option, security-redirect-url, selected-usergroups, split-tunneling, ssid, tkip-counter-measure, usergroup, utm-profile, vdom, vlan-auto, vlan-pooling, vlanid, voice-enterprise]</span> </li>
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
    - name: send request to /pm/config/obj/wireless-controller/vap/{vap}/dynamic_mapping
      fmgr_pm_config_obj_wireless_controller_vap_vap_dynamic_mapping:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vap: <value of string>
         params:
            - 
               data: 
                - 
                     _centmgmt: <value in [disable, enable] default: disable>
                     _dhcp_svr_id: <value of string>
                     _intf_allowaccess: 
                      - <value in [https, ping, ssh, ...]>
                     _intf_device-identification: <value in [disable, enable] default: disable>
                     _intf_device-netscan: <value in [disable, enable] default: disable>
                     _intf_dhcp-relay-ip: 
                      - <value of string>
                     _intf_dhcp-relay-service: <value in [disable, enable] default: disable>
                     _intf_dhcp-relay-type: <value in [regular, ipsec] default: regular>
                     _intf_dhcp6-relay-ip: <value of string>
                     _intf_dhcp6-relay-service: <value in [disable, enable] default: disable>
                     _intf_dhcp6-relay-type: <value in [regular] default: regular>
                     _intf_ip: <value of string>
                     _intf_ip6-address: <value of string>
                     _intf_ip6-allowaccess: 
                      - <value in [https, ping, ssh, ...]>
                     _intf_listen-forticlient-connection: <value in [disable, enable] default: disable>
                     _scope: 
                      - 
                           name: <value of string>
                           vdom: <value of string>
                     acct-interim-interval: <value of integer>
                     address-group: <value of string>
                     alias: <value of string>
                     atf-weight: <value of integer>
                     auth: <value in [PSK, psk, RADIUS, ...]>
                     broadcast-ssid: <value in [disable, enable]>
                     broadcast-suppression: 
                      - <value in [dhcp, arp, dhcp2, ...]>
                     captive-portal-ac-name: <value of string>
                     captive-portal-macauth-radius-secret: 
                      - <value of string>
                     captive-portal-macauth-radius-server: <value of string>
                     captive-portal-radius-secret: 
                      - <value of string>
                     captive-portal-radius-server: <value of string>
                     captive-portal-session-timeout-interval: <value of integer>
                     client-count: <value of integer>
                     dhcp-lease-time: <value of integer>
                     dhcp-option82-circuit-id-insertion: <value in [disable, style-1, style-2]>
                     dhcp-option82-insertion: <value in [disable, enable]>
                     dhcp-option82-remote-id-insertion: <value in [disable, style-1]>
                     dynamic-vlan: <value in [disable, enable]>
                     eap-reauth: <value in [disable, enable]>
                     eap-reauth-intv: <value of integer>
                     eapol-key-retries: <value in [disable, enable]>
                     encrypt: <value in [TKIP, AES, TKIP-AES]>
                     external-fast-roaming: <value in [disable, enable]>
                     external-logout: <value of string>
                     external-web: <value of string>
                     fast-bss-transition: <value in [disable, enable]>
                     fast-roaming: <value in [disable, enable]>
                     ft-mobility-domain: <value of integer>
                     ft-over-ds: <value in [disable, enable]>
                     ft-r0-key-lifetime: <value of integer>
                     gtk-rekey: <value in [disable, enable]>
                     gtk-rekey-intv: <value of integer>
                     hotspot20-profile: <value of string>
                     intra-vap-privacy: <value in [disable, enable]>
                     ip: <value of string>
                     key: 
                      - <value of string>
                     keyindex: <value of integer>
                     ldpc: <value in [disable, tx, rx, ...]>
                     local-authentication: <value in [disable, enable]>
                     local-bridging: <value in [disable, enable]>
                     local-lan: <value in [deny, allow]>
                     local-standalone: <value in [disable, enable]>
                     local-standalone-nat: <value in [disable, enable]>
                     local-switching: <value in [disable, enable]>
                     mac-auth-bypass: <value in [disable, enable]>
                     mac-filter: <value in [disable, enable]>
                     mac-filter-policy-other: <value in [deny, allow]>
                     max-clients: <value of integer>
                     max-clients-ap: <value of integer>
                     me-disable-thresh: <value of integer>
                     mesh-backhaul: <value in [disable, enable]>
                     mpsk: <value in [disable, enable]>
                     mpsk-concurrent-clients: <value of integer>
                     multicast-enhance: <value in [disable, enable]>
                     multicast-rate: <value in [0, 6000, 12000, ...]>
                     okc: <value in [disable, enable]>
                     owe-groups: 
                      - <value in [19, 20, 21]>
                     owe-transition: <value in [disable, enable]>
                     owe-transition-ssid: <value of string>
                     passphrase: 
                      - <value of string>
                     pmf: <value in [disable, enable, optional]>
                     pmf-assoc-comeback-timeout: <value of integer>
                     pmf-sa-query-retry-timeout: <value of integer>
                     portal-message-override-group: <value of string>
                     portal-type: <value in [auth, auth+disclaimer, disclaimer, ...]>
                     probe-resp-suppression: <value in [disable, enable]>
                     probe-resp-threshold: <value of string>
                     ptk-rekey: <value in [disable, enable]>
                     ptk-rekey-intv: <value of integer>
                     qos-profile: <value of string>
                     quarantine: <value in [disable, enable]>
                     radio-2g-threshold: <value of string>
                     radio-5g-threshold: <value of string>
                     radio-sensitivity: <value in [disable, enable]>
                     radius-mac-auth: <value in [disable, enable]>
                     radius-mac-auth-server: <value of string>
                     radius-mac-auth-usergroups: 
                      - <value of string>
                     radius-server: <value of string>
                     rates-11a: 
                      - <value in [1, 1-basic, 2, ...]>
                     rates-11ac-ss12: 
                      - <value in [mcs0/1, mcs1/1, mcs2/1, ...]>
                     rates-11ac-ss34: 
                      - <value in [mcs0/3, mcs1/3, mcs2/3, ...]>
                     rates-11bg: 
                      - <value in [1, 1-basic, 2, ...]>
                     rates-11n-ss12: 
                      - <value in [mcs0/1, mcs1/1, mcs2/1, ...]>
                     rates-11n-ss34: 
                      - <value in [mcs16/3, mcs17/3, mcs18/3, ...]>
                     sae-groups: 
                      - <value in [1, 2, 5, ...]>
                     sae-password: 
                      - <value of string>
                     schedule: <value of string>
                     security: <value in [None, WEP64, wep64, ...]>
                     security-exempt-list: <value of string>
                     security-obsolete-option: <value in [disable, enable]>
                     security-redirect-url: <value of string>
                     selected-usergroups: <value of string>
                     split-tunneling: <value in [disable, enable]>
                     ssid: <value of string>
                     tkip-counter-measure: <value in [disable, enable]>
                     usergroup: <value of string>
                     utm-profile: <value of string>
                     vdom: <value of string>
                     vlan-auto: <value in [disable, enable]>
                     vlan-pooling: <value in [wtp-group, round-robin, hash, ...]>
                     vlanid: <value of integer>
                     voice-enterprise: <value in [disable, enable]>
    - name: send request to /pm/config/obj/wireless-controller/vap/{vap}/dynamic_mapping
      fmgr_pm_config_obj_wireless_controller_vap_vap_dynamic_mapping:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vap: <value of string>
         params:
            - 
               attr: <value of string>
               fields: 
                - 
                   - <value in [_centmgmt, _dhcp_svr_id, _intf_allowaccess, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/vap/{vap}/dynamic_mapping</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> _centmgmt </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> _dhcp_svr_id </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> _intf_allowaccess </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> _intf_device-identification </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> _intf_device-netscan </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> _intf_dhcp-relay-ip </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> _intf_dhcp-relay-service </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> _intf_dhcp-relay-type </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: regular</span>  </li>
 <li> <span class="li-return"> _intf_dhcp6-relay-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> _intf_dhcp6-relay-service </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> _intf_dhcp6-relay-type </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: regular</span>  </li>
 <li> <span class="li-return"> _intf_ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> _intf_ip6-address </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> _intf_ip6-allowaccess </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> _intf_listen-forticlient-connection </span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> _scope </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> acct-interim-interval </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> address-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> alias </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> atf-weight </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> auth </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> broadcast-ssid </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> broadcast-suppression </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> captive-portal-ac-name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> captive-portal-macauth-radius-secret </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> captive-portal-macauth-radius-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> captive-portal-radius-secret </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> captive-portal-radius-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> captive-portal-session-timeout-interval </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> client-count </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> dhcp-lease-time </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> dhcp-option82-circuit-id-insertion </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dhcp-option82-insertion </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dhcp-option82-remote-id-insertion </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dynamic-vlan </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> eap-reauth </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> eap-reauth-intv </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> eapol-key-retries </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> encrypt </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> external-fast-roaming </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> external-logout </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> external-web </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fast-bss-transition </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fast-roaming </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ft-mobility-domain </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ft-over-ds </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ft-r0-key-lifetime </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> gtk-rekey </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> gtk-rekey-intv </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> hotspot20-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> intra-vap-privacy </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> key </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> keyindex </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ldpc </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> local-authentication </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> local-bridging </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> local-lan </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> local-standalone </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> local-standalone-nat </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> local-switching </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mac-auth-bypass </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mac-filter </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mac-filter-policy-other </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-clients </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> max-clients-ap </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> me-disable-thresh </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mesh-backhaul </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mpsk </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mpsk-concurrent-clients </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> multicast-enhance </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> multicast-rate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> okc </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> owe-groups </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> owe-transition </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> owe-transition-ssid </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> passphrase </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> pmf </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pmf-assoc-comeback-timeout </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> pmf-sa-query-retry-timeout </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> portal-message-override-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> portal-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> probe-resp-suppression </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> probe-resp-threshold </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ptk-rekey </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ptk-rekey-intv </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> qos-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> quarantine </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> radio-2g-threshold </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> radio-5g-threshold </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> radio-sensitivity </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> radius-mac-auth </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> radius-mac-auth-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> radius-mac-auth-usergroups </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> radius-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rates-11a </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> rates-11ac-ss12 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> rates-11ac-ss34 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> rates-11bg </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> rates-11n-ss12 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> rates-11n-ss34 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> sae-groups </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> sae-password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> schedule </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> security </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> security-exempt-list </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> security-obsolete-option </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> security-redirect-url </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> selected-usergroups </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> split-tunneling </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssid </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tkip-counter-measure </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> usergroup </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> utm-profile </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vlan-auto </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vlan-pooling </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vlanid </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> voice-enterprise </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/vap/{vap}/dynamic_mapping</span>  </li>
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



