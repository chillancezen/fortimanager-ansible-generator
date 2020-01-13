:source: fmgr_system_admin_user_dashboard.py

:orphan:

.. _fmgr_system_admin_user_dashboard:

fmgr_system_admin_user_dashboard -- Custom dashboard widgets.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/admin/user/{user}/dashboard`
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
 <li><span class="li-head">url_params</span> - parameters in url path <span class="li-normal">type: dict</span> <span class="li-required">required: true</span></li>
 <ul class="ul-self">
 <li><span class="li-head">user</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Custom dashboard widgets.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">column</span> - Widgets column ID. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">diskio-content-type</span> - Disk I/O Monitor widgets chart type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [util, iops, blks]</span>  <span class="li-normal">default: util</span> </li>
 <li><span class="li-head">diskio-period</span> - Disk I/O Monitor widgets data period. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1hour, 8hour, 24hour]</span>  <span class="li-normal">default: 1hour</span> </li>
 <li><span class="li-head">log-rate-period</span> - Log receive monitor widgets data period. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [2min , 1hour, 6hours]</span> </li>
 <li><span class="li-head">log-rate-topn</span> - Log receive monitor widgets number of top items to display. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1, 2, 3, 4, 5]</span>  <span class="li-normal">default: 5</span> </li>
 <li><span class="li-head">log-rate-type</span> - Log receive monitor widgets statistics breakdown options. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [log, device]</span>  <span class="li-normal">default: device</span> </li>
 <li><span class="li-head">moduleid</span> - Widget ID. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">name</span> - Widget name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">num-entries</span> - Number of entries. <span class="li-normal">type: int</span>  <span class="li-normal">default: 10</span> </li>
 <li><span class="li-head">refresh-interval</span> - Widgets refresh interval. <span class="li-normal">type: int</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">res-cpu-display</span> - Widgets CPU display type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [average , each]</span>  <span class="li-normal">default: average </span> </li>
 <li><span class="li-head">res-period</span> - Widgets data period. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [10min , hour, day]</span>  <span class="li-normal">default: 10min </span> </li>
 <li><span class="li-head">res-view-type</span> - Widgets data view type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [real-time , history]</span>  <span class="li-normal">default: history</span> </li>
 <li><span class="li-head">status</span> - Widgets opened/closed state. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [close, open]</span>  <span class="li-normal">default: open</span> </li>
 <li><span class="li-head">tabid</span> - ID of tab where widget is displayed. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">time-period</span> - Log Database Monitor widgets data period. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1hour, 8hour, 24hour]</span>  <span class="li-normal">default: 1hour</span> </li>
 <li><span class="li-head">widget-type</span> - Widget type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [top-lograte, sysres, sysinfo, licinfo, jsconsole, sysop, alert, statistics, rpteng, raid, logrecv, devsummary, logdb-perf, logdb-lag, disk-io, log-rcvd-fwd]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Custom dashboard widgets.</li>
 <ul class="ul-self">
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [column, diskio-content-type, diskio-period, log-rate-period, log-rate-topn, log-rate-type, moduleid, name, num-entries, refresh-interval, res-cpu-display, res-period, res-view-type, status, tabid, time-period, widget-type]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">loadsub</span> - Enable or disable the return of any sub-objects. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [count, syntax]</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/ADMIN/USER/{USER}/DASHBOARD
      fmgr_system_admin_user_dashboard:
         method: <value in [add, set, update]>
         url_params:
            user: <value of string>
         params:
            -
               data:
                 -
                     column: <value of integer default: 0>
                     diskio-content-type: <value in [util, iops, blks] default: 'util'>
                     diskio-period: <value in [1hour, 8hour, 24hour] default: '1hour'>
                     log-rate-period: <value in [2min , 1hour, 6hours]>
                     log-rate-topn: <value in [1, 2, 3, ...] default: '5'>
                     log-rate-type: <value in [log, device] default: 'device'>
                     moduleid: <value of integer default: 0>
                     name: <value of string>
                     num-entries: <value of integer default: 10>
                     refresh-interval: <value of integer default: 300>
                     res-cpu-display: <value in [average , each] default: 'average '>
                     res-period: <value in [10min , hour, day] default: '10min '>
                     res-view-type: <value in [real-time , history] default: 'history'>
                     status: <value in [close, open] default: 'open'>
                     tabid: <value of integer default: 0>
                     time-period: <value in [1hour, 8hour, 24hour] default: '1hour'>
                     widget-type: <value in [top-lograte, sysres, sysinfo, ...]>

    - name: REQUESTING /CLI/SYSTEM/ADMIN/USER/{USER}/DASHBOARD
      fmgr_system_admin_user_dashboard:
         method: <value in [get]>
         url_params:
            user: <value of string>
         params:
            -
               fields:
                 -
                    - <value in [column, diskio-content-type, diskio-period, ...]>
               filter:
                 - <value of string>
               loadsub: <value of integer>
               option: <value in [count, syntax]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [add, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/admin/user/{user}/dashboard</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> column </span> - Widgets column ID. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> diskio-content-type </span> - Disk I/O Monitor widgets chart type. <span class="li-normal">type: str</span>  <span class="li-normal">example: util</span>  </li>
 <li> <span class="li-return"> diskio-period </span> - Disk I/O Monitor widgets data period. <span class="li-normal">type: str</span>  <span class="li-normal">example: 1hour</span>  </li>
 <li> <span class="li-return"> log-rate-period </span> - Log receive monitor widgets data period. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> log-rate-topn </span> - Log receive monitor widgets number of top items to display. <span class="li-normal">type: str</span>  <span class="li-normal">example: 5</span>  </li>
 <li> <span class="li-return"> log-rate-type </span> - Log receive monitor widgets statistics breakdown options. <span class="li-normal">type: str</span>  <span class="li-normal">example: device</span>  </li>
 <li> <span class="li-return"> moduleid </span> - Widget ID. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> name </span> - Widget name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> num-entries </span> - Number of entries. <span class="li-normal">type: int</span>  <span class="li-normal">example: 10</span>  </li>
 <li> <span class="li-return"> refresh-interval </span> - Widgets refresh interval. <span class="li-normal">type: int</span>  <span class="li-normal">example: 300</span>  </li>
 <li> <span class="li-return"> res-cpu-display </span> - Widgets CPU display type. <span class="li-normal">type: str</span>  <span class="li-normal">example: average </span>  </li>
 <li> <span class="li-return"> res-period </span> - Widgets data period. <span class="li-normal">type: str</span>  <span class="li-normal">example: 10min </span>  </li>
 <li> <span class="li-return"> res-view-type </span> - Widgets data view type. <span class="li-normal">type: str</span>  <span class="li-normal">example: history</span>  </li>
 <li> <span class="li-return"> status </span> - Widgets opened/closed state. <span class="li-normal">type: str</span>  <span class="li-normal">example: open</span>  </li>
 <li> <span class="li-return"> tabid </span> - ID of tab where widget is displayed. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> time-period </span> - Log Database Monitor widgets data period. <span class="li-normal">type: str</span>  <span class="li-normal">example: 1hour</span>  </li>
 <li> <span class="li-return"> widget-type </span> - Widget type. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/admin/user/{user}/dashboard</span>  </li>
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



