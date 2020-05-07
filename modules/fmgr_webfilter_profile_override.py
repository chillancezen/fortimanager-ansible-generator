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
module: fmgr_webfilter_profile_override
short_description: Web Filter override settings.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/webfilter/profile/{profile}/override
    - /pm/config/global/obj/webfilter/profile/{profile}/override
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
            profile:
                type: str
    schema_object0:
        methods: [get]
        description: 'Web Filter override settings.'
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
    schema_object1:
        methods: [set, update]
        description: 'Web Filter override settings.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                ovrd-cookie:
                    type: str
                    description: 'Allow/deny browser-based (cookie) overrides.'
                    choices:
                        - 'deny'
                        - 'allow'
                ovrd-dur:
                    type: str
                    description: 'Override duration.'
                ovrd-dur-mode:
                    type: str
                    description: 'Override duration mode.'
                    choices:
                        - 'constant'
                        - 'ask'
                ovrd-scope:
                    type: str
                    description: 'Override scope.'
                    choices:
                        - 'user'
                        - 'user-group'
                        - 'ip'
                        - 'ask'
                        - 'browser'
                ovrd-user-group:
                    type: str
                    description: 'User groups with permission to use the override.'
                profile:
                    type: str
                    description: 'Web filter profile with permission to create overrides.'
                profile-attribute:
                    type: str
                    description: 'Profile attribute to retrieve from the RADIUS server.'
                    choices:
                        - 'User-Name'
                        - 'User-Password'
                        - 'CHAP-Password'
                        - 'NAS-IP-Address'
                        - 'NAS-Port'
                        - 'Service-Type'
                        - 'Framed-Protocol'
                        - 'Framed-IP-Address'
                        - 'Framed-IP-Netmask'
                        - 'Framed-Routing'
                        - 'Filter-Id'
                        - 'Framed-MTU'
                        - 'Framed-Compression'
                        - 'Login-IP-Host'
                        - 'Login-Service'
                        - 'Login-TCP-Port'
                        - 'Reply-Message'
                        - 'Callback-Number'
                        - 'Callback-Id'
                        - 'Framed-Route'
                        - 'Framed-IPX-Network'
                        - 'State'
                        - 'Class'
                        - 'Vendor-Specific'
                        - 'Session-Timeout'
                        - 'Idle-Timeout'
                        - 'Termination-Action'
                        - 'Called-Station-Id'
                        - 'Calling-Station-Id'
                        - 'NAS-Identifier'
                        - 'Proxy-State'
                        - 'Login-LAT-Service'
                        - 'Login-LAT-Node'
                        - 'Login-LAT-Group'
                        - 'Framed-AppleTalk-Link'
                        - 'Framed-AppleTalk-Network'
                        - 'Framed-AppleTalk-Zone'
                        - 'Acct-Status-Type'
                        - 'Acct-Delay-Time'
                        - 'Acct-Input-Octets'
                        - 'Acct-Output-Octets'
                        - 'Acct-Session-Id'
                        - 'Acct-Authentic'
                        - 'Acct-Session-Time'
                        - 'Acct-Input-Packets'
                        - 'Acct-Output-Packets'
                        - 'Acct-Terminate-Cause'
                        - 'Acct-Multi-Session-Id'
                        - 'Acct-Link-Count'
                        - 'CHAP-Challenge'
                        - 'NAS-Port-Type'
                        - 'Port-Limit'
                        - 'Login-LAT-Port'
                profile-type:
                    type: str
                    description: 'Override profile type.'
                    choices:
                        - 'list'
                        - 'radius'

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

    - name: REQUESTING /PM/CONFIG/OBJ/WEBFILTER/PROFILE/{PROFILE}/OVERRIDE
      fmgr_webfilter_profile_override:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/WEBFILTER/PROFILE/{PROFILE}/OVERRIDE
      fmgr_webfilter_profile_override:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               data:
                  ovrd-cookie: <value in [deny, allow]>
                  ovrd-dur: <value of string>
                  ovrd-dur-mode: <value in [constant, ask]>
                  ovrd-scope: <value in [user, user-group, ip, ...]>
                  ovrd-user-group: <value of string>
                  profile: <value of string>
                  profile-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
                  profile-type: <value in [list, radius]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            ovrd-cookie:
               type: str
               description: 'Allow/deny browser-based (cookie) overrides.'
            ovrd-dur:
               type: str
               description: 'Override duration.'
            ovrd-dur-mode:
               type: str
               description: 'Override duration mode.'
            ovrd-scope:
               type: str
               description: 'Override scope.'
            ovrd-user-group:
               type: str
               description: 'User groups with permission to use the override.'
            profile:
               type: str
               description: 'Web filter profile with permission to create overrides.'
            profile-attribute:
               type: str
               description: 'Profile attribute to retrieve from the RADIUS server.'
            profile-type:
               type: str
               description: 'Override profile type.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/webfilter/profile/{profile}/override'
