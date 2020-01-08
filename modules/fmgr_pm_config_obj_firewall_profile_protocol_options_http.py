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
module: fmgr_pm_config_obj_firewall_profile_protocol_options_http
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/firewall/profile-protocol-options/{profile-protocol-options}/http
    - /pm/config/global/obj/firewall/profile-protocol-options/{profile-protocol-options}/http
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
            profile-protocol-options:
                type: str
    schema_object0:
        methods: [get]
        description: 'Configure HTTP protocol options.'
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
        description: 'Configure HTTP protocol options.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                block-page-status-code:
                    type: int
                    description: 'Code number returned for blocked HTTP pages (non-FortiGuard only) (100 - 599, default = 403).'
                comfort-amount:
                    type: int
                    description: 'Amount of data to send in a transmission for client comforting (1 - 10240 bytes, default = 1).'
                comfort-interval:
                    type: int
                    description: 'Period of time between start, or last transmission, and the next client comfort transmission of data (1 - 900 sec, default...'
                fortinet-bar:
                    type: str
                    description: 'Enable/disable Fortinet bar on HTML content.'
                    choices:
                        - 'disable'
                        - 'enable'
                fortinet-bar-port:
                    type: int
                    description: 'Port for use by Fortinet Bar (1 - 65535, default = 8011).'
                http-policy:
                    type: str
                    description: 'Enable/disable HTTP policy check.'
                    choices:
                        - 'disable'
                        - 'enable'
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
                            - 'chunkedbypass'
                            - 'clientcomfort'
                            - 'no-content-summary'
                            - 'servercomfort'
                oversize-limit:
                    type: int
                    description: 'Maximum in-memory file size that can be scanned (1 - 383 MB, default = 10).'
                ports:
                    -
                        type: int
                post-lang:
                    -
                        type: str
                        choices:
                            - 'jisx0201'
                            - 'jisx0208'
                            - 'jisx0212'
                            - 'gb2312'
                            - 'ksc5601-ex'
                            - 'euc-jp'
                            - 'sjis'
                            - 'iso2022-jp'
                            - 'iso2022-jp-1'
                            - 'iso2022-jp-2'
                            - 'euc-cn'
                            - 'ces-gbk'
                            - 'hz'
                            - 'ces-big5'
                            - 'euc-kr'
                            - 'iso2022-jp-3'
                            - 'iso8859-1'
                            - 'tis620'
                            - 'cp874'
                            - 'cp1252'
                            - 'cp1251'
                range-block:
                    type: str
                    description: 'Enable/disable blocking of partial downloads.'
                    choices:
                        - 'disable'
                        - 'enable'
                retry-count:
                    type: int
                    description: 'Number of attempts to retry HTTP connection (0 - 100, default = 0).'
                scan-bzip2:
                    type: str
                    description: 'Enable/disable scanning of BZip2 compressed files.'
                    choices:
                        - 'disable'
                        - 'enable'
                status:
                    type: str
                    description: 'Enable/disable the active status of scanning for this protocol.'
                    choices:
                        - 'disable'
                        - 'enable'
                streaming-content-bypass:
                    type: str
                    description: 'Enable/disable bypassing of streaming content from buffering.'
                    choices:
                        - 'disable'
                        - 'enable'
                strip-x-forwarded-for:
                    type: str
                    description: 'Enable/disable stripping of HTTP X-Forwarded-For header.'
                    choices:
                        - 'disable'
                        - 'enable'
                switching-protocols:
                    type: str
                    description: 'Bypass from scanning, or block a connection that attempts to switch protocol.'
                    choices:
                        - 'bypass'
                        - 'block'
                uncompressed-nest-limit:
                    type: int
                    description: 'Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).'
                uncompressed-oversize-limit:
                    type: int
                    description: 'Maximum in-memory uncompressed file size that can be scanned (0 - 383 MB, 0 = unlimited, default = 10).'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/PROFILE-PROTOCOL-OPTIONS/{PROFILE-PROTOCOL-OPTIONS}/HTTP
      fmgr_pm_config_obj_firewall_profile_protocol_options_http:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile-protocol-options: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/PROFILE-PROTOCOL-OPTIONS/{PROFILE-PROTOCOL-OPTIONS}/HTTP
      fmgr_pm_config_obj_firewall_profile_protocol_options_http:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile-protocol-options: <value of string>
         params:
            -
               data:
                  block-page-status-code: <value of integer>
                  comfort-amount: <value of integer>
                  comfort-interval: <value of integer>
                  fortinet-bar: <value in [disable, enable]>
                  fortinet-bar-port: <value of integer>
                  http-policy: <value in [disable, enable]>
                  inspect-all: <value in [disable, enable]>
                  options:
                    - <value in [oversize, chunkedbypass, clientcomfort, ...]>
                  oversize-limit: <value of integer>
                  ports:
                    - <value of integer>
                  post-lang:
                    - <value in [jisx0201, jisx0208, jisx0212, ...]>
                  range-block: <value in [disable, enable]>
                  retry-count: <value of integer>
                  scan-bzip2: <value in [disable, enable]>
                  status: <value in [disable, enable]>
                  streaming-content-bypass: <value in [disable, enable]>
                  strip-x-forwarded-for: <value in [disable, enable]>
                  switching-protocols: <value in [bypass, block]>
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
            block-page-status-code:
               type: int
               description: 'Code number returned for blocked HTTP pages (non-FortiGuard only) (100 - 599, default = 403).'
            comfort-amount:
               type: int
               description: 'Amount of data to send in a transmission for client comforting (1 - 10240 bytes, default = 1).'
            comfort-interval:
               type: int
               description: 'Period of time between start, or last transmission, and the next client comfort transmission of data (1 - 900 sec, default = 10).'
            fortinet-bar:
               type: str
               description: 'Enable/disable Fortinet bar on HTML content.'
            fortinet-bar-port:
               type: int
               description: 'Port for use by Fortinet Bar (1 - 65535, default = 8011).'
            http-policy:
               type: str
               description: 'Enable/disable HTTP policy check.'
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
            post-lang:
               type: array
               suboptions:
                  type: str
            range-block:
               type: str
               description: 'Enable/disable blocking of partial downloads.'
            retry-count:
               type: int
               description: 'Number of attempts to retry HTTP connection (0 - 100, default = 0).'
            scan-bzip2:
               type: str
               description: 'Enable/disable scanning of BZip2 compressed files.'
            status:
               type: str
               description: 'Enable/disable the active status of scanning for this protocol.'
            streaming-content-bypass:
               type: str
               description: 'Enable/disable bypassing of streaming content from buffering.'
            strip-x-forwarded-for:
               type: str
               description: 'Enable/disable stripping of HTTP X-Forwarded-For header.'
            switching-protocols:
               type: str
               description: 'Bypass from scanning, or block a connection that attempts to switch protocol.'
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
from ansible.module_utils.network.fortimanager.common import FAIL_SOCKET_MSG
from ansible.module_utils.network.fortimanager.common import DEFAULT_RESULT_OBJ
from ansible.module_utils.network.fortimanager.common import FMGRCommon
from ansible.module_utils.network.fortimanager.common import FMGBaseException
from ansible.module_utils.network.fortimanager.fortimanager import FortiManagerHandler


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/firewall/profile-protocol-options/{profile-protocol-options}/http',
        '/pm/config/global/obj/firewall/profile-protocol-options/{profile-protocol-options}/http'
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
                        'block-page-status-code': {
                            'type': 'integer'
                        },
                        'comfort-amount': {
                            'type': 'integer'
                        },
                        'comfort-interval': {
                            'type': 'integer'
                        },
                        'fortinet-bar': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fortinet-bar-port': {
                            'type': 'integer'
                        },
                        'http-policy': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
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
                                    'chunkedbypass',
                                    'clientcomfort',
                                    'no-content-summary',
                                    'servercomfort'
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
                        'post-lang': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'jisx0201',
                                    'jisx0208',
                                    'jisx0212',
                                    'gb2312',
                                    'ksc5601-ex',
                                    'euc-jp',
                                    'sjis',
                                    'iso2022-jp',
                                    'iso2022-jp-1',
                                    'iso2022-jp-2',
                                    'euc-cn',
                                    'ces-gbk',
                                    'hz',
                                    'ces-big5',
                                    'euc-kr',
                                    'iso2022-jp-3',
                                    'iso8859-1',
                                    'tis620',
                                    'cp874',
                                    'cp1252',
                                    'cp1251'
                                ]
                            }
                        },
                        'range-block': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'retry-count': {
                            'type': 'integer'
                        },
                        'scan-bzip2': {
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
                        'streaming-content-bypass': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'strip-x-forwarded-for': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'switching-protocols': {
                            'type': 'string',
                            'enum': [
                                'bypass',
                                'block'
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
