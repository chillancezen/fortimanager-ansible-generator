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
module: fmgr_gtp_messagefilterv2
short_description: Message filter for GTPv2 messages.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/gtp/message-filter-v2
    - /pm/config/global/obj/gtp/message-filter-v2
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
        description: 'Message filter for GTPv2 messages.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    bearer-resource-cmd-fail:
                        type: str
                        description: 'Bearer resource (command 68, failure indication 69).'
                        choices:
                            - 'allow'
                            - 'deny'
                    change-notification:
                        type: str
                        description: 'Change notification (req 38, resp 39).'
                        choices:
                            - 'allow'
                            - 'deny'
                    create-bearer:
                        type: str
                        description: 'Create bearer (req 95, resp 96).'
                        choices:
                            - 'allow'
                            - 'deny'
                    create-session:
                        type: str
                        description: 'Create session (req 32, resp 33).'
                        choices:
                            - 'allow'
                            - 'deny'
                    delete-bearer-cmd-fail:
                        type: str
                        description: 'Delete bearer (command 66, failure indication 67).'
                        choices:
                            - 'allow'
                            - 'deny'
                    delete-bearer-req-resp:
                        type: str
                        description: 'Delete bearer (req 99, resp 100).'
                        choices:
                            - 'allow'
                            - 'deny'
                    delete-pdn-connection-set:
                        type: str
                        description: 'Delete PDN connection set (req 101, resp 102).'
                        choices:
                            - 'allow'
                            - 'deny'
                    delete-session:
                        type: str
                        description: 'Delete session (req 36, resp 37).'
                        choices:
                            - 'allow'
                            - 'deny'
                    echo:
                        type: str
                        description: 'Echo (req 1, resp 2).'
                        choices:
                            - 'allow'
                            - 'deny'
                    modify-bearer-cmd-fail:
                        type: str
                        description: 'Modify bearer (command 64 , failure indication 65).'
                        choices:
                            - 'allow'
                            - 'deny'
                    modify-bearer-req-resp:
                        type: str
                        description: 'Modify bearer (req 34, resp 35).'
                        choices:
                            - 'allow'
                            - 'deny'
                    name:
                        type: str
                        description: 'Message filter name.'
                    resume:
                        type: str
                        description: 'Resume (notify 164 , ack 165).'
                        choices:
                            - 'allow'
                            - 'deny'
                    suspend:
                        type: str
                        description: 'Suspend (notify 162, ack 163).'
                        choices:
                            - 'allow'
                            - 'deny'
                    trace-session:
                        type: str
                        description: 'Trace session (activation 71, deactivation 72).'
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
                    update-bearer:
                        type: str
                        description: 'Update bearer (req 97, resp 98).'
                        choices:
                            - 'allow'
                            - 'deny'
                    update-pdn-connection-set:
                        type: str
                        description: 'Update PDN connection set (req 200, resp 201).'
                        choices:
                            - 'allow'
                            - 'deny'
                    version-not-support:
                        type: str
                        description: 'Version not supported (3).'
                        choices:
                            - 'allow'
                            - 'deny'
    schema_object1:
        methods: [get]
        description: 'Message filter for GTPv2 messages.'
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
                            - 'bearer-resource-cmd-fail'
                            - 'change-notification'
                            - 'create-bearer'
                            - 'create-session'
                            - 'delete-bearer-cmd-fail'
                            - 'delete-bearer-req-resp'
                            - 'delete-pdn-connection-set'
                            - 'delete-session'
                            - 'echo'
                            - 'modify-bearer-cmd-fail'
                            - 'modify-bearer-req-resp'
                            - 'name'
                            - 'resume'
                            - 'suspend'
                            - 'trace-session'
                            - 'unknown-message'
                            - 'unknown-message-white-list'
                            - 'update-bearer'
                            - 'update-pdn-connection-set'
                            - 'version-not-support'
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
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/GTP/MESSAGE-FILTER-V2
      fmgr_gtp_messagefilterv2:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     bearer-resource-cmd-fail: <value in [allow, deny]>
                     change-notification: <value in [allow, deny]>
                     create-bearer: <value in [allow, deny]>
                     create-session: <value in [allow, deny]>
                     delete-bearer-cmd-fail: <value in [allow, deny]>
                     delete-bearer-req-resp: <value in [allow, deny]>
                     delete-pdn-connection-set: <value in [allow, deny]>
                     delete-session: <value in [allow, deny]>
                     echo: <value in [allow, deny]>
                     modify-bearer-cmd-fail: <value in [allow, deny]>
                     modify-bearer-req-resp: <value in [allow, deny]>
                     name: <value of string>
                     resume: <value in [allow, deny]>
                     suspend: <value in [allow, deny]>
                     trace-session: <value in [allow, deny]>
                     unknown-message: <value in [allow, deny]>
                     unknown-message-white-list:
                       - <value of integer>
                     update-bearer: <value in [allow, deny]>
                     update-pdn-connection-set: <value in [allow, deny]>
                     version-not-support: <value in [allow, deny]>

    - name: REQUESTING /PM/CONFIG/OBJ/GTP/MESSAGE-FILTER-V2
      fmgr_gtp_messagefilterv2:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [bearer-resource-cmd-fail, change-notification, create-bearer, ...]>
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
            example: '/pm/config/adom/{adom}/obj/gtp/message-filter-v2'
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
               bearer-resource-cmd-fail:
                  type: str
                  description: 'Bearer resource (command 68, failure indication 69).'
               change-notification:
                  type: str
                  description: 'Change notification (req 38, resp 39).'
               create-bearer:
                  type: str
                  description: 'Create bearer (req 95, resp 96).'
               create-session:
                  type: str
                  description: 'Create session (req 32, resp 33).'
               delete-bearer-cmd-fail:
                  type: str
                  description: 'Delete bearer (command 66, failure indication 67).'
               delete-bearer-req-resp:
                  type: str
                  description: 'Delete bearer (req 99, resp 100).'
               delete-pdn-connection-set:
                  type: str
                  description: 'Delete PDN connection set (req 101, resp 102).'
               delete-session:
                  type: str
                  description: 'Delete session (req 36, resp 37).'
               echo:
                  type: str
                  description: 'Echo (req 1, resp 2).'
               modify-bearer-cmd-fail:
                  type: str
                  description: 'Modify bearer (command 64 , failure indication 65).'
               modify-bearer-req-resp:
                  type: str
                  description: 'Modify bearer (req 34, resp 35).'
               name:
                  type: str
                  description: 'Message filter name.'
               resume:
                  type: str
                  description: 'Resume (notify 164 , ack 165).'
               suspend:
                  type: str
                  description: 'Suspend (notify 162, ack 163).'
               trace-session:
                  type: str
                  description: 'Trace session (activation 71, deactivation 72).'
               unknown-message:
                  type: str
                  description: 'Allow or Deny unknown messages.'
               unknown-message-white-list:
                  type: array
                  suboptions:
                     type: int
               update-bearer:
                  type: str
                  description: 'Update bearer (req 97, resp 98).'
               update-pdn-connection-set:
                  type: str
                  description: 'Update PDN connection set (req 200, resp 201).'
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
            example: '/pm/config/adom/{adom}/obj/gtp/message-filter-v2'

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import FAIL_SOCKET_MSG
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import DEFAULT_RESULT_OBJ
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import FMGRCommon
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import FMGBaseException
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.fortimanager import FortiManagerHandler


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/gtp/message-filter-v2',
        '/pm/config/global/obj/gtp/message-filter-v2'
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
                        'bearer-resource-cmd-fail': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'change-notification': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'create-bearer': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'create-session': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'delete-bearer-cmd-fail': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'delete-bearer-req-resp': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'delete-pdn-connection-set': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'delete-session': {
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
                        'modify-bearer-cmd-fail': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'modify-bearer-req-resp': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'name': {
                            'type': 'string'
                        },
                        'resume': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'suspend': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'trace-session': {
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
                        'update-bearer': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'update-pdn-connection-set': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
                            ]
                        },
                        'version-not-support': {
                            'type': 'string',
                            'enum': [
                                'allow',
                                'deny'
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
                                'bearer-resource-cmd-fail',
                                'change-notification',
                                'create-bearer',
                                'create-session',
                                'delete-bearer-cmd-fail',
                                'delete-bearer-req-resp',
                                'delete-pdn-connection-set',
                                'delete-session',
                                'echo',
                                'modify-bearer-cmd-fail',
                                'modify-bearer-req-resp',
                                'name',
                                'resume',
                                'suspend',
                                'trace-session',
                                'unknown-message',
                                'unknown-message-white-list',
                                'update-bearer',
                                'update-pdn-connection-set',
                                'version-not-support'
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
