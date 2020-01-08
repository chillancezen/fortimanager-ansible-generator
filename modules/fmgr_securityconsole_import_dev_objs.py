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
module: fmgr_securityconsole_import_dev_objs
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ exec ] the following apis.
    - /securityconsole/import/dev/objs
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
        methods: [exec]
        description: 'Import objects from device to ADOM, or from ADOM to Global.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                add_mappings:
                    type: str
                    default: 'disable'
                    description: 'Automatically add required dynamic mappings for the device during the search stages.<br/>When used in policy_search action...'
                    choices:
                        - 'disable'
                        - 'enable'
                adom:
                    type: str
                    description: 'Source ADOM name.'
                dst_name:
                    type: str
                    description: 'Name of the policy package where the objects are to be imported. If the package does not already exist in the database, a ...'
                dst_parent:
                    type: str
                    description: 'Path to the folder for the target package. If the package is to be placed in root, leave this field blank.'
                if_all_objs:
                    type: str
                    default: 'none'
                    choices:
                        - 'none'
                        - 'all'
                        - 'filter'
                if_all_policy:
                    type: str
                    default: 'disable'
                    choices:
                        - 'disable'
                        - 'enable'
                import_action:
                    type: str
                    default: 'do'
                    description:
                     - 'do - Perform the policy and object import.'
                     - 'policy_search - Preprocess and scan through device database to gather information about policies that need to be imported. Can autom...'
                     - 'obj_search - Preprocess and scan through device database to collect objects that are required to be imported. Can automatically add ...'
                    choices:
                        - 'do'
                        - 'policy_search'
                        - 'obj_search'
                name:
                    type: str
                    description: 'Source device name.'
                position:
                    type: str
                    default: 'top'
                    choices:
                        - 'bottom'
                        - 'top'
                vdom:
                    type: str

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /SECURITYCONSOLE/IMPORT/DEV/OBJS
      fmgr_securityconsole_import_dev_objs:
         method: <value in [exec]>
         params:
            -
               data:
                  add_mappings: <value in [disable, enable] default: 'disable'>
                  adom: <value of string>
                  dst_name: <value of string>
                  dst_parent: <value of string>
                  if_all_objs: <value in [none, all, filter] default: 'none'>
                  if_all_policy: <value in [disable, enable] default: 'disable'>
                  import_action: <value in [do, policy_search, obj_search] default: 'do'>
                  name: <value of string>
                  position: <value in [bottom, top] default: 'top'>
                  vdom: <value of string>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[exec]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            task:
               type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/securityconsole/import/dev/objs'

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
        '/securityconsole/import/dev/objs'
    ]

    url_schema = [
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'add_mappings': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'adom': {
                            'type': 'string'
                        },
                        'dst_name': {
                            'type': 'string'
                        },
                        'dst_parent': {
                            'type': 'string'
                        },
                        'if_all_objs': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'all',
                                'filter'
                            ]
                        },
                        'if_all_policy': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'import_action': {
                            'type': 'string',
                            'enum': [
                                'do',
                                'policy_search',
                                'obj_search'
                            ]
                        },
                        'name': {
                            'type': 'string'
                        },
                        'position': {
                            'type': 'string',
                            'enum': [
                                'bottom',
                                'top'
                            ]
                        },
                        'vdom': {
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
            'exec': 'object0'
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
                'exec'
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
