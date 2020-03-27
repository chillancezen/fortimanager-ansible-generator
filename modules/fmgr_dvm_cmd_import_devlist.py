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
module: fmgr_dvm_cmd_import_devlist
short_description: Import a list of ADOMs and devices.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ exec ] the following apis.
    - /dvm/cmd/import/dev-list
    - /dvm/cmd/import/dev-list
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
        methods: [exec]
        description: 'Import a list of ADOMs and devices.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                adom:
                    type: str
                    description: 'Name or ID of the ADOM where the command is to be executed on.'
                flags:
                    -
                        type: str
                        choices:
                            - 'none'
                            - 'create_task'
                            - 'nonblocking'
                            - 'log_dev'
                import-adom-members:
                    -
                        adom:
                            type: str
                            description: 'Target ADOM to associate device VDOM with.'
                        dev:
                            type: str
                        vdom:
                            type: str
                import-adoms:
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
                import-devices:
                    -
                        adm_pass:
                            -
                                type: str
                        adm_usr:
                            type: str
                        app_ver:
                            type: str
                        av_ver:
                            type: str
                        beta:
                            type: int
                        branch_pt:
                            type: int
                        build:
                            type: int
                        checksum:
                            type: str
                        conf_status:
                            type: str
                            default: 'unknown'
                            choices:
                                - 'unknown'
                                - 'insync'
                                - 'outofsync'
                        conn_mode:
                            type: str
                            default: 'passive'
                            choices:
                                - 'active'
                                - 'passive'
                        conn_status:
                            type: str
                            default: 'UNKNOWN'
                            choices:
                                - 'UNKNOWN'
                                - 'up'
                                - 'down'
                        db_status:
                            type: str
                            default: 'unknown'
                            choices:
                                - 'unknown'
                                - 'nomod'
                                - 'mod'
                        desc:
                            type: str
                        dev_status:
                            type: str
                            default: 'unknown'
                            choices:
                                - 'none'
                                - 'unknown'
                                - 'checkedin'
                                - 'inprogress'
                                - 'installed'
                                - 'aborted'
                                - 'sched'
                                - 'retry'
                                - 'canceled'
                                - 'pending'
                                - 'retrieved'
                                - 'changed_conf'
                                - 'sync_fail'
                                - 'timeout'
                                - 'rev_revert'
                                - 'auto_updated'
                        fap_cnt:
                            type: int
                        faz.full_act:
                            type: int
                        faz.perm:
                            type: int
                        faz.quota:
                            type: int
                        faz.used:
                            type: int
                        fex_cnt:
                            type: int
                        flags:
                            -
                                type: str
                                choices:
                                    - 'has_hdd'
                                    - 'vdom_enabled'
                                    - 'discover'
                                    - 'reload'
                                    - 'interim_build'
                                    - 'offline_mode'
                                    - 'is_model'
                                    - 'fips_mode'
                                    - 'linked_to_model'
                                    - 'ip-conflict'
                                    - 'faz-autosync'
                        foslic_cpu:
                            type: int
                            description: 'VM Meter vCPU count.'
                        foslic_dr_site:
                            type: str
                            default: 'disable'
                            description: 'VM Meter DR Site status.'
                            choices:
                                - 'disable'
                                - 'enable'
                        foslic_inst_time:
                            type: int
                            description: 'VM Meter first deployment time (in UNIX timestamp).'
                        foslic_last_sync:
                            type: int
                            description: 'VM Meter last synchronized time (in UNIX timestamp).'
                        foslic_ram:
                            type: int
                            description: 'VM Meter device RAM size (in MB).'
                        foslic_type:
                            type: str
                            default: 'temporary'
                            description: 'VM Meter license type.'
                            choices:
                                - 'temporary'
                                - 'trial'
                                - 'regular'
                                - 'trial_expired'
                        foslic_utm:
                            -
                                type: str
                                choices:
                                    - 'fw'
                                    - 'av'
                                    - 'ips'
                                    - 'app'
                                    - 'url'
                                    - 'utm'
                                    - 'fwb'
                        fsw_cnt:
                            type: int
                        ha_group_id:
                            type: int
                        ha_group_name:
                            type: str
                        ha_mode:
                            type: str
                            default: 'standalone'
                            description: 'enabled - Value reserved for non-FOS HA devices.'
                            choices:
                                - 'standalone'
                                - 'AP'
                                - 'AA'
                                - 'ELBC'
                                - 'DUAL'
                                - 'enabled'
                                - 'unknown'
                        ha_slave:
                            -
                                idx:
                                    type: int
                                name:
                                    type: str
                                prio:
                                    type: int
                                role:
                                    type: str
                                    default: 'slave'
                                    choices:
                                        - 'slave'
                                        - 'master'
                                sn:
                                    type: str
                                status:
                                    type: int
                        hdisk_size:
                            type: int
                        hostname:
                            type: str
                        hw_rev_major:
                            type: int
                        hw_rev_minor:
                            type: int
                        ip:
                            type: str
                        ips_ext:
                            type: int
                        ips_ver:
                            type: str
                        last_checked:
                            type: int
                        last_resync:
                            type: int
                        latitude:
                            type: str
                        lic_flags:
                            type: int
                        lic_region:
                            type: str
                        location_from:
                            type: str
                        logdisk_size:
                            type: int
                        longitude:
                            type: str
                        maxvdom:
                            type: int
                            default: 10
                        meta fields:
                            type: str
                        mgmt_id:
                            type: int
                        mgmt_if:
                            type: str
                        mgmt_mode:
                            type: str
                            default: 'unreg'
                            choices:
                                - 'unreg'
                                - 'fmg'
                                - 'faz'
                                - 'fmgfaz'
                        mgt_vdom:
                            type: str
                        mr:
                            type: int
                            default: -1
                        name:
                            type: str
                            description: 'Unique name for the device.'
                        os_type:
                            type: str
                            default: 'unknown'
                            choices:
                                - 'unknown'
                                - 'fos'
                                - 'fsw'
                                - 'foc'
                                - 'fml'
                                - 'faz'
                                - 'fwb'
                                - 'fch'
                                - 'fct'
                                - 'log'
                                - 'fmg'
                                - 'fsa'
                                - 'fdd'
                                - 'fac'
                                - 'fpx'
                        os_ver:
                            type: str
                            default: 'unknown'
                            choices:
                                - 'unknown'
                                - '0.0'
                                - '1.0'
                                - '2.0'
                                - '3.0'
                                - '4.0'
                                - '5.0'
                                - '6.0'
                        patch:
                            type: int
                        platform_str:
                            type: str
                        psk:
                            type: str
                        sn:
                            type: str
                            description: 'Unique value for each device.'
                        vdom:
                            -
                                comments:
                                    type: str
                                name:
                                    type: str
                                opmode:
                                    type: str
                                    default: 'nat'
                                    choices:
                                        - 'nat'
                                        - 'transparent'
                                rtm_prof_id:
                                    type: int
                                status:
                                    type: str
                        version:
                            type: int
                        vm_cpu:
                            type: int
                        vm_cpu_limit:
                            type: int
                        vm_lic_expire:
                            type: int
                        vm_mem:
                            type: int
                        vm_mem_limit:
                            type: int
                        vm_status:
                            type: int
                import-group-members:
                    -
                        adom:
                            type: str
                            description: 'ADOM where the device group is located. Default is "root" if not specified.'
                        dev:
                            type: str
                        grp:
                            type: str
                            description: 'Target device group to associate device VDOM with.'
                        vdom:
                            type: str

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

    - name: REQUESTING /DVM/CMD/IMPORT/DEV-LIST
      fmgr_dvm_cmd_import_devlist:
         method: <value in [exec]>
         params:
            -
               data:
                  adom: <value of string>
                  flags:
                    - <value in [none, create_task, nonblocking, ...]>
                  import-adom-members:
                    -
                        adom: <value of string>
                        dev: <value of string>
                        vdom: <value of string>
                  import-adoms:
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
                  import-devices:
                    -
                        adm_pass:
                          - <value of string>
                        adm_usr: <value of string>
                        app_ver: <value of string>
                        av_ver: <value of string>
                        beta: <value of integer>
                        branch_pt: <value of integer>
                        build: <value of integer>
                        checksum: <value of string>
                        conf_status: <value in [unknown, insync, outofsync] default: 'unknown'>
                        conn_mode: <value in [active, passive] default: 'passive'>
                        conn_status: <value in [UNKNOWN, up, down] default: 'UNKNOWN'>
                        db_status: <value in [unknown, nomod, mod] default: 'unknown'>
                        desc: <value of string>
                        dev_status: <value in [none, unknown, checkedin, ...] default: 'unknown'>
                        fap_cnt: <value of integer>
                        faz.full_act: <value of integer>
                        faz.perm: <value of integer>
                        faz.quota: <value of integer>
                        faz.used: <value of integer>
                        fex_cnt: <value of integer>
                        flags:
                          - <value in [has_hdd, vdom_enabled, discover, ...]>
                        foslic_cpu: <value of integer>
                        foslic_dr_site: <value in [disable, enable] default: 'disable'>
                        foslic_inst_time: <value of integer>
                        foslic_last_sync: <value of integer>
                        foslic_ram: <value of integer>
                        foslic_type: <value in [temporary, trial, regular, ...] default: 'temporary'>
                        foslic_utm:
                          - <value in [fw, av, ips, ...]>
                        fsw_cnt: <value of integer>
                        ha_group_id: <value of integer>
                        ha_group_name: <value of string>
                        ha_mode: <value in [standalone, AP, AA, ...] default: 'standalone'>
                        ha_slave:
                          -
                              idx: <value of integer>
                              name: <value of string>
                              prio: <value of integer>
                              role: <value in [slave, master] default: 'slave'>
                              sn: <value of string>
                              status: <value of integer>
                        hdisk_size: <value of integer>
                        hostname: <value of string>
                        hw_rev_major: <value of integer>
                        hw_rev_minor: <value of integer>
                        ip: <value of string>
                        ips_ext: <value of integer>
                        ips_ver: <value of string>
                        last_checked: <value of integer>
                        last_resync: <value of integer>
                        latitude: <value of string>
                        lic_flags: <value of integer>
                        lic_region: <value of string>
                        location_from: <value of string>
                        logdisk_size: <value of integer>
                        longitude: <value of string>
                        maxvdom: <value of integer default: 10>
                        meta fields: <value of string>
                        mgmt_id: <value of integer>
                        mgmt_if: <value of string>
                        mgmt_mode: <value in [unreg, fmg, faz, ...] default: 'unreg'>
                        mgt_vdom: <value of string>
                        mr: <value of integer default: -1>
                        name: <value of string>
                        os_type: <value in [unknown, fos, fsw, ...] default: 'unknown'>
                        os_ver: <value in [unknown, 0.0, 1.0, ...] default: 'unknown'>
                        patch: <value of integer>
                        platform_str: <value of string>
                        psk: <value of string>
                        sn: <value of string>
                        vdom:
                          -
                              comments: <value of string>
                              name: <value of string>
                              opmode: <value in [nat, transparent] default: 'nat'>
                              rtm_prof_id: <value of integer>
                              status: <value of string>
                        version: <value of integer>
                        vm_cpu: <value of integer>
                        vm_cpu_limit: <value of integer>
                        vm_lic_expire: <value of integer>
                        vm_mem: <value of integer>
                        vm_mem_limit: <value of integer>
                        vm_status: <value of integer>
                  import-group-members:
                    -
                        adom: <value of string>
                        dev: <value of string>
                        grp: <value of string>
                        vdom: <value of string>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[exec]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            pid:
               type: int
               description: 'When "nonblocking" flag is set, return the process ID for the command.'
            taskid:
               type: str
               description: 'When "create_task" flag is set, return the ID of the task associated with the command.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/dvm/cmd/import/dev-list'

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
        '/dvm/cmd/import/dev-list',
        '/dvm/cmd/import/dev-list'
    ]

    url_schema = [
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'adom': {
                            'type': 'string'
                        },
                        'flags': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'none',
                                    'create_task',
                                    'nonblocking',
                                    'log_dev'
                                ]
                            }
                        },
                        'import-adom-members': {
                            'type': 'array',
                            'items': {
                                'adom': {
                                    'type': 'string'
                                },
                                'dev': {
                                    'type': 'string'
                                },
                                'vdom': {
                                    'type': 'string'
                                }
                            }
                        },
                        'import-adoms': {
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
                        'import-devices': {
                            'type': 'array',
                            'items': {
                                'adm_pass': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                },
                                'adm_usr': {
                                    'type': 'string'
                                },
                                'app_ver': {
                                    'type': 'string'
                                },
                                'av_ver': {
                                    'type': 'string'
                                },
                                'beta': {
                                    'type': 'integer'
                                },
                                'branch_pt': {
                                    'type': 'integer'
                                },
                                'build': {
                                    'type': 'integer'
                                },
                                'checksum': {
                                    'type': 'string'
                                },
                                'conf_status': {
                                    'type': 'string',
                                    'enum': [
                                        'unknown',
                                        'insync',
                                        'outofsync'
                                    ]
                                },
                                'conn_mode': {
                                    'type': 'string',
                                    'enum': [
                                        'active',
                                        'passive'
                                    ]
                                },
                                'conn_status': {
                                    'type': 'string',
                                    'enum': [
                                        'UNKNOWN',
                                        'up',
                                        'down'
                                    ]
                                },
                                'db_status': {
                                    'type': 'string',
                                    'enum': [
                                        'unknown',
                                        'nomod',
                                        'mod'
                                    ]
                                },
                                'desc': {
                                    'type': 'string'
                                },
                                'dev_status': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'unknown',
                                        'checkedin',
                                        'inprogress',
                                        'installed',
                                        'aborted',
                                        'sched',
                                        'retry',
                                        'canceled',
                                        'pending',
                                        'retrieved',
                                        'changed_conf',
                                        'sync_fail',
                                        'timeout',
                                        'rev_revert',
                                        'auto_updated'
                                    ]
                                },
                                'fap_cnt': {
                                    'type': 'integer'
                                },
                                'faz.full_act': {
                                    'type': 'integer'
                                },
                                'faz.perm': {
                                    'type': 'integer'
                                },
                                'faz.quota': {
                                    'type': 'integer'
                                },
                                'faz.used': {
                                    'type': 'integer'
                                },
                                'fex_cnt': {
                                    'type': 'integer'
                                },
                                'flags': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string',
                                        'enum': [
                                            'has_hdd',
                                            'vdom_enabled',
                                            'discover',
                                            'reload',
                                            'interim_build',
                                            'offline_mode',
                                            'is_model',
                                            'fips_mode',
                                            'linked_to_model',
                                            'ip-conflict',
                                            'faz-autosync'
                                        ]
                                    }
                                },
                                'foslic_cpu': {
                                    'type': 'integer'
                                },
                                'foslic_dr_site': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'foslic_inst_time': {
                                    'type': 'integer'
                                },
                                'foslic_last_sync': {
                                    'type': 'integer'
                                },
                                'foslic_ram': {
                                    'type': 'integer'
                                },
                                'foslic_type': {
                                    'type': 'string',
                                    'enum': [
                                        'temporary',
                                        'trial',
                                        'regular',
                                        'trial_expired'
                                    ]
                                },
                                'foslic_utm': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string',
                                        'enum': [
                                            'fw',
                                            'av',
                                            'ips',
                                            'app',
                                            'url',
                                            'utm',
                                            'fwb'
                                        ]
                                    }
                                },
                                'fsw_cnt': {
                                    'type': 'integer'
                                },
                                'ha_group_id': {
                                    'type': 'integer'
                                },
                                'ha_group_name': {
                                    'type': 'string'
                                },
                                'ha_mode': {
                                    'type': 'string',
                                    'enum': [
                                        'standalone',
                                        'AP',
                                        'AA',
                                        'ELBC',
                                        'DUAL',
                                        'enabled',
                                        'unknown'
                                    ]
                                },
                                'ha_slave': {
                                    'type': 'array',
                                    'items': {
                                        'idx': {
                                            'type': 'integer'
                                        },
                                        'name': {
                                            'type': 'string'
                                        },
                                        'prio': {
                                            'type': 'integer'
                                        },
                                        'role': {
                                            'type': 'string',
                                            'enum': [
                                                'slave',
                                                'master'
                                            ]
                                        },
                                        'sn': {
                                            'type': 'string'
                                        },
                                        'status': {
                                            'type': 'integer'
                                        }
                                    }
                                },
                                'hdisk_size': {
                                    'type': 'integer'
                                },
                                'hostname': {
                                    'type': 'string'
                                },
                                'hw_rev_major': {
                                    'type': 'integer'
                                },
                                'hw_rev_minor': {
                                    'type': 'integer'
                                },
                                'ip': {
                                    'type': 'string'
                                },
                                'ips_ext': {
                                    'type': 'integer'
                                },
                                'ips_ver': {
                                    'type': 'string'
                                },
                                'last_checked': {
                                    'type': 'integer'
                                },
                                'last_resync': {
                                    'type': 'integer'
                                },
                                'latitude': {
                                    'type': 'string'
                                },
                                'lic_flags': {
                                    'type': 'integer'
                                },
                                'lic_region': {
                                    'type': 'string'
                                },
                                'location_from': {
                                    'type': 'string'
                                },
                                'logdisk_size': {
                                    'type': 'integer'
                                },
                                'longitude': {
                                    'type': 'string'
                                },
                                'maxvdom': {
                                    'type': 'integer',
                                    'default': 10,
                                    'example': 10
                                },
                                'meta fields': {
                                    'type': 'string'
                                },
                                'mgmt_id': {
                                    'type': 'integer'
                                },
                                'mgmt_if': {
                                    'type': 'string'
                                },
                                'mgmt_mode': {
                                    'type': 'string',
                                    'enum': [
                                        'unreg',
                                        'fmg',
                                        'faz',
                                        'fmgfaz'
                                    ]
                                },
                                'mgt_vdom': {
                                    'type': 'string'
                                },
                                'mr': {
                                    'type': 'integer',
                                    'default': -1,
                                    'example': -1
                                },
                                'name': {
                                    'type': 'string'
                                },
                                'os_type': {
                                    'type': 'string',
                                    'enum': [
                                        'unknown',
                                        'fos',
                                        'fsw',
                                        'foc',
                                        'fml',
                                        'faz',
                                        'fwb',
                                        'fch',
                                        'fct',
                                        'log',
                                        'fmg',
                                        'fsa',
                                        'fdd',
                                        'fac',
                                        'fpx'
                                    ]
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
                                'patch': {
                                    'type': 'integer'
                                },
                                'platform_str': {
                                    'type': 'string'
                                },
                                'psk': {
                                    'type': 'string'
                                },
                                'sn': {
                                    'type': 'string'
                                },
                                'vdom': {
                                    'type': 'array',
                                    'items': {
                                        'comments': {
                                            'type': 'string'
                                        },
                                        'name': {
                                            'type': 'string'
                                        },
                                        'opmode': {
                                            'type': 'string',
                                            'enum': [
                                                'nat',
                                                'transparent'
                                            ]
                                        },
                                        'rtm_prof_id': {
                                            'type': 'integer'
                                        },
                                        'status': {
                                            'type': 'string'
                                        }
                                    }
                                },
                                'version': {
                                    'type': 'integer'
                                },
                                'vm_cpu': {
                                    'type': 'integer'
                                },
                                'vm_cpu_limit': {
                                    'type': 'integer'
                                },
                                'vm_lic_expire': {
                                    'type': 'integer'
                                },
                                'vm_mem': {
                                    'type': 'integer'
                                },
                                'vm_mem_limit': {
                                    'type': 'integer'
                                },
                                'vm_status': {
                                    'type': 'integer'
                                }
                            }
                        },
                        'import-group-members': {
                            'type': 'array',
                            'items': {
                                'adom': {
                                    'type': 'string'
                                },
                                'dev': {
                                    'type': 'string'
                                },
                                'grp': {
                                    'type': 'string'
                                },
                                'vdom': {
                                    'type': 'string'
                                }
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
            'exec': 'object0'
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
                'exec'
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
