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
module: fmgr_pm_config_obj_web_proxy_forward_server_group_forward_server_group
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/web-proxy/forward-server-group/{forward-server-group}
    - /pm/config/global/obj/web-proxy/forward-server-group/{forward-server-group}
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
            forward-server-group:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Configure a forward server group consisting or multiple forward servers. Supports failover and load balancing.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                affinity:
                    type: str
                    description: 'Enable/disable affinity, attaching a source-ip's traffic to the assigned forwarding server until the forward-server-affinity-timeout is reached (under web-proxy global).'
                    choices:
                        - disable
                        - enable
                group-down-option:
                    type: str
                    description: 'Action to take when all of the servers in the forward server group are down: block sessions until at least one server is back up or pass sessions to their destination.'
                    choices:
                        - block
                        - pass
                ldb-method:
                    type: str
                    description: 'Load balance method: weighted or least-session.'
                    choices:
                        - weighted
                        - least-session
                name:
                    type: str
                    description: 'Configure a forward server group consisting one or multiple forward servers. Supports failover and load balancing.'
                server-list:
                    -
                        name:
                            type: str
                            description: 'Forward server name.'
                        weight:
                            type: int
                            description: 'Optionally assign a weight of the forwarding server for weighted load balancing (1 - 100, default = 10)'
    schema_object1:
        methods: [delete]
        description: 'Configure a forward server group consisting or multiple forward servers. Supports failover and load balancing.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Configure a forward server group consisting or multiple forward servers. Supports failover and load balancing.'
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
    - name: send request to /pm/config/obj/web-proxy/forward-server-group/{forward-server-group}
      fmgr_pm_config_obj_web_proxy_forward_server_group_forward_server_group:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            forward-server-group: <value of string>
         params:
            - 
               data: 
                  affinity: <value in [disable, enable]>
                  group-down-option: <value in [block, pass]>
                  ldb-method: <value in [weighted, least-session]>
                  name: <value of string>
                  server-list: 
                   - 
                        name: <value of string>
                        weight: <value of integer>
    - name: send request to /pm/config/obj/web-proxy/forward-server-group/{forward-server-group}
      fmgr_pm_config_obj_web_proxy_forward_server_group_forward_server_group:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            forward-server-group: <value of string>
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
            example: /pm/config/adom/{adom}/obj/web-proxy/forward-server-group/{forward-server-group}
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            affinity:
               type: str
               description: 'Enable/disable affinity, attaching a source-ip's traffic to the assigned forwarding server until the forward-server-affinity-timeout is reached (under web-proxy global).'
            group-down-option:
               type: str
               description: 'Action to take when all of the servers in the forward server group are down: block sessions until at least one server is back up or pass sessions to their destination.'
            ldb-method:
               type: str
               description: 'Load balance method: weighted or least-session.'
            name:
               type: str
               description: 'Configure a forward server group consisting one or multiple forward servers. Supports failover and load balancing.'
            server-list:
               type: array
               suboptions:
                  name:
                     type: str
                     description: 'Forward server name.'
                  weight:
                     type: int
                     description: 'Optionally assign a weight of the forwarding server for weighted load balancing (1 - 100, default = 10)'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/obj/web-proxy/forward-server-group/{forward-server-group}

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
        '/pm/config/adom/{adom}/obj/web-proxy/forward-server-group/{forward-server-group}',
        '/pm/config/global/obj/web-proxy/forward-server-group/{forward-server-group}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'forward-server-group',
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
                        'affinity': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'group-down-option': {
                            'type': 'string',
                            'enum': [
                                'block',
                                'pass'
                            ]
                        },
                        'ldb-method': {
                            'type': 'string',
                            'enum': [
                                'weighted',
                                'least-session'
                            ]
                        },
                        'name': {
                            'type': 'string'
                        },
                        'server-list': {
                            'type': 'array',
                            'items': {
                                'name': {
                                    'type': 'string'
                                },
                                'weight': {
                                    'type': 'integer'
                                }
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