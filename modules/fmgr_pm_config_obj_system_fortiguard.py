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
module: fmgr_pm_config_obj_system_fortiguard
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis:
    - /pm/config/adom/{adom}/obj/system/fortiguard
    - /pm/config/global/obj/system/fortiguard
    - Examples include all parameters and values need to be adjusted to data 
      sources before usage.
     

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
        methods: [get]
        description: 'Configure FortiGuard services.'
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
        description: 'Configure FortiGuard services.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                antispam-cache:
                    type: str
                    description: 'Enable/disable FortiGuard antispam request caching. Uses a small amount of memory but improves performance.'
                    choices:
                        - disable
                        - enable
                antispam-cache-mpercent:
                    type: int
                    description: 'Maximum percent of FortiGate memory the antispam cache is allowed to use (1 - 15%).'
                antispam-cache-ttl:
                    type: int
                    description: 'Time-to-live for antispam cache entries in seconds (300 - 86400). Lower times reduce the cache size. Higher times may improve performance since the cache will have more entries.'
                antispam-expiration:
                    type: int
                antispam-force-off:
                    type: str
                    description: 'Enable/disable turning off the FortiGuard antispam service.'
                    choices:
                        - disable
                        - enable
                antispam-license:
                    type: int
                antispam-timeout:
                    type: int
                    description: 'Antispam query time out (1 - 30 sec, default = 7).'
                auto-join-forticloud:
                    type: str
                    description: 'Automatically connect to and login to FortiCloud.'
                    choices:
                        - disable
                        - enable
                ddns-server-ip:
                    type: str
                    description: 'IP address of the FortiDDNS server.'
                ddns-server-port:
                    type: int
                    description: 'Port used to communicate with FortiDDNS servers.'
                load-balance-servers:
                    type: int
                    description: 'Number of servers to alternate between as first FortiGuard option.'
                outbreak-prevention-cache:
                    type: str
                    description: 'Enable/disable FortiGuard Virus Outbreak Prevention cache.'
                    choices:
                        - disable
                        - enable
                outbreak-prevention-cache-mpercent:
                    type: int
                    description: 'Maximum percent of memory FortiGuard Virus Outbreak Prevention cache can use (1 - 15%, default = 2).'
                outbreak-prevention-cache-ttl:
                    type: int
                    description: 'Time-to-live for FortiGuard Virus Outbreak Prevention cache entries (300 - 86400 sec, default = 300).'
                outbreak-prevention-expiration:
                    type: int
                outbreak-prevention-force-off:
                    type: str
                    description: 'Turn off FortiGuard Virus Outbreak Prevention service.'
                    choices:
                        - disable
                        - enable
                outbreak-prevention-license:
                    type: int
                outbreak-prevention-timeout:
                    type: int
                    description: 'FortiGuard Virus Outbreak Prevention time out (1 - 30 sec, default = 7).'
                port:
                    type: str
                    description: 'Port used to communicate with the FortiGuard servers.'
                    choices:
                        - 53
                        - 80
                        - 8888
                sdns-server-ip:
                    -
                        type: str
                sdns-server-port:
                    type: int
                    description: 'Port used to communicate with FortiDNS servers.'
                service-account-id:
                    type: str
                    description: 'Service account ID.'
                source-ip:
                    type: str
                    description: 'Source IPv4 address used to communicate with FortiGuard.'
                source-ip6:
                    type: str
                    description: 'Source IPv6 address used to communicate with FortiGuard.'
                update-server-location:
                    type: str
                    description: 'Signature update server location.'
                    choices:
                        - any
                        - usa
                webfilter-cache:
                    type: str
                    description: 'Enable/disable FortiGuard web filter caching.'
                    choices:
                        - disable
                        - enable
                webfilter-cache-ttl:
                    type: int
                    description: 'Time-to-live for web filter cache entries in seconds (300 - 86400).'
                webfilter-expiration:
                    type: int
                webfilter-force-off:
                    type: str
                    description: 'Enable/disable turning off the FortiGuard web filtering service.'
                    choices:
                        - disable
                        - enable
                webfilter-license:
                    type: int
                webfilter-timeout:
                    type: int
                    description: 'Web filter query time out (1 - 30 sec, default = 7).'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /pm/config/obj/system/fortiguard
      fmgr_pm_config_obj_system_fortiguard:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            - 
               option: <value in [object member, chksum, datasrc]>
    - name: send request to /pm/config/obj/system/fortiguard
      fmgr_pm_config_obj_system_fortiguard:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            - 
               data: 
                  antispam-cache: <value in [disable, enable]>
                  antispam-cache-mpercent: <value of integer>
                  antispam-cache-ttl: <value of integer>
                  antispam-expiration: <value of integer>
                  antispam-force-off: <value in [disable, enable]>
                  antispam-license: <value of integer>
                  antispam-timeout: <value of integer>
                  auto-join-forticloud: <value in [disable, enable]>
                  ddns-server-ip: <value of string>
                  ddns-server-port: <value of integer>
                  load-balance-servers: <value of integer>
                  outbreak-prevention-cache: <value in [disable, enable]>
                  outbreak-prevention-cache-mpercent: <value of integer>
                  outbreak-prevention-cache-ttl: <value of integer>
                  outbreak-prevention-expiration: <value of integer>
                  outbreak-prevention-force-off: <value in [disable, enable]>
                  outbreak-prevention-license: <value of integer>
                  outbreak-prevention-timeout: <value of integer>
                  port: <value in [53, 80, 8888]>
                  sdns-server-ip: 
                   - <value of string>
                  sdns-server-port: <value of integer>
                  service-account-id: <value of string>
                  source-ip: <value of string>
                  source-ip6: <value of string>
                  update-server-location: <value in [any, usa]>
                  webfilter-cache: <value in [disable, enable]>
                  webfilter-cache-ttl: <value of integer>
                  webfilter-expiration: <value of integer>
                  webfilter-force-off: <value in [disable, enable]>
                  webfilter-license: <value of integer>
                  webfilter-timeout: <value of integer>

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
            antispam-cache:
               type: str
               description: 'Enable/disable FortiGuard antispam request caching. Uses a small amount of memory but improves performance.'
            antispam-cache-mpercent:
               type: int
               description: 'Maximum percent of FortiGate memory the antispam cache is allowed to use (1 - 15%).'
            antispam-cache-ttl:
               type: int
               description: 'Time-to-live for antispam cache entries in seconds (300 - 86400). Lower times reduce the cache size. Higher times may improve performance since the cache will have more entries.'
            antispam-expiration:
               type: int
            antispam-force-off:
               type: str
               description: 'Enable/disable turning off the FortiGuard antispam service.'
            antispam-license:
               type: int
            antispam-timeout:
               type: int
               description: 'Antispam query time out (1 - 30 sec, default = 7).'
            auto-join-forticloud:
               type: str
               description: 'Automatically connect to and login to FortiCloud.'
            ddns-server-ip:
               type: str
               description: 'IP address of the FortiDDNS server.'
            ddns-server-port:
               type: int
               description: 'Port used to communicate with FortiDDNS servers.'
            load-balance-servers:
               type: int
               description: 'Number of servers to alternate between as first FortiGuard option.'
            outbreak-prevention-cache:
               type: str
               description: 'Enable/disable FortiGuard Virus Outbreak Prevention cache.'
            outbreak-prevention-cache-mpercent:
               type: int
               description: 'Maximum percent of memory FortiGuard Virus Outbreak Prevention cache can use (1 - 15%, default = 2).'
            outbreak-prevention-cache-ttl:
               type: int
               description: 'Time-to-live for FortiGuard Virus Outbreak Prevention cache entries (300 - 86400 sec, default = 300).'
            outbreak-prevention-expiration:
               type: int
            outbreak-prevention-force-off:
               type: str
               description: 'Turn off FortiGuard Virus Outbreak Prevention service.'
            outbreak-prevention-license:
               type: int
            outbreak-prevention-timeout:
               type: int
               description: 'FortiGuard Virus Outbreak Prevention time out (1 - 30 sec, default = 7).'
            port:
               type: str
               description: 'Port used to communicate with the FortiGuard servers.'
            sdns-server-ip:
               type: array
               suboptions:
                  type: str
            sdns-server-port:
               type: int
               description: 'Port used to communicate with FortiDNS servers.'
            service-account-id:
               type: str
               description: 'Service account ID.'
            source-ip:
               type: str
               description: 'Source IPv4 address used to communicate with FortiGuard.'
            source-ip6:
               type: str
               description: 'Source IPv6 address used to communicate with FortiGuard.'
            update-server-location:
               type: str
               description: 'Signature update server location.'
            webfilter-cache:
               type: str
               description: 'Enable/disable FortiGuard web filter caching.'
            webfilter-cache-ttl:
               type: int
               description: 'Time-to-live for web filter cache entries in seconds (300 - 86400).'
            webfilter-expiration:
               type: int
            webfilter-force-off:
               type: str
               description: 'Enable/disable turning off the FortiGuard web filtering service.'
            webfilter-license:
               type: int
            webfilter-timeout:
               type: int
               description: 'Web filter query time out (1 - 30 sec, default = 7).'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/obj/system/fortiguard
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
            example: /pm/config/adom/{adom}/obj/system/fortiguard

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
        '/pm/config/adom/{adom}/obj/system/fortiguard',
        '/pm/config/global/obj/system/fortiguard'
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
                        'antispam-cache': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'antispam-cache-mpercent': {
                            'type': 'integer'
                        },
                        'antispam-cache-ttl': {
                            'type': 'integer'
                        },
                        'antispam-expiration': {
                            'type': 'integer'
                        },
                        'antispam-force-off': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'antispam-license': {
                            'type': 'integer'
                        },
                        'antispam-timeout': {
                            'type': 'integer'
                        },
                        'auto-join-forticloud': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ddns-server-ip': {
                            'type': 'string'
                        },
                        'ddns-server-port': {
                            'type': 'integer'
                        },
                        'load-balance-servers': {
                            'type': 'integer'
                        },
                        'outbreak-prevention-cache': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'outbreak-prevention-cache-mpercent': {
                            'type': 'integer'
                        },
                        'outbreak-prevention-cache-ttl': {
                            'type': 'integer'
                        },
                        'outbreak-prevention-expiration': {
                            'type': 'integer'
                        },
                        'outbreak-prevention-force-off': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'outbreak-prevention-license': {
                            'type': 'integer'
                        },
                        'outbreak-prevention-timeout': {
                            'type': 'integer'
                        },
                        'port': {
                            'type': 'string',
                            'enum': [
                                '53',
                                '80',
                                '8888'
                            ]
                        },
                        'sdns-server-ip': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'sdns-server-port': {
                            'type': 'integer'
                        },
                        'service-account-id': {
                            'type': 'string'
                        },
                        'source-ip': {
                            'type': 'string'
                        },
                        'source-ip6': {
                            'type': 'string'
                        },
                        'update-server-location': {
                            'type': 'string',
                            'enum': [
                                'any',
                                'usa'
                            ]
                        },
                        'webfilter-cache': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'webfilter-cache-ttl': {
                            'type': 'integer'
                        },
                        'webfilter-expiration': {
                            'type': 'integer'
                        },
                        'webfilter-force-off': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'webfilter-license': {
                            'type': 'integer'
                        },
                        'webfilter-timeout': {
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