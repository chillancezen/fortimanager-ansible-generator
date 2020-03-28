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
module: fmgr_firewall_mmsprofile
short_description: Configure MMS profiles.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/firewall/mms-profile
    - /pm/config/global/obj/firewall/mms-profile
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
        methods: [add, set, update]
        description: 'Configure MMS profiles.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    avnotificationtable:
                        type: str
                        description: 'AntiVirus notification table ID.'
                    bwordtable:
                        type: str
                        description: 'MMS banned word table ID.'
                    carrier-endpoint-prefix:
                        type: str
                        description: 'Enable/disable prefixing of end point values.'
                        choices:
                            - 'disable'
                            - 'enable'
                    carrier-endpoint-prefix-range-max:
                        type: int
                        description: 'Maximum length of end point value that can be prefixed (1 - 48).'
                    carrier-endpoint-prefix-range-min:
                        type: int
                        description: 'Minimum end point length to be prefixed (1 - 48).'
                    carrier-endpoint-prefix-string:
                        type: str
                        description: 'String with which to prefix End point values.'
                    carrierendpointbwltable:
                        type: str
                        description: 'Carrier end point filter table ID.'
                    comment:
                        type: str
                        description: 'Comment.'
                    extended-utm-log:
                        type: str
                        description: 'Enable/disable detailed UTM log messages.'
                        choices:
                            - 'disable'
                            - 'enable'
                    mm1:
                        -
                            type: str
                            choices:
                                - 'avmonitor'
                                - 'block'
                                - 'oversize'
                                - 'quarantine'
                                - 'scan'
                                - 'avquery'
                                - 'bannedword'
                                - 'no-content-summary'
                                - 'archive-summary'
                                - 'archive-full'
                                - 'carrier-endpoint-bwl'
                                - 'remove-blocked'
                                - 'chunkedbypass'
                                - 'clientcomfort'
                                - 'servercomfort'
                                - 'strict-file'
                                - 'mms-checksum'
                    mm1-addr-hdr:
                        type: str
                        description: 'HTTP header field (for MM1) containing user address.'
                    mm1-addr-source:
                        type: str
                        description: 'Source for MM1 user address.'
                        choices:
                            - 'http-header'
                            - 'cookie'
                    mm1-convert-hex:
                        type: str
                        description: 'Enable/disable converting user address from HEX string for MM1.'
                        choices:
                            - 'disable'
                            - 'enable'
                    mm1-outbreak-prevention:
                        type: str
                        description: 'Enable FortiGuard Virus Outbreak Prevention service.'
                        choices:
                            - 'disabled'
                            - 'files'
                            - 'full-archive'
                    mm1-retr-dupe:
                        type: str
                        description: 'Enable/disable duplicate scanning of MM1 retr.'
                        choices:
                            - 'disable'
                            - 'enable'
                    mm1-retrieve-scan:
                        type: str
                        description: 'Enable/disable scanning on MM1 retrieve configuration messages.'
                        choices:
                            - 'disable'
                            - 'enable'
                    mm1comfortamount:
                        type: int
                        description: 'MM1 comfort amount (0 - 4294967295).'
                    mm1comfortinterval:
                        type: int
                        description: 'MM1 comfort interval (0 - 4294967295).'
                    mm1oversizelimit:
                        type: int
                        description: 'Maximum file size to scan (1 - 819200 kB).'
                    mm3:
                        -
                            type: str
                            choices:
                                - 'avmonitor'
                                - 'block'
                                - 'oversize'
                                - 'quarantine'
                                - 'scan'
                                - 'avquery'
                                - 'bannedword'
                                - 'no-content-summary'
                                - 'archive-summary'
                                - 'archive-full'
                                - 'carrier-endpoint-bwl'
                                - 'remove-blocked'
                                - 'fragmail'
                                - 'splice'
                                - 'mms-checksum'
                    mm3-outbreak-prevention:
                        type: str
                        description: 'Enable FortiGuard Virus Outbreak Prevention service.'
                        choices:
                            - 'disabled'
                            - 'files'
                            - 'full-archive'
                    mm3oversizelimit:
                        type: int
                        description: 'Maximum file size to scan (1 - 819200 kB).'
                    mm4:
                        -
                            type: str
                            choices:
                                - 'avmonitor'
                                - 'block'
                                - 'oversize'
                                - 'quarantine'
                                - 'scan'
                                - 'avquery'
                                - 'bannedword'
                                - 'no-content-summary'
                                - 'archive-summary'
                                - 'archive-full'
                                - 'carrier-endpoint-bwl'
                                - 'remove-blocked'
                                - 'fragmail'
                                - 'splice'
                                - 'mms-checksum'
                    mm4-outbreak-prevention:
                        type: str
                        description: 'Enable FortiGuard Virus Outbreak Prevention service.'
                        choices:
                            - 'disabled'
                            - 'files'
                            - 'full-archive'
                    mm4oversizelimit:
                        type: int
                        description: 'Maximum file size to scan (1 - 819200 kB).'
                    mm7:
                        -
                            type: str
                            choices:
                                - 'avmonitor'
                                - 'block'
                                - 'oversize'
                                - 'quarantine'
                                - 'scan'
                                - 'avquery'
                                - 'bannedword'
                                - 'no-content-summary'
                                - 'archive-summary'
                                - 'archive-full'
                                - 'carrier-endpoint-bwl'
                                - 'remove-blocked'
                                - 'chunkedbypass'
                                - 'clientcomfort'
                                - 'servercomfort'
                                - 'strict-file'
                                - 'mms-checksum'
                    mm7-addr-hdr:
                        type: str
                        description: 'HTTP header field (for MM7) containing user address.'
                    mm7-addr-source:
                        type: str
                        description: 'Source for MM7 user address.'
                        choices:
                            - 'http-header'
                            - 'cookie'
                    mm7-convert-hex:
                        type: str
                        description: 'Enable/disable conversion of user address from HEX string for MM7.'
                        choices:
                            - 'disable'
                            - 'enable'
                    mm7-outbreak-prevention:
                        type: str
                        description: 'Enable FortiGuard Virus Outbreak Prevention service.'
                        choices:
                            - 'disabled'
                            - 'files'
                            - 'full-archive'
                    mm7comfortamount:
                        type: int
                        description: 'MM7 comfort amount (0 - 4294967295).'
                    mm7comfortinterval:
                        type: int
                        description: 'MM7 comfort interval (0 - 4294967295).'
                    mm7oversizelimit:
                        type: int
                        description: 'Maximum file size to scan (1 - 819200 kB).'
                    mms-antispam-mass-log:
                        type: str
                        description: 'Enable/disable logging for MMS antispam mass.'
                        choices:
                            - 'disable'
                            - 'enable'
                    mms-av-block-log:
                        type: str
                        description: 'Enable/disable logging for MMS antivirus file blocking.'
                        choices:
                            - 'disable'
                            - 'enable'
                    mms-av-oversize-log:
                        type: str
                        description: 'Enable/disable logging for MMS antivirus oversize file blocking.'
                        choices:
                            - 'disable'
                            - 'enable'
                    mms-av-virus-log:
                        type: str
                        description: 'Enable/disable logging for MMS antivirus scanning.'
                        choices:
                            - 'disable'
                            - 'enable'
                    mms-carrier-endpoint-filter-log:
                        type: str
                        description: 'Enable/disable logging for MMS end point filter blocking.'
                        choices:
                            - 'disable'
                            - 'enable'
                    mms-checksum-log:
                        type: str
                        description: 'Enable/disable MMS content checksum logging.'
                        choices:
                            - 'disable'
                            - 'enable'
                    mms-checksum-table:
                        type: str
                        description: 'MMS content checksum table ID.'
                    mms-notification-log:
                        type: str
                        description: 'Enable/disable logging for MMS notification messages.'
                        choices:
                            - 'disable'
                            - 'enable'
                    mms-web-content-log:
                        type: str
                        description: 'Enable/disable logging for MMS web content blocking.'
                        choices:
                            - 'disable'
                            - 'enable'
                    mmsbwordthreshold:
                        type: int
                        description: 'MMS banned word threshold.'
                    name:
                        type: str
                        description: 'Profile name.'
                    notif-msisdn:
                        -
                            msisdn:
                                type: str
                                description: 'Recipient MSISDN.'
                            threshold:
                                -
                                    type: str
                                    choices:
                                        - 'flood-thresh-1'
                                        - 'flood-thresh-2'
                                        - 'flood-thresh-3'
                                        - 'dupe-thresh-1'
                                        - 'dupe-thresh-2'
                                        - 'dupe-thresh-3'
                    remove-blocked-const-length:
                        type: str
                        description: 'Enable/disable MMS replacement of blocked file constant length.'
                        choices:
                            - 'disable'
                            - 'enable'
                    replacemsg-group:
                        type: str
                        description: 'Replacement message group.'
    schema_object1:
        methods: [get]
        description: 'Configure MMS profiles.'
        api_categories: [api_tag0]
        api_tag0:
            attr:
                type: str
                description: 'The name of the attribute to retrieve its datasource. Only used with &lt;i&gt;datasrc&lt;/i&gt; option.'
            fields:
                -
                    -
                        type: str
                        choices:
                            - 'avnotificationtable'
                            - 'bwordtable'
                            - 'carrier-endpoint-prefix'
                            - 'carrier-endpoint-prefix-range-max'
                            - 'carrier-endpoint-prefix-range-min'
                            - 'carrier-endpoint-prefix-string'
                            - 'carrierendpointbwltable'
                            - 'comment'
                            - 'extended-utm-log'
                            - 'mm1'
                            - 'mm1-addr-hdr'
                            - 'mm1-addr-source'
                            - 'mm1-convert-hex'
                            - 'mm1-outbreak-prevention'
                            - 'mm1-retr-dupe'
                            - 'mm1-retrieve-scan'
                            - 'mm1comfortamount'
                            - 'mm1comfortinterval'
                            - 'mm1oversizelimit'
                            - 'mm3'
                            - 'mm3-outbreak-prevention'
                            - 'mm3oversizelimit'
                            - 'mm4'
                            - 'mm4-outbreak-prevention'
                            - 'mm4oversizelimit'
                            - 'mm7'
                            - 'mm7-addr-hdr'
                            - 'mm7-addr-source'
                            - 'mm7-convert-hex'
                            - 'mm7-outbreak-prevention'
                            - 'mm7comfortamount'
                            - 'mm7comfortinterval'
                            - 'mm7oversizelimit'
                            - 'mms-antispam-mass-log'
                            - 'mms-av-block-log'
                            - 'mms-av-oversize-log'
                            - 'mms-av-virus-log'
                            - 'mms-carrier-endpoint-filter-log'
                            - 'mms-checksum-log'
                            - 'mms-checksum-table'
                            - 'mms-notification-log'
                            - 'mms-web-content-log'
                            - 'mmsbwordthreshold'
                            - 'name'
                            - 'remove-blocked-const-length'
                            - 'replacemsg-group'
            filter:
                -
                    type: str
            get used:
                type: int
            loadsub:
                type: int
                description: 'Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.'
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.'
                 - 'count - Return the number of matching entries instead of the actual entry data.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'datasrc - Return all objects that can be referenced by an attribute. Require <i>attr</i> parameter.'
                 - 'get reserved - Also return reserved objects in the result.'
                 - 'syntax - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.'
                choices:
                    - 'count'
                    - 'object member'
                    - 'datasrc'
                    - 'get reserved'
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
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/MMS-PROFILE
      fmgr_firewall_mmsprofile:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     avnotificationtable: <value of string>
                     bwordtable: <value of string>
                     carrier-endpoint-prefix: <value in [disable, enable]>
                     carrier-endpoint-prefix-range-max: <value of integer>
                     carrier-endpoint-prefix-range-min: <value of integer>
                     carrier-endpoint-prefix-string: <value of string>
                     carrierendpointbwltable: <value of string>
                     comment: <value of string>
                     extended-utm-log: <value in [disable, enable]>
                     mm1:
                       - <value in [avmonitor, block, oversize, ...]>
                     mm1-addr-hdr: <value of string>
                     mm1-addr-source: <value in [http-header, cookie]>
                     mm1-convert-hex: <value in [disable, enable]>
                     mm1-outbreak-prevention: <value in [disabled, files, full-archive]>
                     mm1-retr-dupe: <value in [disable, enable]>
                     mm1-retrieve-scan: <value in [disable, enable]>
                     mm1comfortamount: <value of integer>
                     mm1comfortinterval: <value of integer>
                     mm1oversizelimit: <value of integer>
                     mm3:
                       - <value in [avmonitor, block, oversize, ...]>
                     mm3-outbreak-prevention: <value in [disabled, files, full-archive]>
                     mm3oversizelimit: <value of integer>
                     mm4:
                       - <value in [avmonitor, block, oversize, ...]>
                     mm4-outbreak-prevention: <value in [disabled, files, full-archive]>
                     mm4oversizelimit: <value of integer>
                     mm7:
                       - <value in [avmonitor, block, oversize, ...]>
                     mm7-addr-hdr: <value of string>
                     mm7-addr-source: <value in [http-header, cookie]>
                     mm7-convert-hex: <value in [disable, enable]>
                     mm7-outbreak-prevention: <value in [disabled, files, full-archive]>
                     mm7comfortamount: <value of integer>
                     mm7comfortinterval: <value of integer>
                     mm7oversizelimit: <value of integer>
                     mms-antispam-mass-log: <value in [disable, enable]>
                     mms-av-block-log: <value in [disable, enable]>
                     mms-av-oversize-log: <value in [disable, enable]>
                     mms-av-virus-log: <value in [disable, enable]>
                     mms-carrier-endpoint-filter-log: <value in [disable, enable]>
                     mms-checksum-log: <value in [disable, enable]>
                     mms-checksum-table: <value of string>
                     mms-notification-log: <value in [disable, enable]>
                     mms-web-content-log: <value in [disable, enable]>
                     mmsbwordthreshold: <value of integer>
                     name: <value of string>
                     notif-msisdn:
                       -
                           msisdn: <value of string>
                           threshold:
                             - <value in [flood-thresh-1, flood-thresh-2, flood-thresh-3, ...]>
                     remove-blocked-const-length: <value in [disable, enable]>
                     replacemsg-group: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/MMS-PROFILE
      fmgr_firewall_mmsprofile:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [avnotificationtable, bwordtable, carrier-endpoint-prefix, ...]>
               filter:
                 - <value of string>
               get used: <value of integer>
               loadsub: <value of integer>
               option: <value in [count, object member, datasrc, ...]>
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
            example: '/pm/config/adom/{adom}/obj/firewall/mms-profile'
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
               avnotificationtable:
                  type: str
                  description: 'AntiVirus notification table ID.'
               bwordtable:
                  type: str
                  description: 'MMS banned word table ID.'
               carrier-endpoint-prefix:
                  type: str
                  description: 'Enable/disable prefixing of end point values.'
               carrier-endpoint-prefix-range-max:
                  type: int
                  description: 'Maximum length of end point value that can be prefixed (1 - 48).'
               carrier-endpoint-prefix-range-min:
                  type: int
                  description: 'Minimum end point length to be prefixed (1 - 48).'
               carrier-endpoint-prefix-string:
                  type: str
                  description: 'String with which to prefix End point values.'
               carrierendpointbwltable:
                  type: str
                  description: 'Carrier end point filter table ID.'
               comment:
                  type: str
                  description: 'Comment.'
               extended-utm-log:
                  type: str
                  description: 'Enable/disable detailed UTM log messages.'
               mm1:
                  type: array
                  suboptions:
                     type: str
               mm1-addr-hdr:
                  type: str
                  description: 'HTTP header field (for MM1) containing user address.'
               mm1-addr-source:
                  type: str
                  description: 'Source for MM1 user address.'
               mm1-convert-hex:
                  type: str
                  description: 'Enable/disable converting user address from HEX string for MM1.'
               mm1-outbreak-prevention:
                  type: str
                  description: 'Enable FortiGuard Virus Outbreak Prevention service.'
               mm1-retr-dupe:
                  type: str
                  description: 'Enable/disable duplicate scanning of MM1 retr.'
               mm1-retrieve-scan:
                  type: str
                  description: 'Enable/disable scanning on MM1 retrieve configuration messages.'
               mm1comfortamount:
                  type: int
                  description: 'MM1 comfort amount (0 - 4294967295).'
               mm1comfortinterval:
                  type: int
                  description: 'MM1 comfort interval (0 - 4294967295).'
               mm1oversizelimit:
                  type: int
                  description: 'Maximum file size to scan (1 - 819200 kB).'
               mm3:
                  type: array
                  suboptions:
                     type: str
               mm3-outbreak-prevention:
                  type: str
                  description: 'Enable FortiGuard Virus Outbreak Prevention service.'
               mm3oversizelimit:
                  type: int
                  description: 'Maximum file size to scan (1 - 819200 kB).'
               mm4:
                  type: array
                  suboptions:
                     type: str
               mm4-outbreak-prevention:
                  type: str
                  description: 'Enable FortiGuard Virus Outbreak Prevention service.'
               mm4oversizelimit:
                  type: int
                  description: 'Maximum file size to scan (1 - 819200 kB).'
               mm7:
                  type: array
                  suboptions:
                     type: str
               mm7-addr-hdr:
                  type: str
                  description: 'HTTP header field (for MM7) containing user address.'
               mm7-addr-source:
                  type: str
                  description: 'Source for MM7 user address.'
               mm7-convert-hex:
                  type: str
                  description: 'Enable/disable conversion of user address from HEX string for MM7.'
               mm7-outbreak-prevention:
                  type: str
                  description: 'Enable FortiGuard Virus Outbreak Prevention service.'
               mm7comfortamount:
                  type: int
                  description: 'MM7 comfort amount (0 - 4294967295).'
               mm7comfortinterval:
                  type: int
                  description: 'MM7 comfort interval (0 - 4294967295).'
               mm7oversizelimit:
                  type: int
                  description: 'Maximum file size to scan (1 - 819200 kB).'
               mms-antispam-mass-log:
                  type: str
                  description: 'Enable/disable logging for MMS antispam mass.'
               mms-av-block-log:
                  type: str
                  description: 'Enable/disable logging for MMS antivirus file blocking.'
               mms-av-oversize-log:
                  type: str
                  description: 'Enable/disable logging for MMS antivirus oversize file blocking.'
               mms-av-virus-log:
                  type: str
                  description: 'Enable/disable logging for MMS antivirus scanning.'
               mms-carrier-endpoint-filter-log:
                  type: str
                  description: 'Enable/disable logging for MMS end point filter blocking.'
               mms-checksum-log:
                  type: str
                  description: 'Enable/disable MMS content checksum logging.'
               mms-checksum-table:
                  type: str
                  description: 'MMS content checksum table ID.'
               mms-notification-log:
                  type: str
                  description: 'Enable/disable logging for MMS notification messages.'
               mms-web-content-log:
                  type: str
                  description: 'Enable/disable logging for MMS web content blocking.'
               mmsbwordthreshold:
                  type: int
                  description: 'MMS banned word threshold.'
               name:
                  type: str
                  description: 'Profile name.'
               notif-msisdn:
                  type: array
                  suboptions:
                     msisdn:
                        type: str
                        description: 'Recipient MSISDN.'
                     threshold:
                        type: array
                        suboptions:
                           type: str
               remove-blocked-const-length:
                  type: str
                  description: 'Enable/disable MMS replacement of blocked file constant length.'
               replacemsg-group:
                  type: str
                  description: 'Replacement message group.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/firewall/mms-profile'

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
        '/pm/config/adom/{adom}/obj/firewall/mms-profile',
        '/pm/config/global/obj/firewall/mms-profile'
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
                    'name': 'data',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'avnotificationtable': {
                            'type': 'string'
                        },
                        'bwordtable': {
                            'type': 'string'
                        },
                        'carrier-endpoint-prefix': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'carrier-endpoint-prefix-range-max': {
                            'type': 'integer'
                        },
                        'carrier-endpoint-prefix-range-min': {
                            'type': 'integer'
                        },
                        'carrier-endpoint-prefix-string': {
                            'type': 'string'
                        },
                        'carrierendpointbwltable': {
                            'type': 'string'
                        },
                        'comment': {
                            'type': 'string'
                        },
                        'extended-utm-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mm1': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'avmonitor',
                                    'block',
                                    'oversize',
                                    'quarantine',
                                    'scan',
                                    'avquery',
                                    'bannedword',
                                    'no-content-summary',
                                    'archive-summary',
                                    'archive-full',
                                    'carrier-endpoint-bwl',
                                    'remove-blocked',
                                    'chunkedbypass',
                                    'clientcomfort',
                                    'servercomfort',
                                    'strict-file',
                                    'mms-checksum'
                                ]
                            }
                        },
                        'mm1-addr-hdr': {
                            'type': 'string'
                        },
                        'mm1-addr-source': {
                            'type': 'string',
                            'enum': [
                                'http-header',
                                'cookie'
                            ]
                        },
                        'mm1-convert-hex': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mm1-outbreak-prevention': {
                            'type': 'string',
                            'enum': [
                                'disabled',
                                'files',
                                'full-archive'
                            ]
                        },
                        'mm1-retr-dupe': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mm1-retrieve-scan': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mm1comfortamount': {
                            'type': 'integer'
                        },
                        'mm1comfortinterval': {
                            'type': 'integer'
                        },
                        'mm1oversizelimit': {
                            'type': 'integer'
                        },
                        'mm3': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'avmonitor',
                                    'block',
                                    'oversize',
                                    'quarantine',
                                    'scan',
                                    'avquery',
                                    'bannedword',
                                    'no-content-summary',
                                    'archive-summary',
                                    'archive-full',
                                    'carrier-endpoint-bwl',
                                    'remove-blocked',
                                    'fragmail',
                                    'splice',
                                    'mms-checksum'
                                ]
                            }
                        },
                        'mm3-outbreak-prevention': {
                            'type': 'string',
                            'enum': [
                                'disabled',
                                'files',
                                'full-archive'
                            ]
                        },
                        'mm3oversizelimit': {
                            'type': 'integer'
                        },
                        'mm4': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'avmonitor',
                                    'block',
                                    'oversize',
                                    'quarantine',
                                    'scan',
                                    'avquery',
                                    'bannedword',
                                    'no-content-summary',
                                    'archive-summary',
                                    'archive-full',
                                    'carrier-endpoint-bwl',
                                    'remove-blocked',
                                    'fragmail',
                                    'splice',
                                    'mms-checksum'
                                ]
                            }
                        },
                        'mm4-outbreak-prevention': {
                            'type': 'string',
                            'enum': [
                                'disabled',
                                'files',
                                'full-archive'
                            ]
                        },
                        'mm4oversizelimit': {
                            'type': 'integer'
                        },
                        'mm7': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'avmonitor',
                                    'block',
                                    'oversize',
                                    'quarantine',
                                    'scan',
                                    'avquery',
                                    'bannedword',
                                    'no-content-summary',
                                    'archive-summary',
                                    'archive-full',
                                    'carrier-endpoint-bwl',
                                    'remove-blocked',
                                    'chunkedbypass',
                                    'clientcomfort',
                                    'servercomfort',
                                    'strict-file',
                                    'mms-checksum'
                                ]
                            }
                        },
                        'mm7-addr-hdr': {
                            'type': 'string'
                        },
                        'mm7-addr-source': {
                            'type': 'string',
                            'enum': [
                                'http-header',
                                'cookie'
                            ]
                        },
                        'mm7-convert-hex': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mm7-outbreak-prevention': {
                            'type': 'string',
                            'enum': [
                                'disabled',
                                'files',
                                'full-archive'
                            ]
                        },
                        'mm7comfortamount': {
                            'type': 'integer'
                        },
                        'mm7comfortinterval': {
                            'type': 'integer'
                        },
                        'mm7oversizelimit': {
                            'type': 'integer'
                        },
                        'mms-antispam-mass-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mms-av-block-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mms-av-oversize-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mms-av-virus-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mms-carrier-endpoint-filter-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mms-checksum-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mms-checksum-table': {
                            'type': 'string'
                        },
                        'mms-notification-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mms-web-content-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mmsbwordthreshold': {
                            'type': 'integer'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'notif-msisdn': {
                            'type': 'array',
                            'items': {
                                'msisdn': {
                                    'type': 'string'
                                },
                                'threshold': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string',
                                        'enum': [
                                            'flood-thresh-1',
                                            'flood-thresh-2',
                                            'flood-thresh-3',
                                            'dupe-thresh-1',
                                            'dupe-thresh-2',
                                            'dupe-thresh-3'
                                        ]
                                    }
                                }
                            }
                        },
                        'remove-blocked-const-length': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'replacemsg-group': {
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
                    'name': 'attr',
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
                                'avnotificationtable',
                                'bwordtable',
                                'carrier-endpoint-prefix',
                                'carrier-endpoint-prefix-range-max',
                                'carrier-endpoint-prefix-range-min',
                                'carrier-endpoint-prefix-string',
                                'carrierendpointbwltable',
                                'comment',
                                'extended-utm-log',
                                'mm1',
                                'mm1-addr-hdr',
                                'mm1-addr-source',
                                'mm1-convert-hex',
                                'mm1-outbreak-prevention',
                                'mm1-retr-dupe',
                                'mm1-retrieve-scan',
                                'mm1comfortamount',
                                'mm1comfortinterval',
                                'mm1oversizelimit',
                                'mm3',
                                'mm3-outbreak-prevention',
                                'mm3oversizelimit',
                                'mm4',
                                'mm4-outbreak-prevention',
                                'mm4oversizelimit',
                                'mm7',
                                'mm7-addr-hdr',
                                'mm7-addr-source',
                                'mm7-convert-hex',
                                'mm7-outbreak-prevention',
                                'mm7comfortamount',
                                'mm7comfortinterval',
                                'mm7oversizelimit',
                                'mms-antispam-mass-log',
                                'mms-av-block-log',
                                'mms-av-oversize-log',
                                'mms-av-virus-log',
                                'mms-carrier-endpoint-filter-log',
                                'mms-checksum-log',
                                'mms-checksum-table',
                                'mms-notification-log',
                                'mms-web-content-log',
                                'mmsbwordthreshold',
                                'name',
                                'remove-blocked-const-length',
                                'replacemsg-group'
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
                    'name': 'get used',
                    'api_tag': 0
                },
                {
                    'type': 'integer',
                    'name': 'loadsub',
                    'api_tag': 0
                },
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'count',
                            'object member',
                            'datasrc',
                            'get reserved',
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
        'loose_validation': {
            'type': 'bool',
            'required': False,
            'default': False
        },
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
