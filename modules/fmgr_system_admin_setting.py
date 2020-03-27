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
module: fmgr_system_admin_setting
short_description: Admin setting.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /cli/global/system/admin/setting
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
        description: 'Admin setting.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Admin setting.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                access-banner:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable access banner.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                admin-https-redirect:
                    type: str
                    default: 'enable'
                    description:
                     - 'Enable/disable redirection of HTTP admin traffic to HTTPS.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                admin-login-max:
                    type: int
                    default: 256
                    description: 'Maximum number admin users logged in at one time (1 - 256).'
                admin_server_cert:
                    type: str
                    default: 'server.crt'
                    description: 'HTTPS & Web Service server certificate.'
                allow_register:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable allowance of register an unregistered device.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                auto-update:
                    type: str
                    default: 'enable'
                    description:
                     - 'Enable/disable FortiGate automatic update.'
                     - 'disable - Disable device automatic update.'
                     - 'enable - Enable device automatic update.'
                    choices:
                        - 'disable'
                        - 'enable'
                banner-message:
                    type: str
                    description: 'Banner message.'
                chassis-mgmt:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable or disable chassis management.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                chassis-update-interval:
                    type: int
                    default: 15
                    description: 'Chassis background update interval (4 - 1440 mins).'
                device_sync_status:
                    type: str
                    default: 'enable'
                    description:
                     - 'Enable/disable device synchronization status indication.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                gui-theme:
                    type: str
                    default: 'blue'
                    description:
                     - 'Color scheme to use for the administration GUI.'
                     - 'blue - Blueberry'
                     - 'green - Kiwi'
                     - 'red - Cherry'
                     - 'melongene - Plum'
                     - 'spring - Spring'
                     - 'summer - Summer'
                     - 'autumn - Autumn'
                     - 'winter - Winter'
                     - 'space - Space'
                     - 'calla-lily - Calla Lily'
                     - 'binary-tunnel - Binary Tunnel'
                     - 'diving - Diving'
                     - 'dreamy - Dreamy'
                     - 'technology - Technology'
                     - 'landscape - Landscape'
                     - 'twilight - Twilight'
                     - 'canyon - Canyon'
                     - 'northern-light - Northern Light'
                     - 'astronomy - Astronomy'
                     - 'fish - Fish'
                     - 'penguin - Penguin'
                     - 'panda - Panda'
                     - 'polar-bear - Polar Bear'
                     - 'parrot - Parrot'
                     - 'cave - Cave'
                    choices:
                        - 'blue'
                        - 'green'
                        - 'red'
                        - 'melongene'
                        - 'spring'
                        - 'summer'
                        - 'autumn'
                        - 'winter'
                        - 'space'
                        - 'calla-lily'
                        - 'binary-tunnel'
                        - 'diving'
                        - 'dreamy'
                        - 'technology'
                        - 'landscape'
                        - 'twilight'
                        - 'canyon'
                        - 'northern-light'
                        - 'astronomy'
                        - 'fish'
                        - 'penguin'
                        - 'panda'
                        - 'polar-bear'
                        - 'parrot'
                        - 'cave'
                http_port:
                    type: int
                    default: 80
                    description: 'HTTP port.'
                https_port:
                    type: int
                    default: 443
                    description: 'HTTPS port.'
                idle_timeout:
                    type: int
                    default: 15
                    description: 'Idle timeout (1 - 480 min).'
                install-ifpolicy-only:
                    type: str
                    default: 'disable'
                    description:
                     - 'Allow install interface policy only.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                mgmt-addr:
                    type: str
                    description: 'IP of FortiManager used by FGFM.'
                mgmt-fqdn:
                    type: str
                    description: 'FQDN of FortiManager used by FGFM.'
                objects-force-deletion:
                    type: str
                    default: 'enable'
                    description:
                     - 'Enable/disable used objects force deletion.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                offline_mode:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable offline mode.'
                     - 'disable - Disable offline mode.'
                     - 'enable - Enable offline mode.'
                    choices:
                        - 'disable'
                        - 'enable'
                register_passwd:
                    -
                        type: str
                        default: 'ENC ODA4MzI1MDExMjE4OTgxM/oYbnw5dOwHjdVIoziGMGql3I0Ddz+ewZZfbXj7YeX4ol/rqZveNL7pJsXB6fGh0Bfo+R+211AvBe4558gduEIjb2W9ApZLt...'
                sdwan-monitor-history:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable hostname display in the GUI login page.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                shell-access:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable shell access.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                shell-password:
                    -
                        type: str
                        default: 'ENC NDM0ODk3MTk5MDUyMTEzMUbHl/j5CmTEcBmvdfBvKn99O6PWsq0PdmnxFXT9hypS7GvefFaz0oVwvAJ5/jgxY3HaLJDNTuNDNZfGQBezH6DURHCF23i/U...'
                show-add-multiple:
                    type: str
                    default: 'disable'
                    description:
                     - 'Show add multiple button.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                show-adom-devman:
                    type: str
                    default: 'enable'
                    description:
                     - 'Show ADOM device manager tools on GUI.'
                     - 'disable - Hide device manager tools on GUI.'
                     - 'enable - Show device manager tools on GUI.'
                    choices:
                        - 'disable'
                        - 'enable'
                show-checkbox-in-table:
                    type: str
                    default: 'disable'
                    description:
                     - 'Show checkboxs in tables on GUI.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                show-device-import-export:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable import/export of ADOM, device, and group lists.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                show-hostname:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable hostname display in the GUI login page.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                show_automatic_script:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable automatic script.'
                     - 'disable - Disable script option.'
                     - 'enable - Enable script option.'
                    choices:
                        - 'disable'
                        - 'enable'
                show_grouping_script:
                    type: str
                    default: 'enable'
                    description:
                     - 'Enable/disable grouping script.'
                     - 'disable - Disable script option.'
                     - 'enable - Enable script option.'
                    choices:
                        - 'disable'
                        - 'enable'
                show_schedule_script:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable or disable schedule script.'
                     - 'disable - Disable script option.'
                     - 'enable - Enable script option.'
                    choices:
                        - 'disable'
                        - 'enable'
                show_tcl_script:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable TCL script.'
                     - 'disable - Disable script option.'
                     - 'enable - Enable script option.'
                    choices:
                        - 'disable'
                        - 'enable'
                unreg_dev_opt:
                    type: str
                    default: 'add_allow_service'
                    description:
                     - 'Action to take when unregistered device connects to FortiManager.'
                     - 'add_no_service - Add unregistered devices but deny service requests.'
                     - 'ignore - Ignore unregistered devices.'
                     - 'add_allow_service - Add unregistered devices and allow service requests.'
                    choices:
                        - 'add_no_service'
                        - 'ignore'
                        - 'add_allow_service'
                webadmin_language:
                    type: str
                    default: 'auto_detect'
                    description:
                     - 'Web admin language.'
                     - 'auto_detect - Automatically detect language.'
                     - 'english - English.'
                     - 'simplified_chinese - Simplified Chinese.'
                     - 'traditional_chinese - Traditional Chinese.'
                     - 'japanese - Japanese.'
                     - 'korean - Korean.'
                     - 'spanish - Spanish.'
                    choices:
                        - 'auto_detect'
                        - 'english'
                        - 'simplified_chinese'
                        - 'traditional_chinese'
                        - 'japanese'
                        - 'korean'
                        - 'spanish'

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

    - name: REQUESTING /CLI/SYSTEM/ADMIN/SETTING
      fmgr_system_admin_setting:
         method: <value in [set, update]>
         params:
            -
               data:
                  access-banner: <value in [disable, enable] default: 'disable'>
                  admin-https-redirect: <value in [disable, enable] default: 'enable'>
                  admin-login-max: <value of integer default: 256>
                  admin_server_cert: <value of string default: 'server.crt'>
                  allow_register: <value in [disable, enable] default: 'disable'>
                  auto-update: <value in [disable, enable] default: 'enable'>
                  banner-message: <value of string>
                  chassis-mgmt: <value in [disable, enable] default: 'disable'>
                  chassis-update-interval: <value of integer default: 15>
                  device_sync_status: <value in [disable, enable] default: 'enable'>
                  gui-theme: <value in [blue, green, red, ...] default: 'blue'>
                  http_port: <value of integer default: 80>
                  https_port: <value of integer default: 443>
                  idle_timeout: <value of integer default: 15>
                  install-ifpolicy-only: <value in [disable, enable] default: 'disable'>
                  mgmt-addr: <value of string>
                  mgmt-fqdn: <value of string>
                  objects-force-deletion: <value in [disable, enable] default: 'enable'>
                  offline_mode: <value in [disable, enable] default: 'disable'>
                  register_passwd:
                    - <value of string default: 'ENC ODA4MzI1MDExMjE4OTgxM/oYbnw5dOwHjdVIoziGMGql3I0Ddz+ewZZfbXj7YeX4ol/rqZve...'>
                  sdwan-monitor-history: <value in [disable, enable] default: 'disable'>
                  shell-access: <value in [disable, enable] default: 'disable'>
                  shell-password:
                    - <value of string default: 'ENC NDM0ODk3MTk5MDUyMTEzMUbHl/j5CmTEcBmvdfBvKn99O6PWsq0PdmnxFXT9hypS7GvefFaz...'>
                  show-add-multiple: <value in [disable, enable] default: 'disable'>
                  show-adom-devman: <value in [disable, enable] default: 'enable'>
                  show-checkbox-in-table: <value in [disable, enable] default: 'disable'>
                  show-device-import-export: <value in [disable, enable] default: 'disable'>
                  show-hostname: <value in [disable, enable] default: 'disable'>
                  show_automatic_script: <value in [disable, enable] default: 'disable'>
                  show_grouping_script: <value in [disable, enable] default: 'enable'>
                  show_schedule_script: <value in [disable, enable] default: 'disable'>
                  show_tcl_script: <value in [disable, enable] default: 'disable'>
                  unreg_dev_opt: <value in [add_no_service, ignore, add_allow_service] default: 'add_allow_service'>
                  webadmin_language: <value in [auto_detect, english, simplified_chinese, ...] default: 'auto_detect'>

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
            access-banner:
               type: str
               description: |
                  'Enable/disable access banner.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'disable'
            admin-https-redirect:
               type: str
               description: |
                  'Enable/disable redirection of HTTP admin traffic to HTTPS.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'enable'
            admin-login-max:
               type: int
               description: 'Maximum number admin users logged in at one time (1 - 256).'
               example: 256
            admin_server_cert:
               type: str
               description: 'HTTPS & Web Service server certificate.'
               example: 'server.crt'
            allow_register:
               type: str
               description: |
                  'Enable/disable allowance of register an unregistered device.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'disable'
            auto-update:
               type: str
               description: |
                  'Enable/disable FortiGate automatic update.'
                  'disable - Disable device automatic update.'
                  'enable - Enable device automatic update.'
               example: 'enable'
            banner-message:
               type: str
               description: 'Banner message.'
            chassis-mgmt:
               type: str
               description: |
                  'Enable or disable chassis management.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'disable'
            chassis-update-interval:
               type: int
               description: 'Chassis background update interval (4 - 1440 mins).'
               example: 15
            device_sync_status:
               type: str
               description: |
                  'Enable/disable device synchronization status indication.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'enable'
            gui-theme:
               type: str
               description: |
                  'Color scheme to use for the administration GUI.'
                  'blue - Blueberry'
                  'green - Kiwi'
                  'red - Cherry'
                  'melongene - Plum'
                  'spring - Spring'
                  'summer - Summer'
                  'autumn - Autumn'
                  'winter - Winter'
                  'space - Space'
                  'calla-lily - Calla Lily'
                  'binary-tunnel - Binary Tunnel'
                  'diving - Diving'
                  'dreamy - Dreamy'
                  'technology - Technology'
                  'landscape - Landscape'
                  'twilight - Twilight'
                  'canyon - Canyon'
                  'northern-light - Northern Light'
                  'astronomy - Astronomy'
                  'fish - Fish'
                  'penguin - Penguin'
                  'panda - Panda'
                  'polar-bear - Polar Bear'
                  'parrot - Parrot'
                  'cave - Cave'
               example: 'blue'
            http_port:
               type: int
               description: 'HTTP port.'
               example: 80
            https_port:
               type: int
               description: 'HTTPS port.'
               example: 443
            idle_timeout:
               type: int
               description: 'Idle timeout (1 - 480 min).'
               example: 15
            install-ifpolicy-only:
               type: str
               description: |
                  'Allow install interface policy only.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'disable'
            mgmt-addr:
               type: str
               description: 'IP of FortiManager used by FGFM.'
            mgmt-fqdn:
               type: str
               description: 'FQDN of FortiManager used by FGFM.'
            objects-force-deletion:
               type: str
               description: |
                  'Enable/disable used objects force deletion.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'enable'
            offline_mode:
               type: str
               description: |
                  'Enable/disable offline mode.'
                  'disable - Disable offline mode.'
                  'enable - Enable offline mode.'
               example: 'disable'
            register_passwd:
               type: array
               suboptions:
                  type: str
                  example: 'ENC ODA4MzI1MDExMjE4OTgxM/oYbnw5dOwHjdVIoziGMGql3I0Ddz+ewZZfbXj7YeX4ol/rqZve...'
            sdwan-monitor-history:
               type: str
               description: |
                  'Enable/disable hostname display in the GUI login page.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'disable'
            shell-access:
               type: str
               description: |
                  'Enable/disable shell access.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'disable'
            shell-password:
               type: array
               suboptions:
                  type: str
                  example: 'ENC NDM0ODk3MTk5MDUyMTEzMUbHl/j5CmTEcBmvdfBvKn99O6PWsq0PdmnxFXT9hypS7GvefFaz...'
            show-add-multiple:
               type: str
               description: |
                  'Show add multiple button.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'disable'
            show-adom-devman:
               type: str
               description: |
                  'Show ADOM device manager tools on GUI.'
                  'disable - Hide device manager tools on GUI.'
                  'enable - Show device manager tools on GUI.'
               example: 'enable'
            show-checkbox-in-table:
               type: str
               description: |
                  'Show checkboxs in tables on GUI.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'disable'
            show-device-import-export:
               type: str
               description: |
                  'Enable/disable import/export of ADOM, device, and group lists.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'disable'
            show-hostname:
               type: str
               description: |
                  'Enable/disable hostname display in the GUI login page.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'disable'
            show_automatic_script:
               type: str
               description: |
                  'Enable/disable automatic script.'
                  'disable - Disable script option.'
                  'enable - Enable script option.'
               example: 'disable'
            show_grouping_script:
               type: str
               description: |
                  'Enable/disable grouping script.'
                  'disable - Disable script option.'
                  'enable - Enable script option.'
               example: 'enable'
            show_schedule_script:
               type: str
               description: |
                  'Enable or disable schedule script.'
                  'disable - Disable script option.'
                  'enable - Enable script option.'
               example: 'disable'
            show_tcl_script:
               type: str
               description: |
                  'Enable/disable TCL script.'
                  'disable - Disable script option.'
                  'enable - Enable script option.'
               example: 'disable'
            unreg_dev_opt:
               type: str
               description: |
                  'Action to take when unregistered device connects to FortiManager.'
                  'add_no_service - Add unregistered devices but deny service requests.'
                  'ignore - Ignore unregistered devices.'
                  'add_allow_service - Add unregistered devices and allow service requests.'
               example: 'add_allow_service'
            webadmin_language:
               type: str
               description: |
                  'Web admin language.'
                  'auto_detect - Automatically detect language.'
                  'english - English.'
                  'simplified_chinese - Simplified Chinese.'
                  'traditional_chinese - Traditional Chinese.'
                  'japanese - Japanese.'
                  'korean - Korean.'
                  'spanish - Spanish.'
               example: 'auto_detect'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/cli/global/system/admin/setting'
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
            example: '/cli/global/system/admin/setting'

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
        '/cli/global/system/admin/setting'
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
                        'access-banner': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'admin-https-redirect': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'admin-login-max': {
                            'type': 'integer',
                            'default': 256,
                            'example': 256
                        },
                        'admin_server_cert': {
                            'type': 'string'
                        },
                        'allow_register': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'auto-update': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'banner-message': {
                            'type': 'string'
                        },
                        'chassis-mgmt': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'chassis-update-interval': {
                            'type': 'integer',
                            'default': 15,
                            'example': 15
                        },
                        'device_sync_status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'gui-theme': {
                            'type': 'string',
                            'enum': [
                                'blue',
                                'green',
                                'red',
                                'melongene',
                                'spring',
                                'summer',
                                'autumn',
                                'winter',
                                'space',
                                'calla-lily',
                                'binary-tunnel',
                                'diving',
                                'dreamy',
                                'technology',
                                'landscape',
                                'twilight',
                                'canyon',
                                'northern-light',
                                'astronomy',
                                'fish',
                                'penguin',
                                'panda',
                                'polar-bear',
                                'parrot',
                                'cave'
                            ]
                        },
                        'http_port': {
                            'type': 'integer',
                            'default': 80,
                            'example': 80
                        },
                        'https_port': {
                            'type': 'integer',
                            'default': 443,
                            'example': 443
                        },
                        'idle_timeout': {
                            'type': 'integer',
                            'default': 15,
                            'example': 15
                        },
                        'install-ifpolicy-only': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mgmt-addr': {
                            'type': 'string'
                        },
                        'mgmt-fqdn': {
                            'type': 'string'
                        },
                        'objects-force-deletion': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'offline_mode': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'register_passwd': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'sdwan-monitor-history': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'shell-access': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'shell-password': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'show-add-multiple': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'show-adom-devman': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'show-checkbox-in-table': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'show-device-import-export': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'show-hostname': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'show_automatic_script': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'show_grouping_script': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'show_schedule_script': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'show_tcl_script': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'unreg_dev_opt': {
                            'type': 'string',
                            'enum': [
                                'add_no_service',
                                'ignore',
                                'add_allow_service'
                            ]
                        },
                        'webadmin_language': {
                            'type': 'string',
                            'enum': [
                                'auto_detect',
                                'english',
                                'simplified_chinese',
                                'traditional_chinese',
                                'japanese',
                                'korean',
                                'spanish'
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
