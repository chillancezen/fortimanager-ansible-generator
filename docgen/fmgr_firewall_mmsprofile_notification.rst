:source: fmgr_firewall_mmsprofile_notification.py

:orphan:

.. _fmgr_firewall_mmsprofile_notification:

fmgr_firewall_mmsprofile_notification -- Notification configuration.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/mms-profile/{mms-profile}/notification`
- `/pm/config/global/obj/firewall/mms-profile/{mms-profile}/notification`
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
 <li><span class="li-head">adom</span> - the domain prefix <span class="li-normal">type: str</span> <span class="li-normal"> choices: none, global, custom dom</span></li>
 <li><span class="li-head">mms-profile</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Notification configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Notification configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">alert-int</span> - Alert notification send interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">alert-int-mode</span> - Alert notification interval mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hours, minutes]</span> </li>
 <li><span class="li-head">alert-src-msisdn</span> - Specify from address for alert messages. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">alert-status</span> - Alert notification status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">bword-int</span> - Banned word notification send interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">bword-int-mode</span> - Banned word notification interval mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hours, minutes]</span> </li>
 <li><span class="li-head">bword-status</span> - Banned word notification status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">carrier-endpoint-bwl-int</span> - Carrier end point black/white list notification send interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">carrier-endpoint-bwl-int-mode</span> - Carrier end point black/white list notification interval mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hours, minutes]</span> </li>
 <li><span class="li-head">carrier-endpoint-bwl-status</span> - Carrier end point black/white list notification status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">days-allowed</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sunday, monday, tuesday, wednesday, thursday, friday, saturday]</span> </li>
 </ul>
 <li><span class="li-head">detect-server</span> - Enable/disable automatic server address determination. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dupe-int</span> - Duplicate notification send interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">dupe-int-mode</span> - Duplicate notification interval mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hours, minutes]</span> </li>
 <li><span class="li-head">dupe-status</span> - Duplicate notification status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">file-block-int</span> - File block notification send interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">file-block-int-mode</span> - File block notification interval mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hours, minutes]</span> </li>
 <li><span class="li-head">file-block-status</span> - File block notification status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">flood-int</span> - Flood notification send interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">flood-int-mode</span> - Flood notification interval mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hours, minutes]</span> </li>
 <li><span class="li-head">flood-status</span> - Flood notification status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">from-in-header</span> - Enable/disable insertion of from address in HTTP header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-checksum-int</span> - MMS checksum notification send interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mms-checksum-int-mode</span> - MMS checksum notification interval mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hours, minutes]</span> </li>
 <li><span class="li-head">mms-checksum-status</span> - MMS checksum notification status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mmsc-hostname</span> - Host name or IP address of the MMSC. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mmsc-password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">mmsc-port</span> - Port used on the MMSC for sending MMS messages (1 - 65535). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mmsc-url</span> - URL used on the MMSC for sending MMS messages. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mmsc-username</span> - User name required for authentication with the MMSC. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">msg-protocol</span> - Protocol to use for sending notification messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [mm1, mm3, mm4, mm7]</span> </li>
 <li><span class="li-head">msg-type</span> - MM7 message type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [submit-req, deliver-req]</span> </li>
 <li><span class="li-head">protocol</span> - Protocol. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rate-limit</span> - Rate limit for sending notification messages (0 - 250). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">tod-window-duration</span> - Time of day window duration. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tod-window-end</span> - Obsolete. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tod-window-start</span> - Time of day window start. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">user-domain</span> - Domain name to which the user addresses belong. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vas-id</span> - VAS identifier. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vasp-id</span> - VASP identifier. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">virus-int</span> - Virus notification send interval. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">virus-int-mode</span> - Virus notification interval mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hours, minutes]</span> </li>
 <li><span class="li-head">virus-status</span> - Virus notification status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/MMS-PROFILE/{MMS-PROFILE}/NOTIFICATION
      fmgr_firewall_mmsprofile_notification:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            mms-profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/MMS-PROFILE/{MMS-PROFILE}/NOTIFICATION
      fmgr_firewall_mmsprofile_notification:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            mms-profile: <value of string>
         params:
            -
               data:
                  alert-int: <value of integer>
                  alert-int-mode: <value in [hours, minutes]>
                  alert-src-msisdn: <value of string>
                  alert-status: <value in [disable, enable]>
                  bword-int: <value of integer>
                  bword-int-mode: <value in [hours, minutes]>
                  bword-status: <value in [disable, enable]>
                  carrier-endpoint-bwl-int: <value of integer>
                  carrier-endpoint-bwl-int-mode: <value in [hours, minutes]>
                  carrier-endpoint-bwl-status: <value in [disable, enable]>
                  days-allowed:
                    - <value in [sunday, monday, tuesday, ...]>
                  detect-server: <value in [disable, enable]>
                  dupe-int: <value of integer>
                  dupe-int-mode: <value in [hours, minutes]>
                  dupe-status: <value in [disable, enable]>
                  file-block-int: <value of integer>
                  file-block-int-mode: <value in [hours, minutes]>
                  file-block-status: <value in [disable, enable]>
                  flood-int: <value of integer>
                  flood-int-mode: <value in [hours, minutes]>
                  flood-status: <value in [disable, enable]>
                  from-in-header: <value in [disable, enable]>
                  mms-checksum-int: <value of integer>
                  mms-checksum-int-mode: <value in [hours, minutes]>
                  mms-checksum-status: <value in [disable, enable]>
                  mmsc-hostname: <value of string>
                  mmsc-password:
                    - <value of string>
                  mmsc-port: <value of integer>
                  mmsc-url: <value of string>
                  mmsc-username: <value of string>
                  msg-protocol: <value in [mm1, mm3, mm4, ...]>
                  msg-type: <value in [submit-req, deliver-req]>
                  protocol: <value of string>
                  rate-limit: <value of integer>
                  tod-window-duration: <value of string>
                  tod-window-end: <value of string>
                  tod-window-start: <value of string>
                  user-domain: <value of string>
                  vas-id: <value of string>
                  vasp-id: <value of string>
                  virus-int: <value of integer>
                  virus-int-mode: <value in [hours, minutes]>
                  virus-status: <value in [disable, enable]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> alert-int </span> - Alert notification send interval. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> alert-int-mode </span> - Alert notification interval mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> alert-src-msisdn </span> - Specify from address for alert messages. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> alert-status </span> - Alert notification status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> bword-int </span> - Banned word notification send interval. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> bword-int-mode </span> - Banned word notification interval mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> bword-status </span> - Banned word notification status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> carrier-endpoint-bwl-int </span> - Carrier end point black/white list notification send interval. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> carrier-endpoint-bwl-int-mode </span> - Carrier end point black/white list notification interval mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> carrier-endpoint-bwl-status </span> - Carrier end point black/white list notification status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> days-allowed </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> detect-server </span> - Enable/disable automatic server address determination. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dupe-int </span> - Duplicate notification send interval. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> dupe-int-mode </span> - Duplicate notification interval mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dupe-status </span> - Duplicate notification status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> file-block-int </span> - File block notification send interval. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> file-block-int-mode </span> - File block notification interval mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> file-block-status </span> - File block notification status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> flood-int </span> - Flood notification send interval. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> flood-int-mode </span> - Flood notification interval mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> flood-status </span> - Flood notification status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> from-in-header </span> - Enable/disable insertion of from address in HTTP header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mms-checksum-int </span> - MMS checksum notification send interval. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mms-checksum-int-mode </span> - MMS checksum notification interval mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mms-checksum-status </span> - MMS checksum notification status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mmsc-hostname </span> - Host name or IP address of the MMSC. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mmsc-password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> mmsc-port </span> - Port used on the MMSC for sending MMS messages (1 - 65535). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mmsc-url </span> - URL used on the MMSC for sending MMS messages. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mmsc-username </span> - User name required for authentication with the MMSC. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> msg-protocol </span> - Protocol to use for sending notification messages. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> msg-type </span> - MM7 message type. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> protocol </span> - Protocol. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rate-limit </span> - Rate limit for sending notification messages (0 - 250). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> tod-window-duration </span> - Time of day window duration. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tod-window-end </span> - Obsolete. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tod-window-start </span> - Time of day window start. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> user-domain </span> - Domain name to which the user addresses belong. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vas-id </span> - VAS identifier. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vasp-id </span> - VASP identifier. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> virus-int </span> - Virus notification send interval. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> virus-int-mode </span> - Virus notification interval mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> virus-status </span> - Virus notification status. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/mms-profile/{mms-profile}/notification</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/mms-profile/{mms-profile}/notification</span>  </li>
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



