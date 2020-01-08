:source: fmgr_pm_config_obj_firewall_proxy_address.py

:orphan:

.. _fmgr_pm_config_obj_firewall_proxy_address:

fmgr_pm_config_obj_firewall_proxy_address -- Web proxy address configuration.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/proxy-address`
- `/pm/config/global/obj/firewall/proxy-address`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Web proxy address configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">case-sensitivity</span> - Enable to make the pattern case sensitive. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">category</span> - FortiGuard category ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">color</span> - Integer value to determine the color of the icon in the GUI (1 - 32, default = 0, which sets value to 1). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - Optional comments. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">header</span> - HTTP header name as a regular expression. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">header-group</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">case-sensitivity</span> - Case sensitivity in pattern. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">header</span> - HTTP header regular expression. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">header-name</span> - HTTP header. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">header-name</span> - Name of HTTP header. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">host</span> - Address object for the host. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">host-regex</span> - Host name as a regular expression. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">method</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [delete, get, head, options, post, put, trace, connect]</span> </li>
 </ul>
 <li><span class="li-head">name</span> - Address name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">path</span> - URL path as a regular expression. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">query</span> - Match the query part of the URL as a regular expression. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">referrer</span> - Enable/disable use of referrer field in the HTTP header to match the address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tagging</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">category</span> - Tag category. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Tagging entry name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tags</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">type</span> - Proxy address type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [host-regex, url, category, method, ua, header, src-advanced, dst-advanced]</span> </li>
 <li><span class="li-head">ua</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [chrome, ms, firefox, safari, other]</span> </li>
 </ul>
 <li><span class="li-head">uuid</span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">visibility</span> - Enable/disable visibility of the object in the GUI. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Web proxy address configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [case-sensitivity, category, color, comment, header, header-name, host, host-regex, method, name, path, query, referrer, type, ua, uuid, visibility]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/PROXY-ADDRESS
      fmgr_pm_config_obj_firewall_proxy_address:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     case-sensitivity: <value in [disable, enable]>
                     category: <value of string>
                     color: <value of integer>
                     comment: <value of string>
                     header: <value of string>
                     header-group:
                       -
                           case-sensitivity: <value in [disable, enable]>
                           header: <value of string>
                           header-name: <value of string>
                           id: <value of integer>
                     header-name: <value of string>
                     host: <value of string>
                     host-regex: <value of string>
                     method:
                       - <value in [delete, get, head, ...]>
                     name: <value of string>
                     path: <value of string>
                     query: <value of string>
                     referrer: <value in [disable, enable]>
                     tagging:
                       -
                           category: <value of string>
                           name: <value of string>
                           tags:
                             - <value of string>
                     type: <value in [host-regex, url, category, ...]>
                     ua:
                       - <value in [chrome, ms, firefox, ...]>
                     uuid: <value of string>
                     visibility: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/PROXY-ADDRESS
      fmgr_pm_config_obj_firewall_proxy_address:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [case-sensitivity, category, color, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/proxy-address</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> case-sensitivity </span> - Enable to make the pattern case sensitive. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> category </span> - FortiGuard category ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> color </span> - Integer value to determine the color of the icon in the GUI (1 - 32, default = 0, which sets value to 1). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comment </span> - Optional comments. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> header </span> - HTTP header name as a regular expression. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> header-group </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> case-sensitivity </span> - Case sensitivity in pattern. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> header </span> - HTTP header regular expression. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> header-name </span> - HTTP header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> header-name </span> - Name of HTTP header. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> host </span> - Address object for the host. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> host-regex </span> - Host name as a regular expression. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> method </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> name </span> - Address name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> path </span> - URL path as a regular expression. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> query </span> - Match the query part of the URL as a regular expression. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> referrer </span> - Enable/disable use of referrer field in the HTTP header to match the address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tagging </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> category </span> - Tag category. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Tagging entry name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tags </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 </ul>
 <li> <span class="li-return"> type </span> - Proxy address type. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ua </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> uuid </span> - Universally Unique Identifier (UUID; automatically assigned but can be manually reset). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> visibility </span> - Enable/disable visibility of the object in the GUI. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/proxy-address</span>  </li>
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



