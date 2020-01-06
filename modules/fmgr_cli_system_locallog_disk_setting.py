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
module: fmgr_cli_system_locallog_disk_setting
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /cli/global/system/locallog/disk/setting
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
    schema_object0:
        methods: [get]
        description: 'Settings for local disk logging.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Settings for local disk logging.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                diskfull:
                    type: str
                    default: 'overwrite'
                    description:
                     - 'Policy to apply when disk is full.'
                     - 'overwrite - Overwrite oldest log when disk is full.'
                     - 'nolog - Stop logging when disk is full.'
                    choices:
                        - 'overwrite'
                        - 'nolog'
                log-disk-full-percentage:
                    type: int
                    default: 80
                    description: 'Consider log disk as full at this usage percentage.'
                max-log-file-size:
                    type: int
                    default: 100
                    description: 'Maximum log file size before rolling.'
                roll-day:
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
                roll-schedule:
                    type: str
                    default: 'none'
                    description:
                     - 'Frequency to check log file for rolling.'
                     - 'none - Not scheduled.'
                     - 'daily - Every day.'
                     - 'weekly - Every week.'
                    choices:
                        - 'none'
                        - 'daily'
                        - 'weekly'
                roll-time:
                    -
                        type: str
                server-type:
                    type: str
                    default: 'FTP'
                    description:
                     - 'Server type.'
                     - 'FTP - Upload via FTP.'
                     - 'SFTP - Upload via SFTP.'
                     - 'SCP - Upload via SCP.'
                    choices:
                        - 'FTP'
                        - 'SFTP'
                        - 'SCP'
                severity:
                    type: str
                    default: 'information'
                    description:
                     - 'Least severity level to log.'
                     - 'emergency - Emergency level.'
                     - 'alert - Alert level.'
                     - 'critical - Critical level.'
                     - 'error - Error level.'
                     - 'warning - Warning level.'
                     - 'notification - Notification level.'
                     - 'information - Information level.'
                     - 'debug - Debug level.'
                    choices:
                        - 'emergency'
                        - 'alert'
                        - 'critical'
                        - 'error'
                        - 'warning'
                        - 'notification'
                        - 'information'
                        - 'debug'
                status:
                    type: str
                    default: 'enable'
                    description:
                     - 'Enable/disable local disk log.'
                     - 'disable - Do not log to local disk.'
                     - 'enable - Log to local disk.'
                    choices:
                        - 'disable'
                        - 'enable'
                upload:
                    type: str
                    default: 'disable'
                    description:
                     - 'Upload log file when rolling.'
                     - 'disable - Disable uploading when rolling log file.'
                     - 'enable - Enable uploading when rolling log file.'
                    choices:
                        - 'disable'
                        - 'enable'
                upload-delete-files:
                    type: str
                    default: 'enable'
                    description:
                     - 'Delete log files after uploading (default = enable).'
                     - 'disable - Do not delete log files after uploading.'
                     - 'enable - Delete log files after uploading.'
                    choices:
                        - 'disable'
                        - 'enable'
                upload-time:
                    -
                        type: str
                uploaddir:
                    type: str
                    description: 'Log file upload remote directory.'
                uploadip:
                    type: str
                    default: '0.0.0.0'
                    description: 'IP address of log uploading server.'
                uploadpass:
                    -
                        type: str
                        default: 'ENC NDk0NjE4Nzg3MjIwODA3N71+qrz/6PhYvtMUVz84NXNAP8LBSobOqp91xwfif6Oy3+uy8/crasneRp4VbtBQntyLw7E8MbzHoUlJp8Y2cQLnVfVsTQsRfvtq/BZcpTL+c2yDARD0Bvd1khGe4e1mCVFSVuCTSXxm6CmxqPpcGKFfHLyn'
                uploadport:
                    type: int
                    default: 0
                    description: 'Server port (0 = default protocol port).'
                uploadsched:
                    type: str
                    default: 'disable'
                    description:
                     - 'Scheduled upload (disable = upload when rolling).'
                     - 'disable - Upload when rolling.'
                     - 'enable - Scheduled upload.'
                    choices:
                        - 'disable'
                        - 'enable'
                uploadtype:
                    -
                        type: str
                        choices:
                            - 'event'
                uploaduser:
                    type: str
                    description: 'User account in upload server.'
                uploadzip:
                    type: str
                    default: 'disable'
                    description:
                     - 'Compress upload logs.'
                     - 'disable - Upload log files as plain text.'
                     - 'enable - Upload log files compressed.'
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
    - name: send request to /cli/system/locallog/disk/setting
      fmgr_cli_system_locallog_disk_setting:
         method: <value in [set, update]>
         params:
            - 
               data: 
                  diskfull: <value in [overwrite, nolog] default: overwrite>
                  log-disk-full-percentage: <value of integer default: 80>
                  max-log-file-size: <value of integer default: 100>
                  roll-day: 
                   - <value in [sunday, monday, tuesday, ...]>
                  roll-schedule: <value in [none, daily, weekly] default: none>
                  roll-time: 
                   - <value of string>
                  server-type: <value in [FTP, SFTP, SCP] default: FTP>
                  severity: <value in [emergency, alert, critical, ...] default: information>
                  status: <value in [disable, enable] default: enable>
                  upload: <value in [disable, enable] default: disable>
                  upload-delete-files: <value in [disable, enable] default: enable>
                  upload-time: 
                   - <value of string>
                  uploaddir: <value of string>
                  uploadip: <value of string default: 0.0.0.0>
                  uploadpass: 
                   - <value of string default: ENC NDk0NjE4Nzg3MjIwODA3N71+qrz/6PhYvtMUVz84NXNAP8LBSobOqp91xwfif6Oy3+uy8/crasneRp4VbtBQntyLw7E8MbzHoUlJp8Y2cQLnVfVsTQsRfvtq/BZcpTL+c2yDARD0Bvd1khGe4e1mCVFSVuCTSXxm6CmxqPpcGKFfHLyn>
                  uploadport: <value of integer default: 0>
                  uploadsched: <value in [disable, enable] default: disable>
                  uploadtype: 
                   - <value in [event]>
                  uploaduser: <value of string>
                  uploadzip: <value in [disable, enable] default: disable>

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
            diskfull:
               type: str
               description: |
                  'Policy to apply when disk is full.'
                  'overwrite - Overwrite oldest log when disk is full.'
                  'nolog - Stop logging when disk is full.'
               example: overwrite
            log-disk-full-percentage:
               type: int
               description: 'Consider log disk as full at this usage percentage.'
               example: 80
            max-log-file-size:
               type: int
               description: 'Maximum log file size before rolling.'
               example: 100
            roll-day:
               type: array
               suboptions:
                  type: str
            roll-schedule:
               type: str
               description: |
                  'Frequency to check log file for rolling.'
                  'none - Not scheduled.'
                  'daily - Every day.'
                  'weekly - Every week.'
               example: none
            roll-time:
               type: array
               suboptions:
                  type: str
            server-type:
               type: str
               description: |
                  'Server type.'
                  'FTP - Upload via FTP.'
                  'SFTP - Upload via SFTP.'
                  'SCP - Upload via SCP.'
               example: FTP
            severity:
               type: str
               description: |
                  'Least severity level to log.'
                  'emergency - Emergency level.'
                  'alert - Alert level.'
                  'critical - Critical level.'
                  'error - Error level.'
                  'warning - Warning level.'
                  'notification - Notification level.'
                  'information - Information level.'
                  'debug - Debug level.'
               example: information
            status:
               type: str
               description: |
                  'Enable/disable local disk log.'
                  'disable - Do not log to local disk.'
                  'enable - Log to local disk.'
               example: enable
            upload:
               type: str
               description: |
                  'Upload log file when rolling.'
                  'disable - Disable uploading when rolling log file.'
                  'enable - Enable uploading when rolling log file.'
               example: disable
            upload-delete-files:
               type: str
               description: |
                  'Delete log files after uploading (default = enable).'
                  'disable - Do not delete log files after uploading.'
                  'enable - Delete log files after uploading.'
               example: enable
            upload-time:
               type: array
               suboptions:
                  type: str
            uploaddir:
               type: str
               description: 'Log file upload remote directory.'
            uploadip:
               type: str
               description: 'IP address of log uploading server.'
               example: 0.0.0.0
            uploadpass:
               type: array
               suboptions:
                  type: str
                  example: ENC NDk0NjE4Nzg3MjIwODA3N71+qrz/6PhYvtMUVz84NXNAP8LBSobOqp91xwfif6Oy3+uy8/crasneRp4VbtBQntyLw7E8MbzHoUlJp8Y2cQLnVfVsTQsRfvtq/BZcpTL+c2yDARD0Bvd1khGe4e1mCVFSVuCTSXxm6CmxqPpcGKFfHLyn
            uploadport:
               type: int
               description: 'Server port (0 = default protocol port).'
               example: 0
            uploadsched:
               type: str
               description: |
                  'Scheduled upload (disable = upload when rolling).'
                  'disable - Upload when rolling.'
                  'enable - Scheduled upload.'
               example: disable
            uploadtype:
               type: array
               suboptions:
                  type: str
            uploaduser:
               type: str
               description: 'User account in upload server.'
            uploadzip:
               type: str
               description: |
                  'Compress upload logs.'
                  'disable - Upload log files as plain text.'
                  'enable - Upload log files compressed.'
               example: disable
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /cli/global/system/locallog/disk/setting
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
            example: /cli/global/system/locallog/disk/setting

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
        '/cli/global/system/locallog/disk/setting'
    ]

    url_schema = [
    ]

    body_schema =  {
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
                        'diskfull': {
                            'type': 'string',
                            'default': 'overwrite',
                            'enum': [
                                'overwrite',
                                'nolog'
                            ]
                        },
                        'log-disk-full-percentage': {
                            'type': 'integer',
                            'default': 80,
                            'example': 80
                        },
                        'max-log-file-size': {
                            'type': 'integer',
                            'default': 100,
                            'example': 100
                        },
                        'roll-day': {
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
                        'roll-schedule': {
                            'type': 'string',
                            'default': 'none',
                            'enum': [
                                'none',
                                'daily',
                                'weekly'
                            ]
                        },
                        'roll-time': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'server-type': {
                            'type': 'string',
                            'default': 'FTP',
                            'enum': [
                                'FTP',
                                'SFTP',
                                'SCP'
                            ]
                        },
                        'severity': {
                            'type': 'string',
                            'default': 'information',
                            'enum': [
                                'emergency',
                                'alert',
                                'critical',
                                'error',
                                'warning',
                                'notification',
                                'information',
                                'debug'
                            ]
                        },
                        'status': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'upload': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'upload-delete-files': {
                            'type': 'string',
                            'default': 'enable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'upload-time': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'uploaddir': {
                            'type': 'string'
                        },
                        'uploadip': {
                            'type': 'string',
                            'default': '0.0.0.0'
                        },
                        'uploadpass': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'default': 'ENC NDk0NjE4Nzg3MjIwODA3N71+qrz/6PhYvtMUVz84NXNAP8LBSobOqp91xwfif6Oy3+uy8/crasneRp4VbtBQntyLw7E8MbzHoUlJp8Y2cQLnVfVsTQsRfvtq/BZcpTL+c2yDARD0Bvd1khGe4e1mCVFSVuCTSXxm6CmxqPpcGKFfHLyn'
                            }
                        },
                        'uploadport': {
                            'type': 'integer',
                            'default': 0,
                            'example': 0
                        },
                        'uploadsched': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'uploadtype': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'event'
                                ]
                            }
                        },
                        'uploaduser': {
                            'type': 'string'
                        },
                        'uploadzip': {
                            'type': 'string',
                            'default': 'disable',
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