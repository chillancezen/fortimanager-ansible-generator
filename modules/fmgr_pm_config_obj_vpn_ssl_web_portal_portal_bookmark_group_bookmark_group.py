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
module: fmgr_pm_config_obj_vpn_ssl_web_portal_portal_bookmark_group_bookmark_group
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get move set update ] the following apis.
    - /pm/config/adom/{adom}/obj/vpn/ssl/web/portal/{portal}/bookmark-group/{bookmark-group}
    - /pm/config/global/obj/vpn/ssl/web/portal/{portal}/bookmark-group/{bookmark-group}
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
            portal:
                type: str
            bookmark-group:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Portal bookmark group.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                bookmarks:
                    -
                        additional-params:
                            type: str
                            description: 'Additional parameters.'
                        apptype:
                            type: str
                            description: 'Application type.'
                            choices:
                                - 'web'
                                - 'telnet'
                                - 'ssh'
                                - 'ftp'
                                - 'smb'
                                - 'vnc'
                                - 'rdp'
                                - 'citrix'
                                - 'rdpnative'
                                - 'portforward'
                                - 'sftp'
                        description:
                            type: str
                            description: 'Description.'
                        folder:
                            type: str
                            description: 'Network shared file folder parameter.'
                        form-data:
                            -
                                name:
                                    type: str
                                    description: 'Name.'
                                value:
                                    type: str
                                    description: 'Value.'
                        host:
                            type: str
                            description: 'Host name/IP parameter.'
                        listening-port:
                            type: int
                            description: 'Listening port (0 - 65535).'
                        load-balancing-info:
                            type: str
                            description: 'The load balancing information or cookie which should be provided to the connection broker.'
                        logon-password:
                            -
                                type: str
                        logon-user:
                            type: str
                            description: 'Logon user.'
                        name:
                            type: str
                            description: 'Bookmark name.'
                        port:
                            type: int
                            description: 'Remote port.'
                        preconnection-blob:
                            type: str
                            description: 'An arbitrary string which identifies the RDP source.'
                        preconnection-id:
                            type: int
                            description: 'The numeric ID of the RDP source (0-2147483648).'
                        remote-port:
                            type: int
                            description: 'Remote port (0 - 65535).'
                        security:
                            type: str
                            description: 'Security mode for RDP connection.'
                            choices:
                                - 'rdp'
                                - 'nla'
                                - 'tls'
                                - 'any'
                        server-layout:
                            type: str
                            description: 'Server side keyboard layout.'
                            choices:
                                - 'en-us-qwerty'
                                - 'de-de-qwertz'
                                - 'fr-fr-azerty'
                                - 'it-it-qwerty'
                                - 'sv-se-qwerty'
                                - 'failsafe'
                                - 'en-gb-qwerty'
                                - 'es-es-qwerty'
                                - 'fr-ch-qwertz'
                                - 'ja-jp-qwerty'
                                - 'pt-br-qwerty'
                                - 'tr-tr-qwerty'
                        show-status-window:
                            type: str
                            description: 'Enable/disable showing of status window.'
                            choices:
                                - 'disable'
                                - 'enable'
                        sso:
                            type: str
                            description: 'Single Sign-On.'
                            choices:
                                - 'disable'
                                - 'static'
                                - 'auto'
                        sso-credential:
                            type: str
                            description: 'Single sign-on credentials.'
                            choices:
                                - 'sslvpn-login'
                                - 'alternative'
                        sso-credential-sent-once:
                            type: str
                            description: 'Single sign-on credentials are only sent once to remote server.'
                            choices:
                                - 'disable'
                                - 'enable'
                        sso-password:
                            -
                                type: str
                        sso-username:
                            type: str
                            description: 'SSO user name.'
                        url:
                            type: str
                            description: 'URL parameter.'
                name:
                    type: str
                    description: 'Bookmark group name.'
    schema_object1:
        methods: [delete]
        description: 'Portal bookmark group.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Portal bookmark group.'
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
    schema_object3:
        methods: [move]
        description: 'Portal bookmark group.'
        api_categories: [api_tag0]
        api_tag0:
            option:
                type: str
                choices:
                    - 'before'
                    - 'after'
            target:
                type: str
                description: 'Key to the target entry.'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /pm/config/obj/vpn/ssl/web/portal/{portal}/bookmark-group/{bookmark-group}
      fmgr_pm_config_obj_vpn_ssl_web_portal_portal_bookmark_group_bookmark_group:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            portal: <value of string>
            bookmark-group: <value of string>
         params:
            - 
               data: 
                  bookmarks: 
                   - 
                        additional-params: <value of string>
                        apptype: <value in [web, telnet, ssh, ...]>
                        description: <value of string>
                        folder: <value of string>
                        form-data: 
                         - 
                              name: <value of string>
                              value: <value of string>
                        host: <value of string>
                        listening-port: <value of integer>
                        load-balancing-info: <value of string>
                        logon-password: 
                         - <value of string>
                        logon-user: <value of string>
                        name: <value of string>
                        port: <value of integer>
                        preconnection-blob: <value of string>
                        preconnection-id: <value of integer>
                        remote-port: <value of integer>
                        security: <value in [rdp, nla, tls, ...]>
                        server-layout: <value in [en-us-qwerty, de-de-qwertz, fr-fr-azerty, ...]>
                        show-status-window: <value in [disable, enable]>
                        sso: <value in [disable, static, auto]>
                        sso-credential: <value in [sslvpn-login, alternative]>
                        sso-credential-sent-once: <value in [disable, enable]>
                        sso-password: 
                         - <value of string>
                        sso-username: <value of string>
                        url: <value of string>
                  name: <value of string>
    - name: send request to /pm/config/obj/vpn/ssl/web/portal/{portal}/bookmark-group/{bookmark-group}
      fmgr_pm_config_obj_vpn_ssl_web_portal_portal_bookmark_group_bookmark_group:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            portal: <value of string>
            bookmark-group: <value of string>
         params:
            - 
               option: <value in [object member, chksum, datasrc]>
    - name: send request to /pm/config/obj/vpn/ssl/web/portal/{portal}/bookmark-group/{bookmark-group}
      fmgr_pm_config_obj_vpn_ssl_web_portal_portal_bookmark_group_bookmark_group:
         method: <value in [move]>
         url_params:
            adom: <value in [none, global, custom dom]>
            portal: <value of string>
            bookmark-group: <value of string>
         params:
            - 
               option: <value in [before, after]>
               target: <value of string>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[clone, delete, move, set, update]
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
            example: /pm/config/adom/{adom}/obj/vpn/ssl/web/portal/{portal}/bookmark-group/{bookmark-group}
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            bookmarks:
               type: array
               suboptions:
                  additional-params:
                     type: str
                     description: 'Additional parameters.'
                  apptype:
                     type: str
                     description: 'Application type.'
                  description:
                     type: str
                     description: 'Description.'
                  folder:
                     type: str
                     description: 'Network shared file folder parameter.'
                  form-data:
                     type: array
                     suboptions:
                        name:
                           type: str
                           description: 'Name.'
                        value:
                           type: str
                           description: 'Value.'
                  host:
                     type: str
                     description: 'Host name/IP parameter.'
                  listening-port:
                     type: int
                     description: 'Listening port (0 - 65535).'
                  load-balancing-info:
                     type: str
                     description: 'The load balancing information or cookie which should be provided to the connection broker.'
                  logon-password:
                     type: array
                     suboptions:
                        type: str
                  logon-user:
                     type: str
                     description: 'Logon user.'
                  name:
                     type: str
                     description: 'Bookmark name.'
                  port:
                     type: int
                     description: 'Remote port.'
                  preconnection-blob:
                     type: str
                     description: 'An arbitrary string which identifies the RDP source.'
                  preconnection-id:
                     type: int
                     description: 'The numeric ID of the RDP source (0-2147483648).'
                  remote-port:
                     type: int
                     description: 'Remote port (0 - 65535).'
                  security:
                     type: str
                     description: 'Security mode for RDP connection.'
                  server-layout:
                     type: str
                     description: 'Server side keyboard layout.'
                  show-status-window:
                     type: str
                     description: 'Enable/disable showing of status window.'
                  sso:
                     type: str
                     description: 'Single Sign-On.'
                  sso-credential:
                     type: str
                     description: 'Single sign-on credentials.'
                  sso-credential-sent-once:
                     type: str
                     description: 'Single sign-on credentials are only sent once to remote server.'
                  sso-password:
                     type: array
                     suboptions:
                        type: str
                  sso-username:
                     type: str
                     description: 'SSO user name.'
                  url:
                     type: str
                     description: 'URL parameter.'
            name:
               type: str
               description: 'Bookmark group name.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/obj/vpn/ssl/web/portal/{portal}/bookmark-group/{bookmark-group}

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
        '/pm/config/adom/{adom}/obj/vpn/ssl/web/portal/{portal}/bookmark-group/{bookmark-group}',
        '/pm/config/global/obj/vpn/ssl/web/portal/{portal}/bookmark-group/{bookmark-group}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'portal',
            'type': 'string'
        },
        {
            'name': 'bookmark-group',
            'type': 'string'
        }
    ]

    body_schema =  {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'bookmarks': {
                            'type': 'array',
                            'items': {
                                'additional-params': {
                                    'type': 'string'
                                },
                                'apptype': {
                                    'type': 'string',
                                    'enum': [
                                        'web',
                                        'telnet',
                                        'ssh',
                                        'ftp',
                                        'smb',
                                        'vnc',
                                        'rdp',
                                        'citrix',
                                        'rdpnative',
                                        'portforward',
                                        'sftp'
                                    ]
                                },
                                'description': {
                                    'type': 'string'
                                },
                                'folder': {
                                    'type': 'string'
                                },
                                'form-data': {
                                    'type': 'array',
                                    'items': {
                                        'name': {
                                            'type': 'string'
                                        },
                                        'value': {
                                            'type': 'string'
                                        }
                                    }
                                },
                                'host': {
                                    'type': 'string'
                                },
                                'listening-port': {
                                    'type': 'integer'
                                },
                                'load-balancing-info': {
                                    'type': 'string'
                                },
                                'logon-password': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                },
                                'logon-user': {
                                    'type': 'string'
                                },
                                'name': {
                                    'type': 'string'
                                },
                                'port': {
                                    'type': 'integer'
                                },
                                'preconnection-blob': {
                                    'type': 'string'
                                },
                                'preconnection-id': {
                                    'type': 'integer'
                                },
                                'remote-port': {
                                    'type': 'integer'
                                },
                                'security': {
                                    'type': 'string',
                                    'enum': [
                                        'rdp',
                                        'nla',
                                        'tls',
                                        'any'
                                    ]
                                },
                                'server-layout': {
                                    'type': 'string',
                                    'enum': [
                                        'en-us-qwerty',
                                        'de-de-qwertz',
                                        'fr-fr-azerty',
                                        'it-it-qwerty',
                                        'sv-se-qwerty',
                                        'failsafe',
                                        'en-gb-qwerty',
                                        'es-es-qwerty',
                                        'fr-ch-qwertz',
                                        'ja-jp-qwerty',
                                        'pt-br-qwerty',
                                        'tr-tr-qwerty'
                                    ]
                                },
                                'show-status-window': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'sso': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'static',
                                        'auto'
                                    ]
                                },
                                'sso-credential': {
                                    'type': 'string',
                                    'enum': [
                                        'sslvpn-login',
                                        'alternative'
                                    ]
                                },
                                'sso-credential-sent-once': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'sso-password': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                },
                                'sso-username': {
                                    'type': 'string'
                                },
                                'url': {
                                    'type': 'string'
                                }
                            }
                        },
                        'name': {
                            'type': 'string'
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
            ],
            'object3': [
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'before',
                            'after'
                        ]
                    },
                    'api_tag': 0
                },
                {
                    'type': 'string',
                    'name': 'target',
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
            'move': 'object3',
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
                'move',
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