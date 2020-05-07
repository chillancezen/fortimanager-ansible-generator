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
module: fmgr_firewall_profileprotocoloptions_smtp
short_description: Configure SMTP protocol options.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/firewall/profile-protocol-options/{profile-protocol-options}/smtp
    - /pm/config/global/obj/firewall/profile-protocol-options/{profile-protocol-options}/smtp
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
    loose_validation:
        description: Do parameter validation in a loose way
        required: False
        type: bool
        default: false
    workspace_locking_adom:
        description: the adom to lock in case FortiManager running in workspace mode
        required: False
        type: string
        choices:
          - global
          - custom adom
    workspace_locking_timeout:
        description: teh maximum time in seconds to wait for other user to release the workspace lock
        required: False
        type: integer
        default: 300
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
            profile-protocol-options:
                type: str
    schema_object0:
        methods: [get]
        description: 'Configure SMTP protocol options.'
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
        description: 'Configure SMTP protocol options.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                inspect-all:
                    type: str
                    description: 'Enable/disable the inspection of all ports for the protocol.'
                    choices:
                        - 'disable'
                        - 'enable'
                options:
                    -
                        type: str
                        choices:
                            - 'oversize'
                            - 'fragmail'
                            - 'no-content-summary'
                            - 'splice'
                oversize-limit:
                    type: int
                    description: 'Maximum in-memory file size that can be scanned (1 - 383 MB, default = 10).'
                ports:
                    -
                        type: int
                scan-bzip2:
                    type: str
                    description: 'Enable/disable scanning of BZip2 compressed files.'
                    choices:
                        - 'disable'
                        - 'enable'
                server-busy:
                    type: str
                    description: 'Enable/disable SMTP server busy when server not available.'
                    choices:
                        - 'disable'
                        - 'enable'
                status:
                    type: str
                    description: 'Enable/disable the active status of scanning for this protocol.'
                    choices:
                        - 'disable'
                        - 'enable'
                uncompressed-nest-limit:
                    type: int
                    description: 'Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).'
                uncompressed-oversize-limit:
                    type: int
                    description: 'Maximum in-memory uncompressed file size that can be scanned (0 - 383 MB, 0 = unlimited, default = 10).'

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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/PROFILE-PROTOCOL-OPTIONS/{PROFILE-PROTOCOL-OPTIONS}/SMTP
      fmgr_firewall_profileprotocoloptions_smtp:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile-protocol-options: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/PROFILE-PROTOCOL-OPTIONS/{PROFILE-PROTOCOL-OPTIONS}/SMTP
      fmgr_firewall_profileprotocoloptions_smtp:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile-protocol-options: <value of string>
         params:
            -
               data:
                  inspect-all: <value in [disable, enable]>
                  options:
                    - <value in [oversize, fragmail, no-content-summary, ...]>
                  oversize-limit: <value of integer>
                  ports:
                    - <value of integer>
                  scan-bzip2: <value in [disable, enable]>
                  server-busy: <value in [disable, enable]>
                  status: <value in [disable, enable]>
                  uncompressed-nest-limit: <value of integer>
                  uncompressed-oversize-limit: <value of integer>

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
            inspect-all:
               type: str
               description: 'Enable/disable the inspection of all ports for the protocol.'
            options:
               type: array
               suboptions:
                  type: str
            oversize-limit:
               type: int
               description: 'Maximum in-memory file size that can be scanned (1 - 383 MB, default = 10).'
            ports:
               type: array
               suboptions:
                  type: int
            scan-bzip2:
               type: str
               description: 'Enable/disable scanning of BZip2 compressed files.'
            server-busy:
               type: str
               description: 'Enable/disable SMTP server busy when server not available.'
            status:
               type: str
               description: 'Enable/disable the active status of scanning for this protocol.'
            uncompressed-nest-limit:
               type: int
               description: 'Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).'
            uncompressed-oversize-limit:
               type: int
               description: 'Maximum in-memory uncompressed file size that can be scanned (0 - 383 MB, 0 = unlimited, default = 10).'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/firewall/profile-protocol-options/{profile-protoc...'
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
            example: '/pm/config/adom/{adom}/obj/firewall/profile-protocol-options/{profile-protoc...'

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
        '/pm/config/adom/{adom}/obj/firewall/profile-protocol-options/{profile-protocol-options}/smtp',
        '/pm/config/global/obj/firewall/profile-protocol-options/{profile-protocol-options}/smtp'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'profile-protocol-options',
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
                        'inspect-all': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'options': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'oversize',
                                    'fragmail',
                                    'no-content-summary',
                                    'splice'
                                ]
                            }
                        },
                        'oversize-limit': {
                            'type': 'integer'
                        },
                        'ports': {
                            'type': 'array',
                            'items': {
                                'type': 'integer'
                            }
                        },
                        'scan-bzip2': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'server-busy': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'uncompressed-nest-limit': {
                            'type': 'integer'
                        },
                        'uncompressed-oversize-limit': {
                            'type': 'integer'
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
        'loose_validation': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'workspace_locking_adom': {
            'type': 'str',
            'required': False
        },
        'workspace_locking_timeout': {
            'type': 'int',
            'required': False,
            'default': 300
        },
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
