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
module: fmgr_cli_system_connector
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /cli/global/system/connector
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
    schema_object0:
        methods: [get]
        description: 'Configure connector.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Configure connector.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                fsso-refresh-interval:
                    type: int
                    default: 180
                    description: 'FSSO refresh interval (60 - 1800 seconds).'
                fsso-sess-timeout:
                    type: int
                    default: 300
                    description: 'FSSO session timeout (30 - 600 seconds).'
                px-refresh-interval:
                    type: int
                    default: 300
                    description: 'pxGrid refresh interval (60 - 1800 seconds).'
                px-svr-timeout:
                    type: int
                    default: 900
                    description: 'pxGrid server timeout (30 - 600 seconds).'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /CLI/SYSTEM/CONNECTOR
      fmgr_cli_system_connector:
         method: <value in [set, update]>
         params:
            -
               data:
                  fsso-refresh-interval: <value of integer default: 180>
                  fsso-sess-timeout: <value of integer default: 300>
                  px-refresh-interval: <value of integer default: 300>
                  px-svr-timeout: <value of integer default: 900>

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
            fsso-refresh-interval:
               type: int
               description: 'FSSO refresh interval (60 - 1800 seconds).'
               example: 180
            fsso-sess-timeout:
               type: int
               description: 'FSSO session timeout (30 - 600 seconds).'
               example: 300
            px-refresh-interval:
               type: int
               description: 'pxGrid refresh interval (60 - 1800 seconds).'
               example: 300
            px-svr-timeout:
               type: int
               description: 'pxGrid server timeout (30 - 600 seconds).'
               example: 900
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/cli/global/system/connector'
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
            example: '/cli/global/system/connector'

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
        '/cli/global/system/connector'
    ]

    url_schema = [
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
                        'fsso-refresh-interval': {
                            'type': 'integer',
                            'default': 180,
                            'example': 180
                        },
                        'fsso-sess-timeout': {
                            'type': 'integer',
                            'default': 300,
                            'example': 300
                        },
                        'px-refresh-interval': {
                            'type': 'integer',
                            'default': 300,
                            'example': 300
                        },
                        'px-svr-timeout': {
                            'type': 'integer',
                            'default': 900,
                            'example': 900
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
