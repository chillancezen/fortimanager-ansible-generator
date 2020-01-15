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
module: fmgr_dvmdb_adom
short_description: ADOM table, most attributes are read-only and can only be changed internally.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /dvmdb/adom
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
        description: 'ADOM table, most attributes are read-only and can only be changed internally.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    desc:
                        type: str
                    flags:
                        -
                            type: str
                            choices:
                                - 'migration'
                                - 'db_export'
                                - 'no_vpn_console'
                                - 'backup'
                                - 'other_devices'
                                - 'central_sdwan'
                                - 'is_autosync'
                                - 'per_device_wtp'
                                - 'policy_check_on_install'
                                - 'install_on_policy_check_fail'
                                - 'auto_push_cfg'
                    log_db_retention_hours:
                        type: int
                        default: 1440
                    log_disk_quota:
                        type: int
                    log_disk_quota_alert_thres:
                        type: int
                        default: 90
                    log_disk_quota_split_ratio:
                        type: int
                        default: 70
                    log_file_retention_hours:
                        type: int
                        default: 8760
                    meta fields:
                        type: str
                    mig_mr:
                        type: int
                        default: 2
                    mig_os_ver:
                        type: str
                        default: '6.0'
                        choices:
                            - 'unknown'
                            - '0.0'
                            - '1.0'
                            - '2.0'
                            - '3.0'
                            - '4.0'
                            - '5.0'
                            - '6.0'
                    mode:
                        type: str
                        default: 'gms'
                        description:
                         - 'ems - (Value no longer used as of 4.3)'
                         - 'provider - Global database.'
                        choices:
                            - 'ems'
                            - 'gms'
                            - 'provider'
                    mr:
                        type: int
                        default: 2
                    name:
                        type: str
                    os_ver:
                        type: str
                        default: '6.0'
                        choices:
                            - 'unknown'
                            - '0.0'
                            - '1.0'
                            - '2.0'
                            - '3.0'
                            - '4.0'
                            - '5.0'
                            - '6.0'
                    restricted_prds:
                        -
                            type: str
                            choices:
                                - 'fos'
                                - 'foc'
                                - 'fml'
                                - 'fch'
                                - 'fwb'
                                - 'log'
                                - 'fct'
                                - 'faz'
                                - 'fsa'
                                - 'fsw'
                                - 'fmg'
                                - 'fdd'
                                - 'fac'
                                - 'fpx'
                    state:
                        type: int
                        default: 1
                    uuid:
                        type: str
    schema_object1:
        methods: [get]
        description: 'ADOM table, most attributes are read-only and can only be changed internally.'
        api_categories: [api_tag0]
        api_tag0:
            expand member:
                type: str
                description: 'Fetch all or selected attributes of object members.'
            fields:
                -
                    -
                        type: str
                        choices:
                            - 'desc'
                            - 'flags'
                            - 'log_db_retention_hours'
                            - 'log_disk_quota'
                            - 'log_disk_quota_alert_thres'
                            - 'log_disk_quota_split_ratio'
                            - 'log_file_retention_hours'
                            - 'mig_mr'
                            - 'mig_os_ver'
                            - 'mode'
                            - 'mr'
                            - 'name'
                            - 'os_ver'
                            - 'restricted_prds'
                            - 'state'
                            - 'uuid'
            filter:
                -
                    type: str
            loadsub:
                type: int
                description: 'Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.'
            meta fields:
                -
                    type: str
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.'
                 - 'count - Return the number of matching entries instead of the actual entry data.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'syntax - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.'
                choices:
                    - 'count'
                    - 'object member'
                    - 'syntax'
            range:
                -
                    type: int
            sortings:
                -
                    varidic.attr_name:
                        type: int
                        choices:
                            - 1
                            - -1

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /DVMDB/ADOM
      fmgr_dvmdb_adom:
         method: <value in [add, set, update]>
         params:
            -
               data:
                 -
                     desc: <value of string>
                     flags:
                       - <value in [migration, db_export, no_vpn_console, ...]>
                     log_db_retention_hours: <value of integer default: 1440>
                     log_disk_quota: <value of integer>
                     log_disk_quota_alert_thres: <value of integer default: 90>
                     log_disk_quota_split_ratio: <value of integer default: 70>
                     log_file_retention_hours: <value of integer default: 8760>
                     meta fields: <value of string>
                     mig_mr: <value of integer default: 2>
                     mig_os_ver: <value in [unknown, 0.0, 1.0, ...] default: '6.0'>
                     mode: <value in [ems, gms, provider] default: 'gms'>
                     mr: <value of integer default: 2>
                     name: <value of string>
                     os_ver: <value in [unknown, 0.0, 1.0, ...] default: '6.0'>
                     restricted_prds:
                       - <value in [fos, foc, fml, ...]>
                     state: <value of integer default: 1>
                     uuid: <value of string>

    - name: REQUESTING /DVMDB/ADOM
      fmgr_dvmdb_adom:
         method: <value in [get]>
         params:
            -
               expand member: <value of string>
               fields:
                 -
                    - <value in [desc, flags, log_db_retention_hours, ...]>
               filter:
                 - <value of string>
               loadsub: <value of integer>
               meta fields:
                 - <value of string>
               option: <value in [count, object member, syntax]>
               range:
                 - <value of integer>
               sortings:
                 -
                     varidic.attr_name: <value in [1, -1]>

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
            example: '/dvmdb/adom'
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
               desc:
                  type: str
               flags:
                  type: array
                  suboptions:
                     type: str
               log_db_retention_hours:
                  type: int
                  example: 1440
               log_disk_quota:
                  type: int
               log_disk_quota_alert_thres:
                  type: int
                  example: 90
               log_disk_quota_split_ratio:
                  type: int
                  example: 70
               log_file_retention_hours:
                  type: int
                  example: 8760
               meta fields:
                  type: str
               mig_mr:
                  type: int
                  example: 2
               mig_os_ver:
                  type: str
                  example: '6.0'
               mode:
                  type: str
                  description: |
                     'ems - (Value no longer used as of 4.3)'
                     'provider - Global database.'
                  example: 'gms'
               mr:
                  type: int
                  example: 2
               name:
                  type: str
               os_ver:
                  type: str
                  example: '6.0'
               restricted_prds:
                  type: array
                  suboptions:
                     type: str
               state:
                  type: int
                  example: 1
               uuid:
                  type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/dvmdb/adom'

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
        '/dvmdb/adom'
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
                        'desc': {
                            'type': 'string'
                        },
                        'flags': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'migration',
                                    'db_export',
                                    'no_vpn_console',
                                    'backup',
                                    'other_devices',
                                    'central_sdwan',
                                    'is_autosync',
                                    'per_device_wtp',
                                    'policy_check_on_install',
                                    'install_on_policy_check_fail',
                                    'auto_push_cfg'
                                ]
                            }
                        },
                        'log_db_retention_hours': {
                            'type': 'integer',
                            'default': 1440,
                            'example': 1440
                        },
                        'log_disk_quota': {
                            'type': 'integer'
                        },
                        'log_disk_quota_alert_thres': {
                            'type': 'integer',
                            'default': 90,
                            'example': 90
                        },
                        'log_disk_quota_split_ratio': {
                            'type': 'integer',
                            'default': 70,
                            'example': 70
                        },
                        'log_file_retention_hours': {
                            'type': 'integer',
                            'default': 8760,
                            'example': 8760
                        },
                        'meta fields': {
                            'type': 'string'
                        },
                        'mig_mr': {
                            'type': 'integer',
                            'default': 2,
                            'example': 2
                        },
                        'mig_os_ver': {
                            'type': 'string',
                            'enum': [
                                'unknown',
                                '0.0',
                                '1.0',
                                '2.0',
                                '3.0',
                                '4.0',
                                '5.0',
                                '6.0'
                            ]
                        },
                        'mode': {
                            'type': 'string',
                            'enum': [
                                'ems',
                                'gms',
                                'provider'
                            ]
                        },
                        'mr': {
                            'type': 'integer',
                            'default': 2,
                            'example': 2
                        },
                        'name': {
                            'type': 'string'
                        },
                        'os_ver': {
                            'type': 'string',
                            'enum': [
                                'unknown',
                                '0.0',
                                '1.0',
                                '2.0',
                                '3.0',
                                '4.0',
                                '5.0',
                                '6.0'
                            ]
                        },
                        'restricted_prds': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'fos',
                                    'foc',
                                    'fml',
                                    'fch',
                                    'fwb',
                                    'log',
                                    'fct',
                                    'faz',
                                    'fsa',
                                    'fsw',
                                    'fmg',
                                    'fdd',
                                    'fac',
                                    'fpx'
                                ]
                            }
                        },
                        'state': {
                            'type': 'integer',
                            'default': 1,
                            'example': 1
                        },
                        'uuid': {
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
                    'type': 'string',
                    'name': 'expand member',
                    'api_tag': 0
                },
                {
                    'name': 'fields',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'enum': [
                                'desc',
                                'flags',
                                'log_db_retention_hours',
                                'log_disk_quota',
                                'log_disk_quota_alert_thres',
                                'log_disk_quota_split_ratio',
                                'log_file_retention_hours',
                                'mig_mr',
                                'mig_os_ver',
                                'mode',
                                'mr',
                                'name',
                                'os_ver',
                                'restricted_prds',
                                'state',
                                'uuid'
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
                    'name': 'meta fields',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'type': 'string'
                    }
                },
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'count',
                            'object member',
                            'syntax'
                        ]
                    },
                    'api_tag': 0
                },
                {
                    'name': 'range',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            'type': 'integer',
                            'example': [
                                2,
                                5
                            ]
                        }
                    },
                    'api_tag': 0
                },
                {
                    'name': 'sortings',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            '{attr_name}': {
                                'type': 'integer',
                                'enum': [
                                    1,
                                    -1
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

    module.exit_json(meta=response[1])


if __name__ == '__main__':
    main()
