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
module: fmgr_cli_fmupdate_fds_setting
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis:
    - /cli/global/fmupdate/fds-setting
    - Examples include all parameters and values need to be adjusted to data 
      sources before usage.
     

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
        description: 'Configure FortiGuard settings.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Configure FortiGuard settings.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                User-Agent:
                    type: str
                    default: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)
                    description: 'Configure the user agent string.'
                fds-clt-ssl-protocol:
                    type: str
                    default: tlsv1.2
                    description:
                     - 'The SSL protocols version for connecting fds server (default = tlsv1.2).'
                     - 'sslv3 - set SSLv3 as the client version.'
                     - 'tlsv1.0 - set TLSv1.0 as the client version.'
                     - 'tlsv1.1 - set TLSv1.1 as the client version.'
                     - 'tlsv1.2 - set TLSv1.2 as the client version (default).'
                    choices:
                        - sslv3
                        - tlsv1.0
                        - tlsv1.1
                        - tlsv1.2
                fds-ssl-protocol:
                    type: str
                    default: tlsv1.2
                    description:
                     - 'The SSL protocols version for receiving fgt connection (default = tlsv1.2).'
                     - 'sslv3 - set SSLv3 as the lowest version.'
                     - 'tlsv1.0 - set TLSv1.0 as the lowest version.'
                     - 'tlsv1.1 - set TLSv1.1 as the lowest version.'
                     - 'tlsv1.2 - set TLSv1.2 as the lowest version (default).'
                    choices:
                        - sslv3
                        - tlsv1.0
                        - tlsv1.1
                        - tlsv1.2
                fmtr-log:
                    type: str
                    default: info
                    description:
                     - 'fmtr log level'
                     - 'emergency - Log level - emergency'
                     - 'alert - Log level - alert'
                     - 'critical - Log level - critical'
                     - 'error - Log level - error'
                     - 'warn - Log level - warn'
                     - 'notice - Log level - notice'
                     - 'info - Log level - info'
                     - 'debug - Log level - debug'
                     - 'disable - Disable linkd log'
                    choices:
                        - emergency
                        - alert
                        - critical
                        - error
                        - warn
                        - notice
                        - info
                        - debug
                        - disable
                linkd-log:
                    type: str
                    default: info
                    description:
                     - 'The linkd log level (default = info).'
                     - 'emergency - Log level - emergency'
                     - 'alert - Log level - alert'
                     - 'critical - Log level - critical'
                     - 'error - Log level - error'
                     - 'warn - Log level - warn'
                     - 'notice - Log level - notice'
                     - 'info - Log level - info'
                     - 'debug - Log level - debug'
                     - 'disable - Disable linkd log'
                    choices:
                        - emergency
                        - alert
                        - critical
                        - error
                        - warn
                        - notice
                        - info
                        - debug
                        - disable
                max-av-ips-version:
                    type: int
                    default: 20
                    description: 'The maximum number of downloadable, full version AV/IPS packages (1 - 1000, default = 20).'
                max-work:
                    type: int
                    default: 1
                    description: 'The maximum number of worker processing download requests (1 - 32, default = 1).'
                push-override:
                    ip:
                        type: str
                        default: 0.0.0.0
                        description: 'External or virtual IP address of the NAT device that will forward push messages to the FortiManager unit.'
                    port:
                        type: int
                        default: 9443
                        description: 'Receiving port number on the NAT device (1 - 65535, default = 9443).'
                    status:
                        type: str
                        default: disable
                        description:
                         - 'Enable/disable push updates for clients (default = disable).'
                         - 'disable - Disable setting.'
                         - 'enable - Enable setting.'
                        choices:
                            - disable
                            - enable
                push-override-to-client:
                    announce-ip:
                        -
                            id:
                                type: int
                                default: 0
                                description: 'ID of the announce IP address (1 - 10).'
                            ip:
                                type: str
                                default: 0.0.0.0
                                description: 'Announce IPv4 address.'
                            port:
                                type: int
                                default: 8890
                                description: 'Announce IP port (1 - 65535, default = 8890).'
                    status:
                        type: str
                        default: disable
                        description:
                         - 'Enable/disable push updates (default = disable).'
                         - 'disable - Disable setting.'
                         - 'enable - Enable setting.'
                        choices:
                            - disable
                            - enable
                send_report:
                    type: str
                    default: enable
                    description:
                     - 'send report/fssi to fds server.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - disable
                        - enable
                send_setup:
                    type: str
                    default: disable
                    description:
                     - 'forward setup to fds server.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - disable
                        - enable
                server-override:
                    servlist:
                        -
                            id:
                                type: int
                                default: 0
                                description: 'Override server ID (1 - 10).'
                            ip:
                                type: str
                                default: 0.0.0.0
                                description: 'IPv4 address of the override server.'
                            ip6:
                                type: str
                                default: ::
                                description: 'IPv6 address of the override server.'
                            port:
                                type: int
                                default: 443
                                description: 'Port number to use when contacting FortiGuard (1 - 65535, default = 443).'
                            service-type:
                                -
                                    type: str
                                    choices:
                                        - fds
                                        - fct
                    status:
                        type: str
                        default: disable
                        description:
                         - 'Override status.'
                         - 'disable - Disable setting.'
                         - 'enable - Enable setting.'
                        choices:
                            - disable
                            - enable
                system-support-fct:
                    -
                        type: str
                        choices:
                            - 4.x
                            - 5.0
                            - 5.2
                            - 5.4
                            - 5.6
                            - 6.0
                system-support-fgt:
                    -
                        type: str
                        choices:
                            - 5.4
                            - 5.6
                            - 6.0
                            - 6.2
                system-support-fml:
                    -
                        type: str
                        choices:
                            - 4.x
                            - 5.x
                            - 6.x
                system-support-fsa:
                    -
                        type: str
                        choices:
                            - 1.x
                            - 2.x
                            - 3.x
                system-support-fsw:
                    -
                        type: str
                        choices:
                            - 5.4
                            - 5.6
                            - 6.0
                            - 6.2
                umsvc-log:
                    type: str
                    default: info
                    description:
                     - 'The um_service log level (default = info).'
                     - 'emergency - Log level - emergency'
                     - 'alert - Log level - alert'
                     - 'critical - Log level - critical'
                     - 'error - Log level - error'
                     - 'warn - Log level - warn'
                     - 'notice - Log level - notice'
                     - 'info - Log level - info'
                     - 'debug - Log level - debug'
                     - 'disable - Disable linkd log'
                    choices:
                        - emergency
                        - alert
                        - critical
                        - error
                        - warn
                        - notice
                        - info
                        - debug
                        - disable
                unreg-dev-option:
                    type: str
                    default: add-service
                    description:
                     - 'set the option for unregister devices'
                     - 'ignore - Ignore all unregistered devices.'
                     - 'svc-only - Allow update requests without adding the device.'
                     - 'add-service - Add unregistered devices and allow update request.'
                    choices:
                        - ignore
                        - svc-only
                        - add-service
                update-schedule:
                    day:
                        type: str
                        default: Monday
                        description:
                         - 'Configure the day the update will occur, if the freqnecy is weekly (Sunday - Saturday, default = Monday).'
                         - 'Sunday - Update every Sunday.'
                         - 'Monday - Update every Monday.'
                         - 'Tuesday - Update every Tuesday.'
                         - 'Wednesday - Update every Wednesday.'
                         - 'Thursday - Update every Thursday.'
                         - 'Friday - Update every Friday.'
                         - 'Saturday - Update every Saturday.'
                        choices:
                            - Sunday
                            - Monday
                            - Tuesday
                            - Wednesday
                            - Thursday
                            - Friday
                            - Saturday
                    frequency:
                        type: str
                        default: every
                        description:
                         - 'Configure update frequency: every - time interval, daily - once a day, weekly - once a week (default = every).'
                         - 'every - Time interval.'
                         - 'daily - Every day.'
                         - 'weekly - Every week.'
                        choices:
                            - every
                            - daily
                            - weekly
                    status:
                        type: str
                        default: enable
                        description:
                         - 'Enable/disable scheduled updates.'
                         - 'disable - Disable setting.'
                         - 'enable - Enable setting.'
                        choices:
                            - disable
                            - enable
                    time:
                        -
                            type: str
                wanip-query-mode:
                    type: str
                    default: disable
                    description:
                     - 'public ip query mode'
                     - 'disable - Do not query public ip'
                     - 'ipify - Get public IP through https://api.ipify.org'
                    choices:
                        - disable
                        - ipify

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /cli/fmupdate/fds-setting
      fmgr_cli_fmupdate_fds_setting:
         method: <value in [set, update]>
         params:
            - 
               data: 
                  User-Agent: <value of string default: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)>
                  fds-clt-ssl-protocol: <value in [sslv3, tlsv1.0, tlsv1.1, ...] default: tlsv1.2>
                  fds-ssl-protocol: <value in [sslv3, tlsv1.0, tlsv1.1, ...] default: tlsv1.2>
                  fmtr-log: <value in [emergency, alert, critical, ...] default: info>
                  linkd-log: <value in [emergency, alert, critical, ...] default: info>
                  max-av-ips-version: <value of integer default: 20>
                  max-work: <value of integer default: 1>
                  push-override: 
                     ip: <value of string default: 0.0.0.0>
                     port: <value of integer default: 9443>
                     status: <value in [disable, enable] default: disable>
                  push-override-to-client: 
                     announce-ip: 
                      - 
                           id: <value of integer default: 0>
                           ip: <value of string default: 0.0.0.0>
                           port: <value of integer default: 8890>
                     status: <value in [disable, enable] default: disable>
                  send_report: <value in [disable, enable] default: enable>
                  send_setup: <value in [disable, enable] default: disable>
                  server-override: 
                     servlist: 
                      - 
                           id: <value of integer default: 0>
                           ip: <value of string default: 0.0.0.0>
                           ip6: <value of string default: ::>
                           port: <value of integer default: 443>
                           service-type: 
                            - <value in [fds, fct]>
                     status: <value in [disable, enable] default: disable>
                  system-support-fct: 
                   - <value in [4.x, 5.0, 5.2, ...]>
                  system-support-fgt: 
                   - <value in [5.4, 5.6, 6.0, ...]>
                  system-support-fml: 
                   - <value in [4.x, 5.x, 6.x]>
                  system-support-fsa: 
                   - <value in [1.x, 2.x, 3.x]>
                  system-support-fsw: 
                   - <value in [5.4, 5.6, 6.0, ...]>
                  umsvc-log: <value in [emergency, alert, critical, ...] default: info>
                  unreg-dev-option: <value in [ignore, svc-only, add-service] default: add-service>
                  update-schedule: 
                     day: <value in [Sunday, Monday, Tuesday, ...] default: Monday>
                     frequency: <value in [every, daily, weekly] default: every>
                     status: <value in [disable, enable] default: enable>
                     time: 
                      - <value of string>
                  wanip-query-mode: <value in [disable, ipify] default: disable>

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
            User-Agent:
               type: str
               description: 'Configure the user agent string.'
               example: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)
            fds-clt-ssl-protocol:
               type: str
               description: |
                  'The SSL protocols version for connecting fds server (default = tlsv1.2).'
                  'sslv3 - set SSLv3 as the client version.'
                  'tlsv1.0 - set TLSv1.0 as the client version.'
                  'tlsv1.1 - set TLSv1.1 as the client version.'
                  'tlsv1.2 - set TLSv1.2 as the client version (default).'
               example: tlsv1.2
            fds-ssl-protocol:
               type: str
               description: |
                  'The SSL protocols version for receiving fgt connection (default = tlsv1.2).'
                  'sslv3 - set SSLv3 as the lowest version.'
                  'tlsv1.0 - set TLSv1.0 as the lowest version.'
                  'tlsv1.1 - set TLSv1.1 as the lowest version.'
                  'tlsv1.2 - set TLSv1.2 as the lowest version (default).'
               example: tlsv1.2
            fmtr-log:
               type: str
               description: |
                  'fmtr log level'
                  'emergency - Log level - emergency'
                  'alert - Log level - alert'
                  'critical - Log level - critical'
                  'error - Log level - error'
                  'warn - Log level - warn'
                  'notice - Log level - notice'
                  'info - Log level - info'
                  'debug - Log level - debug'
                  'disable - Disable linkd log'
               example: info
            linkd-log:
               type: str
               description: |
                  'The linkd log level (default = info).'
                  'emergency - Log level - emergency'
                  'alert - Log level - alert'
                  'critical - Log level - critical'
                  'error - Log level - error'
                  'warn - Log level - warn'
                  'notice - Log level - notice'
                  'info - Log level - info'
                  'debug - Log level - debug'
                  'disable - Disable linkd log'
               example: info
            max-av-ips-version:
               type: int
               description: 'The maximum number of downloadable, full version AV/IPS packages (1 - 1000, default = 20).'
               example: 20
            max-work:
               type: int
               description: 'The maximum number of worker processing download requests (1 - 32, default = 1).'
               example: 1
            push-override:
               ip:
                  type: str
                  description: 'External or virtual IP address of the NAT device that will forward push messages to the FortiManager unit.'
                  example: 0.0.0.0
               port:
                  type: int
                  description: 'Receiving port number on the NAT device (1 - 65535, default = 9443).'
                  example: 9443
               status:
                  type: str
                  description: |
                     'Enable/disable push updates for clients (default = disable).'
                     'disable - Disable setting.'
                     'enable - Enable setting.'
                  example: disable
            push-override-to-client:
               announce-ip:
                  type: array
                  suboptions:
                     id:
                        type: int
                        description: 'ID of the announce IP address (1 - 10).'
                        example: 0
                     ip:
                        type: str
                        description: 'Announce IPv4 address.'
                        example: 0.0.0.0
                     port:
                        type: int
                        description: 'Announce IP port (1 - 65535, default = 8890).'
                        example: 8890
               status:
                  type: str
                  description: |
                     'Enable/disable push updates (default = disable).'
                     'disable - Disable setting.'
                     'enable - Enable setting.'
                  example: disable
            send_report:
               type: str
               description: |
                  'send report/fssi to fds server.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: enable
            send_setup:
               type: str
               description: |
                  'forward setup to fds server.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: disable
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
                        example: 0.0.0.0
                     ip6:
                        type: str
                        description: 'IPv6 address of the override server.'
                        example: ::
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
                  example: disable
            system-support-fct:
               type: array
               suboptions:
                  type: str
            system-support-fgt:
               type: array
               suboptions:
                  type: str
            system-support-fml:
               type: array
               suboptions:
                  type: str
            system-support-fsa:
               type: array
               suboptions:
                  type: str
            system-support-fsw:
               type: array
               suboptions:
                  type: str
            umsvc-log:
               type: str
               description: |
                  'The um_service log level (default = info).'
                  'emergency - Log level - emergency'
                  'alert - Log level - alert'
                  'critical - Log level - critical'
                  'error - Log level - error'
                  'warn - Log level - warn'
                  'notice - Log level - notice'
                  'info - Log level - info'
                  'debug - Log level - debug'
                  'disable - Disable linkd log'
               example: info
            unreg-dev-option:
               type: str
               description: |
                  'set the option for unregister devices'
                  'ignore - Ignore all unregistered devices.'
                  'svc-only - Allow update requests without adding the device.'
                  'add-service - Add unregistered devices and allow update request.'
               example: add-service
            update-schedule:
               day:
                  type: str
                  description: |
                     'Configure the day the update will occur, if the freqnecy is weekly (Sunday - Saturday, default = Monday).'
                     'Sunday - Update every Sunday.'
                     'Monday - Update every Monday.'
                     'Tuesday - Update every Tuesday.'
                     'Wednesday - Update every Wednesday.'
                     'Thursday - Update every Thursday.'
                     'Friday - Update every Friday.'
                     'Saturday - Update every Saturday.'
                  example: Monday
               frequency:
                  type: str
                  description: |
                     'Configure update frequency: every - time interval, daily - once a day, weekly - once a week (default = every).'
                     'every - Time interval.'
                     'daily - Every day.'
                     'weekly - Every week.'
                  example: every
               status:
                  type: str
                  description: |
                     'Enable/disable scheduled updates.'
                     'disable - Disable setting.'
                     'enable - Enable setting.'
                  example: enable
               time:
                  type: array
                  suboptions:
                     type: str
            wanip-query-mode:
               type: str
               description: |
                  'public ip query mode'
                  'disable - Do not query public ip'
                  'ipify - Get public IP through https://api.ipify.org'
               example: disable
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /cli/global/fmupdate/fds-setting
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
            example: /cli/global/fmupdate/fds-setting

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
        '/cli/global/fmupdate/fds-setting'
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
                        'User-Agent': {
                            'type': 'string',
                            'default': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'
                        },
                        'fds-clt-ssl-protocol': {
                            'type': 'string',
                            'default': 'tlsv1.2',
                            'enum': [
                                'sslv3',
                                'tlsv1.0',
                                'tlsv1.1',
                                'tlsv1.2'
                            ]
                        },
                        'fds-ssl-protocol': {
                            'type': 'string',
                            'default': 'tlsv1.2',
                            'enum': [
                                'sslv3',
                                'tlsv1.0',
                                'tlsv1.1',
                                'tlsv1.2'
                            ]
                        },
                        'fmtr-log': {
                            'type': 'string',
                            'default': 'info',
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
                        'linkd-log': {
                            'type': 'string',
                            'default': 'info',
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
                        'max-av-ips-version': {
                            'type': 'integer',
                            'default': 20,
                            'example': 20
                        },
                        'max-work': {
                            'type': 'integer',
                            'default': 1,
                            'example': 1
                        },
                        'push-override': {
                            'ip': {
                                'type': 'string',
                                'default': '0.0.0.0'
                            },
                            'port': {
                                'type': 'integer',
                                'default': 9443,
                                'example': 9443
                            },
                            'status': {
                                'type': 'string',
                                'default': 'disable',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            }
                        },
                        'push-override-to-client': {
                            'announce-ip': {
                                'type': 'array',
                                'items': {
                                    'id': {
                                        'type': 'integer',
                                        'default': 0,
                                        'example': 0
                                    },
                                    'ip': {
                                        'type': 'string',
                                        'default': '0.0.0.0'
                                    },
                                    'port': {
                                        'type': 'integer',
                                        'default': 8890,
                                        'example': 8890
                                    }
                                }
                            },
                            'status': {
                                'type': 'string',
                                'default': 'disable',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            }
                        },
                        'send_report': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'send_setup': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
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
                                        'type': 'string',
                                        'default': '0.0.0.0'
                                    },
                                    'ip6': {
                                        'type': 'string',
                                        'default': '::'
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
                                                'fds',
                                                'fct'
                                            ]
                                        }
                                    }
                                }
                            },
                            'status': {
                                'type': 'string',
                                'default': 'disable',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            }
                        },
                        'system-support-fct': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    '4.x',
                                    '5.0',
                                    '5.2',
                                    '5.4',
                                    '5.6',
                                    '6.0'
                                ]
                            }
                        },
                        'system-support-fgt': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    '5.4',
                                    '5.6',
                                    '6.0',
                                    '6.2'
                                ]
                            }
                        },
                        'system-support-fml': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    '4.x',
                                    '5.x',
                                    '6.x'
                                ]
                            }
                        },
                        'system-support-fsa': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    '1.x',
                                    '2.x',
                                    '3.x'
                                ]
                            }
                        },
                        'system-support-fsw': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    '5.4',
                                    '5.6',
                                    '6.0',
                                    '6.2'
                                ]
                            }
                        },
                        'umsvc-log': {
                            'type': 'string',
                            'default': 'info',
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
                        'unreg-dev-option': {
                            'type': 'string',
                            'default': 'add-service',
                            'enum': [
                                'ignore',
                                'svc-only',
                                'add-service'
                            ]
                        },
                        'update-schedule': {
                            'day': {
                                'type': 'string',
                                'default': 'Monday',
                                'enum': [
                                    'Sunday',
                                    'Monday',
                                    'Tuesday',
                                    'Wednesday',
                                    'Thursday',
                                    'Friday',
                                    'Saturday'
                                ]
                            },
                            'frequency': {
                                'type': 'string',
                                'default': 'every',
                                'enum': [
                                    'every',
                                    'daily',
                                    'weekly'
                                ]
                            },
                            'status': {
                                'type': 'string',
                                'default': 'enable',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'time': {
                                'type': 'array',
                                'items': {
                                    'type': 'string'
                                }
                            }
                        },
                        'wanip-query-mode': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'ipify'
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