:source: fmgr_switchcontroller_lldpprofile_obj.py

:orphan:

.. _fmgr_switchcontroller_lldpprofile_obj:

fmgr_switchcontroller_lldpprofile_obj -- Configure FortiSwitch LLDP profiles.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/switch-controller/lldp-profile/{lldp-profile}`
- `/pm/config/global/obj/switch-controller/lldp-profile/{lldp-profile}`
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
 <li><span class="li-head">lldp-profile</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure FortiSwitch LLDP profiles.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">802.1-tlvs</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [port-vlan-id]</span> </li>
 </ul>
 <li><span class="li-head">802.3-tlvs</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [max-frame-size]</span> </li>
 </ul>
 <li><span class="li-head">auto-isl</span> - Enable/disable auto inter-switch LAG. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auto-isl-hello-timer</span> - Auto inter-switch LAG hello timer duration (1 - 30 sec, default = 3). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">auto-isl-port-group</span> - Auto inter-switch LAG port group ID (0 - 9). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">auto-isl-receive-timeout</span> - Auto inter-switch LAG timeout if no response is received (3 - 90 sec, default = 9). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">custom-tlvs</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">information-string</span> - Organizationally defined information string (0 - 507 hexadecimal bytes). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - TLV name (not sent). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">oui</span> - Organizationally unique identifier (OUI), a 3-byte hexadecimal number, for this TLV. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">subtype</span> - Organizationally defined subtype (0 - 255). <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">med-network-policy</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">dscp</span> - Advertised Differentiated Services Code Point (DSCP) value, a packet header value indicating the level of service requested for traffic, such as high priority or best effort delivery. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - Policy type name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priority</span> - Advertised Layer 2 priority (0 - 7; from lowest to highest priority). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Enable or disable this TLV. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">vlan</span> - ID of VLAN to advertise, if configured on port (0 - 4094, 0 = priority tag). <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">med-tlvs</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [inventory-management, network-policy, power-management, location-identification]</span> </li>
 </ul>
 <li><span class="li-head">name</span> - Profile name. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure FortiSwitch LLDP profiles.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure FortiSwitch LLDP profiles.</li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/SWITCH-CONTROLLER/LLDP-PROFILE/{LLDP-PROFILE}
      fmgr_switchcontroller_lldpprofile_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            lldp-profile: <value of string>
         params:
            -
               data:
                  802.1-tlvs:
                    - <value in [port-vlan-id]>
                  802.3-tlvs:
                    - <value in [max-frame-size]>
                  auto-isl: <value in [disable, enable]>
                  auto-isl-hello-timer: <value of integer>
                  auto-isl-port-group: <value of integer>
                  auto-isl-receive-timeout: <value of integer>
                  custom-tlvs:
                    -
                        information-string: <value of string>
                        name: <value of string>
                        oui: <value of string>
                        subtype: <value of integer>
                  med-network-policy:
                    -
                        dscp: <value of integer>
                        name: <value of string>
                        priority: <value of integer>
                        status: <value in [disable, enable]>
                        vlan: <value of integer>
                  med-tlvs:
                    - <value in [inventory-management, network-policy, power-management, ...]>
                  name: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/SWITCH-CONTROLLER/LLDP-PROFILE/{LLDP-PROFILE}
      fmgr_switchcontroller_lldpprofile_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            lldp-profile: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/switch-controller/lldp-profile/{lldp-profile}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> 802.1-tlvs </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> 802.3-tlvs </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> auto-isl </span> - Enable/disable auto inter-switch LAG. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auto-isl-hello-timer </span> - Auto inter-switch LAG hello timer duration (1 - 30 sec, default = 3). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> auto-isl-port-group </span> - Auto inter-switch LAG port group ID (0 - 9). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> auto-isl-receive-timeout </span> - Auto inter-switch LAG timeout if no response is received (3 - 90 sec, default = 9). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> custom-tlvs </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> information-string </span> - Organizationally defined information string (0 - 507 hexadecimal bytes). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - TLV name (not sent). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> oui </span> - Organizationally unique identifier (OUI), a 3-byte hexadecimal number, for this TLV. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> subtype </span> - Organizationally defined subtype (0 - 255). <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> med-network-policy </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> dscp </span> - Advertised Differentiated Services Code Point (DSCP) value, a packet header value indicating the level of service requested for traffic, such as high priority or best effort delivery. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> name </span> - Policy type name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> priority </span> - Advertised Layer 2 priority (0 - 7; from lowest to highest priority). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> status </span> - Enable or disable this TLV. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vlan </span> - ID of VLAN to advertise, if configured on port (0 - 4094, 0 = priority tag). <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> med-tlvs </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> name </span> - Profile name. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/switch-controller/lldp-profile/{lldp-profile}</span>  </li>
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



