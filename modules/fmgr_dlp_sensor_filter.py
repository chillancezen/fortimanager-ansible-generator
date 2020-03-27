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
module: fmgr_dlp_sensor_filter
short_description: Set up DLP filters for this sensor.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/dlp/sensor/{sensor}/filter
    - /pm/config/global/obj/dlp/sensor/{sensor}/filter
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
            sensor:
                type: str
    schema_object0:
        methods: [add, set, update]
        description: 'Set up DLP filters for this sensor.'
        api_categories: [api_tag0]
        api_tag0:
            data:
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
    schema_object1:
        methods: [get]
        description: 'Set up DLP filters for this sensor.'
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
                            - 'action'
                            - 'archive'
                            - 'company-identifier'
                            - 'expiry'
                            - 'file-size'
                            - 'file-type'
                            - 'filter-by'
                            - 'fp-sensitivity'
                            - 'id'
                            - 'match-percentage'
                            - 'name'
                            - 'proto'
                            - 'regexp'
                            - 'severity'
                            - 'type'
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

    - name: REQUESTING /PM/CONFIG/OBJ/DLP/SENSOR/{SENSOR}/FILTER
      fmgr_dlp_sensor_filter:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            sensor: <value of string>
         params:
            -
               data:
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

    - name: REQUESTING /PM/CONFIG/OBJ/DLP/SENSOR/{SENSOR}/FILTER
      fmgr_dlp_sensor_filter:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            sensor: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [action, archive, company-identifier, ...]>
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
         data:
            type: array
            suboptions:
               id:
                  type: int
                  description: 'ID.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/dlp/sensor/{sensor}/filter'
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
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/dlp/sensor/{sensor}/filter'

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
        '/pm/config/adom/{adom}/obj/dlp/sensor/{sensor}/filter',
        '/pm/config/global/obj/dlp/sensor/{sensor}/filter'
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
                    'api_tag': 0,
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
                                'action',
                                'archive',
                                'company-identifier',
                                'expiry',
                                'file-size',
                                'file-type',
                                'filter-by',
                                'fp-sensitivity',
                                'id',
                                'match-percentage',
                                'name',
                                'proto',
                                'regexp',
                                'severity',
                                'type'
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
