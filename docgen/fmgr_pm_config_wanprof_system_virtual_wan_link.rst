:source: fmgr_pm_config_wanprof_system_virtual_wan_link.py

:orphan:

.. _fmgr_pm_config_wanprof_system_virtual_wan_link:

fmgr_pm_config_wanprof_system_virtual_wan_link -- Configure redundant internet connections using SD-WAN (formerly virtual WAN link).
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link`
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
 <li><span class="li-head">wanprof</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure redundant internet connections using SD-WAN (formerly virtual WAN link).</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Configure redundant internet connections using SD-WAN (formerly virtual WAN link).</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">fail-detect</span> - Enable/disable SD-WAN Internet connection status checking (failure detection). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">health-check</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_dynamic-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">addr-mode</span> - Address mode (IPv4 or IPv6). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipv4, ipv6]</span> </li>
 <li><span class="li-head">failtime</span> - Number of failures before server is considered lost (1 - 3600, default = 5). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">http-agent</span> - String in the http-agent field in the HTTP header. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-get</span> - URL used to communicate with the server if the protocol if the protocol is HTTP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-match</span> - Response string expected from the server if the protocol is HTTP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">interval</span> - Status check interval, or the time between attempting to connect to the server (1 - 3600 sec, default = 5). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">members</span> - Member sequence number list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Status check or health check name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">packet-size</span> - Packet size of a twamp test session, <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">port</span> - Port number used to communicate with the server over the selected protocol. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">protocol</span> - Protocol used to determine if the FortiGate can communicate with the server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ping, tcp-echo, udp-echo, http, twamp, ping6]</span> </li>
 <li><span class="li-head">recoverytime</span> - Number of successful responses received before server is considered recovered (1 - 3600, default = 5). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">security-mode</span> - Twamp controller security mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, authentication]</span> </li>
 <li><span class="li-head">server</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">sla</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - SLA ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">jitter-threshold</span> - Jitter for SLA to make decision in milliseconds. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">latency-threshold</span> - Latency for SLA to make decision in milliseconds. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">link-cost-factor</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [latency, jitter, packet-loss]</span> </li>
 </ul>
 <li><span class="li-head">packetloss-threshold</span> - Packet loss for SLA to make decision in percentage. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">threshold-alert-jitter</span> - Alert threshold for jitter (ms, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold-alert-latency</span> - Alert threshold for latency (ms, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold-alert-packetloss</span> - Alert threshold for packet loss (percentage, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold-warning-jitter</span> - Warning threshold for jitter (ms, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold-warning-latency</span> - Warning threshold for latency (ms, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">threshold-warning-packetloss</span> - Warning threshold for packet loss (percentage, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">update-cascade-interface</span> - Enable/disable update cascade interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">update-static-route</span> - Enable/disable updating the static route. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">load-balance-mode</span> - Algorithm or mode to use for load balancing Internet traffic to SD-WAN members. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [source-ip-based, weight-based, usage-based, source-dest-ip-based, measured-volume-based]</span> </li>
 <li><span class="li-head">members</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_dynamic-member</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">comment</span> - Comments. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gateway</span> - The default gateway for this interface. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">gateway6</span> - IPv6 gateway. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ingress-spillover-threshold</span> - Ingress spillover threshold for this interface (0 - 16776000 kbit/s). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">interface</span> - Interface name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priority</span> - Priority of the interface (0 - 4294967295). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">seq-num</span> - Sequence number(1-255). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">source</span> - Source IP address used in the health-check packet to the server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source6</span> - Source IPv6 address used in the health-check packet to the server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spillover-threshold</span> - Egress spillover threshold for this interface (0 - 16776000 kbit/s). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Enable/disable this interface in the SD-WAN. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">volume-ratio</span> - Measured volume ratio (this value / sum of all values = percentage of link volume, 0 - 255). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">weight</span> - Weight of this interface for weighted load balancing. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">service</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">addr-mode</span> - Address mode (IPv4 or IPv6). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipv4, ipv6]</span> </li>
 <li><span class="li-head">bandwidth-weight</span> - Coefficient of reciprocal of available bidirectional bandwidth in the formula of custom-profile-1. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">default</span> - Enable/disable use of SD-WAN as default service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dscp-forward</span> - Enable/disable forward traffic DSCP tag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dscp-forward-tag</span> - Forward traffic DSCP tag. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dscp-reverse</span> - Enable/disable reverse traffic DSCP tag. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dscp-reverse-tag</span> - Reverse traffic DSCP tag. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dst</span> - Destination address name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dst-negate</span> - Enable/disable negation of destination address match. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dst6</span> - Destination address6 name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">end-port</span> - End destination port number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">gateway</span> - Enable/disable SD-WAN service gateway. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">groups</span> - User groups. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">health-check</span> - Health check. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">hold-down-time</span> - Waiting period in seconds when switching from the back-up member to the primary member (0 - 10000000, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">id</span> - Priority rule ID (1 - 4000). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">internet-service</span> - Enable/disable use of Internet service for application-based load balancing. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">internet-service-ctrl</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">internet-service-ctrl-group</span> - Control-based Internet Service group list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-custom</span> - Custom Internet service name list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-custom-group</span> - Custom Internet Service group list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-group</span> - Internet Service group list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-id</span> - Internet service ID list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">jitter-weight</span> - Coefficient of jitter in the formula of custom-profile-1. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">latency-weight</span> - Coefficient of latency in the formula of custom-profile-1. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">link-cost-factor</span> - Link cost factor. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [latency, jitter, packet-loss, inbandwidth, outbandwidth, bibandwidth, custom-profile-1]</span> </li>
 <li><span class="li-head">link-cost-threshold</span> - Percentage threshold change of link cost values that will result in policy route regeneration (0 - 10000000, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">member</span> - Member sequence number. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mode</span> - Control how the priority rule sets the priority of interfaces in the SD-WAN. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto, manual, priority, sla, load-balance]</span> </li>
 <li><span class="li-head">name</span> - Priority rule name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">packet-loss-weight</span> - Coefficient of packet-loss in the formula of custom-profile-1. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">priority-members</span> - Member sequence number list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">protocol</span> - Protocol number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">quality-link</span> - Quality grade. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">route-tag</span> - IPv4 route map route-tag. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sla</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">health-check</span> - Virtual WAN Link health-check. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - SLA ID. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">src</span> - Source address name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">src-negate</span> - Enable/disable negation of source address match. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">src6</span> - Source address6 name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">start-port</span> - Start destination port number. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Enable/disable SD-WAN service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tos</span> - Type of service bit pattern. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tos-mask</span> - Type of service evaluated bits. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">users</span> - User name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">status</span> - Enable/disable SD-WAN. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/WANPROF/{WANPROF}/SYSTEM/VIRTUAL-WAN-LINK
      fmgr_pm_config_wanprof_system_virtual_wan_link:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wanprof: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/WANPROF/{WANPROF}/SYSTEM/VIRTUAL-WAN-LINK
      fmgr_pm_config_wanprof_system_virtual_wan_link:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wanprof: <value of string>
         params:
            -
               data:
                  fail-detect: <value in [disable, enable]>
                  health-check:
                    -
                        _dynamic-server: <value of string>
                        addr-mode: <value in [ipv4, ipv6]>
                        failtime: <value of integer>
                        http-agent: <value of string>
                        http-get: <value of string>
                        http-match: <value of string>
                        interval: <value of integer>
                        members: <value of string>
                        name: <value of string>
                        packet-size: <value of integer>
                        password:
                          - <value of string>
                        port: <value of integer>
                        protocol: <value in [ping, tcp-echo, udp-echo, ...]>
                        recoverytime: <value of integer>
                        security-mode: <value in [none, authentication]>
                        server:
                          - <value of string>
                        sla:
                          -
                              id: <value of integer>
                              jitter-threshold: <value of integer>
                              latency-threshold: <value of integer>
                              link-cost-factor:
                                - <value in [latency, jitter, packet-loss]>
                              packetloss-threshold: <value of integer>
                        threshold-alert-jitter: <value of integer>
                        threshold-alert-latency: <value of integer>
                        threshold-alert-packetloss: <value of integer>
                        threshold-warning-jitter: <value of integer>
                        threshold-warning-latency: <value of integer>
                        threshold-warning-packetloss: <value of integer>
                        update-cascade-interface: <value in [disable, enable]>
                        update-static-route: <value in [disable, enable]>
                  load-balance-mode: <value in [source-ip-based, weight-based, usage-based, ...]>
                  members:
                    -
                        _dynamic-member: <value of string>
                        comment: <value of string>
                        gateway: <value of string>
                        gateway6: <value of string>
                        ingress-spillover-threshold: <value of integer>
                        interface: <value of string>
                        priority: <value of integer>
                        seq-num: <value of integer>
                        source: <value of string>
                        source6: <value of string>
                        spillover-threshold: <value of integer>
                        status: <value in [disable, enable]>
                        volume-ratio: <value of integer>
                        weight: <value of integer>
                  service:
                    -
                        addr-mode: <value in [ipv4, ipv6]>
                        bandwidth-weight: <value of integer>
                        default: <value in [disable, enable]>
                        dscp-forward: <value in [disable, enable]>
                        dscp-forward-tag: <value of string>
                        dscp-reverse: <value in [disable, enable]>
                        dscp-reverse-tag: <value of string>
                        dst: <value of string>
                        dst-negate: <value in [disable, enable]>
                        dst6: <value of string>
                        end-port: <value of integer>
                        gateway: <value in [disable, enable]>
                        groups: <value of string>
                        health-check: <value of string>
                        hold-down-time: <value of integer>
                        id: <value of integer>
                        internet-service: <value in [disable, enable]>
                        internet-service-ctrl:
                          - <value of integer>
                        internet-service-ctrl-group: <value of string>
                        internet-service-custom: <value of string>
                        internet-service-custom-group: <value of string>
                        internet-service-group: <value of string>
                        internet-service-id: <value of string>
                        jitter-weight: <value of integer>
                        latency-weight: <value of integer>
                        link-cost-factor: <value in [latency, jitter, packet-loss, ...]>
                        link-cost-threshold: <value of integer>
                        member: <value of string>
                        mode: <value in [auto, manual, priority, ...]>
                        name: <value of string>
                        packet-loss-weight: <value of integer>
                        priority-members: <value of string>
                        protocol: <value of integer>
                        quality-link: <value of integer>
                        route-tag: <value of integer>
                        sla:
                          -
                              health-check: <value of string>
                              id: <value of integer>
                        src: <value of string>
                        src-negate: <value in [disable, enable]>
                        src6: <value of string>
                        start-port: <value of integer>
                        status: <value in [disable, enable]>
                        tos: <value of string>
                        tos-mask: <value of string>
                        users: <value of string>
                  status: <value in [disable, enable]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> fail-detect </span> - Enable/disable SD-WAN Internet connection status checking (failure detection). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> health-check </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> _dynamic-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> addr-mode </span> - Address mode (IPv4 or IPv6). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> failtime </span> - Number of failures before server is considered lost (1 - 3600, default = 5). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> http-agent </span> - String in the http-agent field in the HTTP header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-get </span> - URL used to communicate with the server if the protocol if the protocol is HTTP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-match </span> - Response string expected from the server if the protocol is HTTP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> interval </span> - Status check interval, or the time between attempting to connect to the server (1 - 3600 sec, default = 5). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> members </span> - Member sequence number list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Status check or health check name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> packet-size </span> - Packet size of a twamp test session, <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> port </span> - Port number used to communicate with the server over the selected protocol. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> protocol </span> - Protocol used to determine if the FortiGate can communicate with the server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> recoverytime </span> - Number of successful responses received before server is considered recovered (1 - 3600, default = 5). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> security-mode </span> - Twamp controller security mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> sla </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - SLA ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> jitter-threshold </span> - Jitter for SLA to make decision in milliseconds. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> latency-threshold </span> - Latency for SLA to make decision in milliseconds. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> link-cost-factor </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> packetloss-threshold </span> - Packet loss for SLA to make decision in percentage. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> threshold-alert-jitter </span> - Alert threshold for jitter (ms, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> threshold-alert-latency </span> - Alert threshold for latency (ms, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> threshold-alert-packetloss </span> - Alert threshold for packet loss (percentage, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> threshold-warning-jitter </span> - Warning threshold for jitter (ms, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> threshold-warning-latency </span> - Warning threshold for latency (ms, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> threshold-warning-packetloss </span> - Warning threshold for packet loss (percentage, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> update-cascade-interface </span> - Enable/disable update cascade interface. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> update-static-route </span> - Enable/disable updating the static route. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> load-balance-mode </span> - Algorithm or mode to use for load balancing Internet traffic to SD-WAN members. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> members </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> _dynamic-member </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> comment </span> - Comments. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> gateway </span> - The default gateway for this interface. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> gateway6 </span> - IPv6 gateway. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ingress-spillover-threshold </span> - Ingress spillover threshold for this interface (0 - 16776000 kbit/s). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> interface </span> - Interface name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> priority </span> - Priority of the interface (0 - 4294967295). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> seq-num </span> - Sequence number(1-255). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> source </span> - Source IP address used in the health-check packet to the server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source6 </span> - Source IPv6 address used in the health-check packet to the server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spillover-threshold </span> - Egress spillover threshold for this interface (0 - 16776000 kbit/s). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable this interface in the SD-WAN. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> volume-ratio </span> - Measured volume ratio (this value / sum of all values = percentage of link volume, 0 - 255). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> weight </span> - Weight of this interface for weighted load balancing. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> service </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> addr-mode </span> - Address mode (IPv4 or IPv6). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> bandwidth-weight </span> - Coefficient of reciprocal of available bidirectional bandwidth in the formula of custom-profile-1. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> default </span> - Enable/disable use of SD-WAN as default service. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dscp-forward </span> - Enable/disable forward traffic DSCP tag. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dscp-forward-tag </span> - Forward traffic DSCP tag. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dscp-reverse </span> - Enable/disable reverse traffic DSCP tag. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dscp-reverse-tag </span> - Reverse traffic DSCP tag. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dst </span> - Destination address name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dst-negate </span> - Enable/disable negation of destination address match. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dst6 </span> - Destination address6 name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> end-port </span> - End destination port number. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> gateway </span> - Enable/disable SD-WAN service gateway. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> groups </span> - User groups. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> health-check </span> - Health check. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> hold-down-time </span> - Waiting period in seconds when switching from the back-up member to the primary member (0 - 10000000, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> id </span> - Priority rule ID (1 - 4000). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> internet-service </span> - Enable/disable use of Internet service for application-based load balancing. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-ctrl </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> internet-service-ctrl-group </span> - Control-based Internet Service group list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-custom </span> - Custom Internet service name list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-custom-group </span> - Custom Internet Service group list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-group </span> - Internet Service group list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-id </span> - Internet service ID list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> jitter-weight </span> - Coefficient of jitter in the formula of custom-profile-1. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> latency-weight </span> - Coefficient of latency in the formula of custom-profile-1. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> link-cost-factor </span> - Link cost factor. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> link-cost-threshold </span> - Percentage threshold change of link cost values that will result in policy route regeneration (0 - 10000000, default = 10). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> member </span> - Member sequence number. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mode </span> - Control how the priority rule sets the priority of interfaces in the SD-WAN. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Priority rule name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> packet-loss-weight </span> - Coefficient of packet-loss in the formula of custom-profile-1. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> priority-members </span> - Member sequence number list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> protocol </span> - Protocol number. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> quality-link </span> - Quality grade. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> route-tag </span> - IPv4 route map route-tag. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> sla </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> health-check </span> - Virtual WAN Link health-check. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - SLA ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> src </span> - Source address name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> src-negate </span> - Enable/disable negation of source address match. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> src6 </span> - Source address6 name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> start-port </span> - Start destination port number. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable SD-WAN service. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tos </span> - Type of service bit pattern. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tos-mask </span> - Type of service evaluated bits. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> users </span> - User name. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> status </span> - Enable/disable SD-WAN. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link</span>  </li>
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



