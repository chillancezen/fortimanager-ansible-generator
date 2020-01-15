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
module: fmgr_fmupdate_webspam_fgdsetting
short_description: Configure the FortiGuard run parameters.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /cli/global/fmupdate/web-spam/fgd-setting
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
        description: 'Configure the FortiGuard run parameters.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Configure the FortiGuard run parameters.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                as-cache:
                    type: int
                    default: 300
                    description: 'Antispam service maximum memory usage in megabytes (Maximum = Physical memory-1024, 0: no limit, default = 300).'
                as-log:
                    type: str
                    default: 'nospam'
                    description:
                     - 'Antispam log setting (default = nospam).'
                     - 'disable - Disable spam log.'
                     - 'nospam - Log non-spam events.'
                     - 'all - Log all spam lookups.'
                    choices:
                        - 'disable'
                        - 'nospam'
                        - 'all'
                as-preload:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable preloading antispam database to memory (default = disable).'
                     - 'disable - Disable antispam database preload.'
                     - 'enable - Enable antispam database preload.'
                    choices:
                        - 'disable'
                        - 'enable'
                av-cache:
                    type: int
                    default: 300
                    description: 'Antivirus service maximum memory usage, in megabytes (100 - 500, default = 300).'
                av-log:
                    type: str
                    default: 'novirus'
                    description:
                     - 'Antivirus log setting (default = novirus).'
                     - 'disable - Disable virus log.'
                     - 'novirus - Log non-virus events.'
                     - 'all - Log all virus lookups.'
                    choices:
                        - 'disable'
                        - 'novirus'
                        - 'all'
                av-preload:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable preloading antivirus database to memory (default = disable).'
                     - 'disable - Disable antivirus database preload.'
                     - 'enable - Enable antivirus database preload.'
                    choices:
                        - 'disable'
                        - 'enable'
                av2-cache:
                    type: int
                    default: 800
                    description: 'Antispam service maximum memory usage in megabytes (Maximum = Physical memory-1024, 0: no limit, default = 800).'
                av2-log:
                    type: str
                    default: 'noav2'
                    description:
                     - 'Outbreak prevention log setting (default = noav2).'
                     - 'disable - Disable av2 log.'
                     - 'noav2 - Log non-av2 events.'
                     - 'all - Log all av2 lookups.'
                    choices:
                        - 'disable'
                        - 'noav2'
                        - 'all'
                av2-preload:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable preloading outbreak prevention database to memory (default = disable).'
                     - 'disable - Disable outbreak prevention database preload.'
                     - 'enable - Enable outbreak prevention database preload.'
                    choices:
                        - 'disable'
                        - 'enable'
                eventlog-query:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable record query to event-log besides fgd-log (default = disable).'
                     - 'disable - Record query to event-log besides fgd-log.'
                     - 'enable - Do not log to event-log.'
                    choices:
                        - 'disable'
                        - 'enable'
                fgd-pull-interval:
                    type: int
                    default: 10
                    description: 'Fgd pull interval setting, in minutes (1 - 1440, default = 10).'
                fq-cache:
                    type: int
                    default: 300
                    description: 'File query service maximum memory usage, in megabytes (100 - 500, default = 300).'
                fq-log:
                    type: str
                    default: 'nofilequery'
                    description:
                     - 'File query log setting (default = nofilequery).'
                     - 'disable - Disable file query log.'
                     - 'nofilequery - Log non-file query events.'
                     - 'all - Log all file query events.'
                    choices:
                        - 'disable'
                        - 'nofilequery'
                        - 'all'
                fq-preload:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable preloading file query database to memory (default = disable).'
                     - 'disable - Disable file query db preload.'
                     - 'enable - Enable file query db preload.'
                    choices:
                        - 'disable'
                        - 'enable'
                linkd-log:
                    type: str
                    default: 'debug'
                    description:
                     - 'Linkd log setting (default = debug).'
                     - 'emergency - The unit is unusable.'
                     - 'alert - Immediate action is required'
                     - 'critical - Functionality is affected.'
                     - 'error - Functionality is probably affected.'
                     - 'warn - Functionality might be affected.'
                     - 'notice - Information about normal events.'
                     - 'info - General information.'
                     - 'debug - Debug information.'
                     - 'disable - Linkd logging is disabled.'
                    choices:
                        - 'emergency'
                        - 'alert'
                        - 'critical'
                        - 'error'
                        - 'warn'
                        - 'notice'
                        - 'info'
                        - 'debug'
                        - 'disable'
                max-client-worker:
                    type: int
                    default: 0
                    description: 'max worker for tcp client connection (0~16: 0 means use cpu number up to 4).'
                max-log-quota:
                    type: int
                    default: 6144
                    description: 'Maximum log quota setting, in megabytes (100 - 20480, default = 6144).'
                max-unrated-site:
                    type: int
                    default: 500
                    description: 'Maximum number of unrated site in memory, in kilobytes(10 - 5120, default = 500).'
                restrict-as1-dbver:
                    type: str
                    description: 'Restrict system update to indicated antispam(1) database version (character limit = 127).'
                restrict-as2-dbver:
                    type: str
                    description: 'Restrict system update to indicated antispam(2) database version (character limit = 127).'
                restrict-as4-dbver:
                    type: str
                    description: 'Restrict system update to indicated antispam(4) database version (character limit = 127).'
                restrict-av-dbver:
                    type: str
                    description: 'Restrict system update to indicated antivirus database version (character limit = 127).'
                restrict-av2-dbver:
                    type: str
                    description: 'Restrict system update to indicated outbreak prevention database version (character limit = 127).'
                restrict-fq-dbver:
                    type: str
                    description: 'Restrict system update to indicated file query database version (character limit = 127).'
                restrict-wf-dbver:
                    type: str
                    description: 'Restrict system update to indicated web filter database version (character limit = 127).'
                server-override:
                    servlist:
                        -
                            id:
                                type: int
                                default: 0
                                description: 'Override server ID (1 - 10).'
                            ip:
                                type: str
                                default: '0.0.0.0'
                                description: 'IPv4 address of the override server.'
                            ip6:
                                type: str
                                default: '::'
                                description: 'IPv6 address of the override server.'
                            port:
                                type: int
                                default: 443
                                description: 'Port number to use when contacting FortiGuard (1 - 65535, default = 443).'
                            service-type:
                                -
                                    type: str
                                    choices:
                                        - 'fgd'
                                        - 'fgc'
                                        - 'fsa'
                    status:
                        type: str
                        default: 'disable'
                        description:
                         - 'Override status.'
                         - 'disable - Disable setting.'
                         - 'enable - Enable setting.'
                        choices:
                            - 'disable'
                            - 'enable'
                stat-log-interval:
                    type: int
                    default: 60
                    description: 'Statistic log interval setting, in minutes (1 - 1440, default = 60).'
                stat-sync-interval:
                    type: int
                    default: 60
                    description: 'Synchronization interval for statistic of unrated site in minutes (1 - 60, default = 60).'
                update-interval:
                    type: int
                    default: 6
                    description: 'FortiGuard database update wait time if not enough delta files, in hours (2 - 24, default = 6).'
                update-log:
                    type: str
                    default: 'enable'
                    description:
                     - 'Enable/disable update log setting (default = enable).'
                     - 'disable - Disable update log.'
                     - 'enable - Enable update log.'
                    choices:
                        - 'disable'
                        - 'enable'
                wf-cache:
                    type: int
                    default: 0
                    description: 'Web filter service maximum memory usage, in megabytes (maximum = Physical memory-1024, 0 = no limit, default = 600).'
                wf-dn-cache-expire-time:
                    type: int
                    default: 30
                    description: 'Web filter DN cache expire time, in minutes (1 - 1440, 0 = never, default = 30).'
                wf-dn-cache-max-number:
                    type: int
                    default: 10000
                    description: 'Maximum number of Web filter DN cache (0 = disable, default = 10000).'
                wf-log:
                    type: str
                    default: 'nourl'
                    description:
                     - 'Web filter log setting (default = nour1)'
                     - 'disable - Disable URL log.'
                     - 'nourl - Log non-URL events.'
                     - 'all - Log all URL lookups.'
                    choices:
                        - 'disable'
                        - 'nourl'
                        - 'all'
                wf-preload:
                    type: str
                    default: 'enable'
                    description:
                     - 'Enable/disable preloading the web filter database into memory (default = disable).'
                     - 'disable - Disable web filter database preload.'
                     - 'enable - Enable web filter database preload.'
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

    - name: REQUESTING /CLI/FMUPDATE/WEB-SPAM/FGD-SETTING
      fmgr_fmupdate_webspam_fgdsetting:
         method: <value in [set, update]>
         params:
            -
               data:
                  as-cache: <value of integer default: 300>
                  as-log: <value in [disable, nospam, all] default: 'nospam'>
                  as-preload: <value in [disable, enable] default: 'disable'>
                  av-cache: <value of integer default: 300>
                  av-log: <value in [disable, novirus, all] default: 'novirus'>
                  av-preload: <value in [disable, enable] default: 'disable'>
                  av2-cache: <value of integer default: 800>
                  av2-log: <value in [disable, noav2, all] default: 'noav2'>
                  av2-preload: <value in [disable, enable] default: 'disable'>
                  eventlog-query: <value in [disable, enable] default: 'disable'>
                  fgd-pull-interval: <value of integer default: 10>
                  fq-cache: <value of integer default: 300>
                  fq-log: <value in [disable, nofilequery, all] default: 'nofilequery'>
                  fq-preload: <value in [disable, enable] default: 'disable'>
                  linkd-log: <value in [emergency, alert, critical, ...] default: 'debug'>
                  max-client-worker: <value of integer default: 0>
                  max-log-quota: <value of integer default: 6144>
                  max-unrated-site: <value of integer default: 500>
                  restrict-as1-dbver: <value of string>
                  restrict-as2-dbver: <value of string>
                  restrict-as4-dbver: <value of string>
                  restrict-av-dbver: <value of string>
                  restrict-av2-dbver: <value of string>
                  restrict-fq-dbver: <value of string>
                  restrict-wf-dbver: <value of string>
                  server-override:
                     servlist:
                       -
                           id: <value of integer default: 0>
                           ip: <value of string default: '0.0.0.0'>
                           ip6: <value of string default: '::'>
                           port: <value of integer default: 443>
                           service-type:
                             - <value in [fgd, fgc, fsa]>
                     status: <value in [disable, enable] default: 'disable'>
                  stat-log-interval: <value of integer default: 60>
                  stat-sync-interval: <value of integer default: 60>
                  update-interval: <value of integer default: 6>
                  update-log: <value in [disable, enable] default: 'enable'>
                  wf-cache: <value of integer default: 0>
                  wf-dn-cache-expire-time: <value of integer default: 30>
                  wf-dn-cache-max-number: <value of integer default: 10000>
                  wf-log: <value in [disable, nourl, all] default: 'nourl'>
                  wf-preload: <value in [disable, enable] default: 'enable'>

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
            as-cache:
               type: int
               description: 'Antispam service maximum memory usage in megabytes (Maximum = Physical memory-1024, 0: no limit, default = 300).'
               example: 300
            as-log:
               type: str
               description: |
                  'Antispam log setting (default = nospam).'
                  'disable - Disable spam log.'
                  'nospam - Log non-spam events.'
                  'all - Log all spam lookups.'
               example: 'nospam'
            as-preload:
               type: str
               description: |
                  'Enable/disable preloading antispam database to memory (default = disable).'
                  'disable - Disable antispam database preload.'
                  'enable - Enable antispam database preload.'
               example: 'disable'
            av-cache:
               type: int
               description: 'Antivirus service maximum memory usage, in megabytes (100 - 500, default = 300).'
               example: 300
            av-log:
               type: str
               description: |
                  'Antivirus log setting (default = novirus).'
                  'disable - Disable virus log.'
                  'novirus - Log non-virus events.'
                  'all - Log all virus lookups.'
               example: 'novirus'
            av-preload:
               type: str
               description: |
                  'Enable/disable preloading antivirus database to memory (default = disable).'
                  'disable - Disable antivirus database preload.'
                  'enable - Enable antivirus database preload.'
               example: 'disable'
            av2-cache:
               type: int
               description: 'Antispam service maximum memory usage in megabytes (Maximum = Physical memory-1024, 0: no limit, default = 800).'
               example: 800
            av2-log:
               type: str
               description: |
                  'Outbreak prevention log setting (default = noav2).'
                  'disable - Disable av2 log.'
                  'noav2 - Log non-av2 events.'
                  'all - Log all av2 lookups.'
               example: 'noav2'
            av2-preload:
               type: str
               description: |
                  'Enable/disable preloading outbreak prevention database to memory (default = disable).'
                  'disable - Disable outbreak prevention database preload.'
                  'enable - Enable outbreak prevention database preload.'
               example: 'disable'
            eventlog-query:
               type: str
               description: |
                  'Enable/disable record query to event-log besides fgd-log (default = disable).'
                  'disable - Record query to event-log besides fgd-log.'
                  'enable - Do not log to event-log.'
               example: 'disable'
            fgd-pull-interval:
               type: int
               description: 'Fgd pull interval setting, in minutes (1 - 1440, default = 10).'
               example: 10
            fq-cache:
               type: int
               description: 'File query service maximum memory usage, in megabytes (100 - 500, default = 300).'
               example: 300
            fq-log:
               type: str
               description: |
                  'File query log setting (default = nofilequery).'
                  'disable - Disable file query log.'
                  'nofilequery - Log non-file query events.'
                  'all - Log all file query events.'
               example: 'nofilequery'
            fq-preload:
               type: str
               description: |
                  'Enable/disable preloading file query database to memory (default = disable).'
                  'disable - Disable file query db preload.'
                  'enable - Enable file query db preload.'
               example: 'disable'
            linkd-log:
               type: str
               description: |
                  'Linkd log setting (default = debug).'
                  'emergency - The unit is unusable.'
                  'alert - Immediate action is required'
                  'critical - Functionality is affected.'
                  'error - Functionality is probably affected.'
                  'warn - Functionality might be affected.'
                  'notice - Information about normal events.'
                  'info - General information.'
                  'debug - Debug information.'
                  'disable - Linkd logging is disabled.'
               example: 'debug'
            max-client-worker:
               type: int
               description: 'max worker for tcp client connection (0~16: 0 means use cpu number up to 4).'
               example: 0
            max-log-quota:
               type: int
               description: 'Maximum log quota setting, in megabytes (100 - 20480, default = 6144).'
               example: 6144
            max-unrated-site:
               type: int
               description: 'Maximum number of unrated site in memory, in kilobytes(10 - 5120, default = 500).'
               example: 500
            restrict-as1-dbver:
               type: str
               description: 'Restrict system update to indicated antispam(1) database version (character limit = 127).'
            restrict-as2-dbver:
               type: str
               description: 'Restrict system update to indicated antispam(2) database version (character limit = 127).'
            restrict-as4-dbver:
               type: str
               description: 'Restrict system update to indicated antispam(4) database version (character limit = 127).'
            restrict-av-dbver:
               type: str
               description: 'Restrict system update to indicated antivirus database version (character limit = 127).'
            restrict-av2-dbver:
               type: str
               description: 'Restrict system update to indicated outbreak prevention database version (character limit = 127).'
            restrict-fq-dbver:
               type: str
               description: 'Restrict system update to indicated file query database version (character limit = 127).'
            restrict-wf-dbver:
               type: str
               description: 'Restrict system update to indicated web filter database version (character limit = 127).'
            server-override:
               servlist:
                  type: array
                  suboptions:
                     id:
                        type: int
                        description: 'Override server ID (1 - 10).'
                        example: 0
                     ip:
                        type: str
                        description: 'IPv4 address of the override server.'
                        example: '0.0.0.0'
                     ip6:
                        type: str
                        description: 'IPv6 address of the override server.'
                        example: '::'
                     port:
                        type: int
                        description: 'Port number to use when contacting FortiGuard (1 - 65535, default = 443).'
                        example: 443
                     service-type:
                        type: array
                        suboptions:
                           type: str
               status:
                  type: str
                  description: |
                     'Override status.'
                     'disable - Disable setting.'
                     'enable - Enable setting.'
                  example: 'disable'
            stat-log-interval:
               type: int
               description: 'Statistic log interval setting, in minutes (1 - 1440, default = 60).'
               example: 60
            stat-sync-interval:
               type: int
               description: 'Synchronization interval for statistic of unrated site in minutes (1 - 60, default = 60).'
               example: 60
            update-interval:
               type: int
               description: 'FortiGuard database update wait time if not enough delta files, in hours (2 - 24, default = 6).'
               example: 6
            update-log:
               type: str
               description: |
                  'Enable/disable update log setting (default = enable).'
                  'disable - Disable update log.'
                  'enable - Enable update log.'
               example: 'enable'
            wf-cache:
               type: int
               description: 'Web filter service maximum memory usage, in megabytes (maximum = Physical memory-1024, 0 = no limit, default = 600).'
               example: 0
            wf-dn-cache-expire-time:
               type: int
               description: 'Web filter DN cache expire time, in minutes (1 - 1440, 0 = never, default = 30).'
               example: 30
            wf-dn-cache-max-number:
               type: int
               description: 'Maximum number of Web filter DN cache (0 = disable, default = 10000).'
               example: 10000
            wf-log:
               type: str
               description: |
                  'Web filter log setting (default = nour1)'
                  'disable - Disable URL log.'
                  'nourl - Log non-URL events.'
                  'all - Log all URL lookups.'
               example: 'nourl'
            wf-preload:
               type: str
               description: |
                  'Enable/disable preloading the web filter database into memory (default = disable).'
                  'disable - Disable web filter database preload.'
                  'enable - Enable web filter database preload.'
               example: 'enable'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/cli/global/fmupdate/web-spam/fgd-setting'
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
            example: '/cli/global/fmupdate/web-spam/fgd-setting'

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
        '/cli/global/fmupdate/web-spam/fgd-setting'
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
                        'as-cache': {
                            'type': 'integer',
                            'default': 300,
                            'example': 300
                        },
                        'as-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'nospam',
                                'all'
                            ]
                        },
                        'as-preload': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'av-cache': {
                            'type': 'integer',
                            'default': 300,
                            'example': 300
                        },
                        'av-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'novirus',
                                'all'
                            ]
                        },
                        'av-preload': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'av2-cache': {
                            'type': 'integer',
                            'default': 800,
                            'example': 800
                        },
                        'av2-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'noav2',
                                'all'
                            ]
                        },
                        'av2-preload': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'eventlog-query': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fgd-pull-interval': {
                            'type': 'integer',
                            'default': 10,
                            'example': 10
                        },
                        'fq-cache': {
                            'type': 'integer',
                            'default': 300,
                            'example': 300
                        },
                        'fq-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'nofilequery',
                                'all'
                            ]
                        },
                        'fq-preload': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'linkd-log': {
                            'type': 'string',
                            'enum': [
                                'emergency',
                                'alert',
                                'critical',
                                'error',
                                'warn',
                                'notice',
                                'info',
                                'debug',
                                'disable'
                            ]
                        },
                        'max-client-worker': {
                            'type': 'integer',
                            'default': 0,
                            'example': 0
                        },
                        'max-log-quota': {
                            'type': 'integer',
                            'default': 6144,
                            'example': 6144
                        },
                        'max-unrated-site': {
                            'type': 'integer',
                            'default': 500,
                            'example': 500
                        },
                        'restrict-as1-dbver': {
                            'type': 'string'
                        },
                        'restrict-as2-dbver': {
                            'type': 'string'
                        },
                        'restrict-as4-dbver': {
                            'type': 'string'
                        },
                        'restrict-av-dbver': {
                            'type': 'string'
                        },
                        'restrict-av2-dbver': {
                            'type': 'string'
                        },
                        'restrict-fq-dbver': {
                            'type': 'string'
                        },
                        'restrict-wf-dbver': {
                            'type': 'string'
                        },
                        'server-override': {
                            'servlist': {
                                'type': 'array',
                                'items': {
                                    'id': {
                                        'type': 'integer',
                                        'default': 0,
                                        'example': 0
                                    },
                                    'ip': {
                                        'type': 'string'
                                    },
                                    'ip6': {
                                        'type': 'string'
                                    },
                                    'port': {
                                        'type': 'integer',
                                        'default': 443,
                                        'example': 443
                                    },
                                    'service-type': {
                                        'type': 'array',
                                        'items': {
                                            'type': 'string',
                                            'enum': [
                                                'fgd',
                                                'fgc',
                                                'fsa'
                                            ]
                                        }
                                    }
                                }
                            },
                            'status': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            }
                        },
                        'stat-log-interval': {
                            'type': 'integer',
                            'default': 60,
                            'example': 60
                        },
                        'stat-sync-interval': {
                            'type': 'integer',
                            'default': 60,
                            'example': 60
                        },
                        'update-interval': {
                            'type': 'integer',
                            'default': 6,
                            'example': 6
                        },
                        'update-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'wf-cache': {
                            'type': 'integer',
                            'default': 0,
                            'example': 0
                        },
                        'wf-dn-cache-expire-time': {
                            'type': 'integer',
                            'default': 30,
                            'example': 30
                        },
                        'wf-dn-cache-max-number': {
                            'type': 'integer',
                            'default': 10000,
                            'example': 10000
                        },
                        'wf-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'nourl',
                                'all'
                            ]
                        },
                        'wf-preload': {
                            'type': 'string',
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
