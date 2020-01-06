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
module: fmgr_pm_config_obj_firewall_gtp_gtp_ie_validation
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/firewall/gtp/{gtp}/ie-validation
    - /pm/config/global/obj/firewall/gtp/{gtp}/ie-validation
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
            gtp:
                type: str
    schema_object0:
        methods: [get]
        description: 'IE validation.'
        api_categories: [api_tag0]
        api_tag0:
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the object will be returned.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'chksum - Return the check-sum value instead of attributes.'
                choices:
                    - object member
                    - chksum
                    - datasrc
    schema_object1:
        methods: [set, update]
        description: 'IE validation.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                apn-restriction:
                    type: str
                    description: 'Validate APN restriction.'
                    choices:
                        - disable
                        - enable
                charging-ID:
                    type: str
                    description: 'Validate charging ID.'
                    choices:
                        - disable
                        - enable
                charging-gateway-addr:
                    type: str
                    description: 'Validate charging gateway address.'
                    choices:
                        - disable
                        - enable
                end-user-addr:
                    type: str
                    description: 'Validate end user address.'
                    choices:
                        - disable
                        - enable
                gsn-addr:
                    type: str
                    description: 'Validate GSN address.'
                    choices:
                        - disable
                        - enable
                imei:
                    type: str
                    description: 'Validate IMEI(SV).'
                    choices:
                        - disable
                        - enable
                imsi:
                    type: str
                    description: 'Validate IMSI.'
                    choices:
                        - disable
                        - enable
                mm-context:
                    type: str
                    description: 'Validate MM context.'
                    choices:
                        - disable
                        - enable
                ms-tzone:
                    type: str
                    description: 'Validate MS time zone.'
                    choices:
                        - disable
                        - enable
                ms-validated:
                    type: str
                    description: 'Validate MS validated.'
                    choices:
                        - disable
                        - enable
                msisdn:
                    type: str
                    description: 'Validate MSISDN.'
                    choices:
                        - disable
                        - enable
                nsapi:
                    type: str
                    description: 'Validate NSAPI.'
                    choices:
                        - disable
                        - enable
                pdp-context:
                    type: str
                    description: 'Validate PDP context.'
                    choices:
                        - disable
                        - enable
                qos-profile:
                    type: str
                    description: 'Validate Quality of Service(QoS) profile.'
                    choices:
                        - disable
                        - enable
                rai:
                    type: str
                    description: 'Validate RAI.'
                    choices:
                        - disable
                        - enable
                rat-type:
                    type: str
                    description: 'Validate RAT type.'
                    choices:
                        - disable
                        - enable
                reordering-required:
                    type: str
                    description: 'Validate re-ordering required.'
                    choices:
                        - disable
                        - enable
                selection-mode:
                    type: str
                    description: 'Validate selection mode.'
                    choices:
                        - disable
                        - enable
                uli:
                    type: str
                    description: 'Validate user location information.'
                    choices:
                        - disable
                        - enable

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /pm/config/obj/firewall/gtp/{gtp}/ie-validation
      fmgr_pm_config_obj_firewall_gtp_gtp_ie_validation:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            gtp: <value of string>
         params:
            - 
               option: <value in [object member, chksum, datasrc]>
    - name: send request to /pm/config/obj/firewall/gtp/{gtp}/ie-validation
      fmgr_pm_config_obj_firewall_gtp_gtp_ie_validation:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            gtp: <value of string>
         params:
            - 
               data: 
                  apn-restriction: <value in [disable, enable]>
                  charging-ID: <value in [disable, enable]>
                  charging-gateway-addr: <value in [disable, enable]>
                  end-user-addr: <value in [disable, enable]>
                  gsn-addr: <value in [disable, enable]>
                  imei: <value in [disable, enable]>
                  imsi: <value in [disable, enable]>
                  mm-context: <value in [disable, enable]>
                  ms-tzone: <value in [disable, enable]>
                  ms-validated: <value in [disable, enable]>
                  msisdn: <value in [disable, enable]>
                  nsapi: <value in [disable, enable]>
                  pdp-context: <value in [disable, enable]>
                  qos-profile: <value in [disable, enable]>
                  rai: <value in [disable, enable]>
                  rat-type: <value in [disable, enable]>
                  reordering-required: <value in [disable, enable]>
                  selection-mode: <value in [disable, enable]>
                  uli: <value in [disable, enable]>

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
            apn-restriction:
               type: str
               description: 'Validate APN restriction.'
            charging-ID:
               type: str
               description: 'Validate charging ID.'
            charging-gateway-addr:
               type: str
               description: 'Validate charging gateway address.'
            end-user-addr:
               type: str
               description: 'Validate end user address.'
            gsn-addr:
               type: str
               description: 'Validate GSN address.'
            imei:
               type: str
               description: 'Validate IMEI(SV).'
            imsi:
               type: str
               description: 'Validate IMSI.'
            mm-context:
               type: str
               description: 'Validate MM context.'
            ms-tzone:
               type: str
               description: 'Validate MS time zone.'
            ms-validated:
               type: str
               description: 'Validate MS validated.'
            msisdn:
               type: str
               description: 'Validate MSISDN.'
            nsapi:
               type: str
               description: 'Validate NSAPI.'
            pdp-context:
               type: str
               description: 'Validate PDP context.'
            qos-profile:
               type: str
               description: 'Validate Quality of Service(QoS) profile.'
            rai:
               type: str
               description: 'Validate RAI.'
            rat-type:
               type: str
               description: 'Validate RAT type.'
            reordering-required:
               type: str
               description: 'Validate re-ordering required.'
            selection-mode:
               type: str
               description: 'Validate selection mode.'
            uli:
               type: str
               description: 'Validate user location information.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/obj/firewall/gtp/{gtp}/ie-validation
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
            example: /pm/config/adom/{adom}/obj/firewall/gtp/{gtp}/ie-validation

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
        '/pm/config/adom/{adom}/obj/firewall/gtp/{gtp}/ie-validation',
        '/pm/config/global/obj/firewall/gtp/{gtp}/ie-validation'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'gtp',
            'type': 'string'
        }
    ]

    body_schema =  {
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
                        'apn-restriction': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'charging-ID': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'charging-gateway-addr': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'end-user-addr': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'gsn-addr': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'imei': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'imsi': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mm-context': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ms-tzone': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ms-validated': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'msisdn': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'nsapi': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'pdp-context': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'qos-profile': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'rai': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'rat-type': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'reordering-required': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'selection-mode': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'uli': {
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
            ]
        },
        'method_mapping': {
            'get': 'object0',
            'set': 'object1',
            'update': 'object1'
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