return_of_api_category_0:
   description: items returned for method:[set, update]
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
            example: '/pm/config/adom/{adom}/obj/webfilter/profile/{profile}/override'

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
        '/pm/config/adom/{adom}/obj/webfilter/profile/{profile}/override',
        '/pm/config/global/obj/webfilter/profile/{profile}/override'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'profile',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
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
            'object1': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'ovrd-cookie': {
                            'type': 'string',
                            'enum': [
                                'deny',
                                'allow'
                            ]
                        },
                        'ovrd-dur': {
                            'type': 'string'
                        },
                        'ovrd-dur-mode': {
                            'type': 'string',
                            'enum': [
                                'constant',
                                'ask'
                            ]
                        },
                        'ovrd-scope': {
                            'type': 'string',
                            'enum': [
                                'user',
                                'user-group',
                                'ip',
                                'ask',
                                'browser'
                            ]
                        },
                        'ovrd-user-group': {
                            'type': 'string'
                        },
                        'profile': {
                            'type': 'string'
                        },
                        'profile-attribute': {
                            'type': 'string',
                            'enum': [
                                'User-Name',
                                'User-Password',
                                'CHAP-Password',
                                'NAS-IP-Address',
                                'NAS-Port',
                                'Service-Type',
                                'Framed-Protocol',
                                'Framed-IP-Address',
                                'Framed-IP-Netmask',
                                'Framed-Routing',
                                'Filter-Id',
                                'Framed-MTU',
                                'Framed-Compression',
                                'Login-IP-Host',
                                'Login-Service',
                                'Login-TCP-Port',
                                'Reply-Message',
                                'Callback-Number',
                                'Callback-Id',
                                'Framed-Route',
                                'Framed-IPX-Network',
                                'State',
                                'Class',
                                'Vendor-Specific',
                                'Session-Timeout',
                                'Idle-Timeout',
                                'Termination-Action',
                                'Called-Station-Id',
                                'Calling-Station-Id',
                                'NAS-Identifier',
                                'Proxy-State',
                                'Login-LAT-Service',
                                'Login-LAT-Node',
                                'Login-LAT-Group',
                                'Framed-AppleTalk-Link',
                                'Framed-AppleTalk-Network',
                                'Framed-AppleTalk-Zone',
                                'Acct-Status-Type',
                                'Acct-Delay-Time',
                                'Acct-Input-Octets',
                                'Acct-Output-Octets',
                                'Acct-Session-Id',
                                'Acct-Authentic',
                                'Acct-Session-Time',
                                'Acct-Input-Packets',
                                'Acct-Output-Packets',
                                'Acct-Terminate-Cause',
                                'Acct-Multi-Session-Id',
                                'Acct-Link-Count',
                                'CHAP-Challenge',
                                'NAS-Port-Type',
                                'Port-Limit',
                                'Login-LAT-Port'
                            ]
                        },
                        'profile-type': {
                            'type': 'string',
                            'enum': [
                                'list',
                                'radius'
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
            ]
        },
        'method_mapping': {
            'get': 'object0',
            'set': 'object1',
            'update': 'object1'
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
