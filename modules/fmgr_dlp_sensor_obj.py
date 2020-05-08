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
module: fmgr_dlp_sensor_obj
short_description: Configure DLP sensors.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/dlp/sensor/{sensor}
    - /pm/config/global/obj/dlp/sensor/{sensor}
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
        description: the maximum time in seconds to wait for other user to release the workspace lock
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
            sensor:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Configure DLP sensors.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                comment:
                    type: str
                    description: 'Comment.'
                dlp-log:
                    type: str
                    description: 'Enable/disable DLP logging.'
                    choices:
                        - 'disable'
                        - 'enable'
                extended-log:
                    type: str
                    description: 'Enable/disable extended logging for data leak prevention.'
                    choices:
                        - 'disable'
                        - 'enable'
                filter:
                    -
                        action:
                            type: str
                            description: 'Action to take with content that this DLP sensor matches.'
                            choices:
                                - 'log-only'
                                - 'block'
                                - 'exempt'
                                - 'ban'
                                - 'ban-sender'
                                - 'quarantine-ip'
                                - 'quarantine-port'
                                - 'none'
                                - 'allow'
                        archive:
                            type: str
                            description: 'Enable/disable DLP archiving.'
                            choices:
                                - 'disable'
                                - 'enable'
                                - 'summary-only'
                        company-identifier:
                            type: str
                            description: 'Enter a company identifier watermark to match. Only watermarks that your company has placed on the files are matched.'
                        expiry:
                            type: str
                            description: 'Quarantine duration in days, hours, minutes format (dddhhmm).'
                        file-size:
                            type: int
                            description: 'Match files this size or larger (0 - 4294967295 kbytes).'
                        file-type:
                            type: str
                            description: 'Select the number of a DLP file pattern table to match.'
                        filter-by:
                            type: str
                            description: 'Select the type of content to match.'
                            choices:
                                - 'credit-card'
                                - 'ssn'
                                - 'regexp'
                                - 'file-type'
                                - 'file-size'
                                - 'fingerprint'
                                - 'watermark'
                                - 'encrypted'
                        fp-sensitivity:
                            type: str
                            description: 'Select a DLP file pattern sensitivity to match.'
                        id:
                            type: int
                            description: 'ID.'
                        match-percentage:
                            type: int
                            description: 'Percentage of fingerprints in the fingerprint databases designated with the selected fp-sensitivity to match.'
                        name:
                            type: str
                            description: 'Filter name.'
                        proto:
                            -
                                type: str
                                choices:
                                    - 'imap'
                                    - 'smtp'
                                    - 'pop3'
                                    - 'ftp'
                                    - 'nntp'
                                    - 'mm1'
                                    - 'mm3'
                                    - 'mm4'
                                    - 'mm7'
                                    - 'mapi'
                                    - 'aim'
                                    - 'icq'
                                    - 'msn'
                                    - 'yahoo'
                                    - 'http-get'
                                    - 'http-post'
                        regexp:
                            type: str
                            description: 'Enter a regular expression to match (max. 255 characters).'
                        severity:
                            type: str
                            description: 'Select the severity or threat level that matches this filter.'
                            choices:
                                - 'info'
                                - 'low'
                                - 'medium'
                                - 'high'
                                - 'critical'
                        type:
                            type: str
                            description: 'Select whether to check the content of messages (an email message) or files (downloaded files or email attachments).'
                            choices:
                                - 'file'
                                - 'message'
                flow-based:
                    type: str
                    description: 'Enable/disable flow-based DLP.'
                    choices:
                        - 'disable'
                        - 'enable'
                full-archive-proto:
                    -
                        type: str
                        choices:
                            - 'imap'
                            - 'smtp'
                            - 'pop3'
                            - 'ftp'
                            - 'nntp'
                            - 'mm1'
                            - 'mm3'
                            - 'mm4'
                            - 'mm7'
                            - 'mapi'
                            - 'aim'
                            - 'icq'
                            - 'msn'
                            - 'yahoo'
                            - 'http-get'
                            - 'http-post'
                nac-quar-log:
                    type: str
                    description: 'Enable/disable NAC quarantine logging.'
                    choices:
                        - 'disable'
                        - 'enable'
                name:
                    type: str
                    description: 'Name of the DLP sensor.'
                options:
                    type: str
                    description: 'Configure DLP options.'
                    choices:
                        - 'strict-file'
                replacemsg-group:
                    type: str
                    description: 'Replacement message group used by this DLP sensor.'
                summary-proto:
                    -
                        type: str
                        choices:
                            - 'imap'
                            - 'smtp'
                            - 'pop3'
                            - 'ftp'
                            - 'nntp'
                            - 'mm1'
                            - 'mm3'
                            - 'mm4'
                            - 'mm7'
                            - 'mapi'
                            - 'aim'
                            - 'icq'
                            - 'msn'
                            - 'yahoo'
                            - 'http-get'
                            - 'http-post'
    schema_object1:
        methods: [delete]
        description: 'Configure DLP sensors.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Configure DLP sensors.'
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

    - name: REQUESTING /PM/CONFIG/OBJ/DLP/SENSOR/{SENSOR}
      fmgr_dlp_sensor_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            sensor: <value of string>
         params:
            -
               data:
                  comment: <value of string>
                  dlp-log: <value in [disable, enable]>
                  extended-log: <value in [disable, enable]>
                  filter:
                    -
                        action: <value in [log-only, block, exempt, ...]>
                        archive: <value in [disable, enable, summary-only]>
                        company-identifier: <value of string>
                        expiry: <value of string>
                        file-size: <value of integer>
                        file-type: <value of string>
                        filter-by: <value in [credit-card, ssn, regexp, ...]>
                        fp-sensitivity: <value of string>
                        id: <value of integer>
                        match-percentage: <value of integer>
                        name: <value of string>
                        proto:
                          - <value in [imap, smtp, pop3, ...]>
                        regexp: <value of string>
                        severity: <value in [info, low, medium, ...]>
                        type: <value in [file, message]>
                  flow-based: <value in [disable, enable]>
                  full-archive-proto:
                    - <value in [imap, smtp, pop3, ...]>
                  nac-quar-log: <value in [disable, enable]>
                  name: <value of string>
                  options: <value in [strict-file]>
                  replacemsg-group: <value of string>
                  summary-proto:
                    - <value in [imap, smtp, pop3, ...]>

    - name: REQUESTING /PM/CONFIG/OBJ/DLP/SENSOR/{SENSOR}
      fmgr_dlp_sensor_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            sensor: <value of string>
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
            example: '/pm/config/adom/{adom}/obj/dlp/sensor/{sensor}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            comment:
               type: str
               description: 'Comment.'
            dlp-log:
               type: str
               description: 'Enable/disable DLP logging.'
            extended-log:
               type: str
               description: 'Enable/disable extended logging for data leak prevention.'
            filter:
               type: array
               suboptions:
                  action:
                     type: str
                     description: 'Action to take with content that this DLP sensor matches.'
                  archive:
                     type: str
                     description: 'Enable/disable DLP archiving.'
                  company-identifier:
                     type: str
                     description: 'Enter a company identifier watermark to match. Only watermarks that your company has placed on the files are matched.'
                  expiry:
                     type: str
                     description: 'Quarantine duration in days, hours, minutes format (dddhhmm).'
                  file-size:
                     type: int
                     description: 'Match files this size or larger (0 - 4294967295 kbytes).'
                  file-type:
                     type: str
                     description: 'Select the number of a DLP file pattern table to match.'
                  filter-by:
                     type: str
                     description: 'Select the type of content to match.'
                  fp-sensitivity:
                     type: str
                     description: 'Select a DLP file pattern sensitivity to match.'
                  id:
                     type: int
                     description: 'ID.'
                  match-percentage:
                     type: int
                     description: 'Percentage of fingerprints in the fingerprint databases designated with the selected fp-sensitivity to match.'
                  name:
                     type: str
                     description: 'Filter name.'
                  proto:
                     type: array
                     suboptions:
                        type: str
                  regexp:
                     type: str
                     description: 'Enter a regular expression to match (max. 255 characters).'
                  severity:
                     type: str
                     description: 'Select the severity or threat level that matches this filter.'
                  type:
                     type: str
                     description: 'Select whether to check the content of messages (an email message) or files (downloaded files or email attachments).'
            flow-based:
               type: str
               description: 'Enable/disable flow-based DLP.'
            full-archive-proto:
               type: array
               suboptions:
                  type: str
            nac-quar-log:
               type: str
               description: 'Enable/disable NAC quarantine logging.'
            name:
               type: str
               description: 'Name of the DLP sensor.'
            options:
               type: str
               description: 'Configure DLP options.'
            replacemsg-group:
               type: str
               description: 'Replacement message group used by this DLP sensor.'
            summary-proto:
               type: array
               suboptions:
                  type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/dlp/sensor/{sensor}'

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
        '/pm/config/adom/{adom}/obj/dlp/sensor/{sensor}',
        '/pm/config/global/obj/dlp/sensor/{sensor}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'sensor',
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
                        'comment': {
                            'type': 'string'
                        },
                        'dlp-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'extended-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'filter': {
                            'type': 'array',
                            'items': {
                                'action': {
                                    'type': 'string',
                                    'enum': [
                                        'log-only',
                                        'block',
                                        'exempt',
                                        'ban',
                                        'ban-sender',
                                        'quarantine-ip',
                                        'quarantine-port',
                                        'none',
                                        'allow'
                                    ]
                                },
                                'archive': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable',
                                        'summary-only'
                                    ]
                                },
                                'company-identifier': {
                                    'type': 'string'
                                },
                                'expiry': {
                                    'type': 'string'
                                },
                                'file-size': {
                                    'type': 'integer'
                                },
                                'file-type': {
                                    'type': 'string'
                                },
                                'filter-by': {
                                    'type': 'string',
                                    'enum': [
                                        'credit-card',
                                        'ssn',
                                        'regexp',
                                        'file-type',
                                        'file-size',
                                        'fingerprint',
                                        'watermark',
                                        'encrypted'
                                    ]
                                },
                                'fp-sensitivity': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'match-percentage': {
                                    'type': 'integer'
                                },
                                'name': {
                                    'type': 'string'
                                },
                                'proto': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string',
                                        'enum': [
                                            'imap',
                                            'smtp',
                                            'pop3',
                                            'ftp',
                                            'nntp',
                                            'mm1',
                                            'mm3',
                                            'mm4',
                                            'mm7',
                                            'mapi',
                                            'aim',
                                            'icq',
                                            'msn',
                                            'yahoo',
                                            'http-get',
                                            'http-post'
                                        ]
                                    }
                                },
                                'regexp': {
                                    'type': 'string'
                                },
                                'severity': {
                                    'type': 'string',
                                    'enum': [
                                        'info',
                                        'low',
                                        'medium',
                                        'high',
                                        'critical'
                                    ]
                                },
                                'type': {
                                    'type': 'string',
                                    'enum': [
                                        'file',
                                        'message'
                                    ]
                                }
                            }
                        },
                        'flow-based': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'full-archive-proto': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'imap',
                                    'smtp',
                                    'pop3',
                                    'ftp',
                                    'nntp',
                                    'mm1',
                                    'mm3',
                                    'mm4',
                                    'mm7',
                                    'mapi',
                                    'aim',
                                    'icq',
                                    'msn',
                                    'yahoo',
                                    'http-get',
                                    'http-post'
                                ]
                            }
                        },
                        'nac-quar-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'name': {
                            'type': 'string'
                        },
                        'options': {
                            'type': 'string',
                            'enum': [
                                'strict-file'
                            ]
                        },
                        'replacemsg-group': {
                            'type': 'string'
                        },
                        'summary-proto': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'imap',
                                    'smtp',
                                    'pop3',
                                    'ftp',
                                    'nntp',
                                    'mm1',
                                    'mm3',
                                    'mm4',
                                    'mm7',
                                    'mapi',
                                    'aim',
                                    'icq',
                                    'msn',
                                    'yahoo',
                                    'http-get',
                                    'http-post'
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
        if loose_validation is False:
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
