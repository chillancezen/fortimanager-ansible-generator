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
module: fmgr_webfilter_profile_ftgdwf
short_description: FortiGuard Web Filter settings.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/webfilter/profile/{profile}/ftgd-wf
    - /pm/config/global/obj/webfilter/profile/{profile}/ftgd-wf
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
            profile:
                type: str
    schema_object0:
        methods: [get]
        description: 'FortiGuard Web Filter settings.'
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
        description: 'FortiGuard Web Filter settings.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                exempt-quota:
                    type: str
                    description: 'Do not stop quota for these categories.'
                filters:
                    -
                        action:
                            type: str
                            description: 'Action to take for matches.'
                            choices:
                                - 'block'
                                - 'monitor'
                                - 'warning'
                                - 'authenticate'
                        auth-usr-grp:
                            type: str
                            description: 'Groups with permission to authenticate.'
                        category:
                            type: str
                            description: 'Categories and groups the filter examines.'
                        id:
                            type: int
                            description: 'ID number.'
                        log:
                            type: str
                            description: 'Enable/disable logging.'
                            choices:
                                - 'disable'
                                - 'enable'
                        override-replacemsg:
                            type: str
                            description: 'Override replacement message.'
                        warn-duration:
                            type: str
                            description: 'Duration of warnings.'
                        warning-duration-type:
                            type: str
                            description: 'Re-display warning after closing browser or after a timeout.'
                            choices:
                                - 'session'
                                - 'timeout'
                        warning-prompt:
                            type: str
                            description: 'Warning prompts in each category or each domain.'
                            choices:
                                - 'per-domain'
                                - 'per-category'
                max-quota-timeout:
                    type: int
                    description: 'Maximum FortiGuard quota used by single page view in seconds (excludes streams).'
                options:
                    -
                        type: str
                        choices:
                            - 'error-allow'
                            - 'http-err-detail'
                            - 'rate-image-urls'
                            - 'strict-blocking'
                            - 'rate-server-ip'
                            - 'redir-block'
                            - 'connect-request-bypass'
                            - 'log-all-url'
                            - 'ftgd-disable'
                ovrd:
                    type: str
                    description: 'Allow web filter profile overrides.'
                quota:
                    -
                        category:
                            type: str
                            description: 'FortiGuard categories to apply quota to (category action must be set to monitor).'
                        duration:
                            type: str
                            description: 'Duration of quota.'
                        id:
                            type: int
                            description: 'ID number.'
                        override-replacemsg:
                            type: str
                            description: 'Override replacement message.'
                        type:
                            type: str
                            description: 'Quota type.'
                            choices:
                                - 'time'
                                - 'traffic'
                        unit:
                            type: str
                            description: 'Traffic quota unit of measurement.'
                            choices:
                                - 'B'
                                - 'KB'
                                - 'MB'
                                - 'GB'
                        value:
                            type: int
                            description: 'Traffic quota value.'
                rate-crl-urls:
                    type: str
                    description: 'Enable/disable rating CRL by URL.'
                    choices:
                        - 'disable'
                        - 'enable'
                rate-css-urls:
                    type: str
                    description: 'Enable/disable rating CSS by URL.'
                    choices:
                        - 'disable'
                        - 'enable'
                rate-image-urls:
                    type: str
                    description: 'Enable/disable rating images by URL.'
                    choices:
                        - 'disable'
                        - 'enable'
                rate-javascript-urls:
                    type: str
                    description: 'Enable/disable rating JavaScript by URL.'
                    choices:
                        - 'disable'
                        - 'enable'

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

    - name: REQUESTING /PM/CONFIG/OBJ/WEBFILTER/PROFILE/{PROFILE}/FTGD-WF
      fmgr_webfilter_profile_ftgdwf:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/WEBFILTER/PROFILE/{PROFILE}/FTGD-WF
      fmgr_webfilter_profile_ftgdwf:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               data:
                  exempt-quota: <value of string>
                  filters:
                    -
                        action: <value in [block, monitor, warning, ...]>
                        auth-usr-grp: <value of string>
                        category: <value of string>
                        id: <value of integer>
                        log: <value in [disable, enable]>
                        override-replacemsg: <value of string>
                        warn-duration: <value of string>
                        warning-duration-type: <value in [session, timeout]>
                        warning-prompt: <value in [per-domain, per-category]>
                  max-quota-timeout: <value of integer>
                  options:
                    - <value in [error-allow, http-err-detail, rate-image-urls, ...]>
                  ovrd: <value of string>
                  quota:
                    -
                        category: <value of string>
                        duration: <value of string>
                        id: <value of integer>
                        override-replacemsg: <value of string>
                        type: <value in [time, traffic]>
                        unit: <value in [B, KB, MB, ...]>
                        value: <value of integer>
                  rate-crl-urls: <value in [disable, enable]>
                  rate-css-urls: <value in [disable, enable]>
                  rate-image-urls: <value in [disable, enable]>
                  rate-javascript-urls: <value in [disable, enable]>

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
            exempt-quota:
               type: str
               description: 'Do not stop quota for these categories.'
            filters:
               type: array
               suboptions:
                  action:
                     type: str
                     description: 'Action to take for matches.'
                  auth-usr-grp:
                     type: str
                     description: 'Groups with permission to authenticate.'
                  category:
                     type: str
                     description: 'Categories and groups the filter examines.'
                  id:
                     type: int
                     description: 'ID number.'
                  log:
                     type: str
                     description: 'Enable/disable logging.'
                  override-replacemsg:
                     type: str
                     description: 'Override replacement message.'
                  warn-duration:
                     type: str
                     description: 'Duration of warnings.'
                  warning-duration-type:
                     type: str
                     description: 'Re-display warning after closing browser or after a timeout.'
                  warning-prompt:
                     type: str
                     description: 'Warning prompts in each category or each domain.'
            max-quota-timeout:
               type: int
               description: 'Maximum FortiGuard quota used by single page view in seconds (excludes streams).'
            options:
               type: array
               suboptions:
                  type: str
            ovrd:
               type: str
               description: 'Allow web filter profile overrides.'
            quota:
               type: array
               suboptions:
                  category:
                     type: str
                     description: 'FortiGuard categories to apply quota to (category action must be set to monitor).'
                  duration:
                     type: str
                     description: 'Duration of quota.'
                  id:
                     type: int
                     description: 'ID number.'
                  override-replacemsg:
                     type: str
                     description: 'Override replacement message.'
                  type:
                     type: str
                     description: 'Quota type.'
                  unit:
                     type: str
                     description: 'Traffic quota unit of measurement.'
                  value:
                     type: int
                     description: 'Traffic quota value.'
            rate-crl-urls:
               type: str
               description: 'Enable/disable rating CRL by URL.'
            rate-css-urls:
               type: str
               description: 'Enable/disable rating CSS by URL.'
            rate-image-urls:
               type: str
               description: 'Enable/disable rating images by URL.'
            rate-javascript-urls:
               type: str
               description: 'Enable/disable rating JavaScript by URL.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/webfilter/profile/{profile}/ftgd-wf'
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
            example: '/pm/config/adom/{adom}/obj/webfilter/profile/{profile}/ftgd-wf'

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
        '/pm/config/adom/{adom}/obj/webfilter/profile/{profile}/ftgd-wf',
        '/pm/config/global/obj/webfilter/profile/{profile}/ftgd-wf'
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
                        'exempt-quota': {
                            'type': 'string'
                        },
                        'filters': {
                            'type': 'array',
                            'items': {
                                'action': {
                                    'type': 'string',
                                    'enum': [
                                        'block',
                                        'monitor',
                                        'warning',
                                        'authenticate'
                                    ]
                                },
                                'auth-usr-grp': {
                                    'type': 'string'
                                },
                                'category': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'log': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'override-replacemsg': {
                                    'type': 'string'
                                },
                                'warn-duration': {
                                    'type': 'string'
                                },
                                'warning-duration-type': {
                                    'type': 'string',
                                    'enum': [
                                        'session',
                                        'timeout'
                                    ]
                                },
                                'warning-prompt': {
                                    'type': 'string',
                                    'enum': [
                                        'per-domain',
                                        'per-category'
                                    ]
                                }
                            }
                        },
                        'max-quota-timeout': {
                            'type': 'integer'
                        },
                        'options': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'error-allow',
                                    'http-err-detail',
                                    'rate-image-urls',
                                    'strict-blocking',
                                    'rate-server-ip',
                                    'redir-block',
                                    'connect-request-bypass',
                                    'log-all-url',
                                    'ftgd-disable'
                                ]
                            }
                        },
                        'ovrd': {
                            'type': 'string'
                        },
                        'quota': {
                            'type': 'array',
                            'items': {
                                'category': {
                                    'type': 'string'
                                },
                                'duration': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'override-replacemsg': {
                                    'type': 'string'
                                },
                                'type': {
                                    'type': 'string',
                                    'enum': [
                                        'time',
                                        'traffic'
                                    ]
                                },
                                'unit': {
                                    'type': 'string',
                                    'enum': [
                                        'B',
                                        'KB',
                                        'MB',
                                        'GB'
                                    ]
                                },
                                'value': {
                                    'type': 'integer'
                                }
                            }
                        },
                        'rate-crl-urls': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'rate-css-urls': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'rate-image-urls': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'rate-javascript-urls': {
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
        'loose_validation': {
            'type': 'bool',
            'required': False,
            'default': False
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
