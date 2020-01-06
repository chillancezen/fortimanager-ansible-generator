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
module: fmgr_cli_system_admin_user_user
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ delete get set update ] the following apis.
    - /cli/global/system/admin/user/{user}
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
        methods: [delete, get]
        description: 'Admin user.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Admin user.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                adom:
                    -
                        adom-name:
                            type: str
                            description: 'Admin domain names.'
                adom-exclude:
                    -
                        adom-name:
                            type: str
                            description: 'Admin domain names.'
                app-filter:
                    -
                        app-filter-name:
                            type: str
                            description: 'App filter name.'
                avatar:
                    type: str
                    description: 'Image file for avatar (maximum 4K base64 encoded).'
                ca:
                    type: str
                    description: 'PKI user certificate CA (CA name in local).'
                change-password:
                    type: str
                    default: disable
                    description:
                     - 'Enable/disable restricted user to change self password.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - disable
                        - enable
                dashboard:
                    -
                        column:
                            type: int
                            default: 0
                            description: 'Widget's column ID.'
                        diskio-content-type:
                            type: str
                            default: util
                            description:
                             - 'Disk I/O Monitor widget's chart type.'
                             - 'util - bandwidth utilization.'
                             - 'iops - the number of I/O requests.'
                             - 'blks - the amount of data of I/O requests.'
                            choices:
                                - util
                                - iops
                                - blks
                        diskio-period:
                            type: str
                            default: 1hour
                            description:
                             - 'Disk I/O Monitor widget's data period.'
                             - '1hour - 1 hour.'
                             - '8hour - 8 hour.'
                             - '24hour - 24 hour.'
                            choices:
                                - 1hour
                                - 8hour
                                - 24hour
                        log-rate-period:
                            type: str
                            description:
                             - 'Log receive monitor widget's data period.'
                             - '2min  - 2 minutes.'
                             - '1hour - 1 hour.'
                             - '6hours - 6 hours.'
                            choices:
                                - 2min 
                                - 1hour
                                - 6hours
                        log-rate-topn:
                            type: str
                            default: 5
                            description:
                             - 'Log receive monitor widget's number of top items to display.'
                             - '1 - Top 1.'
                             - '2 - Top 2.'
                             - '3 - Top 3.'
                             - '4 - Top 4.'
                             - '5 - Top 5.'
                            choices:
                                - 1
                                - 2
                                - 3
                                - 4
                                - 5
                        log-rate-type:
                            type: str
                            default: device
                            description:
                             - 'Log receive monitor widget's statistics breakdown options.'
                             - 'log - Show log rates for each log type.'
                             - 'device - Show log rates for each device.'
                            choices:
                                - log
                                - device
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
                            description: 'Widget's refresh interval.'
                        res-cpu-display:
                            type: str
                            default: average 
                            description:
                             - 'Widget's CPU display type.'
                             - 'average  - Average usage of CPU.'
                             - 'each - Each usage of CPU.'
                            choices:
                                - average 
                                - each
                        res-period:
                            type: str
                            default: 10min 
                            description:
                             - 'Widget's data period.'
                             - '10min  - Last 10 minutes.'
                             - 'hour - Last hour.'
                             - 'day - Last day.'
                            choices:
                                - 10min 
                                - hour
                                - day
                        res-view-type:
                            type: str
                            default: history
                            description:
                             - 'Widget's data view type.'
                             - 'real-time  - Real-time view.'
                             - 'history - History view.'
                            choices:
                                - real-time 
                                - history
                        status:
                            type: str
                            default: open
                            description:
                             - 'Widget's opened/closed state.'
                             - 'close - Widget closed.'
                             - 'open - Widget opened.'
                            choices:
                                - close
                                - open
                        tabid:
                            type: int
                            default: 0
                            description: 'ID of tab where widget is displayed.'
                        time-period:
                            type: str
                            default: 1hour
                            description:
                             - 'Log Database Monitor widget's data period.'
                             - '1hour - 1 hour.'
                             - '8hour - 8 hour.'
                             - '24hour - 24 hour.'
                            choices:
                                - 1hour
                                - 8hour
                                - 24hour
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
                                - top-lograte
                                - sysres
                                - sysinfo
                                - licinfo
                                - jsconsole
                                - sysop
                                - alert
                                - statistics
                                - rpteng
                                - raid
                                - logrecv
                                - devsummary
                                - logdb-perf
                                - logdb-lag
                                - disk-io
                                - log-rcvd-fwd
                dashboard-tabs:
                    -
                        name:
                            type: str
                            description: 'Tab name.'
                        tabid:
                            type: int
                            default: 0
                            description: 'Tab ID.'
                description:
                    type: str
                    description: 'Description.'
                dev-group:
                    type: str
                    description: 'device group.'
                email-address:
                    type: str
                    description: 'Email address.'
                ext-auth-accprofile-override:
                    type: str
                    default: disable
                    description:
                     - 'Allow to use the access profile provided by the remote authentication server.'
                     - 'disable - Disable access profile override.'
                     - 'enable - Enable access profile override.'
                    choices:
                        - disable
                        - enable
                ext-auth-adom-override:
                    type: str
                    default: disable
                    description:
                     - 'Allow to use the ADOM provided by the remote authentication server.'
                     - 'disable - Disable ADOM override.'
                     - 'enable - Enable ADOM override.'
                    choices:
                        - disable
                        - enable
                ext-auth-group-match:
                    type: str
                    description: 'Only administrators belonging to this group can login.'
                first-name:
                    type: str
                    description: 'First name.'
                force-password-change:
                    type: str
                    default: disable
                    description:
                     - 'Enable/disable force password change on next login.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - disable
                        - enable
                group:
                    type: str
                    description: 'Group name.'
                hidden:
                    type: int
                    default: 0
                    description: 'Hidden administrator.'
                ips-filter:
                    -
                        ips-filter-name:
                            type: str
                            description: 'IPS filter name.'
                ipv6_trusthost1:
                    type: str
                    default: ::/0
                    description: 'Admin user trusted host IPv6, default ::/0 for all.'
                ipv6_trusthost10:
                    type: str
                    default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
                    description: 'Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none.'
                ipv6_trusthost2:
                    type: str
                    default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
                    description: 'Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none.'
                ipv6_trusthost3:
                    type: str
                    default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
                    description: 'Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none.'
                ipv6_trusthost4:
                    type: str
                    default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
                    description: 'Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none.'
                ipv6_trusthost5:
                    type: str
                    default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
                    description: 'Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none.'
                ipv6_trusthost6:
                    type: str
                    default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
                    description: 'Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none.'
                ipv6_trusthost7:
                    type: str
                    default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
                    description: 'Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none.'
                ipv6_trusthost8:
                    type: str
                    default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
                    description: 'Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none.'
                ipv6_trusthost9:
                    type: str
                    default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
                    description: 'Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none.'
                last-name:
                    type: str
                    description: 'Last name.'
                ldap-server:
                    type: str
                    description: 'LDAP server name.'
                meta-data:
                    -
                        fieldlength:
                            type: int
                            default: 0
                            description: 'Field length.'
                        fieldname:
                            type: str
                            description: 'Field name.'
                        fieldvalue:
                            type: str
                            description: 'Field value.'
                        importance:
                            type: str
                            default: optional
                            description:
                             - 'Importance.'
                             - 'optional - This field is optional.'
                             - 'required - This field is required.'
                            choices:
                                - optional
                                - required
                        status:
                            type: str
                            default: enabled
                            description:
                             - 'Status.'
                             - 'disabled - This field is disabled.'
                             - 'enabled - This field is enabled.'
                            choices:
                                - disabled
                                - enabled
                mobile-number:
                    type: str
                    description: 'Mobile number.'
                pager-number:
                    type: str
                    description: 'Pager number.'
                password:
                    -
                        type: str
                        default: ENC ODU0NTM3NDg1NTMxMDg0MEm8OIAeHq0agoeKH1cknBy7orKo5c0jSfMSXT+VuqYN+atv8wiIW7W8PMzVMSjUkVEnbEpEW/komaek5rcWGIHzpijPphfS09Vlm0vEArsMz6UNqGxf5qLL/MxjITcW4WPWIFLPTPxZQAMoakc7pn8jNgVL
                password-expire:
                    -
                        type: str
                phone-number:
                    type: str
                    description: 'Phone number.'
                policy-package:
                    -
                        policy-package-name:
                            type: str
                            description: 'Policy package names.'
                profileid:
                    type: str
                    default: Restricted_User
                    description: 'Profile ID.'
                radius_server:
                    type: str
                    description: 'RADIUS server name.'
                restrict-access:
                    type: str
                    default: disable
                    description:
                     - 'Enable/disable restricted access to development VDOM.'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - disable
                        - enable
                restrict-dev-vdom:
                    -
                        dev-vdom:
                            type: str
                            description: 'Device or device VDOM.'
                rpc-permit:
                    type: str
                    default: none
                    description:
                     - 'set none/read/read-write rpc-permission.'
                     - 'read-write - Read-write permission.'
                     - 'none - No permission.'
                     - 'read - Read-only permission.'
                    choices:
                        - read-write
                        - none
                        - read
                ssh-public-key1:
                    -
                        type: str
                ssh-public-key2:
                    -
                        type: str
                ssh-public-key3:
                    -
                        type: str
                subject:
                    type: str
                    description: 'PKI user certificate name constraints.'
                tacacs-plus-server:
                    type: str
                    description: 'TACACS+ server name.'
                trusthost1:
                    type: str
                    default: 0.0.0.0 0.0.0.0
                    description: 'Admin user trusted host IP, default 0.0.0.0 0.0.0.0 for all.'
                trusthost10:
                    type: str
                    default: 255.255.255.255 255.255.255.255
                    description: 'Admin user trusted host IP, default 255.255.255.255 255.255.255.255 for none.'
                trusthost2:
                    type: str
                    default: 255.255.255.255 255.255.255.255
                    description: 'Admin user trusted host IP, default 255.255.255.255 255.255.255.255 for none.'
                trusthost3:
                    type: str
                    default: 255.255.255.255 255.255.255.255
                    description: 'Admin user trusted host IP, default 255.255.255.255 255.255.255.255 for none.'
                trusthost4:
                    type: str
                    default: 255.255.255.255 255.255.255.255
                    description: 'Admin user trusted host IP, default 255.255.255.255 255.255.255.255 for none.'
                trusthost5:
                    type: str
                    default: 255.255.255.255 255.255.255.255
                    description: 'Admin user trusted host IP, default 255.255.255.255 255.255.255.255 for none.'
                trusthost6:
                    type: str
                    default: 255.255.255.255 255.255.255.255
                    description: 'Admin user trusted host IP, default 255.255.255.255 255.255.255.255 for none.'
                trusthost7:
                    type: str
                    default: 255.255.255.255 255.255.255.255
                    description: 'Admin user trusted host IP, default 255.255.255.255 255.255.255.255 for none.'
                trusthost8:
                    type: str
                    default: 255.255.255.255 255.255.255.255
                    description: 'Admin user trusted host IP, default 255.255.255.255 255.255.255.255 for none.'
                trusthost9:
                    type: str
                    default: 255.255.255.255 255.255.255.255
                    description: 'Admin user trusted host IP, default 255.255.255.255 255.255.255.255 for none.'
                two-factor-auth:
                    type: str
                    default: disable
                    description:
                     - 'Enable 2-factor authentication (certificate + password).'
                     - 'disable - Disable 2-factor authentication.'
                     - 'enable - Enable 2-factor authentication.'
                    choices:
                        - disable
                        - enable
                user_type:
                    type: str
                    default: local
                    description:
                     - 'User type.'
                     - 'local - Local user.'
                     - 'radius - RADIUS user.'
                     - 'ldap - LDAP user.'
                     - 'tacacs-plus - TACACS+ user.'
                     - 'pki-auth - PKI user.'
                     - 'group - Group user.'
                    choices:
                        - local
                        - radius
                        - ldap
                        - tacacs-plus
                        - pki-auth
                        - group
                userid:
                    type: str
                    description: 'User name.'
                web-filter:
                    -
                        web-filter-name:
                            type: str
                            description: 'Web filter name.'
                wildcard:
                    type: str
                    default: disable
                    description:
                     - 'Enable/disable wildcard remote authentication.'
                     - 'disable - Disable username wildcard.'
                     - 'enable - Enable username wildcard.'
                    choices:
                        - disable
                        - enable

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /cli/system/admin/user/{user}
      fmgr_cli_system_admin_user_user:
         method: <value in [set, update]>
         url_params:
            user: <value of string>
         params:
            - 
               data: 
                  adom: 
                   - 
                        adom-name: <value of string>
                  adom-exclude: 
                   - 
                        adom-name: <value of string>
                  app-filter: 
                   - 
                        app-filter-name: <value of string>
                  avatar: <value of string>
                  ca: <value of string>
                  change-password: <value in [disable, enable] default: disable>
                  dashboard: 
                   - 
                        column: <value of integer default: 0>
                        diskio-content-type: <value in [util, iops, blks] default: util>
                        diskio-period: <value in [1hour, 8hour, 24hour] default: 1hour>
                        log-rate-period: <value in [2min , 1hour, 6hours]>
                        log-rate-topn: <value in [1, 2, 3, ...] default: 5>
                        log-rate-type: <value in [log, device] default: device>
                        moduleid: <value of integer default: 0>
                        name: <value of string>
                        num-entries: <value of integer default: 10>
                        refresh-interval: <value of integer default: 300>
                        res-cpu-display: <value in [average , each] default: average >
                        res-period: <value in [10min , hour, day] default: 10min >
                        res-view-type: <value in [real-time , history] default: history>
                        status: <value in [close, open] default: open>
                        tabid: <value of integer default: 0>
                        time-period: <value in [1hour, 8hour, 24hour] default: 1hour>
                        widget-type: <value in [top-lograte, sysres, sysinfo, ...]>
                  dashboard-tabs: 
                   - 
                        name: <value of string>
                        tabid: <value of integer default: 0>
                  description: <value of string>
                  dev-group: <value of string>
                  email-address: <value of string>
                  ext-auth-accprofile-override: <value in [disable, enable] default: disable>
                  ext-auth-adom-override: <value in [disable, enable] default: disable>
                  ext-auth-group-match: <value of string>
                  first-name: <value of string>
                  force-password-change: <value in [disable, enable] default: disable>
                  group: <value of string>
                  hidden: <value of integer default: 0>
                  ips-filter: 
                   - 
                        ips-filter-name: <value of string>
                  ipv6_trusthost1: <value of string default: ::/0>
                  ipv6_trusthost10: <value of string default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128>
                  ipv6_trusthost2: <value of string default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128>
                  ipv6_trusthost3: <value of string default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128>
                  ipv6_trusthost4: <value of string default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128>
                  ipv6_trusthost5: <value of string default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128>
                  ipv6_trusthost6: <value of string default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128>
                  ipv6_trusthost7: <value of string default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128>
                  ipv6_trusthost8: <value of string default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128>
                  ipv6_trusthost9: <value of string default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128>
                  last-name: <value of string>
                  ldap-server: <value of string>
                  meta-data: 
                   - 
                        fieldlength: <value of integer default: 0>
                        fieldname: <value of string>
                        fieldvalue: <value of string>
                        importance: <value in [optional, required] default: optional>
                        status: <value in [disabled, enabled] default: enabled>
                  mobile-number: <value of string>
                  pager-number: <value of string>
                  password: 
                   - <value of string default: ENC ODU0NTM3NDg1NTMxMDg0MEm8OIAeHq0agoeKH1cknBy7orKo5c0jSfMSXT+VuqYN+atv8wiIW7W8PMzVMSjUkVEnbEpEW/komaek5rcWGIHzpijPphfS09Vlm0vEArsMz6UNqGxf5qLL/MxjITcW4WPWIFLPTPxZQAMoakc7pn8jNgVL>
                  password-expire: 
                   - <value of string>
                  phone-number: <value of string>
                  policy-package: 
                   - 
                        policy-package-name: <value of string>
                  profileid: <value of string default: Restricted_User>
                  radius_server: <value of string>
                  restrict-access: <value in [disable, enable] default: disable>
                  restrict-dev-vdom: 
                   - 
                        dev-vdom: <value of string>
                  rpc-permit: <value in [read-write, none, read] default: none>
                  ssh-public-key1: 
                   - <value of string>
                  ssh-public-key2: 
                   - <value of string>
                  ssh-public-key3: 
                   - <value of string>
                  subject: <value of string>
                  tacacs-plus-server: <value of string>
                  trusthost1: <value of string default: 0.0.0.0 0.0.0.0>
                  trusthost10: <value of string default: 255.255.255.255 255.255.255.255>
                  trusthost2: <value of string default: 255.255.255.255 255.255.255.255>
                  trusthost3: <value of string default: 255.255.255.255 255.255.255.255>
                  trusthost4: <value of string default: 255.255.255.255 255.255.255.255>
                  trusthost5: <value of string default: 255.255.255.255 255.255.255.255>
                  trusthost6: <value of string default: 255.255.255.255 255.255.255.255>
                  trusthost7: <value of string default: 255.255.255.255 255.255.255.255>
                  trusthost8: <value of string default: 255.255.255.255 255.255.255.255>
                  trusthost9: <value of string default: 255.255.255.255 255.255.255.255>
                  two-factor-auth: <value in [disable, enable] default: disable>
                  user_type: <value in [local, radius, ldap, ...] default: local>
                  userid: <value of string>
                  web-filter: 
                   - 
                        web-filter-name: <value of string>
                  wildcard: <value in [disable, enable] default: disable>

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
            example: /cli/global/system/admin/user/{user}
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            adom:
               type: array
               suboptions:
                  adom-name:
                     type: str
                     description: 'Admin domain names.'
            adom-exclude:
               type: array
               suboptions:
                  adom-name:
                     type: str
                     description: 'Admin domain names.'
            app-filter:
               type: array
               suboptions:
                  app-filter-name:
                     type: str
                     description: 'App filter name.'
            avatar:
               type: str
               description: 'Image file for avatar (maximum 4K base64 encoded).'
            ca:
               type: str
               description: 'PKI user certificate CA (CA name in local).'
            change-password:
               type: str
               description: |
                  'Enable/disable restricted user to change self password.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: disable
            dashboard:
               type: array
               suboptions:
                  column:
                     type: int
                     description: 'Widget's column ID.'
                     example: 0
                  diskio-content-type:
                     type: str
                     description: |
                        'Disk I/O Monitor widget's chart type.'
                        'util - bandwidth utilization.'
                        'iops - the number of I/O requests.'
                        'blks - the amount of data of I/O requests.'
                     example: util
                  diskio-period:
                     type: str
                     description: |
                        'Disk I/O Monitor widget's data period.'
                        '1hour - 1 hour.'
                        '8hour - 8 hour.'
                        '24hour - 24 hour.'
                     example: 1hour
                  log-rate-period:
                     type: str
                     description: |
                        'Log receive monitor widget's data period.'
                        '2min  - 2 minutes.'
                        '1hour - 1 hour.'
                        '6hours - 6 hours.'
                  log-rate-topn:
                     type: str
                     description: |
                        'Log receive monitor widget's number of top items to display.'
                        '1 - Top 1.'
                        '2 - Top 2.'
                        '3 - Top 3.'
                        '4 - Top 4.'
                        '5 - Top 5.'
                     example: 5
                  log-rate-type:
                     type: str
                     description: |
                        'Log receive monitor widget's statistics breakdown options.'
                        'log - Show log rates for each log type.'
                        'device - Show log rates for each device.'
                     example: device
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
                     description: 'Widget's refresh interval.'
                     example: 300
                  res-cpu-display:
                     type: str
                     description: |
                        'Widget's CPU display type.'
                        'average  - Average usage of CPU.'
                        'each - Each usage of CPU.'
                     example: average 
                  res-period:
                     type: str
                     description: |
                        'Widget's data period.'
                        '10min  - Last 10 minutes.'
                        'hour - Last hour.'
                        'day - Last day.'
                     example: 10min 
                  res-view-type:
                     type: str
                     description: |
                        'Widget's data view type.'
                        'real-time  - Real-time view.'
                        'history - History view.'
                     example: history
                  status:
                     type: str
                     description: |
                        'Widget's opened/closed state.'
                        'close - Widget closed.'
                        'open - Widget opened.'
                     example: open
                  tabid:
                     type: int
                     description: 'ID of tab where widget is displayed.'
                     example: 0
                  time-period:
                     type: str
                     description: |
                        'Log Database Monitor widget's data period.'
                        '1hour - 1 hour.'
                        '8hour - 8 hour.'
                        '24hour - 24 hour.'
                     example: 1hour
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
            dashboard-tabs:
               type: array
               suboptions:
                  name:
                     type: str
                     description: 'Tab name.'
                  tabid:
                     type: int
                     description: 'Tab ID.'
                     example: 0
            description:
               type: str
               description: 'Description.'
            dev-group:
               type: str
               description: 'device group.'
            email-address:
               type: str
               description: 'Email address.'
            ext-auth-accprofile-override:
               type: str
               description: |
                  'Allow to use the access profile provided by the remote authentication server.'
                  'disable - Disable access profile override.'
                  'enable - Enable access profile override.'
               example: disable
            ext-auth-adom-override:
               type: str
               description: |
                  'Allow to use the ADOM provided by the remote authentication server.'
                  'disable - Disable ADOM override.'
                  'enable - Enable ADOM override.'
               example: disable
            ext-auth-group-match:
               type: str
               description: 'Only administrators belonging to this group can login.'
            first-name:
               type: str
               description: 'First name.'
            force-password-change:
               type: str
               description: |
                  'Enable/disable force password change on next login.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: disable
            group:
               type: str
               description: 'Group name.'
            hidden:
               type: int
               description: 'Hidden administrator.'
               example: 0
            ips-filter:
               type: array
               suboptions:
                  ips-filter-name:
                     type: str
                     description: 'IPS filter name.'
            ipv6_trusthost1:
               type: str
               description: 'Admin user trusted host IPv6, default ::/0 for all.'
               example: ::/0
            ipv6_trusthost10:
               type: str
               description: 'Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none.'
               example: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
            ipv6_trusthost2:
               type: str
               description: 'Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none.'
               example: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
            ipv6_trusthost3:
               type: str
               description: 'Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none.'
               example: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
            ipv6_trusthost4:
               type: str
               description: 'Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none.'
               example: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
            ipv6_trusthost5:
               type: str
               description: 'Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none.'
               example: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
            ipv6_trusthost6:
               type: str
               description: 'Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none.'
               example: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
            ipv6_trusthost7:
               type: str
               description: 'Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none.'
               example: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
            ipv6_trusthost8:
               type: str
               description: 'Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none.'
               example: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
            ipv6_trusthost9:
               type: str
               description: 'Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none.'
               example: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
            last-name:
               type: str
               description: 'Last name.'
            ldap-server:
               type: str
               description: 'LDAP server name.'
            meta-data:
               type: array
               suboptions:
                  fieldlength:
                     type: int
                     description: 'Field length.'
                     example: 0
                  fieldname:
                     type: str
                     description: 'Field name.'
                  fieldvalue:
                     type: str
                     description: 'Field value.'
                  importance:
                     type: str
                     description: |
                        'Importance.'
                        'optional - This field is optional.'
                        'required - This field is required.'
                     example: optional
                  status:
                     type: str
                     description: |
                        'Status.'
                        'disabled - This field is disabled.'
                        'enabled - This field is enabled.'
                     example: enabled
            mobile-number:
               type: str
               description: 'Mobile number.'
            pager-number:
               type: str
               description: 'Pager number.'
            password:
               type: array
               suboptions:
                  type: str
                  example: ENC ODU0NTM3NDg1NTMxMDg0MEm8OIAeHq0agoeKH1cknBy7orKo5c0jSfMSXT+VuqYN+atv8wiIW7W8PMzVMSjUkVEnbEpEW/komaek5rcWGIHzpijPphfS09Vlm0vEArsMz6UNqGxf5qLL/MxjITcW4WPWIFLPTPxZQAMoakc7pn8jNgVL
            password-expire:
               type: array
               suboptions:
                  type: str
            phone-number:
               type: str
               description: 'Phone number.'
            policy-package:
               type: array
               suboptions:
                  policy-package-name:
                     type: str
                     description: 'Policy package names.'
            profileid:
               type: str
               description: 'Profile ID.'
               example: Restricted_User
            radius_server:
               type: str
               description: 'RADIUS server name.'
            restrict-access:
               type: str
               description: |
                  'Enable/disable restricted access to development VDOM.'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: disable
            restrict-dev-vdom:
               type: array
               suboptions:
                  dev-vdom:
                     type: str
                     description: 'Device or device VDOM.'
            rpc-permit:
               type: str
               description: |
                  'set none/read/read-write rpc-permission.'
                  'read-write - Read-write permission.'
                  'none - No permission.'
                  'read - Read-only permission.'
               example: none
            ssh-public-key1:
               type: array
               suboptions:
                  type: str
            ssh-public-key2:
               type: array
               suboptions:
                  type: str
            ssh-public-key3:
               type: array
               suboptions:
                  type: str
            subject:
               type: str
               description: 'PKI user certificate name constraints.'
            tacacs-plus-server:
               type: str
               description: 'TACACS+ server name.'
            trusthost1:
               type: str
               description: 'Admin user trusted host IP, default 0.0.0.0 0.0.0.0 for all.'
               example: 0.0.0.0 0.0.0.0
            trusthost10:
               type: str
               description: 'Admin user trusted host IP, default 255.255.255.255 255.255.255.255 for none.'
               example: 255.255.255.255 255.255.255.255
            trusthost2:
               type: str
               description: 'Admin user trusted host IP, default 255.255.255.255 255.255.255.255 for none.'
               example: 255.255.255.255 255.255.255.255
            trusthost3:
               type: str
               description: 'Admin user trusted host IP, default 255.255.255.255 255.255.255.255 for none.'
               example: 255.255.255.255 255.255.255.255
            trusthost4:
               type: str
               description: 'Admin user trusted host IP, default 255.255.255.255 255.255.255.255 for none.'
               example: 255.255.255.255 255.255.255.255
            trusthost5:
               type: str
               description: 'Admin user trusted host IP, default 255.255.255.255 255.255.255.255 for none.'
               example: 255.255.255.255 255.255.255.255
            trusthost6:
               type: str
               description: 'Admin user trusted host IP, default 255.255.255.255 255.255.255.255 for none.'
               example: 255.255.255.255 255.255.255.255
            trusthost7:
               type: str
               description: 'Admin user trusted host IP, default 255.255.255.255 255.255.255.255 for none.'
               example: 255.255.255.255 255.255.255.255
            trusthost8:
               type: str
               description: 'Admin user trusted host IP, default 255.255.255.255 255.255.255.255 for none.'
               example: 255.255.255.255 255.255.255.255
            trusthost9:
               type: str
               description: 'Admin user trusted host IP, default 255.255.255.255 255.255.255.255 for none.'
               example: 255.255.255.255 255.255.255.255
            two-factor-auth:
               type: str
               description: |
                  'Enable 2-factor authentication (certificate + password).'
                  'disable - Disable 2-factor authentication.'
                  'enable - Enable 2-factor authentication.'
               example: disable
            user_type:
               type: str
               description: |
                  'User type.'
                  'local - Local user.'
                  'radius - RADIUS user.'
                  'ldap - LDAP user.'
                  'tacacs-plus - TACACS+ user.'
                  'pki-auth - PKI user.'
                  'group - Group user.'
               example: local
            userid:
               type: str
               description: 'User name.'
            web-filter:
               type: array
               suboptions:
                  web-filter-name:
                     type: str
                     description: 'Web filter name.'
            wildcard:
               type: str
               description: |
                  'Enable/disable wildcard remote authentication.'
                  'disable - Disable username wildcard.'
                  'enable - Enable username wildcard.'
               example: disable
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /cli/global/system/admin/user/{user}

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
        '/cli/global/system/admin/user/{user}'
    ]

    url_schema = [
        {
            'name': 'user',
            'type': 'string'
        }
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
                        'adom': {
                            'type': 'array',
                            'items': {
                                'adom-name': {
                                    'type': 'string'
                                }
                            }
                        },
                        'adom-exclude': {
                            'type': 'array',
                            'items': {
                                'adom-name': {
                                    'type': 'string'
                                }
                            }
                        },
                        'app-filter': {
                            'type': 'array',
                            'items': {
                                'app-filter-name': {
                                    'type': 'string'
                                }
                            }
                        },
                        'avatar': {
                            'type': 'string'
                        },
                        'ca': {
                            'type': 'string'
                        },
                        'change-password': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dashboard': {
                            'type': 'array',
                            'items': {
                                'column': {
                                    'type': 'integer',
                                    'default': 0,
                                    'example': 0
                                },
                                'diskio-content-type': {
                                    'type': 'string',
                                    'default': 'util',
                                    'enum': [
                                        'util',
                                        'iops',
                                        'blks'
                                    ]
                                },
                                'diskio-period': {
                                    'type': 'string',
                                    'default': '1hour',
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
                                    'default': '5',
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
                                    'default': 'device',
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
                                    'default': 'average ',
                                    'enum': [
                                        'average ',
                                        'each'
                                    ]
                                },
                                'res-period': {
                                    'type': 'string',
                                    'default': '10min ',
                                    'enum': [
                                        '10min ',
                                        'hour',
                                        'day'
                                    ]
                                },
                                'res-view-type': {
                                    'type': 'string',
                                    'default': 'history',
                                    'enum': [
                                        'real-time ',
                                        'history'
                                    ]
                                },
                                'status': {
                                    'type': 'string',
                                    'default': 'open',
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
                                    'default': '1hour',
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
                        'dashboard-tabs': {
                            'type': 'array',
                            'items': {
                                'name': {
                                    'type': 'string'
                                },
                                'tabid': {
                                    'type': 'integer',
                                    'default': 0,
                                    'example': 0
                                }
                            }
                        },
                        'description': {
                            'type': 'string'
                        },
                        'dev-group': {
                            'type': 'string'
                        },
                        'email-address': {
                            'type': 'string'
                        },
                        'ext-auth-accprofile-override': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ext-auth-adom-override': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ext-auth-group-match': {
                            'type': 'string'
                        },
                        'first-name': {
                            'type': 'string'
                        },
                        'force-password-change': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'group': {
                            'type': 'string'
                        },
                        'hidden': {
                            'type': 'integer',
                            'default': 0,
                            'example': 0
                        },
                        'ips-filter': {
                            'type': 'array',
                            'items': {
                                'ips-filter-name': {
                                    'type': 'string'
                                }
                            }
                        },
                        'ipv6_trusthost1': {
                            'type': 'string',
                            'default': '::/0'
                        },
                        'ipv6_trusthost10': {
                            'type': 'string',
                            'default': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128'
                        },
                        'ipv6_trusthost2': {
                            'type': 'string',
                            'default': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128'
                        },
                        'ipv6_trusthost3': {
                            'type': 'string',
                            'default': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128'
                        },
                        'ipv6_trusthost4': {
                            'type': 'string',
                            'default': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128'
                        },
                        'ipv6_trusthost5': {
                            'type': 'string',
                            'default': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128'
                        },
                        'ipv6_trusthost6': {
                            'type': 'string',
                            'default': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128'
                        },
                        'ipv6_trusthost7': {
                            'type': 'string',
                            'default': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128'
                        },
                        'ipv6_trusthost8': {
                            'type': 'string',
                            'default': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128'
                        },
                        'ipv6_trusthost9': {
                            'type': 'string',
                            'default': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128'
                        },
                        'last-name': {
                            'type': 'string'
                        },
                        'ldap-server': {
                            'type': 'string'
                        },
                        'meta-data': {
                            'type': 'array',
                            'items': {
                                'fieldlength': {
                                    'type': 'integer',
                                    'default': 0,
                                    'example': 0
                                },
                                'fieldname': {
                                    'type': 'string'
                                },
                                'fieldvalue': {
                                    'type': 'string'
                                },
                                'importance': {
                                    'type': 'string',
                                    'default': 'optional',
                                    'enum': [
                                        'optional',
                                        'required'
                                    ]
                                },
                                'status': {
                                    'type': 'string',
                                    'default': 'enabled',
                                    'enum': [
                                        'disabled',
                                        'enabled'
                                    ]
                                }
                            }
                        },
                        'mobile-number': {
                            'type': 'string'
                        },
                        'pager-number': {
                            'type': 'string'
                        },
                        'password': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'default': 'ENC ODU0NTM3NDg1NTMxMDg0MEm8OIAeHq0agoeKH1cknBy7orKo5c0jSfMSXT+VuqYN+atv8wiIW7W8PMzVMSjUkVEnbEpEW/komaek5rcWGIHzpijPphfS09Vlm0vEArsMz6UNqGxf5qLL/MxjITcW4WPWIFLPTPxZQAMoakc7pn8jNgVL'
                            }
                        },
                        'password-expire': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'phone-number': {
                            'type': 'string'
                        },
                        'policy-package': {
                            'type': 'array',
                            'items': {
                                'policy-package-name': {
                                    'type': 'string'
                                }
                            }
                        },
                        'profileid': {
                            'type': 'string',
                            'default': 'Restricted_User'
                        },
                        'radius_server': {
                            'type': 'string'
                        },
                        'restrict-access': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'restrict-dev-vdom': {
                            'type': 'array',
                            'items': {
                                'dev-vdom': {
                                    'type': 'string'
                                }
                            }
                        },
                        'rpc-permit': {
                            'type': 'string',
                            'default': 'none',
                            'enum': [
                                'read-write',
                                'none',
                                'read'
                            ]
                        },
                        'ssh-public-key1': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'ssh-public-key2': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'ssh-public-key3': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'subject': {
                            'type': 'string'
                        },
                        'tacacs-plus-server': {
                            'type': 'string'
                        },
                        'trusthost1': {
                            'type': 'string',
                            'default': '0.0.0.0 0.0.0.0'
                        },
                        'trusthost10': {
                            'type': 'string',
                            'default': '255.255.255.255 255.255.255.255'
                        },
                        'trusthost2': {
                            'type': 'string',
                            'default': '255.255.255.255 255.255.255.255'
                        },
                        'trusthost3': {
                            'type': 'string',
                            'default': '255.255.255.255 255.255.255.255'
                        },
                        'trusthost4': {
                            'type': 'string',
                            'default': '255.255.255.255 255.255.255.255'
                        },
                        'trusthost5': {
                            'type': 'string',
                            'default': '255.255.255.255 255.255.255.255'
                        },
                        'trusthost6': {
                            'type': 'string',
                            'default': '255.255.255.255 255.255.255.255'
                        },
                        'trusthost7': {
                            'type': 'string',
                            'default': '255.255.255.255 255.255.255.255'
                        },
                        'trusthost8': {
                            'type': 'string',
                            'default': '255.255.255.255 255.255.255.255'
                        },
                        'trusthost9': {
                            'type': 'string',
                            'default': '255.255.255.255 255.255.255.255'
                        },
                        'two-factor-auth': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'user_type': {
                            'type': 'string',
                            'default': 'local',
                            'enum': [
                                'local',
                                'radius',
                                'ldap',
                                'tacacs-plus',
                                'pki-auth',
                                'group'
                            ]
                        },
                        'userid': {
                            'type': 'string'
                        },
                        'web-filter': {
                            'type': 'array',
                            'items': {
                                'web-filter-name': {
                                    'type': 'string'
                                }
                            }
                        },
                        'wildcard': {
                            'type': 'string',
                            'default': 'disable',
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