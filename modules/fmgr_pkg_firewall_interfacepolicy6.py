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
module: fmgr_pkg_firewall_interfacepolicy6
short_description: Configure IPv6 interface policies.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/pkg/{pkg}/firewall/interface-policy6
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
            pkg:
                type: str
    schema_object0:
        methods: [add, set, update]
        description: 'Configure IPv6 interface policies.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    address-type:
                        type: str
                        choices:
                            - 'ipv4'
                            - 'ipv6'
                    application-list:
                        type: str
                        description: 'Application list name.'
                    application-list-status:
                        type: str
                        description: 'Enable/disable application control.'
                        choices:
                            - 'disable'
                            - 'enable'
                    av-profile:
                        type: str
                        description: 'Antivirus profile.'
                    av-profile-status:
                        type: str
                        description: 'Enable/disable antivirus.'
                        choices:
                            - 'disable'
                            - 'enable'
                    comments:
                        type: str
                        description: 'Comments.'
                    dlp-sensor:
                        type: str
                        description: 'DLP sensor name.'
                    dlp-sensor-status:
                        type: str
                        description: 'Enable/disable DLP.'
                        choices:
                            - 'disable'
                            - 'enable'
                    dsri:
                        type: str
                        description: 'Enable/disable DSRI.'
                        choices:
                            - 'disable'
                            - 'enable'
                    dstaddr6:
                        type: str
                        description: 'IPv6 address object to limit traffic monitoring to network traffic sent to the specified address or range.'
                    interface:
                        type: str
                        description: 'Monitored interface name from available interfaces.'
                    ips-sensor:
                        type: str
                        description: 'IPS sensor name.'
                    ips-sensor-status:
                        type: str
                        description: 'Enable/disable IPS.'
                        choices:
                            - 'disable'
                            - 'enable'
                    label:
                        type: str
                        description: 'Label.'
                    logtraffic:
                        type: str
                        description: 'Logging type to be used in this policy (Options: all | utm | disable, Default: utm).'
                        choices:
                            - 'disable'
                            - 'all'
                            - 'utm'
                    policyid:
                        type: int
                        description: 'Policy ID.'
                    scan-botnet-connections:
                        type: str
                        description: 'Enable/disable scanning for connections to Botnet servers.'
                        choices:
                            - 'disable'
                            - 'block'
                            - 'monitor'
                    service6:
                        type: str
                        description: 'Service name.'
                    spamfilter-profile:
                        type: str
                        description: 'Antispam profile.'
                    spamfilter-profile-status:
                        type: str
                        description: 'Enable/disable antispam.'
                        choices:
                            - 'disable'
                            - 'enable'
                    srcaddr6:
                        type: str
                        description: 'IPv6 address object to limit traffic monitoring to network traffic sent from the specified address or range.'
                    status:
                        type: str
                        description: 'Enable/disable this policy.'
                        choices:
                            - 'disable'
                            - 'enable'
                    webfilter-profile:
                        type: str
                        description: 'Web filter profile.'
                    webfilter-profile-status:
                        type: str
                        description: 'Enable/disable web filtering.'
                        choices:
                            - 'disable'
                            - 'enable'
    schema_object1:
        methods: [get]
        description: 'Configure IPv6 interface policies.'
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
                            - 'address-type'
                            - 'application-list'
                            - 'application-list-status'
                            - 'av-profile'
                            - 'av-profile-status'
                            - 'comments'
                            - 'dlp-sensor'
                            - 'dlp-sensor-status'
                            - 'dsri'
                            - 'dstaddr6'
                            - 'interface'
                            - 'ips-sensor'
                            - 'ips-sensor-status'
                            - 'label'
                            - 'logtraffic'
                            - 'policyid'
                            - 'scan-botnet-connections'
                            - 'service6'
                            - 'spamfilter-profile'
                            - 'spamfilter-profile-status'
                            - 'srcaddr6'
                            - 'status'
                            - 'webfilter-profile'
                            - 'webfilter-profile-status'
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

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/INTERFACE-POLICY6
      fmgr_pkg_firewall_interfacepolicy6:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
         params:
            -
               data:
                 -
                     address-type: <value in [ipv4, ipv6]>
                     application-list: <value of string>
                     application-list-status: <value in [disable, enable]>
                     av-profile: <value of string>
                     av-profile-status: <value in [disable, enable]>
                     comments: <value of string>
                     dlp-sensor: <value of string>
                     dlp-sensor-status: <value in [disable, enable]>
                     dsri: <value in [disable, enable]>
                     dstaddr6: <value of string>
                     interface: <value of string>
                     ips-sensor: <value of string>
                     ips-sensor-status: <value in [disable, enable]>
                     label: <value of string>
                     logtraffic: <value in [disable, all, utm]>
                     policyid: <value of integer>
                     scan-botnet-connections: <value in [disable, block, monitor]>
                     service6: <value of string>
                     spamfilter-profile: <value of string>
                     spamfilter-profile-status: <value in [disable, enable]>
                     srcaddr6: <value of string>
                     status: <value in [disable, enable]>
                     webfilter-profile: <value of string>
                     webfilter-profile-status: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/INTERFACE-POLICY6
      fmgr_pkg_firewall_interfacepolicy6:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [address-type, application-list, application-list-status, ...]>
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
               policyid:
                  type: int
                  description: 'Policy ID.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/pkg/{pkg}/firewall/interface-policy6'
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
               address-type:
                  type: str
               application-list:
                  type: str
                  description: 'Application list name.'
               application-list-status:
                  type: str
                  description: 'Enable/disable application control.'
               av-profile:
                  type: str
                  description: 'Antivirus profile.'
               av-profile-status:
                  type: str
                  description: 'Enable/disable antivirus.'
               comments:
                  type: str
                  description: 'Comments.'
               dlp-sensor:
                  type: str
                  description: 'DLP sensor name.'
               dlp-sensor-status:
                  type: str
                  description: 'Enable/disable DLP.'
               dsri:
                  type: str
                  description: 'Enable/disable DSRI.'
               dstaddr6:
                  type: str
                  description: 'IPv6 address object to limit traffic monitoring to network traffic sent to the specified address or range.'
               interface:
                  type: str
                  description: 'Monitored interface name from available interfaces.'
               ips-sensor:
                  type: str
                  description: 'IPS sensor name.'
               ips-sensor-status:
                  type: str
                  description: 'Enable/disable IPS.'
               label:
                  type: str
                  description: 'Label.'
               logtraffic:
                  type: str
                  description: 'Logging type to be used in this policy (Options: all | utm | disable, Default: utm).'
               policyid:
                  type: int
                  description: 'Policy ID.'
               scan-botnet-connections:
                  type: str
                  description: 'Enable/disable scanning for connections to Botnet servers.'
               service6:
                  type: str
                  description: 'Service name.'
               spamfilter-profile:
                  type: str
                  description: 'Antispam profile.'
               spamfilter-profile-status:
                  type: str
                  description: 'Enable/disable antispam.'
               srcaddr6:
                  type: str
                  description: 'IPv6 address object to limit traffic monitoring to network traffic sent from the specified address or range.'
               status:
                  type: str
                  description: 'Enable/disable this policy.'
               webfilter-profile:
                  type: str
                  description: 'Web filter profile.'
               webfilter-profile-status:
                  type: str
                  description: 'Enable/disable web filtering.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/pkg/{pkg}/firewall/interface-policy6'

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
        '/pm/config/adom/{adom}/pkg/{pkg}/firewall/interface-policy6'
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
                        'address-type': {
                            'type': 'string',
                            'enum': [
                                'ipv4',
                                'ipv6'
                            ]
                        },
                        'application-list': {
                            'type': 'string'
                        },
                        'application-list-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'av-profile': {
                            'type': 'string'
                        },
                        'av-profile-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'comments': {
                            'type': 'string'
                        },
                        'dlp-sensor': {
                            'type': 'string'
                        },
                        'dlp-sensor-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dsri': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dstaddr6': {
                            'type': 'string'
                        },
                        'interface': {
                            'type': 'string'
                        },
                        'ips-sensor': {
                            'type': 'string'
                        },
                        'ips-sensor-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'label': {
                            'type': 'string'
                        },
                        'logtraffic': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'all',
                                'utm'
                            ]
                        },
                        'policyid': {
                            'type': 'integer'
                        },
                        'scan-botnet-connections': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'block',
                                'monitor'
                            ]
                        },
                        'service6': {
                            'type': 'string'
                        },
                        'spamfilter-profile': {
                            'type': 'string'
                        },
                        'spamfilter-profile-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
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
                        'webfilter-profile': {
                            'type': 'string'
                        },
                        'webfilter-profile-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
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
                                'address-type',
                                'application-list',
                                'application-list-status',
                                'av-profile',
                                'av-profile-status',
                                'comments',
                                'dlp-sensor',
                                'dlp-sensor-status',
                                'dsri',
                                'dstaddr6',
                                'interface',
                                'ips-sensor',
                                'ips-sensor-status',
                                'label',
                                'logtraffic',
                                'policyid',
                                'scan-botnet-connections',
                                'service6',
                                'spamfilter-profile',
                                'spamfilter-profile-status',
                                'srcaddr6',
                                'status',
                                'webfilter-profile',
                                'webfilter-profile-status'
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
