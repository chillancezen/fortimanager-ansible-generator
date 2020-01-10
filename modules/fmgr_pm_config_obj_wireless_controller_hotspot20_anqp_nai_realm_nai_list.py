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
module: fmgr_pm_config_obj_wireless_controller_hotspot20_anqp_nai_realm_nai_list
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/wireless-controller/hotspot20/anqp-nai-realm/{anqp-nai-realm}/nai-list
    - /pm/config/global/obj/wireless-controller/hotspot20/anqp-nai-realm/{anqp-nai-realm}/nai-list
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
            anqp-nai-realm:
                type: str
    schema_object0:
        methods: [add, set, update]
        description: 'NAI list.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    eap-method:
                        -
                            auth-param:
                                -
                                    id:
                                        type: str
                                        description: 'ID of authentication parameter.'
                                        choices:
                                            - 'non-eap-inner-auth'
                                            - 'inner-auth-eap'
                                            - 'credential'
                                            - 'tunneled-credential'
                                    index:
                                        type: int
                                        description: 'Param index.'
                                    val:
                                        type: str
                                        description: 'Value of authentication parameter.'
                                        choices:
                                            - 'eap-identity'
                                            - 'eap-md5'
                                            - 'eap-tls'
                                            - 'eap-ttls'
                                            - 'eap-peap'
                                            - 'eap-sim'
                                            - 'eap-aka'
                                            - 'eap-aka-prime'
                                            - 'non-eap-pap'
                                            - 'non-eap-chap'
                                            - 'non-eap-mschap'
                                            - 'non-eap-mschapv2'
                                            - 'cred-sim'
                                            - 'cred-usim'
                                            - 'cred-nfc'
                                            - 'cred-hardware-token'
                                            - 'cred-softoken'
                                            - 'cred-certificate'
                                            - 'cred-user-pwd'
                                            - 'cred-none'
                                            - 'cred-vendor-specific'
                                            - 'tun-cred-sim'
                                            - 'tun-cred-usim'
                                            - 'tun-cred-nfc'
                                            - 'tun-cred-hardware-token'
                                            - 'tun-cred-softoken'
                                            - 'tun-cred-certificate'
                                            - 'tun-cred-user-pwd'
                                            - 'tun-cred-anonymous'
                                            - 'tun-cred-vendor-specific'
                            index:
                                type: int
                                description: 'EAP method index.'
                            method:
                                type: str
                                description: 'EAP method type.'
                                choices:
                                    - 'eap-identity'
                                    - 'eap-md5'
                                    - 'eap-tls'
                                    - 'eap-ttls'
                                    - 'eap-peap'
                                    - 'eap-sim'
                                    - 'eap-aka'
                                    - 'eap-aka-prime'
                    encoding:
                        type: str
                        description: 'Enable/disable format in accordance with IETF RFC 4282.'
                        choices:
                            - 'disable'
                            - 'enable'
                    nai-realm:
                        type: str
                        description: 'Configure NAI realms (delimited by a semi-colon character).'
                    name:
                        type: str
                        description: 'NAI realm name.'
    schema_object1:
        methods: [get]
        description: 'NAI list.'
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
                            - 'encoding'
                            - 'nai-realm'
                            - 'name'
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

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/HOTSPOT20/ANQP-NAI-REALM/{ANQP-NAI-REALM}/NAI-LIST
      fmgr_pm_config_obj_wireless_controller_hotspot20_anqp_nai_realm_nai_list:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            anqp-nai-realm: <value of string>
         params:
            -
               data:
                 -
                     eap-method:
                       -
                           auth-param:
                             -
                                 id: <value in [non-eap-inner-auth, inner-auth-eap, credential, ...]>
                                 index: <value of integer>
                                 val: <value in [eap-identity, eap-md5, eap-tls, ...]>
                           index: <value of integer>
                           method: <value in [eap-identity, eap-md5, eap-tls, ...]>
                     encoding: <value in [disable, enable]>
                     nai-realm: <value of string>
                     name: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/HOTSPOT20/ANQP-NAI-REALM/{ANQP-NAI-REALM}/NAI-LIST
      fmgr_pm_config_obj_wireless_controller_hotspot20_anqp_nai_realm_nai_list:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            anqp-nai-realm: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [encoding, nai-realm, name]>
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
            example: '/pm/config/adom/{adom}/obj/wireless-controller/hotspot20/anqp-nai-realm/{anq...'
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
               eap-method:
                  type: array
                  suboptions:
                     auth-param:
                        type: array
                        suboptions:
                           id:
                              type: str
                              description: 'ID of authentication parameter.'
                           index:
                              type: int
                              description: 'Param index.'
                           val:
                              type: str
                              description: 'Value of authentication parameter.'
                     index:
                        type: int
                        description: 'EAP method index.'
                     method:
                        type: str
                        description: 'EAP method type.'
               encoding:
                  type: str
                  description: 'Enable/disable format in accordance with IETF RFC 4282.'
               nai-realm:
                  type: str
                  description: 'Configure NAI realms (delimited by a semi-colon character).'
               name:
                  type: str
                  description: 'NAI realm name.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/wireless-controller/hotspot20/anqp-nai-realm/{anq...'

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
        '/pm/config/adom/{adom}/obj/wireless-controller/hotspot20/anqp-nai-realm/{anqp-nai-realm}/nai-list',
        '/pm/config/global/obj/wireless-controller/hotspot20/anqp-nai-realm/{anqp-nai-realm}/nai-list'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'anqp-nai-realm',
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
                        'eap-method': {
                            'type': 'array',
                            'items': {
                                'auth-param': {
                                    'type': 'array',
                                    'items': {
                                        'id': {
                                            'type': 'string',
                                            'enum': [
                                                'non-eap-inner-auth',
                                                'inner-auth-eap',
                                                'credential',
                                                'tunneled-credential'
                                            ]
                                        },
                                        'index': {
                                            'type': 'integer'
                                        },
                                        'val': {
                                            'type': 'string',
                                            'enum': [
                                                'eap-identity',
                                                'eap-md5',
                                                'eap-tls',
                                                'eap-ttls',
                                                'eap-peap',
                                                'eap-sim',
                                                'eap-aka',
                                                'eap-aka-prime',
                                                'non-eap-pap',
                                                'non-eap-chap',
                                                'non-eap-mschap',
                                                'non-eap-mschapv2',
                                                'cred-sim',
                                                'cred-usim',
                                                'cred-nfc',
                                                'cred-hardware-token',
                                                'cred-softoken',
                                                'cred-certificate',
                                                'cred-user-pwd',
                                                'cred-none',
                                                'cred-vendor-specific',
                                                'tun-cred-sim',
                                                'tun-cred-usim',
                                                'tun-cred-nfc',
                                                'tun-cred-hardware-token',
                                                'tun-cred-softoken',
                                                'tun-cred-certificate',
                                                'tun-cred-user-pwd',
                                                'tun-cred-anonymous',
                                                'tun-cred-vendor-specific'
                                            ]
                                        }
                                    }
                                },
                                'index': {
                                    'type': 'integer'
                                },
                                'method': {
                                    'type': 'string',
                                    'enum': [
                                        'eap-identity',
                                        'eap-md5',
                                        'eap-tls',
                                        'eap-ttls',
                                        'eap-peap',
                                        'eap-sim',
                                        'eap-aka',
                                        'eap-aka-prime'
                                    ]
                                }
                            }
                        },
                        'encoding': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'nai-realm': {
                            'type': 'string'
                        },
                        'name': {
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
                                'encoding',
                                'nai-realm',
                                'name'
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

    module.exit_json(**response[1])


if __name__ == '__main__':
    main()
