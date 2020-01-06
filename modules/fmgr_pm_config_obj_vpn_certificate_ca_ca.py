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
module: fmgr_pm_config_obj_vpn_certificate_ca_ca
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/vpn/certificate/ca/{ca}
    - /pm/config/global/obj/vpn/certificate/ca/{ca}
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
            ca:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'CA certificate.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                _private_key:
                    type: str
                auto-update-days:
                    type: int
                    description: 'Number of days to wait before requesting an updated CA certificate (0 - 4294967295, 0 = disabled).'
                auto-update-days-warning:
                    type: int
                    description: 'Number of days before an expiry-warning message is generated (0 - 4294967295, 0 = disabled).'
                ca:
                    type: str
                    description: 'CA certificate as a PEM file.'
                last-updated:
                    type: int
                    description: 'Time at which CA was last updated.'
                name:
                    type: str
                    description: 'Name.'
                range:
                    type: str
                    description: 'Either global or VDOM IP address range for the CA certificate.'
                    choices:
                        - global
                        - vdom
                scep-url:
                    type: str
                    description: 'URL of the SCEP server.'
                source:
                    type: str
                    description: 'CA certificate source type.'
                    choices:
                        - factory
                        - user
                        - bundle
                        - fortiguard
                source-ip:
                    type: str
                    description: 'Source IP address for communications to the SCEP server.'
                trusted:
                    type: str
                    description: 'Enable/disable as a trusted CA.'
                    choices:
                        - disable
                        - enable
    schema_object1:
        methods: [delete]
        description: 'CA certificate.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'CA certificate.'
        api_categories: [api_tag0]
        api_tag0:
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the object will be returned.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'chksum - Return the check-sum value instead of attributes.'
                choices:
                    - object member
                    - chksum
                    - datasrc

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /pm/config/obj/vpn/certificate/ca/{ca}
      fmgr_pm_config_obj_vpn_certificate_ca_ca:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            ca: <value of string>
         params:
            - 
               data: 
                  _private_key: <value of string>
                  auto-update-days: <value of integer>
                  auto-update-days-warning: <value of integer>
                  ca: <value of string>
                  last-updated: <value of integer>
                  name: <value of string>
                  range: <value in [global, vdom]>
                  scep-url: <value of string>
                  source: <value in [factory, user, bundle, ...]>
                  source-ip: <value of string>
                  trusted: <value in [disable, enable]>
    - name: send request to /pm/config/obj/vpn/certificate/ca/{ca}
      fmgr_pm_config_obj_vpn_certificate_ca_ca:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            ca: <value of string>
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
            example: /pm/config/adom/{adom}/obj/vpn/certificate/ca/{ca}
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            _private_key:
               type: str
            auto-update-days:
               type: int
               description: 'Number of days to wait before requesting an updated CA certificate (0 - 4294967295, 0 = disabled).'
            auto-update-days-warning:
               type: int
               description: 'Number of days before an expiry-warning message is generated (0 - 4294967295, 0 = disabled).'
            ca:
               type: str
               description: 'CA certificate as a PEM file.'
            last-updated:
               type: int
               description: 'Time at which CA was last updated.'
            name:
               type: str
               description: 'Name.'
            range:
               type: str
               description: 'Either global or VDOM IP address range for the CA certificate.'
            scep-url:
               type: str
               description: 'URL of the SCEP server.'
            source:
               type: str
               description: 'CA certificate source type.'
            source-ip:
               type: str
               description: 'Source IP address for communications to the SCEP server.'
            trusted:
               type: str
               description: 'Enable/disable as a trusted CA.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/obj/vpn/certificate/ca/{ca}

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
        '/pm/config/adom/{adom}/obj/vpn/certificate/ca/{ca}',
        '/pm/config/global/obj/vpn/certificate/ca/{ca}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'ca',
            'type': 'string'
        }
    ]

    body_schema =  {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        '_private_key': {
                            'type': 'string'
                        },
                        'auto-update-days': {
                            'type': 'integer'
                        },
                        'auto-update-days-warning': {
                            'type': 'integer'
                        },
                        'ca': {
                            'type': 'string'
                        },
                        'last-updated': {
                            'type': 'integer'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'range': {
                            'type': 'string',
                            'enum': [
                                'global',
                                'vdom'
                            ]
                        },
                        'scep-url': {
                            'type': 'string'
                        },
                        'source': {
                            'type': 'string',
                            'enum': [
                                'factory',
                                'user',
                                'bundle',
                                'fortiguard'
                            ]
                        },
                        'source-ip': {
                            'type': 'string'
                        },
                        'trusted': {
                            'type': 'string',
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