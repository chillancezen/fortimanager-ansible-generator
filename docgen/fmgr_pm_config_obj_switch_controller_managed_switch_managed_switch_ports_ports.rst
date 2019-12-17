:source: fmgr_pm_config_obj_switch_controller_managed_switch_managed_switch_ports_ports.py

:orphan:

.. _fmgr_pm_config_obj_switch_controller_managed_switch_managed_switch_ports_ports:

fmgr_pm_config_obj_switch_controller_managed_switch_managed_switch_ports_ports -- Managed-switch port list.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/switch-controller/managed-switch/{managed-switch}/ports/{ports}`
- `/pm/config/global/obj/switch-controller/managed-switch/{managed-switch}/ports/{ports}`
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
 <li><span class="li-head">managed-switch</span> - the object name <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ports</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Managed-switch port list.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">allowed-vlans</span> - Configure switch port tagged vlans <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">allowed-vlans-all</span> - Enable/disable all defined vlans on this port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">arp-inspection-trust</span> - Trusted or untrusted dynamic ARP inspection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [untrusted, trusted]</span> </li>
 <li><span class="li-head">bundle</span> - Enable/disable Link Aggregation Group (LAG) bundling for non-FortiLink interfaces. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">description</span> - Description for port. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dhcp-snoop-option82-trust</span> - Enable/disable allowance of DHCP with option-82 on untrusted interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dhcp-snooping</span> - Trusted or untrusted DHCP-snooping interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [trusted, untrusted]</span> </li>
 <li><span class="li-head">discard-mode</span> - Configure discard mode for port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, all-untagged, all-tagged]</span> </li>
 <li><span class="li-head">edge-port</span> - Enable/disable this interface as an edge port, bridging connections between workstations and/or computers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">igmp-snooping</span> - Set IGMP snooping mode for the physical port interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">igmps-flood-reports</span> - Enable/disable flooding of IGMP reports to this interface when igmp-snooping enabled. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">igmps-flood-traffic</span> - Enable/disable flooding of IGMP snooping traffic to this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">lacp-speed</span> - end Link Aggregation Control Protocol (LACP) messages every 30 seconds (slow) or every second (fast). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [slow, fast]</span> </li>
 <li><span class="li-head">learning-limit</span> - Limit the number of dynamic MAC addresses on this Port (1 - 128, 0 = no limit, default). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">lldp-profile</span> - LLDP port TLV profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">lldp-status</span> - LLDP transmit and receive status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, rx-only, tx-only, tx-rx]</span> </li>
 <li><span class="li-head">loop-guard</span> - Enable/disable loop-guard on this interface, an STP optimization used to prevent network loops. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">loop-guard-timeout</span> - Loop-guard timeout (0 - 120 min, default = 45). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">max-bundle</span> - Maximum size of LAG bundle (1 - 24, default = 24) <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mclag</span> - Enable/disable multi-chassis link aggregation (MCLAG). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">member-withdrawal-behavior</span> - Port behavior after it withdraws because of loss of control packets. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [forward, block]</span> </li>
 <li><span class="li-head">members</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">min-bundle</span> - Minimum size of LAG bundle (1 - 24, default = 1) <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mode</span> - LACP mode: ignore and do not send control messages, or negotiate 802. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, lacp-passive, lacp-active]</span> </li>
 <li><span class="li-head">poe-pre-standard-detection</span> - Enable/disable PoE pre-standard detection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">poe-status</span> - Enable/disable PoE status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">port-name</span> - Switch port name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port-owner</span> - Switch port name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port-security-policy</span> - Switch controller authentication policy to apply to this managed switch from available options. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port-selection-criteria</span> - Algorithm for aggregate port selection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [src-mac, dst-mac, src-dst-mac, src-ip, dst-ip, src-dst-ip]</span> </li>
 <li><span class="li-head">qos-policy</span> - Switch controller QoS policy from available options. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sample-direction</span> - sFlow sample direction. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rx, tx, both]</span> </li>
 <li><span class="li-head">sflow-counter-interval</span> - sFlow sampler counter polling interval (1 - 255 sec). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sflow-sample-rate</span> - sFlow sampler sample rate (0 - 99999 p/sec). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sflow-sampler</span> - Enable/disable sFlow protocol on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">stp-bpdu-guard</span> - Enable/disable STP BPDU guard on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">stp-bpdu-guard-timeout</span> - BPDU Guard disabling protection (0 - 120 min). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">stp-root-guard</span> - Enable/disable STP root guard on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">stp-state</span> - Enable/disable Spanning Tree Protocol (STP) on this interface. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span> </li>
 <li><span class="li-head">type</span> - Interface type: physical or trunk port. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [physical, trunk]</span> </li>
 <li><span class="li-head">untagged-vlans</span> - Configure switch port untagged vlans <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vlan</span> - Assign switch ports to a VLAN. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Managed-switch port list.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Managed-switch port list.</li>
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
    - name: send request to /pm/config/obj/switch-controller/managed-switch/{managed-switch}/ports/{ports}
      fmgr_pm_config_obj_switch_controller_managed_switch_managed_switch_ports_ports:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            managed-switch: <value of string>
            ports: <value of string>
         params:
            - 
               data: 
                  allowed-vlans: <value of string>
                  allowed-vlans-all: <value in [disable, enable]>
                  arp-inspection-trust: <value in [untrusted, trusted]>
                  bundle: <value in [disable, enable]>
                  description: <value of string>
                  dhcp-snoop-option82-trust: <value in [disable, enable]>
                  dhcp-snooping: <value in [trusted, untrusted]>
                  discard-mode: <value in [none, all-untagged, all-tagged]>
                  edge-port: <value in [disable, enable]>
                  igmp-snooping: <value in [disable, enable]>
                  igmps-flood-reports: <value in [disable, enable]>
                  igmps-flood-traffic: <value in [disable, enable]>
                  lacp-speed: <value in [slow, fast]>
                  learning-limit: <value of integer>
                  lldp-profile: <value of string>
                  lldp-status: <value in [disable, rx-only, tx-only, ...]>
                  loop-guard: <value in [disabled, enabled]>
                  loop-guard-timeout: <value of integer>
                  max-bundle: <value of integer>
                  mclag: <value in [disable, enable]>
                  member-withdrawal-behavior: <value in [forward, block]>
                  members: 
                   - <value of string>
                  min-bundle: <value of integer>
                  mode: <value in [static, lacp-passive, lacp-active]>
                  poe-pre-standard-detection: <value in [disable, enable]>
                  poe-status: <value in [disable, enable]>
                  port-name: <value of string>
                  port-owner: <value of string>
                  port-security-policy: <value of string>
                  port-selection-criteria: <value in [src-mac, dst-mac, src-dst-mac, ...]>
                  qos-policy: <value of string>
                  sample-direction: <value in [rx, tx, both]>
                  sflow-counter-interval: <value of integer>
                  sflow-sample-rate: <value of integer>
                  sflow-sampler: <value in [disabled, enabled]>
                  stp-bpdu-guard: <value in [disabled, enabled]>
                  stp-bpdu-guard-timeout: <value of integer>
                  stp-root-guard: <value in [disabled, enabled]>
                  stp-state: <value in [disabled, enabled]>
                  type: <value in [physical, trunk]>
                  untagged-vlans: <value of string>
                  vlan: <value of string>
    - name: send request to /pm/config/obj/switch-controller/managed-switch/{managed-switch}/ports/{ports}
      fmgr_pm_config_obj_switch_controller_managed_switch_managed_switch_ports_ports:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            managed-switch: <value of string>
            ports: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/switch-controller/managed-switch/{managed-switch}/ports/{ports}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> allowed-vlans </span> - Configure switch port tagged vlans <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> allowed-vlans-all </span> - Enable/disable all defined vlans on this port. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> arp-inspection-trust </span> - Trusted or untrusted dynamic ARP inspection. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> bundle </span> - Enable/disable Link Aggregation Group (LAG) bundling for non-FortiLink interfaces. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> description </span> - Description for port. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dhcp-snoop-option82-trust </span> - Enable/disable allowance of DHCP with option-82 on untrusted interface. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dhcp-snooping </span> - Trusted or untrusted DHCP-snooping interface. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> discard-mode </span> - Configure discard mode for port. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> edge-port </span> - Enable/disable this interface as an edge port, bridging connections between workstations and/or computers. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> igmp-snooping </span> - Set IGMP snooping mode for the physical port interface. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> igmps-flood-reports </span> - Enable/disable flooding of IGMP reports to this interface when igmp-snooping enabled. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> igmps-flood-traffic </span> - Enable/disable flooding of IGMP snooping traffic to this interface. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> lacp-speed </span> - end Link Aggregation Control Protocol (LACP) messages every 30 seconds (slow) or every second (fast). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> learning-limit </span> - Limit the number of dynamic MAC addresses on this Port (1 - 128, 0 = no limit, default). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> lldp-profile </span> - LLDP port TLV profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> lldp-status </span> - LLDP transmit and receive status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> loop-guard </span> - Enable/disable loop-guard on this interface, an STP optimization used to prevent network loops. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> loop-guard-timeout </span> - Loop-guard timeout (0 - 120 min, default = 45). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> max-bundle </span> - Maximum size of LAG bundle (1 - 24, default = 24) <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mclag </span> - Enable/disable multi-chassis link aggregation (MCLAG). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> member-withdrawal-behavior </span> - Port behavior after it withdraws because of loss of control packets. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> members </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> min-bundle </span> - Minimum size of LAG bundle (1 - 24, default = 1) <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mode </span> - LACP mode: ignore and do not send control messages, or negotiate 802. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> poe-pre-standard-detection </span> - Enable/disable PoE pre-standard detection. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> poe-status </span> - Enable/disable PoE status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port-name </span> - Switch port name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port-owner </span> - Switch port name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port-security-policy </span> - Switch controller authentication policy to apply to this managed switch from available options. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port-selection-criteria </span> - Algorithm for aggregate port selection. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> qos-policy </span> - Switch controller QoS policy from available options. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sample-direction </span> - sFlow sample direction. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sflow-counter-interval </span> - sFlow sampler counter polling interval (1 - 255 sec). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> sflow-sample-rate </span> - sFlow sampler sample rate (0 - 99999 p/sec). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> sflow-sampler </span> - Enable/disable sFlow protocol on this interface. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> stp-bpdu-guard </span> - Enable/disable STP BPDU guard on this interface. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> stp-bpdu-guard-timeout </span> - BPDU Guard disabling protection (0 - 120 min). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> stp-root-guard </span> - Enable/disable STP root guard on this interface. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> stp-state </span> - Enable/disable Spanning Tree Protocol (STP) on this interface. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - Interface type: physical or trunk port. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> untagged-vlans </span> - Configure switch port untagged vlans <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vlan </span> - Assign switch ports to a VLAN. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/switch-controller/managed-switch/{managed-switch}/ports/{ports}</span>  </li>
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



