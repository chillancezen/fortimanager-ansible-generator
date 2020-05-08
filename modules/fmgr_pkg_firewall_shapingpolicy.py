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
module: fmgr_pkg_firewall_shapingpolicy
short_description: Configure shaping policies.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/pkg/{pkg}/firewall/shaping-policy
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
            pkg:
                type: str
    schema_object0:
        methods: [add, set, update]
        description: 'Configure shaping policies.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    app-category:
                        type: str
                        description: 'IDs of one or more application categories that this shaper applies application control traffic shaping to.'
                    application:
                        -
                            type: int
                    dstaddr:
                        type: str
                        description: 'IPv4 destination address and address group names.'
                    dstaddr6:
                        type: str
                        description: 'IPv6 destination address and address group names.'
                    dstintf:
                        type: str
                        description: 'One or more outgoing (egress) interfaces.'
                    groups:
                        type: str
                        description: 'Apply this traffic shaping policy to user groups that have authenticated with the FortiGate.'
                    id:
                        type: int
                        description: 'Shaping policy ID.'
                    ip-version:
                        type: str
                        description: 'Apply this traffic shaping policy to IPv4 or IPv6 traffic.'
                        choices:
                            - '4'
                            - '6'
                    per-ip-shaper:
                        type: str
                        description: 'Per-IP traffic shaper to apply with this policy.'
                    schedule:
                        type: str
                        description: 'Schedule name.'
                    service:
                        type: str
                        description: 'Service and service group names.'
                    srcaddr:
                        type: str
                        description: 'IPv4 source address and address group names.'
                    srcaddr6:
                        type: str
                        description: 'IPv6 source address and address group names.'
                    status:
                        type: str
                        description: 'Enable/disable this traffic shaping policy.'
                        choices:
                            - 'disable'
                            - 'enable'
                    traffic-shaper:
                        type: str
                        description: 'Traffic shaper to apply to traffic forwarded by the firewall policy.'
                    traffic-shaper-reverse:
                        type: str
                        description: 'Traffic shaper to apply to response traffic received by the firewall policy.'
                    url-category:
                        type: str
                        description: 'IDs of one or more FortiGuard Web Filtering categories that this shaper applies traffic shaping to.'
                    users:
                        type: str
                        description: 'Apply this traffic shaping policy to individual users that have authenticated with the FortiGate.'
    schema_object1:
        methods: [get]
        description: 'Configure shaping policies.'
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
                            - 'app-category'
                            - 'application'
                            - 'dstaddr'
                            - 'dstaddr6'
                            - 'dstintf'
                            - 'groups'
                            - 'id'
                            - 'ip-version'
                            - 'per-ip-shaper'
                            - 'schedule'
                            - 'service'
                            - 'srcaddr'
                            - 'srcaddr6'
                            - 'status'
                            - 'traffic-shaper'
                            - 'traffic-shaper-reverse'
                            - 'url-category'
                            - 'users'
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

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/SHAPING-POLICY
      fmgr_pkg_firewall_shapingpolicy:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
         params:
            -
               data:
                 -
                     app-category: <value of string>
                     application:
                       - <value of integer>
                     dstaddr: <value of string>
                     dstaddr6: <value of string>
                     dstintf: <value of string>
                     groups: <value of string>
                     id: <value of integer>
                     ip-version: <value in [4, 6]>
                     per-ip-shaper: <value of string>
                     schedule: <value of string>
                     service: <value of string>
                     srcaddr: <value of string>
                     srcaddr6: <value of string>
                     status: <value in [disable, enable]>
                     traffic-shaper: <value of string>
                     traffic-shaper-reverse: <value of string>
                     url-category: <value of string>
                     users: <value of string>

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/SHAPING-POLICY
      fmgr_pkg_firewall_shapingpolicy:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [app-category, application, dstaddr, ...]>
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
                  description: 'Shaping policy ID.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/pkg/{pkg}/firewall/shaping-policy'
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
                  description: 'IDs of one or more application categories that this shaper applies application control traffic shaping to.'
               application:
                  type: array
                  suboptions:
                     type: int
               dstaddr:
                  type: str
                  description: 'IPv4 destination address and address group names.'
               dstaddr6:
                  type: str
                  description: 'IPv6 destination address and address group names.'
               dstintf:
                  type: str
                  description: 'One or more outgoing (egress) interfaces.'
               groups:
                  type: str
                  description: 'Apply this traffic shaping policy to user groups that have authenticated with the FortiGate.'
               id:
                  type: int
                  description: 'Shaping policy ID.'
               ip-version:
                  type: str
                  description: 'Apply this traffic shaping policy to IPv4 or IPv6 traffic.'
               per-ip-shaper:
                  type: str
                  description: 'Per-IP traffic shaper to apply with this policy.'
               schedule:
                  type: str
                  description: 'Schedule name.'
               service:
                  type: str
                  description: 'Service and service group names.'
               srcaddr:
                  type: str
                  description: 'IPv4 source address and address group names.'
               srcaddr6:
                  type: str
                  description: 'IPv6 source address and address group names.'
               status:
                  type: str
                  description: 'Enable/disable this traffic shaping policy.'
               traffic-shaper:
                  type: str
                  description: 'Traffic shaper to apply to traffic forwarded by the firewall policy.'
               traffic-shaper-reverse:
                  type: str
                  description: 'Traffic shaper to apply to response traffic received by the firewall policy.'
               url-category:
                  type: str
                  description: 'IDs of one or more FortiGuard Web Filtering categories that this shaper applies traffic shaping to.'
               users:
                  type: str
                  description: 'Apply this traffic shaping policy to individual users that have authenticated with the FortiGate.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/pkg/{pkg}/firewall/shaping-policy'

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
        '/pm/config/adom/{adom}/pkg/{pkg}/firewall/shaping-policy'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'pkg',
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
                        'app-category': {
                            'type': 'string'
                        },
                        'application': {
                            'type': 'array',
                            'items': {
                                'type': 'integer'
                            }
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
                        'ip-version': {
                            'type': 'string',
                            'enum': [
                                '4',
                                '6'
                            ]
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
                        'status': {
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
                                'application',
                                'dstaddr',
                                'dstaddr6',
                                'dstintf',
                                'groups',
                                'id',
                                'ip-version',
                                'per-ip-shaper',
                                'schedule',
                                'service',
                                'srcaddr',
                                'srcaddr6',
                                'status',
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
