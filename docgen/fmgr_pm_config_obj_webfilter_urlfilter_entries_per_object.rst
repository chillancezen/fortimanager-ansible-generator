:source: fmgr_pm_config_obj_webfilter_urlfilter_entries_per_object.py

:orphan:

.. _fmgr_pm_config_obj_webfilter_urlfilter_entries_per_object:

fmgr_pm_config_obj_webfilter_urlfilter_entries_per_object -- URL filter entries.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, move, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/webfilter/urlfilter/{urlfilter}/entries/{entries}`
- `/pm/config/global/obj/webfilter/urlfilter/{urlfilter}/entries/{entries}`
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
 <li><span class="li-head">entries</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - URL filter entries.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
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
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - URL filter entries.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - URL filter entries.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [move]</span> - URL filter entries.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [before, after]</span> </li>
 <li><span class="li-head">target</span> - Key to the target entry. <span class="li-normal">type: str</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WEBFILTER/URLFILTER/{URLFILTER}/ENTRIES/{ENTRIES}
      fmgr_pm_config_obj_webfilter_urlfilter_entries_per_object:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            urlfilter: <value of string>
            entries: <value of string>
         params:
            -
               data:
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

    - name: REQUESTING /PM/CONFIG/OBJ/WEBFILTER/URLFILTER/{URLFILTER}/ENTRIES/{ENTRIES}
      fmgr_pm_config_obj_webfilter_urlfilter_entries_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            urlfilter: <value of string>
            entries: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/WEBFILTER/URLFILTER/{URLFILTER}/ENTRIES/{ENTRIES}
      fmgr_pm_config_obj_webfilter_urlfilter_entries_per_object:
         method: <value in [move]>
         url_params:
            adom: <value in [none, global, custom dom]>
            urlfilter: <value of string>
            entries: <value of string>
         params:
            -
               option: <value in [before, after]>
               target: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [clone, move, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - Id. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/webfilter/urlfilter/{urlfilter}/entries/{entries}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [delete]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/webfilter/urlfilter/{urlfilter}/entries/{entries}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
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
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/webfilter/urlfilter/{urlfilter}/entries/{entries}</span>  </li>
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



