:source: fmgr_pm_config_obj_wireless_controller_hotspot20_hs_profile_hs_profile.py

:orphan:

.. _fmgr_pm_config_obj_wireless_controller_hotspot20_hs_profile_hs_profile:

fmgr_pm_config_obj_wireless_controller_hotspot20_hs_profile_hs_profile -- Configure hotspot profile.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/wireless-controller/hotspot20/hs-profile/{hs-profile}`
- `/pm/config/global/obj/wireless-controller/hotspot20/hs-profile/{hs-profile}`
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
 <li><span class="li-head">hs-profile</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure hotspot profile.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">3gpp-plmn</span> - 3GPP PLMN name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">access-network-asra</span> - Enable/disable additional step required for access (ASRA). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">access-network-esr</span> - Enable/disable emergency services reachable (ESR). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">access-network-internet</span> - Enable/disable connectivity to the Internet. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">access-network-type</span> - Access network type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [private-network, private-network-with-guest-access, chargeable-public-network, free-public-network, personal-device-network, emergency-services-only-network, test-or-experimental, wildcard]</span> </li>
 <li><span class="li-head">access-network-uesa</span> - Enable/disable unauthenticated emergency service accessible (UESA). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">anqp-domain-id</span> - ANQP Domain ID (0-65535). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">bss-transition</span> - Enable/disable basic service set (BSS) transition Support. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">conn-cap</span> - Connection capability name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">deauth-request-timeout</span> - Deauthentication request timeout (in seconds). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dgaf</span> - Enable/disable downstream group-addressed forwarding (DGAF). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">domain-name</span> - Domain name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gas-comeback-delay</span> - GAS comeback delay (0 or 100 - 4000 milliseconds, default = 500). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">gas-fragmentation-limit</span> - GAS fragmentation limit (512 - 4096, default = 1024). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">hessid</span> - Homogeneous extended service set identifier (HESSID). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip-addr-type</span> - IP address type name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">l2tif</span> - Enable/disable Layer 2 traffic inspection and filtering. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">nai-realm</span> - NAI realm list name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Hotspot profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">network-auth</span> - Network authentication name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">oper-friendly-name</span> - Operator friendly name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">osu-provider</span> - Manually selected list of OSU provider(s). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">osu-ssid</span> - Online sign up (OSU) SSID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">pame-bi</span> - Enable/disable Pre-Association Message Exchange BSSID Independent (PAME-BI). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">proxy-arp</span> - Enable/disable Proxy ARP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">qos-map</span> - QoS MAP set ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">roaming-consortium</span> - Roaming consortium list name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">venue-group</span> - Venue group. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unspecified, assembly, business, educational, factory, institutional, mercantile, residential, storage, utility, vehicular, outdoor]</span> </li>
 <li><span class="li-head">venue-name</span> - Venue name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">venue-type</span> - Venue type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unspecified, arena, stadium, passenger-terminal, amphitheater, amusement-park, place-of-worship, convention-center, library, museum, restaurant, theater, bar, coffee-shop, zoo-or-aquarium, emergency-center, doctor-office, bank, fire-station, police-station, post-office, professional-office, research-facility, attorney-office, primary-school, secondary-school, university-or-college, factory, hospital, long-term-care-facility, rehab-center, group-home, prison-or-jail, retail-store, grocery-market, auto-service-station, shopping-mall, gas-station, private, hotel-or-motel, dormitory, boarding-house, automobile, airplane, bus, ferry, ship-or-boat, train, motor-bike, muni-mesh-network, city-park, rest-area, traffic-control, bus-stop, kiosk]</span> </li>
 <li><span class="li-head">wan-metrics</span> - WAN metric name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wnm-sleep-mode</span> - Enable/disable wireless network management (WNM) sleep mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure hotspot profile.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure hotspot profile.</li>
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
    - name: send request to /pm/config/obj/wireless-controller/hotspot20/hs-profile/{hs-profile}
      fmgr_pm_config_obj_wireless_controller_hotspot20_hs_profile_hs_profile:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            hs-profile: <value of string>
         params:
            - 
               data: 
                  3gpp-plmn: <value of string>
                  access-network-asra: <value in [disable, enable]>
                  access-network-esr: <value in [disable, enable]>
                  access-network-internet: <value in [disable, enable]>
                  access-network-type: <value in [private-network, private-network-with-guest-access, chargeable-public-network, ...]>
                  access-network-uesa: <value in [disable, enable]>
                  anqp-domain-id: <value of integer>
                  bss-transition: <value in [disable, enable]>
                  conn-cap: <value of string>
                  deauth-request-timeout: <value of integer>
                  dgaf: <value in [disable, enable]>
                  domain-name: <value of string>
                  gas-comeback-delay: <value of integer>
                  gas-fragmentation-limit: <value of integer>
                  hessid: <value of string>
                  ip-addr-type: <value of string>
                  l2tif: <value in [disable, enable]>
                  nai-realm: <value of string>
                  name: <value of string>
                  network-auth: <value of string>
                  oper-friendly-name: <value of string>
                  osu-provider: <value of string>
                  osu-ssid: <value of string>
                  pame-bi: <value in [disable, enable]>
                  proxy-arp: <value in [disable, enable]>
                  qos-map: <value of string>
                  roaming-consortium: <value of string>
                  venue-group: <value in [unspecified, assembly, business, ...]>
                  venue-name: <value of string>
                  venue-type: <value in [unspecified, arena, stadium, ...]>
                  wan-metrics: <value of string>
                  wnm-sleep-mode: <value in [disable, enable]>
    - name: send request to /pm/config/obj/wireless-controller/hotspot20/hs-profile/{hs-profile}
      fmgr_pm_config_obj_wireless_controller_hotspot20_hs_profile_hs_profile:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            hs-profile: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/hotspot20/hs-profile/{hs-profile}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> 3gpp-plmn </span> - 3GPP PLMN name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> access-network-asra </span> - Enable/disable additional step required for access (ASRA). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> access-network-esr </span> - Enable/disable emergency services reachable (ESR). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> access-network-internet </span> - Enable/disable connectivity to the Internet. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> access-network-type </span> - Access network type. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> access-network-uesa </span> - Enable/disable unauthenticated emergency service accessible (UESA). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> anqp-domain-id </span> - ANQP Domain ID (0-65535). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> bss-transition </span> - Enable/disable basic service set (BSS) transition Support. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> conn-cap </span> - Connection capability name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> deauth-request-timeout </span> - Deauthentication request timeout (in seconds). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> dgaf </span> - Enable/disable downstream group-addressed forwarding (DGAF). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> domain-name </span> - Domain name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> gas-comeback-delay </span> - GAS comeback delay (0 or 100 - 4000 milliseconds, default = 500). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> gas-fragmentation-limit </span> - GAS fragmentation limit (512 - 4096, default = 1024). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> hessid </span> - Homogeneous extended service set identifier (HESSID). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip-addr-type </span> - IP address type name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> l2tif </span> - Enable/disable Layer 2 traffic inspection and filtering. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> nai-realm </span> - NAI realm list name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Hotspot profile name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> network-auth </span> - Network authentication name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> oper-friendly-name </span> - Operator friendly name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> osu-provider </span> - Manually selected list of OSU provider(s). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> osu-ssid </span> - Online sign up (OSU) SSID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pame-bi </span> - Enable/disable Pre-Association Message Exchange BSSID Independent (PAME-BI). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> proxy-arp </span> - Enable/disable Proxy ARP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> qos-map </span> - QoS MAP set ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> roaming-consortium </span> - Roaming consortium list name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> venue-group </span> - Venue group. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> venue-name </span> - Venue name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> venue-type </span> - Venue type. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wan-metrics </span> - WAN metric name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wnm-sleep-mode </span> - Enable/disable wireless network management (WNM) sleep mode. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/wireless-controller/hotspot20/hs-profile/{hs-profile}</span>  </li>
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



