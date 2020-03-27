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
module: fmgr_system_logfetch_clientprofile_logfilter_obj
short_description: Log content filters.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ delete get set update ] the following apis.
    - /cli/global/system/log-fetch/client-profile/{client-profile}/log-filter/{log-filter}
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
            client-profile:
                type: str
            log-filter:
                type: str
    schema_object0:
        methods: [delete, get]
        description: 'Log content filters.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Log content filters.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                field:
                    type: str
                    description: 'Field name.'
                id:
                    type: int
                    default: 0
                    description: 'Log filter ID.'
                oper:
                    type: str
                    default: '='
                    description:
                     - 'Field filter operator.'
                     - '&lt; - =Less than or equal to'
                     - '&gt; - =Greater than or equal to'
                     - 'contain - Contain'
                     - 'not-contain - Not contain'
                     - 'match - Match (expression)'
                    choices:
                        - '='
                        - '!='
                        - '<'
                        - '>'
                        - '<='
                        - '>='
                        - 'contain'
                        - 'not-contain'
                        - 'match'
                value:
                    type: str
                    description: 'Field filter operand or free-text matching expression.'

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

    - name: REQUESTING /CLI/SYSTEM/LOG-FETCH/CLIENT-PROFILE/{CLIENT-PROFILE}/LOG-FILTER/{LOG-FILTER}
      fmgr_system_logfetch_clientprofile_logfilter_obj:
         method: <value in [set, update]>
         url_params:
            client-profile: <value of string>
            log-filter: <value of string>
         params:
            -
               data:
                  field: <value of string>
                  id: <value of integer default: 0>
                  oper: <value in [=, !=, <, ...] default: '='>
                  value: <value of string>

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
            example: '/cli/global/system/log-fetch/client-profile/{client-profile}/log-filter/{log...'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            field:
               type: str
               description: 'Field name.'
            id:
               type: int
               description: 'Log filter ID.'
               example: 0
            oper:
               type: str
               description: |
                  'Field filter operator.'
                  '&lt; - =Less than or equal to'
                  '&gt; - =Greater than or equal to'
                  'contain - Contain'
                  'not-contain - Not contain'
                  'match - Match (expression)'
               example: '='
            value:
               type: str
               description: 'Field filter operand or free-text matching expression.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/cli/global/system/log-fetch/client-profile/{client-profile}/log-filter/{log...'

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
        '/cli/global/system/log-fetch/client-profile/{client-profile}/log-filter/{log-filter}'
    ]

    url_schema = [
        {
            'name': 'client-profile',
            'type': 'string'
        },
        {
            'name': 'log-filter',
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
                        'field': {
                            'type': 'string'
                        },
                        'id': {
                            'type': 'integer',
                            'default': 0,
                            'example': 0
                        },
                        'oper': {
                            'type': 'string',
                            'enum': [
                                '=',
                                '!=',
                                '<',
                                '>',
                                '<=',
                                '>=',
                                'contain',
                                'not-contain',
                                'match'
                            ]
                        },
                        'value': {
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

    module.exit_json(meta=response[1])


if __name__ == '__main__':
    main()
