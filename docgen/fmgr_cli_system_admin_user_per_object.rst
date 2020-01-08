:source: fmgr_cli_system_admin_user_per_object.py

:orphan:

.. _fmgr_cli_system_admin_user_per_object:

fmgr_cli_system_admin_user_per_object -- Admin user.
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[delete, get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/admin/user/{user}`
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
 <li><span class="li-head">parameters for method: [delete, get]</span> - Admin user.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Admin user.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">adom</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">adom-name</span> - Admin domain names. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">adom-exclude</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">adom-name</span> - Admin domain names. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">app-filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">app-filter-name</span> - App filter name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">avatar</span> - Image file for avatar (maximum 4K base64 encoded). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ca</span> - PKI user certificate CA (CA name in local). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">change-password</span> - Enable/disable restricted user to change self password. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">dashboard</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
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
 <li><span class="li-head">dashboard-tabs</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - Tab name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tabid</span> - Tab ID. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 </ul>
 <li><span class="li-head">description</span> - Description. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dev-group</span> - device group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">email-address</span> - Email address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ext-auth-accprofile-override</span> - Allow to use the access profile provided by the remote authentication server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">ext-auth-adom-override</span> - Allow to use the ADOM provided by the remote authentication server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">ext-auth-group-match</span> - Only administrators belonging to this group can login. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">first-name</span> - First name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">force-password-change</span> - Enable/disable force password change on next login. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">group</span> - Group name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">hidden</span> - Hidden administrator. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">ips-filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">ips-filter-name</span> - IPS filter name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ipv6_trusthost1</span> - Admin user trusted host IPv6, default ::/0 for all. <span class="li-normal">type: str</span>  <span class="li-normal">default: ::/0</span> </li>
 <li><span class="li-head">ipv6_trusthost10</span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span>  <span class="li-normal">default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128</span> </li>
 <li><span class="li-head">ipv6_trusthost2</span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span>  <span class="li-normal">default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128</span> </li>
 <li><span class="li-head">ipv6_trusthost3</span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span>  <span class="li-normal">default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128</span> </li>
 <li><span class="li-head">ipv6_trusthost4</span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span>  <span class="li-normal">default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128</span> </li>
 <li><span class="li-head">ipv6_trusthost5</span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span>  <span class="li-normal">default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128</span> </li>
 <li><span class="li-head">ipv6_trusthost6</span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span>  <span class="li-normal">default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128</span> </li>
 <li><span class="li-head">ipv6_trusthost7</span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span>  <span class="li-normal">default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128</span> </li>
 <li><span class="li-head">ipv6_trusthost8</span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span>  <span class="li-normal">default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128</span> </li>
 <li><span class="li-head">ipv6_trusthost9</span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span>  <span class="li-normal">default: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128</span> </li>
 <li><span class="li-head">last-name</span> - Last name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ldap-server</span> - LDAP server name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">meta-data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">fieldlength</span> - Field length. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">fieldname</span> - Field name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fieldvalue</span> - Field value. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">importance</span> - Importance. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [optional, required]</span>  <span class="li-normal">default: optional</span> </li>
 <li><span class="li-head">status</span> - Status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span>  <span class="li-normal">default: enabled</span> </li>
 </ul>
 <li><span class="li-head">mobile-number</span> - Mobile number. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">pager-number</span> - Pager number. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC ODU0NTM3NDg1NTMxMDg0MEm8OIAeHq0agoeKH1cknBy7orKo5c0jSfMSXT+VuqYN+atv8wiIW7W8PMzVMSjUkVEnbEpEW/komaek5rcWGIHzpijPphfS09Vlm0vEArsMz6UNqGxf5qLL/MxjITcW4WPWIFLPTPxZQAMoakc7pn8jNgVL</span> </li>
 </ul>
 <li><span class="li-head">password-expire</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">phone-number</span> - Phone number. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">policy-package</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">policy-package-name</span> - Policy package names. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">profileid</span> - Profile ID. <span class="li-normal">type: str</span>  <span class="li-normal">default: Restricted_User</span> </li>
 <li><span class="li-head">radius_server</span> - RADIUS server name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">restrict-access</span> - Enable/disable restricted access to development VDOM. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">restrict-dev-vdom</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">dev-vdom</span> - Device or device VDOM. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">rpc-permit</span> - set none/read/read-write rpc-permission. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [read-write, none, read]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">ssh-public-key1</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ssh-public-key2</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ssh-public-key3</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">subject</span> - PKI user certificate name constraints. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tacacs-plus-server</span> - TACACS+ server name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">trusthost1</span> - Admin user trusted host IP, default 0. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0 0.0.0.0</span> </li>
 <li><span class="li-head">trusthost10</span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span>  <span class="li-normal">default: 255.255.255.255 255.255.255.255</span> </li>
 <li><span class="li-head">trusthost2</span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span>  <span class="li-normal">default: 255.255.255.255 255.255.255.255</span> </li>
 <li><span class="li-head">trusthost3</span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span>  <span class="li-normal">default: 255.255.255.255 255.255.255.255</span> </li>
 <li><span class="li-head">trusthost4</span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span>  <span class="li-normal">default: 255.255.255.255 255.255.255.255</span> </li>
 <li><span class="li-head">trusthost5</span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span>  <span class="li-normal">default: 255.255.255.255 255.255.255.255</span> </li>
 <li><span class="li-head">trusthost6</span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span>  <span class="li-normal">default: 255.255.255.255 255.255.255.255</span> </li>
 <li><span class="li-head">trusthost7</span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span>  <span class="li-normal">default: 255.255.255.255 255.255.255.255</span> </li>
 <li><span class="li-head">trusthost8</span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span>  <span class="li-normal">default: 255.255.255.255 255.255.255.255</span> </li>
 <li><span class="li-head">trusthost9</span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span>  <span class="li-normal">default: 255.255.255.255 255.255.255.255</span> </li>
 <li><span class="li-head">two-factor-auth</span> - Enable 2-factor authentication (certificate + password). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">user_type</span> - User type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [local, radius, ldap, tacacs-plus, pki-auth, group]</span>  <span class="li-normal">default: local</span> </li>
 <li><span class="li-head">userid</span> - User name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">web-filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">web-filter-name</span> - Web filter name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">wildcard</span> - Enable/disable wildcard remote authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/ADMIN/USER/{USER}
      fmgr_cli_system_admin_user_per_object:
         method: <value in [set, update]>
         url_params:
            user: <value of string>
         params:
            -
               data:
                  adom:
                    -
                        adom-name: <value of string>
                  adom-exclude:
                    -
                        adom-name: <value of string>
                  app-filter:
                    -
                        app-filter-name: <value of string>
                  avatar: <value of string>
                  ca: <value of string>
                  change-password: <value in [disable, enable] default: 'disable'>
                  dashboard:
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
                  dashboard-tabs:
                    -
                        name: <value of string>
                        tabid: <value of integer default: 0>
                  description: <value of string>
                  dev-group: <value of string>
                  email-address: <value of string>
                  ext-auth-accprofile-override: <value in [disable, enable] default: 'disable'>
                  ext-auth-adom-override: <value in [disable, enable] default: 'disable'>
                  ext-auth-group-match: <value of string>
                  first-name: <value of string>
                  force-password-change: <value in [disable, enable] default: 'disable'>
                  group: <value of string>
                  hidden: <value of integer default: 0>
                  ips-filter:
                    -
                        ips-filter-name: <value of string>
                  ipv6_trusthost1: <value of string default: '::/0'>
                  ipv6_trusthost10: <value of string default: 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128'>
                  ipv6_trusthost2: <value of string default: 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128'>
                  ipv6_trusthost3: <value of string default: 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128'>
                  ipv6_trusthost4: <value of string default: 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128'>
                  ipv6_trusthost5: <value of string default: 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128'>
                  ipv6_trusthost6: <value of string default: 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128'>
                  ipv6_trusthost7: <value of string default: 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128'>
                  ipv6_trusthost8: <value of string default: 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128'>
                  ipv6_trusthost9: <value of string default: 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128'>
                  last-name: <value of string>
                  ldap-server: <value of string>
                  meta-data:
                    -
                        fieldlength: <value of integer default: 0>
                        fieldname: <value of string>
                        fieldvalue: <value of string>
                        importance: <value in [optional, required] default: 'optional'>
                        status: <value in [disabled, enabled] default: 'enabled'>
                  mobile-number: <value of string>
                  pager-number: <value of string>
                  password:
                    - <value of string default: 'ENC ODU0NTM3NDg1NTMxMDg0MEm8OIAeHq0agoeKH1cknBy7orKo5c0jSfMSXT+VuqYN+atv8wiI...'>
                  password-expire:
                    - <value of string>
                  phone-number: <value of string>
                  policy-package:
                    -
                        policy-package-name: <value of string>
                  profileid: <value of string default: 'Restricted_User'>
                  radius_server: <value of string>
                  restrict-access: <value in [disable, enable] default: 'disable'>
                  restrict-dev-vdom:
                    -
                        dev-vdom: <value of string>
                  rpc-permit: <value in [read-write, none, read] default: 'none'>
                  ssh-public-key1:
                    - <value of string>
                  ssh-public-key2:
                    - <value of string>
                  ssh-public-key3:
                    - <value of string>
                  subject: <value of string>
                  tacacs-plus-server: <value of string>
                  trusthost1: <value of string default: '0.0.0.0 0.0.0.0'>
                  trusthost10: <value of string default: '255.255.255.255 255.255.255.255'>
                  trusthost2: <value of string default: '255.255.255.255 255.255.255.255'>
                  trusthost3: <value of string default: '255.255.255.255 255.255.255.255'>
                  trusthost4: <value of string default: '255.255.255.255 255.255.255.255'>
                  trusthost5: <value of string default: '255.255.255.255 255.255.255.255'>
                  trusthost6: <value of string default: '255.255.255.255 255.255.255.255'>
                  trusthost7: <value of string default: '255.255.255.255 255.255.255.255'>
                  trusthost8: <value of string default: '255.255.255.255 255.255.255.255'>
                  trusthost9: <value of string default: '255.255.255.255 255.255.255.255'>
                  two-factor-auth: <value in [disable, enable] default: 'disable'>
                  user_type: <value in [local, radius, ldap, ...] default: 'local'>
                  userid: <value of string>
                  web-filter:
                    -
                        web-filter-name: <value of string>
                  wildcard: <value in [disable, enable] default: 'disable'>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [delete, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/admin/user/{user}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> adom </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> adom-name </span> - Admin domain names. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> adom-exclude </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> adom-name </span> - Admin domain names. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> app-filter </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> app-filter-name </span> - App filter name. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> avatar </span> - Image file for avatar (maximum 4K base64 encoded). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ca </span> - PKI user certificate CA (CA name in local). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> change-password </span> - Enable/disable restricted user to change self password. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> dashboard </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
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
 <li> <span class="li-return"> dashboard-tabs </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - Tab name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tabid </span> - Tab ID. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 </ul>
 <li> <span class="li-return"> description </span> - Description. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dev-group </span> - device group. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> email-address </span> - Email address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ext-auth-accprofile-override </span> - Allow to use the access profile provided by the remote authentication server. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> ext-auth-adom-override </span> - Allow to use the ADOM provided by the remote authentication server. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> ext-auth-group-match </span> - Only administrators belonging to this group can login. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> first-name </span> - First name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> force-password-change </span> - Enable/disable force password change on next login. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> group </span> - Group name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> hidden </span> - Hidden administrator. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> ips-filter </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> ips-filter-name </span> - IPS filter name. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ipv6_trusthost1 </span> - Admin user trusted host IPv6, default ::/0 for all. <span class="li-normal">type: str</span>  <span class="li-normal">example: ::/0</span>  </li>
 <li> <span class="li-return"> ipv6_trusthost10 </span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span>  <span class="li-normal">example: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128</span>  </li>
 <li> <span class="li-return"> ipv6_trusthost2 </span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span>  <span class="li-normal">example: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128</span>  </li>
 <li> <span class="li-return"> ipv6_trusthost3 </span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span>  <span class="li-normal">example: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128</span>  </li>
 <li> <span class="li-return"> ipv6_trusthost4 </span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span>  <span class="li-normal">example: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128</span>  </li>
 <li> <span class="li-return"> ipv6_trusthost5 </span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span>  <span class="li-normal">example: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128</span>  </li>
 <li> <span class="li-return"> ipv6_trusthost6 </span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span>  <span class="li-normal">example: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128</span>  </li>
 <li> <span class="li-return"> ipv6_trusthost7 </span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span>  <span class="li-normal">example: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128</span>  </li>
 <li> <span class="li-return"> ipv6_trusthost8 </span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span>  <span class="li-normal">example: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128</span>  </li>
 <li> <span class="li-return"> ipv6_trusthost9 </span> - Admin user trusted host IPv6, default ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128 for none. <span class="li-normal">type: str</span>  <span class="li-normal">example: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128</span>  </li>
 <li> <span class="li-return"> last-name </span> - Last name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ldap-server </span> - LDAP server name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> meta-data </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> fieldlength </span> - Field length. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> fieldname </span> - Field name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fieldvalue </span> - Field value. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> importance </span> - Importance. <span class="li-normal">type: str</span>  <span class="li-normal">example: optional</span>  </li>
 <li> <span class="li-return"> status </span> - Status. <span class="li-normal">type: str</span>  <span class="li-normal">example: enabled</span>  </li>
 </ul>
 <li> <span class="li-return"> mobile-number </span> - Mobile number. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pager-number </span> - Pager number. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC ODU0NTM3NDg1NTMxMDg0MEm8OIAeHq0agoeKH1cknBy7orKo5c0jSfMSXT+VuqYN+atv8wiIW7W8PMzVMSjUkVEnbEpEW/komaek5rcWGIHzpijPphfS09Vlm0vEArsMz6UNqGxf5qLL/MxjITcW4WPWIFLPTPxZQAMoakc7pn8jNgVL</span>  </li>
 </ul>
 <li> <span class="li-return"> password-expire </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> phone-number </span> - Phone number. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> policy-package </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> policy-package-name </span> - Policy package names. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> profileid </span> - Profile ID. <span class="li-normal">type: str</span>  <span class="li-normal">example: Restricted_User</span>  </li>
 <li> <span class="li-return"> radius_server </span> - RADIUS server name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> restrict-access </span> - Enable/disable restricted access to development VDOM. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> restrict-dev-vdom </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> dev-vdom </span> - Device or device VDOM. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> rpc-permit </span> - set none/read/read-write rpc-permission. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> ssh-public-key1 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ssh-public-key2 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ssh-public-key3 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> subject </span> - PKI user certificate name constraints. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tacacs-plus-server </span> - TACACS+ server name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> trusthost1 </span> - Admin user trusted host IP, default 0. <span class="li-normal">type: str</span>  <span class="li-normal">example: 0.0.0.0 0.0.0.0</span>  </li>
 <li> <span class="li-return"> trusthost10 </span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span>  <span class="li-normal">example: 255.255.255.255 255.255.255.255</span>  </li>
 <li> <span class="li-return"> trusthost2 </span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span>  <span class="li-normal">example: 255.255.255.255 255.255.255.255</span>  </li>
 <li> <span class="li-return"> trusthost3 </span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span>  <span class="li-normal">example: 255.255.255.255 255.255.255.255</span>  </li>
 <li> <span class="li-return"> trusthost4 </span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span>  <span class="li-normal">example: 255.255.255.255 255.255.255.255</span>  </li>
 <li> <span class="li-return"> trusthost5 </span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span>  <span class="li-normal">example: 255.255.255.255 255.255.255.255</span>  </li>
 <li> <span class="li-return"> trusthost6 </span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span>  <span class="li-normal">example: 255.255.255.255 255.255.255.255</span>  </li>
 <li> <span class="li-return"> trusthost7 </span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span>  <span class="li-normal">example: 255.255.255.255 255.255.255.255</span>  </li>
 <li> <span class="li-return"> trusthost8 </span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span>  <span class="li-normal">example: 255.255.255.255 255.255.255.255</span>  </li>
 <li> <span class="li-return"> trusthost9 </span> - Admin user trusted host IP, default 255. <span class="li-normal">type: str</span>  <span class="li-normal">example: 255.255.255.255 255.255.255.255</span>  </li>
 <li> <span class="li-return"> two-factor-auth </span> - Enable 2-factor authentication (certificate + password). <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> user_type </span> - User type. <span class="li-normal">type: str</span>  <span class="li-normal">example: local</span>  </li>
 <li> <span class="li-return"> userid </span> - User name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> web-filter </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> web-filter-name </span> - Web filter name. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> wildcard </span> - Enable/disable wildcard remote authentication. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/admin/user/{user}</span>  </li>
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



