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
module: fmgr_fsp_vlan_interface
short_description: no description
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/interface
    - /pm/config/global/obj/fsp/vlan/{vlan}/interface
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
            vlan:
                type: str
    schema_object0:
        methods: [get]
        description: ''
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
        description: ''
        api_categories: [api_tag0]
        api_tag0:
            data:
                ac-name:
                    type: str
                aggregate:
                    type: str
                algorithm:
                    type: str
                    choices:
                        - 'L2'
                        - 'L3'
                        - 'L4'
                alias:
                    type: str
                allowaccess:
                    -
                        type: str
                        choices:
                            - 'https'
                            - 'ping'
                            - 'ssh'
                            - 'snmp'
                            - 'http'
                            - 'telnet'
                            - 'fgfm'
                            - 'auto-ipsec'
                            - 'radius-acct'
                            - 'probe-response'
                            - 'capwap'
                            - 'dnp'
                            - 'ftm'
                ap-discover:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                arpforward:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                atm-protocol:
                    type: str
                    choices:
                        - 'none'
                        - 'ipoa'
                auth-type:
                    type: str
                    choices:
                        - 'auto'
                        - 'pap'
                        - 'chap'
                        - 'mschapv1'
                        - 'mschapv2'
                auto-auth-extension-device:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                bfd:
                    type: str
                    choices:
                        - 'global'
                        - 'enable'
                        - 'disable'
                bfd-desired-min-tx:
                    type: int
                bfd-detect-mult:
                    type: int
                bfd-required-min-rx:
                    type: int
                broadcast-forticlient-discovery:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                broadcast-forward:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                captive-portal:
                    type: int
                cli-conn-status:
                    type: int
                color:
                    type: int
                ddns:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ddns-auth:
                    type: str
                    choices:
                        - 'disable'
                        - 'tsig'
                ddns-domain:
                    type: str
                ddns-key:
                    type: str
                ddns-keyname:
                    type: str
                ddns-password:
                    -
                        type: str
                ddns-server:
                    type: str
                    choices:
                        - 'dhs.org'
                        - 'dyndns.org'
                        - 'dyns.net'
                        - 'tzo.com'
                        - 'ods.org'
                        - 'vavic.com'
                        - 'now.net.cn'
                        - 'dipdns.net'
                        - 'easydns.com'
                        - 'genericDDNS'
                ddns-server-ip:
                    type: str
                ddns-sn:
                    type: str
                ddns-ttl:
                    type: int
                ddns-username:
                    type: str
                ddns-zone:
                    type: str
                dedicated-to:
                    type: str
                    choices:
                        - 'none'
                        - 'management'
                defaultgw:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                description:
                    type: str
                detected-peer-mtu:
                    type: int
                detectprotocol:
                    -
                        type: str
                        choices:
                            - 'ping'
                            - 'tcp-echo'
                            - 'udp-echo'
                detectserver:
                    type: str
                device-access-list:
                    type: str
                device-identification:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                device-identification-active-scan:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                device-netscan:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                device-user-identification:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                devindex:
                    type: int
                dhcp-client-identifier:
                    type: str
                dhcp-relay-agent-option:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                dhcp-relay-ip:
                    -
                        type: str
                dhcp-relay-service:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                dhcp-relay-type:
                    type: str
                    choices:
                        - 'regular'
                        - 'ipsec'
                dhcp-renew-time:
                    type: int
                disc-retry-timeout:
                    type: int
                disconnect-threshold:
                    type: int
                distance:
                    type: int
                dns-query:
                    type: str
                    choices:
                        - 'disable'
                        - 'recursive'
                        - 'non-recursive'
                dns-server-override:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                drop-fragment:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                drop-overlapped-fragment:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                egress-cos:
                    type: str
                    choices:
                        - 'disable'
                        - 'cos0'
                        - 'cos1'
                        - 'cos2'
                        - 'cos3'
                        - 'cos4'
                        - 'cos5'
                        - 'cos6'
                        - 'cos7'
                egress-shaping-profile:
                    type: str
                endpoint-compliance:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                estimated-downstream-bandwidth:
                    type: int
                estimated-upstream-bandwidth:
                    type: int
                explicit-ftp-proxy:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                explicit-web-proxy:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                external:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                fail-action-on-extender:
                    type: str
                    choices:
                        - 'soft-restart'
                        - 'hard-restart'
                        - 'reboot'
                fail-alert-interfaces:
                    type: str
                fail-alert-method:
                    type: str
                    choices:
                        - 'link-failed-signal'
                        - 'link-down'
                fail-detect:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                fail-detect-option:
                    -
                        type: str
                        choices:
                            - 'detectserver'
                            - 'link-down'
                fdp:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                fortiheartbeat:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                fortilink:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                fortilink-backup-link:
                    type: int
                fortilink-split-interface:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                fortilink-stacking:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                forward-domain:
                    type: int
                forward-error-correction:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                        - 'rs-fec'
                        - 'base-r-fec'
                fp-anomaly:
                    -
                        type: str
                        choices:
                            - 'drop_tcp_fin_noack'
                            - 'pass_winnuke'
                            - 'pass_tcpland'
                            - 'pass_udpland'
                            - 'pass_icmpland'
                            - 'pass_ipland'
                            - 'pass_iprr'
                            - 'pass_ipssrr'
                            - 'pass_iplsrr'
                            - 'pass_ipstream'
                            - 'pass_ipsecurity'
                            - 'pass_iptimestamp'
                            - 'pass_ipunknown_option'
                            - 'pass_ipunknown_prot'
                            - 'pass_icmp_frag'
                            - 'pass_tcp_no_flag'
                            - 'pass_tcp_fin_noack'
                            - 'drop_winnuke'
                            - 'drop_tcpland'
                            - 'drop_udpland'
                            - 'drop_icmpland'
                            - 'drop_ipland'
                            - 'drop_iprr'
                            - 'drop_ipssrr'
                            - 'drop_iplsrr'
                            - 'drop_ipstream'
                            - 'drop_ipsecurity'
                            - 'drop_iptimestamp'
                            - 'drop_ipunknown_option'
                            - 'drop_ipunknown_prot'
                            - 'drop_icmp_frag'
                            - 'drop_tcp_no_flag'
                fp-disable:
                    -
                        type: str
                        choices:
                            - 'all'
                            - 'ipsec'
                            - 'none'
                gateway-address:
                    type: str
                gi-gk:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                gwaddr:
                    type: str
                gwdetect:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ha-priority:
                    type: int
                icmp-accept-redirect:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                icmp-redirect:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                icmp-send-redirect:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ident-accept:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                idle-timeout:
                    type: int
                if-mdix:
                    type: str
                    choices:
                        - 'auto'
                        - 'normal'
                        - 'crossover'
                if-media:
                    type: str
                    choices:
                        - 'auto'
                        - 'copper'
                        - 'fiber'
                in-force-vlan-cos:
                    type: int
                inbandwidth:
                    type: int
                ingress-cos:
                    type: str
                    choices:
                        - 'disable'
                        - 'cos0'
                        - 'cos1'
                        - 'cos2'
                        - 'cos3'
                        - 'cos4'
                        - 'cos5'
                        - 'cos6'
                        - 'cos7'
                ingress-spillover-threshold:
                    type: int
                internal:
                    type: int
                ip:
                    type: str
                ipmac:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ips-sniffer-mode:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ipunnumbered:
                    type: str
                ipv6:
                    autoconf:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    dhcp6-client-options:
                        -
                            type: str
                            choices:
                                - 'rapid'
                                - 'iapd'
                                - 'iana'
                                - 'dns'
                                - 'dnsname'
                    dhcp6-information-request:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    dhcp6-prefix-delegation:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    dhcp6-prefix-hint:
                        type: str
                    dhcp6-prefix-hint-plt:
                        type: int
                    dhcp6-prefix-hint-vlt:
                        type: int
                    dhcp6-relay-ip:
                        type: str
                    dhcp6-relay-service:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    dhcp6-relay-type:
                        type: str
                        choices:
                            - 'regular'
                    ip6-address:
                        type: str
                    ip6-allowaccess:
                        -
                            type: str
                            choices:
                                - 'https'
                                - 'ping'
                                - 'ssh'
                                - 'snmp'
                                - 'http'
                                - 'telnet'
                                - 'fgfm'
                                - 'capwap'
                    ip6-default-life:
                        type: int
                    ip6-dns-server-override:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    ip6-hop-limit:
                        type: int
                    ip6-link-mtu:
                        type: int
                    ip6-manage-flag:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    ip6-max-interval:
                        type: int
                    ip6-min-interval:
                        type: int
                    ip6-mode:
                        type: str
                        choices:
                            - 'static'
                            - 'dhcp'
                            - 'pppoe'
                            - 'delegated'
                    ip6-other-flag:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    ip6-reachable-time:
                        type: int
                    ip6-retrans-time:
                        type: int
                    ip6-send-adv:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    ip6-subnet:
                        type: str
                    ip6-upstream-interface:
                        type: str
                    nd-cert:
                        type: str
                    nd-cga-modifier:
                        type: str
                    nd-mode:
                        type: str
                        choices:
                            - 'basic'
                            - 'SEND-compatible'
                    nd-security-level:
                        type: int
                    nd-timestamp-delta:
                        type: int
                    nd-timestamp-fuzz:
                        type: int
                    vrip6_link_local:
                        type: str
                    vrrp-virtual-mac6:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                l2forward:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                l2tp-client:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                lacp-ha-slave:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                lacp-mode:
                    type: str
                    choices:
                        - 'static'
                        - 'passive'
                        - 'active'
                lacp-speed:
                    type: str
                    choices:
                        - 'slow'
                        - 'fast'
                lcp-echo-interval:
                    type: int
                lcp-max-echo-fails:
                    type: int
                link-up-delay:
                    type: int
                listen-forticlient-connection:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                lldp-network-policy:
                    type: str
                lldp-reception:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                        - 'vdom'
                lldp-transmission:
                    type: str
                    choices:
                        - 'enable'
                        - 'disable'
                        - 'vdom'
                log:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                macaddr:
                    type: str
                management-ip:
                    type: str
                max-egress-burst-rate:
                    type: int
                max-egress-rate:
                    type: int
                mediatype:
                    type: str
                    choices:
                        - 'serdes-sfp'
                        - 'sgmii-sfp'
                        - 'cfp2-sr10'
                        - 'cfp2-lr4'
                        - 'serdes-copper-sfp'
                        - 'sr'
                        - 'cr'
                        - 'lr'
                        - 'qsfp28-sr4'
                        - 'qsfp28-lr4'
                        - 'qsfp28-cr4'
                member:
                    type: str
                min-links:
                    type: int
                min-links-down:
                    type: str
                    choices:
                        - 'operational'
                        - 'administrative'
                mode:
                    type: str
                    choices:
                        - 'static'
                        - 'dhcp'
                        - 'pppoe'
                        - 'pppoa'
                        - 'ipoa'
                        - 'eoa'
                mtu:
                    type: int
                mtu-override:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                mux-type:
                    type: str
                    choices:
                        - 'llc-encaps'
                        - 'vc-encaps'
                name:
                    type: str
                ndiscforward:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                netbios-forward:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                netflow-sampler:
                    type: str
                    choices:
                        - 'disable'
                        - 'tx'
                        - 'rx'
                        - 'both'
                npu-fastpath:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                nst:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                out-force-vlan-cos:
                    type: int
                outbandwidth:
                    type: int
                padt-retry-timeout:
                    type: int
                password:
                    -
                        type: str
                peer-interface:
                    type: str
                phy-mode:
                    type: str
                    choices:
                        - 'auto'
                        - 'adsl'
                        - 'vdsl'
                ping-serv-status:
                    type: int
                poe:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                polling-interval:
                    type: int
                pppoe-unnumbered-negotiate:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                pptp-auth-type:
                    type: str
                    choices:
                        - 'auto'
                        - 'pap'
                        - 'chap'
                        - 'mschapv1'
                        - 'mschapv2'
                pptp-client:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                pptp-password:
                    -
                        type: str
                pptp-server-ip:
                    type: str
                pptp-timeout:
                    type: int
                pptp-user:
                    type: str
                preserve-session-route:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                priority:
                    type: int
                priority-override:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                proxy-captive-portal:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                redundant-interface:
                    type: str
                remote-ip:
                    type: str
                replacemsg-override-group:
                    type: str
                retransmission:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                role:
                    type: str
                    choices:
                        - 'lan'
                        - 'wan'
                        - 'dmz'
                        - 'undefined'
                sample-direction:
                    type: str
                    choices:
                        - 'rx'
                        - 'tx'
                        - 'both'
                sample-rate:
                    type: int
                scan-botnet-connections:
                    type: str
                    choices:
                        - 'disable'
                        - 'block'
                        - 'monitor'
                secondary-IP:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                secondaryip:
                    -
                        allowaccess:
                            -
                                type: str
                                choices:
                                    - 'https'
                                    - 'ping'
                                    - 'ssh'
                                    - 'snmp'
                                    - 'http'
                                    - 'telnet'
                                    - 'fgfm'
                                    - 'auto-ipsec'
                                    - 'radius-acct'
                                    - 'probe-response'
                                    - 'capwap'
                                    - 'dnp'
                                    - 'ftm'
                        detectprotocol:
                            -
                                type: str
                                choices:
                                    - 'ping'
                                    - 'tcp-echo'
                                    - 'udp-echo'
                        detectserver:
                            type: str
                        gwdetect:
                            type: str
                            choices:
                                - 'disable'
                                - 'enable'
                        ha-priority:
                            type: int
                        id:
                            type: int
                        ip:
                            type: str
                        ping-serv-status:
                            type: int
                        seq:
                            type: int
                security-8021x-dynamic-vlan-id:
                    type: int
                security-8021x-master:
                    type: str
                security-8021x-mode:
                    type: str
                    choices:
                        - 'default'
                        - 'dynamic-vlan'
                        - 'fallback'
                        - 'slave'
                security-exempt-list:
                    type: str
                security-external-logout:
                    type: str
                security-external-web:
                    type: str
                security-groups:
                    type: str
                security-mac-auth-bypass:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                        - 'mac-auth-only'
                security-mode:
                    type: str
                    choices:
                        - 'none'
                        - 'captive-portal'
                        - '802.1X'
                security-redirect-url:
                    type: str
                service-name:
                    type: str
                sflow-sampler:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                speed:
                    type: str
                    choices:
                        - 'auto'
                        - '10full'
                        - '10half'
                        - '100full'
                        - '100half'
                        - '1000full'
                        - '1000half'
                        - '10000full'
                        - '1000auto'
                        - '10000auto'
                        - '40000full'
                        - '100Gfull'
                        - '25000full'
                        - '40000auto'
                        - '25000auto'
                        - '100Gauto'
                spillover-threshold:
                    type: int
                src-check:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                status:
                    type: str
                    choices:
                        - 'down'
                        - 'up'
                stp:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                stp-ha-slave:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                        - 'priority-adjust'
                stpforward:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                stpforward-mode:
                    type: str
                    choices:
                        - 'rpl-all-ext-id'
                        - 'rpl-bridge-ext-id'
                        - 'rpl-nothing'
                strip-priority-vlan-tag:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                subst:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                substitute-dst-mac:
                    type: str
                switch:
                    type: str
                switch-controller-access-vlan:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                switch-controller-arp-inspection:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                switch-controller-auth:
                    type: str
                    choices:
                        - 'radius'
                        - 'usergroup'
                switch-controller-dhcp-snooping:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                switch-controller-dhcp-snooping-option82:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                switch-controller-dhcp-snooping-verify-mac:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                switch-controller-igmp-snooping:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                switch-controller-learning-limit:
                    type: int
                switch-controller-radius-server:
                    type: str
                switch-controller-traffic-policy:
                    type: str
                tc-mode:
                    type: str
                    choices:
                        - 'ptm'
                        - 'atm'
                tcp-mss:
                    type: int
                trunk:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                trust-ip-1:
                    type: str
                trust-ip-2:
                    type: str
                trust-ip-3:
                    type: str
                trust-ip6-1:
                    type: str
                trust-ip6-2:
                    type: str
                trust-ip6-3:
                    type: str
                type:
                    type: str
                    choices:
                        - 'physical'
                        - 'vlan'
                        - 'aggregate'
                        - 'redundant'
                        - 'tunnel'
                        - 'wireless'
                        - 'vdom-link'
                        - 'loopback'
                        - 'switch'
                        - 'hard-switch'
                        - 'hdlc'
                        - 'vap-switch'
                        - 'wl-mesh'
                        - 'fortilink'
                        - 'switch-vlan'
                        - 'fctrl-trunk'
                        - 'tdm'
                        - 'fext-wan'
                        - 'vxlan'
                        - 'emac-vlan'
                username:
                    type: str
                vci:
                    type: int
                vectoring:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                vindex:
                    type: int
                vlanforward:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                vlanid:
                    type: int
                vpi:
                    type: int
                vrf:
                    type: int
                vrrp:
                    -
                        accept-mode:
                            type: str
                            choices:
                                - 'disable'
                                - 'enable'
                        adv-interval:
                            type: int
                        ignore-default-route:
                            type: str
                            choices:
                                - 'disable'
                                - 'enable'
                        preempt:
                            type: str
                            choices:
                                - 'disable'
                                - 'enable'
                        priority:
                            type: int
                        start-time:
                            type: int
                        status:
                            type: str
                            choices:
                                - 'disable'
                                - 'enable'
                        version:
                            type: str
                            choices:
                                - '2'
                                - '3'
                        vrdst:
                            -
                                type: str
                        vrdst-priority:
                            type: int
                        vrgrp:
                            type: int
                        vrid:
                            type: int
                        vrip:
                            type: str
                vrrp-virtual-mac:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                wccp:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                weight:
                    type: int
                wifi-5g-threshold:
                    type: str
                wifi-acl:
                    type: str
                    choices:
                        - 'deny'
                        - 'allow'
                wifi-ap-band:
                    type: str
                    choices:
                        - 'any'
                        - '5g-preferred'
                        - '5g-only'
                wifi-auth:
                    type: str
                    choices:
                        - 'PSK'
                        - 'RADIUS'
                        - 'radius'
                        - 'usergroup'
                wifi-auto-connect:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                wifi-auto-save:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                wifi-broadcast-ssid:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                wifi-encrypt:
                    type: str
                    choices:
                        - 'TKIP'
                        - 'AES'
                wifi-fragment-threshold:
                    type: int
                wifi-key:
                    -
                        type: str
                wifi-keyindex:
                    type: int
                wifi-mac-filter:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                wifi-passphrase:
                    -
                        type: str
                wifi-radius-server:
                    type: str
                wifi-rts-threshold:
                    type: int
                wifi-security:
                    type: str
                    choices:
                        - 'None'
                        - 'WEP64'
                        - 'wep64'
                        - 'WEP128'
                        - 'wep128'
                        - 'WPA_PSK'
                        - 'WPA_RADIUS'
                        - 'WPA'
                        - 'WPA2'
                        - 'WPA2_AUTO'
                        - 'open'
                        - 'wpa-personal'
                        - 'wpa-enterprise'
                        - 'wpa-only-personal'
                        - 'wpa-only-enterprise'
                        - 'wpa2-only-personal'
                        - 'wpa2-only-enterprise'
                wifi-ssid:
                    type: str
                wifi-usergroup:
                    type: str
                wins-ip:
                    type: str

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

    - name: REQUESTING /PM/CONFIG/OBJ/FSP/VLAN/{VLAN}/INTERFACE
      fmgr_fsp_vlan_interface:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vlan: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/FSP/VLAN/{VLAN}/INTERFACE
      fmgr_fsp_vlan_interface:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vlan: <value of string>
         params:
            -
               data:
                  ac-name: <value of string>
                  aggregate: <value of string>
                  algorithm: <value in [L2, L3, L4]>
                  alias: <value of string>
                  allowaccess:
                    - <value in [https, ping, ssh, ...]>
                  ap-discover: <value in [disable, enable]>
                  arpforward: <value in [disable, enable]>
                  atm-protocol: <value in [none, ipoa]>
                  auth-type: <value in [auto, pap, chap, ...]>
                  auto-auth-extension-device: <value in [disable, enable]>
                  bfd: <value in [global, enable, disable]>
                  bfd-desired-min-tx: <value of integer>
                  bfd-detect-mult: <value of integer>
                  bfd-required-min-rx: <value of integer>
                  broadcast-forticlient-discovery: <value in [disable, enable]>
                  broadcast-forward: <value in [disable, enable]>
                  captive-portal: <value of integer>
                  cli-conn-status: <value of integer>
                  color: <value of integer>
                  ddns: <value in [disable, enable]>
                  ddns-auth: <value in [disable, tsig]>
                  ddns-domain: <value of string>
                  ddns-key: <value of string>
                  ddns-keyname: <value of string>
                  ddns-password:
                    - <value of string>
                  ddns-server: <value in [dhs.org, dyndns.org, dyns.net, ...]>
                  ddns-server-ip: <value of string>
                  ddns-sn: <value of string>
                  ddns-ttl: <value of integer>
                  ddns-username: <value of string>
                  ddns-zone: <value of string>
                  dedicated-to: <value in [none, management]>
                  defaultgw: <value in [disable, enable]>
                  description: <value of string>
                  detected-peer-mtu: <value of integer>
                  detectprotocol:
                    - <value in [ping, tcp-echo, udp-echo]>
                  detectserver: <value of string>
                  device-access-list: <value of string>
                  device-identification: <value in [disable, enable]>
                  device-identification-active-scan: <value in [disable, enable]>
                  device-netscan: <value in [disable, enable]>
                  device-user-identification: <value in [disable, enable]>
                  devindex: <value of integer>
                  dhcp-client-identifier: <value of string>
                  dhcp-relay-agent-option: <value in [disable, enable]>
                  dhcp-relay-ip:
                    - <value of string>
                  dhcp-relay-service: <value in [disable, enable]>
                  dhcp-relay-type: <value in [regular, ipsec]>
                  dhcp-renew-time: <value of integer>
                  disc-retry-timeout: <value of integer>
                  disconnect-threshold: <value of integer>
                  distance: <value of integer>
                  dns-query: <value in [disable, recursive, non-recursive]>
                  dns-server-override: <value in [disable, enable]>
                  drop-fragment: <value in [disable, enable]>
                  drop-overlapped-fragment: <value in [disable, enable]>
                  egress-cos: <value in [disable, cos0, cos1, ...]>
                  egress-shaping-profile: <value of string>
                  endpoint-compliance: <value in [disable, enable]>
                  estimated-downstream-bandwidth: <value of integer>
                  estimated-upstream-bandwidth: <value of integer>
                  explicit-ftp-proxy: <value in [disable, enable]>
                  explicit-web-proxy: <value in [disable, enable]>
                  external: <value in [disable, enable]>
                  fail-action-on-extender: <value in [soft-restart, hard-restart, reboot]>
                  fail-alert-interfaces: <value of string>
                  fail-alert-method: <value in [link-failed-signal, link-down]>
                  fail-detect: <value in [disable, enable]>
                  fail-detect-option:
                    - <value in [detectserver, link-down]>
                  fdp: <value in [disable, enable]>
                  fortiheartbeat: <value in [disable, enable]>
                  fortilink: <value in [disable, enable]>
                  fortilink-backup-link: <value of integer>
                  fortilink-split-interface: <value in [disable, enable]>
                  fortilink-stacking: <value in [disable, enable]>
                  forward-domain: <value of integer>
                  forward-error-correction: <value in [disable, enable, rs-fec, ...]>
                  fp-anomaly:
                    - <value in [drop_tcp_fin_noack, pass_winnuke, pass_tcpland, ...]>
                  fp-disable:
                    - <value in [all, ipsec, none]>
                  gateway-address: <value of string>
                  gi-gk: <value in [disable, enable]>
                  gwaddr: <value of string>
                  gwdetect: <value in [disable, enable]>
                  ha-priority: <value of integer>
                  icmp-accept-redirect: <value in [disable, enable]>
                  icmp-redirect: <value in [disable, enable]>
                  icmp-send-redirect: <value in [disable, enable]>
                  ident-accept: <value in [disable, enable]>
                  idle-timeout: <value of integer>
                  if-mdix: <value in [auto, normal, crossover]>
                  if-media: <value in [auto, copper, fiber]>
                  in-force-vlan-cos: <value of integer>
                  inbandwidth: <value of integer>
                  ingress-cos: <value in [disable, cos0, cos1, ...]>
                  ingress-spillover-threshold: <value of integer>
                  internal: <value of integer>
                  ip: <value of string>
                  ipmac: <value in [disable, enable]>
                  ips-sniffer-mode: <value in [disable, enable]>
                  ipunnumbered: <value of string>
                  ipv6:
                     autoconf: <value in [disable, enable]>
                     dhcp6-client-options:
                       - <value in [rapid, iapd, iana, ...]>
                     dhcp6-information-request: <value in [disable, enable]>
                     dhcp6-prefix-delegation: <value in [disable, enable]>
                     dhcp6-prefix-hint: <value of string>
                     dhcp6-prefix-hint-plt: <value of integer>
                     dhcp6-prefix-hint-vlt: <value of integer>
                     dhcp6-relay-ip: <value of string>
                     dhcp6-relay-service: <value in [disable, enable]>
                     dhcp6-relay-type: <value in [regular]>
                     ip6-address: <value of string>
                     ip6-allowaccess:
                       - <value in [https, ping, ssh, ...]>
                     ip6-default-life: <value of integer>
                     ip6-dns-server-override: <value in [disable, enable]>
                     ip6-hop-limit: <value of integer>
                     ip6-link-mtu: <value of integer>
                     ip6-manage-flag: <value in [disable, enable]>
                     ip6-max-interval: <value of integer>
                     ip6-min-interval: <value of integer>
                     ip6-mode: <value in [static, dhcp, pppoe, ...]>
                     ip6-other-flag: <value in [disable, enable]>
                     ip6-reachable-time: <value of integer>
                     ip6-retrans-time: <value of integer>
                     ip6-send-adv: <value in [disable, enable]>
                     ip6-subnet: <value of string>
                     ip6-upstream-interface: <value of string>
                     nd-cert: <value of string>
                     nd-cga-modifier: <value of string>
                     nd-mode: <value in [basic, SEND-compatible]>
                     nd-security-level: <value of integer>
                     nd-timestamp-delta: <value of integer>
                     nd-timestamp-fuzz: <value of integer>
                     vrip6_link_local: <value of string>
                     vrrp-virtual-mac6: <value in [disable, enable]>
                  l2forward: <value in [disable, enable]>
                  l2tp-client: <value in [disable, enable]>
                  lacp-ha-slave: <value in [disable, enable]>
                  lacp-mode: <value in [static, passive, active]>
                  lacp-speed: <value in [slow, fast]>
                  lcp-echo-interval: <value of integer>
                  lcp-max-echo-fails: <value of integer>
                  link-up-delay: <value of integer>
                  listen-forticlient-connection: <value in [disable, enable]>
                  lldp-network-policy: <value of string>
                  lldp-reception: <value in [disable, enable, vdom]>
                  lldp-transmission: <value in [enable, disable, vdom]>
                  log: <value in [disable, enable]>
                  macaddr: <value of string>
                  management-ip: <value of string>
                  max-egress-burst-rate: <value of integer>
                  max-egress-rate: <value of integer>
                  mediatype: <value in [serdes-sfp, sgmii-sfp, cfp2-sr10, ...]>
                  member: <value of string>
                  min-links: <value of integer>
                  min-links-down: <value in [operational, administrative]>
                  mode: <value in [static, dhcp, pppoe, ...]>
                  mtu: <value of integer>
                  mtu-override: <value in [disable, enable]>
                  mux-type: <value in [llc-encaps, vc-encaps]>
                  name: <value of string>
                  ndiscforward: <value in [disable, enable]>
                  netbios-forward: <value in [disable, enable]>
                  netflow-sampler: <value in [disable, tx, rx, ...]>
                  npu-fastpath: <value in [disable, enable]>
                  nst: <value in [disable, enable]>
                  out-force-vlan-cos: <value of integer>
                  outbandwidth: <value of integer>
                  padt-retry-timeout: <value of integer>
                  password:
                    - <value of string>
                  peer-interface: <value of string>
                  phy-mode: <value in [auto, adsl, vdsl]>
                  ping-serv-status: <value of integer>
                  poe: <value in [disable, enable]>
                  polling-interval: <value of integer>
                  pppoe-unnumbered-negotiate: <value in [disable, enable]>
                  pptp-auth-type: <value in [auto, pap, chap, ...]>
                  pptp-client: <value in [disable, enable]>
                  pptp-password:
                    - <value of string>
                  pptp-server-ip: <value of string>
                  pptp-timeout: <value of integer>
                  pptp-user: <value of string>
                  preserve-session-route: <value in [disable, enable]>
                  priority: <value of integer>
                  priority-override: <value in [disable, enable]>
                  proxy-captive-portal: <value in [disable, enable]>
                  redundant-interface: <value of string>
                  remote-ip: <value of string>
                  replacemsg-override-group: <value of string>
                  retransmission: <value in [disable, enable]>
                  role: <value in [lan, wan, dmz, ...]>
                  sample-direction: <value in [rx, tx, both]>
                  sample-rate: <value of integer>
                  scan-botnet-connections: <value in [disable, block, monitor]>
                  secondary-IP: <value in [disable, enable]>
                  secondaryip:
                    -
                        allowaccess:
                          - <value in [https, ping, ssh, ...]>
                        detectprotocol:
                          - <value in [ping, tcp-echo, udp-echo]>
                        detectserver: <value of string>
                        gwdetect: <value in [disable, enable]>
                        ha-priority: <value of integer>
                        id: <value of integer>
                        ip: <value of string>
                        ping-serv-status: <value of integer>
                        seq: <value of integer>
                  security-8021x-dynamic-vlan-id: <value of integer>
                  security-8021x-master: <value of string>
                  security-8021x-mode: <value in [default, dynamic-vlan, fallback, ...]>
                  security-exempt-list: <value of string>
                  security-external-logout: <value of string>
                  security-external-web: <value of string>
                  security-groups: <value of string>
                  security-mac-auth-bypass: <value in [disable, enable, mac-auth-only]>
                  security-mode: <value in [none, captive-portal, 802.1X]>
                  security-redirect-url: <value of string>
                  service-name: <value of string>
                  sflow-sampler: <value in [disable, enable]>
                  speed: <value in [auto, 10full, 10half, ...]>
                  spillover-threshold: <value of integer>
                  src-check: <value in [disable, enable]>
                  status: <value in [down, up]>
                  stp: <value in [disable, enable]>
                  stp-ha-slave: <value in [disable, enable, priority-adjust]>
                  stpforward: <value in [disable, enable]>
                  stpforward-mode: <value in [rpl-all-ext-id, rpl-bridge-ext-id, rpl-nothing]>
                  strip-priority-vlan-tag: <value in [disable, enable]>
                  subst: <value in [disable, enable]>
                  substitute-dst-mac: <value of string>
                  switch: <value of string>
                  switch-controller-access-vlan: <value in [disable, enable]>
                  switch-controller-arp-inspection: <value in [disable, enable]>
                  switch-controller-auth: <value in [radius, usergroup]>
                  switch-controller-dhcp-snooping: <value in [disable, enable]>
                  switch-controller-dhcp-snooping-option82: <value in [disable, enable]>
                  switch-controller-dhcp-snooping-verify-mac: <value in [disable, enable]>
                  switch-controller-igmp-snooping: <value in [disable, enable]>
                  switch-controller-learning-limit: <value of integer>
                  switch-controller-radius-server: <value of string>
                  switch-controller-traffic-policy: <value of string>
                  tc-mode: <value in [ptm, atm]>
                  tcp-mss: <value of integer>
                  trunk: <value in [disable, enable]>
                  trust-ip-1: <value of string>
                  trust-ip-2: <value of string>
                  trust-ip-3: <value of string>
                  trust-ip6-1: <value of string>
                  trust-ip6-2: <value of string>
                  trust-ip6-3: <value of string>
                  type: <value in [physical, vlan, aggregate, ...]>
                  username: <value of string>
                  vci: <value of integer>
                  vectoring: <value in [disable, enable]>
                  vindex: <value of integer>
                  vlanforward: <value in [disable, enable]>
                  vlanid: <value of integer>
                  vpi: <value of integer>
                  vrf: <value of integer>
                  vrrp:
                    -
                        accept-mode: <value in [disable, enable]>
                        adv-interval: <value of integer>
                        ignore-default-route: <value in [disable, enable]>
                        preempt: <value in [disable, enable]>
                        priority: <value of integer>
                        start-time: <value of integer>
                        status: <value in [disable, enable]>
                        version: <value in [2, 3]>
                        vrdst:
                          - <value of string>
                        vrdst-priority: <value of integer>
                        vrgrp: <value of integer>
                        vrid: <value of integer>
                        vrip: <value of string>
                  vrrp-virtual-mac: <value in [disable, enable]>
                  wccp: <value in [disable, enable]>
                  weight: <value of integer>
                  wifi-5g-threshold: <value of string>
                  wifi-acl: <value in [deny, allow]>
                  wifi-ap-band: <value in [any, 5g-preferred, 5g-only]>
                  wifi-auth: <value in [PSK, RADIUS, radius, ...]>
                  wifi-auto-connect: <value in [disable, enable]>
                  wifi-auto-save: <value in [disable, enable]>
                  wifi-broadcast-ssid: <value in [disable, enable]>
                  wifi-encrypt: <value in [TKIP, AES]>
                  wifi-fragment-threshold: <value of integer>
                  wifi-key:
                    - <value of string>
                  wifi-keyindex: <value of integer>
                  wifi-mac-filter: <value in [disable, enable]>
                  wifi-passphrase:
                    - <value of string>
                  wifi-radius-server: <value of string>
                  wifi-rts-threshold: <value of integer>
                  wifi-security: <value in [None, WEP64, wep64, ...]>
                  wifi-ssid: <value of string>
                  wifi-usergroup: <value of string>
                  wins-ip: <value of string>

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
            ac-name:
               type: str
            aggregate:
               type: str
            algorithm:
               type: str
            alias:
               type: str
            allowaccess:
               type: array
               suboptions:
                  type: str
            ap-discover:
               type: str
            arpforward:
               type: str
            atm-protocol:
               type: str
            auth-type:
               type: str
            auto-auth-extension-device:
               type: str
            bfd:
               type: str
            bfd-desired-min-tx:
               type: int
            bfd-detect-mult:
               type: int
            bfd-required-min-rx:
               type: int
            broadcast-forticlient-discovery:
               type: str
            broadcast-forward:
               type: str
            captive-portal:
               type: int
            cli-conn-status:
               type: int
            color:
               type: int
            ddns:
               type: str
            ddns-auth:
               type: str
            ddns-domain:
               type: str
            ddns-key:
               type: str
            ddns-keyname:
               type: str
            ddns-password:
               type: array
               suboptions:
                  type: str
            ddns-server:
               type: str
            ddns-server-ip:
               type: str
            ddns-sn:
               type: str
            ddns-ttl:
               type: int
            ddns-username:
               type: str
            ddns-zone:
               type: str
            dedicated-to:
               type: str
            defaultgw:
               type: str
            description:
               type: str
            detected-peer-mtu:
               type: int
            detectprotocol:
               type: array
               suboptions:
                  type: str
            detectserver:
               type: str
            device-access-list:
               type: str
            device-identification:
               type: str
            device-identification-active-scan:
               type: str
            device-netscan:
               type: str
            device-user-identification:
               type: str
            devindex:
               type: int
            dhcp-client-identifier:
               type: str
            dhcp-relay-agent-option:
               type: str
            dhcp-relay-ip:
               type: array
               suboptions:
                  type: str
            dhcp-relay-service:
               type: str
            dhcp-relay-type:
               type: str
            dhcp-renew-time:
               type: int
            disc-retry-timeout:
               type: int
            disconnect-threshold:
               type: int
            distance:
               type: int
            dns-query:
               type: str
            dns-server-override:
               type: str
            drop-fragment:
               type: str
            drop-overlapped-fragment:
               type: str
            egress-cos:
               type: str
            egress-shaping-profile:
               type: str
            endpoint-compliance:
               type: str
            estimated-downstream-bandwidth:
               type: int
            estimated-upstream-bandwidth:
               type: int
            explicit-ftp-proxy:
               type: str
            explicit-web-proxy:
               type: str
            external:
               type: str
            fail-action-on-extender:
               type: str
            fail-alert-interfaces:
               type: str
            fail-alert-method:
               type: str
            fail-detect:
               type: str
            fail-detect-option:
               type: array
               suboptions:
                  type: str
            fdp:
               type: str
            fortiheartbeat:
               type: str
            fortilink:
               type: str
            fortilink-backup-link:
               type: int
            fortilink-split-interface:
               type: str
            fortilink-stacking:
               type: str
            forward-domain:
               type: int
            forward-error-correction:
               type: str
            fp-anomaly:
               type: array
               suboptions:
                  type: str
            fp-disable:
               type: array
               suboptions:
                  type: str
            gateway-address:
               type: str
            gi-gk:
               type: str
            gwaddr:
               type: str
            gwdetect:
               type: str
            ha-priority:
               type: int
            icmp-accept-redirect:
               type: str
            icmp-redirect:
               type: str
            icmp-send-redirect:
               type: str
            ident-accept:
               type: str
            idle-timeout:
               type: int
            if-mdix:
               type: str
            if-media:
               type: str
            in-force-vlan-cos:
               type: int
            inbandwidth:
               type: int
            ingress-cos:
               type: str
            ingress-spillover-threshold:
               type: int
            internal:
               type: int
            ip:
               type: str
            ipmac:
               type: str
            ips-sniffer-mode:
               type: str
            ipunnumbered:
               type: str
            ipv6:
               autoconf:
                  type: str
               dhcp6-client-options:
                  type: array
                  suboptions:
                     type: str
               dhcp6-information-request:
                  type: str
               dhcp6-prefix-delegation:
                  type: str
               dhcp6-prefix-hint:
                  type: str
               dhcp6-prefix-hint-plt:
                  type: int
               dhcp6-prefix-hint-vlt:
                  type: int
               dhcp6-relay-ip:
                  type: str
               dhcp6-relay-service:
                  type: str
               dhcp6-relay-type:
                  type: str
               ip6-address:
                  type: str
               ip6-allowaccess:
                  type: array
                  suboptions:
                     type: str
               ip6-default-life:
                  type: int
               ip6-dns-server-override:
                  type: str
               ip6-hop-limit:
                  type: int
               ip6-link-mtu:
                  type: int
               ip6-manage-flag:
                  type: str
               ip6-max-interval:
                  type: int
               ip6-min-interval:
                  type: int
               ip6-mode:
                  type: str
               ip6-other-flag:
                  type: str
               ip6-reachable-time:
                  type: int
               ip6-retrans-time:
                  type: int
               ip6-send-adv:
                  type: str
               ip6-subnet:
                  type: str
               ip6-upstream-interface:
                  type: str
               nd-cert:
                  type: str
               nd-cga-modifier:
                  type: str
               nd-mode:
                  type: str
               nd-security-level:
                  type: int
               nd-timestamp-delta:
                  type: int
               nd-timestamp-fuzz:
                  type: int
               vrip6_link_local:
                  type: str
               vrrp-virtual-mac6:
                  type: str
            l2forward:
               type: str
            l2tp-client:
               type: str
            lacp-ha-slave:
               type: str
            lacp-mode:
               type: str
            lacp-speed:
               type: str
            lcp-echo-interval:
               type: int
            lcp-max-echo-fails:
               type: int
            link-up-delay:
               type: int
            listen-forticlient-connection:
               type: str
            lldp-network-policy:
               type: str
            lldp-reception:
               type: str
            lldp-transmission:
               type: str
            log:
               type: str
            macaddr:
               type: str
            management-ip:
               type: str
            max-egress-burst-rate:
               type: int
            max-egress-rate:
               type: int
            mediatype:
               type: str
            member:
               type: str
            min-links:
               type: int
            min-links-down:
               type: str
            mode:
               type: str
            mtu:
               type: int
            mtu-override:
               type: str
            mux-type:
               type: str
            name:
               type: str
            ndiscforward:
               type: str
            netbios-forward:
               type: str
            netflow-sampler:
               type: str
            npu-fastpath:
               type: str
            nst:
               type: str
            out-force-vlan-cos:
               type: int
            outbandwidth:
               type: int
            padt-retry-timeout:
               type: int
            password:
               type: array
               suboptions:
                  type: str
            peer-interface:
               type: str
            phy-mode:
               type: str
            ping-serv-status:
               type: int
            poe:
               type: str
            polling-interval:
               type: int
            pppoe-unnumbered-negotiate:
               type: str
            pptp-auth-type:
               type: str
            pptp-client:
               type: str
            pptp-password:
               type: array
               suboptions:
                  type: str
            pptp-server-ip:
               type: str
            pptp-timeout:
               type: int
            pptp-user:
               type: str
            preserve-session-route:
               type: str
            priority:
               type: int
            priority-override:
               type: str
            proxy-captive-portal:
               type: str
            redundant-interface:
               type: str
            remote-ip:
               type: str
            replacemsg-override-group:
               type: str
            retransmission:
               type: str
            role:
               type: str
            sample-direction:
               type: str
            sample-rate:
               type: int
            scan-botnet-connections:
               type: str
            secondary-IP:
               type: str
            secondaryip:
               type: array
               suboptions:
                  allowaccess:
                     type: array
                     suboptions:
                        type: str
                  detectprotocol:
                     type: array
                     suboptions:
                        type: str
                  detectserver:
                     type: str
                  gwdetect:
                     type: str
                  ha-priority:
                     type: int
                  id:
                     type: int
                  ip:
                     type: str
                  ping-serv-status:
                     type: int
                  seq:
                     type: int
            security-8021x-dynamic-vlan-id:
               type: int
            security-8021x-master:
               type: str
            security-8021x-mode:
               type: str
            security-exempt-list:
               type: str
            security-external-logout:
               type: str
            security-external-web:
               type: str
            security-groups:
               type: str
            security-mac-auth-bypass:
               type: str
            security-mode:
               type: str
            security-redirect-url:
               type: str
            service-name:
               type: str
            sflow-sampler:
               type: str
            speed:
               type: str
            spillover-threshold:
               type: int
            src-check:
               type: str
            status:
               type: str
            stp:
               type: str
            stp-ha-slave:
               type: str
            stpforward:
               type: str
            stpforward-mode:
               type: str
            strip-priority-vlan-tag:
               type: str
            subst:
               type: str
            substitute-dst-mac:
               type: str
            switch:
               type: str
            switch-controller-access-vlan:
               type: str
            switch-controller-arp-inspection:
               type: str
            switch-controller-auth:
               type: str
            switch-controller-dhcp-snooping:
               type: str
            switch-controller-dhcp-snooping-option82:
               type: str
            switch-controller-dhcp-snooping-verify-mac:
               type: str
            switch-controller-igmp-snooping:
               type: str
            switch-controller-learning-limit:
               type: int
            switch-controller-radius-server:
               type: str
            switch-controller-traffic-policy:
               type: str
            tc-mode:
               type: str
            tcp-mss:
               type: int
            trunk:
               type: str
            trust-ip-1:
               type: str
            trust-ip-2:
               type: str
            trust-ip-3:
               type: str
            trust-ip6-1:
               type: str
            trust-ip6-2:
               type: str
            trust-ip6-3:
               type: str
            type:
               type: str
            username:
               type: str
            vci:
               type: int
            vectoring:
               type: str
            vindex:
               type: int
            vlanforward:
               type: str
            vlanid:
               type: int
            vpi:
               type: int
            vrf:
               type: int
            vrrp:
               type: array
               suboptions:
                  accept-mode:
                     type: str
                  adv-interval:
                     type: int
                  ignore-default-route:
                     type: str
                  preempt:
                     type: str
                  priority:
                     type: int
                  start-time:
                     type: int
                  status:
                     type: str
                  version:
                     type: str
                  vrdst:
                     type: array
                     suboptions:
                        type: str
                  vrdst-priority:
                     type: int
                  vrgrp:
                     type: int
                  vrid:
                     type: int
                  vrip:
                     type: str
            vrrp-virtual-mac:
               type: str
            wccp:
               type: str
            weight:
               type: int
            wifi-5g-threshold:
               type: str
            wifi-acl:
               type: str
            wifi-ap-band:
               type: str
            wifi-auth:
               type: str
            wifi-auto-connect:
               type: str
            wifi-auto-save:
               type: str
            wifi-broadcast-ssid:
               type: str
            wifi-encrypt:
               type: str
            wifi-fragment-threshold:
               type: int
            wifi-key:
               type: array
               suboptions:
                  type: str
            wifi-keyindex:
               type: int
            wifi-mac-filter:
               type: str
            wifi-passphrase:
               type: array
               suboptions:
                  type: str
            wifi-radius-server:
               type: str
            wifi-rts-threshold:
               type: int
            wifi-security:
               type: str
            wifi-ssid:
               type: str
            wifi-usergroup:
               type: str
            wins-ip:
               type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/interface'
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
            example: '/pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/interface'

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
        '/pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/interface',
        '/pm/config/global/obj/fsp/vlan/{vlan}/interface'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'vlan',
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
                        'ac-name': {
                            'type': 'string'
                        },
                        'aggregate': {
                            'type': 'string'
                        },
                        'algorithm': {
                            'type': 'string',
                            'enum': [
                                'L2',
                                'L3',
                                'L4'
                            ]
                        },
                        'alias': {
                            'type': 'string'
                        },
                        'allowaccess': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'https',
                                    'ping',
                                    'ssh',
                                    'snmp',
                                    'http',
                                    'telnet',
                                    'fgfm',
                                    'auto-ipsec',
                                    'radius-acct',
                                    'probe-response',
                                    'capwap',
                                    'dnp',
                                    'ftm'
                                ]
                            }
                        },
                        'ap-discover': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'arpforward': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'atm-protocol': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'ipoa'
                            ]
                        },
                        'auth-type': {
                            'type': 'string',
                            'enum': [
                                'auto',
                                'pap',
                                'chap',
                                'mschapv1',
                                'mschapv2'
                            ]
                        },
                        'auto-auth-extension-device': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'bfd': {
                            'type': 'string',
                            'enum': [
                                'global',
                                'enable',
                                'disable'
                            ]
                        },
                        'bfd-desired-min-tx': {
                            'type': 'integer'
                        },
                        'bfd-detect-mult': {
                            'type': 'integer'
                        },
                        'bfd-required-min-rx': {
                            'type': 'integer'
                        },
                        'broadcast-forticlient-discovery': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'broadcast-forward': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'captive-portal': {
                            'type': 'integer'
                        },
                        'cli-conn-status': {
                            'type': 'integer'
                        },
                        'color': {
                            'type': 'integer'
                        },
                        'ddns': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ddns-auth': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'tsig'
                            ]
                        },
                        'ddns-domain': {
                            'type': 'string'
                        },
                        'ddns-key': {
                            'type': 'string'
                        },
                        'ddns-keyname': {
                            'type': 'string'
                        },
                        'ddns-password': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'ddns-server': {
                            'type': 'string',
                            'enum': [
                                'dhs.org',
                                'dyndns.org',
                                'dyns.net',
                                'tzo.com',
                                'ods.org',
                                'vavic.com',
                                'now.net.cn',
                                'dipdns.net',
                                'easydns.com',
                                'genericDDNS'
                            ]
                        },
                        'ddns-server-ip': {
                            'type': 'string'
                        },
                        'ddns-sn': {
                            'type': 'string'
                        },
                        'ddns-ttl': {
                            'type': 'integer'
                        },
                        'ddns-username': {
                            'type': 'string'
                        },
                        'ddns-zone': {
                            'type': 'string'
                        },
                        'dedicated-to': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'management'
                            ]
                        },
                        'defaultgw': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'description': {
                            'type': 'string'
                        },
                        'detected-peer-mtu': {
                            'type': 'integer'
                        },
                        'detectprotocol': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'ping',
                                    'tcp-echo',
                                    'udp-echo'
                                ]
                            }
                        },
                        'detectserver': {
                            'type': 'string'
                        },
                        'device-access-list': {
                            'type': 'string'
                        },
                        'device-identification': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'device-identification-active-scan': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'device-netscan': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'device-user-identification': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'devindex': {
                            'type': 'integer'
                        },
                        'dhcp-client-identifier': {
                            'type': 'string'
                        },
                        'dhcp-relay-agent-option': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dhcp-relay-ip': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'dhcp-relay-service': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dhcp-relay-type': {
                            'type': 'string',
                            'enum': [
                                'regular',
                                'ipsec'
                            ]
                        },
                        'dhcp-renew-time': {
                            'type': 'integer'
                        },
                        'disc-retry-timeout': {
                            'type': 'integer'
                        },
                        'disconnect-threshold': {
                            'type': 'integer'
                        },
                        'distance': {
                            'type': 'integer'
                        },
                        'dns-query': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'recursive',
                                'non-recursive'
                            ]
                        },
                        'dns-server-override': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'drop-fragment': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'drop-overlapped-fragment': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'egress-cos': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'cos0',
                                'cos1',
                                'cos2',
                                'cos3',
                                'cos4',
                                'cos5',
                                'cos6',
                                'cos7'
                            ]
                        },
                        'egress-shaping-profile': {
                            'type': 'string'
                        },
                        'endpoint-compliance': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'estimated-downstream-bandwidth': {
                            'type': 'integer'
                        },
                        'estimated-upstream-bandwidth': {
                            'type': 'integer'
                        },
                        'explicit-ftp-proxy': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'explicit-web-proxy': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'external': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fail-action-on-extender': {
                            'type': 'string',
                            'enum': [
                                'soft-restart',
                                'hard-restart',
                                'reboot'
                            ]
                        },
                        'fail-alert-interfaces': {
                            'type': 'string'
                        },
                        'fail-alert-method': {
                            'type': 'string',
                            'enum': [
                                'link-failed-signal',
                                'link-down'
                            ]
                        },
                        'fail-detect': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fail-detect-option': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'detectserver',
                                    'link-down'
                                ]
                            }
                        },
                        'fdp': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fortiheartbeat': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fortilink': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fortilink-backup-link': {
                            'type': 'integer'
                        },
                        'fortilink-split-interface': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fortilink-stacking': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'forward-domain': {
                            'type': 'integer'
                        },
                        'forward-error-correction': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable',
                                'rs-fec',
                                'base-r-fec'
                            ]
                        },
                        'fp-anomaly': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'drop_tcp_fin_noack',
                                    'pass_winnuke',
                                    'pass_tcpland',
                                    'pass_udpland',
                                    'pass_icmpland',
                                    'pass_ipland',
                                    'pass_iprr',
                                    'pass_ipssrr',
                                    'pass_iplsrr',
                                    'pass_ipstream',
                                    'pass_ipsecurity',
                                    'pass_iptimestamp',
                                    'pass_ipunknown_option',
                                    'pass_ipunknown_prot',
                                    'pass_icmp_frag',
                                    'pass_tcp_no_flag',
                                    'pass_tcp_fin_noack',
                                    'drop_winnuke',
                                    'drop_tcpland',
                                    'drop_udpland',
                                    'drop_icmpland',
                                    'drop_ipland',
                                    'drop_iprr',
                                    'drop_ipssrr',
                                    'drop_iplsrr',
                                    'drop_ipstream',
                                    'drop_ipsecurity',
                                    'drop_iptimestamp',
                                    'drop_ipunknown_option',
                                    'drop_ipunknown_prot',
                                    'drop_icmp_frag',
                                    'drop_tcp_no_flag'
                                ]
                            }
                        },
                        'fp-disable': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'all',
                                    'ipsec',
                                    'none'
                                ]
                            }
                        },
                        'gateway-address': {
                            'type': 'string'
                        },
                        'gi-gk': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'gwaddr': {
                            'type': 'string'
                        },
                        'gwdetect': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ha-priority': {
                            'type': 'integer'
                        },
                        'icmp-accept-redirect': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'icmp-redirect': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'icmp-send-redirect': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ident-accept': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'idle-timeout': {
                            'type': 'integer'
                        },
                        'if-mdix': {
                            'type': 'string',
                            'enum': [
                                'auto',
                                'normal',
                                'crossover'
                            ]
                        },
                        'if-media': {
                            'type': 'string',
                            'enum': [
                                'auto',
                                'copper',
                                'fiber'
                            ]
                        },
                        'in-force-vlan-cos': {
                            'type': 'integer'
                        },
                        'inbandwidth': {
                            'type': 'integer'
                        },
                        'ingress-cos': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'cos0',
                                'cos1',
                                'cos2',
                                'cos3',
                                'cos4',
                                'cos5',
                                'cos6',
                                'cos7'
                            ]
                        },
                        'ingress-spillover-threshold': {
                            'type': 'integer'
                        },
                        'internal': {
                            'type': 'integer'
                        },
                        'ip': {
                            'type': 'string'
                        },
                        'ipmac': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ips-sniffer-mode': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ipunnumbered': {
                            'type': 'string'
                        },
                        'ipv6': {
                            'autoconf': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'dhcp6-client-options': {
                                'type': 'array',
                                'items': {
                                    'type': 'string',
                                    'enum': [
                                        'rapid',
                                        'iapd',
                                        'iana',
                                        'dns',
                                        'dnsname'
                                    ]
                                }
                            },
                            'dhcp6-information-request': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'dhcp6-prefix-delegation': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'dhcp6-prefix-hint': {
                                'type': 'string'
                            },
                            'dhcp6-prefix-hint-plt': {
                                'type': 'integer'
                            },
                            'dhcp6-prefix-hint-vlt': {
                                'type': 'integer'
                            },
                            'dhcp6-relay-ip': {
                                'type': 'string'
                            },
                            'dhcp6-relay-service': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'dhcp6-relay-type': {
                                'type': 'string',
                                'enum': [
                                    'regular'
                                ]
                            },
                            'ip6-address': {
                                'type': 'string'
                            },
                            'ip6-allowaccess': {
                                'type': 'array',
                                'items': {
                                    'type': 'string',
                                    'enum': [
                                        'https',
                                        'ping',
                                        'ssh',
                                        'snmp',
                                        'http',
                                        'telnet',
                                        'fgfm',
                                        'capwap'
                                    ]
                                }
                            },
                            'ip6-default-life': {
                                'type': 'integer'
                            },
                            'ip6-dns-server-override': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'ip6-hop-limit': {
                                'type': 'integer'
                            },
                            'ip6-link-mtu': {
                                'type': 'integer'
                            },
                            'ip6-manage-flag': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'ip6-max-interval': {
                                'type': 'integer'
                            },
                            'ip6-min-interval': {
                                'type': 'integer'
                            },
                            'ip6-mode': {
                                'type': 'string',
                                'enum': [
                                    'static',
                                    'dhcp',
                                    'pppoe',
                                    'delegated'
                                ]
                            },
                            'ip6-other-flag': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'ip6-reachable-time': {
                                'type': 'integer'
                            },
                            'ip6-retrans-time': {
                                'type': 'integer'
                            },
                            'ip6-send-adv': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'ip6-subnet': {
                                'type': 'string'
                            },
                            'ip6-upstream-interface': {
                                'type': 'string'
                            },
                            'nd-cert': {
                                'type': 'string'
                            },
                            'nd-cga-modifier': {
                                'type': 'string'
                            },
                            'nd-mode': {
                                'type': 'string',
                                'enum': [
                                    'basic',
                                    'SEND-compatible'
                                ]
                            },
                            'nd-security-level': {
                                'type': 'integer'
                            },
                            'nd-timestamp-delta': {
                                'type': 'integer'
                            },
                            'nd-timestamp-fuzz': {
                                'type': 'integer'
                            },
                            'vrip6_link_local': {
                                'type': 'string'
                            },
                            'vrrp-virtual-mac6': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            }
                        },
                        'l2forward': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'l2tp-client': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'lacp-ha-slave': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'lacp-mode': {
                            'type': 'string',
                            'enum': [
                                'static',
                                'passive',
                                'active'
                            ]
                        },
                        'lacp-speed': {
                            'type': 'string',
                            'enum': [
                                'slow',
                                'fast'
                            ]
                        },
                        'lcp-echo-interval': {
                            'type': 'integer'
                        },
                        'lcp-max-echo-fails': {
                            'type': 'integer'
                        },
                        'link-up-delay': {
                            'type': 'integer'
                        },
                        'listen-forticlient-connection': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'lldp-network-policy': {
                            'type': 'string'
                        },
                        'lldp-reception': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable',
                                'vdom'
                            ]
                        },
                        'lldp-transmission': {
                            'type': 'string',
                            'enum': [
                                'enable',
                                'disable',
                                'vdom'
                            ]
                        },
                        'log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'macaddr': {
                            'type': 'string'
                        },
                        'management-ip': {
                            'type': 'string'
                        },
                        'max-egress-burst-rate': {
                            'type': 'integer'
                        },
                        'max-egress-rate': {
                            'type': 'integer'
                        },
                        'mediatype': {
                            'type': 'string',
                            'enum': [
                                'serdes-sfp',
                                'sgmii-sfp',
                                'cfp2-sr10',
                                'cfp2-lr4',
                                'serdes-copper-sfp',
                                'sr',
                                'cr',
                                'lr',
                                'qsfp28-sr4',
                                'qsfp28-lr4',
                                'qsfp28-cr4'
                            ]
                        },
                        'member': {
                            'type': 'string'
                        },
                        'min-links': {
                            'type': 'integer'
                        },
                        'min-links-down': {
                            'type': 'string',
                            'enum': [
                                'operational',
                                'administrative'
                            ]
                        },
                        'mode': {
                            'type': 'string',
                            'enum': [
                                'static',
                                'dhcp',
                                'pppoe',
                                'pppoa',
                                'ipoa',
                                'eoa'
                            ]
                        },
                        'mtu': {
                            'type': 'integer'
                        },
                        'mtu-override': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mux-type': {
                            'type': 'string',
                            'enum': [
                                'llc-encaps',
                                'vc-encaps'
                            ]
                        },
                        'name': {
                            'type': 'string'
                        },
                        'ndiscforward': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'netbios-forward': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'netflow-sampler': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'tx',
                                'rx',
                                'both'
                            ]
                        },
                        'npu-fastpath': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'nst': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'out-force-vlan-cos': {
                            'type': 'integer'
                        },
                        'outbandwidth': {
                            'type': 'integer'
                        },
                        'padt-retry-timeout': {
                            'type': 'integer'
                        },
                        'password': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'peer-interface': {
                            'type': 'string'
                        },
                        'phy-mode': {
                            'type': 'string',
                            'enum': [
                                'auto',
                                'adsl',
                                'vdsl'
                            ]
                        },
                        'ping-serv-status': {
                            'type': 'integer'
                        },
                        'poe': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'polling-interval': {
                            'type': 'integer'
                        },
                        'pppoe-unnumbered-negotiate': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'pptp-auth-type': {
                            'type': 'string',
                            'enum': [
                                'auto',
                                'pap',
                                'chap',
                                'mschapv1',
                                'mschapv2'
                            ]
                        },
                        'pptp-client': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'pptp-password': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'pptp-server-ip': {
                            'type': 'string'
                        },
                        'pptp-timeout': {
                            'type': 'integer'
                        },
                        'pptp-user': {
                            'type': 'string'
                        },
                        'preserve-session-route': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'priority': {
                            'type': 'integer'
                        },
                        'priority-override': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'proxy-captive-portal': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'redundant-interface': {
                            'type': 'string'
                        },
                        'remote-ip': {
                            'type': 'string'
                        },
                        'replacemsg-override-group': {
                            'type': 'string'
                        },
                        'retransmission': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'role': {
                            'type': 'string',
                            'enum': [
                                'lan',
                                'wan',
                                'dmz',
                                'undefined'
                            ]
                        },
                        'sample-direction': {
                            'type': 'string',
                            'enum': [
                                'rx',
                                'tx',
                                'both'
                            ]
                        },
                        'sample-rate': {
                            'type': 'integer'
                        },
                        'scan-botnet-connections': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'block',
                                'monitor'
                            ]
                        },
                        'secondary-IP': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'secondaryip': {
                            'type': 'array',
                            'items': {
                                'allowaccess': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string',
                                        'enum': [
                                            'https',
                                            'ping',
                                            'ssh',
                                            'snmp',
                                            'http',
                                            'telnet',
                                            'fgfm',
                                            'auto-ipsec',
                                            'radius-acct',
                                            'probe-response',
                                            'capwap',
                                            'dnp',
                                            'ftm'
                                        ]
                                    }
                                },
                                'detectprotocol': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string',
                                        'enum': [
                                            'ping',
                                            'tcp-echo',
                                            'udp-echo'
                                        ]
                                    }
                                },
                                'detectserver': {
                                    'type': 'string'
                                },
                                'gwdetect': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'ha-priority': {
                                    'type': 'integer'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'ip': {
                                    'type': 'string'
                                },
                                'ping-serv-status': {
                                    'type': 'integer'
                                },
                                'seq': {
                                    'type': 'integer'
                                }
                            }
                        },
                        'security-8021x-dynamic-vlan-id': {
                            'type': 'integer'
                        },
                        'security-8021x-master': {
                            'type': 'string'
                        },
                        'security-8021x-mode': {
                            'type': 'string',
                            'enum': [
                                'default',
                                'dynamic-vlan',
                                'fallback',
                                'slave'
                            ]
                        },
                        'security-exempt-list': {
                            'type': 'string'
                        },
                        'security-external-logout': {
                            'type': 'string'
                        },
                        'security-external-web': {
                            'type': 'string'
                        },
                        'security-groups': {
                            'type': 'string'
                        },
                        'security-mac-auth-bypass': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable',
                                'mac-auth-only'
                            ]
                        },
                        'security-mode': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'captive-portal',
                                '802.1X'
                            ]
                        },
                        'security-redirect-url': {
                            'type': 'string'
                        },
                        'service-name': {
                            'type': 'string'
                        },
                        'sflow-sampler': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'speed': {
                            'type': 'string',
                            'enum': [
                                'auto',
                                '10full',
                                '10half',
                                '100full',
                                '100half',
                                '1000full',
                                '1000half',
                                '10000full',
                                '1000auto',
                                '10000auto',
                                '40000full',
                                '100Gfull',
                                '25000full',
                                '40000auto',
                                '25000auto',
                                '100Gauto'
                            ]
                        },
                        'spillover-threshold': {
                            'type': 'integer'
                        },
                        'src-check': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'down',
                                'up'
                            ]
                        },
                        'stp': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'stp-ha-slave': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable',
                                'priority-adjust'
                            ]
                        },
                        'stpforward': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'stpforward-mode': {
                            'type': 'string',
                            'enum': [
                                'rpl-all-ext-id',
                                'rpl-bridge-ext-id',
                                'rpl-nothing'
                            ]
                        },
                        'strip-priority-vlan-tag': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'subst': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'substitute-dst-mac': {
                            'type': 'string'
                        },
                        'switch': {
                            'type': 'string'
                        },
                        'switch-controller-access-vlan': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'switch-controller-arp-inspection': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'switch-controller-auth': {
                            'type': 'string',
                            'enum': [
                                'radius',
                                'usergroup'
                            ]
                        },
                        'switch-controller-dhcp-snooping': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'switch-controller-dhcp-snooping-option82': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'switch-controller-dhcp-snooping-verify-mac': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'switch-controller-igmp-snooping': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'switch-controller-learning-limit': {
                            'type': 'integer'
                        },
                        'switch-controller-radius-server': {
                            'type': 'string'
                        },
                        'switch-controller-traffic-policy': {
                            'type': 'string'
                        },
                        'tc-mode': {
                            'type': 'string',
                            'enum': [
                                'ptm',
                                'atm'
                            ]
                        },
                        'tcp-mss': {
                            'type': 'integer'
                        },
                        'trunk': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'trust-ip-1': {
                            'type': 'string'
                        },
                        'trust-ip-2': {
                            'type': 'string'
                        },
                        'trust-ip-3': {
                            'type': 'string'
                        },
                        'trust-ip6-1': {
                            'type': 'string'
                        },
                        'trust-ip6-2': {
                            'type': 'string'
                        },
                        'trust-ip6-3': {
                            'type': 'string'
                        },
                        'type': {
                            'type': 'string',
                            'enum': [
                                'physical',
                                'vlan',
                                'aggregate',
                                'redundant',
                                'tunnel',
                                'wireless',
                                'vdom-link',
                                'loopback',
                                'switch',
                                'hard-switch',
                                'hdlc',
                                'vap-switch',
                                'wl-mesh',
                                'fortilink',
                                'switch-vlan',
                                'fctrl-trunk',
                                'tdm',
                                'fext-wan',
                                'vxlan',
                                'emac-vlan'
                            ]
                        },
                        'username': {
                            'type': 'string'
                        },
                        'vci': {
                            'type': 'integer'
                        },
                        'vectoring': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'vindex': {
                            'type': 'integer'
                        },
                        'vlanforward': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'vlanid': {
                            'type': 'integer'
                        },
                        'vpi': {
                            'type': 'integer'
                        },
                        'vrf': {
                            'type': 'integer'
                        },
                        'vrrp': {
                            'type': 'array',
                            'items': {
                                'accept-mode': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'adv-interval': {
                                    'type': 'integer'
                                },
                                'ignore-default-route': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'preempt': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'priority': {
                                    'type': 'integer'
                                },
                                'start-time': {
                                    'type': 'integer'
                                },
                                'status': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'version': {
                                    'type': 'string',
                                    'enum': [
                                        '2',
                                        '3'
                                    ]
                                },
                                'vrdst': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                },
                                'vrdst-priority': {
                                    'type': 'integer'
                                },
                                'vrgrp': {
                                    'type': 'integer'
                                },
                                'vrid': {
                                    'type': 'integer'
                                },
                                'vrip': {
                                    'type': 'string'
                                }
                            }
                        },
                        'vrrp-virtual-mac': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'wccp': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'weight': {
                            'type': 'integer'
                        },
                        'wifi-5g-threshold': {
                            'type': 'string'
                        },
                        'wifi-acl': {
                            'type': 'string',
                            'enum': [
                                'deny',
                                'allow'
                            ]
                        },
                        'wifi-ap-band': {
                            'type': 'string',
                            'enum': [
                                'any',
                                '5g-preferred',
                                '5g-only'
                            ]
                        },
                        'wifi-auth': {
                            'type': 'string',
                            'enum': [
                                'PSK',
                                'RADIUS',
                                'radius',
                                'usergroup'
                            ]
                        },
                        'wifi-auto-connect': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'wifi-auto-save': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'wifi-broadcast-ssid': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'wifi-encrypt': {
                            'type': 'string',
                            'enum': [
                                'TKIP',
                                'AES'
                            ]
                        },
                        'wifi-fragment-threshold': {
                            'type': 'integer'
                        },
                        'wifi-key': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'wifi-keyindex': {
                            'type': 'integer'
                        },
                        'wifi-mac-filter': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'wifi-passphrase': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'wifi-radius-server': {
                            'type': 'string'
                        },
                        'wifi-rts-threshold': {
                            'type': 'integer'
                        },
                        'wifi-security': {
                            'type': 'string',
                            'enum': [
                                'None',
                                'WEP64',
                                'wep64',
                                'WEP128',
                                'wep128',
                                'WPA_PSK',
                                'WPA_RADIUS',
                                'WPA',
                                'WPA2',
                                'WPA2_AUTO',
                                'open',
                                'wpa-personal',
                                'wpa-enterprise',
                                'wpa-only-personal',
                                'wpa-only-enterprise',
                                'wpa2-only-personal',
                                'wpa2-only-enterprise'
                            ]
                        },
                        'wifi-ssid': {
                            'type': 'string'
                        },
                        'wifi-usergroup': {
                            'type': 'string'
                        },
                        'wins-ip': {
                            'type': 'string'
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
