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
module: fmgr_system_sql
short_description: SQL settings.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /cli/global/system/sql
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
        description: 'SQL settings.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'SQL settings.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                background-rebuild:
                    type: str
                    default: 'enable'
                    description:
                     - 'Disable/Enable rebuild SQL database in the background.'
                     - 'disable - Rebuild SQL database not in the background.'
                     - 'enable - Rebuild SQL database in the background.'
                    choices:
                        - 'disable'
                        - 'enable'
                custom-index:
                    -
                        case-sensitive:
                            type: str
                            default: 'disable'
                            description:
                             - 'Disable/Enable case sensitive index.'
                             - 'disable - Build a case insensitive index.'
                             - 'enable - Build a case sensitive index.'
                            choices:
                                - 'disable'
                                - 'enable'
                        device-type:
                            type: str
                            default: 'FortiGate'
                            description:
                             - 'Device type.'
                             - 'FortiGate - Device type to FortiGate.'
                             - 'FortiManager - Set device type to FortiManager'
                             - 'FortiClient - Set device type to FortiClient'
                             - 'FortiMail - Device type to FortiMail.'
                             - 'FortiWeb - Device type to FortiWeb.'
                             - 'FortiCache - Set device type to FortiCache'
                             - 'FortiSandbox - Set device type to FortiSandbox'
                             - 'FortiDDoS - Set device type to FortiDDoS'
                             - 'FortiAuthenticator - Set device type to FortiAuthenticator'
                             - 'FortiProxy - Set device type to FortiProxy'
                            choices:
                                - 'FortiGate'
                                - 'FortiManager'
                                - 'FortiClient'
                                - 'FortiMail'
                                - 'FortiWeb'
                                - 'FortiCache'
                                - 'FortiSandbox'
                                - 'FortiDDoS'
                                - 'FortiAuthenticator'
                                - 'FortiProxy'
                        id:
                            type: int
                            default: 0
                            description: 'Add or Edit log index fields.'
                        index-field:
                            type: str
                            description: 'Log field name to be indexed.'
                        log-type:
                            type: str
                            default: 'traffic'
                            description:
                             - 'Log type.'
                             - 'none - none'
                             - 'app-ctrl '
                             - 'attack '
                             - 'content '
                             - 'dlp '
                             - 'emailfilter '
                             - 'event '
                             - 'generic '
                             - 'history '
                             - 'traffic '
                             - 'virus '
                             - 'voip '
                             - 'webfilter '
                             - 'netscan '
                             - 'fct-event '
                             - 'fct-traffic '
                             - 'fct-netscan '
                             - 'waf '
                             - 'gtp '
                             - 'dns '
                             - 'ssh '
                             - 'ssl '
                            choices:
                                - 'none'
                                - 'app-ctrl'
                                - 'attack'
                                - 'content'
                                - 'dlp'
                                - 'emailfilter'
                                - 'event'
                                - 'generic'
                                - 'history'
                                - 'traffic'
                                - 'virus'
                                - 'voip'
                                - 'webfilter'
                                - 'netscan'
                                - 'fct-event'
                                - 'fct-traffic'
                                - 'fct-netscan'
                                - 'waf'
                                - 'gtp'
                                - 'dns'
                                - 'ssh'
                                - 'ssl'
                database-name:
                    type: str
                    description: 'Database name.'
                database-type:
                    type: str
                    default: 'postgres'
                    description:
                     - 'Database type.'
                     - 'mysql - MySQL database.'
                     - 'postgres - PostgreSQL local database.'
                    choices:
                        - 'mysql'
                        - 'postgres'
                device-count-high:
                    type: str
                    default: 'disable'
                    description:
                     - 'Must set to enable if the count of registered devices is greater than 8000.'
                     - 'disable - Set to disable if device count is less than 8000.'
                     - 'enable - Set to enable if device count is equal to or greater than 8000.'
                    choices:
                        - 'disable'
                        - 'enable'
                event-table-partition-time:
                    type: int
                    default: 0
                    description: 'Maximum SQL database table partitioning time range in minute (0 for unlimited) for event logs.'
                fct-table-partition-time:
                    type: int
                    default: 240
                    description: 'Maximum SQL database table partitioning time range in minute (0 for unlimited) for FortiClient logs.'
                logtype:
                    -
                        type: str
                        choices:
                            - 'none'
                            - 'app-ctrl'
                            - 'attack'
                            - 'content'
                            - 'dlp'
                            - 'emailfilter'
                            - 'event'
                            - 'generic'
                            - 'history'
                            - 'traffic'
                            - 'virus'
                            - 'voip'
                            - 'webfilter'
                            - 'netscan'
                            - 'fct-event'
                            - 'fct-traffic'
                            - 'fct-netscan'
                            - 'waf'
                            - 'gtp'
                            - 'dns'
                            - 'ssh'
                            - 'ssl'
                password:
                    -
                        type: str
                        default: 'ENC NjQ3NzAyNTQ0MjIyMDUxNUE+4gCrDBIJb7pqPICInSs5KmyrG1Tt8M8Zl+eK2k42FSlwDSDiBpNLwRPdCyo8dSIl+p0KUlKP781RcCnzzGAb/gOob+zQw...'
                prompt-sql-upgrade:
                    type: str
                    default: 'enable'
                    description:
                     - 'Prompt to convert log database into SQL database at start time on GUI.'
                     - 'disable - Do not prompt to upgrade log database to SQL database at start time on GUI.'
                     - 'enable - Prompt to upgrade log database to SQL database at start time on GUI.'
                    choices:
                        - 'disable'
                        - 'enable'
                rebuild-event:
                    type: str
                    default: 'enable'
                    description:
                     - 'Disable/Enable rebuild event during SQL database rebuilding.'
                     - 'disable - Do not rebuild event during SQL database rebuilding.'
                     - 'enable - Rebuild event during SQL database rebuilding.'
                    choices:
                        - 'disable'
                        - 'enable'
                rebuild-event-start-time:
                    -
                        type: str
                server:
                    type: str
                    description: 'Database IP or hostname.'
                start-time:
                    -
                        type: str
                status:
                    type: str
                    default: 'local'
                    description:
                     - 'SQL database status.'
                     - 'disable - Disable SQL database.'
                     - 'local - Enable local database.'
                    choices:
                        - 'disable'
                        - 'local'
                text-search-index:
                    type: str
                    default: 'disable'
                    description:
                     - 'Disable/Enable text search index.'
                     - 'disable - Do not create text search index.'
                     - 'enable - Create text search index.'
                    choices:
                        - 'disable'
                        - 'enable'
                traffic-table-partition-time:
                    type: int
                    default: 0
                    description: 'Maximum SQL database table partitioning time range in minute (0 for unlimited) for traffic logs.'
                ts-index-field:
                    -
                        category:
                            type: str
                            description: 'Category of text search index fields.'
                        value:
                            type: str
                            description: 'Fields of text search index.'
                username:
                    type: str
                    description: 'User name for login remote database.'
                utm-table-partition-time:
                    type: int
                    default: 0
                    description: 'Maximum SQL database table partitioning time range in minute (0 for unlimited) for UTM logs.'

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

    - name: REQUESTING /CLI/SYSTEM/SQL
      fmgr_system_sql:
         method: <value in [set, update]>
         params:
            -
               data:
                  background-rebuild: <value in [disable, enable] default: 'enable'>
                  custom-index:
                    -
                        case-sensitive: <value in [disable, enable] default: 'disable'>
                        device-type: <value in [FortiGate, FortiManager, FortiClient, ...] default: 'FortiGate'>
                        id: <value of integer default: 0>
                        index-field: <value of string>
                        log-type: <value in [none, app-ctrl, attack, ...] default: 'traffic'>
                  database-name: <value of string>
                  database-type: <value in [mysql, postgres] default: 'postgres'>
                  device-count-high: <value in [disable, enable] default: 'disable'>
                  event-table-partition-time: <value of integer default: 0>
                  fct-table-partition-time: <value of integer default: 240>
                  logtype:
                    - <value in [none, app-ctrl, attack, ...]>
                  password:
                    - <value of string default: 'ENC NjQ3NzAyNTQ0MjIyMDUxNUE+4gCrDBIJb7pqPICInSs5KmyrG1Tt8M8Zl+eK2k42FSlwDSDi...'>
                  prompt-sql-upgrade: <value in [disable, enable] default: 'enable'>
                  rebuild-event: <value in [disable, enable] default: 'enable'>
                  rebuild-event-start-time:
                    - <value of string>
                  server: <value of string>
                  start-time:
                    - <value of string>
                  status: <value in [disable, local] default: 'local'>
                  text-search-index: <value in [disable, enable] default: 'disable'>
                  traffic-table-partition-time: <value of integer default: 0>
                  ts-index-field:
                    -
                        category: <value of string>
                        value: <value of string>
                  username: <value of string>
                  utm-table-partition-time: <value of integer default: 0>

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
            background-rebuild:
               type: str
               description: |
                  'Disable/Enable rebuild SQL database in the background.'
                  'disable - Rebuild SQL database not in the background.'
                  'enable - Rebuild SQL database in the background.'
               example: 'enable'
            custom-index:
               type: array
               suboptions:
                  case-sensitive:
                     type: str
                     description: |
                        'Disable/Enable case sensitive index.'
                        'disable - Build a case insensitive index.'
                        'enable - Build a case sensitive index.'
                     example: 'disable'
                  device-type:
                     type: str
                     description: |
                        'Device type.'
                        'FortiGate - Device type to FortiGate.'
                        'FortiManager - Set device type to FortiManager'
                        'FortiClient - Set device type to FortiClient'
                        'FortiMail - Device type to FortiMail.'
                        'FortiWeb - Device type to FortiWeb.'
                        'FortiCache - Set device type to FortiCache'
                        'FortiSandbox - Set device type to FortiSandbox'
                        'FortiDDoS - Set device type to FortiDDoS'
                        'FortiAuthenticator - Set device type to FortiAuthenticator'
                        'FortiProxy - Set device type to FortiProxy'
                     example: 'FortiGate'
                  id:
                     type: int
                     description: 'Add or Edit log index fields.'
                     example: 0
                  index-field:
                     type: str
                     description: 'Log field name to be indexed.'
                  log-type:
                     type: str
                     description: |
                        'Log type.'
                        'none - none'
                        'app-ctrl '
                        'attack '
                        'content '
                        'dlp '
                        'emailfilter '
                        'event '
                        'generic '
                        'history '
                        'traffic '
                        'virus '
                        'voip '
                        'webfilter '
                        'netscan '
                        'fct-event '
                        'fct-traffic '
                        'fct-netscan '
                        'waf '
                        'gtp '
                        'dns '
                        'ssh '
                        'ssl '
                     example: 'traffic'
            database-name:
               type: str
               description: 'Database name.'
            database-type:
               type: str
               description: |
                  'Database type.'
                  'mysql - MySQL database.'
                  'postgres - PostgreSQL local database.'
               example: 'postgres'
            device-count-high:
               type: str
               description: |
                  'Must set to enable if the count of registered devices is greater than 8000.'
                  'disable - Set to disable if device count is less than 8000.'
                  'enable - Set to enable if device count is equal to or greater than 8000.'
               example: 'disable'
            event-table-partition-time:
               type: int
               description: 'Maximum SQL database table partitioning time range in minute (0 for unlimited) for event logs.'
               example: 0
            fct-table-partition-time:
               type: int
               description: 'Maximum SQL database table partitioning time range in minute (0 for unlimited) for FortiClient logs.'
               example: 240
            logtype:
               type: array
               suboptions:
                  type: str
            password:
               type: array
               suboptions:
                  type: str
                  example: 'ENC NjQ3NzAyNTQ0MjIyMDUxNUE+4gCrDBIJb7pqPICInSs5KmyrG1Tt8M8Zl+eK2k42FSlwDSDi...'
            prompt-sql-upgrade:
               type: str
               description: |
                  'Prompt to convert log database into SQL database at start time on GUI.'
                  'disable - Do not prompt to upgrade log database to SQL database at start time on GUI.'
                  'enable - Prompt to upgrade log database to SQL database at start time on GUI.'
               example: 'enable'
            rebuild-event:
               type: str
               description: |
                  'Disable/Enable rebuild event during SQL database rebuilding.'
                  'disable - Do not rebuild event during SQL database rebuilding.'
                  'enable - Rebuild event during SQL database rebuilding.'
               example: 'enable'
            rebuild-event-start-time:
               type: array
               suboptions:
                  type: str
            server:
               type: str
               description: 'Database IP or hostname.'
            start-time:
               type: array
               suboptions:
                  type: str
            status:
               type: str
               description: |
                  'SQL database status.'
                  'disable - Disable SQL database.'
                  'local - Enable local database.'
               example: 'local'
            text-search-index:
               type: str
               description: |
                  'Disable/Enable text search index.'
                  'disable - Do not create text search index.'
                  'enable - Create text search index.'
               example: 'disable'
            traffic-table-partition-time:
               type: int
               description: 'Maximum SQL database table partitioning time range in minute (0 for unlimited) for traffic logs.'
               example: 0
            ts-index-field:
               type: array
               suboptions:
                  category:
                     type: str
                     description: 'Category of text search index fields.'
                  value:
                     type: str
                     description: 'Fields of text search index.'
            username:
               type: str
               description: 'User name for login remote database.'
            utm-table-partition-time:
               type: int
               description: 'Maximum SQL database table partitioning time range in minute (0 for unlimited) for UTM logs.'
               example: 0
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/cli/global/system/sql'
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
            example: '/cli/global/system/sql'

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
        '/cli/global/system/sql'
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
                        'background-rebuild': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'custom-index': {
                            'type': 'array',
                            'items': {
                                'case-sensitive': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'device-type': {
                                    'type': 'string',
                                    'enum': [
                                        'FortiGate',
                                        'FortiManager',
                                        'FortiClient',
                                        'FortiMail',
                                        'FortiWeb',
                                        'FortiCache',
                                        'FortiSandbox',
                                        'FortiDDoS',
                                        'FortiAuthenticator',
                                        'FortiProxy'
                                    ]
                                },
                                'id': {
                                    'type': 'integer',
                                    'default': 0,
                                    'example': 0
                                },
                                'index-field': {
                                    'type': 'string'
                                },
                                'log-type': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'app-ctrl',
                                        'attack',
                                        'content',
                                        'dlp',
                                        'emailfilter',
                                        'event',
                                        'generic',
                                        'history',
                                        'traffic',
                                        'virus',
                                        'voip',
                                        'webfilter',
                                        'netscan',
                                        'fct-event',
                                        'fct-traffic',
                                        'fct-netscan',
                                        'waf',
                                        'gtp',
                                        'dns',
                                        'ssh',
                                        'ssl'
                                    ]
                                }
                            }
                        },
                        'database-name': {
                            'type': 'string'
                        },
                        'database-type': {
                            'type': 'string',
                            'enum': [
                                'mysql',
                                'postgres'
                            ]
                        },
                        'device-count-high': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'event-table-partition-time': {
                            'type': 'integer',
                            'default': 0,
                            'example': 0
                        },
                        'fct-table-partition-time': {
                            'type': 'integer',
                            'default': 240,
                            'example': 240
                        },
                        'logtype': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'none',
                                    'app-ctrl',
                                    'attack',
                                    'content',
                                    'dlp',
                                    'emailfilter',
                                    'event',
                                    'generic',
                                    'history',
                                    'traffic',
                                    'virus',
                                    'voip',
                                    'webfilter',
                                    'netscan',
                                    'fct-event',
                                    'fct-traffic',
                                    'fct-netscan',
                                    'waf',
                                    'gtp',
                                    'dns',
                                    'ssh',
                                    'ssl'
                                ]
                            }
                        },
                        'password': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'prompt-sql-upgrade': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'rebuild-event': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'rebuild-event-start-time': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'server': {
                            'type': 'string'
                        },
                        'start-time': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'local'
                            ]
                        },
                        'text-search-index': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'traffic-table-partition-time': {
                            'type': 'integer',
                            'default': 0,
                            'example': 0
                        },
                        'ts-index-field': {
                            'type': 'array',
                            'items': {
                                'category': {
                                    'type': 'string'
                                },
                                'value': {
                                    'type': 'string'
                                }
                            }
                        },
                        'username': {
                            'type': 'string'
                        },
                        'utm-table-partition-time': {
                            'type': 'integer',
                            'default': 0,
                            'example': 0
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

    module.exit_json(meta=response[1])


if __name__ == '__main__':
    main()
