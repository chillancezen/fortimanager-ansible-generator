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
module: fmgr_cli_system_admin_user_dashboard
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /cli/global/system/admin/user/{user}/dashboard
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
            user:
                type: str
    schema_object0:
        methods: [add, set, update]
        description: 'Custom dashboard widgets.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    column:
                        type: int
                        default: 0
                        description: 'Widgets column ID.'
                    diskio-content-type:
                        type: str
                        default: 'util'
                        description:
                         - 'Disk I/O Monitor widgets chart type.'
                         - 'util - bandwidth utilization.'
                         - 'iops - the number of I/O requests.'
                         - 'blks - the amount of data of I/O requests.'
                        choices:
                            - 'util'
                            - 'iops'
                            - 'blks'
                    diskio-period:
                        type: str
                        default: '1hour'
                        description:
                         - 'Disk I/O Monitor widgets data period.'
                         - '1hour - 1 hour.'
                         - '8hour - 8 hour.'
                         - '24hour - 24 hour.'
                        choices:
                            - '1hour'
                            - '8hour'
                            - '24hour'
                    log-rate-period:
                        type: str
                        description:
                         - 'Log receive monitor widgets data period.'
                         - '2min  - 2 minutes.'
                         - '1hour - 1 hour.'
                         - '6hours - 6 hours.'
                        choices:
                            - '2min '
                            - '1hour'
                            - '6hours'
                    log-rate-topn:
                        type: str
                        default: '5'
                        description:
                         - 'Log receive monitor widgets number of top items to display.'
                         - '1 - Top 1.'
                         - '2 - Top 2.'
                         - '3 - Top 3.'
                         - '4 - Top 4.'
                         - '5 - Top 5.'
                        choices:
                            - '1'
                            - '2'
                            - '3'
                            - '4'
                            - '5'
                    log-rate-type:
                        type: str
                        default: 'device'
                        description:
                         - 'Log receive monitor widgets statistics breakdown options.'
                         - 'log - Show log rates for each log type.'
                         - 'device - Show log rates for each device.'
                        choices:
                            - 'log'
                            - 'device'
                    moduleid:
                        type: int
                        default: 0
                        description: 'Widget ID.'
                    name:
                        type: str
                        description: 'Widget name.'
                    num-entries:
                        type: int
                        default: 10
                        description: 'Number of entries.'
                    refresh-interval:
                        type: int
                        default: 300
                        description: 'Widgets refresh interval.'
                    res-cpu-display:
                        type: str
                        default: 'average '
                        description:
                         - 'Widgets CPU display type.'
                         - 'average  - Average usage of CPU.'
                         - 'each - Each usage of CPU.'
                        choices:
                            - 'average '
                            - 'each'
                    res-period:
                        type: str
                        default: '10min '
                        description:
                         - 'Widgets data period.'
                         - '10min  - Last 10 minutes.'
                         - 'hour - Last hour.'
                         - 'day - Last day.'
                        choices:
                            - '10min '
                            - 'hour'
                            - 'day'
                    res-view-type:
                        type: str
                        default: 'history'
                        description:
                         - 'Widgets data view type.'
                         - 'real-time  - Real-time view.'
                         - 'history - History view.'
                        choices:
                            - 'real-time '
                            - 'history'
                    status:
                        type: str
                        default: 'open'
                        description:
                         - 'Widgets opened/closed state.'
                         - 'close - Widget closed.'
                         - 'open - Widget opened.'
                        choices:
                            - 'close'
                            - 'open'
                    tabid:
                        type: int
                        default: 0
                        description: 'ID of tab where widget is displayed.'
                    time-period:
                        type: str
                        default: '1hour'
                        description:
                         - 'Log Database Monitor widgets data period.'
                         - '1hour - 1 hour.'
                         - '8hour - 8 hour.'
                         - '24hour - 24 hour.'
                        choices:
                            - '1hour'
                            - '8hour'
                            - '24hour'
                    widget-type:
                        type: str
                        description:
                         - 'Widget type.'
                         - 'top-lograte - Log Receive Monitor.'
                         - 'sysres - System resources.'
                         - 'sysinfo - System Information.'
                         - 'licinfo - License Information.'
                         - 'jsconsole - CLI Console.'
                         - 'sysop - Unit Operation.'
                         - 'alert - Alert Message Console.'
                         - 'statistics - Statistics.'
                         - 'rpteng - Report Engine.'
                         - 'raid - Disk Monitor.'
                         - 'logrecv - Logs/Data Received.'
                         - 'devsummary - Device Summary.'
                         - 'logdb-perf - Log Database Performance Monitor.'
                         - 'logdb-lag - Log Database Lag Time.'
                         - 'disk-io - Disk I/O.'
                         - 'log-rcvd-fwd - Log receive and forwarding Monitor.'
                        choices:
                            - 'top-lograte'
                            - 'sysres'
                            - 'sysinfo'
                            - 'licinfo'
                            - 'jsconsole'
                            - 'sysop'
                            - 'alert'
                            - 'statistics'
                            - 'rpteng'
                            - 'raid'
                            - 'logrecv'
                            - 'devsummary'
                            - 'logdb-perf'
                            - 'logdb-lag'
                            - 'disk-io'
                            - 'log-rcvd-fwd'
    schema_object1:
        methods: [get]
        description: 'Custom dashboard widgets.'
        api_categories: [api_tag0]
        api_tag0:
            fields:
                -
                    -
                        type: str
                        choices:
                            - 'column'
                            - 'diskio-content-type'
                            - 'diskio-period'
                            - 'log-rate-period'
                            - 'log-rate-topn'
                            - 'log-rate-type'
                            - 'moduleid'
                            - 'name'
                            - 'num-entries'
                            - 'refresh-interval'
                            - 'res-cpu-display'
                            - 'res-period'
                            - 'res-view-type'
                            - 'status'
                            - 'tabid'
                            - 'time-period'
                            - 'widget-type'
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

    - name: REQUESTING /CLI/SYSTEM/ADMIN/USER/{USER}/DASHBOARD
      fmgr_cli_system_admin_user_dashboard:
         method: <value in [add, set, update]>
         url_params:
            user: <value of string>
         params:
            -
               data:
                 -
                     column: <value of integer default: 0>
                     diskio-content-type: <value in [util, iops, blks] default: 'util'>
                     diskio-period: <value in [1hour, 8hour, 24hour] default: '1hour'>
                     log-rate-period: <value in [2min , 1hour, 6hours]>
                     log-rate-topn: <value in [1, 2, 3, ...] default: '5'>
                     log-rate-type: <value in [log, device] default: 'device'>
                     moduleid: <value of integer default: 0>
                     name: <value of string>
                     num-entries: <value of integer default: 10>
                     refresh-interval: <value of integer default: 300>
                     res-cpu-display: <value in [average , each] default: 'average '>
                     res-period: <value in [10min , hour, day] default: '10min '>
                     res-view-type: <value in [real-time , history] default: 'history'>
                     status: <value in [close, open] default: 'open'>
                     tabid: <value of integer default: 0>
                     time-period: <value in [1hour, 8hour, 24hour] default: '1hour'>
                     widget-type: <value in [top-lograte, sysres, sysinfo, ...]>

    - name: REQUESTING /CLI/SYSTEM/ADMIN/USER/{USER}/DASHBOARD
      fmgr_cli_system_admin_user_dashboard:
         method: <value in [get]>
         url_params:
            user: <value of string>
         params:
            -
               fields:
                 -
                    - <value in [column, diskio-content-type, diskio-period, ...]>
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
            example: '/cli/global/system/admin/user/{user}/dashboard'
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
               column:
                  type: int
                  description: 'Widgets column ID.'
                  example: 0
               diskio-content-type:
                  type: str
                  description: |
                     'Disk I/O Monitor widgets chart type.'
                     'util - bandwidth utilization.'
                     'iops - the number of I/O requests.'
                     'blks - the amount of data of I/O requests.'
                  example: 'util'
               diskio-period:
                  type: str
                  description: |
                     'Disk I/O Monitor widgets data period.'
                     '1hour - 1 hour.'
                     '8hour - 8 hour.'
                     '24hour - 24 hour.'
                  example: '1hour'
               log-rate-period:
                  type: str
                  description: |
                     'Log receive monitor widgets data period.'
                     '2min  - 2 minutes.'
                     '1hour - 1 hour.'
                     '6hours - 6 hours.'
               log-rate-topn:
                  type: str
                  description: |
                     'Log receive monitor widgets number of top items to display.'
                     '1 - Top 1.'
                     '2 - Top 2.'
                     '3 - Top 3.'
                     '4 - Top 4.'
                     '5 - Top 5.'
                  example: '5'
               log-rate-type:
                  type: str
                  description: |
                     'Log receive monitor widgets statistics breakdown options.'
                     'log - Show log rates for each log type.'
                     'device - Show log rates for each device.'
                  example: 'device'
               moduleid:
                  type: int
                  description: 'Widget ID.'
                  example: 0
               name:
                  type: str
                  description: 'Widget name.'
               num-entries:
                  type: int
                  description: 'Number of entries.'
                  example: 10
               refresh-interval:
                  type: int
                  description: 'Widgets refresh interval.'
                  example: 300
               res-cpu-display:
                  type: str
                  description: |
                     'Widgets CPU display type.'
                     'average  - Average usage of CPU.'
                     'each - Each usage of CPU.'
                  example: 'average '
               res-period:
                  type: str
                  description: |
                     'Widgets data period.'
                     '10min  - Last 10 minutes.'
                     'hour - Last hour.'
                     'day - Last day.'
                  example: '10min '
               res-view-type:
                  type: str
                  description: |
                     'Widgets data view type.'
                     'real-time  - Real-time view.'
                     'history - History view.'
                  example: 'history'
               status:
                  type: str
                  description: |
                     'Widgets opened/closed state.'
                     'close - Widget closed.'
                     'open - Widget opened.'
                  example: 'open'
               tabid:
                  type: int
                  description: 'ID of tab where widget is displayed.'
                  example: 0
               time-period:
                  type: str
                  description: |
                     'Log Database Monitor widgets data period.'
                     '1hour - 1 hour.'
                     '8hour - 8 hour.'
                     '24hour - 24 hour.'
                  example: '1hour'
               widget-type:
                  type: str
                  description: |
                     'Widget type.'
                     'top-lograte - Log Receive Monitor.'
                     'sysres - System resources.'
                     'sysinfo - System Information.'
                     'licinfo - License Information.'
                     'jsconsole - CLI Console.'
                     'sysop - Unit Operation.'
                     'alert - Alert Message Console.'
                     'statistics - Statistics.'
                     'rpteng - Report Engine.'
                     'raid - Disk Monitor.'
                     'logrecv - Logs/Data Received.'
                     'devsummary - Device Summary.'
                     'logdb-perf - Log Database Performance Monitor.'
                     'logdb-lag - Log Database Lag Time.'
                     'disk-io - Disk I/O.'
                     'log-rcvd-fwd - Log receive and forwarding Monitor.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/cli/global/system/admin/user/{user}/dashboard'

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
        '/cli/global/system/admin/user/{user}/dashboard'
    ]

    url_schema = [
        {
            'name': 'user',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'column': {
                            'type': 'integer',
                            'default': 0,
                            'example': 0
                        },
                        'diskio-content-type': {
                            'type': 'string',
                            'enum': [
                                'util',
                                'iops',
                                'blks'
                            ]
                        },
                        'diskio-period': {
                            'type': 'string',
                            'enum': [
                                '1hour',
                                '8hour',
                                '24hour'
                            ]
                        },
                        'log-rate-period': {
                            'type': 'string',
                            'enum': [
                                '2min ',
                                '1hour',
                                '6hours'
                            ]
                        },
                        'log-rate-topn': {
                            'type': 'string',
                            'enum': [
                                '1',
                                '2',
                                '3',
                                '4',
                                '5'
                            ]
                        },
                        'log-rate-type': {
                            'type': 'string',
                            'enum': [
                                'log',
                                'device'
                            ]
                        },
                        'moduleid': {
                            'type': 'integer',
                            'default': 0,
                            'example': 0
                        },
                        'name': {
                            'type': 'string'
                        },
                        'num-entries': {
                            'type': 'integer',
                            'default': 10,
                            'example': 10
                        },
                        'refresh-interval': {
                            'type': 'integer',
                            'default': 300,
                            'example': 300
                        },
                        'res-cpu-display': {
                            'type': 'string',
                            'enum': [
                                'average ',
                                'each'
                            ]
                        },
                        'res-period': {
                            'type': 'string',
                            'enum': [
                                '10min ',
                                'hour',
                                'day'
                            ]
                        },
                        'res-view-type': {
                            'type': 'string',
                            'enum': [
                                'real-time ',
                                'history'
                            ]
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'close',
                                'open'
                            ]
                        },
                        'tabid': {
                            'type': 'integer',
                            'default': 0,
                            'example': 0
                        },
                        'time-period': {
                            'type': 'string',
                            'enum': [
                                '1hour',
                                '8hour',
                                '24hour'
                            ]
                        },
                        'widget-type': {
                            'type': 'string',
                            'enum': [
                                'top-lograte',
                                'sysres',
                                'sysinfo',
                                'licinfo',
                                'jsconsole',
                                'sysop',
                                'alert',
                                'statistics',
                                'rpteng',
                                'raid',
                                'logrecv',
                                'devsummary',
                                'logdb-perf',
                                'logdb-lag',
                                'disk-io',
                                'log-rcvd-fwd'
                            ]
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
                                'column',
                                'diskio-content-type',
                                'diskio-period',
                                'log-rate-period',
                                'log-rate-topn',
                                'log-rate-type',
                                'moduleid',
                                'name',
                                'num-entries',
                                'refresh-interval',
                                'res-cpu-display',
                                'res-period',
                                'res-view-type',
                                'status',
                                'tabid',
                                'time-period',
                                'widget-type'
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
