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
module: fmgr_wanprof_system_virtualwanlink_service_obj
short_description: Create SD-WAN rules or priority rules (also called services) to control how sessions are distributed to physical interfaces in the SD-WAN.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get move set update ] the following apis.
    - /pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/service/{service}
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
    loose_validation:
        description: Do parameter validation in a loose way
        required: False
        type: bool
        default: false
    workspace_locking_adom:
        description: the adom to lock in case FortiManager running in workspace mode
        required: False
        type: string
        choices:
          - global
          - custom adom
    workspace_locking_timeout:
        description: the maximum time in seconds to wait for other user to release the workspace lock
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
            service:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Create SD-WAN rules or priority rules (also called services) to control how sessions are distributed to physical interfaces in the SD-...'
        api_categories: [api_tag0]
        api_tag0:
            data:
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
                    description: 'Percentage threshold change of link cost values that will result in policy route regeneration (0 - 10000000, default = 10).'
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
    schema_object1:
        methods: [delete]
        description: 'Create SD-WAN rules or priority rules (also called services) to control how sessions are distributed to physical interfaces in the SD-...'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Create SD-WAN rules or priority rules (also called services) to control how sessions are distributed to physical interfaces in the SD-...'
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
    schema_object3:
        methods: [move]
        description: 'Create SD-WAN rules or priority rules (also called services) to control how sessions are distributed to physical interfaces in the SD-...'
        api_categories: [api_tag0]
        api_tag0:
            option:
                type: str
                choices:
                    - 'before'
                    - 'after'
            target:
                type: str
                description: 'Key to the target entry.'

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

    - name: REQUESTING /PM/CONFIG/WANPROF/{WANPROF}/SYSTEM/VIRTUAL-WAN-LINK/SERVICE/{SERVICE}
      fmgr_wanprof_system_virtualwanlink_service_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wanprof: <value of string>
            service: <value of string>
         params:
            -
               data:
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

    - name: REQUESTING /PM/CONFIG/WANPROF/{WANPROF}/SYSTEM/VIRTUAL-WAN-LINK/SERVICE/{SERVICE}
      fmgr_wanprof_system_virtualwanlink_service_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wanprof: <value of string>
            service: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/WANPROF/{WANPROF}/SYSTEM/VIRTUAL-WAN-LINK/SERVICE/{SERVICE}
      fmgr_wanprof_system_virtualwanlink_service_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [move]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wanprof: <value of string>
            service: <value of string>
         params:
            -
               option: <value in [before, after]>
               target: <value of string>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[clone, move, set, update]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            id:
               type: int
               description: 'Priority rule ID (1 - 4000).'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/service/{se...'
return_of_api_category_0:
   description: items returned for method:[delete]
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
            example: '/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/service/{se...'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
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
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/service/{se...'

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
        '/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/service/{service}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'wanprof',
            'type': 'string'
        },
        {
            'name': 'service',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
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
            ],
            'object3': [
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'before',
                            'after'
                        ]
                    },
                    'api_tag': 0
                },
                {
                    'type': 'string',
                    'name': 'target',
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
            'move': 'object3',
            'set': 'object0',
            'update': 'object0'
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
                'clone',
                'delete',
                'get',
                'move',
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
        if loose_validation is False:
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
