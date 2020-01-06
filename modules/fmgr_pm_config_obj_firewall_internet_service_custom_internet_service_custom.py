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
module: fmgr_pm_config_obj_firewall_internet_service_custom_internet_service_custom
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/firewall/internet-service-custom/{internet-service-custom}
    - /pm/config/global/obj/firewall/internet-service-custom/{internet-service-custom}
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
            internet-service-custom:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Configure custom Internet Services.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                comment:
                    type: str
                    description: 'Comment.'
                disable-entry:
                    -
                        id:
                            type: int
                            description: 'Disable entry ID.'
                        ip-range:
                            -
                                end-ip:
                                    type: str
                                    description: 'End IP address.'
                                id:
                                    type: int
                                    description: 'Disable entry range ID.'
                                start-ip:
                                    type: str
                                    description: 'Start IP address.'
                        port:
                            -
                                type: int
                        protocol:
                            type: int
                            description: 'Integer value for the protocol type as defined by IANA (0 - 255).'
                entry:
                    -
                        dst:
                            type: str
                            description: 'Destination address or address group name.'
                        id:
                            type: int
                            description: 'Entry ID(1-255).'
                        port-range:
                            -
                                end-port:
                                    type: int
                                    description: 'Integer value for ending TCP/UDP/SCTP destination port in range (1 to 65535).'
                                id:
                                    type: int
                                    description: 'Custom entry port range ID.'
                                start-port:
                                    type: int
                                    description: 'Integer value for starting TCP/UDP/SCTP destination port in range (1 to 65535).'
                        protocol:
                            type: int
                            description: 'Integer value for the protocol type as defined by IANA (0 - 255).'
                master-service-id:
                    type: str
                    description: 'Internet Service ID in the Internet Service database.'
                name:
                    type: str
                    description: 'Internet Service name.'
    schema_object1:
        methods: [delete]
        description: 'Configure custom Internet Services.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Configure custom Internet Services.'
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
    - name: send request to /pm/config/obj/firewall/internet-service-custom/{internet-service-custom}
      fmgr_pm_config_obj_firewall_internet_service_custom_internet_service_custom:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            internet-service-custom: <value of string>
         params:
            - 
               data: 
                  comment: <value of string>
                  disable-entry: 
                   - 
                        id: <value of integer>
                        ip-range: 
                         - 
                              end-ip: <value of string>
                              id: <value of integer>
                              start-ip: <value of string>
                        port: 
                         - <value of integer>
                        protocol: <value of integer>
                  entry: 
                   - 
                        dst: <value of string>
                        id: <value of integer>
                        port-range: 
                         - 
                              end-port: <value of integer>
                              id: <value of integer>
                              start-port: <value of integer>
                        protocol: <value of integer>
                  master-service-id: <value of string>
                  name: <value of string>
    - name: send request to /pm/config/obj/firewall/internet-service-custom/{internet-service-custom}
      fmgr_pm_config_obj_firewall_internet_service_custom_internet_service_custom:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            internet-service-custom: <value of string>
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
            example: /pm/config/adom/{adom}/obj/firewall/internet-service-custom/{internet-service-custom}
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            comment:
               type: str
               description: 'Comment.'
            disable-entry:
               type: array
               suboptions:
                  id:
                     type: int
                     description: 'Disable entry ID.'
                  ip-range:
                     type: array
                     suboptions:
                        end-ip:
                           type: str
                           description: 'End IP address.'
                        id:
                           type: int
                           description: 'Disable entry range ID.'
                        start-ip:
                           type: str
                           description: 'Start IP address.'
                  port:
                     type: array
                     suboptions:
                        type: int
                  protocol:
                     type: int
                     description: 'Integer value for the protocol type as defined by IANA (0 - 255).'
            entry:
               type: array
               suboptions:
                  dst:
                     type: str
                     description: 'Destination address or address group name.'
                  id:
                     type: int
                     description: 'Entry ID(1-255).'
                  port-range:
                     type: array
                     suboptions:
                        end-port:
                           type: int
                           description: 'Integer value for ending TCP/UDP/SCTP destination port in range (1 to 65535).'
                        id:
                           type: int
                           description: 'Custom entry port range ID.'
                        start-port:
                           type: int
                           description: 'Integer value for starting TCP/UDP/SCTP destination port in range (1 to 65535).'
                  protocol:
                     type: int
                     description: 'Integer value for the protocol type as defined by IANA (0 - 255).'
            master-service-id:
               type: str
               description: 'Internet Service ID in the Internet Service database.'
            name:
               type: str
               description: 'Internet Service name.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/obj/firewall/internet-service-custom/{internet-service-custom}

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
        '/pm/config/adom/{adom}/obj/firewall/internet-service-custom/{internet-service-custom}',
        '/pm/config/global/obj/firewall/internet-service-custom/{internet-service-custom}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'internet-service-custom',
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
                        'comment': {
                            'type': 'string'
                        },
                        'disable-entry': {
                            'type': 'array',
                            'items': {
                                'id': {
                                    'type': 'integer'
                                },
                                'ip-range': {
                                    'type': 'array',
                                    'items': {
                                        'end-ip': {
                                            'type': 'string'
                                        },
                                        'id': {
                                            'type': 'integer'
                                        },
                                        'start-ip': {
                                            'type': 'string'
                                        }
                                    }
                                },
                                'port': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'integer'
                                    }
                                },
                                'protocol': {
                                    'type': 'integer'
                                }
                            }
                        },
                        'entry': {
                            'type': 'array',
                            'items': {
                                'dst': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'port-range': {
                                    'type': 'array',
                                    'items': {
                                        'end-port': {
                                            'type': 'integer'
                                        },
                                        'id': {
                                            'type': 'integer'
                                        },
                                        'start-port': {
                                            'type': 'integer'
                                        }
                                    }
                                },
                                'protocol': {
                                    'type': 'integer'
                                }
                            }
                        },
                        'master-service-id': {
                            'type': 'string'
                        },
                        'name': {
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