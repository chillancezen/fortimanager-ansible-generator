#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019 Fortinet, Inc.
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
module: fmgr_pm_config_obj_switch_controller_managed_switch_managed_switch_ports_ports
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis:
    - /pm/config/adom/{adom}/obj/switch-controller/managed-switch/{managed-switch}/ports/{ports}
    - /pm/config/global/obj/switch-controller/managed-switch/{managed-switch}/ports/{ports}
    - Examples include all parameters and values need to be adjusted to data 
      sources before usage.
     

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
            managed-switch:
                type: str
            ports:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Managed-switch port list.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                allowed-vlans:
                    type: str
                    description: 'Configure switch port tagged vlans'
                allowed-vlans-all:
                    type: str
                    description: 'Enable/disable all defined vlans on this port.'
                    choices:
                        - disable
                        - enable
                arp-inspection-trust:
                    type: str
                    description: 'Trusted or untrusted dynamic ARP inspection.'
                    choices:
                        - untrusted
                        - trusted
                bundle:
                    type: str
                    description: 'Enable/disable Link Aggregation Group (LAG) bundling for non-FortiLink interfaces.'
                    choices:
                        - disable
                        - enable
                description:
                    type: str
                    description: 'Description for port.'
                dhcp-snoop-option82-trust:
                    type: str
                    description: 'Enable/disable allowance of DHCP with option-82 on untrusted interface.'
                    choices:
                        - disable
                        - enable
                dhcp-snooping:
                    type: str
                    description: 'Trusted or untrusted DHCP-snooping interface.'
                    choices:
                        - trusted
                        - untrusted
                discard-mode:
                    type: str
                    description: 'Configure discard mode for port.'
                    choices:
                        - none
                        - all-untagged
                        - all-tagged
                edge-port:
                    type: str
                    description: 'Enable/disable this interface as an edge port, bridging connections between workstations and/or computers.'
                    choices:
                        - disable
                        - enable
                igmp-snooping:
                    type: str
                    description: 'Set IGMP snooping mode for the physical port interface.'
                    choices:
                        - disable
                        - enable
                igmps-flood-reports:
                    type: str
                    description: 'Enable/disable flooding of IGMP reports to this interface when igmp-snooping enabled.'
                    choices:
                        - disable
                        - enable
                igmps-flood-traffic:
                    type: str
                    description: 'Enable/disable flooding of IGMP snooping traffic to this interface.'
                    choices:
                        - disable
                        - enable
                lacp-speed:
                    type: str
                    description: 'end Link Aggregation Control Protocol (LACP) messages every 30 seconds (slow) or every second (fast).'
                    choices:
                        - slow
                        - fast
                learning-limit:
                    type: int
                    description: 'Limit the number of dynamic MAC addresses on this Port (1 - 128, 0 = no limit, default).'
                lldp-profile:
                    type: str
                    description: 'LLDP port TLV profile.'
                lldp-status:
                    type: str
                    description: 'LLDP transmit and receive status.'
                    choices:
                        - disable
                        - rx-only
                        - tx-only
                        - tx-rx
                loop-guard:
                    type: str
                    description: 'Enable/disable loop-guard on this interface, an STP optimization used to prevent network loops.'
                    choices:
                        - disabled
                        - enabled
                loop-guard-timeout:
                    type: int
                    description: 'Loop-guard timeout (0 - 120 min, default = 45).'
                max-bundle:
                    type: int
                    description: 'Maximum size of LAG bundle (1 - 24, default = 24)'
                mclag:
                    type: str
                    description: 'Enable/disable multi-chassis link aggregation (MCLAG).'
                    choices:
                        - disable
                        - enable
                member-withdrawal-behavior:
                    type: str
                    description: 'Port behavior after it withdraws because of loss of control packets.'
                    choices:
                        - forward
                        - block
                members:
                    -
                        type: str
                min-bundle:
                    type: int
                    description: 'Minimum size of LAG bundle (1 - 24, default = 1)'
                mode:
                    type: str
                    description: 'LACP mode: ignore and do not send control messages, or negotiate 802.3ad aggregation passively or actively.'
                    choices:
                        - static
                        - lacp-passive
                        - lacp-active
                poe-pre-standard-detection:
                    type: str
                    description: 'Enable/disable PoE pre-standard detection.'
                    choices:
                        - disable
                        - enable
                poe-status:
                    type: str
                    description: 'Enable/disable PoE status.'
                    choices:
                        - disable
                        - enable
                port-name:
                    type: str
                    description: 'Switch port name.'
                port-owner:
                    type: str
                    description: 'Switch port name.'
                port-security-policy:
                    type: str
                    description: 'Switch controller authentication policy to apply to this managed switch from available options.'
                port-selection-criteria:
                    type: str
                    description: 'Algorithm for aggregate port selection.'
                    choices:
                        - src-mac
                        - dst-mac
                        - src-dst-mac
                        - src-ip
                        - dst-ip
                        - src-dst-ip
                qos-policy:
                    type: str
                    description: 'Switch controller QoS policy from available options.'
                sample-direction:
                    type: str
                    description: 'sFlow sample direction.'
                    choices:
                        - rx
                        - tx
                        - both
                sflow-counter-interval:
                    type: int
                    description: 'sFlow sampler counter polling interval (1 - 255 sec).'
                sflow-sample-rate:
                    type: int
                    description: 'sFlow sampler sample rate (0 - 99999 p/sec).'
                sflow-sampler:
                    type: str
                    description: 'Enable/disable sFlow protocol on this interface.'
                    choices:
                        - disabled
                        - enabled
                stp-bpdu-guard:
                    type: str
                    description: 'Enable/disable STP BPDU guard on this interface.'
                    choices:
                        - disabled
                        - enabled
                stp-bpdu-guard-timeout:
                    type: int
                    description: 'BPDU Guard disabling protection (0 - 120 min).'
                stp-root-guard:
                    type: str
                    description: 'Enable/disable STP root guard on this interface.'
                    choices:
                        - disabled
                        - enabled
                stp-state:
                    type: str
                    description: 'Enable/disable Spanning Tree Protocol (STP) on this interface.'
                    choices:
                        - disabled
                        - enabled
                type:
                    type: str
                    description: 'Interface type: physical or trunk port.'
                    choices:
                        - physical
                        - trunk
                untagged-vlans:
                    type: str
                    description: 'Configure switch port untagged vlans'
                vlan:
                    type: str
                    description: 'Assign switch ports to a VLAN.'
    schema_object1:
        methods: [delete]
        description: 'Managed-switch port list.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Managed-switch port list.'
        api_categories: [api_tag0]
        api_tag0:
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the object will be returned.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'chksum - Return the check-sum value instead of attributes.'
                choices:
                    - object member
                    - chksum
                    - datasrc

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /pm/config/obj/switch-controller/managed-switch/{managed-switch}/ports/{ports}
      fmgr_pm_config_obj_switch_controller_managed_switch_managed_switch_ports_ports:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            managed-switch: <value of string>
            ports: <value of string>
         params:
            - 
               data: 
                  allowed-vlans: <value of string>
                  allowed-vlans-all: <value in [disable, enable]>
                  arp-inspection-trust: <value in [untrusted, trusted]>
                  bundle: <value in [disable, enable]>
                  description: <value of string>
                  dhcp-snoop-option82-trust: <value in [disable, enable]>
                  dhcp-snooping: <value in [trusted, untrusted]>
                  discard-mode: <value in [none, all-untagged, all-tagged]>
                  edge-port: <value in [disable, enable]>
                  igmp-snooping: <value in [disable, enable]>
                  igmps-flood-reports: <value in [disable, enable]>
                  igmps-flood-traffic: <value in [disable, enable]>
                  lacp-speed: <value in [slow, fast]>
                  learning-limit: <value of integer>
                  lldp-profile: <value of string>
                  lldp-status: <value in [disable, rx-only, tx-only, ...]>
                  loop-guard: <value in [disabled, enabled]>
                  loop-guard-timeout: <value of integer>
                  max-bundle: <value of integer>
                  mclag: <value in [disable, enable]>
                  member-withdrawal-behavior: <value in [forward, block]>
                  members: 
                   - <value of string>
                  min-bundle: <value of integer>
                  mode: <value in [static, lacp-passive, lacp-active]>
                  poe-pre-standard-detection: <value in [disable, enable]>
                  poe-status: <value in [disable, enable]>
                  port-name: <value of string>
                  port-owner: <value of string>
                  port-security-policy: <value of string>
                  port-selection-criteria: <value in [src-mac, dst-mac, src-dst-mac, ...]>
                  qos-policy: <value of string>
                  sample-direction: <value in [rx, tx, both]>
                  sflow-counter-interval: <value of integer>
                  sflow-sample-rate: <value of integer>
                  sflow-sampler: <value in [disabled, enabled]>
                  stp-bpdu-guard: <value in [disabled, enabled]>
                  stp-bpdu-guard-timeout: <value of integer>
                  stp-root-guard: <value in [disabled, enabled]>
                  stp-state: <value in [disabled, enabled]>
                  type: <value in [physical, trunk]>
                  untagged-vlans: <value of string>
                  vlan: <value of string>
    - name: send request to /pm/config/obj/switch-controller/managed-switch/{managed-switch}/ports/{ports}
      fmgr_pm_config_obj_switch_controller_managed_switch_managed_switch_ports_ports:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            managed-switch: <value of string>
            ports: <value of string>
         params:
            - 
               option: <value in [object member, chksum, datasrc]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[clone, delete, set, update]
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
            example: /pm/config/adom/{adom}/obj/switch-controller/managed-switch/{managed-switch}/ports/{ports}
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            allowed-vlans:
               type: str
               description: 'Configure switch port tagged vlans'
            allowed-vlans-all:
               type: str
               description: 'Enable/disable all defined vlans on this port.'
            arp-inspection-trust:
               type: str
               description: 'Trusted or untrusted dynamic ARP inspection.'
            bundle:
               type: str
               description: 'Enable/disable Link Aggregation Group (LAG) bundling for non-FortiLink interfaces.'
            description:
               type: str
               description: 'Description for port.'
            dhcp-snoop-option82-trust:
               type: str
               description: 'Enable/disable allowance of DHCP with option-82 on untrusted interface.'
            dhcp-snooping:
               type: str
               description: 'Trusted or untrusted DHCP-snooping interface.'
            discard-mode:
               type: str
               description: 'Configure discard mode for port.'
            edge-port:
               type: str
               description: 'Enable/disable this interface as an edge port, bridging connections between workstations and/or computers.'
            igmp-snooping:
               type: str
               description: 'Set IGMP snooping mode for the physical port interface.'
            igmps-flood-reports:
               type: str
               description: 'Enable/disable flooding of IGMP reports to this interface when igmp-snooping enabled.'
            igmps-flood-traffic:
               type: str
               description: 'Enable/disable flooding of IGMP snooping traffic to this interface.'
            lacp-speed:
               type: str
               description: 'end Link Aggregation Control Protocol (LACP) messages every 30 seconds (slow) or every second (fast).'
            learning-limit:
               type: int
               description: 'Limit the number of dynamic MAC addresses on this Port (1 - 128, 0 = no limit, default).'
            lldp-profile:
               type: str
               description: 'LLDP port TLV profile.'
            lldp-status:
               type: str
               description: 'LLDP transmit and receive status.'
            loop-guard:
               type: str
               description: 'Enable/disable loop-guard on this interface, an STP optimization used to prevent network loops.'
            loop-guard-timeout:
               type: int
               description: 'Loop-guard timeout (0 - 120 min, default = 45).'
            max-bundle:
               type: int
               description: 'Maximum size of LAG bundle (1 - 24, default = 24)'
            mclag:
               type: str
               description: 'Enable/disable multi-chassis link aggregation (MCLAG).'
            member-withdrawal-behavior:
               type: str
               description: 'Port behavior after it withdraws because of loss of control packets.'
            members:
               type: array
               suboptions:
                  type: str
            min-bundle:
               type: int
               description: 'Minimum size of LAG bundle (1 - 24, default = 1)'
            mode:
               type: str
               description: 'LACP mode: ignore and do not send control messages, or negotiate 802.3ad aggregation passively or actively.'
            poe-pre-standard-detection:
               type: str
               description: 'Enable/disable PoE pre-standard detection.'
            poe-status:
               type: str
               description: 'Enable/disable PoE status.'
            port-name:
               type: str
               description: 'Switch port name.'
            port-owner:
               type: str
               description: 'Switch port name.'
            port-security-policy:
               type: str
               description: 'Switch controller authentication policy to apply to this managed switch from available options.'
            port-selection-criteria:
               type: str
               description: 'Algorithm for aggregate port selection.'
            qos-policy:
               type: str
               description: 'Switch controller QoS policy from available options.'
            sample-direction:
               type: str
               description: 'sFlow sample direction.'
            sflow-counter-interval:
               type: int
               description: 'sFlow sampler counter polling interval (1 - 255 sec).'
            sflow-sample-rate:
               type: int
               description: 'sFlow sampler sample rate (0 - 99999 p/sec).'
            sflow-sampler:
               type: str
               description: 'Enable/disable sFlow protocol on this interface.'
            stp-bpdu-guard:
               type: str
               description: 'Enable/disable STP BPDU guard on this interface.'
            stp-bpdu-guard-timeout:
               type: int
               description: 'BPDU Guard disabling protection (0 - 120 min).'
            stp-root-guard:
               type: str
               description: 'Enable/disable STP root guard on this interface.'
            stp-state:
               type: str
               description: 'Enable/disable Spanning Tree Protocol (STP) on this interface.'
            type:
               type: str
               description: 'Interface type: physical or trunk port.'
            untagged-vlans:
               type: str
               description: 'Configure switch port untagged vlans'
            vlan:
               type: str
               description: 'Assign switch ports to a VLAN.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/obj/switch-controller/managed-switch/{managed-switch}/ports/{ports}

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible.module_utils.network.fortimanager.common import FAIL_SOCKET_MSG
from ansible.module_utils.network.fortimanager.common import DEFAULT_RESULT_OBJ
from ansible.module_utils.network.fortimanager.common import FMGRCommon
from ansible.module_utils.network.fortimanager.common import FMGBaseException
from ansible.module_utils.network.fortimanager.fortimanager import FortiManagerHandler

