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
module: fmgr_firewall_vip6_sslciphersuites_obj
short_description: SSL/TLS cipher suites acceptable from a client, ordered by priority.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/firewall/vip6/{vip6}/ssl-cipher-suites/{ssl-cipher-suites}
    - /pm/config/global/obj/firewall/vip6/{vip6}/ssl-cipher-suites/{ssl-cipher-suites}
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
            vip6:
                type: str
            ssl-cipher-suites:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'SSL/TLS cipher suites acceptable from a client, ordered by priority.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                cipher:
                    type: str
                    description: 'Cipher suite name.'
                    choices:
                        - 'TLS-RSA-WITH-RC4-128-MD5'
                        - 'TLS-RSA-WITH-RC4-128-SHA'
                        - 'TLS-RSA-WITH-DES-CBC-SHA'
                        - 'TLS-RSA-WITH-3DES-EDE-CBC-SHA'
                        - 'TLS-RSA-WITH-AES-128-CBC-SHA'
                        - 'TLS-RSA-WITH-AES-256-CBC-SHA'
                        - 'TLS-RSA-WITH-AES-128-CBC-SHA256'
                        - 'TLS-RSA-WITH-AES-256-CBC-SHA256'
                        - 'TLS-RSA-WITH-CAMELLIA-128-CBC-SHA'
                        - 'TLS-RSA-WITH-CAMELLIA-256-CBC-SHA'
                        - 'TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256'
                        - 'TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256'
                        - 'TLS-RSA-WITH-SEED-CBC-SHA'
                        - 'TLS-RSA-WITH-ARIA-128-CBC-SHA256'
                        - 'TLS-RSA-WITH-ARIA-256-CBC-SHA384'
                        - 'TLS-DHE-RSA-WITH-DES-CBC-SHA'
                        - 'TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA'
                        - 'TLS-DHE-RSA-WITH-AES-128-CBC-SHA'
                        - 'TLS-DHE-RSA-WITH-AES-256-CBC-SHA'
                        - 'TLS-DHE-RSA-WITH-AES-128-CBC-SHA256'
                        - 'TLS-DHE-RSA-WITH-AES-256-CBC-SHA256'
                        - 'TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA'
                        - 'TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA'
                        - 'TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256'
                        - 'TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256'
                        - 'TLS-DHE-RSA-WITH-SEED-CBC-SHA'
                        - 'TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256'
                        - 'TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384'
                        - 'TLS-ECDHE-RSA-WITH-RC4-128-SHA'
                        - 'TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA'
                        - 'TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA'
                        - 'TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA'
                        - 'TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256'
                        - 'TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256'
                        - 'TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256'
                        - 'TLS-DHE-RSA-WITH-AES-128-GCM-SHA256'
                        - 'TLS-DHE-RSA-WITH-AES-256-GCM-SHA384'
                        - 'TLS-DHE-DSS-WITH-AES-128-CBC-SHA'
                        - 'TLS-DHE-DSS-WITH-AES-256-CBC-SHA'
                        - 'TLS-DHE-DSS-WITH-AES-128-CBC-SHA256'
                        - 'TLS-DHE-DSS-WITH-AES-128-GCM-SHA256'
                        - 'TLS-DHE-DSS-WITH-AES-256-CBC-SHA256'
                        - 'TLS-DHE-DSS-WITH-AES-256-GCM-SHA384'
                        - 'TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256'
                        - 'TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256'
                        - 'TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384'
                        - 'TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384'
                        - 'TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA'
                        - 'TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256'
                        - 'TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256'
                        - 'TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384'
                        - 'TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384'
                        - 'TLS-RSA-WITH-AES-128-GCM-SHA256'
                        - 'TLS-RSA-WITH-AES-256-GCM-SHA384'
                        - 'TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA'
                        - 'TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA'
                        - 'TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256'
                        - 'TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256'
                        - 'TLS-DHE-DSS-WITH-SEED-CBC-SHA'
                        - 'TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256'
                        - 'TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384'
                        - 'TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256'
                        - 'TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384'
                        - 'TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256'
                        - 'TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384'
                        - 'TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA'
                        - 'TLS-DHE-DSS-WITH-DES-CBC-SHA'
                priority:
                    type: int
                    description: 'SSL/TLS cipher suites priority.'
                versions:
                    -
                        type: str
                        choices:
                            - 'ssl-3.0'
                            - 'tls-1.0'
                            - 'tls-1.1'
                            - 'tls-1.2'
    schema_object1:
        methods: [delete]
        description: 'SSL/TLS cipher suites acceptable from a client, ordered by priority.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'SSL/TLS cipher suites acceptable from a client, ordered by priority.'
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
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/VIP6/{VIP6}/SSL-CIPHER-SUITES/{SSL-CIPHER-SUITES}
      fmgr_firewall_vip6_sslciphersuites_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vip6: <value of string>
            ssl-cipher-suites: <value of string>
         params:
            -
               data:
                  cipher: <value in [TLS-RSA-WITH-RC4-128-MD5, TLS-RSA-WITH-RC4-128-SHA, TLS-RSA-WITH-DES-CBC-SHA, ...]>
                  priority: <value of integer>
                  versions:
                    - <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/VIP6/{VIP6}/SSL-CIPHER-SUITES/{SSL-CIPHER-SUITES}
      fmgr_firewall_vip6_sslciphersuites_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vip6: <value of string>
            ssl-cipher-suites: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[clone, set, update]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            priority:
               type: int
               description: 'SSL/TLS cipher suites priority.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/firewall/vip6/{vip6}/ssl-cipher-suites/{ssl-ciphe...'
