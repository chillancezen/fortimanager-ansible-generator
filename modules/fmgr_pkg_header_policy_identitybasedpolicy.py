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
module: fmgr_pkg_header_policy_identitybasedpolicy
short_description: no description
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/global/pkg/{pkg}/global/header/policy/{policy}/identity-based-policy
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
            pkg:
                type: str
            policy:
                type: str
    schema_object0:
        methods: [add, set, update]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    action:
                        type: str
                        choices:
                            - 'deny'
                            - 'accept'
                    application-charts:
                        -
                            type: str
                            choices:
                                - 'top10-app'
                                - 'top10-p2p-user'
                                - 'top10-media-user'
                    application-list:
                        type: str
                    av-profile:
                        type: str
                    capture-packet:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    deep-inspection-options:
                        type: str
                    devices:
                        type: str
                    dlp-sensor:
                        type: str
                    dstaddr:
                        type: str
                    dstaddr-negate:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    endpoint-compliance:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    groups:
                        type: str
                    icap-profile:
                        type: str
                    id:
                        type: int
                    ips-sensor:
                        type: str
                    logtraffic:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                            - 'all'
                            - 'utm'
                    logtraffic-app:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    logtraffic-start:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    mms-profile:
                        type: str
                    per-ip-shaper:
                        type: str
                    profile-group:
                        type: str
                    profile-protocol-options:
                        type: str
                    profile-type:
                        type: str
                        choices:
                            - 'single'
                            - 'group'
                    replacemsg-group:
                        type: str
                    schedule:
                        type: str
                    send-deny-packet:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    service:
                        type: str
                    service-negate:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    spamfilter-profile:
                        type: str
                    sslvpn-portal:
                        type: str
                    sslvpn-realm:
                        type: str
                    traffic-shaper:
                        type: str
                    traffic-shaper-reverse:
                        type: str
                    users:
                        type: str
                    utm-status:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    voip-profile:
                        type: str
                    webfilter-profile:
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
                            - 'action'
                            - 'application-charts'
                            - 'application-list'
                            - 'av-profile'
                            - 'capture-packet'
                            - 'deep-inspection-options'
                            - 'devices'
                            - 'dlp-sensor'
                            - 'dstaddr'
                            - 'dstaddr-negate'
                            - 'endpoint-compliance'
                            - 'groups'
                            - 'icap-profile'
                            - 'id'
                            - 'ips-sensor'
                            - 'logtraffic'
                            - 'logtraffic-app'
                            - 'logtraffic-start'
                            - 'mms-profile'
                            - 'per-ip-shaper'
                            - 'profile-group'
                            - 'profile-protocol-options'
                            - 'profile-type'
                            - 'replacemsg-group'
                            - 'schedule'
                            - 'send-deny-packet'
                            - 'service'
                            - 'service-negate'
                            - 'spamfilter-profile'
                            - 'sslvpn-portal'
                            - 'sslvpn-realm'
                            - 'traffic-shaper'
                            - 'traffic-shaper-reverse'
                            - 'users'
                            - 'utm-status'
                            - 'voip-profile'
                            - 'webfilter-profile'
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

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/HEADER/POLICY/{POLICY}/IDENTITY-BASED-POLICY
      fmgr_pkg_header_policy_identitybasedpolicy:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [add, set, update]>
         url_params:
            pkg: <value of string>
            policy: <value of string>
         params:
            -
               data:
                 -
                     action: <value in [deny, accept]>
                     application-charts:
                       - <value in [top10-app, top10-p2p-user, top10-media-user]>
                     application-list: <value of string>
                     av-profile: <value of string>
                     capture-packet: <value in [disable, enable]>
                     deep-inspection-options: <value of string>
                     devices: <value of string>
                     dlp-sensor: <value of string>
                     dstaddr: <value of string>
                     dstaddr-negate: <value in [disable, enable]>
                     endpoint-compliance: <value in [disable, enable]>
                     groups: <value of string>
                     icap-profile: <value of string>
                     id: <value of integer>
                     ips-sensor: <value of string>
                     logtraffic: <value in [disable, enable, all, ...]>
                     logtraffic-app: <value in [disable, enable]>
                     logtraffic-start: <value in [disable, enable]>
                     mms-profile: <value of string>
                     per-ip-shaper: <value of string>
                     profile-group: <value of string>
                     profile-protocol-options: <value of string>
                     profile-type: <value in [single, group]>
                     replacemsg-group: <value of string>
                     schedule: <value of string>
                     send-deny-packet: <value in [disable, enable]>
                     service: <value of string>
                     service-negate: <value in [disable, enable]>
                     spamfilter-profile: <value of string>
                     sslvpn-portal: <value of string>
                     sslvpn-realm: <value of string>
                     traffic-shaper: <value of string>
                     traffic-shaper-reverse: <value of string>
                     users: <value of string>
                     utm-status: <value in [disable, enable]>
                     voip-profile: <value of string>
                     webfilter-profile: <value of string>

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/HEADER/POLICY/{POLICY}/IDENTITY-BASED-POLICY
      fmgr_pkg_header_policy_identitybasedpolicy:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            pkg: <value of string>
            policy: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [action, application-charts, application-list, ...]>
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
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/global/pkg/{pkg}/global/header/policy/{policy}/identity-based-policy'
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
               application-charts:
                  type: array
                  suboptions:
                     type: str
               application-list:
                  type: str
               av-profile:
                  type: str
               capture-packet:
                  type: str
               deep-inspection-options:
                  type: str
               devices:
                  type: str
               dlp-sensor:
                  type: str
               dstaddr:
                  type: str
               dstaddr-negate:
                  type: str
               endpoint-compliance:
                  type: str
               groups:
                  type: str
               icap-profile:
                  type: str
               id:
                  type: int
               ips-sensor:
                  type: str
               logtraffic:
                  type: str
               logtraffic-app:
                  type: str
               logtraffic-start:
                  type: str
               mms-profile:
                  type: str
               per-ip-shaper:
                  type: str
               profile-group:
                  type: str
               profile-protocol-options:
                  type: str
               profile-type:
                  type: str
               replacemsg-group:
                  type: str
               schedule:
                  type: str
               send-deny-packet:
                  type: str
               service:
                  type: str
               service-negate:
                  type: str
               spamfilter-profile:
                  type: str
               sslvpn-portal:
                  type: str
               sslvpn-realm:
                  type: str
               traffic-shaper:
                  type: str
               traffic-shaper-reverse:
                  type: str
               users:
                  type: str
               utm-status:
                  type: str
               voip-profile:
                  type: str
               webfilter-profile:
                  type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/global/pkg/{pkg}/global/header/policy/{policy}/identity-based-policy'

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
        '/pm/config/global/pkg/{pkg}/global/header/policy/{policy}/identity-based-policy'
    ]

    url_schema = [
        {
            'name': 'pkg',
            'type': 'string'
        },
        {
            'name': 'policy',
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
                                'deny',
                                'accept'
                            ]
                        },
                        'application-charts': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'top10-app',
                                    'top10-p2p-user',
                                    'top10-media-user'
                                ]
                            }
                        },
                        'application-list': {
                            'type': 'string'
                        },
                        'av-profile': {
                            'type': 'string'
                        },
                        'capture-packet': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'deep-inspection-options': {
                            'type': 'string'
                        },
                        'devices': {
                            'type': 'string'
                        },
                        'dlp-sensor': {
                            'type': 'string'
                        },
                        'dstaddr': {
                            'type': 'string'
                        },
                        'dstaddr-negate': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'endpoint-compliance': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'groups': {
                            'type': 'string'
                        },
                        'icap-profile': {
                            'type': 'string'
                        },
                        'id': {
                            'type': 'integer'
                        },
                        'ips-sensor': {
                            'type': 'string'
                        },
                        'logtraffic': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable',
                                'all',
                                'utm'
                            ]
                        },
                        'logtraffic-app': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'logtraffic-start': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mms-profile': {
                            'type': 'string'
                        },
                        'per-ip-shaper': {
                            'type': 'string'
                        },
                        'profile-group': {
                            'type': 'string'
                        },
                        'profile-protocol-options': {
                            'type': 'string'
                        },
                        'profile-type': {
                            'type': 'string',
                            'enum': [
                                'single',
                                'group'
                            ]
                        },
                        'replacemsg-group': {
                            'type': 'string'
                        },
                        'schedule': {
                            'type': 'string'
                        },
                        'send-deny-packet': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'service': {
                            'type': 'string'
                        },
                        'service-negate': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'spamfilter-profile': {
                            'type': 'string'
                        },
                        'sslvpn-portal': {
                            'type': 'string'
                        },
                        'sslvpn-realm': {
                            'type': 'string'
                        },
                        'traffic-shaper': {
                            'type': 'string'
                        },
                        'traffic-shaper-reverse': {
                            'type': 'string'
                        },
                        'users': {
                            'type': 'string'
                        },
                        'utm-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'voip-profile': {
                            'type': 'string'
                        },
                        'webfilter-profile': {
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
                                'action',
                                'application-charts',
                                'application-list',
                                'av-profile',
                                'capture-packet',
                                'deep-inspection-options',
                                'devices',
                                'dlp-sensor',
                                'dstaddr',
                                'dstaddr-negate',
                                'endpoint-compliance',
                                'groups',
                                'icap-profile',
                                'id',
                                'ips-sensor',
                                'logtraffic',
                                'logtraffic-app',
                                'logtraffic-start',
                                'mms-profile',
                                'per-ip-shaper',
                                'profile-group',
                                'profile-protocol-options',
                                'profile-type',
                                'replacemsg-group',
                                'schedule',
                                'send-deny-packet',
                                'service',
                                'service-negate',
                                'spamfilter-profile',
                                'sslvpn-portal',
                                'sslvpn-realm',
                                'traffic-shaper',
                                'traffic-shaper-reverse',
                                'users',
                                'utm-status',
                                'voip-profile',
                                'webfilter-profile'
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
