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
module: fmgr_firewall_vip6_realservers
short_description: Select the real servers that this server load balancing VIP will distribute traffic to.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/firewall/vip6/{vip6}/realservers
    - /pm/config/global/obj/firewall/vip6/{vip6}/realservers
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
            vip6:
                type: str
    schema_object0:
        methods: [add, set, update]
        description: 'Select the real servers that this server load balancing VIP will distribute traffic to.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    client-ip:
                        type: str
                        description: 'Only clients in this IP range can connect to this real server.'
                    healthcheck:
                        type: str
                        description: 'Enable to check the responsiveness of the real server before forwarding traffic.'
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'vip'
                    holddown-interval:
                        type: int
                        description: 'Time in seconds that the health check monitor continues to monitor an unresponsive server that should be active.'
                    http-host:
                        type: str
                        description: 'HTTP server domain name in HTTP header.'
                    id:
                        type: int
                        description: 'Real server ID.'
                    ip:
                        type: str
                        description: 'IPv6 address of the real server.'
                    max-connections:
                        type: int
                        description: 'Max number of active connections that can directed to the real server. When reached, sessions are sent to other real s...'
                    monitor:
                        type: str
                        description: 'Name of the health check monitor to use when polling to determine a virtual servers connectivity status.'
                    port:
                        type: int
                        description: 'Port for communicating with the real server. Required if port forwarding is enabled.'
                    status:
                        type: str
                        description: 'Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traffic is ...'
                        choices:
                            - 'active'
                            - 'standby'
                            - 'disable'
                    weight:
                        type: int
                        description: 'Weight of the real server. If weighted load balancing is enabled, the server with the highest weight gets more connect...'
    schema_object1:
        methods: [get]
        description: 'Select the real servers that this server load balancing VIP will distribute traffic to.'
        api_categories: [api_tag0]
        api_tag0:
            attr:
                type: str
                description: 'The name of the attribute to retrieve its datasource. Only used with &lt;i&gt;datasrc&lt;/i&gt; option.'
            fields:
                -
                    -
                        type: str
                        choices:
                            - 'client-ip'
                            - 'healthcheck'
                            - 'holddown-interval'
                            - 'http-host'
                            - 'id'
                            - 'ip'
                            - 'max-connections'
                            - 'monitor'
                            - 'port'
                            - 'status'
                            - 'weight'
            filter:
                -
                    type: str
            get used:
                type: int
            loadsub:
                type: int
                description: 'Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.'
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.'
                 - 'count - Return the number of matching entries instead of the actual entry data.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'datasrc - Return all objects that can be referenced by an attribute. Require <i>attr</i> parameter.'
                 - 'get reserved - Also return reserved objects in the result.'
                 - 'syntax - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.'
                choices:
                    - 'count'
                    - 'object member'
                    - 'datasrc'
                    - 'get reserved'
                    - 'syntax'
            range:
                -
                    type: int
            sortings:
                -
                    varidic.attr_name:
                        type: int
                        choices:
                            - 1
                            - -1

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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/VIP6/{VIP6}/REALSERVERS
      fmgr_firewall_vip6_realservers:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vip6: <value of string>
         params:
            -
               data:
                 -
                     client-ip: <value of string>
                     healthcheck: <value in [disable, enable, vip]>
                     holddown-interval: <value of integer>
                     http-host: <value of string>
                     id: <value of integer>
                     ip: <value of string>
                     max-connections: <value of integer>
                     monitor: <value of string>
                     port: <value of integer>
                     status: <value in [active, standby, disable]>
                     weight: <value of integer>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/VIP6/{VIP6}/REALSERVERS
      fmgr_firewall_vip6_realservers:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vip6: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [client-ip, healthcheck, holddown-interval, ...]>
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

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[add, set, update]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            type: array
            suboptions:
               id:
                  type: int
                  description: 'Real server ID.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/firewall/vip6/{vip6}/realservers'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            type: array
            suboptions:
               client-ip:
                  type: str
                  description: 'Only clients in this IP range can connect to this real server.'
               healthcheck:
                  type: str
                  description: 'Enable to check the responsiveness of the real server before forwarding traffic.'
               holddown-interval:
                  type: int
                  description: 'Time in seconds that the health check monitor continues to monitor an unresponsive server that should be active.'
               http-host:
                  type: str
                  description: 'HTTP server domain name in HTTP header.'
               id:
                  type: int
                  description: 'Real server ID.'
               ip:
                  type: str
                  description: 'IPv6 address of the real server.'
               max-connections:
                  type: int
                  description: 'Max number of active connections that can directed to the real server. When reached, sessions are sent to other real servers.'
               monitor:
                  type: str
                  description: 'Name of the health check monitor to use when polling to determine a virtual servers connectivity status.'
               port:
                  type: int
                  description: 'Port for communicating with the real server. Required if port forwarding is enabled.'
               status:
                  type: str
                  description: 'Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traffic is sent.'
               weight:
                  type: int
                  description: 'Weight of the real server. If weighted load balancing is enabled, the server with the highest weight gets more connections.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/firewall/vip6/{vip6}/realservers'

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
        '/pm/config/adom/{adom}/obj/firewall/vip6/{vip6}/realservers',
        '/pm/config/global/obj/firewall/vip6/{vip6}/realservers'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'vip6',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'client-ip': {
                            'type': 'string'
                        },
                        'healthcheck': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable',
                                'vip'
                            ]
                        },
                        'holddown-interval': {
                            'type': 'integer'
                        },
                        'http-host': {
                            'type': 'string'
                        },
                        'id': {
                            'type': 'integer'
                        },
                        'ip': {
                            'type': 'string'
                        },
                        'max-connections': {
                            'type': 'integer'
                        },
                        'monitor': {
                            'type': 'string'
                        },
                        'port': {
                            'type': 'integer'
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'active',
                                'standby',
                                'disable'
                            ]
                        },
                        'weight': {
                            'type': 'integer'
                        }
                    }
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
                    'name': 'attr',
                    'api_tag': 0
                },
                {
                    'name': 'fields',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'enum': [
                                'client-ip',
                                'healthcheck',
                                'holddown-interval',
                                'http-host',
                                'id',
                                'ip',
                                'max-connections',
                                'monitor',
                                'port',
                                'status',
                                'weight'
                            ]
                        }
                    }
                },
                {
                    'name': 'filter',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'example': [
                                '<attr>',
                                '==',
                                'test'
                            ]
                        }
                    },
                    'api_tag': 0
                },
                {
                    'type': 'integer',
                    'name': 'get used',
                    'api_tag': 0
                },
                {
                    'type': 'integer',
                    'name': 'loadsub',
                    'api_tag': 0
                },
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'count',
                            'object member',
                            'datasrc',
                            'get reserved',
                            'syntax'
                        ]
                    },
                    'api_tag': 0
                },
                {
                    'name': 'range',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            'type': 'integer',
                            'example': [
                                2,
                                5
                            ]
                        }
                    },
                    'api_tag': 0
                },
                {
                    'name': 'sortings',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            '{attr_name}': {
                                'type': 'integer',
                                'enum': [
                                    1,
                                    -1
                                ]
                            }
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
            'add': 'object0',
            'get': 'object1',
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
                'add',
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

    module.exit_json(meta=response[1])


if __name__ == '__main__':
    main()
