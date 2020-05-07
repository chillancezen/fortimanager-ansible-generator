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
module: fmgr_system_replacemsggroup
short_description: Configure replacement message groups.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/system/replacemsg-group
    - /pm/config/global/obj/system/replacemsg-group
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
    loose_validation:
        description: Do parameter validation in a loose way
        required: False
        type: bool
        default: false
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
            adom:
                type: str
                description: the domain prefix, the none and global are reserved
                choices:
                  - none
                  - global
                  - custom dom
    schema_object0:
        methods: [add, set, update]
        description: 'Configure replacement message groups.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    admin:
                        -
                            buffer:
                                type: str
                                description: 'Message string.'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            msg-type:
                                type: str
                                description: 'Message type.'
                    alertmail:
                        -
                            buffer:
                                type: str
                                description: 'Message string.'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            msg-type:
                                type: str
                                description: 'Message type.'
                    auth:
                        -
                            buffer:
                                type: str
                                description: 'Message string.'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            msg-type:
                                type: str
                                description: 'Message type.'
                    comment:
                        type: str
                        description: 'Comment.'
                    custom-message:
                        -
                            buffer:
                                type: str
                                description: 'Message string.'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            msg-type:
                                type: str
                                description: 'Message type.'
                    device-detection-portal:
                        -
                            buffer:
                                type: str
                                description: 'Message string.'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            msg-type:
                                type: str
                                description: 'Message type.'
                    ec:
                        -
                            buffer:
                                type: str
                                description: 'Message string.'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            msg-type:
                                type: str
                                description: 'Message type.'
                    fortiguard-wf:
                        -
                            buffer:
                                type: str
                                description: 'Message string.'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            msg-type:
                                type: str
                                description: 'Message type.'
                    ftp:
                        -
                            buffer:
                                type: str
                                description: 'Message string.'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            msg-type:
                                type: str
                                description: 'Message type.'
                    group-type:
                        type: str
                        description: 'Group type.'
                        choices:
                            - 'default'
                            - 'utm'
                            - 'auth'
                            - 'ec'
                            - 'captive-portal'
                    http:
                        -
                            buffer:
                                type: str
                                description: 'Message string.'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            msg-type:
                                type: str
                                description: 'Message type.'
                    icap:
                        -
                            buffer:
                                type: str
                                description: 'Message string.'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            msg-type:
                                type: str
                                description: 'Message type.'
                    mail:
                        -
                            buffer:
                                type: str
                                description: 'Message string.'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            msg-type:
                                type: str
                                description: 'Message type.'
                    mm1:
                        -
                            add-smil:
                                type: str
                                description: 'add message encapsulation'
                                choices:
                                    - 'disable'
                                    - 'enable'
                            charset:
                                type: str
                                description: 'character encoding used for replacement message'
                                choices:
                                    - 'us-ascii'
                                    - 'utf-8'
                            class:
                                type: str
                                description: 'message class'
                                choices:
                                    - 'personal'
                                    - 'advertisement'
                                    - 'information'
                                    - 'automatic'
                                    - 'not-included'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            from:
                                type: str
                                description: 'from address'
                            from-sender:
                                type: str
                                description: 'notification message sent from recipient'
                                choices:
                                    - 'disable'
                                    - 'enable'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            image:
                                type: str
                                description: 'Message string.'
                            message:
                                type: str
                                description: 'message text'
                            msg-type:
                                type: str
                                description: 'Message type.'
                            priority:
                                type: str
                                description: 'message priority'
                                choices:
                                    - 'low'
                                    - 'normal'
                                    - 'high'
                                    - 'not-included'
                            rsp-status:
                                type: str
                                description: 'response status code'
                                choices:
                                    - 'ok'
                                    - 'err-unspecified'
                                    - 'err-srv-denied'
                                    - 'err-msg-fmt-corrupt'
                                    - 'err-snd-addr-unresolv'
                                    - 'err-msg-not-found'
                                    - 'err-net-prob'
                                    - 'err-content-not-accept'
                                    - 'err-unsupp-msg'
                            rsp-text:
                                type: str
                                description: 'response text'
                            sender-visibility:
                                type: str
                                description: 'sender visibility'
                                choices:
                                    - 'hide'
                                    - 'show'
                                    - 'not-specified'
                            smil-part:
                                type: str
                                description: 'message encapsulation text'
                            subject:
                                type: str
                                description: 'subject text string'
                    mm3:
                        -
                            add-html:
                                type: str
                                description: 'add message encapsulation'
                                choices:
                                    - 'disable'
                                    - 'enable'
                            charset:
                                type: str
                                description: 'character encoding used for replacement message'
                                choices:
                                    - 'us-ascii'
                                    - 'utf-8'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            from:
                                type: str
                                description: 'from address'
                            from-sender:
                                type: str
                                description: 'notification message sent from recipient'
                                choices:
                                    - 'disable'
                                    - 'enable'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            html-part:
                                type: str
                                description: 'message encapsulation text'
                            image:
                                type: str
                                description: 'Message string.'
                            message:
                                type: str
                                description: 'message text'
                            msg-type:
                                type: str
                                description: 'Message type.'
                            priority:
                                type: str
                                description: 'message priority'
                                choices:
                                    - 'low'
                                    - 'normal'
                                    - 'high'
                                    - 'not-included'
                            subject:
                                type: str
                                description: 'subject text string'
                    mm4:
                        -
                            add-smil:
                                type: str
                                description: 'add message encapsulation'
                                choices:
                                    - 'disable'
                                    - 'enable'
                            charset:
                                type: str
                                description: 'character encoding used for replacement message'
                                choices:
                                    - 'us-ascii'
                                    - 'utf-8'
                            class:
                                type: str
                                description: 'message class'
                                choices:
                                    - 'personal'
                                    - 'advertisement'
                                    - 'informational'
                                    - 'auto'
                                    - 'not-included'
                            domain:
                                type: str
                                description: 'from address domain'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            from:
                                type: str
                                description: 'from address'
                            from-sender:
                                type: str
                                description: 'notification message sent from recipient'
                                choices:
                                    - 'disable'
                                    - 'enable'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            image:
                                type: str
                                description: 'Message string.'
                            message:
                                type: str
                                description: 'message text'
                            msg-type:
                                type: str
                                description: 'Message type.'
                            priority:
                                type: str
                                description: 'message priority'
                                choices:
                                    - 'low'
                                    - 'normal'
                                    - 'high'
                                    - 'not-included'
                            rsp-status:
                                type: str
                                description: 'response status'
                                choices:
                                    - 'ok'
                                    - 'err-unspecified'
                                    - 'err-srv-denied'
                                    - 'err-msg-fmt-corrupt'
                                    - 'err-snd-addr-unresolv'
                                    - 'err-net-prob'
                                    - 'err-content-not-accept'
                                    - 'err-unsupp-msg'
                            smil-part:
                                type: str
                                description: 'message encapsulation text'
                            subject:
                                type: str
                                description: 'subject text string'
                    mm7:
                        -
                            add-smil:
                                type: str
                                description: 'add message encapsulation'
                                choices:
                                    - 'disable'
                                    - 'enable'
                            addr-type:
                                type: str
                                description: 'from address type'
                                choices:
                                    - 'rfc2822-addr'
                                    - 'number'
                                    - 'short-code'
                            allow-content-adaptation:
                                type: str
                                description: 'allow content adaptations'
                                choices:
                                    - 'disable'
                                    - 'enable'
                            charset:
                                type: str
                                description: 'character encoding used for replacement message'
                                choices:
                                    - 'us-ascii'
                                    - 'utf-8'
                            class:
                                type: str
                                description: 'message class'
                                choices:
                                    - 'personal'
                                    - 'advertisement'
                                    - 'informational'
                                    - 'auto'
                                    - 'not-included'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            from:
                                type: str
                                description: 'from address'
                            from-sender:
                                type: str
                                description: 'notification message sent from recipient'
                                choices:
                                    - 'disable'
                                    - 'enable'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            image:
                                type: str
                                description: 'Message string.'
                            message:
                                type: str
                                description: 'message text'
                            msg-type:
                                type: str
                                description: 'Message type.'
                            priority:
                                type: str
                                description: 'message priority'
                                choices:
                                    - 'low'
                                    - 'normal'
                                    - 'high'
                                    - 'not-included'
                            rsp-status:
                                type: str
                                description: 'response status'
                                choices:
                                    - 'success'
                                    - 'partial-success'
                                    - 'client-err'
                                    - 'oper-restrict'
                                    - 'addr-err'
                                    - 'addr-not-found'
                                    - 'content-refused'
                                    - 'msg-id-not-found'
                                    - 'link-id-not-found'
                                    - 'msg-fmt-corrupt'
                                    - 'app-id-not-found'
                                    - 'repl-app-id-not-found'
                                    - 'srv-err'
                                    - 'not-possible'
                                    - 'msg-rejected'
                                    - 'multiple-addr-not-supp'
                                    - 'app-addr-not-supp'
                                    - 'gen-service-err'
                                    - 'improper-ident'
                                    - 'unsupp-ver'
                                    - 'unsupp-oper'
                                    - 'validation-err'
                                    - 'service-err'
                                    - 'service-unavail'
                                    - 'service-denied'
                                    - 'app-denied'
                            smil-part:
                                type: str
                                description: 'message encapsulation text'
                            subject:
                                type: str
                                description: 'subject text string'
                    mms:
                        -
                            buffer:
                                type: str
                                description: 'Message string.'
                            charset:
                                type: str
                                description: 'character encoding used for replacement message'
                                choices:
                                    - 'us-ascii'
                                    - 'utf-8'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            image:
                                type: str
                                description: 'Message string.'
                            msg-type:
                                type: str
                                description: 'Message type.'
                    nac-quar:
                        -
                            buffer:
                                type: str
                                description: 'Message string.'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            msg-type:
                                type: str
                                description: 'Message type.'
                    name:
                        type: str
                        description: 'Group name.'
                    nntp:
                        -
                            buffer:
                                type: str
                                description: 'Message string.'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            msg-type:
                                type: str
                                description: 'Message type.'
                    spam:
                        -
                            buffer:
                                type: str
                                description: 'Message string.'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            msg-type:
                                type: str
                                description: 'Message type.'
                    sslvpn:
                        -
                            buffer:
                                type: str
                                description: 'Message string.'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            msg-type:
                                type: str
                                description: 'Message type.'
                    traffic-quota:
                        -
                            buffer:
                                type: str
                                description: 'Message string.'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            msg-type:
                                type: str
                                description: 'Message type.'
                    utm:
                        -
                            buffer:
                                type: str
                                description: 'Message string.'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            msg-type:
                                type: str
                                description: 'Message type.'
                    webproxy:
                        -
                            buffer:
                                type: str
                                description: 'Message string.'
                            format:
                                type: str
                                description: 'Format flag.'
                                choices:
                                    - 'none'
                                    - 'text'
                                    - 'html'
                                    - 'wml'
                            header:
                                type: str
                                description: 'Header flag.'
                                choices:
                                    - 'none'
                                    - 'http'
                                    - '8bit'
                            msg-type:
                                type: str
                                description: 'Message type.'
    schema_object1:
        methods: [get]
        description: 'Configure replacement message groups.'
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
                            - 'comment'
                            - 'group-type'
                            - 'name'
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

    - name: REQUESTING /PM/CONFIG/OBJ/SYSTEM/REPLACEMSG-GROUP
      fmgr_system_replacemsggroup:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     admin:
                       -
                           buffer: <value of string>
                           format: <value in [none, text, html, ...]>
                           header: <value in [none, http, 8bit]>
                           msg-type: <value of string>
                     alertmail:
                       -
                           buffer: <value of string>
                           format: <value in [none, text, html, ...]>
                           header: <value in [none, http, 8bit]>
                           msg-type: <value of string>
                     auth:
                       -
                           buffer: <value of string>
                           format: <value in [none, text, html, ...]>
                           header: <value in [none, http, 8bit]>
                           msg-type: <value of string>
                     comment: <value of string>
                     custom-message:
                       -
                           buffer: <value of string>
                           format: <value in [none, text, html, ...]>
                           header: <value in [none, http, 8bit]>
                           msg-type: <value of string>
                     device-detection-portal:
                       -
                           buffer: <value of string>
                           format: <value in [none, text, html, ...]>
                           header: <value in [none, http, 8bit]>
                           msg-type: <value of string>
                     ec:
                       -
                           buffer: <value of string>
                           format: <value in [none, text, html, ...]>
                           header: <value in [none, http, 8bit]>
                           msg-type: <value of string>
                     fortiguard-wf:
                       -
                           buffer: <value of string>
                           format: <value in [none, text, html, ...]>
                           header: <value in [none, http, 8bit]>
                           msg-type: <value of string>
                     ftp:
                       -
                           buffer: <value of string>
                           format: <value in [none, text, html, ...]>
                           header: <value in [none, http, 8bit]>
                           msg-type: <value of string>
                     group-type: <value in [default, utm, auth, ...]>
                     http:
                       -
                           buffer: <value of string>
                           format: <value in [none, text, html, ...]>
                           header: <value in [none, http, 8bit]>
                           msg-type: <value of string>
                     icap:
                       -
                           buffer: <value of string>
                           format: <value in [none, text, html, ...]>
                           header: <value in [none, http, 8bit]>
                           msg-type: <value of string>
                     mail:
                       -
                           buffer: <value of string>
                           format: <value in [none, text, html, ...]>
                           header: <value in [none, http, 8bit]>
                           msg-type: <value of string>
                     mm1:
                       -
                           add-smil: <value in [disable, enable]>
                           charset: <value in [us-ascii, utf-8]>
                           class: <value in [personal, advertisement, information, ...]>
                           format: <value in [none, text, html, ...]>
                           from: <value of string>
                           from-sender: <value in [disable, enable]>
                           header: <value in [none, http, 8bit]>
                           image: <value of string>
                           message: <value of string>
                           msg-type: <value of string>
                           priority: <value in [low, normal, high, ...]>
                           rsp-status: <value in [ok, err-unspecified, err-srv-denied, ...]>
                           rsp-text: <value of string>
                           sender-visibility: <value in [hide, show, not-specified]>
                           smil-part: <value of string>
                           subject: <value of string>
                     mm3:
                       -
                           add-html: <value in [disable, enable]>
                           charset: <value in [us-ascii, utf-8]>
                           format: <value in [none, text, html, ...]>
                           from: <value of string>
                           from-sender: <value in [disable, enable]>
                           header: <value in [none, http, 8bit]>
                           html-part: <value of string>
                           image: <value of string>
                           message: <value of string>
                           msg-type: <value of string>
                           priority: <value in [low, normal, high, ...]>
                           subject: <value of string>
                     mm4:
                       -
                           add-smil: <value in [disable, enable]>
                           charset: <value in [us-ascii, utf-8]>
                           class: <value in [personal, advertisement, informational, ...]>
                           domain: <value of string>
                           format: <value in [none, text, html, ...]>
                           from: <value of string>
                           from-sender: <value in [disable, enable]>
                           header: <value in [none, http, 8bit]>
                           image: <value of string>
                           message: <value of string>
                           msg-type: <value of string>
                           priority: <value in [low, normal, high, ...]>
                           rsp-status: <value in [ok, err-unspecified, err-srv-denied, ...]>
                           smil-part: <value of string>
                           subject: <value of string>
                     mm7:
                       -
                           add-smil: <value in [disable, enable]>
                           addr-type: <value in [rfc2822-addr, number, short-code]>
                           allow-content-adaptation: <value in [disable, enable]>
                           charset: <value in [us-ascii, utf-8]>
                           class: <value in [personal, advertisement, informational, ...]>
                           format: <value in [none, text, html, ...]>
                           from: <value of string>
                           from-sender: <value in [disable, enable]>
                           header: <value in [none, http, 8bit]>
                           image: <value of string>
                           message: <value of string>
                           msg-type: <value of string>
                           priority: <value in [low, normal, high, ...]>
                           rsp-status: <value in [success, partial-success, client-err, ...]>
                           smil-part: <value of string>
                           subject: <value of string>
                     mms:
                       -
                           buffer: <value of string>
                           charset: <value in [us-ascii, utf-8]>
                           format: <value in [none, text, html, ...]>
                           header: <value in [none, http, 8bit]>
                           image: <value of string>
                           msg-type: <value of string>
                     nac-quar:
                       -
                           buffer: <value of string>
                           format: <value in [none, text, html, ...]>
                           header: <value in [none, http, 8bit]>
                           msg-type: <value of string>
                     name: <value of string>
                     nntp:
                       -
                           buffer: <value of string>
                           format: <value in [none, text, html, ...]>
                           header: <value in [none, http, 8bit]>
                           msg-type: <value of string>
                     spam:
                       -
                           buffer: <value of string>
                           format: <value in [none, text, html, ...]>
                           header: <value in [none, http, 8bit]>
                           msg-type: <value of string>
                     sslvpn:
                       -
                           buffer: <value of string>
                           format: <value in [none, text, html, ...]>
                           header: <value in [none, http, 8bit]>
                           msg-type: <value of string>
                     traffic-quota:
                       -
                           buffer: <value of string>
                           format: <value in [none, text, html, ...]>
                           header: <value in [none, http, 8bit]>
                           msg-type: <value of string>
                     utm:
                       -
                           buffer: <value of string>
                           format: <value in [none, text, html, ...]>
                           header: <value in [none, http, 8bit]>
                           msg-type: <value of string>
                     webproxy:
                       -
                           buffer: <value of string>
                           format: <value in [none, text, html, ...]>
                           header: <value in [none, http, 8bit]>
                           msg-type: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/SYSTEM/REPLACEMSG-GROUP
      fmgr_system_replacemsggroup:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [comment, group-type, name]>
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
            example: '/pm/config/adom/{adom}/obj/system/replacemsg-group'
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
               admin:
                  type: array
                  suboptions:
                     buffer:
                        type: str
                        description: 'Message string.'
                     format:
                        type: str
                        description: 'Format flag.'
                     header:
                        type: str
                        description: 'Header flag.'
                     msg-type:
                        type: str
                        description: 'Message type.'
               alertmail:
                  type: array
                  suboptions:
                     buffer:
                        type: str
                        description: 'Message string.'
                     format:
                        type: str
                        description: 'Format flag.'
                     header:
                        type: str
                        description: 'Header flag.'
                     msg-type:
                        type: str
                        description: 'Message type.'
               auth:
                  type: array
                  suboptions:
                     buffer:
                        type: str
                        description: 'Message string.'
                     format:
                        type: str
                        description: 'Format flag.'
                     header:
                        type: str
                        description: 'Header flag.'
                     msg-type:
                        type: str
                        description: 'Message type.'
               comment:
                  type: str
                  description: 'Comment.'
               custom-message:
                  type: array
                  suboptions:
                     buffer:
                        type: str
                        description: 'Message string.'
                     format:
                        type: str
                        description: 'Format flag.'
                     header:
                        type: str
                        description: 'Header flag.'
                     msg-type:
                        type: str
                        description: 'Message type.'
               device-detection-portal:
                  type: array
                  suboptions:
                     buffer:
                        type: str
                        description: 'Message string.'
                     format:
                        type: str
                        description: 'Format flag.'
                     header:
                        type: str
                        description: 'Header flag.'
                     msg-type:
                        type: str
                        description: 'Message type.'
               ec:
                  type: array
                  suboptions:
                     buffer:
                        type: str
                        description: 'Message string.'
                     format:
                        type: str
                        description: 'Format flag.'
                     header:
                        type: str
                        description: 'Header flag.'
                     msg-type:
                        type: str
                        description: 'Message type.'
               fortiguard-wf:
                  type: array
                  suboptions:
                     buffer:
                        type: str
                        description: 'Message string.'
                     format:
                        type: str
                        description: 'Format flag.'
                     header:
                        type: str
                        description: 'Header flag.'
                     msg-type:
                        type: str
                        description: 'Message type.'
               ftp:
                  type: array
                  suboptions:
                     buffer:
                        type: str
                        description: 'Message string.'
                     format:
                        type: str
                        description: 'Format flag.'
                     header:
                        type: str
                        description: 'Header flag.'
                     msg-type:
                        type: str
                        description: 'Message type.'
               group-type:
                  type: str
                  description: 'Group type.'
               http:
                  type: array
                  suboptions:
                     buffer:
                        type: str
                        description: 'Message string.'
                     format:
                        type: str
                        description: 'Format flag.'
                     header:
                        type: str
                        description: 'Header flag.'
                     msg-type:
                        type: str
                        description: 'Message type.'
               icap:
                  type: array
                  suboptions:
                     buffer:
                        type: str
                        description: 'Message string.'
                     format:
                        type: str
                        description: 'Format flag.'
                     header:
                        type: str
                        description: 'Header flag.'
                     msg-type:
                        type: str
                        description: 'Message type.'
               mail:
                  type: array
                  suboptions:
                     buffer:
                        type: str
                        description: 'Message string.'
                     format:
                        type: str
                        description: 'Format flag.'
                     header:
                        type: str
                        description: 'Header flag.'
                     msg-type:
                        type: str
                        description: 'Message type.'
               mm1:
                  type: array
                  suboptions:
                     add-smil:
                        type: str
                        description: 'add message encapsulation'
                     charset:
                        type: str
                        description: 'character encoding used for replacement message'
                     class:
                        type: str
                        description: 'message class'
                     format:
                        type: str
                        description: 'Format flag.'
                     from:
                        type: str
                        description: 'from address'
                     from-sender:
                        type: str
                        description: 'notification message sent from recipient'
                     header:
                        type: str
                        description: 'Header flag.'
                     image:
                        type: str
                        description: 'Message string.'
                     message:
                        type: str
                        description: 'message text'
                     msg-type:
                        type: str
                        description: 'Message type.'
                     priority:
                        type: str
                        description: 'message priority'
                     rsp-status:
                        type: str
                        description: 'response status code'
                     rsp-text:
                        type: str
                        description: 'response text'
                     sender-visibility:
                        type: str
                        description: 'sender visibility'
                     smil-part:
                        type: str
                        description: 'message encapsulation text'
                     subject:
                        type: str
                        description: 'subject text string'
               mm3:
                  type: array
                  suboptions:
                     add-html:
                        type: str
                        description: 'add message encapsulation'
                     charset:
                        type: str
                        description: 'character encoding used for replacement message'
                     format:
                        type: str
                        description: 'Format flag.'
                     from:
                        type: str
                        description: 'from address'
                     from-sender:
                        type: str
                        description: 'notification message sent from recipient'
                     header:
                        type: str
                        description: 'Header flag.'
                     html-part:
                        type: str
                        description: 'message encapsulation text'
                     image:
                        type: str
                        description: 'Message string.'
                     message:
                        type: str
                        description: 'message text'
                     msg-type:
                        type: str
                        description: 'Message type.'
                     priority:
                        type: str
                        description: 'message priority'
                     subject:
                        type: str
                        description: 'subject text string'
               mm4:
                  type: array
                  suboptions:
                     add-smil:
                        type: str
                        description: 'add message encapsulation'
                     charset:
                        type: str
                        description: 'character encoding used for replacement message'
                     class:
                        type: str
                        description: 'message class'
                     domain:
                        type: str
                        description: 'from address domain'
                     format:
                        type: str
                        description: 'Format flag.'
                     from:
                        type: str
                        description: 'from address'
                     from-sender:
                        type: str
                        description: 'notification message sent from recipient'
                     header:
                        type: str
                        description: 'Header flag.'
                     image:
                        type: str
                        description: 'Message string.'
                     message:
                        type: str
                        description: 'message text'
                     msg-type:
                        type: str
                        description: 'Message type.'
                     priority:
                        type: str
                        description: 'message priority'
                     rsp-status:
                        type: str
                        description: 'response status'
                     smil-part:
                        type: str
                        description: 'message encapsulation text'
                     subject:
                        type: str
                        description: 'subject text string'
               mm7:
                  type: array
                  suboptions:
                     add-smil:
                        type: str
                        description: 'add message encapsulation'
                     addr-type:
                        type: str
                        description: 'from address type'
                     allow-content-adaptation:
                        type: str
                        description: 'allow content adaptations'
                     charset:
                        type: str
                        description: 'character encoding used for replacement message'
                     class:
                        type: str
                        description: 'message class'
                     format:
                        type: str
                        description: 'Format flag.'
                     from:
                        type: str
                        description: 'from address'
                     from-sender:
                        type: str
                        description: 'notification message sent from recipient'
                     header:
                        type: str
                        description: 'Header flag.'
                     image:
                        type: str
                        description: 'Message string.'
                     message:
                        type: str
                        description: 'message text'
                     msg-type:
                        type: str
                        description: 'Message type.'
                     priority:
                        type: str
                        description: 'message priority'
                     rsp-status:
                        type: str
                        description: 'response status'
                     smil-part:
                        type: str
                        description: 'message encapsulation text'
                     subject:
                        type: str
                        description: 'subject text string'
               mms:
                  type: array
                  suboptions:
                     buffer:
                        type: str
                        description: 'Message string.'
                     charset:
                        type: str
                        description: 'character encoding used for replacement message'
                     format:
                        type: str
                        description: 'Format flag.'
                     header:
                        type: str
                        description: 'Header flag.'
                     image:
                        type: str
                        description: 'Message string.'
                     msg-type:
                        type: str
                        description: 'Message type.'
               nac-quar:
                  type: array
                  suboptions:
                     buffer:
                        type: str
                        description: 'Message string.'
                     format:
                        type: str
                        description: 'Format flag.'
                     header:
                        type: str
                        description: 'Header flag.'
                     msg-type:
                        type: str
                        description: 'Message type.'
               name:
                  type: str
                  description: 'Group name.'
               nntp:
                  type: array
                  suboptions:
                     buffer:
                        type: str
                        description: 'Message string.'
                     format:
                        type: str
                        description: 'Format flag.'
                     header:
                        type: str
                        description: 'Header flag.'
                     msg-type:
                        type: str
                        description: 'Message type.'
               spam:
                  type: array
                  suboptions:
                     buffer:
                        type: str
                        description: 'Message string.'
                     format:
                        type: str
                        description: 'Format flag.'
                     header:
                        type: str
                        description: 'Header flag.'
                     msg-type:
                        type: str
                        description: 'Message type.'
               sslvpn:
                  type: array
                  suboptions:
                     buffer:
                        type: str
                        description: 'Message string.'
                     format:
                        type: str
                        description: 'Format flag.'
                     header:
                        type: str
                        description: 'Header flag.'
                     msg-type:
                        type: str
                        description: 'Message type.'
               traffic-quota:
                  type: array
                  suboptions:
                     buffer:
                        type: str
                        description: 'Message string.'
                     format:
                        type: str
                        description: 'Format flag.'
                     header:
                        type: str
                        description: 'Header flag.'
                     msg-type:
                        type: str
                        description: 'Message type.'
               utm:
                  type: array
                  suboptions:
                     buffer:
                        type: str
                        description: 'Message string.'
                     format:
                        type: str
                        description: 'Format flag.'
                     header:
                        type: str
                        description: 'Header flag.'
                     msg-type:
                        type: str
                        description: 'Message type.'
               webproxy:
                  type: array
                  suboptions:
                     buffer:
                        type: str
                        description: 'Message string.'
                     format:
                        type: str
                        description: 'Format flag.'
                     header:
                        type: str
                        description: 'Header flag.'
                     msg-type:
                        type: str
                        description: 'Message type.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/system/replacemsg-group'

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
        '/pm/config/adom/{adom}/obj/system/replacemsg-group',
        '/pm/config/global/obj/system/replacemsg-group'
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
                        'admin': {
                            'type': 'array',
                            'items': {
                                'buffer': {
                                    'type': 'string'
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'msg-type': {
                                    'type': 'string'
                                }
                            }
                        },
                        'alertmail': {
                            'type': 'array',
                            'items': {
                                'buffer': {
                                    'type': 'string'
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'msg-type': {
                                    'type': 'string'
                                }
                            }
                        },
                        'auth': {
                            'type': 'array',
                            'items': {
                                'buffer': {
                                    'type': 'string'
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'msg-type': {
                                    'type': 'string'
                                }
                            }
                        },
                        'comment': {
                            'type': 'string'
                        },
                        'custom-message': {
                            'type': 'array',
                            'items': {
                                'buffer': {
                                    'type': 'string'
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'msg-type': {
                                    'type': 'string'
                                }
                            }
                        },
                        'device-detection-portal': {
                            'type': 'array',
                            'items': {
                                'buffer': {
                                    'type': 'string'
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'msg-type': {
                                    'type': 'string'
                                }
                            }
                        },
                        'ec': {
                            'type': 'array',
                            'items': {
                                'buffer': {
                                    'type': 'string'
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'msg-type': {
                                    'type': 'string'
                                }
                            }
                        },
                        'fortiguard-wf': {
                            'type': 'array',
                            'items': {
                                'buffer': {
                                    'type': 'string'
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'msg-type': {
                                    'type': 'string'
                                }
                            }
                        },
                        'ftp': {
                            'type': 'array',
                            'items': {
                                'buffer': {
                                    'type': 'string'
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'msg-type': {
                                    'type': 'string'
                                }
                            }
                        },
                        'group-type': {
                            'type': 'string',
                            'enum': [
                                'default',
                                'utm',
                                'auth',
                                'ec',
                                'captive-portal'
                            ]
                        },
                        'http': {
                            'type': 'array',
                            'items': {
                                'buffer': {
                                    'type': 'string'
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'msg-type': {
                                    'type': 'string'
                                }
                            }
                        },
                        'icap': {
                            'type': 'array',
                            'items': {
                                'buffer': {
                                    'type': 'string'
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'msg-type': {
                                    'type': 'string'
                                }
                            }
                        },
                        'mail': {
                            'type': 'array',
                            'items': {
                                'buffer': {
                                    'type': 'string'
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'msg-type': {
                                    'type': 'string'
                                }
                            }
                        },
                        'mm1': {
                            'type': 'array',
                            'items': {
                                'add-smil': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'charset': {
                                    'type': 'string',
                                    'enum': [
                                        'us-ascii',
                                        'utf-8'
                                    ]
                                },
                                'class': {
                                    'type': 'string',
                                    'enum': [
                                        'personal',
                                        'advertisement',
                                        'information',
                                        'automatic',
                                        'not-included'
                                    ]
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'from': {
                                    'type': 'string'
                                },
                                'from-sender': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'image': {
                                    'type': 'string'
                                },
                                'message': {
                                    'type': 'string'
                                },
                                'msg-type': {
                                    'type': 'string'
                                },
                                'priority': {
                                    'type': 'string',
                                    'enum': [
                                        'low',
                                        'normal',
                                        'high',
                                        'not-included'
                                    ]
                                },
                                'rsp-status': {
                                    'type': 'string',
                                    'enum': [
                                        'ok',
                                        'err-unspecified',
                                        'err-srv-denied',
                                        'err-msg-fmt-corrupt',
                                        'err-snd-addr-unresolv',
                                        'err-msg-not-found',
                                        'err-net-prob',
                                        'err-content-not-accept',
                                        'err-unsupp-msg'
                                    ]
                                },
                                'rsp-text': {
                                    'type': 'string'
                                },
                                'sender-visibility': {
                                    'type': 'string',
                                    'enum': [
                                        'hide',
                                        'show',
                                        'not-specified'
                                    ]
                                },
                                'smil-part': {
                                    'type': 'string'
                                },
                                'subject': {
                                    'type': 'string'
                                }
                            }
                        },
                        'mm3': {
                            'type': 'array',
                            'items': {
                                'add-html': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'charset': {
                                    'type': 'string',
                                    'enum': [
                                        'us-ascii',
                                        'utf-8'
                                    ]
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'from': {
                                    'type': 'string'
                                },
                                'from-sender': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'html-part': {
                                    'type': 'string'
                                },
                                'image': {
                                    'type': 'string'
                                },
                                'message': {
                                    'type': 'string'
                                },
                                'msg-type': {
                                    'type': 'string'
                                },
                                'priority': {
                                    'type': 'string',
                                    'enum': [
                                        'low',
                                        'normal',
                                        'high',
                                        'not-included'
                                    ]
                                },
                                'subject': {
                                    'type': 'string'
                                }
                            }
                        },
                        'mm4': {
                            'type': 'array',
                            'items': {
                                'add-smil': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'charset': {
                                    'type': 'string',
                                    'enum': [
                                        'us-ascii',
                                        'utf-8'
                                    ]
                                },
                                'class': {
                                    'type': 'string',
                                    'enum': [
                                        'personal',
                                        'advertisement',
                                        'informational',
                                        'auto',
                                        'not-included'
                                    ]
                                },
                                'domain': {
                                    'type': 'string'
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'from': {
                                    'type': 'string'
                                },
                                'from-sender': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'image': {
                                    'type': 'string'
                                },
                                'message': {
                                    'type': 'string'
                                },
                                'msg-type': {
                                    'type': 'string'
                                },
                                'priority': {
                                    'type': 'string',
                                    'enum': [
                                        'low',
                                        'normal',
                                        'high',
                                        'not-included'
                                    ]
                                },
                                'rsp-status': {
                                    'type': 'string',
                                    'enum': [
                                        'ok',
                                        'err-unspecified',
                                        'err-srv-denied',
                                        'err-msg-fmt-corrupt',
                                        'err-snd-addr-unresolv',
                                        'err-net-prob',
                                        'err-content-not-accept',
                                        'err-unsupp-msg'
                                    ]
                                },
                                'smil-part': {
                                    'type': 'string'
                                },
                                'subject': {
                                    'type': 'string'
                                }
                            }
                        },
                        'mm7': {
                            'type': 'array',
                            'items': {
                                'add-smil': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'addr-type': {
                                    'type': 'string',
                                    'enum': [
                                        'rfc2822-addr',
                                        'number',
                                        'short-code'
                                    ]
                                },
                                'allow-content-adaptation': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'charset': {
                                    'type': 'string',
                                    'enum': [
                                        'us-ascii',
                                        'utf-8'
                                    ]
                                },
                                'class': {
                                    'type': 'string',
                                    'enum': [
                                        'personal',
                                        'advertisement',
                                        'informational',
                                        'auto',
                                        'not-included'
                                    ]
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'from': {
                                    'type': 'string'
                                },
                                'from-sender': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'image': {
                                    'type': 'string'
                                },
                                'message': {
                                    'type': 'string'
                                },
                                'msg-type': {
                                    'type': 'string'
                                },
                                'priority': {
                                    'type': 'string',
                                    'enum': [
                                        'low',
                                        'normal',
                                        'high',
                                        'not-included'
                                    ]
                                },
                                'rsp-status': {
                                    'type': 'string',
                                    'enum': [
                                        'success',
                                        'partial-success',
                                        'client-err',
                                        'oper-restrict',
                                        'addr-err',
                                        'addr-not-found',
                                        'content-refused',
                                        'msg-id-not-found',
                                        'link-id-not-found',
                                        'msg-fmt-corrupt',
                                        'app-id-not-found',
                                        'repl-app-id-not-found',
                                        'srv-err',
                                        'not-possible',
                                        'msg-rejected',
                                        'multiple-addr-not-supp',
                                        'app-addr-not-supp',
                                        'gen-service-err',
                                        'improper-ident',
                                        'unsupp-ver',
                                        'unsupp-oper',
                                        'validation-err',
                                        'service-err',
                                        'service-unavail',
                                        'service-denied',
                                        'app-denied'
                                    ]
                                },
                                'smil-part': {
                                    'type': 'string'
                                },
                                'subject': {
                                    'type': 'string'
                                }
                            }
                        },
                        'mms': {
                            'type': 'array',
                            'items': {
                                'buffer': {
                                    'type': 'string'
                                },
                                'charset': {
                                    'type': 'string',
                                    'enum': [
                                        'us-ascii',
                                        'utf-8'
                                    ]
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'image': {
                                    'type': 'string'
                                },
                                'msg-type': {
                                    'type': 'string'
                                }
                            }
                        },
                        'nac-quar': {
                            'type': 'array',
                            'items': {
                                'buffer': {
                                    'type': 'string'
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'msg-type': {
                                    'type': 'string'
                                }
                            }
                        },
                        'name': {
                            'type': 'string'
                        },
                        'nntp': {
                            'type': 'array',
                            'items': {
                                'buffer': {
                                    'type': 'string'
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'msg-type': {
                                    'type': 'string'
                                }
                            }
                        },
                        'spam': {
                            'type': 'array',
                            'items': {
                                'buffer': {
                                    'type': 'string'
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'msg-type': {
                                    'type': 'string'
                                }
                            }
                        },
                        'sslvpn': {
                            'type': 'array',
                            'items': {
                                'buffer': {
                                    'type': 'string'
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'msg-type': {
                                    'type': 'string'
                                }
                            }
                        },
                        'traffic-quota': {
                            'type': 'array',
                            'items': {
                                'buffer': {
                                    'type': 'string'
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'msg-type': {
                                    'type': 'string'
                                }
                            }
                        },
                        'utm': {
                            'type': 'array',
                            'items': {
                                'buffer': {
                                    'type': 'string'
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'msg-type': {
                                    'type': 'string'
                                }
                            }
                        },
                        'webproxy': {
                            'type': 'array',
                            'items': {
                                'buffer': {
                                    'type': 'string'
                                },
                                'format': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'text',
                                        'html',
                                        'wml'
                                    ]
                                },
                                'header': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'http',
                                        '8bit'
                                    ]
                                },
                                'msg-type': {
                                    'type': 'string'
                                }
                            }
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
                                'comment',
                                'group-type',
                                'name'
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
