#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019-2020 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fmgr_wanprof_system_virtualwanlink
short_description: Configure redundant internet connections using SD-WAN (formerly virtual WAN link).
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link
    - Examples include all parameters and values need to be adjusted to data sources before usage.

version_added: "2.10"
author:
    - Frank Shen (@fshen01)
    - Link Zheng (@zhengl)
notes:
    - There are only three top-level parameters where 'method' is always required
      while other two 'params' and 'url_params' can be optional
    - Due to the complexity of fortimanager api schema, the validation is done
      out of Ansible native parameter validation procedure.
    - The syntax of OPTIONS doen not comply with the standard Ansible argument
      specification, but with the structure of fortimanager API schema, we need
      a trivial transformation when we are filling the ansible playbook
options:
    workspace_locking_adom:
        description: the adom to lock in case FortiManager running in workspace mode
        required: False
        type: string
        choices:
          - global
          - custom adom
    workspace_locking_timeout:
        description: teh maximum time in seconds to wait for other user to release the workspace lock
        required: False
        type: integer
        default: 300
    url_params:
        description: the parameters in url path
        required: True
        type: dict
        suboptions:
            adom:
                type: str
                description: the domain prefix, the none and global are reserved
                choices:
                  - none
                  - global
                  - custom dom
            wanprof:
                type: str
    schema_object0:
        methods: [get]
        description: 'Configure redundant internet connections using SD-WAN (formerly virtual WAN link).'
        api_categories: [api_tag0]
        api_tag0:
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the object will be returned.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'chksum - Return the check-sum value instead of attributes.'
                choices:
                    - 'object member'
                    - 'chksum'
                    - 'datasrc'
    schema_object1:
        methods: [set, update]
        description: 'Configure redundant internet connections using SD-WAN (formerly virtual WAN link).'
        api_categories: [api_tag0]
        api_tag0:
            data:
                fail-detect:
                    type: str
                    description: 'Enable/disable SD-WAN Internet connection status checking (failure detection).'
                    choices:
                        - 'disable'
                        - 'enable'
                health-check:
                    -
                        _dynamic-server:
                            type: str
                        addr-mode:
                            type: str
                            description: 'Address mode (IPv4 or IPv6).'
                            choices:
                                - 'ipv4'
                                - 'ipv6'
                        failtime:
                            type: int
                            description: 'Number of failures before server is considered lost (1 - 3600, default = 5).'
                        http-agent:
                            type: str
                            description: 'String in the http-agent field in the HTTP header.'
                        http-get:
                            type: str
                            description: 'URL used to communicate with the server if the protocol if the protocol is HTTP.'
                        http-match:
                            type: str
                            description: 'Response string expected from the server if the protocol is HTTP.'
                        interval:
                            type: int
                            description: 'Status check interval, or the time between attempting to connect to the server (1 - 3600 sec, default = 5).'
                        members:
                            type: str
                            description: 'Member sequence number list.'
                        name:
                            type: str
                            description: 'Status check or health check name.'
                        packet-size:
                            type: int
                            description: 'Packet size of a twamp test session,'
                        password:
                            -
                                type: str
                        port:
                            type: int
                            description: 'Port number used to communicate with the server over the selected protocol.'
                        protocol:
                            type: str
                            description: 'Protocol used to determine if the FortiGate can communicate with the server.'
                            choices:
                                - 'ping'
                                - 'tcp-echo'
                                - 'udp-echo'
                                - 'http'
                                - 'twamp'
                                - 'ping6'
                        recoverytime:
                            type: int
                            description: 'Number of successful responses received before server is considered recovered (1 - 3600, default = 5).'
                        security-mode:
                            type: str
                            description: 'Twamp controller security mode.'
                            choices:
                                - 'none'
                                - 'authentication'
                        server:
                            -
                                type: str
                        sla:
                            -
                                id:
                                    type: int
                                    description: 'SLA ID.'
                                jitter-threshold:
                                    type: int
                                    description: 'Jitter for SLA to make decision in milliseconds. (0 - 10000000, default = 5).'
                                latency-threshold:
                                    type: int
                                    description: 'Latency for SLA to make decision in milliseconds. (0 - 10000000, default = 5).'
                                link-cost-factor:
                                    -
                                        type: str
                                        choices:
                                            - 'latency'
                                            - 'jitter'
                                            - 'packet-loss'
                                packetloss-threshold:
                                    type: int
                                    description: 'Packet loss for SLA to make decision in percentage. (0 - 100, default = 0).'
                        threshold-alert-jitter:
                            type: int
                            description: 'Alert threshold for jitter (ms, default = 0).'
                        threshold-alert-latency:
                            type: int
                            description: 'Alert threshold for latency (ms, default = 0).'
                        threshold-alert-packetloss:
                            type: int
                            description: 'Alert threshold for packet loss (percentage, default = 0).'
                        threshold-warning-jitter:
                            type: int
                            description: 'Warning threshold for jitter (ms, default = 0).'
                        threshold-warning-latency:
                            type: int
                            description: 'Warning threshold for latency (ms, default = 0).'
                        threshold-warning-packetloss:
                            type: int
                            description: 'Warning threshold for packet loss (percentage, default = 0).'
                        update-cascade-interface:
                            type: str
                            description: 'Enable/disable update cascade interface.'
                            choices:
                                - 'disable'
                                - 'enable'
                        update-static-route:
                            type: str
                            description: 'Enable/disable updating the static route.'
                            choices:
                                - 'disable'
                                - 'enable'
                load-balance-mode:
                    type: str
                    description: 'Algorithm or mode to use for load balancing Internet traffic to SD-WAN members.'
                    choices:
                        - 'source-ip-based'
                        - 'weight-based'
                        - 'usage-based'
                        - 'source-dest-ip-based'
                        - 'measured-volume-based'
                members:
                    -
                        _dynamic-member:
                            type: str
                        comment:
                            type: str
                            description: 'Comments.'
                        gateway:
                            type: str
                            description: 'The default gateway for this interface. Usually the default gateway of the Internet service provider that this int...'
                        gateway6:
                            type: str
                            description: 'IPv6 gateway.'
                        ingress-spillover-threshold:
                            type: int
                            description: 'Ingress spillover threshold for this interface (0 - 16776000 kbit/s). When this traffic volume threshold is reache...'
                        interface:
                            type: str
                            description: 'Interface name.'
                        priority:
                            type: int
                            description: 'Priority of the interface (0 - 4294967295). Used for SD-WAN rules or priority rules.'
                        seq-num:
                            type: int
                            description: 'Sequence number(1-255).'
                        source:
                            type: str
                            description: 'Source IP address used in the health-check packet to the server.'
                        source6:
                            type: str
                            description: 'Source IPv6 address used in the health-check packet to the server.'
                        spillover-threshold:
                            type: int
                            description: 'Egress spillover threshold for this interface (0 - 16776000 kbit/s). When this traffic volume threshold is reached...'
                        status:
                            type: str
                            description: 'Enable/disable this interface in the SD-WAN.'
                            choices:
                                - 'disable'
                                - 'enable'
                        volume-ratio:
                            type: int
                            description: 'Measured volume ratio (this value / sum of all values = percentage of link volume, 0 - 255).'
                        weight:
                            type: int
                            description: 'Weight of this interface for weighted load balancing. (0 - 255) More traffic is directed to interfaces with higher...'
                service:
                    -
                        addr-mode:
                            type: str
                            description: 'Address mode (IPv4 or IPv6).'
                            choices:
                                - 'ipv4'
                                - 'ipv6'
                        bandwidth-weight:
                            type: int
                            description: 'Coefficient of reciprocal of available bidirectional bandwidth in the formula of custom-profile-1.'
                        default:
                            type: str
                            description: 'Enable/disable use of SD-WAN as default service.'
                            choices:
                                - 'disable'
                                - 'enable'
                        dscp-forward:
                            type: str
                            description: 'Enable/disable forward traffic DSCP tag.'
                            choices:
                                - 'disable'
                                - 'enable'
                        dscp-forward-tag:
                            type: str
                            description: 'Forward traffic DSCP tag.'
                        dscp-reverse:
                            type: str
                            description: 'Enable/disable reverse traffic DSCP tag.'
                            choices:
                                - 'disable'
                                - 'enable'
                        dscp-reverse-tag:
                            type: str
                            description: 'Reverse traffic DSCP tag.'
                        dst:
                            type: str
                            description: 'Destination address name.'
                        dst-negate:
                            type: str
                            description: 'Enable/disable negation of destination address match.'
                            choices:
                                - 'disable'
                                - 'enable'
                        dst6:
                            type: str
                            description: 'Destination address6 name.'
                        end-port:
                            type: int
                            description: 'End destination port number.'
                        gateway:
                            type: str
                            description: 'Enable/disable SD-WAN service gateway.'
                            choices:
                                - 'disable'
                                - 'enable'
                        groups:
                            type: str
                            description: 'User groups.'
                        health-check:
                            type: str
                            description: 'Health check.'
                        hold-down-time:
                            type: int
                            description: 'Waiting period in seconds when switching from the back-up member to the primary member (0 - 10000000, default = 0).'
                        id:
                            type: int
                            description: 'Priority rule ID (1 - 4000).'
                        internet-service:
                            type: str
                            description: 'Enable/disable use of Internet service for application-based load balancing.'
                            choices:
                                - 'disable'
                                - 'enable'
                        internet-service-ctrl:
                            -
                                type: int
                        internet-service-ctrl-group:
                            type: str
                            description: 'Control-based Internet Service group list.'
                        internet-service-custom:
                            type: str
                            description: 'Custom Internet service name list.'
                        internet-service-custom-group:
                            type: str
                            description: 'Custom Internet Service group list.'
                        internet-service-group:
                            type: str
                            description: 'Internet Service group list.'
                        internet-service-id:
                            type: str
                            description: 'Internet service ID list.'
                        jitter-weight:
                            type: int
                            description: 'Coefficient of jitter in the formula of custom-profile-1.'
                        latency-weight:
                            type: int
                            description: 'Coefficient of latency in the formula of custom-profile-1.'
                        link-cost-factor:
                            type: str
                            description: 'Link cost factor.'
                            choices:
                                - 'latency'
                                - 'jitter'
                                - 'packet-loss'
                                - 'inbandwidth'
                                - 'outbandwidth'
                                - 'bibandwidth'
                                - 'custom-profile-1'
                        link-cost-threshold:
                            type: int
                            description: 'Percentage threshold change of link cost values that will result in policy route regeneration (0 - 10000000, defau...'
                        member:
                            type: str
                            description: 'Member sequence number.'
                        mode:
                            type: str
                            description: 'Control how the priority rule sets the priority of interfaces in the SD-WAN.'
                            choices:
                                - 'auto'
                                - 'manual'
                                - 'priority'
                                - 'sla'
                                - 'load-balance'
                        name:
                            type: str
                            description: 'Priority rule name.'
                        packet-loss-weight:
                            type: int
                            description: 'Coefficient of packet-loss in the formula of custom-profile-1.'
                        priority-members:
                            type: str
                            description: 'Member sequence number list.'
                        protocol:
                            type: int
                            description: 'Protocol number.'
                        quality-link:
                            type: int
                            description: 'Quality grade.'
                        route-tag:
                            type: int
                            description: 'IPv4 route map route-tag.'
                        sla:
                            -
                                health-check:
                                    type: str
                                    description: 'Virtual WAN Link health-check.'
                                id:
                                    type: int
                                    description: 'SLA ID.'
                        src:
                            type: str
                            description: 'Source address name.'
                        src-negate:
                            type: str
                            description: 'Enable/disable negation of source address match.'
                            choices:
                                - 'disable'
                                - 'enable'
                        src6:
                            type: str
                            description: 'Source address6 name.'
                        start-port:
                            type: int
                            description: 'Start destination port number.'
                        status:
                            type: str
                            description: 'Enable/disable SD-WAN service.'
                            choices:
                                - 'disable'
                                - 'enable'
                        tos:
                            type: str
                            description: 'Type of service bit pattern.'
                        tos-mask:
                            type: str
                            description: 'Type of service evaluated bits.'
                        users:
                            type: str
                            description: 'User name.'
                status:
                    type: str
                    description: 'Enable/disable SD-WAN.'
                    choices:
                        - 'disable'
                        - 'enable'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/WANPROF/{WANPROF}/SYSTEM/VIRTUAL-WAN-LINK
      fmgr_wanprof_system_virtualwanlink:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wanprof: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/WANPROF/{WANPROF}/SYSTEM/VIRTUAL-WAN-LINK
      fmgr_wanprof_system_virtualwanlink:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
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

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            fail-detect:
               type: str
               description: 'Enable/disable SD-WAN Internet connection status checking (failure detection).'
            health-check:
               type: array
               suboptions:
                  _dynamic-server:
                     type: str
                  addr-mode:
                     type: str
                     description: 'Address mode (IPv4 or IPv6).'
                  failtime:
                     type: int
                     description: 'Number of failures before server is considered lost (1 - 3600, default = 5).'
                  http-agent:
                     type: str
                     description: 'String in the http-agent field in the HTTP header.'
                  http-get:
                     type: str
                     description: 'URL used to communicate with the server if the protocol if the protocol is HTTP.'
                  http-match:
                     type: str
                     description: 'Response string expected from the server if the protocol is HTTP.'
                  interval:
                     type: int
                     description: 'Status check interval, or the time between attempting to connect to the server (1 - 3600 sec, default = 5).'
                  members:
                     type: str
                     description: 'Member sequence number list.'
                  name:
                     type: str
                     description: 'Status check or health check name.'
                  packet-size:
                     type: int
                     description: 'Packet size of a twamp test session,'
                  password:
                     type: array
                     suboptions:
                        type: str
                  port:
                     type: int
                     description: 'Port number used to communicate with the server over the selected protocol.'
                  protocol:
                     type: str
                     description: 'Protocol used to determine if the FortiGate can communicate with the server.'
                  recoverytime:
                     type: int
                     description: 'Number of successful responses received before server is considered recovered (1 - 3600, default = 5).'
                  security-mode:
                     type: str
                     description: 'Twamp controller security mode.'
                  server:
                     type: array
                     suboptions:
                        type: str
                  sla:
                     type: array
                     suboptions:
                        id:
                           type: int
                           description: 'SLA ID.'
                        jitter-threshold:
                           type: int
                           description: 'Jitter for SLA to make decision in milliseconds. (0 - 10000000, default = 5).'
                        latency-threshold:
                           type: int
                           description: 'Latency for SLA to make decision in milliseconds. (0 - 10000000, default = 5).'
                        link-cost-factor:
                           type: array
                           suboptions:
                              type: str
                        packetloss-threshold:
                           type: int
                           description: 'Packet loss for SLA to make decision in percentage. (0 - 100, default = 0).'
                  threshold-alert-jitter:
                     type: int
                     description: 'Alert threshold for jitter (ms, default = 0).'
                  threshold-alert-latency:
                     type: int
                     description: 'Alert threshold for latency (ms, default = 0).'
                  threshold-alert-packetloss:
                     type: int
                     description: 'Alert threshold for packet loss (percentage, default = 0).'
                  threshold-warning-jitter:
                     type: int
                     description: 'Warning threshold for jitter (ms, default = 0).'
                  threshold-warning-latency:
                     type: int
                     description: 'Warning threshold for latency (ms, default = 0).'
                  threshold-warning-packetloss:
                     type: int
                     description: 'Warning threshold for packet loss (percentage, default = 0).'
                  update-cascade-interface:
                     type: str
                     description: 'Enable/disable update cascade interface.'
                  update-static-route:
                     type: str
                     description: 'Enable/disable updating the static route.'
            load-balance-mode:
               type: str
               description: 'Algorithm or mode to use for load balancing Internet traffic to SD-WAN members.'
            members:
               type: array
               suboptions:
                  _dynamic-member:
                     type: str
                  comment:
                     type: str
                     description: 'Comments.'
                  gateway:
                     type: str
                     description: 'The default gateway for this interface. Usually the default gateway of the Internet service provider that this interface ...'
                  gateway6:
                     type: str
                     description: 'IPv6 gateway.'
                  ingress-spillover-threshold:
                     type: int
                     description: 'Ingress spillover threshold for this interface (0 - 16776000 kbit/s). When this traffic volume threshold is reached, new ...'
                  interface:
                     type: str
                     description: 'Interface name.'
                  priority:
                     type: int
                     description: 'Priority of the interface (0 - 4294967295). Used for SD-WAN rules or priority rules.'
                  seq-num:
                     type: int
                     description: 'Sequence number(1-255).'
                  source:
                     type: str
                     description: 'Source IP address used in the health-check packet to the server.'
                  source6:
                     type: str
                     description: 'Source IPv6 address used in the health-check packet to the server.'
                  spillover-threshold:
                     type: int
                     description: 'Egress spillover threshold for this interface (0 - 16776000 kbit/s). When this traffic volume threshold is reached, new s...'
                  status:
                     type: str
                     description: 'Enable/disable this interface in the SD-WAN.'
                  volume-ratio:
                     type: int
                     description: 'Measured volume ratio (this value / sum of all values = percentage of link volume, 0 - 255).'
                  weight:
                     type: int
                     description: 'Weight of this interface for weighted load balancing. (0 - 255) More traffic is directed to interfaces with higher weights.'
            service:
               type: array
               suboptions:
                  addr-mode:
                     type: str
                     description: 'Address mode (IPv4 or IPv6).'
                  bandwidth-weight:
                     type: int
                     description: 'Coefficient of reciprocal of available bidirectional bandwidth in the formula of custom-profile-1.'
                  default:
                     type: str
                     description: 'Enable/disable use of SD-WAN as default service.'
                  dscp-forward:
                     type: str
                     description: 'Enable/disable forward traffic DSCP tag.'
                  dscp-forward-tag:
                     type: str
                     description: 'Forward traffic DSCP tag.'
                  dscp-reverse:
                     type: str
                     description: 'Enable/disable reverse traffic DSCP tag.'
                  dscp-reverse-tag:
                     type: str
                     description: 'Reverse traffic DSCP tag.'
                  dst:
                     type: str
                     description: 'Destination address name.'
                  dst-negate:
                     type: str
                     description: 'Enable/disable negation of destination address match.'
                  dst6:
                     type: str
                     description: 'Destination address6 name.'
                  end-port:
                     type: int
                     description: 'End destination port number.'
                  gateway:
                     type: str
                     description: 'Enable/disable SD-WAN service gateway.'
                  groups:
                     type: str
                     description: 'User groups.'
                  health-check:
                     type: str
                     description: 'Health check.'
                  hold-down-time:
                     type: int
                     description: 'Waiting period in seconds when switching from the back-up member to the primary member (0 - 10000000, default = 0).'
                  id:
                     type: int
                     description: 'Priority rule ID (1 - 4000).'
                  internet-service:
                     type: str
                     description: 'Enable/disable use of Internet service for application-based load balancing.'
                  internet-service-ctrl:
                     type: array
                     suboptions:
                        type: int
                  internet-service-ctrl-group:
                     type: str
                     description: 'Control-based Internet Service group list.'
                  internet-service-custom:
                     type: str
                     description: 'Custom Internet service name list.'
                  internet-service-custom-group:
                     type: str
                     description: 'Custom Internet Service group list.'
                  internet-service-group:
                     type: str
                     description: 'Internet Service group list.'
                  internet-service-id:
                     type: str
                     description: 'Internet service ID list.'
                  jitter-weight:
                     type: int
                     description: 'Coefficient of jitter in the formula of custom-profile-1.'
                  latency-weight:
                     type: int
                     description: 'Coefficient of latency in the formula of custom-profile-1.'
                  link-cost-factor:
                     type: str
                     description: 'Link cost factor.'
                  link-cost-threshold:
                     type: int
                     description: 'Percentage threshold change of link cost values that will result in policy route regeneration (0 - 10000000, default = 10).'
                  member:
                     type: str
                     description: 'Member sequence number.'
                  mode:
                     type: str
                     description: 'Control how the priority rule sets the priority of interfaces in the SD-WAN.'
                  name:
                     type: str
                     description: 'Priority rule name.'
                  packet-loss-weight:
                     type: int
                     description: 'Coefficient of packet-loss in the formula of custom-profile-1.'
                  priority-members:
                     type: str
                     description: 'Member sequence number list.'
                  protocol:
                     type: int
                     description: 'Protocol number.'
                  quality-link:
                     type: int
                     description: 'Quality grade.'
                  route-tag:
                     type: int
                     description: 'IPv4 route map route-tag.'
                  sla:
                     type: array
                     suboptions:
                        health-check:
                           type: str
                           description: 'Virtual WAN Link health-check.'
                        id:
                           type: int
                           description: 'SLA ID.'
                  src:
                     type: str
                     description: 'Source address name.'
                  src-negate:
                     type: str
                     description: 'Enable/disable negation of source address match.'
                  src6:
                     type: str
                     description: 'Source address6 name.'
                  start-port:
                     type: int
                     description: 'Start destination port number.'
                  status:
                     type: str
                     description: 'Enable/disable SD-WAN service.'
                  tos:
                     type: str
                     description: 'Type of service bit pattern.'
                  tos-mask:
                     type: str
                     description: 'Type of service evaluated bits.'
                  users:
                     type: str
                     description: 'User name.'
            status:
               type: str
               description: 'Enable/disable SD-WAN.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link'
