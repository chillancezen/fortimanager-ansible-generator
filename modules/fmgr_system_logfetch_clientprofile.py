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
module: fmgr_system_logfetch_clientprofile
short_description: Log-fetch client profile settings.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /cli/global/system/log-fetch/client-profile
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
        methods: [add, set, update]
        description: 'Log-fetch client profile settings.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    client-adom:
                        type: str
                        description: 'Log-fetch client sides adom name.'
                    data-range:
                        type: str
                        default: 'custom'
                        description:
                         - 'Data-range for fetched logs.'
                         - 'custom - Specify some other date and time range.'
                        choices:
                            - 'custom'
                    data-range-value:
                        type: int
                        default: 10
                        description: 'Last n days or hours.'
                    device-filter:
                        -
                            adom:
                                type: str
                                default: '*'
                                description: 'Adom name.'
                            device:
                                type: str
                                default: '*'
                                description: 'Device name or Serial number.'
                            id:
                                type: int
                                default: 0
                                description: 'Add or edit a device filter.'
                            vdom:
                                type: str
                                default: '*'
                                description: 'Vdom filters.'
                    end-time:
                        -
                            type: str
                    id:
                        type: int
                        default: 0
                        description: 'Log-fetch client profile ID.'
                    index-fetch-logs:
                        type: str
                        default: 'enable'
                        description:
                         - 'Enable/Disable indexing logs automatically after fetching logs.'
                         - 'disable - Disable attribute function.'
                         - 'enable - Enable attribute function.'
                        choices:
                            - 'disable'
                            - 'enable'
                    log-filter:
                        -
                            field:
                                type: str
                                description: 'Field name.'
                            id:
                                type: int
                                default: 0
                                description: 'Log filter ID.'
                            oper:
                                type: str
                                default: '='
                                description:
                                 - 'Field filter operator.'
                                 - '&lt; - =Less than or equal to'
                                 - '&gt; - =Greater than or equal to'
                                 - 'contain - Contain'
                                 - 'not-contain - Not contain'
                                 - 'match - Match (expression)'
                                choices:
                                    - '='
                                    - '!='
                                    - '<'
                                    - '>'
                                    - '<='
                                    - '>='
                                    - 'contain'
                                    - 'not-contain'
                                    - 'match'
                            value:
                                type: str
                                description: 'Field filter operand or free-text matching expression.'
                    log-filter-logic:
                        type: str
                        default: 'or'
                        description:
                         - 'And/Or logic for log-filters.'
                         - 'and - Logic And.'
                         - 'or - Logic Or.'
                        choices:
                            - 'and'
                            - 'or'
                    log-filter-status:
                        type: str
                        default: 'disable'
                        description:
                         - 'Enable/Disable log-filter.'
                         - 'disable - Disable attribute function.'
                         - 'enable - Enable attribute function.'
                        choices:
                            - 'disable'
                            - 'enable'
                    name:
                        type: str
                        description: 'Name of log-fetch client profile.'
                    password:
                        -
                            type: str
                            default: 'ENC NzkzMDg4MDc2MTgwNjUzNhwvJBDjPF8MRvYpIukmL7G++XrKmHYTQF5zcGV+Ss3GXWsKe9F9Ie2B55rWFdty9EbQ6aAhGObDlAP7FQ7Otz0SNL49B...'
                    secure-connection:
                        type: str
                        default: 'enable'
                        description:
                         - 'Enable/Disable protecting log-fetch connection with TLS/SSL.'
                         - 'disable - Disable attribute function.'
                         - 'enable - Enable attribute function.'
                        choices:
                            - 'disable'
                            - 'enable'
                    server-adom:
                        type: str
                        description: 'Log-fetch server sides adom name.'
                    server-ip:
                        type: str
                        default: '0.0.0.0'
                        description: 'Log-fetch server IP address.'
                    start-time:
                        -
                            type: str
                    sync-adom-config:
                        type: str
                        default: 'disable'
                        description:
                         - 'Enable/Disable sync adom related config.'
                         - 'disable - Disable attribute function.'
                         - 'enable - Enable attribute function.'
                        choices:
                            - 'disable'
                            - 'enable'
                    user:
                        type: str
                        description: 'Log-fetch server login username.'
    schema_object1:
        methods: [get]
        description: 'Log-fetch client profile settings.'
        api_categories: [api_tag0]
        api_tag0:
            fields:
                -
                    -
                        type: str
                        choices:
                            - 'client-adom'
                            - 'data-range'
                            - 'data-range-value'
                            - 'end-time'
                            - 'id'
                            - 'index-fetch-logs'
                            - 'log-filter-logic'
                            - 'log-filter-status'
                            - 'name'
                            - 'password'
                            - 'secure-connection'
                            - 'server-adom'
                            - 'server-ip'
                            - 'start-time'
                            - 'sync-adom-config'
                            - 'user'
            filter:
                -
                    type: str
            loadsub:
                type: int
                description: 'Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.'
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.'
                 - 'count - Return the number of matching entries instead of the actual entry data.'
                 - 'syntax - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.'
                choices:
                    - 'count'
                    - 'syntax'

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

    - name: REQUESTING /CLI/SYSTEM/LOG-FETCH/CLIENT-PROFILE
      fmgr_system_logfetch_clientprofile:
         method: <value in [add, set, update]>
         params:
            -
               data:
                 -
                     client-adom: <value of string>
                     data-range: <value in [custom] default: 'custom'>
                     data-range-value: <value of integer default: 10>
                     device-filter:
                       -
                           adom: <value of string default: '*'>
                           device: <value of string default: '*'>
                           id: <value of integer default: 0>
                           vdom: <value of string default: '*'>
                     end-time:
                       - <value of string>
                     id: <value of integer default: 0>
                     index-fetch-logs: <value in [disable, enable] default: 'enable'>
                     log-filter:
                       -
                           field: <value of string>
                           id: <value of integer default: 0>
                           oper: <value in [=, !=, <, ...] default: '='>
                           value: <value of string>
                     log-filter-logic: <value in [and, or] default: 'or'>
                     log-filter-status: <value in [disable, enable] default: 'disable'>
                     name: <value of string>
                     password:
                       - <value of string default: 'ENC NzkzMDg4MDc2MTgwNjUzNhwvJBDjPF8MRvYpIukmL7G++XrKmHYTQF5zcGV+Ss3GXWsKe9F9...'>
                     secure-connection: <value in [disable, enable] default: 'enable'>
                     server-adom: <value of string>
                     server-ip: <value of string default: '0.0.0.0'>
                     start-time:
                       - <value of string>
                     sync-adom-config: <value in [disable, enable] default: 'disable'>
                     user: <value of string>

    - name: REQUESTING /CLI/SYSTEM/LOG-FETCH/CLIENT-PROFILE
      fmgr_system_logfetch_clientprofile:
         method: <value in [get]>
         params:
            -
               fields:
                 -
                    - <value in [client-adom, data-range, data-range-value, ...]>
               filter:
                 - <value of string>
               loadsub: <value of integer>
               option: <value in [count, syntax]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[add, set, update]
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
            example: '/cli/global/system/log-fetch/client-profile'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            type: array
            suboptions:
               client-adom:
                  type: str
                  description: 'Log-fetch client sides adom name.'
               data-range:
                  type: str
                  description: |
                     'Data-range for fetched logs.'
                     'custom - Specify some other date and time range.'
                  example: 'custom'
               data-range-value:
                  type: int
                  description: 'Last n days or hours.'
                  example: 10
               device-filter:
                  type: array
                  suboptions:
                     adom:
                        type: str
                        description: 'Adom name.'
                        example: '*'
                     device:
                        type: str
                        description: 'Device name or Serial number.'
                        example: '*'
                     id:
                        type: int
                        description: 'Add or edit a device filter.'
                        example: 0
                     vdom:
                        type: str
                        description: 'Vdom filters.'
                        example: '*'
               end-time:
                  type: array
                  suboptions:
                     type: str
               id:
                  type: int
                  description: 'Log-fetch client profile ID.'
                  example: 0
               index-fetch-logs:
                  type: str
                  description: |
                     'Enable/Disable indexing logs automatically after fetching logs.'
                     'disable - Disable attribute function.'
                     'enable - Enable attribute function.'
                  example: 'enable'
               log-filter:
                  type: array
                  suboptions:
                     field:
                        type: str
                        description: 'Field name.'
                     id:
                        type: int
                        description: 'Log filter ID.'
                        example: 0
                     oper:
                        type: str
                        description: |
                           'Field filter operator.'
                           '&lt; - =Less than or equal to'
                           '&gt; - =Greater than or equal to'
                           'contain - Contain'
                           'not-contain - Not contain'
                           'match - Match (expression)'
                        example: '='
                     value:
                        type: str
                        description: 'Field filter operand or free-text matching expression.'
               log-filter-logic:
                  type: str
                  description: |
                     'And/Or logic for log-filters.'
                     'and - Logic And.'
                     'or - Logic Or.'
                  example: 'or'
               log-filter-status:
                  type: str
                  description: |
                     'Enable/Disable log-filter.'
                     'disable - Disable attribute function.'
                     'enable - Enable attribute function.'
                  example: 'disable'
               name:
                  type: str
                  description: 'Name of log-fetch client profile.'
               password:
                  type: array
                  suboptions:
                     type: str
                     example: 'ENC NzkzMDg4MDc2MTgwNjUzNhwvJBDjPF8MRvYpIukmL7G++XrKmHYTQF5zcGV+Ss3GXWsKe9F9...'
               secure-connection:
                  type: str
                  description: |
                     'Enable/Disable protecting log-fetch connection with TLS/SSL.'
                     'disable - Disable attribute function.'
                     'enable - Enable attribute function.'
                  example: 'enable'
               server-adom:
                  type: str
                  description: 'Log-fetch server sides adom name.'
               server-ip:
                  type: str
                  description: 'Log-fetch server IP address.'
                  example: '0.0.0.0'
               start-time:
                  type: array
                  suboptions:
                     type: str
               sync-adom-config:
                  type: str
                  description: |
                     'Enable/Disable sync adom related config.'
                     'disable - Disable attribute function.'
                     'enable - Enable attribute function.'
                  example: 'disable'
               user:
                  type: str
                  description: 'Log-fetch server login username.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/cli/global/system/log-fetch/client-profile'

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
        '/cli/global/system/log-fetch/client-profile'
    ]

    url_schema = [
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'client-adom': {
                            'type': 'string'
                        },
                        'data-range': {
                            'type': 'string',
                            'enum': [
                                'custom'
                            ]
                        },
                        'data-range-value': {
                            'type': 'integer',
                            'default': 10,
                            'example': 10
                        },
                        'device-filter': {
                            'type': 'array',
                            'items': {
                                'adom': {
                                    'type': 'string'
                                },
                                'device': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer',
                                    'default': 0,
                                    'example': 0
                                },
                                'vdom': {
                                    'type': 'string'
                                }
                            }
                        },
                        'end-time': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'id': {
                            'type': 'integer',
                            'default': 0,
                            'example': 0
                        },
                        'index-fetch-logs': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'log-filter': {
                            'type': 'array',
                            'items': {
                                'field': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer',
                                    'default': 0,
                                    'example': 0
                                },
                                'oper': {
                                    'type': 'string',
                                    'enum': [
                                        '=',
                                        '!=',
                                        '<',
                                        '>',
                                        '<=',
                                        '>=',
                                        'contain',
                                        'not-contain',
                                        'match'
                                    ]
                                },
                                'value': {
                                    'type': 'string'
                                }
                            }
                        },
                        'log-filter-logic': {
                            'type': 'string',
                            'enum': [
                                'and',
                                'or'
                            ]
                        },
                        'log-filter-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'name': {
                            'type': 'string'
                        },
                        'password': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'secure-connection': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'server-adom': {
                            'type': 'string'
                        },
                        'server-ip': {
                            'type': 'string'
                        },
                        'start-time': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'sync-adom-config': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'user': {
                            'type': 'string'
                        }
                    }
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object1': [
                {
                    'name': 'fields',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'enum': [
                                'client-adom',
                                'data-range',
                                'data-range-value',
                                'end-time',
                                'id',
                                'index-fetch-logs',
                                'log-filter-logic',
                                'log-filter-status',
                                'name',
                                'password',
                                'secure-connection',
                                'server-adom',
                                'server-ip',
                                'start-time',
                                'sync-adom-config',
                                'user'
                            ]
                        }
                    }
                },
                {
                    'name': 'filter',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'example': [
                                '<attr>',
                                '==',
                                'test'
                            ]
                        }
                    },
                    'api_tag': 0
                },
                {
                    'type': 'integer',
                    'name': 'loadsub',
                    'api_tag': 0
                },
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'count',
                            'syntax'
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
            'add': 'object0',
            'get': 'object1',
            'set': 'object0',
            'update': 'object0'
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
                'add',
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
