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
module: fmgr_cli_system_admin_profile_datamask_custom_fields_per_object
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ delete get set update ] the following apis.
    - /cli/global/system/admin/profile/{profile}/datamask-custom-fields/{datamask-custom-fields}
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
            profile:
                type: str
            datamask-custom-fields:
                type: str
    schema_object0:
        methods: [delete, get]
        description: 'Customized datamask fields.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Customized datamask fields.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                field-category:
                    -
                        type: str
                        choices:
                            - 'log'
                            - 'fortiview'
                            - 'alert'
                            - 'ueba'
                            - 'all'
                field-name:
                    type: str
                    description: 'Field name.'
                field-status:
                    type: str
                    default: 'enable'
                    description:
                     - 'Field status.'
                     - 'disable - Disable field.'
                     - 'enable - Enable field.'
                    choices:
                        - 'disable'
                        - 'enable'
                field-type:
                    type: str
                    default: 'string'
                    description:
                     - 'Field type.'
                     - 'string - String.'
                     - 'ip - IP.'
                     - 'mac - MAC address.'
                     - 'email - Email address.'
                     - 'unknown - Unknown.'
                    choices:
                        - 'string'
                        - 'ip'
                        - 'mac'
                        - 'email'
                        - 'unknown'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /CLI/SYSTEM/ADMIN/PROFILE/{PROFILE}/DATAMASK-CUSTOM-FIELDS/{DATAMASK-CUSTOM-FIELDS}
      fmgr_cli_system_admin_profile_datamask_custom_fields_per_object:
         method: <value in [set, update]>
         url_params:
            profile: <value of string>
            datamask-custom-fields: <value of string>
         params:
            -
               data:
                  field-category:
                    - <value in [log, fortiview, alert, ...]>
                  field-name: <value of string>
                  field-status: <value in [disable, enable] default: 'enable'>
                  field-type: <value in [string, ip, mac, ...] default: 'string'>

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
            example: '/cli/global/system/admin/profile/{profile}/datamask-custom-fields/{datamask-...'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            field-category:
               type: array
               suboptions:
                  type: str
            field-name:
               type: str
               description: 'Field name.'
            field-status:
               type: str
               description: |
                  'Field status.'
                  'disable - Disable field.'
                  'enable - Enable field.'
               example: 'enable'
            field-type:
               type: str
               description: |
                  'Field type.'
                  'string - String.'
                  'ip - IP.'
                  'mac - MAC address.'
                  'email - Email address.'
                  'unknown - Unknown.'
               example: 'string'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/cli/global/system/admin/profile/{profile}/datamask-custom-fields/{datamask-...'

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
        '/cli/global/system/admin/profile/{profile}/datamask-custom-fields/{datamask-custom-fields}'
    ]

    url_schema = [
        {
            'name': 'profile',
            'type': 'string'
        },
        {
            'name': 'datamask-custom-fields',
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
                        'field-category': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'log',
                                    'fortiview',
                                    'alert',
                                    'ueba',
                                    'all'
                                ]
                            }
                        },
                        'field-name': {
                            'type': 'string'
                        },
                        'field-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'field-type': {
                            'type': 'string',
                            'enum': [
                                'string',
                                'ip',
                                'mac',
                                'email',
                                'unknown'
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
