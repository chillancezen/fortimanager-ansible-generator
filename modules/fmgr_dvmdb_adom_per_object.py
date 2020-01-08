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
module: fmgr_dvmdb_adom_per_object
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ delete get set update add ] the following apis.
    - /dvmdb/adom/{adom}
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
    schema_object0:
        methods: [delete]
        description: 'ADOM table, most attributes are read-only and can only be changed internally.'
        api_categories: [api_tag0, api_tag1]
        api_tag0:
        api_tag1:
            data:
                -
                    name:
                        type: str
                    vdom:
                        type: str
    schema_object1:
        methods: [get]
        description: 'ADOM table, most attributes are read-only and can only be changed internally.'
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
    schema_object2:
        methods: [set, update]
        description: 'ADOM table, most attributes are read-only and can only be changed internally.'
        api_categories: [api_tag0, api_tag1]
        api_tag0:
            data:
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
        api_tag1:
            data:
                -
                    name:
                        type: str
                    vdom:
                        type: str
    schema_object3:
        methods: [add]
        description: 'ADOM table, most attributes are read-only and can only be changed internally.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    name:
                        type: str
                    vdom:
                        type: str

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /DVMDB/ADOM/{ADOM}
      fmgr_dvmdb_adom_per_object:
         method: <value in [delete]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     name: <value of string>
                     vdom: <value of string>

    - name: REQUESTING /DVMDB/ADOM/{ADOM}
      fmgr_dvmdb_adom_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               option: <value in [object member, chksum]>

    - name: REQUESTING /DVMDB/ADOM/{ADOM}
      fmgr_dvmdb_adom_per_object:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
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

    - name: REQUESTING /DVMDB/ADOM/{ADOM}
      fmgr_dvmdb_adom_per_object:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     name: <value of string>
                     vdom: <value of string>

    - name: REQUESTING /DVMDB/ADOM/{ADOM}
      fmgr_dvmdb_adom_per_object:
         method: <value in [add]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     name: <value of string>
                     vdom: <value of string>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[delete, set, update]
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
            example: '/dvmdb/adom/{adom}'
return_of_api_category_1:
   description: items returned for method:[delete, set, update]
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
            example: '/dvmdb/adom/{adom}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
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
            example: '/dvmdb/adom/{adom}'
return_of_api_category_0:
   description: items returned for method:[add]
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
            example: '/dvmdb/adom/{adom}'

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
        '/dvmdb/adom/{adom}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                },
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            'name': {
                                'type': 'string'
                            },
                            'vdom': {
                                'type': 'string'
                            }
                        }
                    },
                    'api_tag': 1
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 1
                }
            ],
            'object1': [
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'object member',
                            'chksum'
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
            'object2': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
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
                    },
                    'api_tag': 0
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                },
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            'name': {
                                'type': 'string'
                            },
                            'vdom': {
                                'type': 'string'
                            }
                        }
                    },
                    'api_tag': 1
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 1
                }
            ],
            'object3': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            'name': {
                                'type': 'string'
                            },
                            'vdom': {
                                'type': 'string'
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
            'delete': 'object0',
            'get': 'object1',
            'set': 'object2',
            'update': 'object2',
            'add': 'object3'
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
                'delete',
                'get',
                'set',
                'update',
                'add'
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
