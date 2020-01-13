:source: fmgr_firewall_vip6_dynamicmapping.py

:orphan:

.. _fmgr_firewall_vip6_dynamicmapping:

fmgr_firewall_vip6_dynamicmapping
+++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/vip6/{vip6}/dynamic_mapping`
- `/pm/config/global/obj/firewall/vip6/{vip6}/dynamic_mapping`
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
 <li><span class="li-head">vip6</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">arp-reply</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">color</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extport</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-cookie-age</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">http-cookie-domain</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-cookie-domain-from-host</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">http-cookie-generation</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">http-cookie-path</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-cookie-share</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, same-ip]</span> </li>
 <li><span class="li-head">http-ip-header</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">http-ip-header-name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">http-multiplex</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">https-cookie-secure</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ldb-method</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static, round-robin, weighted, least-session, least-rtt, first-alive, http-host]</span> </li>
 <li><span class="li-head">mappedip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mappedport</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-embryonic-connections</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">monitor</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">outlook-web-access</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">persistence</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [none, http-cookie, ssl-session-id]</span> </li>
 <li><span class="li-head">portforward</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">protocol</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [tcp, udp, sctp]</span> </li>
 <li><span class="li-head">server-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [http, https, ssl, tcp, udp, ip, imaps, pop3s, smtps]</span> </li>
 <li><span class="li-head">src-filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">ssl-algorithm</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [high, low, medium, custom]</span> </li>
 <li><span class="li-head">ssl-certificate</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-client-fallback</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-client-renegotiation</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, allow, secure]</span> </li>
 <li><span class="li-head">ssl-client-session-state-max</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-client-session-state-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-client-session-state-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, time, count, both]</span> </li>
 <li><span class="li-head">ssl-dh-bits</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [768, 1024, 1536, 2048, 3072, 4096]</span> </li>
 <li><span class="li-head">ssl-hpkp</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, report-only]</span> </li>
 <li><span class="li-head">ssl-hpkp-age</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-hpkp-backup</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-hpkp-include-subdomains</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-hpkp-primary</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-hpkp-report-uri</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ssl-hsts</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-hsts-age</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-hsts-include-subdomains</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-http-location-conversion</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-http-match-host</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-max-version</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2]</span> </li>
 <li><span class="li-head">ssl-min-version</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2]</span> </li>
 <li><span class="li-head">ssl-mode</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [half, full]</span> </li>
 <li><span class="li-head">ssl-pfs</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [require, deny, allow]</span> </li>
 <li><span class="li-head">ssl-send-empty-frags</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-server-algorithm</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [high, low, medium, custom, client]</span> </li>
 <li><span class="li-head">ssl-server-max-version</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2, client]</span> </li>
 <li><span class="li-head">ssl-server-min-version</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ssl-3.0, tls-1.0, tls-1.1, tls-1.2, client]</span> </li>
 <li><span class="li-head">ssl-server-session-state-max</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-server-session-state-timeout</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ssl-server-session-state-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, time, count, both]</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [static-nat, server-load-balance]</span> </li>
 <li><span class="li-head">uuid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">weblogic-server</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">websphere-server</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [_scope, arp-reply, color, comment, extip, extport, http-cookie-age, http-cookie-domain, http-cookie-domain-from-host, http-cookie-generation, http-cookie-path, http-cookie-share, http-ip-header, http-ip-header-name, http-multiplex, https-cookie-secure, id, ldb-method, mappedip, mappedport, max-embryonic-connections, monitor, outlook-web-access, persistence, portforward, protocol, server-type, src-filter, ssl-algorithm, ssl-certificate, ssl-client-fallback, ssl-client-renegotiation, ssl-client-session-state-max, ssl-client-session-state-timeout, ssl-client-session-state-type, ssl-dh-bits, ssl-hpkp, ssl-hpkp-age, ssl-hpkp-backup, ssl-hpkp-include-subdomains, ssl-hpkp-primary, ssl-hpkp-report-uri, ssl-hsts, ssl-hsts-age, ssl-hsts-include-subdomains, ssl-http-location-conversion, ssl-http-match-host, ssl-max-version, ssl-min-version, ssl-mode, ssl-pfs, ssl-send-empty-frags, ssl-server-algorithm, ssl-server-max-version, ssl-server-min-version, ssl-server-session-state-max, ssl-server-session-state-timeout, ssl-server-session-state-type, type, uuid, weblogic-server, websphere-server]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">get used</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">loadsub</span> - Enable or disable the return of any sub-objects. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [count, object member, datasrc, get reserved, syntax]</span> </li>
 <li><span class="li-head">range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">sortings</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{attr_name}</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">choices: [1, -1]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/VIP6/{VIP6}/DYNAMIC_MAPPING
      fmgr_firewall_vip6_dynamicmapping:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vip6: <value of string>
         params:
            -
               data:
                 -
                     _scope:
                       -
                           name: <value of string>
                           vdom: <value of string>
                     arp-reply: <value in [disable, enable]>
                     color: <value of integer>
                     comment: <value of string>
                     extip: <value of string>
                     extport: <value of string>
                     http-cookie-age: <value of integer>
                     http-cookie-domain: <value of string>
                     http-cookie-domain-from-host: <value in [disable, enable]>
                     http-cookie-generation: <value of integer>
                     http-cookie-path: <value of string>
                     http-cookie-share: <value in [disable, same-ip]>
                     http-ip-header: <value in [disable, enable]>
                     http-ip-header-name: <value of string>
                     http-multiplex: <value in [disable, enable]>
                     https-cookie-secure: <value in [disable, enable]>
                     id: <value of integer>
                     ldb-method: <value in [static, round-robin, weighted, ...]>
                     mappedip: <value of string>
                     mappedport: <value of string>
                     max-embryonic-connections: <value of integer>
                     monitor: <value of string>
                     outlook-web-access: <value in [disable, enable]>
                     persistence: <value in [none, http-cookie, ssl-session-id]>
                     portforward: <value in [disable, enable]>
                     protocol: <value in [tcp, udp, sctp]>
                     server-type: <value in [http, https, ssl, ...]>
                     src-filter:
                       - <value of string>
                     ssl-algorithm: <value in [high, low, medium, ...]>
                     ssl-certificate: <value of string>
                     ssl-client-fallback: <value in [disable, enable]>
                     ssl-client-renegotiation: <value in [deny, allow, secure]>
                     ssl-client-session-state-max: <value of integer>
                     ssl-client-session-state-timeout: <value of integer>
                     ssl-client-session-state-type: <value in [disable, time, count, ...]>
                     ssl-dh-bits: <value in [768, 1024, 1536, ...]>
                     ssl-hpkp: <value in [disable, enable, report-only]>
                     ssl-hpkp-age: <value of integer>
                     ssl-hpkp-backup: <value of string>
                     ssl-hpkp-include-subdomains: <value in [disable, enable]>
                     ssl-hpkp-primary: <value of string>
                     ssl-hpkp-report-uri: <value of string>
                     ssl-hsts: <value in [disable, enable]>
                     ssl-hsts-age: <value of integer>
                     ssl-hsts-include-subdomains: <value in [disable, enable]>
                     ssl-http-location-conversion: <value in [disable, enable]>
                     ssl-http-match-host: <value in [disable, enable]>
                     ssl-max-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
                     ssl-min-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
                     ssl-mode: <value in [half, full]>
                     ssl-pfs: <value in [require, deny, allow]>
                     ssl-send-empty-frags: <value in [disable, enable]>
                     ssl-server-algorithm: <value in [high, low, medium, ...]>
                     ssl-server-max-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
                     ssl-server-min-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
                     ssl-server-session-state-max: <value of integer>
                     ssl-server-session-state-timeout: <value of integer>
                     ssl-server-session-state-type: <value in [disable, time, count, ...]>
                     type: <value in [static-nat, server-load-balance]>
                     uuid: <value of string>
                     weblogic-server: <value in [disable, enable]>
                     websphere-server: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/VIP6/{VIP6}/DYNAMIC_MAPPING
      fmgr_firewall_vip6_dynamicmapping:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vip6: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [_scope, arp-reply, color, ...]>
               filter:
                 - <value of string>
               get used: <value of integer>
               loadsub: <value of integer>
               option: <value in [count, object member, datasrc, ...]>
               range:
                 - <value of integer>
               sortings:
                 -
                     varidic.attr_name: <value in [1, -1]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [add, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/vip6/{vip6}/dynamic_mapping</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> _scope </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> arp-reply </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> color </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comment </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> extip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> extport </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-cookie-age </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> http-cookie-domain </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-cookie-domain-from-host </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-cookie-generation </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> http-cookie-path </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-cookie-share </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-ip-header </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-ip-header-name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> http-multiplex </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> https-cookie-secure </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ldb-method </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mappedip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mappedport </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-embryonic-connections </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> monitor </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> outlook-web-access </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> persistence </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> portforward </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> protocol </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> src-filter </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> ssl-algorithm </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-certificate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-client-fallback </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-client-renegotiation </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-client-session-state-max </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ssl-client-session-state-timeout </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ssl-client-session-state-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-dh-bits </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hpkp </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hpkp-age </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ssl-hpkp-backup </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hpkp-include-subdomains </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hpkp-primary </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hpkp-report-uri </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hsts </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-hsts-age </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ssl-hsts-include-subdomains </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-http-location-conversion </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-http-match-host </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-max-version </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-min-version </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-mode </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-pfs </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-send-empty-frags </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-server-algorithm </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-server-max-version </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-server-min-version </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-server-session-state-max </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ssl-server-session-state-timeout </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ssl-server-session-state-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> uuid </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> weblogic-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> websphere-server </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/vip6/{vip6}/dynamic_mapping</span>  </li>
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



