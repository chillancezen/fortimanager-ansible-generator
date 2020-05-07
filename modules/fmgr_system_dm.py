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
module: fmgr_system_dm
short_description: Configure dm.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /cli/global/system/dm
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
    loose_validation:
        description: Do parameter validation in a loose way
        required: False
        type: bool
        default: false
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
    schema_object0:
        methods: [get]
        description: 'Configure dm.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Configure dm.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                concurrent-install-image-limit:
                    type: int
                    default: 500
                    description: 'Maximum number of concurrent install image (1 - 1000).'
                concurrent-install-limit:
                    type: int
                    default: 480
                    description: 'Maximum number of concurrent installs (5 - 2000).'
                concurrent-install-script-limit:
                    type: int
                    default: 480
                    description: 'Maximum number of concurrent install scripts (5 - 2000).'
                discover-timeout:
                    type: int
                    default: 6
                    description: 'Check connection timeout when discover device (3 - 15).'
                dpm-logsize:
                    type: int
                    default: 10000
                    description: 'Maximum dpm log size per device (1 - 10000K).'
                fgfm-sock-timeout:
                    type: int
                    default: 360
                    description: 'Maximum FGFM socket idle time (90 - 1800 sec).'
                fgfm_keepalive_itvl:
                    type: int
                    default: 120
                    description: 'FGFM protocol keep alive interval (30 - 600 sec).'
                force-remote-diff:
                    type: str
                    default: 'disable'
                    description:
                     - 'Always use remote diff when installing.'
                     - 'disable - Disable.'
                     - 'enable - Enable.'
                    choices:
                        - 'disable'
                        - 'enable'
                fortiap-refresh-cnt:
                    type: int
                    default: 500
                    description: 'Max auto refresh FortiAP number each time (1 - 10000).'
                fortiap-refresh-itvl:
                    type: int
                    default: 10
                    description: 'Auto refresh FortiAP status interval (0 - 1440) minutes, set to 0 will disable auto refresh.'
                fortiext-refresh-cnt:
                    type: int
                    default: 50
                    description: 'Max device number for FortiExtender auto refresh (1 - 10000).'
                install-image-timeout:
                    type: int
                    default: 3600
                    description: 'Maximum waiting time for image transfer and device upgrade (600 - 7200 sec).'
                install-tunnel-retry-itvl:
                    type: int
                    default: 60
                    description: 'Time to re-establish tunnel during install (10 - 60 sec).'
                max-revs:
                    type: int
                    default: 100
                    description: 'Maximum number of revisions saved (1 - 250).'
                nr-retry:
                    type: int
                    default: 1
                    description: 'Number of retries.'
                retry:
                    type: str
                    default: 'enable'
                    description:
                     - 'Enable/disable configuration install retry.'
                     - 'disable - Disable.'
                     - 'enable - Enable.'
                    choices:
                        - 'disable'
                        - 'enable'
                retry-intvl:
                    type: int
                    default: 15
                    description: 'Retry interval.'
                rollback-allow-reboot:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable FortiGate reboot to rollback when installing script/config.'
                     - 'disable - Disable.'
                     - 'enable - Enable.'
                    choices:
                        - 'disable'
                        - 'enable'
                script-logsize:
                    type: int
                    default: 100
                    description: 'Maximum script log size per device (1 - 10000K).'
                skip-scep-check:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable installing scep related objects even if scep url is configured.'
                     - 'disable - Disable.'
                     - 'enable - Enable.'
                    choices:
                        - 'disable'
                        - 'enable'
                skip-tunnel-fcp-req:
                    type: str
                    default: 'enable'
                    description:
                     - 'Enable/disable skip the fcp request sent from fgfm tunnel'
                     - 'disable - Disable.'
                     - 'enable - Enable.'
                    choices:
                        - 'disable'
                        - 'enable'
                verify-install:
                    type: str
                    default: 'enable'
                    description:
                     - 'Verify install against remote configuration.'
                     - 'disable - Disable.'
                     - 'optimal - Verify installation for command errors.'
                     - 'enable - Always verify installation.'
                    choices:
                        - 'disable'
                        - 'optimal'
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

    - name: REQUESTING /CLI/SYSTEM/DM
      fmgr_system_dm:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [set, update]>
         params:
            -
               data:
                  concurrent-install-image-limit: <value of integer default: 500>
                  concurrent-install-limit: <value of integer default: 480>
                  concurrent-install-script-limit: <value of integer default: 480>
                  discover-timeout: <value of integer default: 6>
                  dpm-logsize: <value of integer default: 10000>
                  fgfm-sock-timeout: <value of integer default: 360>
                  fgfm_keepalive_itvl: <value of integer default: 120>
                  force-remote-diff: <value in [disable, enable] default: 'disable'>
                  fortiap-refresh-cnt: <value of integer default: 500>
                  fortiap-refresh-itvl: <value of integer default: 10>
                  fortiext-refresh-cnt: <value of integer default: 50>
                  install-image-timeout: <value of integer default: 3600>
                  install-tunnel-retry-itvl: <value of integer default: 60>
                  max-revs: <value of integer default: 100>
                  nr-retry: <value of integer default: 1>
                  retry: <value in [disable, enable] default: 'enable'>
                  retry-intvl: <value of integer default: 15>
                  rollback-allow-reboot: <value in [disable, enable] default: 'disable'>
                  script-logsize: <value of integer default: 100>
                  skip-scep-check: <value in [disable, enable] default: 'disable'>
                  skip-tunnel-fcp-req: <value in [disable, enable] default: 'enable'>
                  verify-install: <value in [disable, optimal, enable] default: 'enable'>

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
            concurrent-install-image-limit:
               type: int
               description: 'Maximum number of concurrent install image (1 - 1000).'
               example: 500
            concurrent-install-limit:
               type: int
               description: 'Maximum number of concurrent installs (5 - 2000).'
               example: 480
            concurrent-install-script-limit:
               type: int
               description: 'Maximum number of concurrent install scripts (5 - 2000).'
               example: 480
            discover-timeout:
               type: int
               description: 'Check connection timeout when discover device (3 - 15).'
               example: 6
            dpm-logsize:
               type: int
               description: 'Maximum dpm log size per device (1 - 10000K).'
               example: 10000
            fgfm-sock-timeout:
               type: int
               description: 'Maximum FGFM socket idle time (90 - 1800 sec).'
               example: 360
            fgfm_keepalive_itvl:
               type: int
               description: 'FGFM protocol keep alive interval (30 - 600 sec).'
               example: 120
            force-remote-diff:
               type: str
               description: |
                  'Always use remote diff when installing.'
                  'disable - Disable.'
                  'enable - Enable.'
               example: 'disable'
            fortiap-refresh-cnt:
               type: int
               description: 'Max auto refresh FortiAP number each time (1 - 10000).'
               example: 500
            fortiap-refresh-itvl:
               type: int
               description: 'Auto refresh FortiAP status interval (0 - 1440) minutes, set to 0 will disable auto refresh.'
               example: 10
            fortiext-refresh-cnt:
               type: int
               description: 'Max device number for FortiExtender auto refresh (1 - 10000).'
               example: 50
            install-image-timeout:
               type: int
               description: 'Maximum waiting time for image transfer and device upgrade (600 - 7200 sec).'
               example: 3600
            install-tunnel-retry-itvl:
               type: int
               description: 'Time to re-establish tunnel during install (10 - 60 sec).'
               example: 60
            max-revs:
               type: int
               description: 'Maximum number of revisions saved (1 - 250).'
               example: 100
            nr-retry:
               type: int
               description: 'Number of retries.'
               example: 1
            retry:
               type: str
               description: |
                  'Enable/disable configuration install retry.'
                  'disable - Disable.'
                  'enable - Enable.'
               example: 'enable'
            retry-intvl:
               type: int
               description: 'Retry interval.'
               example: 15
            rollback-allow-reboot:
               type: str
               description: |
                  'Enable/disable FortiGate reboot to rollback when installing script/config.'
                  'disable - Disable.'
                  'enable - Enable.'
               example: 'disable'
            script-logsize:
               type: int
               description: 'Maximum script log size per device (1 - 10000K).'
               example: 100
            skip-scep-check:
               type: str
               description: |
                  'Enable/disable installing scep related objects even if scep url is configured.'
                  'disable - Disable.'
                  'enable - Enable.'
               example: 'disable'
            skip-tunnel-fcp-req:
               type: str
               description: |
                  'Enable/disable skip the fcp request sent from fgfm tunnel'
                  'disable - Disable.'
                  'enable - Enable.'
               example: 'enable'
            verify-install:
               type: str
               description: |
                  'Verify install against remote configuration.'
                  'disable - Disable.'
                  'optimal - Verify installation for command errors.'
                  'enable - Always verify installation.'
               example: 'enable'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/cli/global/system/dm'
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
            example: '/cli/global/system/dm'

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
        '/cli/global/system/dm'
    ]

    url_schema = [
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
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
                        'concurrent-install-image-limit': {
                            'type': 'integer',
                            'default': 500,
                            'example': 500
                        },
                        'concurrent-install-limit': {
                            'type': 'integer',
                            'default': 480,
                            'example': 480
                        },
                        'concurrent-install-script-limit': {
                            'type': 'integer',
                            'default': 480,
                            'example': 480
                        },
                        'discover-timeout': {
                            'type': 'integer',
                            'default': 6,
                            'example': 6
                        },
                        'dpm-logsize': {
                            'type': 'integer',
                            'default': 10000,
                            'example': 10000
                        },
                        'fgfm-sock-timeout': {
                            'type': 'integer',
                            'default': 360,
                            'example': 360
                        },
                        'fgfm_keepalive_itvl': {
                            'type': 'integer',
                            'default': 120,
                            'example': 120
                        },
                        'force-remote-diff': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fortiap-refresh-cnt': {
                            'type': 'integer',
                            'default': 500,
                            'example': 500
                        },
                        'fortiap-refresh-itvl': {
                            'type': 'integer',
                            'default': 10,
                            'example': 10
                        },
                        'fortiext-refresh-cnt': {
                            'type': 'integer',
                            'default': 50,
                            'example': 50
                        },
                        'install-image-timeout': {
                            'type': 'integer',
                            'default': 3600,
                            'example': 3600
                        },
                        'install-tunnel-retry-itvl': {
                            'type': 'integer',
                            'default': 60,
                            'example': 60
                        },
                        'max-revs': {
                            'type': 'integer',
                            'default': 100,
                            'example': 100
                        },
                        'nr-retry': {
                            'type': 'integer',
                            'default': 1,
                            'example': 1
                        },
                        'retry': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'retry-intvl': {
                            'type': 'integer',
                            'default': 15,
                            'example': 15
                        },
                        'rollback-allow-reboot': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'script-logsize': {
                            'type': 'integer',
                            'default': 100,
                            'example': 100
                        },
                        'skip-scep-check': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'skip-tunnel-fcp-req': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'verify-install': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'optimal',
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
