:source: fmgr_pkg_firewall_proxypolicy_obj.py

:orphan:

.. _fmgr_pkg_firewall_proxypolicy_obj:

fmgr_pkg_firewall_proxypolicy_obj -- Configure proxy policies.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, move, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/pkg/{pkg}/firewall/proxy-policy/{proxy-policy}`
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
 <li><span class="li-head">proxy-policy</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, update]</span> - Configure proxy policies.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Accept or deny traffic matching the policy parameters. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [accept, deny, redirect]</span> </li>
 <li><span class="li-head">application-list</span> - Name of an existing Application list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">av-profile</span> - Name of an existing Antivirus profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">comments</span> - Optional comments. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">disclaimer</span> - Web proxy disclaimer setting: by domain, policy, or user. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, domain, policy, user]</span> </li>
 <li><span class="li-head">dlp-sensor</span> - Name of an existing DLP sensor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr</span> - Destination address objects. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr-negate</span> - When enabled, destination addresses match against any address EXCEPT the specified destination addresses. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dstaddr6</span> - IPv6 destination address objects. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstintf</span> - Destination interface names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">global-label</span> - Global web-based manager visible label. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">groups</span> - Names of group objects. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-tunnel-auth</span> - Enable/disable HTTP tunnel authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">icap-profile</span> - Name of an existing ICAP profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service</span> - Enable/disable use of Internet Services for this policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">internet-service-custom</span> - Custom Internet Service name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-id</span> - Internet Service ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-negate</span> - When enabled, Internet Services match against any internet service EXCEPT the selected Internet Service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ips-sensor</span> - Name of an existing IPS sensor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">label</span> - VDOM-specific GUI visible label. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">logtraffic</span> - Enable/disable logging traffic through the policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, all, utm]</span> </li>
 <li><span class="li-head">logtraffic-start</span> - Enable/disable policy log traffic start. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-profile</span> - Name of an existing MMS profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">policyid</span> - Policy ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">poolname</span> - Name of IP pool object. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-group</span> - Name of profile group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-protocol-options</span> - Name of an existing Protocol options profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-type</span> - Determine whether the firewall policy allows security profile groups or single profiles only. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [single, group]</span> </li>
 <li><span class="li-head">proxy</span> - Type of explicit proxy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [explicit-web, transparent-web, ftp, wanopt, ssh, ssh-tunnel]</span> </li>
 <li><span class="li-head">redirect-url</span> - Redirect URL for further explicit web proxy processing. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">replacemsg-override-group</span> - Authentication replacement message override group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">scan-botnet-connections</span> - Enable/disable scanning of connections to Botnet servers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, block, monitor]</span> </li>
 <li><span class="li-head">schedule</span> - Name of schedule object. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service</span> - Name of service objects. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service-negate</span> - When enabled, services match against any service EXCEPT the specified destination services. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">spamfilter-profile</span> - Name of an existing Spam filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr</span> - Source address objects (must be set when using Web proxy). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr-negate</span> - When enabled, source addresses match against any address EXCEPT the specified source addresses. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">srcaddr6</span> - IPv6 source address objects. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcintf</span> - Source interface names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-ssh-profile</span> - Name of an existing SSL SSH profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the active status of the policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tags</span> - Names of object-tags applied to address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">transparent</span> - Enable to use the IP address of the client to connect to the server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">users</span> - Names of user objects. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">utm-status</span> - Enable the use of UTM profiles/sensors/lists. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">uuid</span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">waf-profile</span> - Name of an existing Web application firewall profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">webcache</span> - Enable/disable web caching. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">webcache-https</span> - Enable/disable web caching for HTTPS (Requires deep-inspection enabled in ssl-ssh-profile). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">webfilter-profile</span> - Name of an existing Web filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">webproxy-forward-server</span> - Name of web proxy forward server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">webproxy-profile</span> - Name of web proxy profile. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure proxy policies.</li>
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
 <li><span class="li-head">parameters for method: [get]</span> - Configure proxy policies.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [move]</span> - Configure proxy policies.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [before, after]</span> </li>
 <li><span class="li-head">target</span> - Key to the target entry. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set]</span> - Configure proxy policies.</li>
 <ul class="ul-self">
 <ul class="ul-self">
 <li><span class="li-head">parameter collection 0</span></li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Accept or deny traffic matching the policy parameters. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [accept, deny, redirect]</span> </li>
 <li><span class="li-head">application-list</span> - Name of an existing Application list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">av-profile</span> - Name of an existing Antivirus profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">comments</span> - Optional comments. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">disclaimer</span> - Web proxy disclaimer setting: by domain, policy, or user. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, domain, policy, user]</span> </li>
 <li><span class="li-head">dlp-sensor</span> - Name of an existing DLP sensor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr</span> - Destination address objects. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr-negate</span> - When enabled, destination addresses match against any address EXCEPT the specified destination addresses. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">dstaddr6</span> - IPv6 destination address objects. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstintf</span> - Destination interface names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">global-label</span> - Global web-based manager visible label. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">groups</span> - Names of group objects. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-tunnel-auth</span> - Enable/disable HTTP tunnel authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">icap-profile</span> - Name of an existing ICAP profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service</span> - Enable/disable use of Internet Services for this policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">internet-service-custom</span> - Custom Internet Service name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-id</span> - Internet Service ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-negate</span> - When enabled, Internet Services match against any internet service EXCEPT the selected Internet Service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ips-sensor</span> - Name of an existing IPS sensor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">label</span> - VDOM-specific GUI visible label. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">logtraffic</span> - Enable/disable logging traffic through the policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, all, utm]</span> </li>
 <li><span class="li-head">logtraffic-start</span> - Enable/disable policy log traffic start. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-profile</span> - Name of an existing MMS profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">policyid</span> - Policy ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">poolname</span> - Name of IP pool object. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-group</span> - Name of profile group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-protocol-options</span> - Name of an existing Protocol options profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-type</span> - Determine whether the firewall policy allows security profile groups or single profiles only. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [single, group]</span> </li>
 <li><span class="li-head">proxy</span> - Type of explicit proxy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [explicit-web, transparent-web, ftp, wanopt, ssh, ssh-tunnel]</span> </li>
 <li><span class="li-head">redirect-url</span> - Redirect URL for further explicit web proxy processing. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">replacemsg-override-group</span> - Authentication replacement message override group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">scan-botnet-connections</span> - Enable/disable scanning of connections to Botnet servers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, block, monitor]</span> </li>
 <li><span class="li-head">schedule</span> - Name of schedule object. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service</span> - Name of service objects. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service-negate</span> - When enabled, services match against any service EXCEPT the specified destination services. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">spamfilter-profile</span> - Name of an existing Spam filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr</span> - Source address objects (must be set when using Web proxy). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr-negate</span> - When enabled, source addresses match against any address EXCEPT the specified source addresses. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">srcaddr6</span> - IPv6 source address objects. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcintf</span> - Source interface names. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-ssh-profile</span> - Name of an existing SSL SSH profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the active status of the policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tags</span> - Names of object-tags applied to address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">transparent</span> - Enable to use the IP address of the client to connect to the server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">users</span> - Names of user objects. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">utm-status</span> - Enable the use of UTM profiles/sensors/lists. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">uuid</span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">waf-profile</span> - Name of an existing Web application firewall profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">webcache</span> - Enable/disable web caching. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">webcache-https</span> - Enable/disable web caching for HTTPS (Requires deep-inspection enabled in ssl-ssh-profile). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">webfilter-profile</span> - Name of an existing Web filter profile. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">webproxy-forward-server</span> - Name of web proxy forward server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">webproxy-profile</span> - Name of web proxy profile. <span class="li-normal">type: str</span> </li>
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

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/PROXY-POLICY/{PROXY-POLICY}
      fmgr_pkg_firewall_proxypolicy_obj:
         method: <value in [clone, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            proxy-policy: <value of string>
         params:
            -
               data:
                  action: <value in [accept, deny, redirect]>
                  application-list: <value of string>
                  av-profile: <value of string>
                  comments: <value of string>
                  disclaimer: <value in [disable, domain, policy, ...]>
                  dlp-sensor: <value of string>
                  dstaddr: <value of string>
                  dstaddr-negate: <value in [disable, enable]>
                  dstaddr6: <value of string>
                  dstintf: <value of string>
                  global-label: <value of string>
                  groups: <value of string>
                  http-tunnel-auth: <value in [disable, enable]>
                  icap-profile: <value of string>
                  internet-service: <value in [disable, enable]>
                  internet-service-custom: <value of string>
                  internet-service-id: <value of string>
                  internet-service-negate: <value in [disable, enable]>
                  ips-sensor: <value of string>
                  label: <value of string>
                  logtraffic: <value in [disable, all, utm]>
                  logtraffic-start: <value in [disable, enable]>
                  mms-profile: <value of string>
                  policyid: <value of integer>
                  poolname: <value of string>
                  profile-group: <value of string>
                  profile-protocol-options: <value of string>
                  profile-type: <value in [single, group]>
                  proxy: <value in [explicit-web, transparent-web, ftp, ...]>
                  redirect-url: <value of string>
                  replacemsg-override-group: <value of string>
                  scan-botnet-connections: <value in [disable, block, monitor]>
                  schedule: <value of string>
                  service: <value of string>
                  service-negate: <value in [disable, enable]>
                  spamfilter-profile: <value of string>
                  srcaddr: <value of string>
                  srcaddr-negate: <value in [disable, enable]>
                  srcaddr6: <value of string>
                  srcintf: <value of string>
                  ssl-ssh-profile: <value of string>
                  status: <value in [disable, enable]>
                  tags: <value of string>
                  transparent: <value in [disable, enable]>
                  users: <value of string>
                  utm-status: <value in [disable, enable]>
                  uuid: <value of string>
                  waf-profile: <value of string>
                  webcache: <value in [disable, enable]>
                  webcache-https: <value in [disable, enable]>
                  webfilter-profile: <value of string>
                  webproxy-forward-server: <value of string>
                  webproxy-profile: <value of string>

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/PROXY-POLICY/{PROXY-POLICY}
      fmgr_pkg_firewall_proxypolicy_obj:
         method: <value in [delete]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            proxy-policy: <value of string>
         params:
            -
               data:
                  attr: <value in [label, global-label]>
                  name: <value of string>

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/PROXY-POLICY/{PROXY-POLICY}
      fmgr_pkg_firewall_proxypolicy_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            proxy-policy: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/PROXY-POLICY/{PROXY-POLICY}
      fmgr_pkg_firewall_proxypolicy_obj:
         method: <value in [move]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            proxy-policy: <value of string>
         params:
            -
               option: <value in [before, after]>
               target: <value of string>

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/PROXY-POLICY/{PROXY-POLICY}
      fmgr_pkg_firewall_proxypolicy_obj:
         method: <value in [set]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            proxy-policy: <value of string>
         params:
            -
               data:
                  action: <value in [accept, deny, redirect]>
                  application-list: <value of string>
                  av-profile: <value of string>
                  comments: <value of string>
                  disclaimer: <value in [disable, domain, policy, ...]>
                  dlp-sensor: <value of string>
                  dstaddr: <value of string>
                  dstaddr-negate: <value in [disable, enable]>
                  dstaddr6: <value of string>
                  dstintf: <value of string>
                  global-label: <value of string>
                  groups: <value of string>
                  http-tunnel-auth: <value in [disable, enable]>
                  icap-profile: <value of string>
                  internet-service: <value in [disable, enable]>
                  internet-service-custom: <value of string>
                  internet-service-id: <value of string>
                  internet-service-negate: <value in [disable, enable]>
                  ips-sensor: <value of string>
                  label: <value of string>
                  logtraffic: <value in [disable, all, utm]>
                  logtraffic-start: <value in [disable, enable]>
                  mms-profile: <value of string>
                  policyid: <value of integer>
                  poolname: <value of string>
                  profile-group: <value of string>
                  profile-protocol-options: <value of string>
                  profile-type: <value in [single, group]>
                  proxy: <value in [explicit-web, transparent-web, ftp, ...]>
                  redirect-url: <value of string>
                  replacemsg-override-group: <value of string>
                  scan-botnet-connections: <value in [disable, block, monitor]>
                  schedule: <value of string>
                  service: <value of string>
                  service-negate: <value in [disable, enable]>
                  spamfilter-profile: <value of string>
                  srcaddr: <value of string>
                  srcaddr-negate: <value in [disable, enable]>
                  srcaddr6: <value of string>
                  srcintf: <value of string>
                  ssl-ssh-profile: <value of string>
                  status: <value in [disable, enable]>
                  tags: <value of string>
                  transparent: <value in [disable, enable]>
                  users: <value of string>
                  utm-status: <value in [disable, enable]>
                  uuid: <value of string>
                  waf-profile: <value of string>
                  webcache: <value in [disable, enable]>
                  webcache-https: <value in [disable, enable]>
                  webfilter-profile: <value of string>
                  webproxy-forward-server: <value of string>
                  webproxy-profile: <value of string>

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/PROXY-POLICY/{PROXY-POLICY}
      fmgr_pkg_firewall_proxypolicy_obj:
         method: <value in [set]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            proxy-policy: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/proxy-policy/{proxy-policy}</span>  </li>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/proxy-policy/{proxy-policy}</span>  </li>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/proxy-policy/{proxy-policy}</span>  </li>
 </ul>
 </ul>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - Accept or deny traffic matching the policy parameters. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> application-list </span> - Name of an existing Application list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> av-profile </span> - Name of an existing Antivirus profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> comments </span> - Optional comments. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> disclaimer </span> - Web proxy disclaimer setting: by domain, policy, or user. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dlp-sensor </span> - Name of an existing DLP sensor. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstaddr </span> - Destination address objects. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstaddr-negate </span> - When enabled, destination addresses match against any address EXCEPT the specified destination addresses. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstaddr6 </span> - IPv6 destination address objects. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstintf </span> - Destination interface names. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> global-label </span> - Global web-based manager visible label. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> groups </span> - Names of group objects. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-tunnel-auth </span> - Enable/disable HTTP tunnel authentication. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> icap-profile </span> - Name of an existing ICAP profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service </span> - Enable/disable use of Internet Services for this policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-custom </span> - Custom Internet Service name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-id </span> - Internet Service ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-negate </span> - When enabled, Internet Services match against any internet service EXCEPT the selected Internet Service. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ips-sensor </span> - Name of an existing IPS sensor. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> label </span> - VDOM-specific GUI visible label. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> logtraffic </span> - Enable/disable logging traffic through the policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> logtraffic-start </span> - Enable/disable policy log traffic start. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mms-profile </span> - Name of an existing MMS profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> policyid </span> - Policy ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> poolname </span> - Name of IP pool object. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> profile-group </span> - Name of profile group. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> profile-protocol-options </span> - Name of an existing Protocol options profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> profile-type </span> - Determine whether the firewall policy allows security profile groups or single profiles only. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> proxy </span> - Type of explicit proxy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> redirect-url </span> - Redirect URL for further explicit web proxy processing. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> replacemsg-override-group </span> - Authentication replacement message override group. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> scan-botnet-connections </span> - Enable/disable scanning of connections to Botnet servers. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> schedule </span> - Name of schedule object. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> service </span> - Name of service objects. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> service-negate </span> - When enabled, services match against any service EXCEPT the specified destination services. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> spamfilter-profile </span> - Name of an existing Spam filter profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcaddr </span> - Source address objects (must be set when using Web proxy). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcaddr-negate </span> - When enabled, source addresses match against any address EXCEPT the specified source addresses. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcaddr6 </span> - IPv6 source address objects. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcintf </span> - Source interface names. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-ssh-profile </span> - Name of an existing SSL SSH profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable the active status of the policy. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tags </span> - Names of object-tags applied to address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> transparent </span> - Enable to use the IP address of the client to connect to the server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> users </span> - Names of user objects. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> utm-status </span> - Enable the use of UTM profiles/sensors/lists. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> uuid </span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> waf-profile </span> - Name of an existing Web application firewall profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webcache </span> - Enable/disable web caching. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webcache-https </span> - Enable/disable web caching for HTTPS (Requires deep-inspection enabled in ssl-ssh-profile). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webfilter-profile </span> - Name of an existing Web filter profile. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webproxy-forward-server </span> - Name of web proxy forward server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webproxy-profile </span> - Name of web proxy profile. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/proxy-policy/{proxy-policy}</span>  </li>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/proxy-policy/{proxy-policy}</span>  </li>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/proxy-policy/{proxy-policy}</span>  </li>
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



