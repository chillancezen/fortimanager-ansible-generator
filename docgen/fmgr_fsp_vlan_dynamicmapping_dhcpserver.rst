:source: fmgr_fsp_vlan_dynamicmapping_dhcpserver.py

:orphan:

.. _fmgr_fsp_vlan_dynamicmapping_dhcpserver:

fmgr_fsp_vlan_dynamicmapping_dhcpserver
+++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/dynamic_mapping/{dynamic_mapping}/dhcp-server`
- `/pm/config/global/obj/fsp/vlan/{vlan}/dynamic_mapping/{dynamic_mapping}/dhcp-server`
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
 <li><span class="li-head">vlan</span> - the object name <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dynamic_mapping</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">auto-configuration</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">conflicted-ip-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ddns-auth</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, tsig]</span> </li>
 <li><span class="li-head">ddns-key</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ddns-keyname</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ddns-server-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ddns-ttl</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ddns-update</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ddns-update-override</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ddns-zone</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">default-gateway</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-server1</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-server2</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-server3</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dns-service</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, specify, local]</span> </li>
 <li><span class="li-head">domain</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">enable</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">exclude-range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">end-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">start-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">filename</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">forticlient-on-net-status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [range, usrgrp]</span> </li>
 <li><span class="li-head">ip-range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">end-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">start-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ipsec-lease-hold</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">lease-time</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mac-acl-default-action</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [assign, block]</span> </li>
 <li><span class="li-head">netmask</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">next-server</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ntp-server1</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ntp-server2</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ntp-server3</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ntp-service</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, specify, local]</span> </li>
 <li><span class="li-head">option1</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">option2</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">option3</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">option4</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">option5</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">option6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">code</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hex, string, ip, fqdn]</span> </li>
 <li><span class="li-head">value</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">reserved-address</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [assign, block, reserved]</span> </li>
 <li><span class="li-head">circuit-id</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">circuit-id-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hex, string]</span> </li>
 <li><span class="li-head">description</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mac</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">remote-id</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">remote-id-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [hex, string]</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [mac, option82]</span> </li>
 </ul>
 <li><span class="li-head">server-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [regular, ipsec]</span> </li>
 <li><span class="li-head">status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tftp-server</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">timezone</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]</span> </li>
 <li><span class="li-head">timezone-option</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, default, specify]</span> </li>
 <li><span class="li-head">vci-match</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">vci-string</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">wifi-ac1</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wifi-ac2</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wifi-ac3</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wins-server1</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wins-server2</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FSP/VLAN/{VLAN}/DYNAMIC_MAPPING/{DYNAMIC_MAPPING}/DHCP-SERVER
      fmgr_fsp_vlan_dynamicmapping_dhcpserver:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vlan: <value of string>
            dynamic_mapping: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/FSP/VLAN/{VLAN}/DYNAMIC_MAPPING/{DYNAMIC_MAPPING}/DHCP-SERVER
      fmgr_fsp_vlan_dynamicmapping_dhcpserver:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vlan: <value of string>
            dynamic_mapping: <value of string>
         params:
            -
               data:
                  auto-configuration: <value in [disable, enable]>
                  conflicted-ip-timeout: <value of integer>
                  ddns-auth: <value in [disable, tsig]>
                  ddns-key: <value of string>
                  ddns-keyname: <value of string>
                  ddns-server-ip: <value of string>
                  ddns-ttl: <value of integer>
                  ddns-update: <value in [disable, enable]>
                  ddns-update-override: <value in [disable, enable]>
                  ddns-zone: <value of string>
                  default-gateway: <value of string>
                  dns-server1: <value of string>
                  dns-server2: <value of string>
                  dns-server3: <value of string>
                  dns-service: <value in [default, specify, local]>
                  domain: <value of string>
                  enable: <value in [disable, enable]>
                  exclude-range:
                    -
                        end-ip: <value of string>
                        id: <value of integer>
                        start-ip: <value of string>
                  filename: <value of string>
                  forticlient-on-net-status: <value in [disable, enable]>
                  id: <value of integer>
                  interface: <value of string>
                  ip-mode: <value in [range, usrgrp]>
                  ip-range:
                    -
                        end-ip: <value of string>
                        id: <value of integer>
                        start-ip: <value of string>
                  ipsec-lease-hold: <value of integer>
                  lease-time: <value of integer>
                  mac-acl-default-action: <value in [assign, block]>
                  netmask: <value of string>
                  next-server: <value of string>
                  ntp-server1: <value of string>
                  ntp-server2: <value of string>
                  ntp-server3: <value of string>
                  ntp-service: <value in [default, specify, local]>
                  option1:
                    - <value of string>
                  option2:
                    - <value of string>
                  option3:
                    - <value of string>
                  option4: <value of string>
                  option5: <value of string>
                  option6: <value of string>
                  options:
                    -
                        code: <value of integer>
                        id: <value of integer>
                        ip:
                          - <value of string>
                        type: <value in [hex, string, ip, ...]>
                        value: <value of string>
                  reserved-address:
                    -
                        action: <value in [assign, block, reserved]>
                        circuit-id: <value of string>
                        circuit-id-type: <value in [hex, string]>
                        description: <value of string>
                        id: <value of integer>
                        ip: <value of string>
                        mac: <value of string>
                        remote-id: <value of string>
                        remote-id-type: <value in [hex, string]>
                        type: <value in [mac, option82]>
                  server-type: <value in [regular, ipsec]>
                  status: <value in [disable, enable]>
                  tftp-server:
                    - <value of string>
                  timezone: <value in [00, 01, 02, ...]>
                  timezone-option: <value in [disable, default, specify]>
                  vci-match: <value in [disable, enable]>
                  vci-string:
                    - <value of string>
                  wifi-ac1: <value of string>
                  wifi-ac2: <value of string>
                  wifi-ac3: <value of string>
                  wins-server1: <value of string>
                  wins-server2: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> auto-configuration </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> conflicted-ip-timeout </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ddns-auth </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ddns-key </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ddns-keyname </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ddns-server-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ddns-ttl </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ddns-update </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ddns-update-override </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ddns-zone </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> default-gateway </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dns-server1 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dns-server2 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dns-server3 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dns-service </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> domain </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> enable </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> exclude-range </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> end-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> start-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> filename </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> forticlient-on-net-status </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> interface </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip-mode </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip-range </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> end-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> start-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ipsec-lease-hold </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> lease-time </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mac-acl-default-action </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> netmask </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> next-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ntp-server1 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ntp-server2 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ntp-server3 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ntp-service </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> option1 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> option2 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> option3 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> option4 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> option5 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> option6 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> options </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> value </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> reserved-address </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> circuit-id </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> circuit-id-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> description </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mac </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> remote-id </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> remote-id-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> server-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tftp-server </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> timezone </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> timezone-option </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vci-match </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vci-string </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> wifi-ac1 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wifi-ac2 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wifi-ac3 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wins-server1 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wins-server2 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/dynamic_mapping/{dynamic_mapping}/dhcp-server</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/fsp/vlan/{vlan}/dynamic_mapping/{dynamic_mapping}/dhcp-server</span>  </li>
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



