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
module: fmgr_fmupdate_webspam_webproxy
short_description: Configure the web proxy for use with FortiGuard antivirus and IPS updates.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /cli/global/fmupdate/web-spam/web-proxy
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
        description: 'Configure the web proxy for use with FortiGuard antivirus and IPS updates.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Configure the web proxy for use with FortiGuard antivirus and IPS updates.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                ip:
                    type: str
                    default: '0.0.0.0'
                    description: 'IPv4 address of the web proxy.'
                ip6:
                    type: str
                    default: '::'
                    description: 'IPv6 address of the web proxy.'
                mode:
                    type: str
                    default: 'proxy'
                    description:
                     - 'Web proxy mode: proxy - http proxy, tunnel - http tunnel (default = proxy).'
                     - 'proxy - HTTP proxy.'
                     - 'tunnel - HTTP tunnel.'
                    choices:
                        - 'proxy'
                        - 'tunnel'
                password:
                    -
                        type: str
                        default: 'ENC MTQ4ODM1MjcyOTk3ODExNreUBchLdkFIbIbcd8CigXCsJs8gguZ6mOjknXBH4Tm3shANGNo7nlVP8rFMUYX0OzAZMe+28CSkktL4ruOhitTk30S9SNOWi...'
                port:
                    type: int
                    default: 80
                    description: 'The port number of the web proxy (1 - 65535, default = 80).'
                status:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable connections through the web proxy (default = disable).'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                username:
                    type: str
                    description: 'The user name used for authentication.'

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

    - name: REQUESTING /CLI/FMUPDATE/WEB-SPAM/WEB-PROXY
      fmgr_fmupdate_webspam_webproxy:
         method: <value in [set, update]>
         params:
            -
               data:
                  ip: <value of string default: '0.0.0.0'>
                  ip6: <value of string default: '::'>
                  mode: <value in [proxy, tunnel] default: 'proxy'>
                  password:
                    - <value of string default: 'ENC MTQ4ODM1MjcyOTk3ODExNreUBchLdkFIbIbcd8CigXCsJs8gguZ6mOjknXBH4Tm3shANGNo7...'>
                  port: <value of integer default: 80>
                  status: <value in [disable, enable] default: 'disable'>
                  username: <value of string>

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
            ip:
               type: str
               description: 'IPv4 address of the web proxy.'
               example: '0.0.0.0'
            ip6:
               type: str
               description: 'IPv6 address of the web proxy.'
               example: '::'
            mode:
               type: str
               description: |
                  'Web proxy mode: proxy - http proxy, tunnel - http tunnel (default = proxy).'
                  'proxy - HTTP proxy.'
                  'tunnel - HTTP tunnel.'
               example: 'proxy'
            password:
               type: array
               suboptions:
                  type: str
                  example: 'ENC MTQ4ODM1MjcyOTk3ODExNreUBchLdkFIbIbcd8CigXCsJs8gguZ6mOjknXBH4Tm3shANGNo7...'
            port:
               type: int
               description: 'The port number of the web proxy (1 - 65535, default = 80).'
               example: 80
            status:
               type: str
               description: |
                  'Enable/disable connections through the web proxy (default = disable).'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'disable'
            username:
               type: str
               description: 'The user name used for authentication.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/cli/global/fmupdate/web-spam/web-proxy'
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
            example: '/cli/global/fmupdate/web-spam/web-proxy'

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
        '/cli/global/fmupdate/web-spam/web-proxy'
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
                        'ip': {
                            'type': 'string'
                        },
                        'ip6': {
                            'type': 'string'
                        },
                        'mode': {
                            'type': 'string',
                            'enum': [
                                'proxy',
                                'tunnel'
                            ]
                        },
                        'password': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'port': {
                            'type': 'integer',
                            'default': 80,
                            'example': 80
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'username': {
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
