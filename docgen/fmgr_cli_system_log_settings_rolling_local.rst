:source: fmgr_cli_system_log_settings_rolling_local.py

:orphan:

.. _fmgr_cli_system_log_settings_rolling_local:

fmgr_cli_system_log_settings_rolling_local -- Log rolling policy for local logs.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/log/settings/rolling-local`
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
 <li><span class="li-head">parameters for method: [get]</span> - Log rolling policy for local logs.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Log rolling policy for local logs.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">days</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sun, mon, tue, wed, thu, fri, sat]</span> </li>
 </ul>
 <li><span class="li-head">del-files</span> - Enable/disable log file deletion after uploading. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">directory</span> - Upload server directory, for Unix server, use absolute <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">file-size</span> - Roll log files when they reach this size (MB). <span class="li-normal">type: int</span>  <span class="li-normal">default: 200</span> </li>
 <li><span class="li-head">gzip-format</span> - Enable/disable compression of uploaded log files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">hour</span> - Log files rolling schedule (hour). <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">ip</span> - Upload server IP address. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">ip2</span> - Upload server IP2 address. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">ip3</span> - Upload server IP3 address. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">log-format</span> - Format of uploaded log files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [native, text, csv]</span>  <span class="li-normal">default: native</span> </li>
 <li><span class="li-head">min</span> - Log files rolling schedule (minutes). <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC MTA3MjA4MzMzNDU1NjUyNKTuKbF8PktnhHOXsSkxjhxlHjwIE22BP2ak2RRotV+wsRkGD/HamAdeTJyxk8NUM5OZPMpAHhPZssCynPvryOwf6S7Bq6wiH2BSRxNp+JDC+OcO7KbXMy+0JRgHFegouXqd2l9n+MweBcSP4qsn/P2nZEbm</span> </li>
 </ul>
 <li><span class="li-head">password2</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC NjYyODA3OTExODQ2OTQ0N1452tPlCQK0/AvB5jye7GpFLLpArdcOazRo1BOGPYnKcgz2Iqn/Nt+7ZZereH6gM4nFNmsLipjwaznrIUtA2dAogsuYgiTXfCbK5hwOSXo5AniueUP1/fJcBeU7xnIUqTCWf8OBrStYnmyEHg0QHHzSmvRq</span> </li>
 </ul>
 <li><span class="li-head">password3</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC Mzk3ODgxMDA2MjU0NzUwNft3N0w+quBucyAJLuI78/qyOQAkHkRQnCPqX7Crikas/93czxOX2okFGGyPN7MhHEFPwsNyxKziYau12Szy5r5kYxSVnovhsE6m4D9uMiOEfqIm+ZM8t8x0vvZiERLvbNCwn8E4nMkDvz09rKXJdDK1lelu</span> </li>
 </ul>
 <li><span class="li-head">server-type</span> - Upload server type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ftp, sftp, scp]</span>  <span class="li-normal">default: ftp</span> </li>
 <li><span class="li-head">upload</span> - Enable/disable log file uploads. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">upload-hour</span> - Log files upload schedule (hour). <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">upload-mode</span> - Upload mode with multiple servers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [backup, mirror]</span>  <span class="li-normal">default: backup</span> </li>
 <li><span class="li-head">upload-trigger</span> - Event triggering log files upload. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [on-roll, on-schedule]</span>  <span class="li-normal">default: on-roll</span> </li>
 <li><span class="li-head">username</span> - Upload server login username. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">username2</span> - Upload server login username2. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">username3</span> - Upload server login username3. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">when</span> - Roll log files periodically. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, daily, weekly]</span>  <span class="li-normal">default: none</span> </li>
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
    - name: send request to /cli/system/log/settings/rolling-local
      fmgr_cli_system_log_settings_rolling_local:
         method: <value in [set, update]>
         params:
            - 
               data: 
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



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> days </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> del-files </span> - Enable/disable log file deletion after uploading. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> directory </span> - Upload server directory, for Unix server, use absolute <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> file-size </span> - Roll log files when they reach this size (MB). <span class="li-normal">type: int</span>  <span class="li-normal">example: 200</span>  </li>
 <li> <span class="li-return"> gzip-format </span> - Enable/disable compression of uploaded log files. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> hour </span> - Log files rolling schedule (hour). <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> ip </span> - Upload server IP address. <span class="li-normal">type: str</span>  <span class="li-normal">example: 0.0.0.0</span>  </li>
 <li> <span class="li-return"> ip2 </span> - Upload server IP2 address. <span class="li-normal">type: str</span>  <span class="li-normal">example: 0.0.0.0</span>  </li>
 <li> <span class="li-return"> ip3 </span> - Upload server IP3 address. <span class="li-normal">type: str</span>  <span class="li-normal">example: 0.0.0.0</span>  </li>
 <li> <span class="li-return"> log-format </span> - Format of uploaded log files. <span class="li-normal">type: str</span>  <span class="li-normal">example: native</span>  </li>
 <li> <span class="li-return"> min </span> - Log files rolling schedule (minutes). <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC MTA3MjA4MzMzNDU1NjUyNKTuKbF8PktnhHOXsSkxjhxlHjwIE22BP2ak2RRotV+wsRkGD/HamAdeTJyxk8NUM5OZPMpAHhPZssCynPvryOwf6S7Bq6wiH2BSRxNp+JDC+OcO7KbXMy+0JRgHFegouXqd2l9n+MweBcSP4qsn/P2nZEbm</span>  </li>
 </ul>
 <li> <span class="li-return"> password2 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC NjYyODA3OTExODQ2OTQ0N1452tPlCQK0/AvB5jye7GpFLLpArdcOazRo1BOGPYnKcgz2Iqn/Nt+7ZZereH6gM4nFNmsLipjwaznrIUtA2dAogsuYgiTXfCbK5hwOSXo5AniueUP1/fJcBeU7xnIUqTCWf8OBrStYnmyEHg0QHHzSmvRq</span>  </li>
 </ul>
 <li> <span class="li-return"> password3 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC Mzk3ODgxMDA2MjU0NzUwNft3N0w+quBucyAJLuI78/qyOQAkHkRQnCPqX7Crikas/93czxOX2okFGGyPN7MhHEFPwsNyxKziYau12Szy5r5kYxSVnovhsE6m4D9uMiOEfqIm+ZM8t8x0vvZiERLvbNCwn8E4nMkDvz09rKXJdDK1lelu</span>  </li>
 </ul>
 <li> <span class="li-return"> server-type </span> - Upload server type. <span class="li-normal">type: str</span>  <span class="li-normal">example: ftp</span>  </li>
 <li> <span class="li-return"> upload </span> - Enable/disable log file uploads. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> upload-hour </span> - Log files upload schedule (hour). <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> upload-mode </span> - Upload mode with multiple servers. <span class="li-normal">type: str</span>  <span class="li-normal">example: backup</span>  </li>
 <li> <span class="li-return"> upload-trigger </span> - Event triggering log files upload. <span class="li-normal">type: str</span>  <span class="li-normal">example: on-roll</span>  </li>
 <li> <span class="li-return"> username </span> - Upload server login username. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> username2 </span> - Upload server login username2. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> username3 </span> - Upload server login username3. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> when </span> - Roll log files periodically. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/log/settings/rolling-local</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/log/settings/rolling-local</span>  </li>
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



