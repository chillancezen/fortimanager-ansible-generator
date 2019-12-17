:source: fmgr_cli_system_admin_setting.py

:orphan:

.. _fmgr_cli_system_admin_setting:

fmgr_cli_system_admin_setting -- Admin setting.
+++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/admin/setting`
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
 <li><span class="li-head">parameters for method: [get]</span> - Admin setting.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Admin setting.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">access-banner</span> - Enable/disable access banner. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">admin-https-redirect</span> - Enable/disable redirection of HTTP admin traffic to HTTPS. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">admin-login-max</span> - Maximum number admin users logged in at one time (1 - 256). <span class="li-normal">type: int</span>  <span class="li-normal">default: 256</span> </li>
 <li><span class="li-head">admin_server_cert</span> - HTTPS & Web Service server certificate. <span class="li-normal">type: str</span>  <span class="li-normal">default: server.crt</span> </li>
 <li><span class="li-head">allow_register</span> - Enable/disable allowance of register an unregistered device. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">auto-update</span> - Enable/disable FortiGate automatic update. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">banner-message</span> - Banner message. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">chassis-mgmt</span> - Enable or disable chassis management. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">chassis-update-interval</span> - Chassis background update interval (4 - 1440 mins). <span class="li-normal">type: int</span>  <span class="li-normal">default: 15</span> </li>
 <li><span class="li-head">device_sync_status</span> - Enable/disable device synchronization status indication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">gui-theme</span> - Color scheme to use for the administration GUI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [blue, green, red, melongene, spring, summer, autumn, winter, space, calla-lily, binary-tunnel, diving, dreamy, technology, landscape, twilight, canyon, northern-light, astronomy, fish, penguin, panda, polar-bear, parrot, cave]</span>  <span class="li-normal">default: blue</span> </li>
 <li><span class="li-head">http_port</span> - HTTP port. <span class="li-normal">type: int</span>  <span class="li-normal">default: 80</span> </li>
 <li><span class="li-head">https_port</span> - HTTPS port. <span class="li-normal">type: int</span>  <span class="li-normal">default: 443</span> </li>
 <li><span class="li-head">idle_timeout</span> - Idle timeout (1 - 480 min). <span class="li-normal">type: int</span>  <span class="li-normal">default: 15</span> </li>
 <li><span class="li-head">install-ifpolicy-only</span> - Allow install interface policy only. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">mgmt-addr</span> - IP of FortiManager used by FGFM. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mgmt-fqdn</span> - FQDN of FortiManager used by FGFM. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">objects-force-deletion</span> - Enable/disable used objects force deletion. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">offline_mode</span> - Enable/disable offline mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">register_passwd</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC ODA4MzI1MDExMjE4OTgxM/oYbnw5dOwHjdVIoziGMGql3I0Ddz+ewZZfbXj7YeX4ol/rqZveNL7pJsXB6fGh0Bfo+R+211AvBe4558gduEIjb2W9ApZLtp5OAzm78LkH4dyrXL9N/SySeIPG1Oh6i5wvEK4Ox22xdNQmN26CaAMZG9Jl</span> </li>
 </ul>
 <li><span class="li-head">sdwan-monitor-history</span> - Enable/disable hostname display in the GUI login page. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">shell-access</span> - Enable/disable shell access. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">shell-password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC NDM0ODk3MTk5MDUyMTEzMUbHl/j5CmTEcBmvdfBvKn99O6PWsq0PdmnxFXT9hypS7GvefFaz0oVwvAJ5/jgxY3HaLJDNTuNDNZfGQBezH6DURHCF23i/UXtmSSMrrIS8g2oidOj6e593sP+BSfGpQie0tLXFnMb9Lrd4dUAgfnYZpYLh</span> </li>
 </ul>
 <li><span class="li-head">show-add-multiple</span> - Show add multiple button. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">show-adom-devman</span> - Show ADOM device manager tools on GUI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">show-checkbox-in-table</span> - Show checkboxs in tables on GUI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">show-device-import-export</span> - Enable/disable import/export of ADOM, device, and group lists. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">show-hostname</span> - Enable/disable hostname display in the GUI login page. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">show_automatic_script</span> - Enable/disable automatic script. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">show_grouping_script</span> - Enable/disable grouping script. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">show_schedule_script</span> - Enable or disable schedule script. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">show_tcl_script</span> - Enable/disable TCL script. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">unreg_dev_opt</span> - Action to take when unregistered device connects to FortiManager. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [add_no_service, ignore, add_allow_service]</span>  <span class="li-normal">default: add_allow_service</span> </li>
 <li><span class="li-head">webadmin_language</span> - Web admin language. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto_detect, english, simplified_chinese, traditional_chinese, japanese, korean, spanish]</span>  <span class="li-normal">default: auto_detect</span> </li>
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
    - name: send request to /cli/system/admin/setting
      fmgr_cli_system_admin_setting:
         method: <value in [set, update]>
         params:
            - 
               data: 
                  access-banner: <value in [disable, enable] default: disable>
                  admin-https-redirect: <value in [disable, enable] default: enable>
                  admin-login-max: <value of integer default: 256>
                  admin_server_cert: <value of string default: server.crt>
                  allow_register: <value in [disable, enable] default: disable>
                  auto-update: <value in [disable, enable] default: enable>
                  banner-message: <value of string>
                  chassis-mgmt: <value in [disable, enable] default: disable>
                  chassis-update-interval: <value of integer default: 15>
                  device_sync_status: <value in [disable, enable] default: enable>
                  gui-theme: <value in [blue, green, red, ...] default: blue>
                  http_port: <value of integer default: 80>
                  https_port: <value of integer default: 443>
                  idle_timeout: <value of integer default: 15>
                  install-ifpolicy-only: <value in [disable, enable] default: disable>
                  mgmt-addr: <value of string>
                  mgmt-fqdn: <value of string>
                  objects-force-deletion: <value in [disable, enable] default: enable>
                  offline_mode: <value in [disable, enable] default: disable>
                  register_passwd: 
                   - <value of string default: ENC ODA4MzI1MDExMjE4OTgxM/oYbnw5dOwHjdVIoziGMGql3I0Ddz+ewZZfbXj7YeX4ol/rqZveNL7pJsXB6fGh0Bfo+R+211AvBe4558gduEIjb2W9ApZLtp5OAzm78LkH4dyrXL9N/SySeIPG1Oh6i5wvEK4Ox22xdNQmN26CaAMZG9Jl>
                  sdwan-monitor-history: <value in [disable, enable] default: disable>
                  shell-access: <value in [disable, enable] default: disable>
                  shell-password: 
                   - <value of string default: ENC NDM0ODk3MTk5MDUyMTEzMUbHl/j5CmTEcBmvdfBvKn99O6PWsq0PdmnxFXT9hypS7GvefFaz0oVwvAJ5/jgxY3HaLJDNTuNDNZfGQBezH6DURHCF23i/UXtmSSMrrIS8g2oidOj6e593sP+BSfGpQie0tLXFnMb9Lrd4dUAgfnYZpYLh>
                  show-add-multiple: <value in [disable, enable] default: disable>
                  show-adom-devman: <value in [disable, enable] default: enable>
                  show-checkbox-in-table: <value in [disable, enable] default: disable>
                  show-device-import-export: <value in [disable, enable] default: disable>
                  show-hostname: <value in [disable, enable] default: disable>
                  show_automatic_script: <value in [disable, enable] default: disable>
                  show_grouping_script: <value in [disable, enable] default: enable>
                  show_schedule_script: <value in [disable, enable] default: disable>
                  show_tcl_script: <value in [disable, enable] default: disable>
                  unreg_dev_opt: <value in [add_no_service, ignore, add_allow_service] default: add_allow_service>
                  webadmin_language: <value in [auto_detect, english, simplified_chinese, ...] default: auto_detect>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> access-banner </span> - Enable/disable access banner. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> admin-https-redirect </span> - Enable/disable redirection of HTTP admin traffic to HTTPS. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> admin-login-max </span> - Maximum number admin users logged in at one time (1 - 256). <span class="li-normal">type: int</span>  <span class="li-normal">example: 256</span>  </li>
 <li> <span class="li-return"> admin_server_cert </span> - HTTPS & Web Service server certificate. <span class="li-normal">type: str</span>  <span class="li-normal">example: server.crt</span>  </li>
 <li> <span class="li-return"> allow_register </span> - Enable/disable allowance of register an unregistered device. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> auto-update </span> - Enable/disable FortiGate automatic update. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> banner-message </span> - Banner message. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> chassis-mgmt </span> - Enable or disable chassis management. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> chassis-update-interval </span> - Chassis background update interval (4 - 1440 mins). <span class="li-normal">type: int</span>  <span class="li-normal">example: 15</span>  </li>
 <li> <span class="li-return"> device_sync_status </span> - Enable/disable device synchronization status indication. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> gui-theme </span> - Color scheme to use for the administration GUI. <span class="li-normal">type: str</span>  <span class="li-normal">example: blue</span>  </li>
 <li> <span class="li-return"> http_port </span> - HTTP port. <span class="li-normal">type: int</span>  <span class="li-normal">example: 80</span>  </li>
 <li> <span class="li-return"> https_port </span> - HTTPS port. <span class="li-normal">type: int</span>  <span class="li-normal">example: 443</span>  </li>
 <li> <span class="li-return"> idle_timeout </span> - Idle timeout (1 - 480 min). <span class="li-normal">type: int</span>  <span class="li-normal">example: 15</span>  </li>
 <li> <span class="li-return"> install-ifpolicy-only </span> - Allow install interface policy only. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> mgmt-addr </span> - IP of FortiManager used by FGFM. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mgmt-fqdn </span> - FQDN of FortiManager used by FGFM. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> objects-force-deletion </span> - Enable/disable used objects force deletion. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> offline_mode </span> - Enable/disable offline mode. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> register_passwd </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC ODA4MzI1MDExMjE4OTgxM/oYbnw5dOwHjdVIoziGMGql3I0Ddz+ewZZfbXj7YeX4ol/rqZveNL7pJsXB6fGh0Bfo+R+211AvBe4558gduEIjb2W9ApZLtp5OAzm78LkH4dyrXL9N/SySeIPG1Oh6i5wvEK4Ox22xdNQmN26CaAMZG9Jl</span>  </li>
 </ul>
 <li> <span class="li-return"> sdwan-monitor-history </span> - Enable/disable hostname display in the GUI login page. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> shell-access </span> - Enable/disable shell access. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> shell-password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC NDM0ODk3MTk5MDUyMTEzMUbHl/j5CmTEcBmvdfBvKn99O6PWsq0PdmnxFXT9hypS7GvefFaz0oVwvAJ5/jgxY3HaLJDNTuNDNZfGQBezH6DURHCF23i/UXtmSSMrrIS8g2oidOj6e593sP+BSfGpQie0tLXFnMb9Lrd4dUAgfnYZpYLh</span>  </li>
 </ul>
 <li> <span class="li-return"> show-add-multiple </span> - Show add multiple button. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> show-adom-devman </span> - Show ADOM device manager tools on GUI. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> show-checkbox-in-table </span> - Show checkboxs in tables on GUI. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> show-device-import-export </span> - Enable/disable import/export of ADOM, device, and group lists. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> show-hostname </span> - Enable/disable hostname display in the GUI login page. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> show_automatic_script </span> - Enable/disable automatic script. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> show_grouping_script </span> - Enable/disable grouping script. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> show_schedule_script </span> - Enable or disable schedule script. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> show_tcl_script </span> - Enable/disable TCL script. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> unreg_dev_opt </span> - Action to take when unregistered device connects to FortiManager. <span class="li-normal">type: str</span>  <span class="li-normal">example: add_allow_service</span>  </li>
 <li> <span class="li-return"> webadmin_language </span> - Web admin language. <span class="li-normal">type: str</span>  <span class="li-normal">example: auto_detect</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/admin/setting</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/admin/setting</span>  </li>
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



