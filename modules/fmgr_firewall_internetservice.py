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
module: fmgr_firewall_internetservice
short_description: Show Internet Service application.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/firewall/internet-service
    - /pm/config/global/obj/firewall/internet-service
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
    schema_object0:
        methods: [get]
        description: 'Show Internet Service application.'
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
        description: 'Show Internet Service application.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                database:
                    type: str
                    choices:
                        - 'isdb'
                        - 'irdb'
                direction:
                    type: str
                    choices:
                        - 'src'
                        - 'dst'
                        - 'both'
                entry:
                    -
                        id:
                            type: int
                            description: 'Entry ID.'
                        ip-number:
                            type: int
                            description: 'Total number of IP addresses.'
                        ip-range-number:
                            type: int
                            description: 'Total number of IP ranges.'
                        port:
                            -
                                type: int
                        protocol:
                            type: int
                            description: 'Integer value for the protocol type as defined by IANA (0 - 255).'
                icon-id:
                    type: int
                id:
                    type: int
                name:
                    type: str
                offset:
                    type: int
                reputation:
                    type: int
                sld-id:
                    type: int

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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/INTERNET-SERVICE
      fmgr_firewall_internetservice:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/INTERNET-SERVICE
      fmgr_firewall_internetservice:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                  database: <value in [isdb, irdb]>
                  direction: <value in [src, dst, both]>
                  entry:
                    -
                        id: <value of integer>
                        ip-number: <value of integer>
                        ip-range-number: <value of integer>
                        port:
                          - <value of integer>
                        protocol: <value of integer>
                  icon-id: <value of integer>
                  id: <value of integer>
                  name: <value of string>
                  offset: <value of integer>
                  reputation: <value of integer>
                  sld-id: <value of integer>

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
            database:
               type: str
            direction:
               type: str
            entry:
               type: array
               suboptions:
                  id:
                     type: int
                     description: 'Entry ID.'
                  ip-number:
                     type: int
                     description: 'Total number of IP addresses.'
                  ip-range-number:
                     type: int
                     description: 'Total number of IP ranges.'
                  port:
                     type: array
                     suboptions:
                        type: int
                  protocol:
                     type: int
                     description: 'Integer value for the protocol type as defined by IANA (0 - 255).'
            icon-id:
               type: int
            id:
               type: int
            name:
               type: str
            offset:
               type: int
            reputation:
               type: int
            sld-id:
               type: int
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/firewall/internet-service'
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
            example: '/pm/config/adom/{adom}/obj/firewall/internet-service'

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
        '/pm/config/adom/{adom}/obj/firewall/internet-service',
        '/pm/config/global/obj/firewall/internet-service'
    ]

    url_schema = [
        {
            'name': 'adom',
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
                        'database': {
                            'type': 'string',
                            'enum': [
                                'isdb',
                                'irdb'
                            ]
                        },
                        'direction': {
                            'type': 'string',
                            'enum': [
                                'src',
                                'dst',
                                'both'
                            ]
                        },
                        'entry': {
                            'type': 'array',
                            'items': {
                                'id': {
                                    'type': 'integer'
                                },
                                'ip-number': {
                                    'type': 'integer'
                                },
                                'ip-range-number': {
                                    'type': 'integer'
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
                        'icon-id': {
                            'type': 'integer'
                        },
                        'id': {
                            'type': 'integer'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'offset': {
                            'type': 'integer'
                        },
                        'reputation': {
                            'type': 'integer'
                        },
                        'sld-id': {
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
