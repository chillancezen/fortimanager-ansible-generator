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
module: fmgr_system_alertevent
short_description: Alert events.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /cli/global/system/alert-event
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
        description: 'Alert events.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    alert-destination:
                        -
                            from:
                                type: str
                                description: 'Sender email address to use in alert emails.'
                            smtp-name:
                                type: str
                                description: 'SMTP server name.'
                            snmp-name:
                                type: str
                                description: 'SNMP trap name.'
                            syslog-name:
                                type: str
                                description: 'Syslog server name.'
                            to:
                                type: str
                                description: 'Recipient email address to use in alert emails.'
                            type:
                                type: str
                                default: 'mail'
                                description:
                                 - 'Destination type.'
                                 - 'mail - Send email alert.'
                                 - 'snmp - Send SNMP trap.'
                                 - 'syslog - Send syslog message.'
                                choices:
                                    - 'mail'
                                    - 'snmp'
                                    - 'syslog'
                    enable-generic-text:
                        -
                            type: str
                            choices:
                                - 'enable'
                                - 'disable'
                    enable-severity-filter:
                        -
                            type: str
                            choices:
                                - 'enable'
                                - 'disable'
                    event-time-period:
                        type: str
                        default: '0.5'
                        description:
                         - 'Time period (hours).'
                         - '0.5 - 30 minutes.'
                         - '1 - 1 hour.'
                         - '3 - 3 hours.'
                         - '6 - 6 hours.'
                         - '12 - 12 hours.'
                         - '24 - 1 day.'
                         - '72 - 3 days.'
                         - '168 - 1 week.'
                        choices:
                            - '0.5'
                            - '1'
                            - '3'
                            - '6'
                            - '12'
                            - '24'
                            - '72'
                            - '168'
                    generic-text:
                        type: str
                        description: 'Text that must be contained in a log to trigger alert.'
                    name:
                        type: str
                        description: 'Alert name.'
                    num-events:
                        type: str
                        default: '1'
                        description:
                         - 'Minimum number of events required within time period.'
                         - '1 - 1 event.'
                         - '5 - 5 events.'
                         - '10 - 10 events.'
                         - '50 - 50 events.'
                         - '100 - 100 events.'
                        choices:
                            - '1'
                            - '5'
                            - '10'
                            - '50'
                            - '100'
                    severity-filter:
                        type: str
                        default: 'high'
                        description:
                         - 'Required log severity to trigger alert.'
                         - 'high - High level alert.'
                         - 'medium-high - Medium-high level alert.'
                         - 'medium - Medium level alert.'
                         - 'medium-low - Medium-low level alert.'
                         - 'low - Low level alert.'
                        choices:
                            - 'high'
                            - 'medium-high'
                            - 'medium'
                            - 'medium-low'
                            - 'low'
                    severity-level-comp:
                        -
                            type: str
                            choices:
                                - '>='
                                - '='
                                - '<='
                    severity-level-logs:
                        -
                            type: str
                            choices:
                                - 'no-check'
                                - 'information'
                                - 'notify'
                                - 'warning'
                                - 'error'
                                - 'critical'
                                - 'alert'
                                - 'emergency'
    schema_object1:
        methods: [get]
        description: 'Alert events.'
        api_categories: [api_tag0]
        api_tag0:
            fields:
                -
                    -
                        type: str
                        choices:
                            - 'enable-generic-text'
                            - 'enable-severity-filter'
                            - 'event-time-period'
                            - 'generic-text'
                            - 'name'
                            - 'num-events'
                            - 'severity-filter'
                            - 'severity-level-comp'
                            - 'severity-level-logs'
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
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /CLI/SYSTEM/ALERT-EVENT
      fmgr_system_alertevent:
         method: <value in [add, set, update]>
         params:
            -
               data:
                 -
                     alert-destination:
                       -
                           from: <value of string>
                           smtp-name: <value of string>
                           snmp-name: <value of string>
                           syslog-name: <value of string>
                           to: <value of string>
                           type: <value in [mail, snmp, syslog] default: 'mail'>
                     enable-generic-text:
                       - <value in [enable, disable]>
                     enable-severity-filter:
                       - <value in [enable, disable]>
                     event-time-period: <value in [0.5, 1, 3, ...] default: '0.5'>
                     generic-text: <value of string>
                     name: <value of string>
                     num-events: <value in [1, 5, 10, ...] default: '1'>
                     severity-filter: <value in [high, medium-high, medium, ...] default: 'high'>
                     severity-level-comp:
                       - <value in [>=, =, <=]>
                     severity-level-logs:
                       - <value in [no-check, information, notify, ...]>

    - name: REQUESTING /CLI/SYSTEM/ALERT-EVENT
      fmgr_system_alertevent:
         method: <value in [get]>
         params:
            -
               fields:
                 -
                    - <value in [enable-generic-text, enable-severity-filter, event-time-period, ...]>
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
            example: '/cli/global/system/alert-event'
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
               alert-destination:
                  type: array
                  suboptions:
                     from:
                        type: str
                        description: 'Sender email address to use in alert emails.'
                     smtp-name:
                        type: str
                        description: 'SMTP server name.'
                     snmp-name:
                        type: str
                        description: 'SNMP trap name.'
                     syslog-name:
                        type: str
                        description: 'Syslog server name.'
                     to:
                        type: str
                        description: 'Recipient email address to use in alert emails.'
                     type:
                        type: str
                        description: |
                           'Destination type.'
                           'mail - Send email alert.'
                           'snmp - Send SNMP trap.'
                           'syslog - Send syslog message.'
                        example: 'mail'
               enable-generic-text:
                  type: array
                  suboptions:
                     type: str
               enable-severity-filter:
                  type: array
                  suboptions:
                     type: str
               event-time-period:
                  type: str
                  description: |
                     'Time period (hours).'
                     '0.5 - 30 minutes.'
                     '1 - 1 hour.'
                     '3 - 3 hours.'
                     '6 - 6 hours.'
                     '12 - 12 hours.'
                     '24 - 1 day.'
                     '72 - 3 days.'
                     '168 - 1 week.'
                  example: '0.5'
               generic-text:
                  type: str
                  description: 'Text that must be contained in a log to trigger alert.'
               name:
                  type: str
                  description: 'Alert name.'
               num-events:
                  type: str
                  description: |
                     'Minimum number of events required within time period.'
                     '1 - 1 event.'
                     '5 - 5 events.'
                     '10 - 10 events.'
                     '50 - 50 events.'
                     '100 - 100 events.'
                  example: '1'
               severity-filter:
                  type: str
                  description: |
                     'Required log severity to trigger alert.'
                     'high - High level alert.'
                     'medium-high - Medium-high level alert.'
                     'medium - Medium level alert.'
                     'medium-low - Medium-low level alert.'
                     'low - Low level alert.'
                  example: 'high'
               severity-level-comp:
                  type: array
                  suboptions:
                     type: str
               severity-level-logs:
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
            example: '/cli/global/system/alert-event'

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
        '/cli/global/system/alert-event'
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
                        'alert-destination': {
                            'type': 'array',
                            'items': {
                                'from': {
                                    'type': 'string'
                                },
                                'smtp-name': {
                                    'type': 'string'
                                },
                                'snmp-name': {
                                    'type': 'string'
                                },
                                'syslog-name': {
                                    'type': 'string'
                                },
                                'to': {
                                    'type': 'string'
                                },
                                'type': {
                                    'type': 'string',
                                    'enum': [
                                        'mail',
                                        'snmp',
                                        'syslog'
                                    ]
                                }
                            }
                        },
                        'enable-generic-text': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'enable',
                                    'disable'
                                ]
                            }
                        },
                        'enable-severity-filter': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'enable',
                                    'disable'
                                ]
                            }
                        },
                        'event-time-period': {
                            'type': 'string',
                            'enum': [
                                '0.5',
                                '1',
                                '3',
                                '6',
                                '12',
                                '24',
                                '72',
                                '168'
                            ]
                        },
                        'generic-text': {
                            'type': 'string'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'num-events': {
                            'type': 'string',
                            'enum': [
                                '1',
                                '5',
                                '10',
                                '50',
                                '100'
                            ]
                        },
                        'severity-filter': {
                            'type': 'string',
                            'enum': [
                                'high',
                                'medium-high',
                                'medium',
                                'medium-low',
                                'low'
                            ]
                        },
                        'severity-level-comp': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    '>=',
                                    '=',
                                    '<='
                                ]
                            }
                        },
                        'severity-level-logs': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'no-check',
                                    'information',
                                    'notify',
                                    'warning',
                                    'error',
                                    'critical',
                                    'alert',
                                    'emergency'
                                ]
                            }
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
                                'enable-generic-text',
                                'enable-severity-filter',
                                'event-time-period',
                                'generic-text',
                                'name',
                                'num-events',
                                'severity-filter',
                                'severity-level-comp',
                                'severity-level-logs'
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
