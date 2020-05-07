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
module: fmgr_system_admin_profile_obj
short_description: Admin profile.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ delete get set update ] the following apis.
    - /cli/global/system/admin/profile/{profile}
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
    workspace_locking_adom:
        description: the adom to lock in case FortiManager running in workspace mode
        required: False
        type: string
        choices:
          - global
          - custom adom
    workspace_locking_timeout:
        description: teh maximum time in seconds to wait for other user to release the workspace lock
        required: False
        type: integer
        default: 300
    url_params:
        description: the parameters in url path
        required: True
        type: dict
        suboptions:
            profile:
                type: str
    schema_object0:
        methods: [delete, get]
        description: 'Admin profile.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Admin profile.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                adom-lock:
                    type: str
                    default: 'none'
                    description:
                     - 'ADOM locking'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                adom-policy-packages:
                    type: str
                    default: 'none'
                    description:
                     - 'ADOM policy packages.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                adom-switch:
                    type: str
                    default: 'none'
                    description:
                     - 'Administrator domain.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                app-filter:
                    type: str
                    default: 'disable'
                    description:
                     - 'App filter.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                assignment:
                    type: str
                    default: 'none'
                    description:
                     - 'Assignment permission.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                change-password:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable restricted user to change self password.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                config-retrieve:
                    type: str
                    default: 'none'
                    description:
                     - 'Configuration retrieve.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                config-revert:
                    type: str
                    default: 'none'
                    description:
                     - 'Revert Configuration from Revision History'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                consistency-check:
                    type: str
                    default: 'none'
                    description:
                     - 'Consistency check.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                datamask:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable data masking.'
                     - 'disable - Disable data masking.'
                     - 'enable - Enable data masking.'
                    choices:
                        - 'disable'
                        - 'enable'
                datamask-custom-fields:
                    -
                        field-category:
                            -
                                type: str
                                choices:
                                    - 'log'
                                    - 'fortiview'
                                    - 'alert'
                                    - 'ueba'
                                    - 'all'
                        field-name:
                            type: str
                            description: 'Field name.'
                        field-status:
                            type: str
                            default: 'enable'
                            description:
                             - 'Field status.'
                             - 'disable - Disable field.'
                             - 'enable - Enable field.'
                            choices:
                                - 'disable'
                                - 'enable'
                        field-type:
                            type: str
                            default: 'string'
                            description:
                             - 'Field type.'
                             - 'string - String.'
                             - 'ip - IP.'
                             - 'mac - MAC address.'
                             - 'email - Email address.'
                             - 'unknown - Unknown.'
                            choices:
                                - 'string'
                                - 'ip'
                                - 'mac'
                                - 'email'
                                - 'unknown'
                datamask-custom-priority:
                    type: str
                    default: 'disable'
                    description:
                     - 'Prioritize custom fields.'
                     - 'disable - Disable custom field search priority.'
                     - 'enable - Enable custom field search priority.'
                    choices:
                        - 'disable'
                        - 'enable'
                datamask-fields:
                    -
                        type: str
                        choices:
                            - 'user'
                            - 'srcip'
                            - 'srcname'
                            - 'srcmac'
                            - 'dstip'
                            - 'dstname'
                            - 'email'
                            - 'message'
                            - 'domain'
                datamask-key:
                    -
                        type: str
                        default: 'ENC MzI1Nzc3MjAyNTg1Njg0NNKOn5kCfNawE/VnDbtMpWXduJpvaREIOxBK4PNmJmqeRwgB9loHz7FqcMzTT5DrD50rb65MQrxNOiuHZ7eM/qmDuMiCMym4F...'
                deploy-management:
                    type: str
                    default: 'none'
                    description:
                     - 'Install to devices.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                description:
                    type: str
                    description: 'Description.'
                device-ap:
                    type: str
                    default: 'none'
                    description:
                     - 'Manage AP.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                device-config:
                    type: str
                    default: 'none'
                    description:
                     - 'Manage device configurations.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                device-forticlient:
                    type: str
                    default: 'none'
                    description:
                     - 'Manage FortiClient.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                device-fortiswitch:
                    type: str
                    default: 'none'
                    description:
                     - 'Manage FortiSwitch.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                device-manager:
                    type: str
                    default: 'none'
                    description:
                     - 'Device manager.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                device-op:
                    type: str
                    default: 'none'
                    description:
                     - 'Device add/delete/edit.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                device-policy-package-lock:
                    type: str
                    default: 'none'
                    description:
                     - 'Device/Policy Package locking'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                device-profile:
                    type: str
                    default: 'none'
                    description:
                     - 'Device profile permission.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                device-revision-deletion:
                    type: str
                    default: 'none'
                    description:
                     - 'Delete device revision.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                device-wan-link-load-balance:
                    type: str
                    default: 'none'
                    description:
                     - 'Manage WAN link load balance.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                event-management:
                    type: str
                    default: 'none'
                    description:
                     - 'Event management.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                fgd-center-advanced:
                    type: str
                    default: 'none'
                    description:
                     - 'FortiGuard Center Advanced.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                fgd-center-fmw-mgmt:
                    type: str
                    default: 'none'
                    description:
                     - 'FortiGuard Center Firmware Management.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                fgd-center-licensing:
                    type: str
                    default: 'none'
                    description:
                     - 'FortiGuard Center Licensing.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                fgd_center:
                    type: str
                    default: 'none'
                    description:
                     - 'FortiGuard Center.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                global-policy-packages:
                    type: str
                    default: 'none'
                    description:
                     - 'Global policy packages.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                import-policy-packages:
                    type: str
                    default: 'none'
                    description:
                     - 'Import Policy Package.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                intf-mapping:
                    type: str
                    default: 'none'
                    description:
                     - 'Interface Mapping'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                ips-filter:
                    type: str
                    default: 'disable'
                    description:
                     - 'IPS filter.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'
                log-viewer:
                    type: str
                    default: 'none'
                    description:
                     - 'Log viewer.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                policy-objects:
                    type: str
                    default: 'none'
                    description:
                     - 'Policy objects permission.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                profileid:
                    type: str
                    description: 'Profile ID.'
                read-passwd:
                    type: str
                    default: 'none'
                    description:
                     - 'View password in clear text.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                realtime-monitor:
                    type: str
                    default: 'none'
                    description:
                     - 'Realtime monitor.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                report-viewer:
                    type: str
                    default: 'none'
                    description:
                     - 'Report viewer.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                scope:
                    type: str
                    default: 'global'
                    description:
                     - 'Scope.'
                     - 'global - Global scope.'
                     - 'adom - ADOM scope.'
                    choices:
                        - 'global'
                        - 'adom'
                set-install-targets:
                    type: str
                    default: 'none'
                    description:
                     - 'Edit installation targets.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                system-setting:
                    type: str
                    default: 'none'
                    description:
                     - 'System setting.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                term-access:
                    type: str
                    default: 'none'
                    description:
                     - 'Terminal access.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                type:
                    type: str
                    default: 'system'
                    description:
                     - 'profile type.'
                     - 'system - System admin.'
                     - 'restricted - Restricted admin.'
                    choices:
                        - 'system'
                        - 'restricted'
                vpn-manager:
                    type: str
                    default: 'none'
                    description:
                     - 'VPN manager.'
                     - 'none - No permission.'
                     - 'read - Read permission.'
                     - 'read-write - Read-write permission.'
                    choices:
                        - 'none'
                        - 'read'
                        - 'read-write'
                web-filter:
                    type: str
                    default: 'disable'
                    description:
                     - 'Web filter.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'

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

    - name: REQUESTING /CLI/SYSTEM/ADMIN/PROFILE/{PROFILE}
      fmgr_system_admin_profile_obj:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [set, update]>
         url_params:
            profile: <value of string>
         params:
            -
               data:
                  adom-lock: <value in [none, read, read-write] default: 'none'>
                  adom-policy-packages: <value in [none, read, read-write] default: 'none'>
                  adom-switch: <value in [none, read, read-write] default: 'none'>
                  app-filter: <value in [disable, enable] default: 'disable'>
                  assignment: <value in [none, read, read-write] default: 'none'>
                  change-password: <value in [disable, enable] default: 'disable'>
                  config-retrieve: <value in [none, read, read-write] default: 'none'>
                  config-revert: <value in [none, read, read-write] default: 'none'>
                  consistency-check: <value in [none, read, read-write] default: 'none'>
                  datamask: <value in [disable, enable] default: 'disable'>
                  datamask-custom-fields:
                    -
                        field-category:
                          - <value in [log, fortiview, alert, ...]>
                        field-name: <value of string>
                        field-status: <value in [disable, enable] default: 'enable'>
                        field-type: <value in [string, ip, mac, ...] default: 'string'>
                  datamask-custom-priority: <value in [disable, enable] default: 'disable'>
                  datamask-fields:
                    - <value in [user, srcip, srcname, ...]>
                  datamask-key:
                    - <value of string default: 'ENC MzI1Nzc3MjAyNTg1Njg0NNKOn5kCfNawE/VnDbtMpWXduJpvaREIOxBK4PNmJmqeRwgB9loH...'>
                  deploy-management: <value in [none, read, read-write] default: 'none'>
                  description: <value of string>
                  device-ap: <value in [none, read, read-write] default: 'none'>
                  device-config: <value in [none, read, read-write] default: 'none'>
                  device-forticlient: <value in [none, read, read-write] default: 'none'>
                  device-fortiswitch: <value in [none, read, read-write] default: 'none'>
                  device-manager: <value in [none, read, read-write] default: 'none'>
                  device-op: <value in [none, read, read-write] default: 'none'>
                  device-policy-package-lock: <value in [none, read, read-write] default: 'none'>
                  device-profile: <value in [none, read, read-write] default: 'none'>
                  device-revision-deletion: <value in [none, read, read-write] default: 'none'>
                  device-wan-link-load-balance: <value in [none, read, read-write] default: 'none'>
                  event-management: <value in [none, read, read-write] default: 'none'>
                  fgd-center-advanced: <value in [none, read, read-write] default: 'none'>
                  fgd-center-fmw-mgmt: <value in [none, read, read-write] default: 'none'>
                  fgd-center-licensing: <value in [none, read, read-write] default: 'none'>
                  fgd_center: <value in [none, read, read-write] default: 'none'>
                  global-policy-packages: <value in [none, read, read-write] default: 'none'>
                  import-policy-packages: <value in [none, read, read-write] default: 'none'>
                  intf-mapping: <value in [none, read, read-write] default: 'none'>
                  ips-filter: <value in [disable, enable] default: 'disable'>
                  log-viewer: <value in [none, read, read-write] default: 'none'>
                  policy-objects: <value in [none, read, read-write] default: 'none'>
                  profileid: <value of string>
                  read-passwd: <value in [none, read, read-write] default: 'none'>
                  realtime-monitor: <value in [none, read, read-write] default: 'none'>
                  report-viewer: <value in [none, read, read-write] default: 'none'>
                  scope: <value in [global, adom] default: 'global'>
                  set-install-targets: <value in [none, read, read-write] default: 'none'>
                  system-setting: <value in [none, read, read-write] default: 'none'>
                  term-access: <value in [none, read, read-write] default: 'none'>
                  type: <value in [system, restricted] default: 'system'>
                  vpn-manager: <value in [none, read, read-write] default: 'none'>
                  web-filter: <value in [disable, enable] default: 'disable'>

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
            example: '/cli/global/system/admin/profile/{profile}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            adom-lock:
               type: str
               description: |
                  'ADOM locking'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            adom-policy-packages:
               type: str
               description: |
                  'ADOM policy packages.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            adom-switch:
               type: str
               description: |
                  'Administrator domain.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            app-filter:
               type: str
               description: |
                  'App filter.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'disable'
            assignment:
               type: str
               description: |
                  'Assignment permission.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            change-password:
               type: str
               description: |
                  'Enable/disable restricted user to change self password.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'disable'
            config-retrieve:
               type: str
               description: |
                  'Configuration retrieve.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            config-revert:
               type: str
               description: |
                  'Revert Configuration from Revision History'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            consistency-check:
               type: str
               description: |
                  'Consistency check.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            datamask:
               type: str
               description: |
                  'Enable/disable data masking.'
                  'disable - Disable data masking.'
                  'enable - Enable data masking.'
               example: 'disable'
            datamask-custom-fields:
               type: array
               suboptions:
                  field-category:
                     type: array
                     suboptions:
                        type: str
                  field-name:
                     type: str
                     description: 'Field name.'
                  field-status:
                     type: str
                     description: |
                        'Field status.'
                        'disable - Disable field.'
                        'enable - Enable field.'
                     example: 'enable'
                  field-type:
                     type: str
                     description: |
                        'Field type.'
                        'string - String.'
                        'ip - IP.'
                        'mac - MAC address.'
                        'email - Email address.'
                        'unknown - Unknown.'
                     example: 'string'
            datamask-custom-priority:
               type: str
               description: |
                  'Prioritize custom fields.'
                  'disable - Disable custom field search priority.'
                  'enable - Enable custom field search priority.'
               example: 'disable'
            datamask-fields:
               type: array
               suboptions:
                  type: str
            datamask-key:
               type: array
               suboptions:
                  type: str
                  example: 'ENC MzI1Nzc3MjAyNTg1Njg0NNKOn5kCfNawE/VnDbtMpWXduJpvaREIOxBK4PNmJmqeRwgB9loH...'
            deploy-management:
               type: str
               description: |
                  'Install to devices.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            description:
               type: str
               description: 'Description.'
            device-ap:
               type: str
               description: |
                  'Manage AP.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            device-config:
               type: str
               description: |
                  'Manage device configurations.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            device-forticlient:
               type: str
               description: |
                  'Manage FortiClient.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            device-fortiswitch:
               type: str
               description: |
                  'Manage FortiSwitch.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            device-manager:
               type: str
               description: |
                  'Device manager.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            device-op:
               type: str
               description: |
                  'Device add/delete/edit.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            device-policy-package-lock:
               type: str
               description: |
                  'Device/Policy Package locking'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            device-profile:
               type: str
               description: |
                  'Device profile permission.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            device-revision-deletion:
               type: str
               description: |
                  'Delete device revision.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            device-wan-link-load-balance:
               type: str
               description: |
                  'Manage WAN link load balance.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            event-management:
               type: str
               description: |
                  'Event management.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            fgd-center-advanced:
               type: str
               description: |
                  'FortiGuard Center Advanced.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            fgd-center-fmw-mgmt:
               type: str
               description: |
                  'FortiGuard Center Firmware Management.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            fgd-center-licensing:
               type: str
               description: |
                  'FortiGuard Center Licensing.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            fgd_center:
               type: str
               description: |
                  'FortiGuard Center.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            global-policy-packages:
               type: str
               description: |
                  'Global policy packages.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            import-policy-packages:
               type: str
               description: |
                  'Import Policy Package.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            intf-mapping:
               type: str
               description: |
                  'Interface Mapping'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            ips-filter:
               type: str
               description: |
                  'IPS filter.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'disable'
            log-viewer:
               type: str
               description: |
                  'Log viewer.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            policy-objects:
               type: str
               description: |
                  'Policy objects permission.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            profileid:
               type: str
               description: 'Profile ID.'
            read-passwd:
               type: str
               description: |
                  'View password in clear text.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            realtime-monitor:
               type: str
               description: |
                  'Realtime monitor.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            report-viewer:
               type: str
               description: |
                  'Report viewer.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            scope:
               type: str
               description: |
                  'Scope.'
                  'global - Global scope.'
                  'adom - ADOM scope.'
               example: 'global'
            set-install-targets:
               type: str
               description: |
                  'Edit installation targets.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            system-setting:
               type: str
               description: |
                  'System setting.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            term-access:
               type: str
               description: |
                  'Terminal access.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            type:
               type: str
               description: |
                  'profile type.'
                  'system - System admin.'
                  'restricted - Restricted admin.'
               example: 'system'
            vpn-manager:
               type: str
               description: |
                  'VPN manager.'
                  'none - No permission.'
                  'read - Read permission.'
                  'read-write - Read-write permission.'
               example: 'none'
            web-filter:
               type: str
               description: |
                  'Web filter.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'disable'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/cli/global/system/admin/profile/{profile}'

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
        '/cli/global/system/admin/profile/{profile}'
    ]

    url_schema = [
        {
            'name': 'profile',
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
                }
            ],
            'object1': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'adom-lock': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'adom-policy-packages': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'adom-switch': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'app-filter': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'assignment': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'change-password': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'config-retrieve': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'config-revert': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'consistency-check': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'datamask': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'datamask-custom-fields': {
                            'type': 'array',
                            'items': {
                                'field-category': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string',
                                        'enum': [
                                            'log',
                                            'fortiview',
                                            'alert',
                                            'ueba',
                                            'all'
                                        ]
                                    }
                                },
                                'field-name': {
                                    'type': 'string'
                                },
                                'field-status': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'field-type': {
                                    'type': 'string',
                                    'enum': [
                                        'string',
                                        'ip',
                                        'mac',
                                        'email',
                                        'unknown'
                                    ]
                                }
                            }
                        },
                        'datamask-custom-priority': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'datamask-fields': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'user',
                                    'srcip',
                                    'srcname',
                                    'srcmac',
                                    'dstip',
                                    'dstname',
                                    'email',
                                    'message',
                                    'domain'
                                ]
                            }
                        },
                        'datamask-key': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'deploy-management': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'description': {
                            'type': 'string'
                        },
                        'device-ap': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'device-config': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'device-forticlient': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'device-fortiswitch': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'device-manager': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'device-op': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'device-policy-package-lock': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'device-profile': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'device-revision-deletion': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'device-wan-link-load-balance': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'event-management': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'fgd-center-advanced': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'fgd-center-fmw-mgmt': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'fgd-center-licensing': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'fgd_center': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'global-policy-packages': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'import-policy-packages': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'intf-mapping': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'ips-filter': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'log-viewer': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'policy-objects': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'profileid': {
                            'type': 'string'
                        },
                        'read-passwd': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'realtime-monitor': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'report-viewer': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'scope': {
                            'type': 'string',
                            'enum': [
                                'global',
                                'adom'
                            ]
                        },
                        'set-install-targets': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'system-setting': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'term-access': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'type': {
                            'type': 'string',
                            'enum': [
                                'system',
                                'restricted'
                            ]
                        },
                        'vpn-manager': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'read',
                                'read-write'
                            ]
                        },
                        'web-filter': {
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
            'delete': 'object0',
            'get': 'object0',
            'set': 'object1',
            'update': 'object1'
        }
    }

    module_arg_spec = {
        'loose_validation': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'workspace_locking_adom': {
            'type': 'str',
            'required': False
        },
        'workspace_locking_timeout': {
            'type': 'int',
            'required': False,
            'default': 300
        },
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
    loose_validation = module.params['loose_validation']

    fmgr = None
    payload = None
    response = DEFAULT_RESULT_OBJ

    if module._socket_path:
        connection = Connection(module._socket_path)
        tools = FMGRCommon()
        if loose_validation == False:
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
