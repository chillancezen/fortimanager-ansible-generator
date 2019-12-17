:source: fmgr_cli_system_backup_all_settings.py

:orphan:

.. _fmgr_cli_system_backup_all_settings:

fmgr_cli_system_backup_all_settings -- Scheduled backup settings.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/backup/all-settings`
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
 <li><span class="li-head">parameters for method: [get]</span> - Scheduled backup settings.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Scheduled backup settings.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">cert</span> - SSH certificate for authentication. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">crptpasswd</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC MTMzMDc1MDgxNzQ0ODY0M2NSZUKD2VMvwzY+fu/IOqXefv5r84Cvz6X817vduD08gM1BG0K7muAtsALrSSvZjpqR08ZjShNGdhTR6Y7clcN6rnCh7jFAA9qF9cXracjbMmMkmLh2JuJH35O0EplcfinZKTXky8RCyig4J/DXAtiQpW7l</span> </li>
 </ul>
 <li><span class="li-head">directory</span> - Directory in which file will be stored on backup server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">passwd</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC NjE1OTk5NjcxODE1MDYyOR9zgwo4rNRY0psUIe6ZdXfehJTrTnmzU4GJWXfob8IxqxmLrU/5rQxywxo85lXVAnrjLD1WUkUEls6PMhOwReIaAQVP0y0g8qNzjlHU+Tsm6L13KblsH7G+yJEdMMyVj8MNSwdwJiXw9s94q+hXRCAs4iwJ</span> </li>
 </ul>
 <li><span class="li-head">protocol</span> - Protocol used to backup. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sftp, ftp, scp]</span>  <span class="li-normal">default: sftp</span> </li>
 <li><span class="li-head">server</span> - Backup server name/IP. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable schedule backup. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">time</span> - Time to backup. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">user</span> - Backup server login user. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">week_days</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [monday, tuesday, wednesday, thursday, friday, saturday, sunday]</span> </li>
 </ul>
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
    - name: send request to /cli/system/backup/all-settings
      fmgr_cli_system_backup_all_settings:
         method: <value in [set, update]>
         params:
            - 
               data: 
                  cert: <value of string>
                  crptpasswd: 
                   - <value of string default: ENC MTMzMDc1MDgxNzQ0ODY0M2NSZUKD2VMvwzY+fu/IOqXefv5r84Cvz6X817vduD08gM1BG0K7muAtsALrSSvZjpqR08ZjShNGdhTR6Y7clcN6rnCh7jFAA9qF9cXracjbMmMkmLh2JuJH35O0EplcfinZKTXky8RCyig4J/DXAtiQpW7l>
                  directory: <value of string>
                  passwd: 
                   - <value of string default: ENC NjE1OTk5NjcxODE1MDYyOR9zgwo4rNRY0psUIe6ZdXfehJTrTnmzU4GJWXfob8IxqxmLrU/5rQxywxo85lXVAnrjLD1WUkUEls6PMhOwReIaAQVP0y0g8qNzjlHU+Tsm6L13KblsH7G+yJEdMMyVj8MNSwdwJiXw9s94q+hXRCAs4iwJ>
                  protocol: <value in [sftp, ftp, scp] default: sftp>
                  server: <value of string>
                  status: <value in [disable, enable] default: disable>
                  time: <value of string>
                  user: <value of string>
                  week_days: 
                   - <value in [monday, tuesday, wednesday, ...]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> cert </span> - SSH certificate for authentication. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> crptpasswd </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC MTMzMDc1MDgxNzQ0ODY0M2NSZUKD2VMvwzY+fu/IOqXefv5r84Cvz6X817vduD08gM1BG0K7muAtsALrSSvZjpqR08ZjShNGdhTR6Y7clcN6rnCh7jFAA9qF9cXracjbMmMkmLh2JuJH35O0EplcfinZKTXky8RCyig4J/DXAtiQpW7l</span>  </li>
 </ul>
 <li> <span class="li-return"> directory </span> - Directory in which file will be stored on backup server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> passwd </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC NjE1OTk5NjcxODE1MDYyOR9zgwo4rNRY0psUIe6ZdXfehJTrTnmzU4GJWXfob8IxqxmLrU/5rQxywxo85lXVAnrjLD1WUkUEls6PMhOwReIaAQVP0y0g8qNzjlHU+Tsm6L13KblsH7G+yJEdMMyVj8MNSwdwJiXw9s94q+hXRCAs4iwJ</span>  </li>
 </ul>
 <li> <span class="li-return"> protocol </span> - Protocol used to backup. <span class="li-normal">type: str</span>  <span class="li-normal">example: sftp</span>  </li>
 <li> <span class="li-return"> server </span> - Backup server name/IP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable schedule backup. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> time </span> - Time to backup. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> user </span> - Backup server login user. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> week_days </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/backup/all-settings</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/backup/all-settings</span>  </li>
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



