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
module: fmgr_firewall_gtp_messageratelimit
short_description: Message rate limiting.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/firewall/gtp/{gtp}/message-rate-limit
    - /pm/config/global/obj/firewall/gtp/{gtp}/message-rate-limit
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
            gtp:
                type: str
    schema_object0:
        methods: [get]
        description: 'Message rate limiting.'
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
    schema_object1:
        methods: [set, update]
        description: 'Message rate limiting.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                create-aa-pdp-request:
                    type: int
                    description: 'Rate limit for create AA PDP context request (packets per second).'
                create-aa-pdp-response:
                    type: int
                    description: 'Rate limit for create AA PDP context response (packets per second).'
                create-mbms-request:
                    type: int
                    description: 'Rate limit for create MBMS context request (packets per second).'
                create-mbms-response:
                    type: int
                    description: 'Rate limit for create MBMS context response (packets per second).'
                create-pdp-request:
                    type: int
                    description: 'Rate limit for create PDP context request (packets per second).'
                create-pdp-response:
                    type: int
                    description: 'Rate limit for create PDP context response (packets per second).'
                delete-aa-pdp-request:
                    type: int
                    description: 'Rate limit for delete AA PDP context request (packets per second).'
                delete-aa-pdp-response:
                    type: int
                    description: 'Rate limit for delete AA PDP context response (packets per second).'
                delete-mbms-request:
                    type: int
                    description: 'Rate limit for delete MBMS context request (packets per second).'
                delete-mbms-response:
                    type: int
                    description: 'Rate limit for delete MBMS context response (packets per second).'
                delete-pdp-request:
                    type: int
                    description: 'Rate limit for delete PDP context request (packets per second).'
                delete-pdp-response:
                    type: int
                    description: 'Rate limit for delete PDP context response (packets per second).'
                echo-reponse:
                    type: int
                    description: 'Rate limit for echo response (packets per second).'
                echo-request:
                    type: int
                    description: 'Rate limit for echo requests (packets per second).'
                error-indication:
                    type: int
                    description: 'Rate limit for error indication (packets per second).'
                failure-report-request:
                    type: int
                    description: 'Rate limit for failure report request (packets per second).'
                failure-report-response:
                    type: int
                    description: 'Rate limit for failure report response (packets per second).'
                fwd-reloc-complete-ack:
                    type: int
                    description: 'Rate limit for forward relocation complete acknowledge (packets per second).'
                fwd-relocation-complete:
                    type: int
                    description: 'Rate limit for forward relocation complete (packets per second).'
                fwd-relocation-request:
                    type: int
                    description: 'Rate limit for forward relocation request (packets per second).'
                fwd-relocation-response:
                    type: int
                    description: 'Rate limit for forward relocation response (packets per second).'
                fwd-srns-context:
                    type: int
                    description: 'Rate limit for forward SRNS context (packets per second).'
                fwd-srns-context-ack:
                    type: int
                    description: 'Rate limit for forward SRNS context acknowledge (packets per second).'
                g-pdu:
                    type: int
                    description: 'Rate limit for G-PDU (packets per second).'
                identification-request:
                    type: int
                    description: 'Rate limit for identification request (packets per second).'
                identification-response:
                    type: int
                    description: 'Rate limit for identification response (packets per second).'
                mbms-de-reg-request:
                    type: int
                    description: 'Rate limit for MBMS de-registration request (packets per second).'
                mbms-de-reg-response:
                    type: int
                    description: 'Rate limit for MBMS de-registration response (packets per second).'
                mbms-notify-rej-request:
                    type: int
                    description: 'Rate limit for MBMS notification reject request (packets per second).'
                mbms-notify-rej-response:
                    type: int
                    description: 'Rate limit for MBMS notification reject response (packets per second).'
                mbms-notify-request:
                    type: int
                    description: 'Rate limit for MBMS notification request (packets per second).'
                mbms-notify-response:
                    type: int
                    description: 'Rate limit for MBMS notification response (packets per second).'
                mbms-reg-request:
                    type: int
                    description: 'Rate limit for MBMS registration request (packets per second).'
                mbms-reg-response:
                    type: int
                    description: 'Rate limit for MBMS registration response (packets per second).'
                mbms-ses-start-request:
                    type: int
                    description: 'Rate limit for MBMS session start request (packets per second).'
                mbms-ses-start-response:
                    type: int
                    description: 'Rate limit for MBMS session start response (packets per second).'
                mbms-ses-stop-request:
                    type: int
                    description: 'Rate limit for MBMS session stop request (packets per second).'
                mbms-ses-stop-response:
                    type: int
                    description: 'Rate limit for MBMS session stop response (packets per second).'
                note-ms-request:
                    type: int
                    description: 'Rate limit for note MS GPRS present request (packets per second).'
                note-ms-response:
                    type: int
                    description: 'Rate limit for note MS GPRS present response (packets per second).'
                pdu-notify-rej-request:
                    type: int
                    description: 'Rate limit for PDU notify reject request (packets per second).'
                pdu-notify-rej-response:
                    type: int
                    description: 'Rate limit for PDU notify reject response (packets per second).'
                pdu-notify-request:
                    type: int
                    description: 'Rate limit for PDU notify request (packets per second).'
                pdu-notify-response:
                    type: int
                    description: 'Rate limit for PDU notify response (packets per second).'
                ran-info:
                    type: int
                    description: 'Rate limit for RAN information relay (packets per second).'
                relocation-cancel-request:
                    type: int
                    description: 'Rate limit for relocation cancel request (packets per second).'
                relocation-cancel-response:
                    type: int
                    description: 'Rate limit for relocation cancel response (packets per second).'
                send-route-request:
                    type: int
                    description: 'Rate limit for send routing information for GPRS request (packets per second).'
                send-route-response:
                    type: int
                    description: 'Rate limit for send routing information for GPRS response (packets per second).'
                sgsn-context-ack:
                    type: int
                    description: 'Rate limit for SGSN context acknowledgement (packets per second).'
                sgsn-context-request:
                    type: int
                    description: 'Rate limit for SGSN context request (packets per second).'
                sgsn-context-response:
                    type: int
                    description: 'Rate limit for SGSN context response (packets per second).'
                support-ext-hdr-notify:
                    type: int
                    description: 'Rate limit for support extension headers notification (packets per second).'
                update-mbms-request:
                    type: int
                    description: 'Rate limit for update MBMS context request (packets per second).'
                update-mbms-response:
                    type: int
                    description: 'Rate limit for update MBMS context response (packets per second).'
                update-pdp-request:
                    type: int
                    description: 'Rate limit for update PDP context request (packets per second).'
                update-pdp-response:
                    type: int
                    description: 'Rate limit for update PDP context response (packets per second).'
                version-not-support:
                    type: int
                    description: 'Rate limit for version not supported (packets per second).'

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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/GTP/{GTP}/MESSAGE-RATE-LIMIT
      fmgr_firewall_gtp_messageratelimit:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            gtp: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/GTP/{GTP}/MESSAGE-RATE-LIMIT
      fmgr_firewall_gtp_messageratelimit:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            gtp: <value of string>
         params:
            -
               data:
                  create-aa-pdp-request: <value of integer>
                  create-aa-pdp-response: <value of integer>
                  create-mbms-request: <value of integer>
                  create-mbms-response: <value of integer>
                  create-pdp-request: <value of integer>
                  create-pdp-response: <value of integer>
                  delete-aa-pdp-request: <value of integer>
                  delete-aa-pdp-response: <value of integer>
                  delete-mbms-request: <value of integer>
                  delete-mbms-response: <value of integer>
                  delete-pdp-request: <value of integer>
                  delete-pdp-response: <value of integer>
                  echo-reponse: <value of integer>
                  echo-request: <value of integer>
                  error-indication: <value of integer>
                  failure-report-request: <value of integer>
                  failure-report-response: <value of integer>
                  fwd-reloc-complete-ack: <value of integer>
                  fwd-relocation-complete: <value of integer>
                  fwd-relocation-request: <value of integer>
                  fwd-relocation-response: <value of integer>
                  fwd-srns-context: <value of integer>
                  fwd-srns-context-ack: <value of integer>
                  g-pdu: <value of integer>
                  identification-request: <value of integer>
                  identification-response: <value of integer>
                  mbms-de-reg-request: <value of integer>
                  mbms-de-reg-response: <value of integer>
                  mbms-notify-rej-request: <value of integer>
                  mbms-notify-rej-response: <value of integer>
                  mbms-notify-request: <value of integer>
                  mbms-notify-response: <value of integer>
                  mbms-reg-request: <value of integer>
                  mbms-reg-response: <value of integer>
                  mbms-ses-start-request: <value of integer>
                  mbms-ses-start-response: <value of integer>
                  mbms-ses-stop-request: <value of integer>
                  mbms-ses-stop-response: <value of integer>
                  note-ms-request: <value of integer>
                  note-ms-response: <value of integer>
                  pdu-notify-rej-request: <value of integer>
                  pdu-notify-rej-response: <value of integer>
                  pdu-notify-request: <value of integer>
                  pdu-notify-response: <value of integer>
                  ran-info: <value of integer>
                  relocation-cancel-request: <value of integer>
                  relocation-cancel-response: <value of integer>
                  send-route-request: <value of integer>
                  send-route-response: <value of integer>
                  sgsn-context-ack: <value of integer>
                  sgsn-context-request: <value of integer>
                  sgsn-context-response: <value of integer>
                  support-ext-hdr-notify: <value of integer>
                  update-mbms-request: <value of integer>
                  update-mbms-response: <value of integer>
                  update-pdp-request: <value of integer>
                  update-pdp-response: <value of integer>
                  version-not-support: <value of integer>

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
            create-aa-pdp-request:
               type: int
               description: 'Rate limit for create AA PDP context request (packets per second).'
            create-aa-pdp-response:
               type: int
               description: 'Rate limit for create AA PDP context response (packets per second).'
            create-mbms-request:
               type: int
               description: 'Rate limit for create MBMS context request (packets per second).'
            create-mbms-response:
               type: int
               description: 'Rate limit for create MBMS context response (packets per second).'
            create-pdp-request:
               type: int
               description: 'Rate limit for create PDP context request (packets per second).'
            create-pdp-response:
               type: int
               description: 'Rate limit for create PDP context response (packets per second).'
            delete-aa-pdp-request:
               type: int
               description: 'Rate limit for delete AA PDP context request (packets per second).'
            delete-aa-pdp-response:
               type: int
               description: 'Rate limit for delete AA PDP context response (packets per second).'
            delete-mbms-request:
               type: int
               description: 'Rate limit for delete MBMS context request (packets per second).'
            delete-mbms-response:
               type: int
               description: 'Rate limit for delete MBMS context response (packets per second).'
            delete-pdp-request:
               type: int
               description: 'Rate limit for delete PDP context request (packets per second).'
            delete-pdp-response:
               type: int
               description: 'Rate limit for delete PDP context response (packets per second).'
            echo-reponse:
               type: int
               description: 'Rate limit for echo response (packets per second).'
            echo-request:
               type: int
               description: 'Rate limit for echo requests (packets per second).'
            error-indication:
               type: int
               description: 'Rate limit for error indication (packets per second).'
            failure-report-request:
               type: int
               description: 'Rate limit for failure report request (packets per second).'
            failure-report-response:
               type: int
               description: 'Rate limit for failure report response (packets per second).'
            fwd-reloc-complete-ack:
               type: int
               description: 'Rate limit for forward relocation complete acknowledge (packets per second).'
            fwd-relocation-complete:
               type: int
               description: 'Rate limit for forward relocation complete (packets per second).'
            fwd-relocation-request:
               type: int
               description: 'Rate limit for forward relocation request (packets per second).'
            fwd-relocation-response:
               type: int
               description: 'Rate limit for forward relocation response (packets per second).'
            fwd-srns-context:
               type: int
               description: 'Rate limit for forward SRNS context (packets per second).'
            fwd-srns-context-ack:
               type: int
               description: 'Rate limit for forward SRNS context acknowledge (packets per second).'
            g-pdu:
               type: int
               description: 'Rate limit for G-PDU (packets per second).'
            identification-request:
               type: int
               description: 'Rate limit for identification request (packets per second).'
            identification-response:
               type: int
               description: 'Rate limit for identification response (packets per second).'
            mbms-de-reg-request:
               type: int
               description: 'Rate limit for MBMS de-registration request (packets per second).'
            mbms-de-reg-response:
               type: int
               description: 'Rate limit for MBMS de-registration response (packets per second).'
            mbms-notify-rej-request:
               type: int
               description: 'Rate limit for MBMS notification reject request (packets per second).'
            mbms-notify-rej-response:
               type: int
               description: 'Rate limit for MBMS notification reject response (packets per second).'
            mbms-notify-request:
               type: int
               description: 'Rate limit for MBMS notification request (packets per second).'
            mbms-notify-response:
               type: int
               description: 'Rate limit for MBMS notification response (packets per second).'
            mbms-reg-request:
               type: int
               description: 'Rate limit for MBMS registration request (packets per second).'
            mbms-reg-response:
               type: int
               description: 'Rate limit for MBMS registration response (packets per second).'
            mbms-ses-start-request:
               type: int
               description: 'Rate limit for MBMS session start request (packets per second).'
            mbms-ses-start-response:
               type: int
               description: 'Rate limit for MBMS session start response (packets per second).'
            mbms-ses-stop-request:
               type: int
               description: 'Rate limit for MBMS session stop request (packets per second).'
            mbms-ses-stop-response:
               type: int
               description: 'Rate limit for MBMS session stop response (packets per second).'
            note-ms-request:
               type: int
               description: 'Rate limit for note MS GPRS present request (packets per second).'
            note-ms-response:
               type: int
               description: 'Rate limit for note MS GPRS present response (packets per second).'
            pdu-notify-rej-request:
               type: int
               description: 'Rate limit for PDU notify reject request (packets per second).'
            pdu-notify-rej-response:
               type: int
               description: 'Rate limit for PDU notify reject response (packets per second).'
            pdu-notify-request:
               type: int
               description: 'Rate limit for PDU notify request (packets per second).'
            pdu-notify-response:
               type: int
               description: 'Rate limit for PDU notify response (packets per second).'
            ran-info:
               type: int
               description: 'Rate limit for RAN information relay (packets per second).'
            relocation-cancel-request:
               type: int
               description: 'Rate limit for relocation cancel request (packets per second).'
            relocation-cancel-response:
               type: int
               description: 'Rate limit for relocation cancel response (packets per second).'
            send-route-request:
               type: int
               description: 'Rate limit for send routing information for GPRS request (packets per second).'
            send-route-response:
               type: int
               description: 'Rate limit for send routing information for GPRS response (packets per second).'
            sgsn-context-ack:
               type: int
               description: 'Rate limit for SGSN context acknowledgement (packets per second).'
            sgsn-context-request:
               type: int
               description: 'Rate limit for SGSN context request (packets per second).'
            sgsn-context-response:
               type: int
               description: 'Rate limit for SGSN context response (packets per second).'
            support-ext-hdr-notify:
               type: int
               description: 'Rate limit for support extension headers notification (packets per second).'
            update-mbms-request:
               type: int
               description: 'Rate limit for update MBMS context request (packets per second).'
            update-mbms-response:
               type: int
               description: 'Rate limit for update MBMS context response (packets per second).'
            update-pdp-request:
               type: int
               description: 'Rate limit for update PDP context request (packets per second).'
            update-pdp-response:
               type: int
               description: 'Rate limit for update PDP context response (packets per second).'
            version-not-support:
               type: int
               description: 'Rate limit for version not supported (packets per second).'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/firewall/gtp/{gtp}/message-rate-limit'
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
            example: '/pm/config/adom/{adom}/obj/firewall/gtp/{gtp}/message-rate-limit'

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
        '/pm/config/adom/{adom}/obj/firewall/gtp/{gtp}/message-rate-limit',
        '/pm/config/global/obj/firewall/gtp/{gtp}/message-rate-limit'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'gtp',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
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
            ],
            'object1': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'create-aa-pdp-request': {
                            'type': 'integer'
                        },
                        'create-aa-pdp-response': {
                            'type': 'integer'
                        },
                        'create-mbms-request': {
                            'type': 'integer'
                        },
                        'create-mbms-response': {
                            'type': 'integer'
                        },
                        'create-pdp-request': {
                            'type': 'integer'
                        },
                        'create-pdp-response': {
                            'type': 'integer'
                        },
                        'delete-aa-pdp-request': {
                            'type': 'integer'
                        },
                        'delete-aa-pdp-response': {
                            'type': 'integer'
                        },
                        'delete-mbms-request': {
                            'type': 'integer'
                        },
                        'delete-mbms-response': {
                            'type': 'integer'
                        },
                        'delete-pdp-request': {
                            'type': 'integer'
                        },
                        'delete-pdp-response': {
                            'type': 'integer'
                        },
                        'echo-reponse': {
                            'type': 'integer'
                        },
                        'echo-request': {
                            'type': 'integer'
                        },
                        'error-indication': {
                            'type': 'integer'
                        },
                        'failure-report-request': {
                            'type': 'integer'
                        },
                        'failure-report-response': {
                            'type': 'integer'
                        },
                        'fwd-reloc-complete-ack': {
                            'type': 'integer'
                        },
                        'fwd-relocation-complete': {
                            'type': 'integer'
                        },
                        'fwd-relocation-request': {
                            'type': 'integer'
                        },
                        'fwd-relocation-response': {
                            'type': 'integer'
                        },
                        'fwd-srns-context': {
                            'type': 'integer'
                        },
                        'fwd-srns-context-ack': {
                            'type': 'integer'
                        },
                        'g-pdu': {
                            'type': 'integer'
                        },
                        'identification-request': {
                            'type': 'integer'
                        },
                        'identification-response': {
                            'type': 'integer'
                        },
                        'mbms-de-reg-request': {
                            'type': 'integer'
                        },
                        'mbms-de-reg-response': {
                            'type': 'integer'
                        },
                        'mbms-notify-rej-request': {
                            'type': 'integer'
                        },
                        'mbms-notify-rej-response': {
                            'type': 'integer'
                        },
                        'mbms-notify-request': {
                            'type': 'integer'
                        },
                        'mbms-notify-response': {
                            'type': 'integer'
                        },
                        'mbms-reg-request': {
                            'type': 'integer'
                        },
                        'mbms-reg-response': {
                            'type': 'integer'
                        },
                        'mbms-ses-start-request': {
                            'type': 'integer'
                        },
                        'mbms-ses-start-response': {
                            'type': 'integer'
                        },
                        'mbms-ses-stop-request': {
                            'type': 'integer'
                        },
                        'mbms-ses-stop-response': {
                            'type': 'integer'
                        },
                        'note-ms-request': {
                            'type': 'integer'
                        },
                        'note-ms-response': {
                            'type': 'integer'
                        },
                        'pdu-notify-rej-request': {
                            'type': 'integer'
                        },
                        'pdu-notify-rej-response': {
                            'type': 'integer'
                        },
                        'pdu-notify-request': {
                            'type': 'integer'
                        },
                        'pdu-notify-response': {
                            'type': 'integer'
                        },
                        'ran-info': {
                            'type': 'integer'
                        },
                        'relocation-cancel-request': {
                            'type': 'integer'
                        },
                        'relocation-cancel-response': {
                            'type': 'integer'
                        },
                        'send-route-request': {
                            'type': 'integer'
                        },
                        'send-route-response': {
                            'type': 'integer'
                        },
                        'sgsn-context-ack': {
                            'type': 'integer'
                        },
                        'sgsn-context-request': {
                            'type': 'integer'
                        },
                        'sgsn-context-response': {
                            'type': 'integer'
                        },
                        'support-ext-hdr-notify': {
                            'type': 'integer'
                        },
                        'update-mbms-request': {
                            'type': 'integer'
                        },
                        'update-mbms-response': {
                            'type': 'integer'
                        },
                        'update-pdp-request': {
                            'type': 'integer'
                        },
                        'update-pdp-response': {
                            'type': 'integer'
                        },
                        'version-not-support': {
                            'type': 'integer'
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
