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
module: fmgr_pm_config_devprof_log_fortianalyzer_setting
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/devprof/{devprof}/log/fortianalyzer/setting
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
            devprof:
                type: str
    schema_object0:
        methods: [get]
        description: 'Global FortiAnalyzer settings.'
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
        description: 'Global FortiAnalyzer settings.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                certificate:
                    type: str
                    description: 'Certificate used to communicate with FortiAnalyzer.'
                conn-timeout:
                    type: int
                    description: 'FortiAnalyzer connection time-out in seconds (for status and log buffer).'
                enc-algorithm:
                    type: str
                    description: 'Enable/disable sending FortiAnalyzer log data with SSL encryption.'
                    choices:
                        - 'default'
                        - 'high'
                        - 'low'
                        - 'disable'
                        - 'high-medium'
                        - 'low-medium'
                hmac-algorithm:
                    type: str
                    description: 'FortiAnalyzer IPsec tunnel HMAC algorithm.'
                    choices:
                        - 'sha256'
                        - 'sha1'
                ips-archive:
                    type: str
                    description: 'Enable/disable IPS packet archive logging.'
                    choices:
                        - 'disable'
                        - 'enable'
                monitor-failure-retry-period:
                    type: int
                    description: 'Time between FortiAnalyzer connection retries in seconds (for status and log buffer).'
                monitor-keepalive-period:
                    type: int
                    description: 'Time between OFTP keepalives in seconds (for status and log buffer).'
                reliable:
                    type: str
                    description: 'Enable/disable reliable logging to FortiAnalyzer.'
                    choices:
                        - 'disable'
                        - 'enable'
                ssl-min-proto-version:
                    type: str
                    description: 'Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).'
                    choices:
                        - 'default'
                        - 'TLSv1'
                        - 'TLSv1-1'
                        - 'TLSv1-2'
                        - 'SSLv3'
                upload-day:
                    type: str
                    description: 'Day of week (month) to upload logs.'
                upload-interval:
                    type: str
                    description: 'Frequency to upload log files to FortiAnalyzer.'
                    choices:
                        - 'daily'
                        - 'weekly'
                        - 'monthly'
                upload-option:
                    type: str
                    description: 'Enable/disable logging to hard disk and then uploading to FortiAnalyzer.'
                    choices:
                        - 'store-and-upload'
                        - 'realtime'
                        - '1-minute'
                        - '5-minute'
                upload-time:
                    type: str
                    description: 'Time to upload logs (hh:mm).'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/DEVPROF/{DEVPROF}/LOG/FORTIANALYZER/SETTING
      fmgr_pm_config_devprof_log_fortianalyzer_setting:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            devprof: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/DEVPROF/{DEVPROF}/LOG/FORTIANALYZER/SETTING
      fmgr_pm_config_devprof_log_fortianalyzer_setting:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            devprof: <value of string>
         params:
            -
               data:
                  certificate: <value of string>
                  conn-timeout: <value of integer>
                  enc-algorithm: <value in [default, high, low, ...]>
                  hmac-algorithm: <value in [sha256, sha1]>
                  ips-archive: <value in [disable, enable]>
                  monitor-failure-retry-period: <value of integer>
                  monitor-keepalive-period: <value of integer>
                  reliable: <value in [disable, enable]>
                  ssl-min-proto-version: <value in [default, TLSv1, TLSv1-1, ...]>
                  upload-day: <value of string>
                  upload-interval: <value in [daily, weekly, monthly]>
                  upload-option: <value in [store-and-upload, realtime, 1-minute, ...]>
                  upload-time: <value of string>

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
            certificate:
               type: str
               description: 'Certificate used to communicate with FortiAnalyzer.'
            conn-timeout:
               type: int
               description: 'FortiAnalyzer connection time-out in seconds (for status and log buffer).'
            enc-algorithm:
               type: str
               description: 'Enable/disable sending FortiAnalyzer log data with SSL encryption.'
            hmac-algorithm:
               type: str
               description: 'FortiAnalyzer IPsec tunnel HMAC algorithm.'
            ips-archive:
               type: str
               description: 'Enable/disable IPS packet archive logging.'
            monitor-failure-retry-period:
               type: int
               description: 'Time between FortiAnalyzer connection retries in seconds (for status and log buffer).'
            monitor-keepalive-period:
               type: int
               description: 'Time between OFTP keepalives in seconds (for status and log buffer).'
            reliable:
               type: str
               description: 'Enable/disable reliable logging to FortiAnalyzer.'
            ssl-min-proto-version:
               type: str
               description: 'Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).'
            upload-day:
               type: str
               description: 'Day of week (month) to upload logs.'
            upload-interval:
               type: str
               description: 'Frequency to upload log files to FortiAnalyzer.'
            upload-option:
               type: str
               description: 'Enable/disable logging to hard disk and then uploading to FortiAnalyzer.'
            upload-time:
               type: str
               description: 'Time to upload logs (hh:mm).'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/devprof/{devprof}/log/fortianalyzer/setting'
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
            example: '/pm/config/adom/{adom}/devprof/{devprof}/log/fortianalyzer/setting'

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
        '/pm/config/adom/{adom}/devprof/{devprof}/log/fortianalyzer/setting'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'devprof',
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
                        'certificate': {
                            'type': 'string'
                        },
                        'conn-timeout': {
                            'type': 'integer'
                        },
                        'enc-algorithm': {
                            'type': 'string',
                            'enum': [
                                'default',
                                'high',
                                'low',
                                'disable',
                                'high-medium',
                                'low-medium'
                            ]
                        },
                        'hmac-algorithm': {
                            'type': 'string',
                            'enum': [
                                'sha256',
                                'sha1'
                            ]
                        },
                        'ips-archive': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'monitor-failure-retry-period': {
                            'type': 'integer'
                        },
                        'monitor-keepalive-period': {
                            'type': 'integer'
                        },
                        'reliable': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ssl-min-proto-version': {
                            'type': 'string',
                            'enum': [
                                'default',
                                'TLSv1',
                                'TLSv1-1',
                                'TLSv1-2',
                                'SSLv3'
                            ]
                        },
                        'upload-day': {
                            'type': 'string'
                        },
                        'upload-interval': {
                            'type': 'string',
                            'enum': [
                                'daily',
                                'weekly',
                                'monthly'
                            ]
                        },
                        'upload-option': {
                            'type': 'string',
                            'enum': [
                                'store-and-upload',
                                'realtime',
                                '1-minute',
                                '5-minute'
                            ]
                        },
                        'upload-time': {
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
