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
module: fmgr_pm_config_obj_user_group_per_object
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/user/group/{group}
    - /pm/config/global/obj/user/group/{group}
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
            group:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Configure user groups.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                auth-concurrent-override:
                    type: str
                    description: 'Enable/disable overriding the global number of concurrent authentication sessions for this user group.'
                    choices:
                        - 'disable'
                        - 'enable'
                auth-concurrent-value:
                    type: int
                    description: 'Maximum number of concurrent authenticated connections per user (0 - 100).'
                authtimeout:
                    type: int
                    description: 'Authentication timeout in minutes for this user group. 0 to use the global user setting auth-timeout.'
                company:
                    type: str
                    description: 'Set the action for the company guest user field.'
                    choices:
                        - 'optional'
                        - 'mandatory'
                        - 'disabled'
                email:
                    type: str
                    description: 'Enable/disable the guest user email address field.'
                    choices:
                        - 'disable'
                        - 'enable'
                expire:
                    type: int
                    description: 'Time in seconds before guest user accounts expire. (1 - 31536000 sec)'
                expire-type:
                    type: str
                    description: 'Determine when the expiration countdown begins.'
                    choices:
                        - 'immediately'
                        - 'first-successful-login'
                group-type:
                    type: str
                    description: 'Set the group to be for firewall authentication, FSSO, RSSO, or guest users.'
                    choices:
                        - 'firewall'
                        - 'directory-service'
                        - 'fsso-service'
                        - 'guest'
                        - 'rsso'
                guest:
                    -
                        comment:
                            type: str
                            description: 'Comment.'
                        company:
                            type: str
                            description: 'Set the action for the company guest user field.'
                        email:
                            type: str
                            description: 'Email.'
                        expiration:
                            type: str
                            description: 'Expire time.'
                        mobile-phone:
                            type: str
                            description: 'Mobile phone.'
                        name:
                            type: str
                            description: 'Guest name.'
                        password:
                            -
                                type: str
                        sponsor:
                            type: str
                            description: 'Set the action for the sponsor guest user field.'
                        user-id:
                            type: str
                            description: 'Guest ID.'
                http-digest-realm:
                    type: str
                    description: 'Realm attribute for MD5-digest authentication.'
                id:
                    type: int
                    description: 'Group ID.'
                match:
                    -
                        _gui_meta:
                            type: str
                        group-name:
                            type: str
                            description: 'Name of matching group on remote authentication server.'
                        id:
                            type: int
                            description: 'ID.'
                        server-name:
                            type: str
                            description: 'Name of remote auth server.'
                max-accounts:
                    type: int
                    description: 'Maximum number of guest accounts that can be created for this group (0 means unlimited).'
                member:
                    type: str
                    description: 'Names of users, peers, LDAP severs, or RADIUS servers to add to the user group.'
                mobile-phone:
                    type: str
                    description: 'Enable/disable the guest user mobile phone number field.'
                    choices:
                        - 'disable'
                        - 'enable'
                multiple-guest-add:
                    type: str
                    description: 'Enable/disable addition of multiple guests.'
                    choices:
                        - 'disable'
                        - 'enable'
                name:
                    type: str
                    description: 'Group name.'
                password:
                    type: str
                    description: 'Guest user password type.'
                    choices:
                        - 'auto-generate'
                        - 'specify'
                        - 'disable'
                sms-custom-server:
                    type: str
                    description: 'SMS server.'
                sms-server:
                    type: str
                    description: 'Send SMS through FortiGuard or other external server.'
                    choices:
                        - 'fortiguard'
                        - 'custom'
                sponsor:
                    type: str
                    description: 'Set the action for the sponsor guest user field.'
                    choices:
                        - 'optional'
                        - 'mandatory'
                        - 'disabled'
                sso-attribute-value:
                    type: str
                    description: 'Name of the RADIUS user group that this local user group represents.'
                user-id:
                    type: str
                    description: 'Guest user ID type.'
                    choices:
                        - 'email'
                        - 'auto-generate'
                        - 'specify'
                user-name:
                    type: str
                    description: 'Enable/disable the guest user name entry.'
                    choices:
                        - 'disable'
                        - 'enable'
    schema_object1:
        methods: [delete]
        description: 'Configure user groups.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Configure user groups.'
        api_categories: [api_tag0]
        api_tag0:
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the object will be returned.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'chksum - Return the check-sum value instead of attributes.'
                choices:
                    - 'object member'
                    - 'chksum'
                    - 'datasrc'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/USER/GROUP/{GROUP}
      fmgr_pm_config_obj_user_group_per_object:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            group: <value of string>
         params:
            -
               data:
                  auth-concurrent-override: <value in [disable, enable]>
                  auth-concurrent-value: <value of integer>
                  authtimeout: <value of integer>
                  company: <value in [optional, mandatory, disabled]>
                  email: <value in [disable, enable]>
                  expire: <value of integer>
                  expire-type: <value in [immediately, first-successful-login]>
                  group-type: <value in [firewall, directory-service, fsso-service, ...]>
                  guest:
                    -
                        comment: <value of string>
                        company: <value of string>
                        email: <value of string>
                        expiration: <value of string>
                        mobile-phone: <value of string>
                        name: <value of string>
                        password:
                          - <value of string>
                        sponsor: <value of string>
                        user-id: <value of string>
                  http-digest-realm: <value of string>
                  id: <value of integer>
                  match:
                    -
                        _gui_meta: <value of string>
                        group-name: <value of string>
                        id: <value of integer>
                        server-name: <value of string>
                  max-accounts: <value of integer>
                  member: <value of string>
                  mobile-phone: <value in [disable, enable]>
                  multiple-guest-add: <value in [disable, enable]>
                  name: <value of string>
                  password: <value in [auto-generate, specify, disable]>
                  sms-custom-server: <value of string>
                  sms-server: <value in [fortiguard, custom]>
                  sponsor: <value in [optional, mandatory, disabled]>
                  sso-attribute-value: <value of string>
                  user-id: <value in [email, auto-generate, specify]>
                  user-name: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/USER/GROUP/{GROUP}
      fmgr_pm_config_obj_user_group_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            group: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[clone, delete, set, update]
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
            example: '/pm/config/adom/{adom}/obj/user/group/{group}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            auth-concurrent-override:
               type: str
               description: 'Enable/disable overriding the global number of concurrent authentication sessions for this user group.'
            auth-concurrent-value:
               type: int
               description: 'Maximum number of concurrent authenticated connections per user (0 - 100).'
            authtimeout:
               type: int
               description: 'Authentication timeout in minutes for this user group. 0 to use the global user setting auth-timeout.'
            company:
               type: str
               description: 'Set the action for the company guest user field.'
            email:
               type: str
               description: 'Enable/disable the guest user email address field.'
            expire:
               type: int
               description: 'Time in seconds before guest user accounts expire. (1 - 31536000 sec)'
            expire-type:
               type: str
               description: 'Determine when the expiration countdown begins.'
            group-type:
               type: str
               description: 'Set the group to be for firewall authentication, FSSO, RSSO, or guest users.'
            guest:
               type: array
               suboptions:
                  comment:
                     type: str
                     description: 'Comment.'
                  company:
                     type: str
                     description: 'Set the action for the company guest user field.'
                  email:
                     type: str
                     description: 'Email.'
                  expiration:
                     type: str
                     description: 'Expire time.'
                  mobile-phone:
                     type: str
                     description: 'Mobile phone.'
                  name:
                     type: str
                     description: 'Guest name.'
                  password:
                     type: array
                     suboptions:
                        type: str
                  sponsor:
                     type: str
                     description: 'Set the action for the sponsor guest user field.'
                  user-id:
                     type: str
                     description: 'Guest ID.'
            http-digest-realm:
               type: str
               description: 'Realm attribute for MD5-digest authentication.'
            id:
               type: int
               description: 'Group ID.'
            match:
               type: array
               suboptions:
                  _gui_meta:
                     type: str
                  group-name:
                     type: str
                     description: 'Name of matching group on remote authentication server.'
                  id:
                     type: int
                     description: 'ID.'
                  server-name:
                     type: str
                     description: 'Name of remote auth server.'
            max-accounts:
               type: int
               description: 'Maximum number of guest accounts that can be created for this group (0 means unlimited).'
            member:
               type: str
               description: 'Names of users, peers, LDAP severs, or RADIUS servers to add to the user group.'
            mobile-phone:
               type: str
               description: 'Enable/disable the guest user mobile phone number field.'
            multiple-guest-add:
               type: str
               description: 'Enable/disable addition of multiple guests.'
            name:
               type: str
               description: 'Group name.'
            password:
               type: str
               description: 'Guest user password type.'
            sms-custom-server:
               type: str
               description: 'SMS server.'
            sms-server:
               type: str
               description: 'Send SMS through FortiGuard or other external server.'
            sponsor:
               type: str
               description: 'Set the action for the sponsor guest user field.'
            sso-attribute-value:
               type: str
               description: 'Name of the RADIUS user group that this local user group represents.'
            user-id:
               type: str
               description: 'Guest user ID type.'
            user-name:
               type: str
               description: 'Enable/disable the guest user name entry.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/user/group/{group}'

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
        '/pm/config/adom/{adom}/obj/user/group/{group}',
        '/pm/config/global/obj/user/group/{group}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'group',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
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
                        'company': {
                            'type': 'string',
                            'enum': [
                                'optional',
                                'mandatory',
                                'disabled'
                            ]
                        },
                        'email': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'expire': {
                            'type': 'integer'
                        },
                        'expire-type': {
                            'type': 'string',
                            'enum': [
                                'immediately',
                                'first-successful-login'
                            ]
                        },
                        'group-type': {
                            'type': 'string',
                            'enum': [
                                'firewall',
                                'directory-service',
                                'fsso-service',
                                'guest',
                                'rsso'
                            ]
                        },
                        'guest': {
                            'type': 'array',
                            'items': {
                                'comment': {
                                    'type': 'string'
                                },
                                'company': {
                                    'type': 'string'
                                },
                                'email': {
                                    'type': 'string'
                                },
                                'expiration': {
                                    'type': 'string'
                                },
                                'mobile-phone': {
                                    'type': 'string'
                                },
                                'name': {
                                    'type': 'string'
                                },
                                'password': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                },
                                'sponsor': {
                                    'type': 'string'
                                },
                                'user-id': {
                                    'type': 'string'
                                }
                            }
                        },
                        'http-digest-realm': {
                            'type': 'string'
                        },
                        'id': {
                            'type': 'integer'
                        },
                        'match': {
                            'type': 'array',
                            'items': {
                                '_gui_meta': {
                                    'type': 'string'
                                },
                                'group-name': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'server-name': {
                                    'type': 'string'
                                }
                            }
                        },
                        'max-accounts': {
                            'type': 'integer'
                        },
                        'member': {
                            'type': 'string'
                        },
                        'mobile-phone': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'multiple-guest-add': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'name': {
                            'type': 'string'
                        },
                        'password': {
                            'type': 'string',
                            'enum': [
                                'auto-generate',
                                'specify',
                                'disable'
                            ]
                        },
                        'sms-custom-server': {
                            'type': 'string'
                        },
                        'sms-server': {
                            'type': 'string',
                            'enum': [
                                'fortiguard',
                                'custom'
                            ]
                        },
                        'sponsor': {
                            'type': 'string',
                            'enum': [
                                'optional',
                                'mandatory',
                                'disabled'
                            ]
                        },
                        'sso-attribute-value': {
                            'type': 'string'
                        },
                        'user-id': {
                            'type': 'string',
                            'enum': [
                                'email',
                                'auto-generate',
                                'specify'
                            ]
                        },
                        'user-name': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        }
                    },
                    'api_tag': 0
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
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object2': [
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'object member',
                            'chksum',
                            'datasrc'
                        ]
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
            'clone': 'object0',
            'delete': 'object1',
            'get': 'object2',
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
                'clone',
                'delete',
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
