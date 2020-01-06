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
module: fmgr_pm_config_obj_user_local
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/user/local
    - /pm/config/global/obj/user/local
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
        description: 'Configure local users.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    auth-concurrent-override:
                        type: str
                        description: 'Enable/disable overriding the policy-auth-concurrent under config system global.'
                        choices:
                            - disable
                            - enable
                    auth-concurrent-value:
                        type: int
                        description: 'Maximum number of concurrent logins permitted from the same user.'
                    authtimeout:
                        type: int
                        description: 'Time in minutes before the authentication timeout for a user is reached.'
                    email-to:
                        type: str
                        description: 'Two-factor recipient's email address.'
                    fortitoken:
                        type: str
                        description: 'Two-factor recipient's FortiToken serial number.'
                    id:
                        type: int
                        description: 'User ID.'
                    ldap-server:
                        type: str
                        description: 'Name of LDAP server with which the user must authenticate.'
                    name:
                        type: str
                        description: 'User name.'
                    passwd:
                        -
                            type: str
                    passwd-policy:
                        type: str
                        description: 'Password policy to apply to this user, as defined in config user password-policy.'
                    ppk-identity:
                        type: str
                        description: 'IKEv2 Postquantum Preshared Key Identity.'
                    ppk-secret:
                        -
                            type: str
                    radius-server:
                        type: str
                        description: 'Name of RADIUS server with which the user must authenticate.'
                    sms-custom-server:
                        type: str
                        description: 'Two-factor recipient's SMS server.'
                    sms-phone:
                        type: str
                        description: 'Two-factor recipient's mobile phone number.'
                    sms-server:
                        type: str
                        description: 'Send SMS through FortiGuard or other external server.'
                        choices:
                            - fortiguard
                            - custom
                    status:
                        type: str
                        description: 'Enable/disable allowing the local user to authenticate with the FortiGate unit.'
                        choices:
                            - disable
                            - enable
                    tacacs+-server:
                        type: str
                        description: 'Name of TACACS+ server with which the user must authenticate.'
                    two-factor:
                        type: str
                        description: 'Enable/disable two-factor authentication.'
                        choices:
                            - disable
                            - fortitoken
                            - email
                            - sms
                            - fortitoken-cloud
                    type:
                        type: str
                        description: 'Authentication method.'
                        choices:
                            - password
                            - radius
                            - tacacs+
                            - ldap
                    workstation:
                        type: str
                        description: 'Name of the remote user workstation, if you want to limit the user to authenticate only from a particular workstation.'
    schema_object1:
        methods: [get]
        description: 'Configure local users.'
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
                            - auth-concurrent-override
                            - auth-concurrent-value
                            - authtimeout
                            - email-to
                            - fortitoken
                            - id
                            - ldap-server
                            - name
                            - passwd
                            - passwd-policy
                            - ppk-identity
                            - ppk-secret
                            - radius-server
                            - sms-custom-server
                            - sms-phone
                            - sms-server
                            - status
                            - tacacs+-server
                            - two-factor
                            - type
                            - workstation
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
    - name: send request to /pm/config/obj/user/local
      fmgr_pm_config_obj_user_local:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            - 
               data: 
                - 
                     auth-concurrent-override: <value in [disable, enable]>
                     auth-concurrent-value: <value of integer>
                     authtimeout: <value of integer>
                     email-to: <value of string>
                     fortitoken: <value of string>
                     id: <value of integer>
                     ldap-server: <value of string>
                     name: <value of string>
                     passwd: 
                      - <value of string>
                     passwd-policy: <value of string>
                     ppk-identity: <value of string>
                     ppk-secret: 
                      - <value of string>
                     radius-server: <value of string>
                     sms-custom-server: <value of string>
                     sms-phone: <value of string>
                     sms-server: <value in [fortiguard, custom]>
                     status: <value in [disable, enable]>
                     tacacs+-server: <value of string>
                     two-factor: <value in [disable, fortitoken, email, ...]>
                     type: <value in [password, radius, tacacs+, ...]>
                     workstation: <value of string>
    - name: send request to /pm/config/obj/user/local
      fmgr_pm_config_obj_user_local:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            - 
               attr: <value of string>
               fields: 
                - 
                   - <value in [auth-concurrent-override, auth-concurrent-value, authtimeout, ...]>
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
            example: /pm/config/adom/{adom}/obj/user/local
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
               auth-concurrent-override:
                  type: str
                  description: 'Enable/disable overriding the policy-auth-concurrent under config system global.'
               auth-concurrent-value:
                  type: int
                  description: 'Maximum number of concurrent logins permitted from the same user.'
               authtimeout:
                  type: int
                  description: 'Time in minutes before the authentication timeout for a user is reached.'
               email-to:
                  type: str
                  description: 'Two-factor recipient's email address.'
               fortitoken:
                  type: str
                  description: 'Two-factor recipient's FortiToken serial number.'
               id:
                  type: int
                  description: 'User ID.'
               ldap-server:
                  type: str
                  description: 'Name of LDAP server with which the user must authenticate.'
               name:
                  type: str
                  description: 'User name.'
               passwd:
                  type: array
                  suboptions:
                     type: str
               passwd-policy:
                  type: str
                  description: 'Password policy to apply to this user, as defined in config user password-policy.'
               ppk-identity:
                  type: str
                  description: 'IKEv2 Postquantum Preshared Key Identity.'
               ppk-secret:
                  type: array
                  suboptions:
                     type: str
               radius-server:
                  type: str
                  description: 'Name of RADIUS server with which the user must authenticate.'
               sms-custom-server:
                  type: str
                  description: 'Two-factor recipient's SMS server.'
               sms-phone:
                  type: str
                  description: 'Two-factor recipient's mobile phone number.'
               sms-server:
                  type: str
                  description: 'Send SMS through FortiGuard or other external server.'
               status:
                  type: str
                  description: 'Enable/disable allowing the local user to authenticate with the FortiGate unit.'
               tacacs+-server:
                  type: str
                  description: 'Name of TACACS+ server with which the user must authenticate.'
               two-factor:
                  type: str
                  description: 'Enable/disable two-factor authentication.'
               type:
                  type: str
                  description: 'Authentication method.'
               workstation:
                  type: str
                  description: 'Name of the remote user workstation, if you want to limit the user to authenticate only from a particular workstation.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/obj/user/local

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
        '/pm/config/adom/{adom}/obj/user/local',
        '/pm/config/global/obj/user/local'
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
                        'auth-concurrent-override': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'auth-concurrent-value': {
                            'type': 'integer'
                        },
                        'authtimeout': {
                            'type': 'integer'
                        },
                        'email-to': {
                            'type': 'string'
                        },
                        'fortitoken': {
                            'type': 'string'
                        },
                        'id': {
                            'type': 'integer'
                        },
                        'ldap-server': {
                            'type': 'string'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'passwd': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'passwd-policy': {
                            'type': 'string'
                        },
                        'ppk-identity': {
                            'type': 'string'
                        },
                        'ppk-secret': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'radius-server': {
                            'type': 'string'
                        },
                        'sms-custom-server': {
                            'type': 'string'
                        },
                        'sms-phone': {
                            'type': 'string'
                        },
                        'sms-server': {
                            'type': 'string',
                            'enum': [
                                'fortiguard',
                                'custom'
                            ]
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'tacacs+-server': {
                            'type': 'string'
                        },
                        'two-factor': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'fortitoken',
                                'email',
                                'sms',
                                'fortitoken-cloud'
                            ]
                        },
                        'type': {
                            'type': 'string',
                            'enum': [
                                'password',
                                'radius',
                                'tacacs+',
                                'ldap'
                            ]
                        },
                        'workstation': {
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
                                'auth-concurrent-override',
                                'auth-concurrent-value',
                                'authtimeout',
                                'email-to',
                                'fortitoken',
                                'id',
                                'ldap-server',
                                'name',
                                'passwd',
                                'passwd-policy',
                                'ppk-identity',
                                'ppk-secret',
                                'radius-server',
                                'sms-custom-server',
                                'sms-phone',
                                'sms-server',
                                'status',
                                'tacacs+-server',
                                'two-factor',
                                'type',
                                'workstation'
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