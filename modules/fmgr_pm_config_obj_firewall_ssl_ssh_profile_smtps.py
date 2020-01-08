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
module: fmgr_pm_config_obj_firewall_ssl_ssh_profile_smtps
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/firewall/ssl-ssh-profile/{ssl-ssh-profile}/smtps
    - /pm/config/global/obj/firewall/ssl-ssh-profile/{ssl-ssh-profile}/smtps
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
            ssl-ssh-profile:
                type: str
    schema_object0:
        methods: [get]
        description: 'Configure SMTPS options.'
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
    schema_object1:
        methods: [set, update]
        description: 'Configure SMTPS options.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                allow-invalid-server-cert:
                    type: str
                    description: 'When enabled, allows SSL sessions whose server certificate validation failed.'
                    choices:
                        - 'disable'
                        - 'enable'
                client-cert-request:
                    type: str
                    description: 'Action based on client certificate request.'
                    choices:
                        - 'bypass'
                        - 'inspect'
                        - 'block'
                ports:
                    -
                        type: int
                status:
                    type: str
                    description: 'Configure protocol inspection status.'
                    choices:
                        - 'disable'
                        - 'deep-inspection'
                unsupported-ssl:
                    type: str
                    description: 'Action based on the SSL encryption used being unsupported.'
                    choices:
                        - 'bypass'
                        - 'inspect'
                        - 'block'
                untrusted-cert:
                    type: str
                    description: 'Allow, ignore, or block the untrusted SSL session server certificate.'
                    choices:
                        - 'allow'
                        - 'block'
                        - 'ignore'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/SSL-SSH-PROFILE/{SSL-SSH-PROFILE}/SMTPS
      fmgr_pm_config_obj_firewall_ssl_ssh_profile_smtps:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            ssl-ssh-profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/SSL-SSH-PROFILE/{SSL-SSH-PROFILE}/SMTPS
      fmgr_pm_config_obj_firewall_ssl_ssh_profile_smtps:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            ssl-ssh-profile: <value of string>
         params:
            -
               data:
                  allow-invalid-server-cert: <value in [disable, enable]>
                  client-cert-request: <value in [bypass, inspect, block]>
                  ports:
                    - <value of integer>
                  status: <value in [disable, deep-inspection]>
                  unsupported-ssl: <value in [bypass, inspect, block]>
                  untrusted-cert: <value in [allow, block, ignore]>

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
            allow-invalid-server-cert:
               type: str
               description: 'When enabled, allows SSL sessions whose server certificate validation failed.'
            client-cert-request:
               type: str
               description: 'Action based on client certificate request.'
            ports:
               type: array
               suboptions:
                  type: int
            status:
               type: str
               description: 'Configure protocol inspection status.'
            unsupported-ssl:
               type: str
               description: 'Action based on the SSL encryption used being unsupported.'
            untrusted-cert:
               type: str
               description: 'Allow, ignore, or block the untrusted SSL session server certificate.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/firewall/ssl-ssh-profile/{ssl-ssh-profile}/smtps'
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
            example: '/pm/config/adom/{adom}/obj/firewall/ssl-ssh-profile/{ssl-ssh-profile}/smtps'

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
        '/pm/config/adom/{adom}/obj/firewall/ssl-ssh-profile/{ssl-ssh-profile}/smtps',
        '/pm/config/global/obj/firewall/ssl-ssh-profile/{ssl-ssh-profile}/smtps'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'ssl-ssh-profile',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
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
            ],
            'object1': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'allow-invalid-server-cert': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'client-cert-request': {
                            'type': 'string',
                            'enum': [
                                'bypass',
                                'inspect',
                                'block'
                            ]
                        },
                        'ports': {
                            'type': 'array',
                            'items': {
                                'type': 'integer'
                            }
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'deep-inspection'
                            ]
                        },
                        'unsupported-ssl': {
                            'type': 'string',
                            'enum': [
                                'bypass',
                                'inspect',
                                'block'
                            ]
                        },
                        'untrusted-cert': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'block',
                                'ignore'
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
