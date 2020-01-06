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
module: fmgr_pm_config_obj_firewall_ldb_monitor_ldb_monitor
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/firewall/ldb-monitor/{ldb-monitor}
    - /pm/config/global/obj/firewall/ldb-monitor/{ldb-monitor}
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
            ldb-monitor:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Configure server load balancing health monitors.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                http-get:
                    type: str
                    description: 'URL used to send a GET request to check the health of an HTTP server.'
                http-match:
                    type: str
                    description: 'String to match the value expected in response to an HTTP-GET request.'
                http-max-redirects:
                    type: int
                    description: 'The maximum number of HTTP redirects to be allowed (0 - 5, default = 0).'
                interval:
                    type: int
                    description: 'Time between health checks (5 - 65635 sec, default = 10).'
                name:
                    type: str
                    description: 'Monitor name.'
                port:
                    type: int
                    description: 'Service port used to perform the health check. If 0, health check monitor inherits port configured for the server (0 - 65635, default = 0).'
                retry:
                    type: int
                    description: 'Number health check attempts before the server is considered down (1 - 255, default = 3).'
                timeout:
                    type: int
                    description: 'Time to wait to receive response to a health check from a server. Reaching the timeout means the health check failed (1 - 255 sec, default = 2).'
                type:
                    type: str
                    description: 'Select the Monitor type used by the health check monitor to check the health of the server (PING | TCP | HTTP).'
                    choices:
                        - 'ping'
                        - 'tcp'
                        - 'http'
                        - 'passive-sip'
    schema_object1:
        methods: [delete]
        description: 'Configure server load balancing health monitors.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Configure server load balancing health monitors.'
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
    - name: send request to /pm/config/obj/firewall/ldb-monitor/{ldb-monitor}
      fmgr_pm_config_obj_firewall_ldb_monitor_ldb_monitor:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            ldb-monitor: <value of string>
         params:
            - 
               data: 
                  http-get: <value of string>
                  http-match: <value of string>
                  http-max-redirects: <value of integer>
                  interval: <value of integer>
                  name: <value of string>
                  port: <value of integer>
                  retry: <value of integer>
                  timeout: <value of integer>
                  type: <value in [ping, tcp, http, ...]>
    - name: send request to /pm/config/obj/firewall/ldb-monitor/{ldb-monitor}
      fmgr_pm_config_obj_firewall_ldb_monitor_ldb_monitor:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            ldb-monitor: <value of string>
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
            example: /pm/config/adom/{adom}/obj/firewall/ldb-monitor/{ldb-monitor}
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            http-get:
               type: str
               description: 'URL used to send a GET request to check the health of an HTTP server.'
            http-match:
               type: str
               description: 'String to match the value expected in response to an HTTP-GET request.'
            http-max-redirects:
               type: int
               description: 'The maximum number of HTTP redirects to be allowed (0 - 5, default = 0).'
            interval:
               type: int
               description: 'Time between health checks (5 - 65635 sec, default = 10).'
            name:
               type: str
               description: 'Monitor name.'
            port:
               type: int
               description: 'Service port used to perform the health check. If 0, health check monitor inherits port configured for the server (0 - 65635, default = 0).'
            retry:
               type: int
               description: 'Number health check attempts before the server is considered down (1 - 255, default = 3).'
            timeout:
               type: int
               description: 'Time to wait to receive response to a health check from a server. Reaching the timeout means the health check failed (1 - 255 sec, default = 2).'
            type:
               type: str
               description: 'Select the Monitor type used by the health check monitor to check the health of the server (PING | TCP | HTTP).'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/obj/firewall/ldb-monitor/{ldb-monitor}

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
        '/pm/config/adom/{adom}/obj/firewall/ldb-monitor/{ldb-monitor}',
        '/pm/config/global/obj/firewall/ldb-monitor/{ldb-monitor}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'ldb-monitor',
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
                        'http-get': {
                            'type': 'string'
                        },
                        'http-match': {
                            'type': 'string'
                        },
                        'http-max-redirects': {
                            'type': 'integer'
                        },
                        'interval': {
                            'type': 'integer'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'port': {
                            'type': 'integer'
                        },
                        'retry': {
                            'type': 'integer'
                        },
                        'timeout': {
                            'type': 'integer'
                        },
                        'type': {
                            'type': 'string',
                            'enum': [
                                'ping',
                                'tcp',
                                'http',
                                'passive-sip'
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