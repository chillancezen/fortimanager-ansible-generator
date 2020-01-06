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
module: fmgr_cli_system_locallog_syslogd3_filter
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /cli/global/system/locallog/syslogd3/filter
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
        description: 'Filter for syslog logging.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Filter for syslog logging.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                devcfg:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log device configuration message.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                devops:
                    type: str
                    default: 'enable'
                    description:
                     - 'Managered devices operations messages.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                diskquota:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log Fortianalyzer disk quota messages.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                dm:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log deployment manager message.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                dvm:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log device manager messages.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                ediscovery:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log Fortianalyzer ediscovery messages.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                epmgr:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log endpoint manager message.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                event:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log event messages.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                eventmgmt:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log Fortianalyzer event handler messages.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                faz:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log Fortianalyzer messages.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                fazha:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log Fortianalyzer HA messages.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                fazsys:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log Fortianalyzer system messages.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                fgd:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log FortiGuard service message.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                fgfm:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log FGFM protocol message.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                fips:
                    type: str
                    default: 'enable'
                    description:
                     - 'Whether to log fips messages.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                fmgws:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log web service messages.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                fmlmgr:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log FortiMail manager message.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                fmwmgr:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log firmware manager message.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                fortiview:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log Fortianalyzer FortiView messages.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                glbcfg:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log global database message.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                ha:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log HA message.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                hcache:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log Fortianalyzer hcache messages.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                iolog:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log debug IO log message.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                logd:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log the status of log daemon.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                logdb:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log Fortianalyzer log DB messages.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                logdev:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log Fortianalyzer log device messages.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                logfile:
                    type: str
                    description:
                     - 'Log Fortianalyzer log file messages.'
                     - 'enable - Enable setting.'
                     - 'disable - Disable setting.'
                    choices:
                        - 'enable'
                        - 'disable'
                logging:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log Fortianalyzer logging messages.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                lrmgr:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log log and report manager message.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                objcfg:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log object configuration change message.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                report:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log Fortianalyzer report messages.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                rev:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log revision history message.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                rtmon:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log real-time monitor message.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                scfw:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log firewall objects message.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                scply:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log policy console message.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                scrmgr:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log script manager message.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                scvpn:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log VPN console message.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                system:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log system manager message.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                webport:
                    type: str
                    default: 'enable'
                    description:
                     - 'Log web portal message.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /cli/system/locallog/syslogd3/filter
      fmgr_cli_system_locallog_syslogd3_filter:
         method: <value in [set, update]>
         params:
            - 
               data: 
                  devcfg: <value in [disable, enable] default: enable>
                  devops: <value in [disable, enable] default: enable>
                  diskquota: <value in [disable, enable] default: enable>
                  dm: <value in [disable, enable] default: enable>
                  dvm: <value in [disable, enable] default: enable>
                  ediscovery: <value in [disable, enable] default: enable>
                  epmgr: <value in [disable, enable] default: enable>
                  event: <value in [disable, enable] default: enable>
                  eventmgmt: <value in [disable, enable] default: enable>
                  faz: <value in [disable, enable] default: enable>
                  fazha: <value in [disable, enable] default: enable>
                  fazsys: <value in [disable, enable] default: enable>
                  fgd: <value in [disable, enable] default: enable>
                  fgfm: <value in [disable, enable] default: enable>
                  fips: <value in [disable, enable] default: enable>
                  fmgws: <value in [disable, enable] default: enable>
                  fmlmgr: <value in [disable, enable] default: enable>
                  fmwmgr: <value in [disable, enable] default: enable>
                  fortiview: <value in [disable, enable] default: enable>
                  glbcfg: <value in [disable, enable] default: enable>
                  ha: <value in [disable, enable] default: enable>
                  hcache: <value in [disable, enable] default: enable>
                  iolog: <value in [disable, enable] default: enable>
                  logd: <value in [disable, enable] default: enable>
                  logdb: <value in [disable, enable] default: enable>
                  logdev: <value in [disable, enable] default: enable>
                  logfile: <value in [enable, disable]>
                  logging: <value in [disable, enable] default: enable>
                  lrmgr: <value in [disable, enable] default: enable>
                  objcfg: <value in [disable, enable] default: enable>
                  report: <value in [disable, enable] default: enable>
                  rev: <value in [disable, enable] default: enable>
                  rtmon: <value in [disable, enable] default: enable>
                  scfw: <value in [disable, enable] default: enable>
                  scply: <value in [disable, enable] default: enable>
                  scrmgr: <value in [disable, enable] default: enable>
                  scvpn: <value in [disable, enable] default: enable>
                  system: <value in [disable, enable] default: enable>
                  webport: <value in [disable, enable] default: enable>

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
            devcfg:
               type: str
               description: |
                  'Log device configuration message.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            devops:
               type: str
               description: |
                  'Managered devices operations messages.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            diskquota:
               type: str
               description: |
                  'Log Fortianalyzer disk quota messages.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            dm:
               type: str
               description: |
                  'Log deployment manager message.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            dvm:
               type: str
               description: |
                  'Log device manager messages.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            ediscovery:
               type: str
               description: |
                  'Log Fortianalyzer ediscovery messages.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            epmgr:
               type: str
               description: |
                  'Log endpoint manager message.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            event:
               type: str
               description: |
                  'Log event messages.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            eventmgmt:
               type: str
               description: |
                  'Log Fortianalyzer event handler messages.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            faz:
               type: str
               description: |
                  'Log Fortianalyzer messages.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            fazha:
               type: str
               description: |
                  'Log Fortianalyzer HA messages.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            fazsys:
               type: str
               description: |
                  'Log Fortianalyzer system messages.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            fgd:
               type: str
               description: |
                  'Log FortiGuard service message.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            fgfm:
               type: str
               description: |
                  'Log FGFM protocol message.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            fips:
               type: str
               description: |
                  'Whether to log fips messages.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            fmgws:
               type: str
               description: |
                  'Log web service messages.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            fmlmgr:
               type: str
               description: |
                  'Log FortiMail manager message.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            fmwmgr:
               type: str
               description: |
                  'Log firmware manager message.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            fortiview:
               type: str
               description: |
                  'Log Fortianalyzer FortiView messages.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            glbcfg:
               type: str
               description: |
                  'Log global database message.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            ha:
               type: str
               description: |
                  'Log HA message.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            hcache:
               type: str
               description: |
                  'Log Fortianalyzer hcache messages.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            iolog:
               type: str
               description: |
                  'Log debug IO log message.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            logd:
               type: str
               description: |
                  'Log the status of log daemon.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            logdb:
               type: str
               description: |
                  'Log Fortianalyzer log DB messages.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            logdev:
               type: str
               description: |
                  'Log Fortianalyzer log device messages.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            logfile:
               type: str
               description: |
                  'Log Fortianalyzer log file messages.'
                  'enable - Enable setting.'
                  'disable - Disable setting.'
            logging:
               type: str
               description: |
                  'Log Fortianalyzer logging messages.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            lrmgr:
               type: str
               description: |
                  'Log log and report manager message.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            objcfg:
               type: str
               description: |
                  'Log object configuration change message.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            report:
               type: str
               description: |
                  'Log Fortianalyzer report messages.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            rev:
               type: str
               description: |
                  'Log revision history message.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            rtmon:
               type: str
               description: |
                  'Log real-time monitor message.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            scfw:
               type: str
               description: |
                  'Log firewall objects message.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            scply:
               type: str
               description: |
                  'Log policy console message.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            scrmgr:
               type: str
               description: |
                  'Log script manager message.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            scvpn:
               type: str
               description: |
                  'Log VPN console message.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            system:
               type: str
               description: |
                  'Log system manager message.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            webport:
               type: str
               description: |
                  'Log web portal message.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /cli/global/system/locallog/syslogd3/filter
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
            example: /cli/global/system/locallog/syslogd3/filter

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
        '/cli/global/system/locallog/syslogd3/filter'
    ]

    url_schema = [
    ]

    body_schema =  {
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
                        'devcfg': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'devops': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'diskquota': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dm': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dvm': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ediscovery': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'epmgr': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'event': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'eventmgmt': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'faz': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fazha': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fazsys': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fgd': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fgfm': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fips': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fmgws': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fmlmgr': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fmwmgr': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fortiview': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'glbcfg': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ha': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'hcache': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'iolog': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'logd': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'logdb': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'logdev': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'logfile': {
                            'type': 'string',
                            'enum': [
                                'enable',
                                'disable'
                            ]
                        },
                        'logging': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'lrmgr': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'objcfg': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'report': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'rev': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'rtmon': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'scfw': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'scply': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'scrmgr': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'scvpn': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'system': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'webport': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
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
    module = AnsibleModule(argument_spec = module_arg_spec,
                           supports_check_mode = False)
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
        fmgr.govern_response(module = module, results = response,
                             msg = 'Operation Finished',
                             ansible_facts = fmgr.construct_ansible_facts(
                                response, module.params, module.params))
    except Exception as e:
        raise FMGBaseException(e)

    module.exit_json(**response[1])

if __name__ == '__main__':
    main()