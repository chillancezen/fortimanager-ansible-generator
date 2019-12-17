:source: fmgr_pm_config_pkg_pkg_firewall_interface_policy_interface_policy.py

:orphan:

.. _fmgr_pm_config_pkg_pkg_firewall_interface_policy_interface_policy:

fmgr_pm_config_pkg_pkg_firewall_interface_policy_interface_policy -- Configure IPv4 interface policies.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, move, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/pkg/{pkg}/firewall/interface-policy/{interface-policy}`
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
 <li><span class="li-head">pkg</span> - the object name <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">interface-policy</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, update]</span> - Configure IPv4 interface policies.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">address-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipv4, ipv6]</span> </li>
 <li><span class="li-head">application-list</span> - Application list name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">application-list-status</span> - Enable/disable application control. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">av-profile</span> - Antivirus profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">av-profile-status</span> - Enable/disable antivirus. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">comments</span> - Comments. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dlp-sensor</span> - DLP sensor name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dlp-sensor-status</span> - Enable/disable DLP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dsri</span> - Enable/disable DSRI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dstaddr</span> - Address object to limit traffic monitoring to network traffic sent to the specified address or range. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">interface</span> - Monitored interface name from available interfaces. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ips-sensor</span> - IPS sensor name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ips-sensor-status</span> - Enable/disable IPS. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">label</span> - Label. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">logtraffic</span> - Logging type to be used in this policy (Options: all | utm | disable, Default: utm). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, all, utm]</span> </li>
 <li><span class="li-head">policyid</span> - Policy ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">scan-botnet-connections</span> - Enable/disable scanning for connections to Botnet servers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, block, monitor]</span> </li>
 <li><span class="li-head">service</span> - Service object from available options. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spamfilter-profile</span> - Antispam profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spamfilter-profile-status</span> - Enable/disable antispam. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">srcaddr</span> - Address object to limit traffic monitoring to network traffic sent from the specified address or range. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable this policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">webfilter-profile</span> - Web filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">webfilter-profile-status</span> - Enable/disable web filtering. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure IPv4 interface policies.</li>
 <ul class="ul-self">
 <ul class="ul-self">
 <li><span class="li-head">parameter collection 0</span></li>
 <ul class="ul-self">
 </ul>
 </ul>
 <ul class="ul-self">
 <li><span class="li-head">parameter collection 1</span></li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">attr</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [label, global-label]</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure IPv4 interface policies.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [move]</span> - Configure IPv4 interface policies.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [before, after]</span> </li>
 <li><span class="li-head">target</span> - Key to the target entry. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set]</span> - Configure IPv4 interface policies.</li>
 <ul class="ul-self">
 <ul class="ul-self">
 <li><span class="li-head">parameter collection 0</span></li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">address-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipv4, ipv6]</span> </li>
 <li><span class="li-head">application-list</span> - Application list name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">application-list-status</span> - Enable/disable application control. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">av-profile</span> - Antivirus profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">av-profile-status</span> - Enable/disable antivirus. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">comments</span> - Comments. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dlp-sensor</span> - DLP sensor name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dlp-sensor-status</span> - Enable/disable DLP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dsri</span> - Enable/disable DSRI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dstaddr</span> - Address object to limit traffic monitoring to network traffic sent to the specified address or range. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">interface</span> - Monitored interface name from available interfaces. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ips-sensor</span> - IPS sensor name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ips-sensor-status</span> - Enable/disable IPS. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">label</span> - Label. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">logtraffic</span> - Logging type to be used in this policy (Options: all | utm | disable, Default: utm). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, all, utm]</span> </li>
 <li><span class="li-head">policyid</span> - Policy ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">scan-botnet-connections</span> - Enable/disable scanning for connections to Botnet servers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, block, monitor]</span> </li>
 <li><span class="li-head">service</span> - Service object from available options. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spamfilter-profile</span> - Antispam profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">spamfilter-profile-status</span> - Enable/disable antispam. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">srcaddr</span> - Address object to limit traffic monitoring to network traffic sent from the specified address or range. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable this policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">webfilter-profile</span> - Web filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">webfilter-profile-status</span> - Enable/disable web filtering. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 </ul>
 <ul class="ul-self">
 <li><span class="li-head">parameter collection 1</span></li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">attr</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [label, global-label]</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
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
    - name: send request to /pm/config/pkg/{pkg}/firewall/interface-policy/{interface-policy}
      fmgr_pm_config_pkg_pkg_firewall_interface_policy_interface_policy:
         method: <value in [clone, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            interface-policy: <value of string>
         params:
            - 
               data: 
                  address-type: <value in [ipv4, ipv6]>
                  application-list: <value of string>
                  application-list-status: <value in [disable, enable]>
                  av-profile: <value of string>
                  av-profile-status: <value in [disable, enable]>
                  comments: <value of string>
                  dlp-sensor: <value of string>
                  dlp-sensor-status: <value in [disable, enable]>
                  dsri: <value in [disable, enable]>
                  dstaddr: <value of string>
                  interface: <value of string>
                  ips-sensor: <value of string>
                  ips-sensor-status: <value in [disable, enable]>
                  label: <value of string>
                  logtraffic: <value in [disable, all, utm]>
                  policyid: <value of integer>
                  scan-botnet-connections: <value in [disable, block, monitor]>
                  service: <value of string>
                  spamfilter-profile: <value of string>
                  spamfilter-profile-status: <value in [disable, enable]>
                  srcaddr: <value of string>
                  status: <value in [disable, enable]>
                  webfilter-profile: <value of string>
                  webfilter-profile-status: <value in [disable, enable]>
    - name: send request to /pm/config/pkg/{pkg}/firewall/interface-policy/{interface-policy}
      fmgr_pm_config_pkg_pkg_firewall_interface_policy_interface_policy:
         method: <value in [delete]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            interface-policy: <value of string>
         params:
            - 
               data: 
                  attr: <value in [label, global-label]>
                  name: <value of string>
    - name: send request to /pm/config/pkg/{pkg}/firewall/interface-policy/{interface-policy}
      fmgr_pm_config_pkg_pkg_firewall_interface_policy_interface_policy:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            interface-policy: <value of string>
         params:
            - 
               option: <value in [object member, chksum, datasrc]>
    - name: send request to /pm/config/pkg/{pkg}/firewall/interface-policy/{interface-policy}
      fmgr_pm_config_pkg_pkg_firewall_interface_policy_interface_policy:
         method: <value in [move]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            interface-policy: <value of string>
         params:
            - 
               option: <value in [before, after]>
               target: <value of string>
    - name: send request to /pm/config/pkg/{pkg}/firewall/interface-policy/{interface-policy}
      fmgr_pm_config_pkg_pkg_firewall_interface_policy_interface_policy:
         method: <value in [set]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            interface-policy: <value of string>
         params:
            - 
               data: 
                  address-type: <value in [ipv4, ipv6]>
                  application-list: <value of string>
                  application-list-status: <value in [disable, enable]>
                  av-profile: <value of string>
                  av-profile-status: <value in [disable, enable]>
                  comments: <value of string>
                  dlp-sensor: <value of string>
                  dlp-sensor-status: <value in [disable, enable]>
                  dsri: <value in [disable, enable]>
                  dstaddr: <value of string>
                  interface: <value of string>
                  ips-sensor: <value of string>
                  ips-sensor-status: <value in [disable, enable]>
                  label: <value of string>
                  logtraffic: <value in [disable, all, utm]>
                  policyid: <value of integer>
                  scan-botnet-connections: <value in [disable, block, monitor]>
                  service: <value of string>
                  spamfilter-profile: <value of string>
                  spamfilter-profile-status: <value in [disable, enable]>
                  srcaddr: <value of string>
                  status: <value in [disable, enable]>
                  webfilter-profile: <value of string>
                  webfilter-profile-status: <value in [disable, enable]>
    - name: send request to /pm/config/pkg/{pkg}/firewall/interface-policy/{interface-policy}
      fmgr_pm_config_pkg_pkg_firewall_interface_policy_interface_policy:
         method: <value in [set]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            interface-policy: <value of string>
         params:
            - 
               data: 
                  attr: <value in [label, global-label]>
                  name: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [clone, move, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> policyid </span> - Policy ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/interface-policy/{interface-policy}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [delete]</span> </li>
 <ul class="ul-self">
 <ul class="ul-self">
 <li><span class="li-return">return values collection 0</span></li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/interface-policy/{interface-policy}</span>  </li>
 </ul>
 </ul>
 <ul class="ul-self">
 <li><span class="li-return">return values collection 1</span></li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/interface-policy/{interface-policy}</span>  </li>
 </ul>
 </ul>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> address-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> application-list </span> - Application list name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> application-list-status </span> - Enable/disable application control. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> av-profile </span> - Antivirus profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> av-profile-status </span> - Enable/disable antivirus. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> comments </span> - Comments. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dlp-sensor </span> - DLP sensor name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dlp-sensor-status </span> - Enable/disable DLP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dsri </span> - Enable/disable DSRI. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstaddr </span> - Address object to limit traffic monitoring to network traffic sent to the specified address or range. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> interface </span> - Monitored interface name from available interfaces. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ips-sensor </span> - IPS sensor name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ips-sensor-status </span> - Enable/disable IPS. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> label </span> - Label. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> logtraffic </span> - Logging type to be used in this policy (Options: all | utm | disable, Default: utm). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> policyid </span> - Policy ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> scan-botnet-connections </span> - Enable/disable scanning for connections to Botnet servers. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> service </span> - Service object from available options. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spamfilter-profile </span> - Antispam profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spamfilter-profile-status </span> - Enable/disable antispam. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcaddr </span> - Address object to limit traffic monitoring to network traffic sent from the specified address or range. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable this policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webfilter-profile </span> - Web filter profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webfilter-profile-status </span> - Enable/disable web filtering. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/interface-policy/{interface-policy}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set]</span> </li>
 <ul class="ul-self">
 <ul class="ul-self">
 <li><span class="li-return">return values collection 0</span></li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> policyid </span> - Policy ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/interface-policy/{interface-policy}</span>  </li>
 </ul>
 </ul>
 <ul class="ul-self">
 <li><span class="li-return">return values collection 1</span></li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/interface-policy/{interface-policy}</span>  </li>
 </ul>
 </ul>
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



