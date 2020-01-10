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
module: fmgr_pm_config_obj_footer_consolidated_policy_per_object
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get ] the following apis.
    - /pm/config/adom/{adom}/obj/global/footer/consolidated/policy/{policy}
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
            policy:
                type: str
    schema_object0:
        methods: [get]
        description: ''
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

    - name: REQUESTING /PM/CONFIG/OBJ/FOOTER/CONSOLIDATED/POLICY/{POLICY}
      fmgr_pm_config_obj_footer_consolidated_policy_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            policy: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

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
            action:
               type: str
            app-category:
               type: array
               suboptions:
                  type: int
            app-group:
               type: str
            application:
               type: array
               suboptions:
                  type: int
            application-list:
               type: str
            auto-asic-offload:
               type: str
            av-profile:
               type: str
            cifs-profile:
               type: str
            comments:
               type: str
            diffserv-forward:
               type: str
            diffserv-reverse:
               type: str
            diffservcode-forward:
               type: str
            diffservcode-rev:
               type: str
            dlp-sensor:
               type: str
            dnsfilter-profile:
               type: str
            dstaddr4:
               type: str
            dstaddr6:
               type: str
            dstintf:
               type: str
            emailfilter-profile:
               type: str
            fixedport:
               type: str
            groups:
               type: str
            http-policy-redirect:
               type: str
            icap-profile:
               type: str
            inbound:
               type: str
            inspection-mode:
               type: str
            ippool:
               type: str
            ips-sensor:
               type: str
            logtraffic:
               type: str
            logtraffic-start:
               type: str
            mms-profile:
               type: str
            name:
               type: str
            nat:
               type: str
            outbound:
               type: str
            per-ip-shaper:
               type: str
            policyid:
               type: int
            poolname4:
               type: str
            poolname6:
               type: str
            profile-group:
               type: str
            profile-protocol-options:
               type: str
            profile-type:
               type: str
            schedule:
               type: str
            schedule-timeout:
               type: str
            service:
               type: str
            session-ttl:
               type: int
            spamfilter-profile:
               type: str
            srcaddr4:
               type: str
            srcaddr6:
               type: str
            srcintf:
               type: str
            ssh-filter-profile:
               type: str
            ssh-policy-redirect:
               type: str
            ssl-ssh-profile:
               type: str
            status:
               type: str
            tcp-mss-receiver:
               type: int
            tcp-mss-sender:
               type: int
            traffic-shaper:
               type: str
            traffic-shaper-reverse:
               type: str
            url-category:
               type: array
               suboptions:
                  type: int
            users:
               type: str
            utm-inspection-mode:
               type: str
            utm-status:
               type: str
            uuid:
               type: str
            voip-profile:
               type: str
            vpntunnel:
               type: str
            waf-profile:
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
            example: '/pm/config/adom/{adom}/obj/global/footer/consolidated/policy/{policy}'

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
        '/pm/config/adom/{adom}/obj/global/footer/consolidated/policy/{policy}'
    ]

    url_schema = [
        {
            'name': 'adom',
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
            'get': 'object0'
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
                'get'
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