return_of_api_category_0:
   description: items returned for method:[delete]
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
            example: '/pm/config/adom/{adom}/obj/firewall/vip6/{vip6}/ssl-cipher-suites/{ssl-ciphe...'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            cipher:
               type: str
               description: 'Cipher suite name.'
            priority:
               type: int
               description: 'SSL/TLS cipher suites priority.'
            versions:
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
            example: '/pm/config/adom/{adom}/obj/firewall/vip6/{vip6}/ssl-cipher-suites/{ssl-ciphe...'

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
        '/pm/config/adom/{adom}/obj/firewall/vip6/{vip6}/ssl-cipher-suites/{ssl-cipher-suites}',
        '/pm/config/global/obj/firewall/vip6/{vip6}/ssl-cipher-suites/{ssl-cipher-suites}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'vip6',
            'type': 'string'
        },
        {
            'name': 'ssl-cipher-suites',
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
                        'cipher': {
                            'type': 'string',
                            'enum': [
                                'TLS-RSA-WITH-RC4-128-MD5',
                                'TLS-RSA-WITH-RC4-128-SHA',
                                'TLS-RSA-WITH-DES-CBC-SHA',
                                'TLS-RSA-WITH-3DES-EDE-CBC-SHA',
                                'TLS-RSA-WITH-AES-128-CBC-SHA',
                                'TLS-RSA-WITH-AES-256-CBC-SHA',
                                'TLS-RSA-WITH-AES-128-CBC-SHA256',
                                'TLS-RSA-WITH-AES-256-CBC-SHA256',
                                'TLS-RSA-WITH-CAMELLIA-128-CBC-SHA',
                                'TLS-RSA-WITH-CAMELLIA-256-CBC-SHA',
                                'TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256',
                                'TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256',
                                'TLS-RSA-WITH-SEED-CBC-SHA',
                                'TLS-RSA-WITH-ARIA-128-CBC-SHA256',
                                'TLS-RSA-WITH-ARIA-256-CBC-SHA384',
                                'TLS-DHE-RSA-WITH-DES-CBC-SHA',
                                'TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA',
                                'TLS-DHE-RSA-WITH-AES-128-CBC-SHA',
                                'TLS-DHE-RSA-WITH-AES-256-CBC-SHA',
                                'TLS-DHE-RSA-WITH-AES-128-CBC-SHA256',
                                'TLS-DHE-RSA-WITH-AES-256-CBC-SHA256',
                                'TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA',
                                'TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA',
                                'TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256',
                                'TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256',
                                'TLS-DHE-RSA-WITH-SEED-CBC-SHA',
                                'TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256',
                                'TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384',
                                'TLS-ECDHE-RSA-WITH-RC4-128-SHA',
                                'TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA',
                                'TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA',
                                'TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA',
                                'TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256',
                                'TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256',
                                'TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256',
                                'TLS-DHE-RSA-WITH-AES-128-GCM-SHA256',
                                'TLS-DHE-RSA-WITH-AES-256-GCM-SHA384',
                                'TLS-DHE-DSS-WITH-AES-128-CBC-SHA',
                                'TLS-DHE-DSS-WITH-AES-256-CBC-SHA',
                                'TLS-DHE-DSS-WITH-AES-128-CBC-SHA256',
                                'TLS-DHE-DSS-WITH-AES-128-GCM-SHA256',
                                'TLS-DHE-DSS-WITH-AES-256-CBC-SHA256',
                                'TLS-DHE-DSS-WITH-AES-256-GCM-SHA384',
                                'TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256',
                                'TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256',
                                'TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384',
                                'TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384',
                                'TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA',
                                'TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256',
                                'TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256',
                                'TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384',
                                'TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384',
                                'TLS-RSA-WITH-AES-128-GCM-SHA256',
                                'TLS-RSA-WITH-AES-256-GCM-SHA384',
                                'TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA',
                                'TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA',
                                'TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256',
                                'TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256',
                                'TLS-DHE-DSS-WITH-SEED-CBC-SHA',
                                'TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256',
                                'TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384',
                                'TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256',
                                'TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384',
                                'TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256',
                                'TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384',
                                'TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA',
                                'TLS-DHE-DSS-WITH-DES-CBC-SHA'
                            ]
                        },
                        'priority': {
                            'type': 'integer'
                        },
                        'versions': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'ssl-3.0',
                                    'tls-1.0',
                                    'tls-1.1',
                                    'tls-1.2'
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

    module.exit_json(**response[1])


if __name__ == '__main__':
    main()
