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
module: fmgr_pm_config_obj_firewall_mms_profile_notification
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/firewall/mms-profile/{mms-profile}/notification
    - /pm/config/global/obj/firewall/mms-profile/{mms-profile}/notification
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
            mms-profile:
                type: str
    schema_object0:
        methods: [get]
        description: 'Notification configuration.'
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
        description: 'Notification configuration.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                alert-int:
                    type: int
                    description: 'Alert notification send interval.'
                alert-int-mode:
                    type: str
                    description: 'Alert notification interval mode.'
                    choices:
                        - 'hours'
                        - 'minutes'
                alert-src-msisdn:
                    type: str
                    description: 'Specify from address for alert messages.'
                alert-status:
                    type: str
                    description: 'Alert notification status.'
                    choices:
                        - 'disable'
                        - 'enable'
                bword-int:
                    type: int
                    description: 'Banned word notification send interval.'
                bword-int-mode:
                    type: str
                    description: 'Banned word notification interval mode.'
                    choices:
                        - 'hours'
                        - 'minutes'
                bword-status:
                    type: str
                    description: 'Banned word notification status.'
                    choices:
                        - 'disable'
                        - 'enable'
                carrier-endpoint-bwl-int:
                    type: int
                    description: 'Carrier end point black/white list notification send interval.'
                carrier-endpoint-bwl-int-mode:
                    type: str
                    description: 'Carrier end point black/white list notification interval mode.'
                    choices:
                        - 'hours'
                        - 'minutes'
                carrier-endpoint-bwl-status:
                    type: str
                    description: 'Carrier end point black/white list notification status.'
                    choices:
                        - 'disable'
                        - 'enable'
                days-allowed:
                    -
                        type: str
                        choices:
                            - 'sunday'
                            - 'monday'
                            - 'tuesday'
                            - 'wednesday'
                            - 'thursday'
                            - 'friday'
                            - 'saturday'
                detect-server:
                    type: str
                    description: 'Enable/disable automatic server address determination.'
                    choices:
                        - 'disable'
                        - 'enable'
                dupe-int:
                    type: int
                    description: 'Duplicate notification send interval.'
                dupe-int-mode:
                    type: str
                    description: 'Duplicate notification interval mode.'
                    choices:
                        - 'hours'
                        - 'minutes'
                dupe-status:
                    type: str
                    description: 'Duplicate notification status.'
                    choices:
                        - 'disable'
                        - 'enable'
                file-block-int:
                    type: int
                    description: 'File block notification send interval.'
                file-block-int-mode:
                    type: str
                    description: 'File block notification interval mode.'
                    choices:
                        - 'hours'
                        - 'minutes'
                file-block-status:
                    type: str
                    description: 'File block notification status.'
                    choices:
                        - 'disable'
                        - 'enable'
                flood-int:
                    type: int
                    description: 'Flood notification send interval.'
                flood-int-mode:
                    type: str
                    description: 'Flood notification interval mode.'
                    choices:
                        - 'hours'
                        - 'minutes'
                flood-status:
                    type: str
                    description: 'Flood notification status.'
                    choices:
                        - 'disable'
                        - 'enable'
                from-in-header:
                    type: str
                    description: 'Enable/disable insertion of from address in HTTP header.'
                    choices:
                        - 'disable'
                        - 'enable'
                mms-checksum-int:
                    type: int
                    description: 'MMS checksum notification send interval.'
                mms-checksum-int-mode:
                    type: str
                    description: 'MMS checksum notification interval mode.'
                    choices:
                        - 'hours'
                        - 'minutes'
                mms-checksum-status:
                    type: str
                    description: 'MMS checksum notification status.'
                    choices:
                        - 'disable'
                        - 'enable'
                mmsc-hostname:
                    type: str
                    description: 'Host name or IP address of the MMSC.'
                mmsc-password:
                    -
                        type: str
                mmsc-port:
                    type: int
                    description: 'Port used on the MMSC for sending MMS messages (1 - 65535).'
                mmsc-url:
                    type: str
                    description: 'URL used on the MMSC for sending MMS messages.'
                mmsc-username:
                    type: str
                    description: 'User name required for authentication with the MMSC.'
                msg-protocol:
                    type: str
                    description: 'Protocol to use for sending notification messages.'
                    choices:
                        - 'mm1'
                        - 'mm3'
                        - 'mm4'
                        - 'mm7'
                msg-type:
                    type: str
                    description: 'MM7 message type.'
                    choices:
                        - 'submit-req'
                        - 'deliver-req'
                protocol:
                    type: str
                    description: 'Protocol.'
                rate-limit:
                    type: int
                    description: 'Rate limit for sending notification messages (0 - 250).'
                tod-window-duration:
                    type: str
                    description: 'Time of day window duration.'
                tod-window-end:
                    type: str
                    description: 'Obsolete.'
                tod-window-start:
                    type: str
                    description: 'Time of day window start.'
                user-domain:
                    type: str
                    description: 'Domain name to which the user addresses belong.'
                vas-id:
                    type: str
                    description: 'VAS identifier.'
                vasp-id:
                    type: str
                    description: 'VASP identifier.'
                virus-int:
                    type: int
                    description: 'Virus notification send interval.'
                virus-int-mode:
                    type: str
                    description: 'Virus notification interval mode.'
                    choices:
                        - 'hours'
                        - 'minutes'
                virus-status:
                    type: str
                    description: 'Virus notification status.'
                    choices:
                        - 'disable'
                        - 'enable'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/MMS-PROFILE/{MMS-PROFILE}/NOTIFICATION
      fmgr_pm_config_obj_firewall_mms_profile_notification:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            mms-profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/MMS-PROFILE/{MMS-PROFILE}/NOTIFICATION
      fmgr_pm_config_obj_firewall_mms_profile_notification:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            mms-profile: <value of string>
         params:
            -
               data:
                  alert-int: <value of integer>
                  alert-int-mode: <value in [hours, minutes]>
                  alert-src-msisdn: <value of string>
                  alert-status: <value in [disable, enable]>
                  bword-int: <value of integer>
                  bword-int-mode: <value in [hours, minutes]>
                  bword-status: <value in [disable, enable]>
                  carrier-endpoint-bwl-int: <value of integer>
                  carrier-endpoint-bwl-int-mode: <value in [hours, minutes]>
                  carrier-endpoint-bwl-status: <value in [disable, enable]>
                  days-allowed:
                    - <value in [sunday, monday, tuesday, ...]>
                  detect-server: <value in [disable, enable]>
                  dupe-int: <value of integer>
                  dupe-int-mode: <value in [hours, minutes]>
                  dupe-status: <value in [disable, enable]>
                  file-block-int: <value of integer>
                  file-block-int-mode: <value in [hours, minutes]>
                  file-block-status: <value in [disable, enable]>
                  flood-int: <value of integer>
                  flood-int-mode: <value in [hours, minutes]>
                  flood-status: <value in [disable, enable]>
                  from-in-header: <value in [disable, enable]>
                  mms-checksum-int: <value of integer>
                  mms-checksum-int-mode: <value in [hours, minutes]>
                  mms-checksum-status: <value in [disable, enable]>
                  mmsc-hostname: <value of string>
                  mmsc-password:
                    - <value of string>
                  mmsc-port: <value of integer>
                  mmsc-url: <value of string>
                  mmsc-username: <value of string>
                  msg-protocol: <value in [mm1, mm3, mm4, ...]>
                  msg-type: <value in [submit-req, deliver-req]>
                  protocol: <value of string>
                  rate-limit: <value of integer>
                  tod-window-duration: <value of string>
                  tod-window-end: <value of string>
                  tod-window-start: <value of string>
                  user-domain: <value of string>
                  vas-id: <value of string>
                  vasp-id: <value of string>
                  virus-int: <value of integer>
                  virus-int-mode: <value in [hours, minutes]>
                  virus-status: <value in [disable, enable]>

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
            alert-int:
               type: int
               description: 'Alert notification send interval.'
            alert-int-mode:
               type: str
               description: 'Alert notification interval mode.'
            alert-src-msisdn:
               type: str
               description: 'Specify from address for alert messages.'
            alert-status:
               type: str
               description: 'Alert notification status.'
            bword-int:
               type: int
               description: 'Banned word notification send interval.'
            bword-int-mode:
               type: str
               description: 'Banned word notification interval mode.'
            bword-status:
               type: str
               description: 'Banned word notification status.'
            carrier-endpoint-bwl-int:
               type: int
               description: 'Carrier end point black/white list notification send interval.'
            carrier-endpoint-bwl-int-mode:
               type: str
               description: 'Carrier end point black/white list notification interval mode.'
            carrier-endpoint-bwl-status:
               type: str
               description: 'Carrier end point black/white list notification status.'
            days-allowed:
               type: array
               suboptions:
                  type: str
            detect-server:
               type: str
               description: 'Enable/disable automatic server address determination.'
            dupe-int:
               type: int
               description: 'Duplicate notification send interval.'
            dupe-int-mode:
               type: str
               description: 'Duplicate notification interval mode.'
            dupe-status:
               type: str
               description: 'Duplicate notification status.'
            file-block-int:
               type: int
               description: 'File block notification send interval.'
            file-block-int-mode:
               type: str
               description: 'File block notification interval mode.'
            file-block-status:
               type: str
               description: 'File block notification status.'
            flood-int:
               type: int
               description: 'Flood notification send interval.'
            flood-int-mode:
               type: str
               description: 'Flood notification interval mode.'
            flood-status:
               type: str
               description: 'Flood notification status.'
            from-in-header:
               type: str
               description: 'Enable/disable insertion of from address in HTTP header.'
            mms-checksum-int:
               type: int
               description: 'MMS checksum notification send interval.'
            mms-checksum-int-mode:
               type: str
               description: 'MMS checksum notification interval mode.'
            mms-checksum-status:
               type: str
               description: 'MMS checksum notification status.'
            mmsc-hostname:
               type: str
               description: 'Host name or IP address of the MMSC.'
            mmsc-password:
               type: array
               suboptions:
                  type: str
            mmsc-port:
               type: int
               description: 'Port used on the MMSC for sending MMS messages (1 - 65535).'
            mmsc-url:
               type: str
               description: 'URL used on the MMSC for sending MMS messages.'
            mmsc-username:
               type: str
               description: 'User name required for authentication with the MMSC.'
            msg-protocol:
               type: str
               description: 'Protocol to use for sending notification messages.'
            msg-type:
               type: str
               description: 'MM7 message type.'
            protocol:
               type: str
               description: 'Protocol.'
            rate-limit:
               type: int
               description: 'Rate limit for sending notification messages (0 - 250).'
            tod-window-duration:
               type: str
               description: 'Time of day window duration.'
            tod-window-end:
               type: str
               description: 'Obsolete.'
            tod-window-start:
               type: str
               description: 'Time of day window start.'
            user-domain:
               type: str
               description: 'Domain name to which the user addresses belong.'
            vas-id:
               type: str
               description: 'VAS identifier.'
            vasp-id:
               type: str
               description: 'VASP identifier.'
            virus-int:
               type: int
               description: 'Virus notification send interval.'
            virus-int-mode:
               type: str
               description: 'Virus notification interval mode.'
            virus-status:
               type: str
               description: 'Virus notification status.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/firewall/mms-profile/{mms-profile}/notification'
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
            example: '/pm/config/adom/{adom}/obj/firewall/mms-profile/{mms-profile}/notification'

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
        '/pm/config/adom/{adom}/obj/firewall/mms-profile/{mms-profile}/notification',
        '/pm/config/global/obj/firewall/mms-profile/{mms-profile}/notification'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'mms-profile',
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
                        'alert-int': {
                            'type': 'integer'
                        },
                        'alert-int-mode': {
                            'type': 'string',
                            'enum': [
                                'hours',
                                'minutes'
                            ]
                        },
                        'alert-src-msisdn': {
                            'type': 'string'
                        },
                        'alert-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'bword-int': {
                            'type': 'integer'
                        },
                        'bword-int-mode': {
                            'type': 'string',
                            'enum': [
                                'hours',
                                'minutes'
                            ]
                        },
                        'bword-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'carrier-endpoint-bwl-int': {
                            'type': 'integer'
                        },
                        'carrier-endpoint-bwl-int-mode': {
                            'type': 'string',
                            'enum': [
                                'hours',
                                'minutes'
                            ]
                        },
                        'carrier-endpoint-bwl-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'days-allowed': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'sunday',
                                    'monday',
                                    'tuesday',
                                    'wednesday',
                                    'thursday',
                                    'friday',
                                    'saturday'
                                ]
                            }
                        },
                        'detect-server': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'dupe-int': {
                            'type': 'integer'
                        },
                        'dupe-int-mode': {
                            'type': 'string',
                            'enum': [
                                'hours',
                                'minutes'
                            ]
                        },
                        'dupe-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'file-block-int': {
                            'type': 'integer'
                        },
                        'file-block-int-mode': {
                            'type': 'string',
                            'enum': [
                                'hours',
                                'minutes'
                            ]
                        },
                        'file-block-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'flood-int': {
                            'type': 'integer'
                        },
                        'flood-int-mode': {
                            'type': 'string',
                            'enum': [
                                'hours',
                                'minutes'
                            ]
                        },
                        'flood-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'from-in-header': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mms-checksum-int': {
                            'type': 'integer'
                        },
                        'mms-checksum-int-mode': {
                            'type': 'string',
                            'enum': [
                                'hours',
                                'minutes'
                            ]
                        },
                        'mms-checksum-status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'mmsc-hostname': {
                            'type': 'string'
                        },
                        'mmsc-password': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'mmsc-port': {
                            'type': 'integer'
                        },
                        'mmsc-url': {
                            'type': 'string'
                        },
                        'mmsc-username': {
                            'type': 'string'
                        },
                        'msg-protocol': {
                            'type': 'string',
                            'enum': [
                                'mm1',
                                'mm3',
                                'mm4',
                                'mm7'
                            ]
                        },
                        'msg-type': {
                            'type': 'string',
                            'enum': [
                                'submit-req',
                                'deliver-req'
                            ]
                        },
                        'protocol': {
                            'type': 'string'
                        },
                        'rate-limit': {
                            'type': 'integer'
                        },
                        'tod-window-duration': {
                            'type': 'string'
                        },
                        'tod-window-end': {
                            'type': 'string'
                        },
                        'tod-window-start': {
                            'type': 'string'
                        },
                        'user-domain': {
                            'type': 'string'
                        },
                        'vas-id': {
                            'type': 'string'
                        },
                        'vasp-id': {
                            'type': 'string'
                        },
                        'virus-int': {
                            'type': 'integer'
                        },
                        'virus-int-mode': {
                            'type': 'string',
                            'enum': [
                                'hours',
                                'minutes'
                            ]
                        },
                        'virus-status': {
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