return_of_api_category_0:
   description: items returned for method:[set, update]
   returned: always
   suboptions:
      id:
         type: int
      result:
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link'

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FAIL_SOCKET_MSG
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import DEFAULT_RESULT_OBJ
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FMGRCommon
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FMGBaseException
from ansible_collections.fortinet.fortimanager.plugins.module_utils.fortimanager import FortiManagerHandler


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'wanprof',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'object member',
                            'chksum',
                            'datasrc'
                        ]
                    },
                    'api_tag': 0
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object1': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'fail-detect': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'health-check': {
                            'type': 'array',
                            'items': {
                                '_dynamic-server': {
                                    'type': 'string'
                                },
                                'addr-mode': {
                                    'type': 'string',
                                    'enum': [
                                        'ipv4',
                                        'ipv6'
                                    ]
                                },
                                'failtime': {
                                    'type': 'integer'
                                },
                                'http-agent': {
                                    'type': 'string'
                                },
                                'http-get': {
                                    'type': 'string'
                                },
                                'http-match': {
                                    'type': 'string'
                                },
                                'interval': {
                                    'type': 'integer'
                                },
                                'members': {
                                    'type': 'string'
                                },
                                'name': {
                                    'type': 'string'
                                },
                                'packet-size': {
                                    'type': 'integer'
                                },
                                'password': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                },
                                'port': {
                                    'type': 'integer'
                                },
                                'protocol': {
                                    'type': 'string',
                                    'enum': [
                                        'ping',
                                        'tcp-echo',
                                        'udp-echo',
                                        'http',
                                        'twamp',
                                        'ping6'
                                    ]
                                },
                                'recoverytime': {
                                    'type': 'integer'
                                },
                                'security-mode': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'authentication'
                                    ]
                                },
                                'server': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                },
                                'sla': {
                                    'type': 'array',
                                    'items': {
                                        'id': {
                                            'type': 'integer'
                                        },
                                        'jitter-threshold': {
                                            'type': 'integer'
                                        },
                                        'latency-threshold': {
                                            'type': 'integer'
                                        },
                                        'link-cost-factor': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'string',
                                                'enum': [
                                                    'latency',
                                                    'jitter',
                                                    'packet-loss'
                                                ]
                                            }
                                        },
                                        'packetloss-threshold': {
                                            'type': 'integer'
                                        }
                                    }
                                },
                                'threshold-alert-jitter': {
                                    'type': 'integer'
                                },
                                'threshold-alert-latency': {
                                    'type': 'integer'
                                },
                                'threshold-alert-packetloss': {
                                    'type': 'integer'
                                },
                                'threshold-warning-jitter': {
                                    'type': 'integer'
                                },
                                'threshold-warning-latency': {
                                    'type': 'integer'
                                },
                                'threshold-warning-packetloss': {
                                    'type': 'integer'
                                },
                                'update-cascade-interface': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'update-static-route': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                }
                            }
                        },
                        'load-balance-mode': {
                            'type': 'string',
                            'enum': [
                                'source-ip-based',
                                'weight-based',
                                'usage-based',
                                'source-dest-ip-based',
                                'measured-volume-based'
                            ]
                        },
                        'members': {
                            'type': 'array',
                            'items': {
                                '_dynamic-member': {
                                    'type': 'string'
                                },
                                'comment': {
                                    'type': 'string'
                                },
                                'gateway': {
                                    'type': 'string'
                                },
                                'gateway6': {
                                    'type': 'string'
                                },
                                'ingress-spillover-threshold': {
                                    'type': 'integer'
                                },
                                'interface': {
                                    'type': 'string'
                                },
                                'priority': {
                                    'type': 'integer'
                                },
                                'seq-num': {
                                    'type': 'integer'
                                },
                                'source': {
                                    'type': 'string'
                                },
                                'source6': {
                                    'type': 'string'
                                },
                                'spillover-threshold': {
                                    'type': 'integer'
                                },
                                'status': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'volume-ratio': {
                                    'type': 'integer'
                                },
                                'weight': {
                                    'type': 'integer'
                                }
                            }
                        },
                        'service': {
                            'type': 'array',
                            'items': {
                                'addr-mode': {
                                    'type': 'string',
                                    'enum': [
                                        'ipv4',
                                        'ipv6'
                                    ]
                                },
                                'bandwidth-weight': {
                                    'type': 'integer'
                                },
                                'default': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'dscp-forward': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'dscp-forward-tag': {
                                    'type': 'string'
                                },
                                'dscp-reverse': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'dscp-reverse-tag': {
                                    'type': 'string'
                                },
                                'dst': {
                                    'type': 'string'
                                },
                                'dst-negate': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'dst6': {
                                    'type': 'string'
                                },
                                'end-port': {
                                    'type': 'integer'
                                },
                                'gateway': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'groups': {
                                    'type': 'string'
                                },
                                'health-check': {
                                    'type': 'string'
                                },
                                'hold-down-time': {
                                    'type': 'integer'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'internet-service': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'internet-service-ctrl': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'integer'
                                    }
                                },
                                'internet-service-ctrl-group': {
                                    'type': 'string'
                                },
                                'internet-service-custom': {
                                    'type': 'string'
                                },
                                'internet-service-custom-group': {
                                    'type': 'string'
                                },
                                'internet-service-group': {
                                    'type': 'string'
                                },
                                'internet-service-id': {
                                    'type': 'string'
                                },
                                'jitter-weight': {
                                    'type': 'integer'
                                },
                                'latency-weight': {
                                    'type': 'integer'
                                },
                                'link-cost-factor': {
                                    'type': 'string',
                                    'enum': [
                                        'latency',
                                        'jitter',
                                        'packet-loss',
                                        'inbandwidth',
                                        'outbandwidth',
                                        'bibandwidth',
                                        'custom-profile-1'
                                    ]
                                },
                                'link-cost-threshold': {
                                    'type': 'integer'
                                },
                                'member': {
                                    'type': 'string'
                                },
                                'mode': {
                                    'type': 'string',
                                    'enum': [
                                        'auto',
                                        'manual',
                                        'priority',
                                        'sla',
                                        'load-balance'
                                    ]
                                },
                                'name': {
                                    'type': 'string'
                                },
                                'packet-loss-weight': {
                                    'type': 'integer'
                                },
                                'priority-members': {
                                    'type': 'string'
                                },
                                'protocol': {
                                    'type': 'integer'
                                },
                                'quality-link': {
                                    'type': 'integer'
                                },
                                'route-tag': {
                                    'type': 'integer'
                                },
                                'sla': {
                                    'type': 'array',
                                    'items': {
                                        'health-check': {
                                            'type': 'string'
                                        },
                                        'id': {
                                            'type': 'integer'
                                        }
                                    }
                                },
                                'src': {
                                    'type': 'string'
                                },
                                'src-negate': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'src6': {
                                    'type': 'string'
                                },
                                'start-port': {
                                    'type': 'integer'
                                },
                                'status': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'tos': {
                                    'type': 'string'
                                },
                                'tos-mask': {
                                    'type': 'string'
                                },
                                'users': {
                                    'type': 'string'
                                }
                            }
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        }
                    },
                    'api_tag': 0
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ]
        },
        'method_mapping': {
            'get': 'object0',
            'set': 'object1',
            'update': 'object1'
        }
    }

    module_arg_spec = {
        'loose_validation': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'workspace_locking_adom': {
            'type': 'str',
            'required': False
        },
        'workspace_locking_timeout': {
            'type': 'int',
            'required': False,
            'default': 300
        },
        'params': {
            'type': 'list',
            'required': False
        },
        'method': {
            'type': 'str',
            'required': True,
            'choices': [
                'get',
                'set',
                'update'
            ]
        },
        'url_params': {
            'type': 'dict',
            'required': False
        }
    }
    module = AnsibleModule(argument_spec=module_arg_spec,
                           supports_check_mode=False)
    method = module.params['method']
    loose_validation = module.params['loose_validation']

    fmgr = None
    payload = None
    response = DEFAULT_RESULT_OBJ

    if module._socket_path:
        connection = Connection(module._socket_path)
        tools = FMGRCommon()
        if loose_validation == False:
            tools.validate_module_params(module, body_schema)
        tools.validate_module_url_params(module, jrpc_urls, url_schema)
        full_url = tools.get_full_url_path(module, jrpc_urls)
        payload = tools.get_full_payload(module, full_url)
        fmgr = FortiManagerHandler(connection, module)
        fmgr.tools = tools
    else:
        module.fail_json(**FAIL_SOCKET_MSG)

    try:
        response = fmgr._conn.send_request(method, payload)
        fmgr.govern_response(module=module, results=response,
                             msg='Operation Finished',
                             ansible_facts=fmgr.construct_ansible_facts(response, module.params, module.params))
    except Exception as e:
        raise FMGBaseException(e)

    module.exit_json(meta=response[1])


if __name__ == '__main__':
    main()
