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
module: fmgr_cli_system_mail_per_object
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ delete get set update ] the following apis.
    - /cli/global/system/mail/{mail}
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
            mail:
                type: str
    schema_object0:
        methods: [delete, get]
        description: 'Alert emails.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Alert emails.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                auth:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable authentication.'
                     - 'disable - Disable authentication.'
                     - 'enable - Enable authentication.'
                    choices:
                        - 'disable'
                        - 'enable'
                id:
                    type: str
                    description: 'Mail Service ID.'
                passwd:
                    -
                        type: str
                        default: 'ENC MTI3MTE1Mzc2NTkxNzM3My6VraLxNsD7/K6FZ6oYkYSCjr1/h55a1R9hSJwHMCRyMEgllLUQEhRyvo6NfN3em5zkIyjoe2lL1IiVMHB7akT/z/3KthjsA...'
                port:
                    type: int
                    default: 25
                    description: 'SMTP server port.'
                secure-option:
                    type: str
                    default: 'default'
                    description:
                     - 'Communication secure option.'
                     - 'default - Try STARTTLS, proceed as plain text communication otherwise.'
                     - 'none - Communication will be in plain text format.'
                     - 'smtps - Communication will be protected by SMTPS.'
                     - 'starttls - Communication will be protected by STARTTLS.'
                    choices:
                        - 'default'
                        - 'none'
                        - 'smtps'
                        - 'starttls'
                server:
                    type: str
                    description: 'SMTP server.'
                user:
                    type: str
                    description: 'SMTP account username.'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /CLI/SYSTEM/MAIL/{MAIL}
      fmgr_cli_system_mail_per_object:
         method: <value in [set, update]>
         url_params:
            mail: <value of string>
         params:
            -
               data:
                  auth: <value in [disable, enable] default: 'disable'>
                  id: <value of string>
                  passwd:
                    - <value of string default: 'ENC MTI3MTE1Mzc2NTkxNzM3My6VraLxNsD7/K6FZ6oYkYSCjr1/h55a1R9hSJwHMCRyMEgllLUQ...'>
                  port: <value of integer default: 25>
                  secure-option: <value in [default, none, smtps, ...] default: 'default'>
                  server: <value of string>
                  user: <value of string>

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
            example: '/cli/global/system/mail/{mail}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            auth:
               type: str
               description: |
                  'Enable authentication.'
                  'disable - Disable authentication.'
                  'enable - Enable authentication.'
               example: 'disable'
            id:
               type: str
               description: 'Mail Service ID.'
            passwd:
               type: array
               suboptions:
                  type: str
                  example: 'ENC MTI3MTE1Mzc2NTkxNzM3My6VraLxNsD7/K6FZ6oYkYSCjr1/h55a1R9hSJwHMCRyMEgllLUQ...'
            port:
               type: int
               description: 'SMTP server port.'
               example: 25
            secure-option:
               type: str
               description: |
                  'Communication secure option.'
                  'default - Try STARTTLS, proceed as plain text communication otherwise.'
                  'none - Communication will be in plain text format.'
                  'smtps - Communication will be protected by SMTPS.'
                  'starttls - Communication will be protected by STARTTLS.'
               example: 'default'
            server:
               type: str
               description: 'SMTP server.'
            user:
               type: str
               description: 'SMTP account username.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/cli/global/system/mail/{mail}'

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
        '/cli/global/system/mail/{mail}'
    ]

    url_schema = [
        {
            'name': 'mail',
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
                        'auth': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'id': {
                            'type': 'string'
                        },
                        'passwd': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'port': {
                            'type': 'integer',
                            'default': 25,
                            'example': 25
                        },
                        'secure-option': {
                            'type': 'string',
                            'enum': [
                                'default',
                                'none',
                                'smtps',
                                'starttls'
                            ]
                        },
                        'server': {
                            'type': 'string'
                        },
                        'user': {
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
