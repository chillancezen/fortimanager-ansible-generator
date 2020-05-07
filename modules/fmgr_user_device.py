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
module: fmgr_user_device
short_description: Configure devices.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/user/device
    - /pm/config/global/obj/user/device
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
    schema_object0:
        methods: [add, set, update]
        description: 'Configure devices.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    alias:
                        type: str
                        description: 'Device alias.'
                    avatar:
                        type: str
                        description: 'Image file for avatar (maximum 4K base64 encoded).'
                    category:
                        type: str
                        description: 'Device category.'
                        choices:
                            - 'none'
                            - 'android-device'
                            - 'blackberry-device'
                            - 'fortinet-device'
                            - 'ios-device'
                            - 'windows-device'
                            - 'amazon-device'
                    comment:
                        type: str
                        description: 'Comment.'
                    dynamic_mapping:
                        -
                            _scope:
                                -
                                    name:
                                        type: str
                                    vdom:
                                        type: str
                            avatar:
                                type: str
                            category:
                                type: str
                                choices:
                                    - 'none'
                                    - 'android-device'
                                    - 'blackberry-device'
                                    - 'fortinet-device'
                                    - 'ios-device'
                                    - 'windows-device'
                                    - 'amazon-device'
                            comment:
                                type: str
                            mac:
                                type: str
                            master-device:
                                type: str
                            tags:
                                type: str
                            type:
                                type: str
                                choices:
                                    - 'ipad'
                                    - 'iphone'
                                    - 'gaming-console'
                                    - 'blackberry-phone'
                                    - 'blackberry-playbook'
                                    - 'linux-pc'
                                    - 'mac'
                                    - 'windows-pc'
                                    - 'android-phone'
                                    - 'android-tablet'
                                    - 'media-streaming'
                                    - 'windows-phone'
                                    - 'fortinet-device'
                                    - 'ip-phone'
                                    - 'router-nat-device'
                                    - 'other-network-device'
                                    - 'windows-tablet'
                                    - 'printer'
                                    - 'forticam'
                                    - 'fortifone'
                                    - 'unknown'
                            user:
                                type: str
                    mac:
                        type: str
                        description: 'Device MAC address(es).'
                    master-device:
                        type: str
                        description: 'Master device (optional).'
                    tagging:
                        -
                            category:
                                type: str
                                description: 'Tag category.'
                            name:
                                type: str
                                description: 'Tagging entry name.'
                            tags:
                                -
                                    type: str
                    type:
                        type: str
                        description: 'Device type.'
                        choices:
                            - 'ipad'
                            - 'iphone'
                            - 'gaming-console'
                            - 'blackberry-phone'
                            - 'blackberry-playbook'
                            - 'linux-pc'
                            - 'mac'
                            - 'windows-pc'
                            - 'android-phone'
                            - 'android-tablet'
                            - 'media-streaming'
                            - 'windows-phone'
                            - 'fortinet-device'
                            - 'ip-phone'
                            - 'router-nat-device'
                            - 'other-network-device'
                            - 'windows-tablet'
                            - 'printer'
                            - 'forticam'
                            - 'fortifone'
                            - 'unknown'
                    user:
                        type: str
                        description: 'User name.'
    schema_object1:
        methods: [get]
        description: 'Configure devices.'
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
                            - 'alias'
                            - 'avatar'
                            - 'category'
                            - 'comment'
                            - 'mac'
                            - 'master-device'
                            - 'type'
                            - 'user'
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

    - name: REQUESTING /PM/CONFIG/OBJ/USER/DEVICE
      fmgr_user_device:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     alias: <value of string>
                     avatar: <value of string>
                     category: <value in [none, android-device, blackberry-device, ...]>
                     comment: <value of string>
                     dynamic_mapping:
                       -
                           _scope:
                             -
                                 name: <value of string>
                                 vdom: <value of string>
                           avatar: <value of string>
                           category: <value in [none, android-device, blackberry-device, ...]>
                           comment: <value of string>
                           mac: <value of string>
                           master-device: <value of string>
                           tags: <value of string>
                           type: <value in [ipad, iphone, gaming-console, ...]>
                           user: <value of string>
                     mac: <value of string>
                     master-device: <value of string>
                     tagging:
                       -
                           category: <value of string>
                           name: <value of string>
                           tags:
                             - <value of string>
                     type: <value in [ipad, iphone, gaming-console, ...]>
                     user: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/USER/DEVICE
      fmgr_user_device:
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
                    - <value in [alias, avatar, category, ...]>
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
            example: '/pm/config/adom/{adom}/obj/user/device'
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
               alias:
                  type: str
                  description: 'Device alias.'
               avatar:
                  type: str
                  description: 'Image file for avatar (maximum 4K base64 encoded).'
               category:
                  type: str
                  description: 'Device category.'
               comment:
                  type: str
                  description: 'Comment.'
               dynamic_mapping:
                  type: array
                  suboptions:
                     _scope:
                        type: array
                        suboptions:
                           name:
                              type: str
                           vdom:
                              type: str
                     avatar:
                        type: str
                     category:
                        type: str
                     comment:
                        type: str
                     mac:
                        type: str
                     master-device:
                        type: str
                     tags:
                        type: str
                     type:
                        type: str
                     user:
                        type: str
               mac:
                  type: str
                  description: 'Device MAC address(es).'
               master-device:
                  type: str
                  description: 'Master device (optional).'
               tagging:
                  type: array
                  suboptions:
                     category:
                        type: str
                        description: 'Tag category.'
                     name:
                        type: str
                        description: 'Tagging entry name.'
                     tags:
                        type: array
                        suboptions:
                           type: str
               type:
                  type: str
                  description: 'Device type.'
               user:
                  type: str
                  description: 'User name.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/user/device'

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
        '/pm/config/adom/{adom}/obj/user/device',
        '/pm/config/global/obj/user/device'
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
                        'alias': {
                            'type': 'string'
                        },
                        'avatar': {
                            'type': 'string'
                        },
                        'category': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'android-device',
                                'blackberry-device',
                                'fortinet-device',
                                'ios-device',
                                'windows-device',
                                'amazon-device'
                            ]
                        },
                        'comment': {
                            'type': 'string'
                        },
                        'dynamic_mapping': {
                            'type': 'array',
                            'items': {
                                '_scope': {
                                    'type': 'array',
                                    'items': {
                                        'name': {
                                            'type': 'string'
                                        },
                                        'vdom': {
                                            'type': 'string'
                                        }
                                    }
                                },
                                'avatar': {
                                    'type': 'string'
                                },
                                'category': {
                                    'type': 'string',
                                    'enum': [
                                        'none',
                                        'android-device',
                                        'blackberry-device',
                                        'fortinet-device',
                                        'ios-device',
                                        'windows-device',
                                        'amazon-device'
                                    ]
                                },
                                'comment': {
                                    'type': 'string'
                                },
                                'mac': {
                                    'type': 'string'
                                },
                                'master-device': {
                                    'type': 'string'
                                },
                                'tags': {
                                    'type': 'string'
                                },
                                'type': {
                                    'type': 'string',
                                    'enum': [
                                        'ipad',
                                        'iphone',
                                        'gaming-console',
                                        'blackberry-phone',
                                        'blackberry-playbook',
                                        'linux-pc',
                                        'mac',
                                        'windows-pc',
                                        'android-phone',
                                        'android-tablet',
                                        'media-streaming',
                                        'windows-phone',
                                        'fortinet-device',
                                        'ip-phone',
                                        'router-nat-device',
                                        'other-network-device',
                                        'windows-tablet',
                                        'printer',
                                        'forticam',
                                        'fortifone',
                                        'unknown'
                                    ]
                                },
                                'user': {
                                    'type': 'string'
                                }
                            }
                        },
                        'mac': {
                            'type': 'string'
                        },
                        'master-device': {
                            'type': 'string'
                        },
                        'tagging': {
                            'type': 'array',
                            'items': {
                                'category': {
                                    'type': 'string'
                                },
                                'name': {
                                    'type': 'string'
                                },
                                'tags': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                }
                            }
                        },
                        'type': {
                            'type': 'string',
                            'enum': [
                                'ipad',
                                'iphone',
                                'gaming-console',
                                'blackberry-phone',
                                'blackberry-playbook',
                                'linux-pc',
                                'mac',
                                'windows-pc',
                                'android-phone',
                                'android-tablet',
                                'media-streaming',
                                'windows-phone',
                                'fortinet-device',
                                'ip-phone',
                                'router-nat-device',
                                'other-network-device',
                                'windows-tablet',
                                'printer',
                                'forticam',
                                'fortifone',
                                'unknown'
                            ]
                        },
                        'user': {
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
                                'alias',
                                'avatar',
                                'category',
                                'comment',
                                'mac',
                                'master-device',
                                'type',
                                'user'
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
