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
module: fmgr_dynamic_virtualwanlink_members_dynamicmapping_obj
short_description: no description
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/dynamic/virtual-wan-link/members/{members}/dynamic_mapping/{dynamic_mapping}
    - /pm/config/global/obj/dynamic/virtual-wan-link/members/{members}/dynamic_mapping/{dynamic_mapping}
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
            members:
                type: str
            dynamic_mapping:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
            data:
                _scope:
                    -
                        name:
                            type: str
                        vdom:
                            type: str
                comment:
                    type: str
                cost:
                    type: int
                detect-failtime:
                    type: int
                detect-http-get:
                    type: str
                detect-http-match:
                    type: str
                detect-http-port:
                    type: int
                detect-interval:
                    type: int
                detect-protocol:
                    type: str
                    choices:
                        - 'ping'
                        - 'tcp-echo'
                        - 'udp-echo'
                        - 'http'
                detect-recoverytime:
                    type: int
                detect-server:
                    type: str
                detect-timeout:
                    type: int
                gateway:
                    type: str
                gateway6:
                    type: str
                ingress-spillover-threshold:
                    type: int
                interface:
                    type: str
                priority:
                    type: int
                source:
                    type: str
                source6:
                    type: str
                spillover-threshold:
                    type: int
                status:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                volume-ratio:
                    type: int
                weight:
                    type: int
    schema_object1:
        methods: [delete]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
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

    - name: REQUESTING /PM/CONFIG/OBJ/DYNAMIC/VIRTUAL-WAN-LINK/MEMBERS/{MEMBERS}/DYNAMIC_MAPPING/{DYNAMIC_MAPPING}
      fmgr_dynamic_virtualwanlink_members_dynamicmapping_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            members: <value of string>
            dynamic_mapping: <value of string>
         params:
            -
               data:
                  _scope:
                    -
                        name: <value of string>
                        vdom: <value of string>
                  comment: <value of string>
                  cost: <value of integer>
                  detect-failtime: <value of integer>
                  detect-http-get: <value of string>
                  detect-http-match: <value of string>
                  detect-http-port: <value of integer>
                  detect-interval: <value of integer>
                  detect-protocol: <value in [ping, tcp-echo, udp-echo, ...]>
                  detect-recoverytime: <value of integer>
                  detect-server: <value of string>
                  detect-timeout: <value of integer>
                  gateway: <value of string>
                  gateway6: <value of string>
                  ingress-spillover-threshold: <value of integer>
                  interface: <value of string>
                  priority: <value of integer>
                  source: <value of string>
                  source6: <value of string>
                  spillover-threshold: <value of integer>
                  status: <value in [disable, enable]>
                  volume-ratio: <value of integer>
                  weight: <value of integer>

    - name: REQUESTING /PM/CONFIG/OBJ/DYNAMIC/VIRTUAL-WAN-LINK/MEMBERS/{MEMBERS}/DYNAMIC_MAPPING/{DYNAMIC_MAPPING}
      fmgr_dynamic_virtualwanlink_members_dynamicmapping_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            members: <value of string>
            dynamic_mapping: <value of string>
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
            example: '/pm/config/adom/{adom}/obj/dynamic/virtual-wan-link/members/{members}/dynami...'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            _scope:
               type: array
               suboptions:
                  name:
                     type: str
                  vdom:
                     type: str
            comment:
               type: str
            cost:
               type: int
            detect-failtime:
               type: int
            detect-http-get:
               type: str
            detect-http-match:
               type: str
            detect-http-port:
               type: int
            detect-interval:
               type: int
            detect-protocol:
               type: str
            detect-recoverytime:
               type: int
            detect-server:
               type: str
            detect-timeout:
               type: int
            gateway:
               type: str
            gateway6:
               type: str
            ingress-spillover-threshold:
               type: int
            interface:
               type: str
            priority:
               type: int
            source:
               type: str
            source6:
               type: str
            spillover-threshold:
               type: int
            status:
               type: str
            volume-ratio:
               type: int
            weight:
               type: int
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/dynamic/virtual-wan-link/members/{members}/dynami...'

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
        '/pm/config/adom/{adom}/obj/dynamic/virtual-wan-link/members/{members}/dynamic_mapping/{dynamic_mapping}',
        '/pm/config/global/obj/dynamic/virtual-wan-link/members/{members}/dynamic_mapping/{dynamic_mapping}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'members',
            'type': 'string'
        },
        {
            'name': 'dynamic_mapping',
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
                        '_scope': {
                            'type': 'array',
                            'items': {
                                'name': {
                                    'type': 'string'
                                },
                                'vdom': {
                                    'type': 'string'
                                }
                            }
                        },
                        'comment': {
                            'type': 'string'
                        },
                        'cost': {
                            'type': 'integer'
                        },
                        'detect-failtime': {
                            'type': 'integer'
                        },
                        'detect-http-get': {
                            'type': 'string'
                        },
                        'detect-http-match': {
                            'type': 'string'
                        },
                        'detect-http-port': {
                            'type': 'integer'
                        },
                        'detect-interval': {
                            'type': 'integer'
                        },
                        'detect-protocol': {
                            'type': 'string',
                            'enum': [
                                'ping',
                                'tcp-echo',
                                'udp-echo',
                                'http'
                            ]
                        },
                        'detect-recoverytime': {
                            'type': 'integer'
                        },
                        'detect-server': {
                            'type': 'string'
                        },
                        'detect-timeout': {
                            'type': 'integer'
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

    module.exit_json(meta=response[1])


if __name__ == '__main__':
    main()
