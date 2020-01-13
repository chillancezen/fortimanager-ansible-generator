:source: fmgr_system_admin_profile_obj.py

:orphan:

.. _fmgr_system_admin_profile_obj:

fmgr_system_admin_profile_obj -- Admin profile.
+++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[delete, get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/admin/profile/{profile}`
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
 <li><span class="li-head">profile</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [delete, get]</span> - Admin profile.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Admin profile.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">adom-lock</span> - ADOM locking <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">adom-policy-packages</span> - ADOM policy packages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">adom-switch</span> - Administrator domain. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">app-filter</span> - App filter. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">assignment</span> - Assignment permission. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">change-password</span> - Enable/disable restricted user to change self password. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">config-retrieve</span> - Configuration retrieve. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">config-revert</span> - Revert Configuration from Revision History <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">consistency-check</span> - Consistency check. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">datamask</span> - Enable/disable data masking. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">datamask-custom-fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">field-category</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [log, fortiview, alert, ueba, all]</span> </li>
 </ul>
 <li><span class="li-head">field-name</span> - Field name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">field-status</span> - Field status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">field-type</span> - Field type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [string, ip, mac, email, unknown]</span>  <span class="li-normal">default: string</span> </li>
 </ul>
 <li><span class="li-head">datamask-custom-priority</span> - Prioritize custom fields. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">datamask-fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [user, srcip, srcname, srcmac, dstip, dstname, email, message, domain]</span> </li>
 </ul>
 <li><span class="li-head">datamask-key</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC MzI1Nzc3MjAyNTg1Njg0NNKOn5kCfNawE/VnDbtMpWXduJpvaREIOxBK4PNmJmqeRwgB9loHz7FqcMzTT5DrD50rb65MQrxNOiuHZ7eM/qmDuMiCMym4F4p2r819t/tQ0emIgt9MTrccrMAZN5Mv9Kmkp5KFjedrsRnbofB058Bi9VBs</span> </li>
 </ul>
 <li><span class="li-head">deploy-management</span> - Install to devices. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">description</span> - Description. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">device-ap</span> - Manage AP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">device-config</span> - Manage device configurations. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">device-forticlient</span> - Manage FortiClient. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">device-fortiswitch</span> - Manage FortiSwitch. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">device-manager</span> - Device manager. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">device-op</span> - Device add/delete/edit. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">device-policy-package-lock</span> - Device/Policy Package locking <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">device-profile</span> - Device profile permission. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">device-revision-deletion</span> - Delete device revision. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">device-wan-link-load-balance</span> - Manage WAN link load balance. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">event-management</span> - Event management. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">fgd-center-advanced</span> - FortiGuard Center Advanced. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">fgd-center-fmw-mgmt</span> - FortiGuard Center Firmware Management. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">fgd-center-licensing</span> - FortiGuard Center Licensing. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">fgd_center</span> - FortiGuard Center. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">global-policy-packages</span> - Global policy packages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">import-policy-packages</span> - Import Policy Package. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">intf-mapping</span> - Interface Mapping <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">ips-filter</span> - IPS filter. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">log-viewer</span> - Log viewer. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">policy-objects</span> - Policy objects permission. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">profileid</span> - Profile ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">read-passwd</span> - View password in clear text. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">realtime-monitor</span> - Realtime monitor. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">report-viewer</span> - Report viewer. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">scope</span> - Scope. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [global, adom]</span>  <span class="li-normal">default: global</span> </li>
 <li><span class="li-head">set-install-targets</span> - Edit installation targets. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">system-setting</span> - System setting. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">term-access</span> - Terminal access. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">type</span> - profile type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [system, restricted]</span>  <span class="li-normal">default: system</span> </li>
 <li><span class="li-head">vpn-manager</span> - VPN manager. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, read, read-write]</span>  <span class="li-normal">default: none</span> </li>
 <li><span class="li-head">web-filter</span> - Web filter. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/ADMIN/PROFILE/{PROFILE}
      fmgr_system_admin_profile_obj:
         method: <value in [set, update]>
         url_params:
            profile: <value of string>
         params:
            -
               data:
                  adom-lock: <value in [none, read, read-write] default: 'none'>
                  adom-policy-packages: <value in [none, read, read-write] default: 'none'>
                  adom-switch: <value in [none, read, read-write] default: 'none'>
                  app-filter: <value in [disable, enable] default: 'disable'>
                  assignment: <value in [none, read, read-write] default: 'none'>
                  change-password: <value in [disable, enable] default: 'disable'>
                  config-retrieve: <value in [none, read, read-write] default: 'none'>
                  config-revert: <value in [none, read, read-write] default: 'none'>
                  consistency-check: <value in [none, read, read-write] default: 'none'>
                  datamask: <value in [disable, enable] default: 'disable'>
                  datamask-custom-fields:
                    -
                        field-category:
                          - <value in [log, fortiview, alert, ...]>
                        field-name: <value of string>
                        field-status: <value in [disable, enable] default: 'enable'>
                        field-type: <value in [string, ip, mac, ...] default: 'string'>
                  datamask-custom-priority: <value in [disable, enable] default: 'disable'>
                  datamask-fields:
                    - <value in [user, srcip, srcname, ...]>
                  datamask-key:
                    - <value of string default: 'ENC MzI1Nzc3MjAyNTg1Njg0NNKOn5kCfNawE/VnDbtMpWXduJpvaREIOxBK4PNmJmqeRwgB9loH...'>
                  deploy-management: <value in [none, read, read-write] default: 'none'>
                  description: <value of string>
                  device-ap: <value in [none, read, read-write] default: 'none'>
                  device-config: <value in [none, read, read-write] default: 'none'>
                  device-forticlient: <value in [none, read, read-write] default: 'none'>
                  device-fortiswitch: <value in [none, read, read-write] default: 'none'>
                  device-manager: <value in [none, read, read-write] default: 'none'>
                  device-op: <value in [none, read, read-write] default: 'none'>
                  device-policy-package-lock: <value in [none, read, read-write] default: 'none'>
                  device-profile: <value in [none, read, read-write] default: 'none'>
                  device-revision-deletion: <value in [none, read, read-write] default: 'none'>
                  device-wan-link-load-balance: <value in [none, read, read-write] default: 'none'>
                  event-management: <value in [none, read, read-write] default: 'none'>
                  fgd-center-advanced: <value in [none, read, read-write] default: 'none'>
                  fgd-center-fmw-mgmt: <value in [none, read, read-write] default: 'none'>
                  fgd-center-licensing: <value in [none, read, read-write] default: 'none'>
                  fgd_center: <value in [none, read, read-write] default: 'none'>
                  global-policy-packages: <value in [none, read, read-write] default: 'none'>
                  import-policy-packages: <value in [none, read, read-write] default: 'none'>
                  intf-mapping: <value in [none, read, read-write] default: 'none'>
                  ips-filter: <value in [disable, enable] default: 'disable'>
                  log-viewer: <value in [none, read, read-write] default: 'none'>
                  policy-objects: <value in [none, read, read-write] default: 'none'>
                  profileid: <value of string>
                  read-passwd: <value in [none, read, read-write] default: 'none'>
                  realtime-monitor: <value in [none, read, read-write] default: 'none'>
                  report-viewer: <value in [none, read, read-write] default: 'none'>
                  scope: <value in [global, adom] default: 'global'>
                  set-install-targets: <value in [none, read, read-write] default: 'none'>
                  system-setting: <value in [none, read, read-write] default: 'none'>
                  term-access: <value in [none, read, read-write] default: 'none'>
                  type: <value in [system, restricted] default: 'system'>
                  vpn-manager: <value in [none, read, read-write] default: 'none'>
                  web-filter: <value in [disable, enable] default: 'disable'>



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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/admin/profile/{profile}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> adom-lock </span> - ADOM locking <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> adom-policy-packages </span> - ADOM policy packages. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> adom-switch </span> - Administrator domain. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> app-filter </span> - App filter. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> assignment </span> - Assignment permission. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> change-password </span> - Enable/disable restricted user to change self password. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> config-retrieve </span> - Configuration retrieve. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> config-revert </span> - Revert Configuration from Revision History <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> consistency-check </span> - Consistency check. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> datamask </span> - Enable/disable data masking. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> datamask-custom-fields </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> field-category </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> field-name </span> - Field name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> field-status </span> - Field status. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> field-type </span> - Field type. <span class="li-normal">type: str</span>  <span class="li-normal">example: string</span>  </li>
 </ul>
 <li> <span class="li-return"> datamask-custom-priority </span> - Prioritize custom fields. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> datamask-fields </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> datamask-key </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC MzI1Nzc3MjAyNTg1Njg0NNKOn5kCfNawE/VnDbtMpWXduJpvaREIOxBK4PNmJmqeRwgB9loHz7FqcMzTT5DrD50rb65MQrxNOiuHZ7eM/qmDuMiCMym4F4p2r819t/tQ0emIgt9MTrccrMAZN5Mv9Kmkp5KFjedrsRnbofB058Bi9VBs</span>  </li>
 </ul>
 <li> <span class="li-return"> deploy-management </span> - Install to devices. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> description </span> - Description. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> device-ap </span> - Manage AP. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> device-config </span> - Manage device configurations. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> device-forticlient </span> - Manage FortiClient. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> device-fortiswitch </span> - Manage FortiSwitch. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> device-manager </span> - Device manager. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> device-op </span> - Device add/delete/edit. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> device-policy-package-lock </span> - Device/Policy Package locking <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> device-profile </span> - Device profile permission. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> device-revision-deletion </span> - Delete device revision. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> device-wan-link-load-balance </span> - Manage WAN link load balance. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> event-management </span> - Event management. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> fgd-center-advanced </span> - FortiGuard Center Advanced. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> fgd-center-fmw-mgmt </span> - FortiGuard Center Firmware Management. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> fgd-center-licensing </span> - FortiGuard Center Licensing. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> fgd_center </span> - FortiGuard Center. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> global-policy-packages </span> - Global policy packages. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> import-policy-packages </span> - Import Policy Package. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> intf-mapping </span> - Interface Mapping <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> ips-filter </span> - IPS filter. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> log-viewer </span> - Log viewer. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> policy-objects </span> - Policy objects permission. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> profileid </span> - Profile ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> read-passwd </span> - View password in clear text. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> realtime-monitor </span> - Realtime monitor. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> report-viewer </span> - Report viewer. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> scope </span> - Scope. <span class="li-normal">type: str</span>  <span class="li-normal">example: global</span>  </li>
 <li> <span class="li-return"> set-install-targets </span> - Edit installation targets. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> system-setting </span> - System setting. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> term-access </span> - Terminal access. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> type </span> - profile type. <span class="li-normal">type: str</span>  <span class="li-normal">example: system</span>  </li>
 <li> <span class="li-return"> vpn-manager </span> - VPN manager. <span class="li-normal">type: str</span>  <span class="li-normal">example: none</span>  </li>
 <li> <span class="li-return"> web-filter </span> - Web filter. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/admin/profile/{profile}</span>  </li>
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



