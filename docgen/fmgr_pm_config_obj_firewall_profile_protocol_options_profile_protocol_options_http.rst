:source: fmgr_pm_config_obj_firewall_profile_protocol_options_profile_protocol_options_http.py

:orphan:

.. _fmgr_pm_config_obj_firewall_profile_protocol_options_profile_protocol_options_http:

fmgr_pm_config_obj_firewall_profile_protocol_options_profile_protocol_options_http -- Configure HTTP protocol options.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/profile-protocol-options/{profile-protocol-options}/http`
- `/pm/config/global/obj/firewall/profile-protocol-options/{profile-protocol-options}/http`
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
 <li><span class="li-head">profile-protocol-options</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure HTTP protocol options.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Configure HTTP protocol options.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">block-page-status-code</span> - Code number returned for blocked HTTP pages (non-FortiGuard only) (100 - 599, default = 403). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comfort-amount</span> - Amount of data to send in a transmission for client comforting (1 - 10240 bytes, default = 1). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comfort-interval</span> - Period of time between start, or last transmission, and the next client comfort transmission of data (1 - 900 sec, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">fortinet-bar</span> - Enable/disable Fortinet bar on HTML content. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">fortinet-bar-port</span> - Port for use by Fortinet Bar (1 - 65535, default = 8011). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">http-policy</span> - Enable/disable HTTP policy check. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">inspect-all</span> - Enable/disable the inspection of all ports for the protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">options</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [oversize, chunkedbypass, clientcomfort, no-content-summary, servercomfort]</span> </li>
 </ul>
 <li><span class="li-head">oversize-limit</span> - Maximum in-memory file size that can be scanned (1 - 383 MB, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ports</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">post-lang</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [jisx0201, jisx0208, jisx0212, gb2312, ksc5601-ex, euc-jp, sjis, iso2022-jp, iso2022-jp-1, iso2022-jp-2, euc-cn, ces-gbk, hz, ces-big5, euc-kr, iso2022-jp-3, iso8859-1, tis620, cp874, cp1252, cp1251]</span> </li>
 </ul>
 <li><span class="li-head">range-block</span> - Enable/disable blocking of partial downloads. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">retry-count</span> - Number of attempts to retry HTTP connection (0 - 100, default = 0). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">scan-bzip2</span> - Enable/disable scanning of BZip2 compressed files. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the active status of scanning for this protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">streaming-content-bypass</span> - Enable/disable bypassing of streaming content from buffering. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">strip-x-forwarded-for</span> - Enable/disable stripping of HTTP X-Forwarded-For header. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">switching-protocols</span> - Bypass from scanning, or block a connection that attempts to switch protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [bypass, block]</span> </li>
 <li><span class="li-head">uncompressed-nest-limit</span> - Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">uncompressed-oversize-limit</span> - Maximum in-memory uncompressed file size that can be scanned (0 - 383 MB, 0 = unlimited, default = 10). <span class="li-normal">type: int</span> </li>
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
    - name: send request to /pm/config/obj/firewall/profile-protocol-options/{profile-protocol-options}/http
      fmgr_pm_config_obj_firewall_profile_protocol_options_profile_protocol_options_http:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile-protocol-options: <value of string>
         params:
            - 
               option: <value in [object member, chksum, datasrc]>
    - name: send request to /pm/config/obj/firewall/profile-protocol-options/{profile-protocol-options}/http
      fmgr_pm_config_obj_firewall_profile_protocol_options_profile_protocol_options_http:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile-protocol-options: <value of string>
         params:
            - 
               data: 
                  block-page-status-code: <value of integer>
                  comfort-amount: <value of integer>
                  comfort-interval: <value of integer>
                  fortinet-bar: <value in [disable, enable]>
                  fortinet-bar-port: <value of integer>
                  http-policy: <value in [disable, enable]>
                  inspect-all: <value in [disable, enable]>
                  options: 
                   - <value in [oversize, chunkedbypass, clientcomfort, ...]>
                  oversize-limit: <value of integer>
                  ports: 
                   - <value of integer>
                  post-lang: 
                   - <value in [jisx0201, jisx0208, jisx0212, ...]>
                  range-block: <value in [disable, enable]>
                  retry-count: <value of integer>
                  scan-bzip2: <value in [disable, enable]>
                  status: <value in [disable, enable]>
                  streaming-content-bypass: <value in [disable, enable]>
                  strip-x-forwarded-for: <value in [disable, enable]>
                  switching-protocols: <value in [bypass, block]>
                  uncompressed-nest-limit: <value of integer>
                  uncompressed-oversize-limit: <value of integer>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> block-page-status-code </span> - Code number returned for blocked HTTP pages (non-FortiGuard only) (100 - 599, default = 403). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comfort-amount </span> - Amount of data to send in a transmission for client comforting (1 - 10240 bytes, default = 1). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comfort-interval </span> - Period of time between start, or last transmission, and the next client comfort transmission of data (1 - 900 sec, default = 10). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> fortinet-bar </span> - Enable/disable Fortinet bar on HTML content. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fortinet-bar-port </span> - Port for use by Fortinet Bar (1 - 65535, default = 8011). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> http-policy </span> - Enable/disable HTTP policy check. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> inspect-all </span> - Enable/disable the inspection of all ports for the protocol. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> options </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> oversize-limit </span> - Maximum in-memory file size that can be scanned (1 - 383 MB, default = 10). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ports </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> post-lang </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> range-block </span> - Enable/disable blocking of partial downloads. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> retry-count </span> - Number of attempts to retry HTTP connection (0 - 100, default = 0). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> scan-bzip2 </span> - Enable/disable scanning of BZip2 compressed files. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable the active status of scanning for this protocol. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> streaming-content-bypass </span> - Enable/disable bypassing of streaming content from buffering. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> strip-x-forwarded-for </span> - Enable/disable stripping of HTTP X-Forwarded-For header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> switching-protocols </span> - Bypass from scanning, or block a connection that attempts to switch protocol. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> uncompressed-nest-limit </span> - Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> uncompressed-oversize-limit </span> - Maximum in-memory uncompressed file size that can be scanned (0 - 383 MB, 0 = unlimited, default = 10). <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/profile-protocol-options/{profile-protocol-options}/http</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/profile-protocol-options/{profile-protocol-options}/http</span>  </li>
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