def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/switch-controller/managed-switch/{managed-switch}/ports/{ports}',
        '/pm/config/global/obj/switch-controller/managed-switch/{managed-switch}/ports/{ports}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'managed-switch',
            'type': 'string'
        },
        {
            'name': 'ports',
            'type': 'string'
        }
    ]

    body_schema =  {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'allowed-vlans': {
                            'type': 'string'
                        },
                        'allowed-vlans-all': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'arp-inspection-trust': {
                            'type': 'string',
                            'enum': [
                                'untrusted',
                                'trusted'
                            ]
                        },
                        'bundle': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'description': {
                            'type': 'string'
                        },
                        'dhcp-snoop-option82-trust': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dhcp-snooping': {
                            'type': 'string',
                            'enum': [
                                'trusted',
                                'untrusted'
                            ]
                        },
                        'discard-mode': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'all-untagged',
                                'all-tagged'
                            ]
                        },
                        'edge-port': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'igmp-snooping': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'igmps-flood-reports': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'igmps-flood-traffic': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'lacp-speed': {
                            'type': 'string',
                            'enum': [
                                'slow',
                                'fast'
                            ]
                        },
                        'learning-limit': {
                            'type': 'integer'
                        },
                        'lldp-profile': {
                            'type': 'string'
                        },
                        'lldp-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'rx-only',
                                'tx-only',
                                'tx-rx'
                            ]
                        },
                        'loop-guard': {
                            'type': 'string',
                            'enum': [
                                'disabled',
                                'enabled'
                            ]
                        },
                        'loop-guard-timeout': {
                            'type': 'integer'
                        },
                        'max-bundle': {
                            'type': 'integer'
                        },
                        'mclag': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'member-withdrawal-behavior': {
                            'type': 'string',
                            'enum': [
                                'forward',
                                'block'
                            ]
                        },
                        'members': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'min-bundle': {
                            'type': 'integer'
                        },
                        'mode': {
                            'type': 'string',
                            'enum': [
                                'static',
                                'lacp-passive',
                                'lacp-active'
                            ]
                        },
                        'poe-pre-standard-detection': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'poe-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'port-name': {
                            'type': 'string'
                        },
                        'port-owner': {
                            'type': 'string'
                        },
                        'port-security-policy': {
                            'type': 'string'
                        },
                        'port-selection-criteria': {
                            'type': 'string',
                            'enum': [
                                'src-mac',
                                'dst-mac',
                                'src-dst-mac',
                                'src-ip',
                                'dst-ip',
                                'src-dst-ip'
                            ]
                        },
                        'qos-policy': {
                            'type': 'string'
                        },
                        'sample-direction': {
                            'type': 'string',
                            'enum': [
                                'rx',
                                'tx',
                                'both'
                            ]
                        },
                        'sflow-counter-interval': {
                            'type': 'integer'
                        },
                        'sflow-sample-rate': {
                            'type': 'integer'
                        },
                        'sflow-sampler': {
                            'type': 'string',
                            'enum': [
                                'disabled',
                                'enabled'
                            ]
                        },
                        'stp-bpdu-guard': {
                            'type': 'string',
                            'enum': [
                                'disabled',
                                'enabled'
                            ]
                        },
                        'stp-bpdu-guard-timeout': {
                            'type': 'integer'
                        },
                        'stp-root-guard': {
                            'type': 'string',
                            'enum': [
                                'disabled',
                                'enabled'
                            ]
                        },
                        'stp-state': {
                            'type': 'string',
                            'enum': [
                                'disabled',
                                'enabled'
                            ]
                        },
                        'type': {
                            'type': 'string',
                            'enum': [
                                'physical',
                                'trunk'
                            ]
                        },
                        'untagged-vlans': {
                            'type': 'string'
                        },
                        'vlan': {
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
            ],
            'object1': [
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object2': [
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
            ]
        },
        'method_mapping': {
            'clone': 'object0',
            'delete': 'object1',
            'get': 'object2',
            'set': 'object0',
            'update': 'object0'
        }
    }


    module_arg_spec = {
        'params': {
            'type': 'list',
            'required': False
        },
        'method': {
            'type': 'str',
            'required': True,
            'choices': [
                'clone',
                'delete',
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
    module = AnsibleModule(argument_spec = module_arg_spec,
                           supports_check_mode = False)
    method = module.params['method']

    fmgr = None
    payload = None
    response = DEFAULT_RESULT_OBJ

    if module._socket_path:
        connection = Connection(module._socket_path)
        tools = FMGRCommon()
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
        fmgr.govern_response(module = module, results = response,
                             msg = 'Operation Finished',
                             ansible_facts = fmgr.construct_ansible_facts(
                                response, module.params, module.params))
    except Exception as e:
        raise FMGBaseException(e)

    module.exit_json(**response[1])

if __name__ == '__main__':
    main()