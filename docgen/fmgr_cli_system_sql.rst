:source: fmgr_cli_system_sql.py

:orphan:

.. _fmgr_cli_system_sql:

fmgr_cli_system_sql -- SQL settings.
++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/sql`
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
 <li><span class="li-head">parameters for method: [get]</span> - SQL settings.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - SQL settings.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">background-rebuild</span> - Disable/Enable rebuild SQL database in the background. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">custom-index</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">case-sensitive</span> - Disable/Enable case sensitive index. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">device-type</span> - Device type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [FortiGate, FortiManager, FortiClient, FortiMail, FortiWeb, FortiCache, FortiSandbox, FortiDDoS, FortiAuthenticator, FortiProxy]</span>  <span class="li-normal">default: FortiGate</span> </li>
 <li><span class="li-head">id</span> - Add or Edit log index fields. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">index-field</span> - Log field name to be indexed. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">log-type</span> - Log type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, app-ctrl, attack, content, dlp, emailfilter, event, generic, history, traffic, virus, voip, webfilter, netscan, fct-event, fct-traffic, fct-netscan, waf, gtp, dns, ssh, ssl]</span>  <span class="li-normal">default: traffic</span> </li>
 </ul>
 <li><span class="li-head">database-name</span> - Database name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">database-type</span> - Database type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [mysql, postgres]</span>  <span class="li-normal">default: postgres</span> </li>
 <li><span class="li-head">device-count-high</span> - Must set to enable if the count of registered devices is greater than 8000. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">event-table-partition-time</span> - Maximum SQL database table partitioning time range in minute (0 for unlimited) for event logs. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">fct-table-partition-time</span> - Maximum SQL database table partitioning time range in minute (0 for unlimited) for FortiClient logs. <span class="li-normal">type: int</span>  <span class="li-normal">default: 240</span> </li>
 <li><span class="li-head">logtype</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, app-ctrl, attack, content, dlp, emailfilter, event, generic, history, traffic, virus, voip, webfilter, netscan, fct-event, fct-traffic, fct-netscan, waf, gtp, dns, ssh, ssl]</span> </li>
 </ul>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC NjQ3NzAyNTQ0MjIyMDUxNUE+4gCrDBIJb7pqPICInSs5KmyrG1Tt8M8Zl+eK2k42FSlwDSDiBpNLwRPdCyo8dSIl+p0KUlKP781RcCnzzGAb/gOob+zQwnCMY730a19D6Tf5E3BBEeL/R375HU5/K0L4aeWS/TsuwFbi0JtMJkVKk0je</span> </li>
 </ul>
 <li><span class="li-head">prompt-sql-upgrade</span> - Prompt to convert log database into SQL database at start time on GUI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">rebuild-event</span> - Disable/Enable rebuild event during SQL database rebuilding. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">rebuild-event-start-time</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">server</span> - Database IP or hostname. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">start-time</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">status</span> - SQL database status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, local]</span>  <span class="li-normal">default: local</span> </li>
 <li><span class="li-head">text-search-index</span> - Disable/Enable text search index. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">traffic-table-partition-time</span> - Maximum SQL database table partitioning time range in minute (0 for unlimited) for traffic logs. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">ts-index-field</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">category</span> - Category of text search index fields. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">value</span> - Fields of text search index. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">username</span> - User name for login remote database. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">utm-table-partition-time</span> - Maximum SQL database table partitioning time range in minute (0 for unlimited) for UTM logs. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/SQL
      fmgr_cli_system_sql:
         method: <value in [set, update]>
         params:
            -
               data:
                  background-rebuild: <value in [disable, enable] default: 'enable'>
                  custom-index:
                    -
                        case-sensitive: <value in [disable, enable] default: 'disable'>
                        device-type: <value in [FortiGate, FortiManager, FortiClient, ...] default: 'FortiGate'>
                        id: <value of integer default: 0>
                        index-field: <value of string>
                        log-type: <value in [none, app-ctrl, attack, ...] default: 'traffic'>
                  database-name: <value of string>
                  database-type: <value in [mysql, postgres] default: 'postgres'>
                  device-count-high: <value in [disable, enable] default: 'disable'>
                  event-table-partition-time: <value of integer default: 0>
                  fct-table-partition-time: <value of integer default: 240>
                  logtype:
                    - <value in [none, app-ctrl, attack, ...]>
                  password:
                    - <value of string default: 'ENC NjQ3NzAyNTQ0MjIyMDUxNUE+4gCrDBIJb7pqPICInSs5KmyrG1Tt8M8Zl+eK2k42FSlwDSDi...'>
                  prompt-sql-upgrade: <value in [disable, enable] default: 'enable'>
                  rebuild-event: <value in [disable, enable] default: 'enable'>
                  rebuild-event-start-time:
                    - <value of string>
                  server: <value of string>
                  start-time:
                    - <value of string>
                  status: <value in [disable, local] default: 'local'>
                  text-search-index: <value in [disable, enable] default: 'disable'>
                  traffic-table-partition-time: <value of integer default: 0>
                  ts-index-field:
                    -
                        category: <value of string>
                        value: <value of string>
                  username: <value of string>
                  utm-table-partition-time: <value of integer default: 0>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> background-rebuild </span> - Disable/Enable rebuild SQL database in the background. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> custom-index </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> case-sensitive </span> - Disable/Enable case sensitive index. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> device-type </span> - Device type. <span class="li-normal">type: str</span>  <span class="li-normal">example: FortiGate</span>  </li>
 <li> <span class="li-return"> id </span> - Add or Edit log index fields. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> index-field </span> - Log field name to be indexed. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log-type </span> - Log type. <span class="li-normal">type: str</span>  <span class="li-normal">example: traffic</span>  </li>
 </ul>
 <li> <span class="li-return"> database-name </span> - Database name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> database-type </span> - Database type. <span class="li-normal">type: str</span>  <span class="li-normal">example: postgres</span>  </li>
 <li> <span class="li-return"> device-count-high </span> - Must set to enable if the count of registered devices is greater than 8000. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> event-table-partition-time </span> - Maximum SQL database table partitioning time range in minute (0 for unlimited) for event logs. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> fct-table-partition-time </span> - Maximum SQL database table partitioning time range in minute (0 for unlimited) for FortiClient logs. <span class="li-normal">type: int</span>  <span class="li-normal">example: 240</span>  </li>
 <li> <span class="li-return"> logtype </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC NjQ3NzAyNTQ0MjIyMDUxNUE+4gCrDBIJb7pqPICInSs5KmyrG1Tt8M8Zl+eK2k42FSlwDSDiBpNLwRPdCyo8dSIl+p0KUlKP781RcCnzzGAb/gOob+zQwnCMY730a19D6Tf5E3BBEeL/R375HU5/K0L4aeWS/TsuwFbi0JtMJkVKk0je</span>  </li>
 </ul>
 <li> <span class="li-return"> prompt-sql-upgrade </span> - Prompt to convert log database into SQL database at start time on GUI. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> rebuild-event </span> - Disable/Enable rebuild event during SQL database rebuilding. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> rebuild-event-start-time </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> server </span> - Database IP or hostname. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> start-time </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> status </span> - SQL database status. <span class="li-normal">type: str</span>  <span class="li-normal">example: local</span>  </li>
 <li> <span class="li-return"> text-search-index </span> - Disable/Enable text search index. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> traffic-table-partition-time </span> - Maximum SQL database table partitioning time range in minute (0 for unlimited) for traffic logs. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> ts-index-field </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> category </span> - Category of text search index fields. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> value </span> - Fields of text search index. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> username </span> - User name for login remote database. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> utm-table-partition-time </span> - Maximum SQL database table partitioning time range in minute (0 for unlimited) for UTM logs. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/sql</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/sql</span>  </li>
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



