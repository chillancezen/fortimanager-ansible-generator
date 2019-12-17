:source: fmgr_pm_config_obj_webfilter_urlfilter_urlfilter.py

:orphan:

.. _fmgr_pm_config_obj_webfilter_urlfilter_urlfilter:

fmgr_pm_config_obj_webfilter_urlfilter_urlfilter -- Configure URL filter lists.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/webfilter/urlfilter/{urlfilter}`
- `/pm/config/global/obj/webfilter/urlfilter/{urlfilter}`
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
 <li><span class="li-head">urlfilter</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure URL filter lists.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">comment</span> - Optional comments. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">entries</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action to take for URL filter matches. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [exempt, block, allow, monitor, pass]</span> </li>
 <li><span class="li-head">dns-address-family</span> - Resolve IPv4 address, IPv6 address, or both from DNS server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipv4, ipv6, both]</span> </li>
 <li><span class="li-head">exempt</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [av, web-content, activex-java-cookie, dlp, fortiguard, all, filepattern, pass, range-block]</span> </li>
 </ul>
 <li><span class="li-head">id</span> - Id. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">referrer-host</span> - Referrer host name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable this URL filter. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">type</span> - Filter type (simple, regex, or wildcard). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [simple, regex, wildcard]</span> </li>
 <li><span class="li-head">url</span> - URL to be filtered. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">web-proxy-profile</span> - Web proxy profile. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip-addr-block</span> - Enable/disable blocking URLs when the hostname appears as an IP address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - Name of URL filter list. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">one-arm-ips-urlfilter</span> - Enable/disable DNS resolver for one-arm IPS URL filter operation. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure URL filter lists.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure URL filter lists.</li>
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
    - name: send request to /pm/config/obj/webfilter/urlfilter/{urlfilter}
      fmgr_pm_config_obj_webfilter_urlfilter_urlfilter:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            urlfilter: <value of string>
         params:
            - 
               data: 
                  comment: <value of string>
                  entries: 
                   - 
                        action: <value in [exempt, block, allow, ...]>
                        dns-address-family: <value in [ipv4, ipv6, both]>
                        exempt: 
                         - <value in [av, web-content, activex-java-cookie, ...]>
                        id: <value of integer>
                        referrer-host: <value of string>
                        status: <value in [disable, enable]>
                        type: <value in [simple, regex, wildcard]>
                        url: <value of string>
                        web-proxy-profile: <value of string>
                  id: <value of integer>
                  ip-addr-block: <value in [disable, enable]>
                  name: <value of string>
                  one-arm-ips-urlfilter: <value in [disable, enable]>
    - name: send request to /pm/config/obj/webfilter/urlfilter/{urlfilter}
      fmgr_pm_config_obj_webfilter_urlfilter_urlfilter:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            urlfilter: <value of string>
         params:
            - 
               option: <value in [object member, chksum, datasrc]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [clone, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/webfilter/urlfilter/{urlfilter}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [delete]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/webfilter/urlfilter/{urlfilter}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> comment </span> - Optional comments. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> entries </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - Action to take for URL filter matches. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dns-address-family </span> - Resolve IPv4 address, IPv6 address, or both from DNS server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> exempt </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> id </span> - Id. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> referrer-host </span> - Referrer host name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable this URL filter. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - Filter type (simple, regex, or wildcard). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> url </span> - URL to be filtered. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> web-proxy-profile </span> - Web proxy profile. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> id </span> - ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip-addr-block </span> - Enable/disable blocking URLs when the hostname appears as an IP address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Name of URL filter list. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> one-arm-ips-urlfilter </span> - Enable/disable DNS resolver for one-arm IPS URL filter operation. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/webfilter/urlfilter/{urlfilter}</span>  </li>
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



