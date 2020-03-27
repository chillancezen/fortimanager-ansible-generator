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
module: fmgr_waf_profile_signature_customsignature_obj
short_description: Custom signature.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/waf/profile/{profile}/signature/custom-signature/{custom-signature}
    - /pm/config/global/obj/waf/profile/{profile}/signature/custom-signature/{custom-signature}
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
            profile:
                type: str
            custom-signature:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Custom signature.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                action:
                    type: str
                    description: 'Action.'
                    choices:
                        - 'allow'
                        - 'block'
                        - 'erase'
                case-sensitivity:
                    type: str
                    description: 'Case sensitivity in pattern.'
                    choices:
                        - 'disable'
                        - 'enable'
                direction:
                    type: str
                    description: 'Traffic direction.'
                    choices:
                        - 'request'
                        - 'response'
                log:
                    type: str
                    description: 'Enable/disable logging.'
                    choices:
                        - 'disable'
                        - 'enable'
                name:
                    type: str
                    description: 'Signature name.'
                pattern:
                    type: str
                    description: 'Match pattern.'
                severity:
                    type: str
                    description: 'Severity.'
                    choices:
                        - 'low'
                        - 'medium'
                        - 'high'
                status:
                    type: str
                    description: 'Status.'
                    choices:
                        - 'disable'
                        - 'enable'
                target:
                    -
                        type: str
                        choices:
                            - 'arg'
                            - 'arg-name'
                            - 'req-body'
                            - 'req-cookie'
                            - 'req-cookie-name'
                            - 'req-filename'
                            - 'req-header'
                            - 'req-header-name'
                            - 'req-raw-uri'
                            - 'req-uri'
                            - 'resp-body'
                            - 'resp-hdr'
                            - 'resp-status'
    schema_object1:
        methods: [delete]
        description: 'Custom signature.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Custom signature.'
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

    - name: REQUESTING /PM/CONFIG/OBJ/WAF/PROFILE/{PROFILE}/SIGNATURE/CUSTOM-SIGNATURE/{CUSTOM-SIGNATURE}
      fmgr_waf_profile_signature_customsignature_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
            custom-signature: <value of string>
         params:
            -
               data:
                  action: <value in [allow, block, erase]>
                  case-sensitivity: <value in [disable, enable]>
                  direction: <value in [request, response]>
                  log: <value in [disable, enable]>
                  name: <value of string>
                  pattern: <value of string>
                  severity: <value in [low, medium, high]>
                  status: <value in [disable, enable]>
                  target:
                    - <value in [arg, arg-name, req-body, ...]>

    - name: REQUESTING /PM/CONFIG/OBJ/WAF/PROFILE/{PROFILE}/SIGNATURE/CUSTOM-SIGNATURE/{CUSTOM-SIGNATURE}
      fmgr_waf_profile_signature_customsignature_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
            custom-signature: <value of string>
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
            example: '/pm/config/adom/{adom}/obj/waf/profile/{profile}/signature/custom-signature/...'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            action:
               type: str
               description: 'Action.'
            case-sensitivity:
               type: str
               description: 'Case sensitivity in pattern.'
            direction:
               type: str
               description: 'Traffic direction.'
            log:
               type: str
               description: 'Enable/disable logging.'
            name:
               type: str
               description: 'Signature name.'
            pattern:
               type: str
               description: 'Match pattern.'
            severity:
               type: str
               description: 'Severity.'
            status:
               type: str
               description: 'Status.'
            target:
               type: array
               suboptions:
                  type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/waf/profile/{profile}/signature/custom-signature/...'

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
        '/pm/config/adom/{adom}/obj/waf/profile/{profile}/signature/custom-signature/{custom-signature}',
        '/pm/config/global/obj/waf/profile/{profile}/signature/custom-signature/{custom-signature}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'profile',
            'type': 'string'
        },
        {
            'name': 'custom-signature',
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
                        'action': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'block',
                                'erase'
                            ]
                        },
                        'case-sensitivity': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'direction': {
                            'type': 'string',
                            'enum': [
                                'request',
                                'response'
                            ]
                        },
                        'log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'name': {
                            'type': 'string'
                        },
                        'pattern': {
                            'type': 'string'
                        },
                        'severity': {
                            'type': 'string',
                            'enum': [
                                'low',
                                'medium',
                                'high'
                            ]
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'target': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'arg',
                                    'arg-name',
                                    'req-body',
                                    'req-cookie',
                                    'req-cookie-name',
                                    'req-filename',
                                    'req-header',
                                    'req-header-name',
                                    'req-raw-uri',
                                    'req-uri',
                                    'resp-body',
                                    'resp-hdr',
                                    'resp-status'
                                ]
                            }
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
