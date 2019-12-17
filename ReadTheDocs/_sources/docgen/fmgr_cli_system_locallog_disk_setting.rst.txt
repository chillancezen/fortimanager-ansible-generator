:source: fmgr_cli_system_locallog_disk_setting.py

:orphan:

.. _fmgr_cli_system_locallog_disk_setting:

fmgr_cli_system_locallog_disk_setting -- Settings for local disk logging.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/locallog/disk/setting`
- Examples include all parameters and values need to be adjusted to data sources before usage.
- Tested with FortiManager v6.0.0


Requirements
------------
The below requirements are needed on the host that executes this module.

- ansible>=2.10.0



Parameters
----------

.. raw:: html

 <ul>
 <li><span class="li-head">parameters for method: [get]</span> - Settings for local disk logging.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Settings for local disk logging.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">diskfull</span> - Policy to apply when disk is full. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [overwrite, nolog]</span>  <span class="li-normal">default: overwrite</span> </li>
 <li><span class="li-head">log-disk-full-percentage</span> - Consider log disk as full at this usage percentage. <span class="li-normal">type: int</span>  <span class="li-normal">default: 80</span> </li>
 <li><span class="li-head">max-log-file-size</span> - Maximum log file size before rolling. <span class="li-normal">type: int</span>  <span class="li-normal">default: 100</span> </li>
 <li><span class="li-head">roll-day</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sunday, monday, tuesday, wednesday, thursday, friday, saturday]</span> </li>
 </ul>
 <li><span class="li-head">roll-schedule</span> - Frequency to check log file for rolling. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, daily, weekly]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">roll-time</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">server-type</span> - Server type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [FTP, SFTP, SCP]</span>  <span class="li-normal">default: FTP</span> </li>
 <li><span class="li-head">severity</span> - Least severity level to log. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [emergency, alert, critical, error, warning, notification, information, debug]</span>  <span class="li-normal">default: information</span> </li>
 <li><span class="li-head">status</span> - Enable/disable local disk log. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">upload</span> - Upload log file when rolling. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">upload-delete-files</span> - Delete log files after uploading (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">upload-time</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">uploaddir</span> - Log file upload remote directory. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">uploadip</span> - IP address of log uploading server. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">uploadpass</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC NDk0NjE4Nzg3MjIwODA3N71+qrz/6PhYvtMUVz84NXNAP8LBSobOqp91xwfif6Oy3+uy8/crasneRp4VbtBQntyLw7E8MbzHoUlJp8Y2cQLnVfVsTQsRfvtq/BZcpTL+c2yDARD0Bvd1khGe4e1mCVFSVuCTSXxm6CmxqPpcGKFfHLyn</span> </li>
 </ul>
 <li><span class="li-head">uploadport</span> - Server port (0 = default protocol port). <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">uploadsched</span> - Scheduled upload (disable = upload when rolling). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">uploadtype</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [event]</span> </li>
 </ul>
 <li><span class="li-head">uploaduser</span> - User account in upload server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">uploadzip</span> - Compress upload logs. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 </ul>
 </ul>
 </ul>






Notes
-----
.. note::

   - The module may supports multiple method, every method has different parameters definition

   - One method may also have more than one parameter definition collection, each collection is dedicated to one API endpoint

   - The module may include domain dependent urls, the domain can be specified in url_params as adom

Examples
--------

.. code-block:: yaml+jinja

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



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> diskfull </span> - Policy to apply when disk is full. <span class="li-normal">type: str</span>  <span class="li-normal">example: overwrite</span>  </li>
 <li> <span class="li-return"> log-disk-full-percentage </span> - Consider log disk as full at this usage percentage. <span class="li-normal">type: int</span>  <span class="li-normal">example: 80</span>  </li>
 <li> <span class="li-return"> max-log-file-size </span> - Maximum log file size before rolling. <span class="li-normal">type: int</span>  <span class="li-normal">example: 100</span>  </li>
 <li> <span class="li-return"> roll-day </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> roll-schedule </span> - Frequency to check log file for rolling. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> roll-time </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> server-type </span> - Server type. <span class="li-normal">type: str</span>  <span class="li-normal">example: FTP</span>  </li>
 <li> <span class="li-return"> severity </span> - Least severity level to log. <span class="li-normal">type: str</span>  <span class="li-normal">example: information</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable local disk log. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> upload </span> - Upload log file when rolling. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> upload-delete-files </span> - Delete log files after uploading (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> upload-time </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> uploaddir </span> - Log file upload remote directory. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> uploadip </span> - IP address of log uploading server. <span class="li-normal">type: str</span>  <span class="li-normal">example: 0.0.0.0</span>  </li>
 <li> <span class="li-return"> uploadpass </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC NDk0NjE4Nzg3MjIwODA3N71+qrz/6PhYvtMUVz84NXNAP8LBSobOqp91xwfif6Oy3+uy8/crasneRp4VbtBQntyLw7E8MbzHoUlJp8Y2cQLnVfVsTQsRfvtq/BZcpTL+c2yDARD0Bvd1khGe4e1mCVFSVuCTSXxm6CmxqPpcGKFfHLyn</span>  </li>
 </ul>
 <li> <span class="li-return"> uploadport </span> - Server port (0 = default protocol port). <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> uploadsched </span> - Scheduled upload (disable = upload when rolling). <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> uploadtype </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> uploaduser </span> - User account in upload server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> uploadzip </span> - Compress upload logs. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/locallog/disk/setting</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/locallog/disk/setting</span>  </li>
 </ul>
 </ul>





Status
------

- This module is not guaranteed to have a backwards compatible interface.


Authors
-------

- Frank Shen (@fshen01)
- Link Zheng (@zhengl)


.. hint::

    If you notice any issues in this documentation, you can create a pull request to improve it.



