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
module: fmgr_gtp_messagefilterv0v1_obj
short_description: Message filter for GTPv0/v1 messages.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/gtp/message-filter-v0v1/{message-filter-v0v1}
    - /pm/config/global/obj/gtp/message-filter-v0v1/{message-filter-v0v1}
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
            adom:
                type: str
                description: the domain prefix, the none and global are reserved
                choices:
                  - none
                  - global
                  - custom dom
            message-filter-v0v1:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Message filter for GTPv0/v1 messages.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                create-mbms:
                    type: str
                    description: 'GTPv1 create MBMS context (req 100, resp 101).'
                    choices:
                        - 'allow'
                        - 'deny'
                create-pdp:
                    type: str
                    description: 'Create PDP context (req 16, resp 17).'
                    choices:
                        - 'allow'
                        - 'deny'
                data-record:
                    type: str
                    description: 'Data record transfer (req 240, resp 241).'
                    choices:
                        - 'allow'
                        - 'deny'
                delete-aa-pdp:
                    type: str
                    description: 'GTPv0 delete AA PDP context (req 24, resp 25).'
                    choices:
                        - 'allow'
                        - 'deny'
                delete-mbms:
                    type: str
                    description: 'GTPv1 delete MBMS context (req 104, resp 105).'
                    choices:
                        - 'allow'
                        - 'deny'
                delete-pdp:
                    type: str
                    description: 'Delete PDP context (req 20, resp 21).'
                    choices:
                        - 'allow'
                        - 'deny'
                echo:
                    type: str
                    description: 'Echo (req 1, resp 2).'
                    choices:
                        - 'allow'
                        - 'deny'
                end-marker:
                    type: str
                    description: 'GTPv1 End marker (254).'
                    choices:
                        - 'allow'
                        - 'deny'
                error-indication:
                    type: str
                    description: 'Error indication (26).'
                    choices:
                        - 'allow'
                        - 'deny'
                failure-report:
                    type: str
                    description: 'Failure report (req 34, resp 35).'
                    choices:
                        - 'allow'
                        - 'deny'
                fwd-relocation:
                    type: str
                    description: 'GTPv1 forward relocation (req 53, resp 54, complete 55, complete ack 59).'
                    choices:
                        - 'allow'
                        - 'deny'
                fwd-srns-context:
                    type: str
                    description: 'GTPv1 forward SRNS (context 58, context ack 60).'
                    choices:
                        - 'allow'
                        - 'deny'
                gtp-pdu:
                    type: str
                    description: 'PDU (255).'
                    choices:
                        - 'allow'
                        - 'deny'
                identification:
                    type: str
                    description: 'Identification (req 48, resp 49).'
                    choices:
                        - 'allow'
                        - 'deny'
                mbms-de-registration:
                    type: str
                    description: 'GTPv1 MBMS de-registration (req 114, resp 115).'
                    choices:
                        - 'allow'
                        - 'deny'
                mbms-notification:
                    type: str
                    description: 'GTPv1 MBMS notification (req 96, resp 97, reject req 98. reject resp 99).'
                    choices:
                        - 'allow'
                        - 'deny'
                mbms-registration:
                    type: str
                    description: 'GTPv1 MBMS registration (req 112, resp 113).'
                    choices:
                        - 'allow'
                        - 'deny'
                mbms-session-start:
                    type: str
                    description: 'GTPv1 MBMS session start (req 116, resp 117).'
                    choices:
                        - 'allow'
                        - 'deny'
                mbms-session-stop:
                    type: str
                    description: 'GTPv1 MBMS session stop (req 118, resp 119).'
                    choices:
                        - 'allow'
                        - 'deny'
                mbms-session-update:
                    type: str
                    description: 'GTPv1 MBMS session update (req 120, resp 121).'
                    choices:
                        - 'allow'
                        - 'deny'
                ms-info-change-notif:
                    type: str
                    description: 'GTPv1 MS info change notification (req 128, resp 129).'
                    choices:
                        - 'allow'
                        - 'deny'
                name:
                    type: str
                    description: 'Message filter name.'
                node-alive:
                    type: str
                    description: 'Node alive (req 4, resp 5).'
                    choices:
                        - 'allow'
                        - 'deny'
                note-ms-present:
                    type: str
                    description: 'Note MS GPRS present (req 36, resp 37).'
                    choices:
                        - 'allow'
                        - 'deny'
                pdu-notification:
                    type: str
                    description: 'PDU notification (req 27, resp 28, reject req 29, reject resp 30).'
                    choices:
                        - 'allow'
                        - 'deny'
                ran-info:
                    type: str
                    description: 'GTPv1 RAN information relay (70).'
                    choices:
                        - 'allow'
                        - 'deny'
                redirection:
                    type: str
                    description: 'Redirection (req 6, resp 7).'
                    choices:
                        - 'allow'
                        - 'deny'
                relocation-cancel:
                    type: str
                    description: 'GTPv1 relocation cancel (req 56, resp 57).'
                    choices:
                        - 'allow'
                        - 'deny'
                send-route:
                    type: str
                    description: 'Send routing information for GPRS (req 32, resp 33).'
                    choices:
                        - 'allow'
                        - 'deny'
                sgsn-context:
                    type: str
                    description: 'SGSN context (req 50, resp 51, ack 52).'
                    choices:
                        - 'allow'
                        - 'deny'
                support-extension:
                    type: str
                    description: 'GTPv1 supported extension headers notify (31).'
                    choices:
                        - 'allow'
                        - 'deny'
                unknown-message:
                    type: str
                    description: 'Allow or Deny unknown messages.'
                    choices:
                        - 'allow'
                        - 'deny'
                unknown-message-white-list:
                    -
                        type: int
                update-mbms:
                    type: str
                    description: 'GTPv1 update MBMS context (req 102, resp 103).'
                    choices:
                        - 'allow'
                        - 'deny'
                update-pdp:
                    type: str
                    description: 'Update PDP context (req 18, resp 19).'
                    choices:
                        - 'allow'
                        - 'deny'
                v0-create-aa-pdp--v1-init-pdp-ctx:
                    type: str
                    description: 'GTPv0 create AA PDP context (req 22, resp 23); Or GTPv1 initiate PDP context (req 22, resp 23).'
                    choices:
                        - 'deny'
                        - 'allow'
                version-not-support:
                    type: str
                    description: 'Version not supported (3).'
                    choices:
                        - 'allow'
                        - 'deny'
    schema_object1:
        methods: [delete]
        description: 'Message filter for GTPv0/v1 messages.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Message filter for GTPv0/v1 messages.'
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
                    - 'datasrc'

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

    - name: REQUESTING /PM/CONFIG/OBJ/GTP/MESSAGE-FILTER-V0V1/{MESSAGE-FILTER-V0V1}
      fmgr_gtp_messagefilterv0v1_obj:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            message-filter-v0v1: <value of string>
         params:
            -
               data:
                  create-mbms: <value in [allow, deny]>
                  create-pdp: <value in [allow, deny]>
                  data-record: <value in [allow, deny]>
                  delete-aa-pdp: <value in [allow, deny]>
                  delete-mbms: <value in [allow, deny]>
                  delete-pdp: <value in [allow, deny]>
                  echo: <value in [allow, deny]>
                  end-marker: <value in [allow, deny]>
                  error-indication: <value in [allow, deny]>
                  failure-report: <value in [allow, deny]>
                  fwd-relocation: <value in [allow, deny]>
                  fwd-srns-context: <value in [allow, deny]>
                  gtp-pdu: <value in [allow, deny]>
                  identification: <value in [allow, deny]>
                  mbms-de-registration: <value in [allow, deny]>
                  mbms-notification: <value in [allow, deny]>
                  mbms-registration: <value in [allow, deny]>
                  mbms-session-start: <value in [allow, deny]>
                  mbms-session-stop: <value in [allow, deny]>
                  mbms-session-update: <value in [allow, deny]>
                  ms-info-change-notif: <value in [allow, deny]>
                  name: <value of string>
                  node-alive: <value in [allow, deny]>
                  note-ms-present: <value in [allow, deny]>
                  pdu-notification: <value in [allow, deny]>
                  ran-info: <value in [allow, deny]>
                  redirection: <value in [allow, deny]>
                  relocation-cancel: <value in [allow, deny]>
                  send-route: <value in [allow, deny]>
                  sgsn-context: <value in [allow, deny]>
                  support-extension: <value in [allow, deny]>
                  unknown-message: <value in [allow, deny]>
                  unknown-message-white-list:
                    - <value of integer>
                  update-mbms: <value in [allow, deny]>
                  update-pdp: <value in [allow, deny]>
                  v0-create-aa-pdp--v1-init-pdp-ctx: <value in [deny, allow]>
                  version-not-support: <value in [allow, deny]>

    - name: REQUESTING /PM/CONFIG/OBJ/GTP/MESSAGE-FILTER-V0V1/{MESSAGE-FILTER-V0V1}
      fmgr_gtp_messagefilterv0v1_obj:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            message-filter-v0v1: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[clone, delete, set, update]
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
            example: '/pm/config/adom/{adom}/obj/gtp/message-filter-v0v1/{message-filter-v0v1}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            create-mbms:
               type: str
               description: 'GTPv1 create MBMS context (req 100, resp 101).'
            create-pdp:
               type: str
               description: 'Create PDP context (req 16, resp 17).'
            data-record:
               type: str
               description: 'Data record transfer (req 240, resp 241).'
            delete-aa-pdp:
               type: str
               description: 'GTPv0 delete AA PDP context (req 24, resp 25).'
            delete-mbms:
               type: str
               description: 'GTPv1 delete MBMS context (req 104, resp 105).'
            delete-pdp:
               type: str
               description: 'Delete PDP context (req 20, resp 21).'
            echo:
               type: str
               description: 'Echo (req 1, resp 2).'
            end-marker:
               type: str
               description: 'GTPv1 End marker (254).'
            error-indication:
               type: str
               description: 'Error indication (26).'
            failure-report:
               type: str
               description: 'Failure report (req 34, resp 35).'
            fwd-relocation:
               type: str
               description: 'GTPv1 forward relocation (req 53, resp 54, complete 55, complete ack 59).'
            fwd-srns-context:
               type: str
               description: 'GTPv1 forward SRNS (context 58, context ack 60).'
            gtp-pdu:
               type: str
               description: 'PDU (255).'
            identification:
               type: str
               description: 'Identification (req 48, resp 49).'
            mbms-de-registration:
               type: str
               description: 'GTPv1 MBMS de-registration (req 114, resp 115).'
            mbms-notification:
               type: str
               description: 'GTPv1 MBMS notification (req 96, resp 97, reject req 98. reject resp 99).'
            mbms-registration:
               type: str
               description: 'GTPv1 MBMS registration (req 112, resp 113).'
            mbms-session-start:
               type: str
               description: 'GTPv1 MBMS session start (req 116, resp 117).'
            mbms-session-stop:
               type: str
               description: 'GTPv1 MBMS session stop (req 118, resp 119).'
            mbms-session-update:
               type: str
               description: 'GTPv1 MBMS session update (req 120, resp 121).'
            ms-info-change-notif:
               type: str
               description: 'GTPv1 MS info change notification (req 128, resp 129).'
            name:
               type: str
               description: 'Message filter name.'
            node-alive:
               type: str
               description: 'Node alive (req 4, resp 5).'
            note-ms-present:
               type: str
               description: 'Note MS GPRS present (req 36, resp 37).'
            pdu-notification:
               type: str
               description: 'PDU notification (req 27, resp 28, reject req 29, reject resp 30).'
            ran-info:
               type: str
               description: 'GTPv1 RAN information relay (70).'
            redirection:
               type: str
               description: 'Redirection (req 6, resp 7).'
            relocation-cancel:
               type: str
               description: 'GTPv1 relocation cancel (req 56, resp 57).'
            send-route:
               type: str
               description: 'Send routing information for GPRS (req 32, resp 33).'
            sgsn-context:
               type: str
               description: 'SGSN context (req 50, resp 51, ack 52).'
            support-extension:
               type: str
               description: 'GTPv1 supported extension headers notify (31).'
            unknown-message:
               type: str
               description: 'Allow or Deny unknown messages.'
            unknown-message-white-list:
               type: array
               suboptions:
                  type: int
            update-mbms:
               type: str
               description: 'GTPv1 update MBMS context (req 102, resp 103).'
            update-pdp:
               type: str
               description: 'Update PDP context (req 18, resp 19).'
            v0-create-aa-pdp--v1-init-pdp-ctx:
               type: str
               description: 'GTPv0 create AA PDP context (req 22, resp 23); Or GTPv1 initiate PDP context (req 22, resp 23).'
            version-not-support:
               type: str
               description: 'Version not supported (3).'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/gtp/message-filter-v0v1/{message-filter-v0v1}'

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
        '/pm/config/adom/{adom}/obj/gtp/message-filter-v0v1/{message-filter-v0v1}',
        '/pm/config/global/obj/gtp/message-filter-v0v1/{message-filter-v0v1}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'message-filter-v0v1',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'create-mbms': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'create-pdp': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'data-record': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'delete-aa-pdp': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'delete-mbms': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'delete-pdp': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'echo': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'end-marker': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'error-indication': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'failure-report': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'fwd-relocation': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'fwd-srns-context': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'gtp-pdu': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'identification': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'mbms-de-registration': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'mbms-notification': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'mbms-registration': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'mbms-session-start': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'mbms-session-stop': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'mbms-session-update': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'ms-info-change-notif': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'name': {
                            'type': 'string'
                        },
                        'node-alive': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'note-ms-present': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'pdu-notification': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'ran-info': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'redirection': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'relocation-cancel': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'send-route': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'sgsn-context': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'support-extension': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'unknown-message': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'unknown-message-white-list': {
                            'type': 'array',
                            'items': {
                                'type': 'integer'
                            }
                        },
                        'update-mbms': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'update-pdp': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'v0-create-aa-pdp--v1-init-pdp-ctx': {
                            'type': 'string',
                            'enum': [
                                'deny',
                                'allow'
                            ]
                        },
                        'version-not-support': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
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
            ],
            'object1': [
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object2': [
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'object member',
                            'chksum',
                            'datasrc'
                        ]
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
            'clone': 'object0',
            'delete': 'object1',
            'get': 'object2',
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
                'clone',
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
