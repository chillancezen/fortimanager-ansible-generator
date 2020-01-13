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
module: fmgr_hotspot20_h2qpwanmetric_obj
short_description: Configure WAN metrics.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/wireless-controller/hotspot20/h2qp-wan-metric/{h2qp-wan-metric}
    - /pm/config/global/obj/wireless-controller/hotspot20/h2qp-wan-metric/{h2qp-wan-metric}
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
            h2qp-wan-metric:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Configure WAN metrics.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                downlink-load:
                    type: int
                    description: 'Downlink load.'
                downlink-speed:
                    type: int
                    description: 'Downlink speed (in kilobits/s).'
                link-at-capacity:
                    type: str
                    description: 'Link at capacity.'
                    choices:
                        - 'disable'
                        - 'enable'
                link-status:
                    type: str
                    description: 'Link status.'
                    choices:
                        - 'down'
                        - 'up'
                        - 'in-test'
                load-measurement-duration:
                    type: int
                    description: 'Load measurement duration (in tenths of a second).'
                name:
                    type: str
                    description: 'WAN metric name.'
                symmetric-wan-link:
                    type: str
                    description: 'WAN link symmetry.'
                    choices:
                        - 'asymmetric'
                        - 'symmetric'
                uplink-load:
                    type: int
                    description: 'Uplink load.'
                uplink-speed:
                    type: int
                    description: 'Uplink speed (in kilobits/s).'
    schema_object1:
        methods: [delete]
        description: 'Configure WAN metrics.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Configure WAN metrics.'
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

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/HOTSPOT20/H2QP-WAN-METRIC/{H2QP-WAN-METRIC}
      fmgr_hotspot20_h2qpwanmetric_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            h2qp-wan-metric: <value of string>
         params:
            -
               data:
                  downlink-load: <value of integer>
                  downlink-speed: <value of integer>
                  link-at-capacity: <value in [disable, enable]>
                  link-status: <value in [down, up, in-test]>
                  load-measurement-duration: <value of integer>
                  name: <value of string>
                  symmetric-wan-link: <value in [asymmetric, symmetric]>
                  uplink-load: <value of integer>
                  uplink-speed: <value of integer>

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/HOTSPOT20/H2QP-WAN-METRIC/{H2QP-WAN-METRIC}
      fmgr_hotspot20_h2qpwanmetric_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            h2qp-wan-metric: <value of string>
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
            example: '/pm/config/adom/{adom}/obj/wireless-controller/hotspot20/h2qp-wan-metric/{h2...'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            downlink-load:
               type: int
               description: 'Downlink load.'
            downlink-speed:
               type: int
               description: 'Downlink speed (in kilobits/s).'
            link-at-capacity:
               type: str
               description: 'Link at capacity.'
            link-status:
               type: str
               description: 'Link status.'
            load-measurement-duration:
               type: int
               description: 'Load measurement duration (in tenths of a second).'
            name:
               type: str
               description: 'WAN metric name.'
            symmetric-wan-link:
               type: str
               description: 'WAN link symmetry.'
            uplink-load:
               type: int
               description: 'Uplink load.'
            uplink-speed:
               type: int
               description: 'Uplink speed (in kilobits/s).'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/wireless-controller/hotspot20/h2qp-wan-metric/{h2...'

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
        '/pm/config/adom/{adom}/obj/wireless-controller/hotspot20/h2qp-wan-metric/{h2qp-wan-metric}',
        '/pm/config/global/obj/wireless-controller/hotspot20/h2qp-wan-metric/{h2qp-wan-metric}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'h2qp-wan-metric',
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
                        'downlink-load': {
                            'type': 'integer'
                        },
                        'downlink-speed': {
                            'type': 'integer'
                        },
                        'link-at-capacity': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'link-status': {
                            'type': 'string',
                            'enum': [
                                'down',
                                'up',
                                'in-test'
                            ]
                        },
                        'load-measurement-duration': {
                            'type': 'integer'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'symmetric-wan-link': {
                            'type': 'string',
                            'enum': [
                                'asymmetric',
                                'symmetric'
                            ]
                        },
                        'uplink-load': {
                            'type': 'integer'
                        },
                        'uplink-speed': {
                            'type': 'integer'
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
