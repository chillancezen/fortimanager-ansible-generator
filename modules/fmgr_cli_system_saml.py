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
module: fmgr_cli_system_saml
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis:
    - /cli/global/system/saml
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
        methods: [get]
        description: 'Global settings for SAML authentication.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Global settings for SAML authentication.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                acs-url:
                    type: str
                    description: 'SP ACS(login) URL.'
                cert:
                    type: str
                    description: 'Certificate name.'
                entity-id:
                    type: str
                    description: 'SP entity ID.'
                idp-cert:
                    type: str
                    description: 'IDP Certificate name.'
                idp-entity-id:
                    type: str
                    description: 'IDP entity ID.'
                idp-single-logout-url:
                    type: str
                    description: 'IDP single logout url.'
                idp-single-sign-on-url:
                    type: str
                    description: 'IDP single sign-on URL.'
                login-auto-redirect:
                    type: str
                    default: disable
                    description:
                     - 'Enable/Disable auto redirect to IDP login page.'
                     - 'disable - Disable auto redirect to IDP Login Page.'
                     - 'enable - Enable auto redirect to IDP Login Page.'
                    choices:
                        - disable
                        - enable
                role:
                    type: str
                    default: SP
                    description:
                     - 'SAML role.'
                     - 'IDP - IDentiy Provider.'
                     - 'SP - Service Provider.'
                    choices:
                        - IDP
                        - SP
                server-address:
                    type: str
                    description: 'server address.'
                service-providers:
                    -
                        idp-entity-id:
                            type: str
                            description: 'IDP Entity ID.'
                        idp-single-logout-url:
                            type: str
                            description: 'IDP single logout url.'
                        idp-single-sign-on-url:
                            type: str
                            description: 'IDP single sign-on URL.'
                        name:
                            type: str
                            description: 'Name.'
                        prefix:
                            type: str
                            description: 'Prefix.'
                        sp-cert:
                            type: str
                            description: 'SP certificate name.'
                        sp-entity-id:
                            type: str
                            description: 'SP Entity ID.'
                        sp-single-logout-url:
                            type: str
                            description: 'SP single logout URL.'
                        sp-single-sign-on-url:
                            type: str
                            description: 'SP single sign-on URL.'
                sls-url:
                    type: str
                    description: 'SP SLS(logout) URL.'
                status:
                    type: str
                    default: disable
                    description:
                     - 'Enable/disable SAML authentication (default = disable).'
                     - 'disable - Disable SAML authentication.'
                     - 'enable - Enabld SAML authentication.'
                    choices:
                        - disable
                        - enable

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /cli/system/saml
      fmgr_cli_system_saml:
         method: <value in [set, update]>
         params:
            - 
               data: 
                  acs-url: <value of string>
                  cert: <value of string>
                  entity-id: <value of string>
                  idp-cert: <value of string>
                  idp-entity-id: <value of string>
                  idp-single-logout-url: <value of string>
                  idp-single-sign-on-url: <value of string>
                  login-auto-redirect: <value in [disable, enable] default: disable>
                  role: <value in [IDP, SP] default: SP>
                  server-address: <value of string>
                  service-providers: 
                   - 
                        idp-entity-id: <value of string>
                        idp-single-logout-url: <value of string>
                        idp-single-sign-on-url: <value of string>
                        name: <value of string>
                        prefix: <value of string>
                        sp-cert: <value of string>
                        sp-entity-id: <value of string>
                        sp-single-logout-url: <value of string>
                        sp-single-sign-on-url: <value of string>
                  sls-url: <value of string>
                  status: <value in [disable, enable] default: disable>

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
            acs-url:
               type: str
               description: 'SP ACS(login) URL.'
            cert:
               type: str
               description: 'Certificate name.'
            entity-id:
               type: str
               description: 'SP entity ID.'
            idp-cert:
               type: str
               description: 'IDP Certificate name.'
            idp-entity-id:
               type: str
               description: 'IDP entity ID.'
            idp-single-logout-url:
               type: str
               description: 'IDP single logout url.'
            idp-single-sign-on-url:
               type: str
               description: 'IDP single sign-on URL.'
            login-auto-redirect:
               type: str
               description: |
                  'Enable/Disable auto redirect to IDP login page.'
                  'disable - Disable auto redirect to IDP Login Page.'
                  'enable - Enable auto redirect to IDP Login Page.'
               example: disable
            role:
               type: str
               description: |
                  'SAML role.'
                  'IDP - IDentiy Provider.'
                  'SP - Service Provider.'
               example: SP
            server-address:
               type: str
               description: 'server address.'
            service-providers:
               type: array
               suboptions:
                  idp-entity-id:
                     type: str
                     description: 'IDP Entity ID.'
                  idp-single-logout-url:
                     type: str
                     description: 'IDP single logout url.'
                  idp-single-sign-on-url:
                     type: str
                     description: 'IDP single sign-on URL.'
                  name:
                     type: str
                     description: 'Name.'
                  prefix:
                     type: str
                     description: 'Prefix.'
                  sp-cert:
                     type: str
                     description: 'SP certificate name.'
                  sp-entity-id:
                     type: str
                     description: 'SP Entity ID.'
                  sp-single-logout-url:
                     type: str
                     description: 'SP single logout URL.'
                  sp-single-sign-on-url:
                     type: str
                     description: 'SP single sign-on URL.'
            sls-url:
               type: str
               description: 'SP SLS(logout) URL.'
            status:
               type: str
               description: |
                  'Enable/disable SAML authentication (default = disable).'
                  'disable - Disable SAML authentication.'
                  'enable - Enabld SAML authentication.'
               example: disable
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /cli/global/system/saml
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
            example: /cli/global/system/saml

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
        '/cli/global/system/saml'
    ]

    url_schema = [
    ]

    body_schema =  {
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
                        'acs-url': {
                            'type': 'string'
                        },
                        'cert': {
                            'type': 'string'
                        },
                        'entity-id': {
                            'type': 'string'
                        },
                        'idp-cert': {
                            'type': 'string'
                        },
                        'idp-entity-id': {
                            'type': 'string'
                        },
                        'idp-single-logout-url': {
                            'type': 'string'
                        },
                        'idp-single-sign-on-url': {
                            'type': 'string'
                        },
                        'login-auto-redirect': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'role': {
                            'type': 'string',
                            'default': 'SP',
                            'enum': [
                                'IDP',
                                'SP'
                            ]
                        },
                        'server-address': {
                            'type': 'string'
                        },
                        'service-providers': {
                            'type': 'array',
                            'items': {
                                'idp-entity-id': {
                                    'type': 'string'
                                },
                                'idp-single-logout-url': {
                                    'type': 'string'
                                },
                                'idp-single-sign-on-url': {
                                    'type': 'string'
                                },
                                'name': {
                                    'type': 'string'
                                },
                                'prefix': {
                                    'type': 'string'
                                },
                                'sp-cert': {
                                    'type': 'string'
                                },
                                'sp-entity-id': {
                                    'type': 'string'
                                },
                                'sp-single-logout-url': {
                                    'type': 'string'
                                },
                                'sp-single-sign-on-url': {
                                    'type': 'string'
                                }
                            }
                        },
                        'sls-url': {
                            'type': 'string'
                        },
                        'status': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
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