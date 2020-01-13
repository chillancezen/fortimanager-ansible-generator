:source: fmgr_system_fortiguard.py

:orphan:

.. _fmgr_system_fortiguard:

fmgr_system_fortiguard -- Configure FortiGuard services.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/system/fortiguard`
- `/pm/config/global/obj/system/fortiguard`
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
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure FortiGuard services.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Configure FortiGuard services.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">antispam-cache</span> - Enable/disable FortiGuard antispam request caching. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">antispam-cache-mpercent</span> - Maximum percent of FortiGate memory the antispam cache is allowed to use (1 - 15%). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">antispam-cache-ttl</span> - Time-to-live for antispam cache entries in seconds (300 - 86400). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">antispam-expiration</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">antispam-force-off</span> - Enable/disable turning off the FortiGuard antispam service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">antispam-license</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">antispam-timeout</span> - Antispam query time out (1 - 30 sec, default = 7). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">auto-join-forticloud</span> - Automatically connect to and login to FortiCloud. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ddns-server-ip</span> - IP address of the FortiDDNS server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ddns-server-port</span> - Port used to communicate with FortiDDNS servers. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">load-balance-servers</span> - Number of servers to alternate between as first FortiGuard option. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">outbreak-prevention-cache</span> - Enable/disable FortiGuard Virus Outbreak Prevention cache. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">outbreak-prevention-cache-mpercent</span> - Maximum percent of memory FortiGuard Virus Outbreak Prevention cache can use (1 - 15%, default = 2). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">outbreak-prevention-cache-ttl</span> - Time-to-live for FortiGuard Virus Outbreak Prevention cache entries (300 - 86400 sec, default = 300). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">outbreak-prevention-expiration</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">outbreak-prevention-force-off</span> - Turn off FortiGuard Virus Outbreak Prevention service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">outbreak-prevention-license</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">outbreak-prevention-timeout</span> - FortiGuard Virus Outbreak Prevention time out (1 - 30 sec, default = 7). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">port</span> - Port used to communicate with the FortiGuard servers. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [53, 80, 8888]</span> </li>
 <li><span class="li-head">sdns-server-ip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">sdns-server-port</span> - Port used to communicate with FortiDNS servers. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">service-account-id</span> - Service account ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-ip</span> - Source IPv4 address used to communicate with FortiGuard. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">source-ip6</span> - Source IPv6 address used to communicate with FortiGuard. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">update-server-location</span> - Signature update server location. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [any, usa]</span> </li>
 <li><span class="li-head">webfilter-cache</span> - Enable/disable FortiGuard web filter caching. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">webfilter-cache-ttl</span> - Time-to-live for web filter cache entries in seconds (300 - 86400). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">webfilter-expiration</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">webfilter-force-off</span> - Enable/disable turning off the FortiGuard web filtering service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">webfilter-license</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">webfilter-timeout</span> - Web filter query time out (1 - 30 sec, default = 7). <span class="li-normal">type: int</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/SYSTEM/FORTIGUARD
      fmgr_system_fortiguard:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/SYSTEM/FORTIGUARD
      fmgr_system_fortiguard:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                  antispam-cache: <value in [disable, enable]>
                  antispam-cache-mpercent: <value of integer>
                  antispam-cache-ttl: <value of integer>
                  antispam-expiration: <value of integer>
                  antispam-force-off: <value in [disable, enable]>
                  antispam-license: <value of integer>
                  antispam-timeout: <value of integer>
                  auto-join-forticloud: <value in [disable, enable]>
                  ddns-server-ip: <value of string>
                  ddns-server-port: <value of integer>
                  load-balance-servers: <value of integer>
                  outbreak-prevention-cache: <value in [disable, enable]>
                  outbreak-prevention-cache-mpercent: <value of integer>
                  outbreak-prevention-cache-ttl: <value of integer>
                  outbreak-prevention-expiration: <value of integer>
                  outbreak-prevention-force-off: <value in [disable, enable]>
                  outbreak-prevention-license: <value of integer>
                  outbreak-prevention-timeout: <value of integer>
                  port: <value in [53, 80, 8888]>
                  sdns-server-ip:
                    - <value of string>
                  sdns-server-port: <value of integer>
                  service-account-id: <value of string>
                  source-ip: <value of string>
                  source-ip6: <value of string>
                  update-server-location: <value in [any, usa]>
                  webfilter-cache: <value in [disable, enable]>
                  webfilter-cache-ttl: <value of integer>
                  webfilter-expiration: <value of integer>
                  webfilter-force-off: <value in [disable, enable]>
                  webfilter-license: <value of integer>
                  webfilter-timeout: <value of integer>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> antispam-cache </span> - Enable/disable FortiGuard antispam request caching. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> antispam-cache-mpercent </span> - Maximum percent of FortiGate memory the antispam cache is allowed to use (1 - 15%). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> antispam-cache-ttl </span> - Time-to-live for antispam cache entries in seconds (300 - 86400). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> antispam-expiration </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> antispam-force-off </span> - Enable/disable turning off the FortiGuard antispam service. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> antispam-license </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> antispam-timeout </span> - Antispam query time out (1 - 30 sec, default = 7). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> auto-join-forticloud </span> - Automatically connect to and login to FortiCloud. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ddns-server-ip </span> - IP address of the FortiDDNS server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ddns-server-port </span> - Port used to communicate with FortiDDNS servers. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> load-balance-servers </span> - Number of servers to alternate between as first FortiGuard option. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> outbreak-prevention-cache </span> - Enable/disable FortiGuard Virus Outbreak Prevention cache. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> outbreak-prevention-cache-mpercent </span> - Maximum percent of memory FortiGuard Virus Outbreak Prevention cache can use (1 - 15%, default = 2). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> outbreak-prevention-cache-ttl </span> - Time-to-live for FortiGuard Virus Outbreak Prevention cache entries (300 - 86400 sec, default = 300). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> outbreak-prevention-expiration </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> outbreak-prevention-force-off </span> - Turn off FortiGuard Virus Outbreak Prevention service. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> outbreak-prevention-license </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> outbreak-prevention-timeout </span> - FortiGuard Virus Outbreak Prevention time out (1 - 30 sec, default = 7). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> port </span> - Port used to communicate with the FortiGuard servers. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sdns-server-ip </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> sdns-server-port </span> - Port used to communicate with FortiDNS servers. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> service-account-id </span> - Service account ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-ip </span> - Source IPv4 address used to communicate with FortiGuard. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> source-ip6 </span> - Source IPv6 address used to communicate with FortiGuard. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> update-server-location </span> - Signature update server location. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webfilter-cache </span> - Enable/disable FortiGuard web filter caching. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webfilter-cache-ttl </span> - Time-to-live for web filter cache entries in seconds (300 - 86400). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> webfilter-expiration </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> webfilter-force-off </span> - Enable/disable turning off the FortiGuard web filtering service. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> webfilter-license </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> webfilter-timeout </span> - Web filter query time out (1 - 30 sec, default = 7). <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/system/fortiguard</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/system/fortiguard</span>  </li>
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



