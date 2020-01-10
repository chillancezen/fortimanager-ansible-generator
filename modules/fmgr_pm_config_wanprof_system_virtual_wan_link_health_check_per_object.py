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
module: fmgr_pm_config_wanprof_system_virtual_wan_link_health_check_per_object
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/health-check/{health-check}
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
            health-check:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'SD-WAN status checking or health checking. Identify a server on the Internet and determine how SD-WAN verifies that the FortiGate can ...'
        api_categories: [api_tag0]
        api_tag0:
            data:
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
    schema_object1:
        methods: [delete]
        description: 'SD-WAN status checking or health checking. Identify a server on the Internet and determine how SD-WAN verifies that the FortiGate can ...'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'SD-WAN status checking or health checking. Identify a server on the Internet and determine how SD-WAN verifies that the FortiGate can ...'
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

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/WANPROF/{WANPROF}/SYSTEM/VIRTUAL-WAN-LINK/HEALTH-CHECK/{HEALTH-CHECK}
      fmgr_pm_config_wanprof_system_virtual_wan_link_health_check_per_object:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wanprof: <value of string>
            health-check: <value of string>
         params:
            -
               data:
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

    - name: REQUESTING /PM/CONFIG/WANPROF/{WANPROF}/SYSTEM/VIRTUAL-WAN-LINK/HEALTH-CHECK/{HEALTH-CHECK}
      fmgr_pm_config_wanprof_system_virtual_wan_link_health_check_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wanprof: <value of string>
            health-check: <value of string>
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
            example: '/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/health-chec...'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
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
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/health-chec...'

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import FAIL_SOCKET_MSG
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import DEFAULT_RESULT_OBJ
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import FMGRCommon
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import FMGBaseException
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.fortimanager import FortiManagerHandler


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/wanprof/{wanprof}/system/virtual-wan-link/health-check/{health-check}'
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
            'name': 'health-check',
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
    module = AnsibleModule(argument_spec=module_arg_spec,
                           supports_check_mode=False)
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
        fmgr.govern_response(module=module, results=response,
                             msg='Operation Finished',
                             ansible_facts=fmgr.construct_ansible_facts(response, module.params, module.params))
    except Exception as e:
        raise FMGBaseException(e)

    module.exit_json(**response[1])


if __name__ == '__main__':
    main()
