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
module: fmgr_pm_config_pkg_pkg_header_shaping_policy
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis:
    - /pm/config/global/pkg/{pkg}/global/header/shaping-policy
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
            pkg:
                type: str
    schema_object0:
        methods: [add, set, update]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    app-category:
                        type: str
                    app-group:
                        type: str
                    application:
                        -
                            type: int
                    class-id:
                        type: int
                    comment:
                        type: str
                    diffserv-forward:
                        type: str
                        choices:
                            - disable
                            - enable
                    diffserv-reverse:
                        type: str
                        choices:
                            - disable
                            - enable
                    diffservcode-forward:
                        type: str
                    diffservcode-rev:
                        type: str
                    dstaddr:
                        type: str
                    dstaddr6:
                        type: str
                    dstintf:
                        type: str
                    groups:
                        type: str
                    id:
                        type: int
                    internet-service:
                        type: str
                        choices:
                            - disable
                            - enable
                    internet-service-custom:
                        type: str
                    internet-service-custom-group:
                        type: str
                    internet-service-group:
                        type: str
                    internet-service-id:
                        type: str
                    internet-service-src:
                        type: str
                        choices:
                            - disable
                            - enable
                    internet-service-src-custom:
                        type: str
                    internet-service-src-custom-group:
                        type: str
                    internet-service-src-group:
                        type: str
                    internet-service-src-id:
                        type: str
                    ip-version:
                        type: str
                        choices:
                            - 4
                            - 6
                    name:
                        type: str
                    per-ip-shaper:
                        type: str
                    schedule:
                        type: str
                    service:
                        type: str
                    srcaddr:
                        type: str
                    srcaddr6:
                        type: str
                    srcintf:
                        type: str
                    status:
                        type: str
                        choices:
                            - disable
                            - enable
                    tos:
                        type: str
                    tos-mask:
                        type: str
                    tos-negate:
                        type: str
                        choices:
                            - disable
                            - enable
                    traffic-shaper:
                        type: str
                    traffic-shaper-reverse:
                        type: str
                    url-category:
                        type: str
                    users:
                        type: str
    schema_object1:
        methods: [get]
        description: ''
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
                            - app-category
                            - app-group
                            - application
                            - class-id
                            - comment
                            - diffserv-forward
                            - diffserv-reverse
                            - diffservcode-forward
                            - diffservcode-rev
                            - dstaddr
                            - dstaddr6
                            - dstintf
                            - groups
                            - id
                            - internet-service
                            - internet-service-custom
                            - internet-service-custom-group
                            - internet-service-group
                            - internet-service-id
                            - internet-service-src
                            - internet-service-src-custom
                            - internet-service-src-custom-group
                            - internet-service-src-group
                            - internet-service-src-id
                            - ip-version
                            - name
                            - per-ip-shaper
                            - schedule
                            - service
                            - srcaddr
                            - srcaddr6
                            - srcintf
                            - status
                            - tos
                            - tos-mask
                            - tos-negate
                            - traffic-shaper
                            - traffic-shaper-reverse
                            - url-category
                            - users
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
    - name: send request to /pm/config/pkg/{pkg}/header/shaping-policy
      fmgr_pm_config_pkg_pkg_header_shaping_policy:
         method: <value in [add, set, update]>
         url_params:
            pkg: <value of string>
         params:
            - 
               data: 
                - 
                     app-category: <value of string>
                     app-group: <value of string>
                     application: 
                      - <value of integer>
                     class-id: <value of integer>
                     comment: <value of string>
                     diffserv-forward: <value in [disable, enable]>
                     diffserv-reverse: <value in [disable, enable]>
                     diffservcode-forward: <value of string>
                     diffservcode-rev: <value of string>
                     dstaddr: <value of string>
                     dstaddr6: <value of string>
                     dstintf: <value of string>
                     groups: <value of string>
                     id: <value of integer>
                     internet-service: <value in [disable, enable]>
                     internet-service-custom: <value of string>
                     internet-service-custom-group: <value of string>
                     internet-service-group: <value of string>
                     internet-service-id: <value of string>
                     internet-service-src: <value in [disable, enable]>
                     internet-service-src-custom: <value of string>
                     internet-service-src-custom-group: <value of string>
                     internet-service-src-group: <value of string>
                     internet-service-src-id: <value of string>
                     ip-version: <value in [4, 6]>
                     name: <value of string>
                     per-ip-shaper: <value of string>
                     schedule: <value of string>
                     service: <value of string>
                     srcaddr: <value of string>
                     srcaddr6: <value of string>
                     srcintf: <value of string>
                     status: <value in [disable, enable]>
                     tos: <value of string>
                     tos-mask: <value of string>
                     tos-negate: <value in [disable, enable]>
                     traffic-shaper: <value of string>
                     traffic-shaper-reverse: <value of string>
                     url-category: <value of string>
                     users: <value of string>
    - name: send request to /pm/config/pkg/{pkg}/header/shaping-policy
      fmgr_pm_config_pkg_pkg_header_shaping_policy:
         method: <value in [get]>
         url_params:
            pkg: <value of string>
         params:
            - 
               attr: <value of string>
               fields: 
                - 
                   - <value in [app-category, app-group, application, ...]>
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
         data:
            type: array
            suboptions:
               id:
                  type: int
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/global/pkg/{pkg}/global/header/shaping-policy
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
               app-category:
                  type: str
               app-group:
                  type: str
               application:
                  type: array
                  suboptions:
                     type: int
               class-id:
                  type: int
               comment:
                  type: str
               diffserv-forward:
                  type: str
               diffserv-reverse:
                  type: str
               diffservcode-forward:
                  type: str
               diffservcode-rev:
                  type: str
               dstaddr:
                  type: str
               dstaddr6:
                  type: str
               dstintf:
                  type: str
               groups:
                  type: str
               id:
                  type: int
               internet-service:
                  type: str
               internet-service-custom:
                  type: str
               internet-service-custom-group:
                  type: str
               internet-service-group:
                  type: str
               internet-service-id:
                  type: str
               internet-service-src:
                  type: str
               internet-service-src-custom:
                  type: str
               internet-service-src-custom-group:
                  type: str
               internet-service-src-group:
                  type: str
               internet-service-src-id:
                  type: str
               ip-version:
                  type: str
               name:
                  type: str
               per-ip-shaper:
                  type: str
               schedule:
                  type: str
               service:
                  type: str
               srcaddr:
                  type: str
               srcaddr6:
                  type: str
               srcintf:
                  type: str
               status:
                  type: str
               tos:
                  type: str
               tos-mask:
                  type: str
               tos-negate:
                  type: str
               traffic-shaper:
                  type: str
               traffic-shaper-reverse:
                  type: str
               url-category:
                  type: str
               users:
                  type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/global/pkg/{pkg}/global/header/shaping-policy

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
        '/pm/config/global/pkg/{pkg}/global/header/shaping-policy'
    ]

    url_schema = [
        {
            'name': 'pkg',
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
                        'app-category': {
                            'type': 'string'
                        },
                        'app-group': {
                            'type': 'string'
                        },
                        'application': {
                            'type': 'array',
                            'items': {
                                'type': 'integer'
                            }
                        },
                        'class-id': {
                            'type': 'integer'
                        },
                        'comment': {
                            'type': 'string'
                        },
                        'diffserv-forward': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'diffserv-reverse': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'diffservcode-forward': {
                            'type': 'string'
                        },
                        'diffservcode-rev': {
                            'type': 'string'
                        },
                        'dstaddr': {
                            'type': 'string'
                        },
                        'dstaddr6': {
                            'type': 'string'
                        },
                        'dstintf': {
                            'type': 'string'
                        },
                        'groups': {
                            'type': 'string'
                        },
                        'id': {
                            'type': 'integer'
                        },
                        'internet-service': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'internet-service-custom': {
                            'type': 'string'
                        },
                        'internet-service-custom-group': {
                            'type': 'string'
                        },
                        'internet-service-group': {
                            'type': 'string'
                        },
                        'internet-service-id': {
                            'type': 'string'
                        },
                        'internet-service-src': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'internet-service-src-custom': {
                            'type': 'string'
                        },
                        'internet-service-src-custom-group': {
                            'type': 'string'
                        },
                        'internet-service-src-group': {
                            'type': 'string'
                        },
                        'internet-service-src-id': {
                            'type': 'string'
                        },
                        'ip-version': {
                            'type': 'string',
                            'enum': [
                                '4',
                                '6'
                            ]
                        },
                        'name': {
                            'type': 'string'
                        },
                        'per-ip-shaper': {
                            'type': 'string'
                        },
                        'schedule': {
                            'type': 'string'
                        },
                        'service': {
                            'type': 'string'
                        },
                        'srcaddr': {
                            'type': 'string'
                        },
                        'srcaddr6': {
                            'type': 'string'
                        },
                        'srcintf': {
                            'type': 'string'
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'tos': {
                            'type': 'string'
                        },
                        'tos-mask': {
                            'type': 'string'
                        },
                        'tos-negate': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'traffic-shaper': {
                            'type': 'string'
                        },
                        'traffic-shaper-reverse': {
                            'type': 'string'
                        },
                        'url-category': {
                            'type': 'string'
                        },
                        'users': {
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
                                'app-category',
                                'app-group',
                                'application',
                                'class-id',
                                'comment',
                                'diffserv-forward',
                                'diffserv-reverse',
                                'diffservcode-forward',
                                'diffservcode-rev',
                                'dstaddr',
                                'dstaddr6',
                                'dstintf',
                                'groups',
                                'id',
                                'internet-service',
                                'internet-service-custom',
                                'internet-service-custom-group',
                                'internet-service-group',
                                'internet-service-id',
                                'internet-service-src',
                                'internet-service-src-custom',
                                'internet-service-src-custom-group',
                                'internet-service-src-group',
                                'internet-service-src-id',
                                'ip-version',
                                'name',
                                'per-ip-shaper',
                                'schedule',
                                'service',
                                'srcaddr',
                                'srcaddr6',
                                'srcintf',
                                'status',
                                'tos',
                                'tos-mask',
                                'tos-negate',
                                'traffic-shaper',
                                'traffic-shaper-reverse',
                                'url-category',
                                'users'
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