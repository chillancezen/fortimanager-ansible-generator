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
module: fmgr_pm_config_obj_dlp_sensor
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis:
    - /pm/config/adom/{adom}/obj/dlp/sensor
    - /pm/config/global/obj/dlp/sensor
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
        description: 'Configure DLP sensors.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    comment:
                        type: str
                        description: 'Comment.'
                    dlp-log:
                        type: str
                        description: 'Enable/disable DLP logging.'
                        choices:
                            - disable
                            - enable
                    extended-log:
                        type: str
                        description: 'Enable/disable extended logging for data leak prevention.'
                        choices:
                            - disable
                            - enable
                    filter:
                        -
                            action:
                                type: str
                                description: 'Action to take with content that this DLP sensor matches.'
                                choices:
                                    - log-only
                                    - block
                                    - exempt
                                    - ban
                                    - ban-sender
                                    - quarantine-ip
                                    - quarantine-port
                                    - none
                                    - allow
                            archive:
                                type: str
                                description: 'Enable/disable DLP archiving.'
                                choices:
                                    - disable
                                    - enable
                                    - summary-only
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
                                    - credit-card
                                    - ssn
                                    - regexp
                                    - file-type
                                    - file-size
                                    - fingerprint
                                    - watermark
                                    - encrypted
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
                                        - imap
                                        - smtp
                                        - pop3
                                        - ftp
                                        - nntp
                                        - mm1
                                        - mm3
                                        - mm4
                                        - mm7
                                        - mapi
                                        - aim
                                        - icq
                                        - msn
                                        - yahoo
                                        - http-get
                                        - http-post
                            regexp:
                                type: str
                                description: 'Enter a regular expression to match (max. 255 characters).'
                            severity:
                                type: str
                                description: 'Select the severity or threat level that matches this filter.'
                                choices:
                                    - info
                                    - low
                                    - medium
                                    - high
                                    - critical
                            type:
                                type: str
                                description: 'Select whether to check the content of messages (an email message) or files (downloaded files or email attachments).'
                                choices:
                                    - file
                                    - message
                    flow-based:
                        type: str
                        description: 'Enable/disable flow-based DLP.'
                        choices:
                            - disable
                            - enable
                    full-archive-proto:
                        -
                            type: str
                            choices:
                                - imap
                                - smtp
                                - pop3
                                - ftp
                                - nntp
                                - mm1
                                - mm3
                                - mm4
                                - mm7
                                - mapi
                                - aim
                                - icq
                                - msn
                                - yahoo
                                - http-get
                                - http-post
                    nac-quar-log:
                        type: str
                        description: 'Enable/disable NAC quarantine logging.'
                        choices:
                            - disable
                            - enable
                    name:
                        type: str
                        description: 'Name of the DLP sensor.'
                    options:
                        type: str
                        description: 'Configure DLP options.'
                        choices:
                            - strict-file
                    replacemsg-group:
                        type: str
                        description: 'Replacement message group used by this DLP sensor.'
                    summary-proto:
                        -
                            type: str
                            choices:
                                - imap
                                - smtp
                                - pop3
                                - ftp
                                - nntp
                                - mm1
                                - mm3
                                - mm4
                                - mm7
                                - mapi
                                - aim
                                - icq
                                - msn
                                - yahoo
                                - http-get
                                - http-post
    schema_object1:
        methods: [get]
        description: 'Configure DLP sensors.'
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
                            - comment
                            - dlp-log
                            - extended-log
                            - flow-based
                            - full-archive-proto
                            - nac-quar-log
                            - name
                            - options
                            - replacemsg-group
                            - summary-proto
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
                    - count
                    - object member
                    - datasrc
                    - get reserved
                    - syntax
            range:
                -
                    type: int
            sortings:
                -
                    \{attr_name\}:
                        type: int
                        choices:
                            - 1
                            - -1

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /pm/config/obj/dlp/sensor
      fmgr_pm_config_obj_dlp_sensor:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            - 
               data: 
                - 
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
    - name: send request to /pm/config/obj/dlp/sensor
      fmgr_pm_config_obj_dlp_sensor:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            - 
               attr: <value of string>
               fields: 
                - 
                   - <value in [comment, dlp-log, extended-log, ...]>
               filter: 
                - <value of string>
               get used: <value of integer>
               loadsub: <value of integer>
               option: <value in [count, object member, datasrc, ...]>
               range: 
                - <value of integer>
               sortings: 
                - 
                     \{attr_name\}: <value in [1, -1]>

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
            example: /pm/config/adom/{adom}/obj/dlp/sensor
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
            example: /pm/config/adom/{adom}/obj/dlp/sensor

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
        '/pm/config/adom/{adom}/obj/dlp/sensor',
        '/pm/config/global/obj/dlp/sensor'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        }
    ]

    body_schema =  {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
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
                                'dlp-log',
                                'extended-log',
                                'flow-based',
                                'full-archive-proto',
                                'nac-quar-log',
                                'name',
                                'options',
                                'replacemsg-group',
                                'summary-proto'
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