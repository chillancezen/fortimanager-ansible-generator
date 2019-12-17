:source: fmgr_cli_fmupdate_fds_setting.py

:orphan:

.. _fmgr_cli_fmupdate_fds_setting:

fmgr_cli_fmupdate_fds_setting -- Configure FortiGuard settings.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/fmupdate/fds-setting`
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
 <li><span class="li-head">parameters for method: [get]</span> - Configure FortiGuard settings.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Configure FortiGuard settings.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">User-Agent</span> - Configure the user agent string. <span class="li-normal">type: str</span>  <span class="li-normal">default: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)</span> </li>
 <li><span class="li-head">fds-clt-ssl-protocol</span> - The SSL protocols version for connecting fds server (default = tlsv1. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sslv3, tlsv1.0, tlsv1.1, tlsv1.2]</span>  <span class="li-normal">default: tlsv1.2</span> </li>
 <li><span class="li-head">fds-ssl-protocol</span> - The SSL protocols version for receiving fgt connection (default = tlsv1. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sslv3, tlsv1.0, tlsv1.1, tlsv1.2]</span>  <span class="li-normal">default: tlsv1.2</span> </li>
 <li><span class="li-head">fmtr-log</span> - fmtr log level <span class="li-normal">type: str</span>  <span class="li-normal">choices: [emergency, alert, critical, error, warn, notice, info, debug, disable]</span>  <span class="li-normal">default: info</span> </li>
 <li><span class="li-head">linkd-log</span> - The linkd log level (default = info). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [emergency, alert, critical, error, warn, notice, info, debug, disable]</span>  <span class="li-normal">default: info</span> </li>
 <li><span class="li-head">max-av-ips-version</span> - The maximum number of downloadable, full version AV/IPS packages (1 - 1000, default = 20). <span class="li-normal">type: int</span>  <span class="li-normal">default: 20</span> </li>
 <li><span class="li-head">max-work</span> - The maximum number of worker processing download requests (1 - 32, default = 1). <span class="li-normal">type: int</span>  <span class="li-normal">default: 1</span> </li>
 <li><span class="li-head">push-override</span> <li><span class="li-head">ip</span> - External or virtual IP address of the NAT device that will forward push messages to the FortiManager unit. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">port</span> - Receiving port number on the NAT device (1 - 65535, default = 9443). <span class="li-normal">type: int</span>  <span class="li-normal">default: 9443</span> </li>
 <li><span class="li-head">status</span> - Enable/disable push updates for clients (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">push-override-to-client</span> <li><span class="li-head">announce-ip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - ID of the announce IP address (1 - 10). <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">ip</span> - Announce IPv4 address. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">port</span> - Announce IP port (1 - 65535, default = 8890). <span class="li-normal">type: int</span>  <span class="li-normal">default: 8890</span> </li>
 </ul>
 <li><span class="li-head">status</span> - Enable/disable push updates (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">send_report</span> - send report/fssi to fds server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">send_setup</span> - forward setup to fds server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">server-override</span> <li><span class="li-head">servlist</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - Override server ID (1 - 10). <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">ip</span> - IPv4 address of the override server. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">ip6</span> - IPv6 address of the override server. <span class="li-normal">type: str</span>  <span class="li-normal">default: ::</span> </li>
 <li><span class="li-head">port</span> - Port number to use when contacting FortiGuard (1 - 65535, default = 443). <span class="li-normal">type: int</span>  <span class="li-normal">default: 443</span> </li>
 <li><span class="li-head">service-type</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [fds, fct]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">status</span> - Override status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">system-support-fct</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [4.x, 5.0, 5.2, 5.4, 5.6, 6.0]</span> </li>
 </ul>
 <li><span class="li-head">system-support-fgt</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [5.4, 5.6, 6.0, 6.2]</span> </li>
 </ul>
 <li><span class="li-head">system-support-fml</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [4.x, 5.x, 6.x]</span> </li>
 </ul>
 <li><span class="li-head">system-support-fsa</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1.x, 2.x, 3.x]</span> </li>
 </ul>
 <li><span class="li-head">system-support-fsw</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [5.4, 5.6, 6.0, 6.2]</span> </li>
 </ul>
 <li><span class="li-head">umsvc-log</span> - The um_service log level (default = info). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [emergency, alert, critical, error, warn, notice, info, debug, disable]</span>  <span class="li-normal">default: info</span> </li>
 <li><span class="li-head">unreg-dev-option</span> - set the option for unregister devices <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ignore, svc-only, add-service]</span>  <span class="li-normal">default: add-service</span> </li>
 <li><span class="li-head">update-schedule</span> <li><span class="li-head">day</span> - Configure the day the update will occur, if the freqnecy is weekly (Sunday - Saturday, default = Monday). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday]</span>  <span class="li-normal">default: Monday</span> </li>
 <li><span class="li-head">frequency</span> - Configure update frequency: every - time interval, daily - once a day, weekly - once a week (default = every). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [every, daily, weekly]</span>  <span class="li-normal">default: every</span> </li>
 <li><span class="li-head">status</span> - Enable/disable scheduled updates. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">time</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">wanip-query-mode</span> - public ip query mode <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, ipify]</span>  <span class="li-normal">default: disable</span> </li>
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
    - name: send request to /cli/fmupdate/fds-setting
      fmgr_cli_fmupdate_fds_setting:
         method: <value in [set, update]>
         params:
            - 
               data: 
                  User-Agent: <value of string default: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)>
                  fds-clt-ssl-protocol: <value in [sslv3, tlsv1.0, tlsv1.1, ...] default: tlsv1.2>
                  fds-ssl-protocol: <value in [sslv3, tlsv1.0, tlsv1.1, ...] default: tlsv1.2>
                  fmtr-log: <value in [emergency, alert, critical, ...] default: info>
                  linkd-log: <value in [emergency, alert, critical, ...] default: info>
                  max-av-ips-version: <value of integer default: 20>
                  max-work: <value of integer default: 1>
                  push-override: 
                     ip: <value of string default: 0.0.0.0>
                     port: <value of integer default: 9443>
                     status: <value in [disable, enable] default: disable>
                  push-override-to-client: 
                     announce-ip: 
                      - 
                           id: <value of integer default: 0>
                           ip: <value of string default: 0.0.0.0>
                           port: <value of integer default: 8890>
                     status: <value in [disable, enable] default: disable>
                  send_report: <value in [disable, enable] default: enable>
                  send_setup: <value in [disable, enable] default: disable>
                  server-override: 
                     servlist: 
                      - 
                           id: <value of integer default: 0>
                           ip: <value of string default: 0.0.0.0>
                           ip6: <value of string default: ::>
                           port: <value of integer default: 443>
                           service-type: 
                            - <value in [fds, fct]>
                     status: <value in [disable, enable] default: disable>
                  system-support-fct: 
                   - <value in [4.x, 5.0, 5.2, ...]>
                  system-support-fgt: 
                   - <value in [5.4, 5.6, 6.0, ...]>
                  system-support-fml: 
                   - <value in [4.x, 5.x, 6.x]>
                  system-support-fsa: 
                   - <value in [1.x, 2.x, 3.x]>
                  system-support-fsw: 
                   - <value in [5.4, 5.6, 6.0, ...]>
                  umsvc-log: <value in [emergency, alert, critical, ...] default: info>
                  unreg-dev-option: <value in [ignore, svc-only, add-service] default: add-service>
                  update-schedule: 
                     day: <value in [Sunday, Monday, Tuesday, ...] default: Monday>
                     frequency: <value in [every, daily, weekly] default: every>
                     status: <value in [disable, enable] default: enable>
                     time: 
                      - <value of string>
                  wanip-query-mode: <value in [disable, ipify] default: disable>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> User-Agent </span> - Configure the user agent string. <span class="li-normal">type: str</span>  <span class="li-normal">example: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)</span>  </li>
 <li> <span class="li-return"> fds-clt-ssl-protocol </span> - The SSL protocols version for connecting fds server (default = tlsv1. <span class="li-normal">type: str</span>  <span class="li-normal">example: tlsv1.2</span>  </li>
 <li> <span class="li-return"> fds-ssl-protocol </span> - The SSL protocols version for receiving fgt connection (default = tlsv1. <span class="li-normal">type: str</span>  <span class="li-normal">example: tlsv1.2</span>  </li>
 <li> <span class="li-return"> fmtr-log </span> - fmtr log level <span class="li-normal">type: str</span>  <span class="li-normal">example: info</span>  </li>
 <li> <span class="li-return"> linkd-log </span> - The linkd log level (default = info). <span class="li-normal">type: str</span>  <span class="li-normal">example: info</span>  </li>
 <li> <span class="li-return"> max-av-ips-version </span> - The maximum number of downloadable, full version AV/IPS packages (1 - 1000, default = 20). <span class="li-normal">type: int</span>  <span class="li-normal">example: 20</span>  </li>
 <li> <span class="li-return"> max-work </span> - The maximum number of worker processing download requests (1 - 32, default = 1). <span class="li-normal">type: int</span>  <span class="li-normal">example: 1</span>  </li>
 <li> <span class="li-return"> push-override </span> <li> <span class="li-return"> ip </span> - External or virtual IP address of the NAT device that will forward push messages to the FortiManager unit. <span class="li-normal">type: str</span>  <span class="li-normal">example: 0.0.0.0</span>  </li>
 <li> <span class="li-return"> port </span> - Receiving port number on the NAT device (1 - 65535, default = 9443). <span class="li-normal">type: int</span>  <span class="li-normal">example: 9443</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable push updates for clients (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> push-override-to-client </span> <li> <span class="li-return"> announce-ip </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - ID of the announce IP address (1 - 10). <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> ip </span> - Announce IPv4 address. <span class="li-normal">type: str</span>  <span class="li-normal">example: 0.0.0.0</span>  </li>
 <li> <span class="li-return"> port </span> - Announce IP port (1 - 65535, default = 8890). <span class="li-normal">type: int</span>  <span class="li-normal">example: 8890</span>  </li>
 </ul>
 <li> <span class="li-return"> status </span> - Enable/disable push updates (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> send_report </span> - send report/fssi to fds server. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> send_setup </span> - forward setup to fds server. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> server-override </span> <li> <span class="li-return"> servlist </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - Override server ID (1 - 10). <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> ip </span> - IPv4 address of the override server. <span class="li-normal">type: str</span>  <span class="li-normal">example: 0.0.0.0</span>  </li>
 <li> <span class="li-return"> ip6 </span> - IPv6 address of the override server. <span class="li-normal">type: str</span>  <span class="li-normal">example: ::</span>  </li>
 <li> <span class="li-return"> port </span> - Port number to use when contacting FortiGuard (1 - 65535, default = 443). <span class="li-normal">type: int</span>  <span class="li-normal">example: 443</span>  </li>
 <li> <span class="li-return"> service-type </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 </ul>
 <li> <span class="li-return"> status </span> - Override status. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> system-support-fct </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> system-support-fgt </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> system-support-fml </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> system-support-fsa </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> system-support-fsw </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> umsvc-log </span> - The um_service log level (default = info). <span class="li-normal">type: str</span>  <span class="li-normal">example: info</span>  </li>
 <li> <span class="li-return"> unreg-dev-option </span> - set the option for unregister devices <span class="li-normal">type: str</span>  <span class="li-normal">example: add-service</span>  </li>
 <li> <span class="li-return"> update-schedule </span> <li> <span class="li-return"> day </span> - Configure the day the update will occur, if the freqnecy is weekly (Sunday - Saturday, default = Monday). <span class="li-normal">type: str</span>  <span class="li-normal">example: Monday</span>  </li>
 <li> <span class="li-return"> frequency </span> - Configure update frequency: every - time interval, daily - once a day, weekly - once a week (default = every). <span class="li-normal">type: str</span>  <span class="li-normal">example: every</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable scheduled updates. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> time </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> wanip-query-mode </span> - public ip query mode <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/fmupdate/fds-setting</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/fmupdate/fds-setting</span>  </li>
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



