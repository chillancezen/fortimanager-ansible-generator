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
module: fmgr_cli_system_log_settings
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis:
    - /cli/global/system/log/settings
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
    schema_object0:
        methods: [get]
        description: 'Log settings.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Log settings.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                FAC-custom-field1:
                    type: str
                    description: 'Name of custom log field to index.'
                FAZ-custom-field1:
                    type: str
                    description: 'Name of custom log field to index.'
                FCH-custom-field1:
                    type: str
                    description: 'Name of custom log field to index.'
                FCT-custom-field1:
                    type: str
                    description: 'Name of custom log field to index.'
                FDD-custom-field1:
                    type: str
                    description: 'Name of custom log field to index.'
                FGT-custom-field1:
                    type: str
                    description: 'Name of custom log field to index.'
                FMG-custom-field1:
                    type: str
                    description: 'Name of custom log field to index.'
                FML-custom-field1:
                    type: str
                    description: 'Name of custom log field to index.'
                FPX-custom-field1:
                    type: str
                    description: 'Name of custom log field to index.'
                FSA-custom-field1:
                    type: str
                    description: 'Name of custom log field to index.'
                FWB-custom-field1:
                    type: str
                    description: 'Name of custom log field to index.'
                browse-max-logfiles:
                    type: int
                    default: 10000
                    description: 'Maximum number of log files for each log browse attempt for each Adom.'
                dns-resolve-dstip:
                    type: str
                    default: disable
                    description:
                     - 'Enable/Disable resolving destination IP by DNS.'
                     - 'disable - Disable resolving destination IP by DNS.'
                     - 'enable - Enable resolving destination IP by DNS.'
                    choices:
                        - disable
                        - enable
                download-max-logs:
                    type: int
                    default: 500000
                    description: 'Maximum number of logs for each log download attempt.'
                ha-auto-migrate:
                    type: str
                    default: disable
                    description:
                     - 'Enabled/Disable automatically merging HA member's logs to HA cluster.'
                     - 'disable - Disable automatically merging HA member's logs to HA cluster.'
                     - 'enable - Enable automatically merging HA member's logs to HA cluster.'
                    choices:
                        - disable
                        - enable
                import-max-logfiles:
                    type: int
                    default: 10000
                    description: 'Maximum number of log files for each log import attempt.'
                log-file-archive-name:
                    type: str
                    default: basic
                    description:
                     - 'Log file name format for archiving, such as backup, upload or download.'
                     - 'basic - Basic format for log archive file name, e.g. FGT20C0000000001.tlog.1417797247.log.'
                     - 'extended - Extended format for log archive file name, e.g. FGT20C0000000001.2014-12-05-08:34:58.tlog.1417797247.log.'
                    choices:
                        - basic
                        - extended
                rolling-analyzer:
                    days:
                        -
                            type: str
                            choices:
                                - sun
                                - mon
                                - tue
                                - wed
                                - thu
                                - fri
                                - sat
                    del-files:
                        type: str
                        default: disable
                        description:
                         - 'Enable/disable log file deletion after uploading.'
                         - 'disable - Disable log file deletion.'
                         - 'enable - Enable log file deletion.'
                        choices:
                            - disable
                            - enable
                    directory:
                        type: str
                        description: 'Upload server directory, for Unix server, use absolute'
                    file-size:
                        type: int
                        default: 200
                        description: 'Roll log files when they reach this size (MB).'
                    gzip-format:
                        type: str
                        default: disable
                        description:
                         - 'Enable/disable compression of uploaded log files.'
                         - 'disable - Disable compression.'
                         - 'enable - Enable compression.'
                        choices:
                            - disable
                            - enable
                    hour:
                        type: int
                        default: 0
                        description: 'Log files rolling schedule (hour).'
                    ip:
                        type: str
                        default: 0.0.0.0
                        description: 'Upload server IP address.'
                    ip2:
                        type: str
                        default: 0.0.0.0
                        description: 'Upload server IP2 address.'
                    ip3:
                        type: str
                        default: 0.0.0.0
                        description: 'Upload server IP3 address.'
                    log-format:
                        type: str
                        default: native
                        description:
                         - 'Format of uploaded log files.'
                         - 'native - Native format (text or compact).'
                         - 'text - Text format (convert if necessary).'
                         - 'csv - CSV (comma-separated value) format.'
                        choices:
                            - native
                            - text
                            - csv
                    min:
                        type: int
                        default: 0
                        description: 'Log files rolling schedule (minutes).'
                    password:
                        -
                            type: str
                            default: ENC MzQ3NjYyODIxOTc1MTg3NhVVByJnhjVIRIq22N8+MG0by/Mxs5TUnkVnhHtwoRdEVnaNNj6P9rGxNsGaBAn2SVhBLt6V9QWnTm1fbC1hAWycBDzkxK37kTzWEwu5NE66yvC4sVh53l+CSOPZabxA2n7XCNB9Kce1X8EeGUr4PqPCtCej
                    password2:
                        -
                            type: str
                            default: ENC MTAwODg0NTQxNDE5OTQwMaPdJv8JESXhogoJmBIvID8+U03pvD8I9Yr/Q1NGxPnlvLKVEOISmJ/IRPZauTQ/oJ5KlJE3LSzrXEOWAhn2mNaoS+nFbu0seQqMEhUdLbx41Q0yi4dCM9n3PF8RETPiFayOQ5sWWPRD7ALjlthRLogqkua5
                    password3:
                        -
                            type: str
                            default: ENC MTMyOTA3MjY4MTgxMTk2N1UB1GKpBMmb5vgQRJTsjWS9sBfCvYmhBhdgf+ipyNKwY43YcyKBx3TaUcf6QLEdeVgFD2ymJHzfX99dusp8IfxNYj7ITnobzP+GcHYMOyPtjtcORJqwHTpEy9rnqCfy6nKz2Sdj1D1SnqOfRhn0R8sonnED
                    server-type:
                        type: str
                        default: ftp
                        description:
                         - 'Upload server type.'
                         - 'ftp - Upload via FTP.'
                         - 'sftp - Upload via SFTP.'
                         - 'scp - Upload via SCP.'
                        choices:
                            - ftp
                            - sftp
                            - scp
                    upload:
                        type: str
                        default: disable
                        description:
                         - 'Enable/disable log file uploads.'
                         - 'disable - Disable log files uploading.'
                         - 'enable - Enable log files uploading.'
                        choices:
                            - disable
                            - enable
                    upload-hour:
                        type: int
                        default: 0
                        description: 'Log files upload schedule (hour).'
                    upload-mode:
                        type: str
                        default: backup
                        description:
                         - 'Upload mode with multiple servers.'
                         - 'backup - Servers are attempted and used one after the other upon failure to connect.'
                         - 'mirror - All configured servers are attempted and used.'
                        choices:
                            - backup
                            - mirror
                    upload-trigger:
                        type: str
                        default: on-roll
                        description:
                         - 'Event triggering log files upload.'
                         - 'on-roll - Upload log files after they are rolled.'
                         - 'on-schedule - Upload log files daily.'
                        choices:
                            - on-roll
                            - on-schedule
                    username:
                        type: str
                        description: 'Upload server login username.'
                    username2:
                        type: str
                        description: 'Upload server login username2.'
                    username3:
                        type: str
                        description: 'Upload server login username3.'
                    when:
                        type: str
                        default: none
                        description:
                         - 'Roll log files periodically.'
                         - 'none - Do not roll log files periodically.'
                         - 'daily - Roll log files daily.'
                         - 'weekly - Roll log files on certain days of week.'
                        choices:
                            - none
                            - daily
                            - weekly
                rolling-local:
                    days:
                        -
                            type: str
                            choices:
                                - sun
                                - mon
                                - tue
                                - wed
                                - thu
                                - fri
                                - sat
                    del-files:
                        type: str
                        default: disable
                        description:
                         - 'Enable/disable log file deletion after uploading.'
                         - 'disable - Disable log file deletion.'
                         - 'enable - Enable log file deletion.'
                        choices:
                            - disable
                            - enable
                    directory:
                        type: str
                        description: 'Upload server directory, for Unix server, use absolute'
                    file-size:
                        type: int
                        default: 200
                        description: 'Roll log files when they reach this size (MB).'
                    gzip-format:
                        type: str
                        default: disable
                        description:
                         - 'Enable/disable compression of uploaded log files.'
                         - 'disable - Disable compression.'
                         - 'enable - Enable compression.'
                        choices:
                            - disable
                            - enable
                    hour:
                        type: int
                        default: 0
                        description: 'Log files rolling schedule (hour).'
                    ip:
                        type: str
                        default: 0.0.0.0
                        description: 'Upload server IP address.'
                    ip2:
                        type: str
                        default: 0.0.0.0
                        description: 'Upload server IP2 address.'
                    ip3:
                        type: str
                        default: 0.0.0.0
                        description: 'Upload server IP3 address.'
                    log-format:
                        type: str
                        default: native
                        description:
                         - 'Format of uploaded log files.'
                         - 'native - Native format (text or compact).'
                         - 'text - Text format (convert if necessary).'
                         - 'csv - CSV (comma-separated value) format.'
                        choices:
                            - native
                            - text
                            - csv
                    min:
                        type: int
                        default: 0
                        description: 'Log files rolling schedule (minutes).'
                    password:
                        -
                            type: str
                            default: ENC MTA3MjA4MzMzNDU1NjUyNKTuKbF8PktnhHOXsSkxjhxlHjwIE22BP2ak2RRotV+wsRkGD/HamAdeTJyxk8NUM5OZPMpAHhPZssCynPvryOwf6S7Bq6wiH2BSRxNp+JDC+OcO7KbXMy+0JRgHFegouXqd2l9n+MweBcSP4qsn/P2nZEbm
                    password2:
                        -
                            type: str
                            default: ENC NjYyODA3OTExODQ2OTQ0N1452tPlCQK0/AvB5jye7GpFLLpArdcOazRo1BOGPYnKcgz2Iqn/Nt+7ZZereH6gM4nFNmsLipjwaznrIUtA2dAogsuYgiTXfCbK5hwOSXo5AniueUP1/fJcBeU7xnIUqTCWf8OBrStYnmyEHg0QHHzSmvRq
                    password3:
                        -
                            type: str
                            default: ENC Mzk3ODgxMDA2MjU0NzUwNft3N0w+quBucyAJLuI78/qyOQAkHkRQnCPqX7Crikas/93czxOX2okFGGyPN7MhHEFPwsNyxKziYau12Szy5r5kYxSVnovhsE6m4D9uMiOEfqIm+ZM8t8x0vvZiERLvbNCwn8E4nMkDvz09rKXJdDK1lelu
                    server-type:
                        type: str
                        default: ftp
                        description:
                         - 'Upload server type.'
                         - 'ftp - Upload via FTP.'
                         - 'sftp - Upload via SFTP.'
                         - 'scp - Upload via SCP.'
                        choices:
                            - ftp
                            - sftp
                            - scp
                    upload:
                        type: str
                        default: disable
                        description:
                         - 'Enable/disable log file uploads.'
                         - 'disable - Disable log files uploading.'
                         - 'enable - Enable log files uploading.'
                        choices:
                            - disable
                            - enable
                    upload-hour:
                        type: int
                        default: 0
                        description: 'Log files upload schedule (hour).'
                    upload-mode:
                        type: str
                        default: backup
                        description:
                         - 'Upload mode with multiple servers.'
                         - 'backup - Servers are attempted and used one after the other upon failure to connect.'
                         - 'mirror - All configured servers are attempted and used.'
                        choices:
                            - backup
                            - mirror
                    upload-trigger:
                        type: str
                        default: on-roll
                        description:
                         - 'Event triggering log files upload.'
                         - 'on-roll - Upload log files after they are rolled.'
                         - 'on-schedule - Upload log files daily.'
                        choices:
                            - on-roll
                            - on-schedule
                    username:
                        type: str
                        description: 'Upload server login username.'
                    username2:
                        type: str
                        description: 'Upload server login username2.'
                    username3:
                        type: str
                        description: 'Upload server login username3.'
                    when:
                        type: str
                        default: none
                        description:
                         - 'Roll log files periodically.'
                         - 'none - Do not roll log files periodically.'
                         - 'daily - Roll log files daily.'
                         - 'weekly - Roll log files on certain days of week.'
                        choices:
                            - none
                            - daily
                            - weekly
                rolling-regular:
                    days:
                        -
                            type: str
                            choices:
                                - sun
                                - mon
                                - tue
                                - wed
                                - thu
                                - fri
                                - sat
                    del-files:
                        type: str
                        default: disable
                        description:
                         - 'Enable/disable log file deletion after uploading.'
                         - 'disable - Disable log file deletion.'
                         - 'enable - Enable log file deletion.'
                        choices:
                            - disable
                            - enable
                    directory:
                        type: str
                        description: 'Upload server directory, for Unix server, use absolute'
                    file-size:
                        type: int
                        default: 200
                        description: 'Roll log files when they reach this size (MB).'
                    gzip-format:
                        type: str
                        default: disable
                        description:
                         - 'Enable/disable compression of uploaded log files.'
                         - 'disable - Disable compression.'
                         - 'enable - Enable compression.'
                        choices:
                            - disable
                            - enable
                    hour:
                        type: int
                        default: 0
                        description: 'Log files rolling schedule (hour).'
                    ip:
                        type: str
                        default: 0.0.0.0
                        description: 'Upload server IP address.'
                    ip2:
                        type: str
                        default: 0.0.0.0
                        description: 'Upload server IP2 address.'
                    ip3:
                        type: str
                        default: 0.0.0.0
                        description: 'Upload server IP3 address.'
                    log-format:
                        type: str
                        default: native
                        description:
                         - 'Format of uploaded log files.'
                         - 'native - Native format (text or compact).'
                         - 'text - Text format (convert if necessary).'
                         - 'csv - CSV (comma-separated value) format.'
                        choices:
                            - native
                            - text
                            - csv
                    min:
                        type: int
                        default: 0
                        description: 'Log files rolling schedule (minutes).'
                    password:
                        -
                            type: str
                            default: ENC ODAwOTQ3NjUzMDIwNzk1OIPHW/nEK7BO24JYo1Em7rYn7CdH7TdDmHCHkrjwr+SVjdV8BYqBZBky2+zlZseWknPUDVeGjpRxz5S4sOpVJpepIlmEWlA52qtz+8yR98QYwq7x6zet0/xPAsnFJfQ5hkw+glg4dEZe8dYhZqUIpBTG3A1f
                    password2:
                        -
                            type: str
                            default: ENC NDI4MzA1MDAwNDc5MDM1NCgaDuO8BbylW468/v7rkRIUl/sgtzU4EClw6xY77UANoEcktN7+aT2a+gQ1XwPLrlWn+8x5CURG3MmkJULSMu2wqfWLPA7C1rIwlHY7Z22A1SW04YvTiPiKK/LY7OjYalTgHqL33VerBXP7/Sgyn5dlEZnu
                    password3:
                        -
                            type: str
                            default: ENC MTI4Mzk5OTgyODM4NjQ2NbWPjK9Eo8bsyoRiMK1soj62ZQgC0L38apk7ls82V9kbFawm+/xT594RzdZD3WU8luDAAvtCGVOECxVPu4I9owGyeS2ioYrWcqFmjTCrgZrM9D0Vb4UvHpENCMz/qImwFE+ka+Y/f8+c79d9b0unoAUgOi6M
                    server-type:
                        type: str
                        default: ftp
                        description:
                         - 'Upload server type.'
                         - 'ftp - Upload via FTP.'
                         - 'sftp - Upload via SFTP.'
                         - 'scp - Upload via SCP.'
                        choices:
                            - ftp
                            - sftp
                            - scp
                    upload:
                        type: str
                        default: disable
                        description:
                         - 'Enable/disable log file uploads.'
                         - 'disable - Disable log files uploading.'
                         - 'enable - Enable log files uploading.'
                        choices:
                            - disable
                            - enable
                    upload-hour:
                        type: int
                        default: 0
                        description: 'Log files upload schedule (hour).'
                    upload-mode:
                        type: str
                        default: backup
                        description:
                         - 'Upload mode with multiple servers.'
                         - 'backup - Servers are attempted and used one after the other upon failure to connect.'
                         - 'mirror - All configured servers are attempted and used.'
                        choices:
                            - backup
                            - mirror
                    upload-trigger:
                        type: str
                        default: on-roll
                        description:
                         - 'Event triggering log files upload.'
                         - 'on-roll - Upload log files after they are rolled.'
                         - 'on-schedule - Upload log files daily.'
                        choices:
                            - on-roll
                            - on-schedule
                    username:
                        type: str
                        description: 'Upload server login username.'
                    username2:
                        type: str
                        description: 'Upload server login username2.'
                    username3:
                        type: str
                        description: 'Upload server login username3.'
                    when:
                        type: str
                        default: none
                        description:
                         - 'Roll log files periodically.'
                         - 'none - Do not roll log files periodically.'
                         - 'daily - Roll log files daily.'
                         - 'weekly - Roll log files on certain days of week.'
                        choices:
                            - none
                            - daily
                            - weekly
                sync-search-timeout:
                    type: int
                    default: 60
                    description: 'Maximum number of seconds for running a log search session in synchronous mode.'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /cli/system/log/settings
      fmgr_cli_system_log_settings:
         method: <value in [set, update]>
         params:
            - 
               data: 
                  FAC-custom-field1: <value of string>
                  FAZ-custom-field1: <value of string>
                  FCH-custom-field1: <value of string>
                  FCT-custom-field1: <value of string>
                  FDD-custom-field1: <value of string>
                  FGT-custom-field1: <value of string>
                  FMG-custom-field1: <value of string>
                  FML-custom-field1: <value of string>
                  FPX-custom-field1: <value of string>
                  FSA-custom-field1: <value of string>
                  FWB-custom-field1: <value of string>
                  browse-max-logfiles: <value of integer default: 10000>
                  dns-resolve-dstip: <value in [disable, enable] default: disable>
                  download-max-logs: <value of integer default: 500000>
                  ha-auto-migrate: <value in [disable, enable] default: disable>
                  import-max-logfiles: <value of integer default: 10000>
                  log-file-archive-name: <value in [basic, extended] default: basic>
                  rolling-analyzer: 
                     days: 
                      - <value in [sun, mon, tue, ...]>
                     del-files: <value in [disable, enable] default: disable>
                     directory: <value of string>
                     file-size: <value of integer default: 200>
                     gzip-format: <value in [disable, enable] default: disable>
                     hour: <value of integer default: 0>
                     ip: <value of string default: 0.0.0.0>
                     ip2: <value of string default: 0.0.0.0>
                     ip3: <value of string default: 0.0.0.0>
                     log-format: <value in [native, text, csv] default: native>
                     min: <value of integer default: 0>
                     password: 
                      - <value of string default: ENC MzQ3NjYyODIxOTc1MTg3NhVVByJnhjVIRIq22N8+MG0by/Mxs5TUnkVnhHtwoRdEVnaNNj6P9rGxNsGaBAn2SVhBLt6V9QWnTm1fbC1hAWycBDzkxK37kTzWEwu5NE66yvC4sVh53l+CSOPZabxA2n7XCNB9Kce1X8EeGUr4PqPCtCej>
                     password2: 
                      - <value of string default: ENC MTAwODg0NTQxNDE5OTQwMaPdJv8JESXhogoJmBIvID8+U03pvD8I9Yr/Q1NGxPnlvLKVEOISmJ/IRPZauTQ/oJ5KlJE3LSzrXEOWAhn2mNaoS+nFbu0seQqMEhUdLbx41Q0yi4dCM9n3PF8RETPiFayOQ5sWWPRD7ALjlthRLogqkua5>
                     password3: 
                      - <value of string default: ENC MTMyOTA3MjY4MTgxMTk2N1UB1GKpBMmb5vgQRJTsjWS9sBfCvYmhBhdgf+ipyNKwY43YcyKBx3TaUcf6QLEdeVgFD2ymJHzfX99dusp8IfxNYj7ITnobzP+GcHYMOyPtjtcORJqwHTpEy9rnqCfy6nKz2Sdj1D1SnqOfRhn0R8sonnED>
                     server-type: <value in [ftp, sftp, scp] default: ftp>
                     upload: <value in [disable, enable] default: disable>
                     upload-hour: <value of integer default: 0>
                     upload-mode: <value in [backup, mirror] default: backup>
                     upload-trigger: <value in [on-roll, on-schedule] default: on-roll>
                     username: <value of string>
                     username2: <value of string>
                     username3: <value of string>
                     when: <value in [none, daily, weekly] default: none>
                  rolling-local: 
                     days: 
                      - <value in [sun, mon, tue, ...]>
                     del-files: <value in [disable, enable] default: disable>
                     directory: <value of string>
                     file-size: <value of integer default: 200>
                     gzip-format: <value in [disable, enable] default: disable>
                     hour: <value of integer default: 0>
                     ip: <value of string default: 0.0.0.0>
                     ip2: <value of string default: 0.0.0.0>
                     ip3: <value of string default: 0.0.0.0>
                     log-format: <value in [native, text, csv] default: native>
                     min: <value of integer default: 0>
                     password: 
                      - <value of string default: ENC MTA3MjA4MzMzNDU1NjUyNKTuKbF8PktnhHOXsSkxjhxlHjwIE22BP2ak2RRotV+wsRkGD/HamAdeTJyxk8NUM5OZPMpAHhPZssCynPvryOwf6S7Bq6wiH2BSRxNp+JDC+OcO7KbXMy+0JRgHFegouXqd2l9n+MweBcSP4qsn/P2nZEbm>
                     password2: 
                      - <value of string default: ENC NjYyODA3OTExODQ2OTQ0N1452tPlCQK0/AvB5jye7GpFLLpArdcOazRo1BOGPYnKcgz2Iqn/Nt+7ZZereH6gM4nFNmsLipjwaznrIUtA2dAogsuYgiTXfCbK5hwOSXo5AniueUP1/fJcBeU7xnIUqTCWf8OBrStYnmyEHg0QHHzSmvRq>
                     password3: 
                      - <value of string default: ENC Mzk3ODgxMDA2MjU0NzUwNft3N0w+quBucyAJLuI78/qyOQAkHkRQnCPqX7Crikas/93czxOX2okFGGyPN7MhHEFPwsNyxKziYau12Szy5r5kYxSVnovhsE6m4D9uMiOEfqIm+ZM8t8x0vvZiERLvbNCwn8E4nMkDvz09rKXJdDK1lelu>
                     server-type: <value in [ftp, sftp, scp] default: ftp>
                     upload: <value in [disable, enable] default: disable>
                     upload-hour: <value of integer default: 0>
                     upload-mode: <value in [backup, mirror] default: backup>
                     upload-trigger: <value in [on-roll, on-schedule] default: on-roll>
                     username: <value of string>
                     username2: <value of string>
                     username3: <value of string>
                     when: <value in [none, daily, weekly] default: none>
                  rolling-regular: 
                     days: 
                      - <value in [sun, mon, tue, ...]>
                     del-files: <value in [disable, enable] default: disable>
                     directory: <value of string>
                     file-size: <value of integer default: 200>
                     gzip-format: <value in [disable, enable] default: disable>
                     hour: <value of integer default: 0>
                     ip: <value of string default: 0.0.0.0>
                     ip2: <value of string default: 0.0.0.0>
                     ip3: <value of string default: 0.0.0.0>
                     log-format: <value in [native, text, csv] default: native>
                     min: <value of integer default: 0>
                     password: 
                      - <value of string default: ENC ODAwOTQ3NjUzMDIwNzk1OIPHW/nEK7BO24JYo1Em7rYn7CdH7TdDmHCHkrjwr+SVjdV8BYqBZBky2+zlZseWknPUDVeGjpRxz5S4sOpVJpepIlmEWlA52qtz+8yR98QYwq7x6zet0/xPAsnFJfQ5hkw+glg4dEZe8dYhZqUIpBTG3A1f>
                     password2: 
                      - <value of string default: ENC NDI4MzA1MDAwNDc5MDM1NCgaDuO8BbylW468/v7rkRIUl/sgtzU4EClw6xY77UANoEcktN7+aT2a+gQ1XwPLrlWn+8x5CURG3MmkJULSMu2wqfWLPA7C1rIwlHY7Z22A1SW04YvTiPiKK/LY7OjYalTgHqL33VerBXP7/Sgyn5dlEZnu>
                     password3: 
                      - <value of string default: ENC MTI4Mzk5OTgyODM4NjQ2NbWPjK9Eo8bsyoRiMK1soj62ZQgC0L38apk7ls82V9kbFawm+/xT594RzdZD3WU8luDAAvtCGVOECxVPu4I9owGyeS2ioYrWcqFmjTCrgZrM9D0Vb4UvHpENCMz/qImwFE+ka+Y/f8+c79d9b0unoAUgOi6M>
                     server-type: <value in [ftp, sftp, scp] default: ftp>
                     upload: <value in [disable, enable] default: disable>
                     upload-hour: <value of integer default: 0>
                     upload-mode: <value in [backup, mirror] default: backup>
                     upload-trigger: <value in [on-roll, on-schedule] default: on-roll>
                     username: <value of string>
                     username2: <value of string>
                     username3: <value of string>
                     when: <value in [none, daily, weekly] default: none>
                  sync-search-timeout: <value of integer default: 60>

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
            FAC-custom-field1:
               type: str
               description: 'Name of custom log field to index.'
            FAZ-custom-field1:
               type: str
               description: 'Name of custom log field to index.'
            FCH-custom-field1:
               type: str
               description: 'Name of custom log field to index.'
            FCT-custom-field1:
               type: str
               description: 'Name of custom log field to index.'
            FDD-custom-field1:
               type: str
               description: 'Name of custom log field to index.'
            FGT-custom-field1:
               type: str
               description: 'Name of custom log field to index.'
            FMG-custom-field1:
               type: str
               description: 'Name of custom log field to index.'
            FML-custom-field1:
               type: str
               description: 'Name of custom log field to index.'
            FPX-custom-field1:
               type: str
               description: 'Name of custom log field to index.'
            FSA-custom-field1:
               type: str
               description: 'Name of custom log field to index.'
            FWB-custom-field1:
               type: str
               description: 'Name of custom log field to index.'
            browse-max-logfiles:
               type: int
               description: 'Maximum number of log files for each log browse attempt for each Adom.'
               example: 10000
            dns-resolve-dstip:
               type: str
               description: |
                  'Enable/Disable resolving destination IP by DNS.'
                  'disable - Disable resolving destination IP by DNS.'
                  'enable - Enable resolving destination IP by DNS.'
               example: disable
            download-max-logs:
               type: int
               description: 'Maximum number of logs for each log download attempt.'
               example: 500000
            ha-auto-migrate:
               type: str
               description: |
                  'Enabled/Disable automatically merging HA member's logs to HA cluster.'
                  'disable - Disable automatically merging HA member's logs to HA cluster.'
                  'enable - Enable automatically merging HA member's logs to HA cluster.'
               example: disable
            import-max-logfiles:
               type: int
               description: 'Maximum number of log files for each log import attempt.'
               example: 10000
            log-file-archive-name:
               type: str
               description: |
                  'Log file name format for archiving, such as backup, upload or download.'
                  'basic - Basic format for log archive file name, e.g. FGT20C0000000001.tlog.1417797247.log.'
                  'extended - Extended format for log archive file name, e.g. FGT20C0000000001.2014-12-05-08:34:58.tlog.1417797247.log.'
               example: basic
            rolling-analyzer:
               days:
                  type: array
                  suboptions:
                     type: str
               del-files:
                  type: str
                  description: |
                     'Enable/disable log file deletion after uploading.'
                     'disable - Disable log file deletion.'
                     'enable - Enable log file deletion.'
                  example: disable
               directory:
                  type: str
                  description: 'Upload server directory, for Unix server, use absolute'
               file-size:
                  type: int
                  description: 'Roll log files when they reach this size (MB).'
                  example: 200
               gzip-format:
                  type: str
                  description: |
                     'Enable/disable compression of uploaded log files.'
                     'disable - Disable compression.'
                     'enable - Enable compression.'
                  example: disable
               hour:
                  type: int
                  description: 'Log files rolling schedule (hour).'
                  example: 0
               ip:
                  type: str
                  description: 'Upload server IP address.'
                  example: 0.0.0.0
               ip2:
                  type: str
                  description: 'Upload server IP2 address.'
                  example: 0.0.0.0
               ip3:
                  type: str
                  description: 'Upload server IP3 address.'
                  example: 0.0.0.0
               log-format:
                  type: str
                  description: |
                     'Format of uploaded log files.'
                     'native - Native format (text or compact).'
                     'text - Text format (convert if necessary).'
                     'csv - CSV (comma-separated value) format.'
                  example: native
               min:
                  type: int
                  description: 'Log files rolling schedule (minutes).'
                  example: 0
               password:
                  type: array
                  suboptions:
                     type: str
                     example: ENC MzQ3NjYyODIxOTc1MTg3NhVVByJnhjVIRIq22N8+MG0by/Mxs5TUnkVnhHtwoRdEVnaNNj6P9rGxNsGaBAn2SVhBLt6V9QWnTm1fbC1hAWycBDzkxK37kTzWEwu5NE66yvC4sVh53l+CSOPZabxA2n7XCNB9Kce1X8EeGUr4PqPCtCej
               password2:
                  type: array
                  suboptions:
                     type: str
                     example: ENC MTAwODg0NTQxNDE5OTQwMaPdJv8JESXhogoJmBIvID8+U03pvD8I9Yr/Q1NGxPnlvLKVEOISmJ/IRPZauTQ/oJ5KlJE3LSzrXEOWAhn2mNaoS+nFbu0seQqMEhUdLbx41Q0yi4dCM9n3PF8RETPiFayOQ5sWWPRD7ALjlthRLogqkua5
               password3:
                  type: array
                  suboptions:
                     type: str
                     example: ENC MTMyOTA3MjY4MTgxMTk2N1UB1GKpBMmb5vgQRJTsjWS9sBfCvYmhBhdgf+ipyNKwY43YcyKBx3TaUcf6QLEdeVgFD2ymJHzfX99dusp8IfxNYj7ITnobzP+GcHYMOyPtjtcORJqwHTpEy9rnqCfy6nKz2Sdj1D1SnqOfRhn0R8sonnED
               server-type:
                  type: str
                  description: |
                     'Upload server type.'
                     'ftp - Upload via FTP.'
                     'sftp - Upload via SFTP.'
                     'scp - Upload via SCP.'
                  example: ftp
               upload:
                  type: str
                  description: |
                     'Enable/disable log file uploads.'
                     'disable - Disable log files uploading.'
                     'enable - Enable log files uploading.'
                  example: disable
               upload-hour:
                  type: int
                  description: 'Log files upload schedule (hour).'
                  example: 0
               upload-mode:
                  type: str
                  description: |
                     'Upload mode with multiple servers.'
                     'backup - Servers are attempted and used one after the other upon failure to connect.'
                     'mirror - All configured servers are attempted and used.'
                  example: backup
               upload-trigger:
                  type: str
                  description: |
                     'Event triggering log files upload.'
                     'on-roll - Upload log files after they are rolled.'
                     'on-schedule - Upload log files daily.'
                  example: on-roll
               username:
                  type: str
                  description: 'Upload server login username.'
               username2:
                  type: str
                  description: 'Upload server login username2.'
               username3:
                  type: str
                  description: 'Upload server login username3.'
               when:
                  type: str
                  description: |
                     'Roll log files periodically.'
                     'none - Do not roll log files periodically.'
                     'daily - Roll log files daily.'
                     'weekly - Roll log files on certain days of week.'
                  example: none
            rolling-local:
               days:
                  type: array
                  suboptions:
                     type: str
               del-files:
                  type: str
                  description: |
                     'Enable/disable log file deletion after uploading.'
                     'disable - Disable log file deletion.'
                     'enable - Enable log file deletion.'
                  example: disable
               directory:
                  type: str
                  description: 'Upload server directory, for Unix server, use absolute'
               file-size:
                  type: int
                  description: 'Roll log files when they reach this size (MB).'
                  example: 200
               gzip-format:
                  type: str
                  description: |
                     'Enable/disable compression of uploaded log files.'
                     'disable - Disable compression.'
                     'enable - Enable compression.'
                  example: disable
               hour:
                  type: int
                  description: 'Log files rolling schedule (hour).'
                  example: 0
               ip:
                  type: str
                  description: 'Upload server IP address.'
                  example: 0.0.0.0
               ip2:
                  type: str
                  description: 'Upload server IP2 address.'
                  example: 0.0.0.0
               ip3:
                  type: str
                  description: 'Upload server IP3 address.'
                  example: 0.0.0.0
               log-format:
                  type: str
                  description: |
                     'Format of uploaded log files.'
                     'native - Native format (text or compact).'
                     'text - Text format (convert if necessary).'
                     'csv - CSV (comma-separated value) format.'
                  example: native
               min:
                  type: int
                  description: 'Log files rolling schedule (minutes).'
                  example: 0
               password:
                  type: array
                  suboptions:
                     type: str
                     example: ENC MTA3MjA4MzMzNDU1NjUyNKTuKbF8PktnhHOXsSkxjhxlHjwIE22BP2ak2RRotV+wsRkGD/HamAdeTJyxk8NUM5OZPMpAHhPZssCynPvryOwf6S7Bq6wiH2BSRxNp+JDC+OcO7KbXMy+0JRgHFegouXqd2l9n+MweBcSP4qsn/P2nZEbm
               password2:
                  type: array
                  suboptions:
                     type: str
                     example: ENC NjYyODA3OTExODQ2OTQ0N1452tPlCQK0/AvB5jye7GpFLLpArdcOazRo1BOGPYnKcgz2Iqn/Nt+7ZZereH6gM4nFNmsLipjwaznrIUtA2dAogsuYgiTXfCbK5hwOSXo5AniueUP1/fJcBeU7xnIUqTCWf8OBrStYnmyEHg0QHHzSmvRq
               password3:
                  type: array
                  suboptions:
                     type: str
                     example: ENC Mzk3ODgxMDA2MjU0NzUwNft3N0w+quBucyAJLuI78/qyOQAkHkRQnCPqX7Crikas/93czxOX2okFGGyPN7MhHEFPwsNyxKziYau12Szy5r5kYxSVnovhsE6m4D9uMiOEfqIm+ZM8t8x0vvZiERLvbNCwn8E4nMkDvz09rKXJdDK1lelu
               server-type:
                  type: str
                  description: |
                     'Upload server type.'
                     'ftp - Upload via FTP.'
                     'sftp - Upload via SFTP.'
                     'scp - Upload via SCP.'
                  example: ftp
               upload:
                  type: str
                  description: |
                     'Enable/disable log file uploads.'
                     'disable - Disable log files uploading.'
                     'enable - Enable log files uploading.'
                  example: disable
               upload-hour:
                  type: int
                  description: 'Log files upload schedule (hour).'
                  example: 0
               upload-mode:
                  type: str
                  description: |
                     'Upload mode with multiple servers.'
                     'backup - Servers are attempted and used one after the other upon failure to connect.'
                     'mirror - All configured servers are attempted and used.'
                  example: backup
               upload-trigger:
                  type: str
                  description: |
                     'Event triggering log files upload.'
                     'on-roll - Upload log files after they are rolled.'
                     'on-schedule - Upload log files daily.'
                  example: on-roll
               username:
                  type: str
                  description: 'Upload server login username.'
               username2:
                  type: str
                  description: 'Upload server login username2.'
               username3:
                  type: str
                  description: 'Upload server login username3.'
               when:
                  type: str
                  description: |
                     'Roll log files periodically.'
                     'none - Do not roll log files periodically.'
                     'daily - Roll log files daily.'
                     'weekly - Roll log files on certain days of week.'
                  example: none
            rolling-regular:
               days:
                  type: array
                  suboptions:
                     type: str
               del-files:
                  type: str
                  description: |
                     'Enable/disable log file deletion after uploading.'
                     'disable - Disable log file deletion.'
                     'enable - Enable log file deletion.'
                  example: disable
               directory:
                  type: str
                  description: 'Upload server directory, for Unix server, use absolute'
               file-size:
                  type: int
                  description: 'Roll log files when they reach this size (MB).'
                  example: 200
               gzip-format:
                  type: str
                  description: |
                     'Enable/disable compression of uploaded log files.'
                     'disable - Disable compression.'
                     'enable - Enable compression.'
                  example: disable
               hour:
                  type: int
                  description: 'Log files rolling schedule (hour).'
                  example: 0
               ip:
                  type: str
                  description: 'Upload server IP address.'
                  example: 0.0.0.0
               ip2:
                  type: str
                  description: 'Upload server IP2 address.'
                  example: 0.0.0.0
               ip3:
                  type: str
                  description: 'Upload server IP3 address.'
                  example: 0.0.0.0
               log-format:
                  type: str
                  description: |
                     'Format of uploaded log files.'
                     'native - Native format (text or compact).'
                     'text - Text format (convert if necessary).'
                     'csv - CSV (comma-separated value) format.'
                  example: native
               min:
                  type: int
                  description: 'Log files rolling schedule (minutes).'
                  example: 0
               password:
                  type: array
                  suboptions:
                     type: str
                     example: ENC ODAwOTQ3NjUzMDIwNzk1OIPHW/nEK7BO24JYo1Em7rYn7CdH7TdDmHCHkrjwr+SVjdV8BYqBZBky2+zlZseWknPUDVeGjpRxz5S4sOpVJpepIlmEWlA52qtz+8yR98QYwq7x6zet0/xPAsnFJfQ5hkw+glg4dEZe8dYhZqUIpBTG3A1f
               password2:
                  type: array
                  suboptions:
                     type: str
                     example: ENC NDI4MzA1MDAwNDc5MDM1NCgaDuO8BbylW468/v7rkRIUl/sgtzU4EClw6xY77UANoEcktN7+aT2a+gQ1XwPLrlWn+8x5CURG3MmkJULSMu2wqfWLPA7C1rIwlHY7Z22A1SW04YvTiPiKK/LY7OjYalTgHqL33VerBXP7/Sgyn5dlEZnu
               password3:
                  type: array
                  suboptions:
                     type: str
                     example: ENC MTI4Mzk5OTgyODM4NjQ2NbWPjK9Eo8bsyoRiMK1soj62ZQgC0L38apk7ls82V9kbFawm+/xT594RzdZD3WU8luDAAvtCGVOECxVPu4I9owGyeS2ioYrWcqFmjTCrgZrM9D0Vb4UvHpENCMz/qImwFE+ka+Y/f8+c79d9b0unoAUgOi6M
               server-type:
                  type: str
                  description: |
                     'Upload server type.'
                     'ftp - Upload via FTP.'
                     'sftp - Upload via SFTP.'
                     'scp - Upload via SCP.'
                  example: ftp
               upload:
                  type: str
                  description: |
                     'Enable/disable log file uploads.'
                     'disable - Disable log files uploading.'
                     'enable - Enable log files uploading.'
                  example: disable
               upload-hour:
                  type: int
                  description: 'Log files upload schedule (hour).'
                  example: 0
               upload-mode:
                  type: str
                  description: |
                     'Upload mode with multiple servers.'
                     'backup - Servers are attempted and used one after the other upon failure to connect.'
                     'mirror - All configured servers are attempted and used.'
                  example: backup
               upload-trigger:
                  type: str
                  description: |
                     'Event triggering log files upload.'
                     'on-roll - Upload log files after they are rolled.'
                     'on-schedule - Upload log files daily.'
                  example: on-roll
               username:
                  type: str
                  description: 'Upload server login username.'
               username2:
                  type: str
                  description: 'Upload server login username2.'
               username3:
                  type: str
                  description: 'Upload server login username3.'
               when:
                  type: str
                  description: |
                     'Roll log files periodically.'
                     'none - Do not roll log files periodically.'
                     'daily - Roll log files daily.'
                     'weekly - Roll log files on certain days of week.'
                  example: none
            sync-search-timeout:
               type: int
               description: 'Maximum number of seconds for running a log search session in synchronous mode.'
               example: 60
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /cli/global/system/log/settings
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
            example: /cli/global/system/log/settings

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
        '/cli/global/system/log/settings'
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
                        'FAC-custom-field1': {
                            'type': 'string'
                        },
                        'FAZ-custom-field1': {
                            'type': 'string'
                        },
                        'FCH-custom-field1': {
                            'type': 'string'
                        },
                        'FCT-custom-field1': {
                            'type': 'string'
                        },
                        'FDD-custom-field1': {
                            'type': 'string'
                        },
                        'FGT-custom-field1': {
                            'type': 'string'
                        },
                        'FMG-custom-field1': {
                            'type': 'string'
                        },
                        'FML-custom-field1': {
                            'type': 'string'
                        },
                        'FPX-custom-field1': {
                            'type': 'string'
                        },
                        'FSA-custom-field1': {
                            'type': 'string'
                        },
                        'FWB-custom-field1': {
                            'type': 'string'
                        },
                        'browse-max-logfiles': {
                            'type': 'integer',
                            'default': 10000,
                            'example': 10000
                        },
                        'dns-resolve-dstip': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'download-max-logs': {
                            'type': 'integer',
                            'default': 500000,
                            'example': 500000
                        },
                        'ha-auto-migrate': {
                            'type': 'string',
                            'default': 'disable',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'import-max-logfiles': {
                            'type': 'integer',
                            'default': 10000,
                            'example': 10000
                        },
                        'log-file-archive-name': {
                            'type': 'string',
                            'default': 'basic',
                            'enum': [
                                'basic',
                                'extended'
                            ]
                        },
                        'rolling-analyzer': {
                            'days': {
                                'type': 'array',
                                'items': {
                                    'type': 'string',
                                    'enum': [
                                        'sun',
                                        'mon',
                                        'tue',
                                        'wed',
                                        'thu',
                                        'fri',
                                        'sat'
                                    ]
                                }
                            },
                            'del-files': {
                                'type': 'string',
                                'default': 'disable',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'directory': {
                                'type': 'string'
                            },
                            'file-size': {
                                'type': 'integer',
                                'default': 200,
                                'example': 200
                            },
                            'gzip-format': {
                                'type': 'string',
                                'default': 'disable',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'hour': {
                                'type': 'integer',
                                'default': 0,
                                'example': 0
                            },
                            'ip': {
                                'type': 'string',
                                'default': '0.0.0.0'
                            },
                            'ip2': {
                                'type': 'string',
                                'default': '0.0.0.0'
                            },
                            'ip3': {
                                'type': 'string',
                                'default': '0.0.0.0'
                            },
                            'log-format': {
                                'type': 'string',
                                'default': 'native',
                                'enum': [
                                    'native',
                                    'text',
                                    'csv'
                                ]
                            },
                            'min': {
                                'type': 'integer',
                                'default': 0,
                                'example': 0
                            },
                            'password': {
                                'type': 'array',
                                'items': {
                                    'type': 'string',
                                    'default': 'ENC MzQ3NjYyODIxOTc1MTg3NhVVByJnhjVIRIq22N8+MG0by/Mxs5TUnkVnhHtwoRdEVnaNNj6P9rGxNsGaBAn2SVhBLt6V9QWnTm1fbC1hAWycBDzkxK37kTzWEwu5NE66yvC4sVh53l+CSOPZabxA2n7XCNB9Kce1X8EeGUr4PqPCtCej'
                                }
                            },
                            'password2': {
                                'type': 'array',
                                'items': {
                                    'type': 'string',
                                    'default': 'ENC MTAwODg0NTQxNDE5OTQwMaPdJv8JESXhogoJmBIvID8+U03pvD8I9Yr/Q1NGxPnlvLKVEOISmJ/IRPZauTQ/oJ5KlJE3LSzrXEOWAhn2mNaoS+nFbu0seQqMEhUdLbx41Q0yi4dCM9n3PF8RETPiFayOQ5sWWPRD7ALjlthRLogqkua5'
                                }
                            },
                            'password3': {
                                'type': 'array',
                                'items': {
                                    'type': 'string',
                                    'default': 'ENC MTMyOTA3MjY4MTgxMTk2N1UB1GKpBMmb5vgQRJTsjWS9sBfCvYmhBhdgf+ipyNKwY43YcyKBx3TaUcf6QLEdeVgFD2ymJHzfX99dusp8IfxNYj7ITnobzP+GcHYMOyPtjtcORJqwHTpEy9rnqCfy6nKz2Sdj1D1SnqOfRhn0R8sonnED'
                                }
                            },
                            'server-type': {
                                'type': 'string',
                                'default': 'ftp',
                                'enum': [
                                    'ftp',
                                    'sftp',
                                    'scp'
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
                            'upload-hour': {
                                'type': 'integer',
                                'default': 0,
                                'example': 0
                            },
                            'upload-mode': {
                                'type': 'string',
                                'default': 'backup',
                                'enum': [
                                    'backup',
                                    'mirror'
                                ]
                            },
                            'upload-trigger': {
                                'type': 'string',
                                'default': 'on-roll',
                                'enum': [
                                    'on-roll',
                                    'on-schedule'
                                ]
                            },
                            'username': {
                                'type': 'string'
                            },
                            'username2': {
                                'type': 'string'
                            },
                            'username3': {
                                'type': 'string'
                            },
                            'when': {
                                'type': 'string',
                                'default': 'none',
                                'enum': [
                                    'none',
                                    'daily',
                                    'weekly'
                                ]
                            }
                        },
                        'rolling-local': {
                            'days': {
                                'type': 'array',
                                'items': {
                                    'type': 'string',
                                    'enum': [
                                        'sun',
                                        'mon',
                                        'tue',
                                        'wed',
                                        'thu',
                                        'fri',
                                        'sat'
                                    ]
                                }
                            },
                            'del-files': {
                                'type': 'string',
                                'default': 'disable',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'directory': {
                                'type': 'string'
                            },
                            'file-size': {
                                'type': 'integer',
                                'default': 200,
                                'example': 200
                            },
                            'gzip-format': {
                                'type': 'string',
                                'default': 'disable',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'hour': {
                                'type': 'integer',
                                'default': 0,
                                'example': 0
                            },
                            'ip': {
                                'type': 'string',
                                'default': '0.0.0.0'
                            },
                            'ip2': {
                                'type': 'string',
                                'default': '0.0.0.0'
                            },
                            'ip3': {
                                'type': 'string',
                                'default': '0.0.0.0'
                            },
                            'log-format': {
                                'type': 'string',
                                'default': 'native',
                                'enum': [
                                    'native',
                                    'text',
                                    'csv'
                                ]
                            },
                            'min': {
                                'type': 'integer',
                                'default': 0,
                                'example': 0
                            },
                            'password': {
                                'type': 'array',
                                'items': {
                                    'type': 'string',
                                    'default': 'ENC MTA3MjA4MzMzNDU1NjUyNKTuKbF8PktnhHOXsSkxjhxlHjwIE22BP2ak2RRotV+wsRkGD/HamAdeTJyxk8NUM5OZPMpAHhPZssCynPvryOwf6S7Bq6wiH2BSRxNp+JDC+OcO7KbXMy+0JRgHFegouXqd2l9n+MweBcSP4qsn/P2nZEbm'
                                }
                            },
                            'password2': {
                                'type': 'array',
                                'items': {
                                    'type': 'string',
                                    'default': 'ENC NjYyODA3OTExODQ2OTQ0N1452tPlCQK0/AvB5jye7GpFLLpArdcOazRo1BOGPYnKcgz2Iqn/Nt+7ZZereH6gM4nFNmsLipjwaznrIUtA2dAogsuYgiTXfCbK5hwOSXo5AniueUP1/fJcBeU7xnIUqTCWf8OBrStYnmyEHg0QHHzSmvRq'
                                }
                            },
                            'password3': {
                                'type': 'array',
                                'items': {
                                    'type': 'string',
                                    'default': 'ENC Mzk3ODgxMDA2MjU0NzUwNft3N0w+quBucyAJLuI78/qyOQAkHkRQnCPqX7Crikas/93czxOX2okFGGyPN7MhHEFPwsNyxKziYau12Szy5r5kYxSVnovhsE6m4D9uMiOEfqIm+ZM8t8x0vvZiERLvbNCwn8E4nMkDvz09rKXJdDK1lelu'
                                }
                            },
                            'server-type': {
                                'type': 'string',
                                'default': 'ftp',
                                'enum': [
                                    'ftp',
                                    'sftp',
                                    'scp'
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
                            'upload-hour': {
                                'type': 'integer',
                                'default': 0,
                                'example': 0
                            },
                            'upload-mode': {
                                'type': 'string',
                                'default': 'backup',
                                'enum': [
                                    'backup',
                                    'mirror'
                                ]
                            },
                            'upload-trigger': {
                                'type': 'string',
                                'default': 'on-roll',
                                'enum': [
                                    'on-roll',
                                    'on-schedule'
                                ]
                            },
                            'username': {
                                'type': 'string'
                            },
                            'username2': {
                                'type': 'string'
                            },
                            'username3': {
                                'type': 'string'
                            },
                            'when': {
                                'type': 'string',
                                'default': 'none',
                                'enum': [
                                    'none',
                                    'daily',
                                    'weekly'
                                ]
                            }
                        },
                        'rolling-regular': {
                            'days': {
                                'type': 'array',
                                'items': {
                                    'type': 'string',
                                    'enum': [
                                        'sun',
                                        'mon',
                                        'tue',
                                        'wed',
                                        'thu',
                                        'fri',
                                        'sat'
                                    ]
                                }
                            },
                            'del-files': {
                                'type': 'string',
                                'default': 'disable',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'directory': {
                                'type': 'string'
                            },
                            'file-size': {
                                'type': 'integer',
                                'default': 200,
                                'example': 200
                            },
                            'gzip-format': {
                                'type': 'string',
                                'default': 'disable',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'hour': {
                                'type': 'integer',
                                'default': 0,
                                'example': 0
                            },
                            'ip': {
                                'type': 'string',
                                'default': '0.0.0.0'
                            },
                            'ip2': {
                                'type': 'string',
                                'default': '0.0.0.0'
                            },
                            'ip3': {
                                'type': 'string',
                                'default': '0.0.0.0'
                            },
                            'log-format': {
                                'type': 'string',
                                'default': 'native',
                                'enum': [
                                    'native',
                                    'text',
                                    'csv'
                                ]
                            },
                            'min': {
                                'type': 'integer',
                                'default': 0,
                                'example': 0
                            },
                            'password': {
                                'type': 'array',
                                'items': {
                                    'type': 'string',
                                    'default': 'ENC ODAwOTQ3NjUzMDIwNzk1OIPHW/nEK7BO24JYo1Em7rYn7CdH7TdDmHCHkrjwr+SVjdV8BYqBZBky2+zlZseWknPUDVeGjpRxz5S4sOpVJpepIlmEWlA52qtz+8yR98QYwq7x6zet0/xPAsnFJfQ5hkw+glg4dEZe8dYhZqUIpBTG3A1f'
                                }
                            },
                            'password2': {
                                'type': 'array',
                                'items': {
                                    'type': 'string',
                                    'default': 'ENC NDI4MzA1MDAwNDc5MDM1NCgaDuO8BbylW468/v7rkRIUl/sgtzU4EClw6xY77UANoEcktN7+aT2a+gQ1XwPLrlWn+8x5CURG3MmkJULSMu2wqfWLPA7C1rIwlHY7Z22A1SW04YvTiPiKK/LY7OjYalTgHqL33VerBXP7/Sgyn5dlEZnu'
                                }
                            },
                            'password3': {
                                'type': 'array',
                                'items': {
                                    'type': 'string',
                                    'default': 'ENC MTI4Mzk5OTgyODM4NjQ2NbWPjK9Eo8bsyoRiMK1soj62ZQgC0L38apk7ls82V9kbFawm+/xT594RzdZD3WU8luDAAvtCGVOECxVPu4I9owGyeS2ioYrWcqFmjTCrgZrM9D0Vb4UvHpENCMz/qImwFE+ka+Y/f8+c79d9b0unoAUgOi6M'
                                }
                            },
                            'server-type': {
                                'type': 'string',
                                'default': 'ftp',
                                'enum': [
                                    'ftp',
                                    'sftp',
                                    'scp'
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
                            'upload-hour': {
                                'type': 'integer',
                                'default': 0,
                                'example': 0
                            },
                            'upload-mode': {
                                'type': 'string',
                                'default': 'backup',
                                'enum': [
                                    'backup',
                                    'mirror'
                                ]
                            },
                            'upload-trigger': {
                                'type': 'string',
                                'default': 'on-roll',
                                'enum': [
                                    'on-roll',
                                    'on-schedule'
                                ]
                            },
                            'username': {
                                'type': 'string'
                            },
                            'username2': {
                                'type': 'string'
                            },
                            'username3': {
                                'type': 'string'
                            },
                            'when': {
                                'type': 'string',
                                'default': 'none',
                                'enum': [
                                    'none',
                                    'daily',
                                    'weekly'
                                ]
                            }
                        },
                        'sync-search-timeout': {
                            'type': 'integer',
                            'default': 60,
                            'example': 60
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