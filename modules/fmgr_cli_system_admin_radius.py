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
module: fmgr_cli_system_admin_radius
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis:
    - /cli/global/system/admin/radius
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
    schema_object0:
        methods: [add, set, update]
        description: 'Configure radius.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    auth-type:
                        type: str
                        default: any
                        description:
                         - 'Authentication protocol.'
                         - 'any - Use any supported authentication protocol.'
                         - 'pap - PAP.'
                         - 'chap - CHAP.'
                         - 'mschap2 - MSCHAPv2.'
                        choices:
                            - any
                            - pap
                            - chap
                            - mschap2
                    name:
                        type: str
                        description: 'Name.'
                    nas-ip:
                        type: str
                        default: 0.0.0.0
                        description: 'NAS IP address and called station ID.'
                    port:
                        type: int
                        default: 1812
                        description: 'Server port.'
                    secondary-secret:
                        -
                            type: str
                            default: ENC MjQ1NDY1NzY1NDA5NDc3NsQvpemPPVnDdmjXG2aGMVw2ewhHNWiM5dWsNnfyIP59U/x0Sh3pI2ORfJmJ/m2bQ9guTxrIH8uvVP4gzItuNQvVvgS5sR/Y4x3jjlmrhvA0vK8TjoXt6sFKfKe86/vEo/cg3Y/RJFF1a1dkdDKNjHxCXJIL
                    secondary-server:
                        type: str
                        description: 'Secondary server name/IP.'
                    secret:
                        -
                            type: str
                            default: ENC ODcxMTExOTAwNDcxNzk4NoWoeEH5WLj2/jjPjplVd8npoc4Pf69w03rfqCi4oVPVPLjIKZTbFLtwEaPQESVBBguR6N1nV9qaAP9EHiMLSzU7Ff/g5ui7hXGXo4hEkXIP09D4PY2eQg9Htz8Oqm42M148kMuPADC3cx8nsiVWb001mIvf
                    server:
                        type: str
                        description: 'Server name/IP.'
    schema_object1:
        methods: [get]
        description: 'Configure radius.'
        api_categories: [api_tag0]
        api_tag0:
            fields:
                -
                    -
                        type: str
                        choices:
                            - auth-type
                            - name
                            - nas-ip
                            - port
                            - secondary-secret
                            - secondary-server
                            - secret
                            - server
            filter:
                -
                    type: str
            loadsub:
                type: int
                description: 'Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.'
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.'
                 - 'count - Return the number of matching entries instead of the actual entry data.'
                 - 'syntax - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.'
                choices:
                    - count
                    - syntax

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /cli/system/admin/radius
      fmgr_cli_system_admin_radius:
         method: <value in [add, set, update]>
         params:
            - 
               data: 
                - 
                     auth-type: <value in [any, pap, chap, ...] default: any>
                     name: <value of string>
                     nas-ip: <value of string default: 0.0.0.0>
                     port: <value of integer default: 1812>
                     secondary-secret: 
                      - <value of string default: ENC MjQ1NDY1NzY1NDA5NDc3NsQvpemPPVnDdmjXG2aGMVw2ewhHNWiM5dWsNnfyIP59U/x0Sh3pI2ORfJmJ/m2bQ9guTxrIH8uvVP4gzItuNQvVvgS5sR/Y4x3jjlmrhvA0vK8TjoXt6sFKfKe86/vEo/cg3Y/RJFF1a1dkdDKNjHxCXJIL>
                     secondary-server: <value of string>
                     secret: 
                      - <value of string default: ENC ODcxMTExOTAwNDcxNzk4NoWoeEH5WLj2/jjPjplVd8npoc4Pf69w03rfqCi4oVPVPLjIKZTbFLtwEaPQESVBBguR6N1nV9qaAP9EHiMLSzU7Ff/g5ui7hXGXo4hEkXIP09D4PY2eQg9Htz8Oqm42M148kMuPADC3cx8nsiVWb001mIvf>
                     server: <value of string>
    - name: send request to /cli/system/admin/radius
      fmgr_cli_system_admin_radius:
         method: <value in [get]>
         params:
            - 
               fields: 
                - 
                   - <value in [auth-type, name, nas-ip, ...]>
               filter: 
                - <value of string>
               loadsub: <value of integer>
               option: <value in [count, syntax]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[add, set, update]
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
            example: /cli/global/system/admin/radius
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
               auth-type:
                  type: str
                  description: |
                     'Authentication protocol.'
                     'any - Use any supported authentication protocol.'
                     'pap - PAP.'
                     'chap - CHAP.'
                     'mschap2 - MSCHAPv2.'
                  example: any
               name:
                  type: str
                  description: 'Name.'
               nas-ip:
                  type: str
                  description: 'NAS IP address and called station ID.'
                  example: 0.0.0.0
               port:
                  type: int
                  description: 'Server port.'
                  example: 1812
               secondary-secret:
                  type: array
                  suboptions:
                     type: str
                     example: ENC MjQ1NDY1NzY1NDA5NDc3NsQvpemPPVnDdmjXG2aGMVw2ewhHNWiM5dWsNnfyIP59U/x0Sh3pI2ORfJmJ/m2bQ9guTxrIH8uvVP4gzItuNQvVvgS5sR/Y4x3jjlmrhvA0vK8TjoXt6sFKfKe86/vEo/cg3Y/RJFF1a1dkdDKNjHxCXJIL
               secondary-server:
                  type: str
                  description: 'Secondary server name/IP.'
               secret:
                  type: array
                  suboptions:
                     type: str
                     example: ENC ODcxMTExOTAwNDcxNzk4NoWoeEH5WLj2/jjPjplVd8npoc4Pf69w03rfqCi4oVPVPLjIKZTbFLtwEaPQESVBBguR6N1nV9qaAP9EHiMLSzU7Ff/g5ui7hXGXo4hEkXIP09D4PY2eQg9Htz8Oqm42M148kMuPADC3cx8nsiVWb001mIvf
               server:
                  type: str
                  description: 'Server name/IP.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /cli/global/system/admin/radius

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
        '/cli/global/system/admin/radius'
    ]

    url_schema = [
    ]

    body_schema =  {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'auth-type': {
                            'type': 'string',
                            'default': 'any',
                            'enum': [
                                'any',
                                'pap',
                                'chap',
                                'mschap2'
                            ]
                        },
                        'name': {
                            'type': 'string'
                        },
                        'nas-ip': {
                            'type': 'string',
                            'default': '0.0.0.0'
                        },
                        'port': {
                            'type': 'integer',
                            'default': 1812,
                            'example': 1812
                        },
                        'secondary-secret': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'default': 'ENC MjQ1NDY1NzY1NDA5NDc3NsQvpemPPVnDdmjXG2aGMVw2ewhHNWiM5dWsNnfyIP59U/x0Sh3pI2ORfJmJ/m2bQ9guTxrIH8uvVP4gzItuNQvVvgS5sR/Y4x3jjlmrhvA0vK8TjoXt6sFKfKe86/vEo/cg3Y/RJFF1a1dkdDKNjHxCXJIL'
                            }
                        },
                        'secondary-server': {
                            'type': 'string'
                        },
                        'secret': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'default': 'ENC ODcxMTExOTAwNDcxNzk4NoWoeEH5WLj2/jjPjplVd8npoc4Pf69w03rfqCi4oVPVPLjIKZTbFLtwEaPQESVBBguR6N1nV9qaAP9EHiMLSzU7Ff/g5ui7hXGXo4hEkXIP09D4PY2eQg9Htz8Oqm42M148kMuPADC3cx8nsiVWb001mIvf'
                            }
                        },
                        'server': {
                            'type': 'string'
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
                    'name': 'fields',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'enum': [
                                'auth-type',
                                'name',
                                'nas-ip',
                                'port',
                                'secondary-secret',
                                'secondary-server',
                                'secret',
                                'server'
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
                            'syntax'
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