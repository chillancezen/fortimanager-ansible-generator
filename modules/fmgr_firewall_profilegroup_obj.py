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
module: fmgr_firewall_profilegroup_obj
short_description: Configure profile groups.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/firewall/profile-group/{profile-group}
    - /pm/config/global/obj/firewall/profile-group/{profile-group}
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
            profile-group:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Configure profile groups.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                application-list:
                    type: str
                    description: 'Name of an existing Application list.'
                av-profile:
                    type: str
                    description: 'Name of an existing Antivirus profile.'
                dlp-sensor:
                    type: str
                    description: 'Name of an existing DLP sensor.'
                dnsfilter-profile:
                    type: str
                    description: 'Name of an existing DNS filter profile.'
                icap-profile:
                    type: str
                    description: 'Name of an existing ICAP profile.'
                ips-sensor:
                    type: str
                    description: 'Name of an existing IPS sensor.'
                mms-profile:
                    type: str
                    description: 'Name of an existing MMS profile.'
                name:
                    type: str
                    description: 'Profile group name.'
                profile-protocol-options:
                    type: str
                    description: 'Name of an existing Protocol options profile.'
                spamfilter-profile:
                    type: str
                    description: 'Name of an existing Spam filter profile.'
                ssh-filter-profile:
                    type: str
                    description: 'Name of an existing SSH filter profile.'
                ssl-ssh-profile:
                    type: str
                    description: 'Name of an existing SSL SSH profile.'
                voip-profile:
                    type: str
                    description: 'Name of an existing VoIP profile.'
                waf-profile:
                    type: str
                    description: 'Name of an existing Web application firewall profile.'
                webfilter-profile:
                    type: str
                    description: 'Name of an existing Web filter profile.'
    schema_object1:
        methods: [delete]
        description: 'Configure profile groups.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Configure profile groups.'
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
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/PROFILE-GROUP/{PROFILE-GROUP}
      fmgr_firewall_profilegroup_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile-group: <value of string>
         params:
            -
               data:
                  application-list: <value of string>
                  av-profile: <value of string>
                  dlp-sensor: <value of string>
                  dnsfilter-profile: <value of string>
                  icap-profile: <value of string>
                  ips-sensor: <value of string>
                  mms-profile: <value of string>
                  name: <value of string>
                  profile-protocol-options: <value of string>
                  spamfilter-profile: <value of string>
                  ssh-filter-profile: <value of string>
                  ssl-ssh-profile: <value of string>
                  voip-profile: <value of string>
                  waf-profile: <value of string>
                  webfilter-profile: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/PROFILE-GROUP/{PROFILE-GROUP}
      fmgr_firewall_profilegroup_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile-group: <value of string>
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
            example: '/pm/config/adom/{adom}/obj/firewall/profile-group/{profile-group}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            application-list:
               type: str
               description: 'Name of an existing Application list.'
            av-profile:
               type: str
               description: 'Name of an existing Antivirus profile.'
            dlp-sensor:
               type: str
               description: 'Name of an existing DLP sensor.'
            dnsfilter-profile:
               type: str
               description: 'Name of an existing DNS filter profile.'
            icap-profile:
               type: str
               description: 'Name of an existing ICAP profile.'
            ips-sensor:
               type: str
               description: 'Name of an existing IPS sensor.'
            mms-profile:
               type: str
               description: 'Name of an existing MMS profile.'
            name:
               type: str
               description: 'Profile group name.'
            profile-protocol-options:
               type: str
               description: 'Name of an existing Protocol options profile.'
            spamfilter-profile:
               type: str
               description: 'Name of an existing Spam filter profile.'
            ssh-filter-profile:
               type: str
               description: 'Name of an existing SSH filter profile.'
            ssl-ssh-profile:
               type: str
               description: 'Name of an existing SSL SSH profile.'
            voip-profile:
               type: str
               description: 'Name of an existing VoIP profile.'
            waf-profile:
               type: str
               description: 'Name of an existing Web application firewall profile.'
            webfilter-profile:
               type: str
               description: 'Name of an existing Web filter profile.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/firewall/profile-group/{profile-group}'

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
        '/pm/config/adom/{adom}/obj/firewall/profile-group/{profile-group}',
        '/pm/config/global/obj/firewall/profile-group/{profile-group}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'profile-group',
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
                        'application-list': {
                            'type': 'string'
                        },
                        'av-profile': {
                            'type': 'string'
                        },
                        'dlp-sensor': {
                            'type': 'string'
                        },
                        'dnsfilter-profile': {
                            'type': 'string'
                        },
                        'icap-profile': {
                            'type': 'string'
                        },
                        'ips-sensor': {
                            'type': 'string'
                        },
                        'mms-profile': {
                            'type': 'string'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'profile-protocol-options': {
                            'type': 'string'
                        },
                        'spamfilter-profile': {
                            'type': 'string'
                        },
                        'ssh-filter-profile': {
                            'type': 'string'
                        },
                        'ssl-ssh-profile': {
                            'type': 'string'
                        },
                        'voip-profile': {
                            'type': 'string'
                        },
                        'waf-profile': {
                            'type': 'string'
                        },
                        'webfilter-profile': {
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

    module.exit_json(meta=response[1])


if __name__ == '__main__':
    main()
