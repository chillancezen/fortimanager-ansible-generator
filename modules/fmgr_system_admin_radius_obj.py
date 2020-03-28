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
module: fmgr_system_admin_radius_obj
short_description: Configure radius.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ delete get set update ] the following apis.
    - /cli/global/system/admin/radius/{radius}
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
            radius:
                type: str
    schema_object0:
        methods: [delete, get]
        description: 'Configure radius.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Configure radius.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                auth-type:
                    type: str
                    default: 'any'
                    description:
                     - 'Authentication protocol.'
                     - 'any - Use any supported authentication protocol.'
                     - 'pap - PAP.'
                     - 'chap - CHAP.'
                     - 'mschap2 - MSCHAPv2.'
                    choices:
                        - 'any'
                        - 'pap'
                        - 'chap'
                        - 'mschap2'
                name:
                    type: str
                    description: 'Name.'
                nas-ip:
                    type: str
                    default: '0.0.0.0'
                    description: 'NAS IP address and called station ID.'
                port:
                    type: int
                    default: 1812
                    description: 'Server port.'
                secondary-secret:
                    -
                        type: str
                        default: 'ENC MjQ1NDY1NzY1NDA5NDc3NsQvpemPPVnDdmjXG2aGMVw2ewhHNWiM5dWsNnfyIP59U/x0Sh3pI2ORfJmJ/m2bQ9guTxrIH8uvVP4gzItuNQvVvgS5sR/Y4...'
                secondary-server:
                    type: str
                    description: 'Secondary server name/IP.'
                secret:
                    -
                        type: str
                        default: 'ENC ODcxMTExOTAwNDcxNzk4NoWoeEH5WLj2/jjPjplVd8npoc4Pf69w03rfqCi4oVPVPLjIKZTbFLtwEaPQESVBBguR6N1nV9qaAP9EHiMLSzU7Ff/g5ui7h...'
                server:
                    type: str
                    description: 'Server name/IP.'

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

    - name: REQUESTING /CLI/SYSTEM/ADMIN/RADIUS/{RADIUS}
      fmgr_system_admin_radius_obj:
         method: <value in [set, update]>
         url_params:
            radius: <value of string>
         params:
            -
               data:
                  auth-type: <value in [any, pap, chap, ...] default: 'any'>
                  name: <value of string>
                  nas-ip: <value of string default: '0.0.0.0'>
                  port: <value of integer default: 1812>
                  secondary-secret:
                    - <value of string default: 'ENC MjQ1NDY1NzY1NDA5NDc3NsQvpemPPVnDdmjXG2aGMVw2ewhHNWiM5dWsNnfyIP59U/x0Sh3p...'>
                  secondary-server: <value of string>
                  secret:
                    - <value of string default: 'ENC ODcxMTExOTAwNDcxNzk4NoWoeEH5WLj2/jjPjplVd8npoc4Pf69w03rfqCi4oVPVPLjIKZTb...'>
                  server: <value of string>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[delete, set, update]
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
            example: '/cli/global/system/admin/radius/{radius}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            auth-type:
               type: str
               description: |
                  'Authentication protocol.'
                  'any - Use any supported authentication protocol.'
                  'pap - PAP.'
                  'chap - CHAP.'
                  'mschap2 - MSCHAPv2.'
               example: 'any'
            name:
               type: str
               description: 'Name.'
            nas-ip:
               type: str
               description: 'NAS IP address and called station ID.'
               example: '0.0.0.0'
            port:
               type: int
               description: 'Server port.'
               example: 1812
            secondary-secret:
               type: array
               suboptions:
                  type: str
                  example: 'ENC MjQ1NDY1NzY1NDA5NDc3NsQvpemPPVnDdmjXG2aGMVw2ewhHNWiM5dWsNnfyIP59U/x0Sh3p...'
            secondary-server:
               type: str
               description: 'Secondary server name/IP.'
            secret:
               type: array
               suboptions:
                  type: str
                  example: 'ENC ODcxMTExOTAwNDcxNzk4NoWoeEH5WLj2/jjPjplVd8npoc4Pf69w03rfqCi4oVPVPLjIKZTb...'
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
            example: '/cli/global/system/admin/radius/{radius}'

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
        '/cli/global/system/admin/radius/{radius}'
    ]

    url_schema = [
        {
            'name': 'radius',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
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
                        'auth-type': {
                            'type': 'string',
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
                            'type': 'string'
                        },
                        'port': {
                            'type': 'integer',
                            'default': 1812,
                            'example': 1812
                        },
                        'secondary-secret': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'secondary-server': {
                            'type': 'string'
                        },
                        'secret': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'server': {
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
            ]
        },
        'method_mapping': {
            'delete': 'object0',
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
