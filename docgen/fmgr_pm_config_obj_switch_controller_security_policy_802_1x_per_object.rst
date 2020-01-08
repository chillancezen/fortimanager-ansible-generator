:source: fmgr_pm_config_obj_switch_controller_security_policy_802_1x_per_object.py

:orphan:

.. _fmgr_pm_config_obj_switch_controller_security_policy_802_1x_per_object:

fmgr_pm_config_obj_switch_controller_security_policy_802_1x_per_object -- Configure 802.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/switch-controller/security-policy/802-1X/{802-1X}`
- `/pm/config/global/obj/switch-controller/security-policy/802-1X/{802-1X}`
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
 <li><span class="li-head">802-1X</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure 802.1x MAC Authentication Bypass (MAB) policies.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">auth-fail-vlan</span> - Enable to allow limited access to clients that cannot authenticate. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auth-fail-vlan-id</span> - VLAN ID on which authentication failed. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">auth-fail-vlanid</span> - VLAN ID on which authentication failed. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">eap-passthru</span> - Enable/disable EAP pass-through mode, allowing protocols (such as LLDP) to pass through ports for more flexible authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">guest-auth-delay</span> - Guest authentication delay (1 - 900  sec, default = 30). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">guest-vlan</span> - Enable the guest VLAN feature to allow limited access to non-802. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">guest-vlan-id</span> - Guest VLAN name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">guest-vlanid</span> - Guest VLAN ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mac-auth-bypass</span> - Enable/disable MAB for this policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - Policy name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">open-auth</span> - Enable/disable open authentication for this policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">policy-type</span> - Policy type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [802.1X]</span> </li>
 <li><span class="li-head">radius-timeout-overwrite</span> - Enable to override the global RADIUS session timeout. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">security-mode</span> - Port or MAC based 802. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [802.1X, 802.1X-mac-based]</span> </li>
 <li><span class="li-head">user-group</span> - Name of user-group to assign to this MAC Authentication Bypass (MAB) policy. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure 802.1x MAC Authentication Bypass (MAB) policies.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure 802.1x MAC Authentication Bypass (MAB) policies.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/SWITCH-CONTROLLER/SECURITY-POLICY/802-1X/{802-1X}
      fmgr_pm_config_obj_switch_controller_security_policy_802_1x_per_object:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            802-1X: <value of string>
         params:
            -
               data:
                  auth-fail-vlan: <value in [disable, enable]>
                  auth-fail-vlan-id: <value of string>
                  auth-fail-vlanid: <value of integer>
                  eap-passthru: <value in [disable, enable]>
                  guest-auth-delay: <value of integer>
                  guest-vlan: <value in [disable, enable]>
                  guest-vlan-id: <value of string>
                  guest-vlanid: <value of integer>
                  mac-auth-bypass: <value in [disable, enable]>
                  name: <value of string>
                  open-auth: <value in [disable, enable]>
                  policy-type: <value in [802.1X]>
                  radius-timeout-overwrite: <value in [disable, enable]>
                  security-mode: <value in [802.1X, 802.1X-mac-based]>
                  user-group: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/SWITCH-CONTROLLER/SECURITY-POLICY/802-1X/{802-1X}
      fmgr_pm_config_obj_switch_controller_security_policy_802_1x_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            802-1X: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [clone, delete, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/switch-controller/security-policy/802-1X/{802-1X}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> auth-fail-vlan </span> - Enable to allow limited access to clients that cannot authenticate. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auth-fail-vlan-id </span> - VLAN ID on which authentication failed. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auth-fail-vlanid </span> - VLAN ID on which authentication failed. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> eap-passthru </span> - Enable/disable EAP pass-through mode, allowing protocols (such as LLDP) to pass through ports for more flexible authentication. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> guest-auth-delay </span> - Guest authentication delay (1 - 900  sec, default = 30). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> guest-vlan </span> - Enable the guest VLAN feature to allow limited access to non-802. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> guest-vlan-id </span> - Guest VLAN name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> guest-vlanid </span> - Guest VLAN ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mac-auth-bypass </span> - Enable/disable MAB for this policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Policy name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> open-auth </span> - Enable/disable open authentication for this policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> policy-type </span> - Policy type. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> radius-timeout-overwrite </span> - Enable to override the global RADIUS session timeout. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> security-mode </span> - Port or MAC based 802. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> user-group </span> - Name of user-group to assign to this MAC Authentication Bypass (MAB) policy. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/switch-controller/security-policy/802-1X/{802-1X}</span>  </li>
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



