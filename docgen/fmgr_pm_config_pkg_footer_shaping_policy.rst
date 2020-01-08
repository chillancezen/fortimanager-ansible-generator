:source: fmgr_pm_config_pkg_footer_shaping_policy.py

:orphan:

.. _fmgr_pm_config_pkg_footer_shaping_policy:

fmgr_pm_config_pkg_footer_shaping_policy
++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/global/pkg/{pkg}/global/footer/shaping-policy`
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
 <li><span class="li-head">pkg</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">app-category</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">app-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">application</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">class-id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">diffserv-forward</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">diffserv-reverse</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">diffservcode-forward</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">diffservcode-rev</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstaddr6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstintf</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">groups</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">internet-service</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">internet-service-custom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-custom-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-id</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-src</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">internet-service-src-custom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-src-custom-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-src-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">internet-service-src-id</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip-version</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [4, 6]</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">per-ip-shaper</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">schedule</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcaddr6</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">srcintf</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">tos</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tos-mask</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tos-negate</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">traffic-shaper</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">traffic-shaper-reverse</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">url-category</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">users</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [app-category, app-group, application, class-id, comment, diffserv-forward, diffserv-reverse, diffservcode-forward, diffservcode-rev, dstaddr, dstaddr6, dstintf, groups, id, internet-service, internet-service-custom, internet-service-custom-group, internet-service-group, internet-service-id, internet-service-src, internet-service-src-custom, internet-service-src-custom-group, internet-service-src-group, internet-service-src-id, ip-version, name, per-ip-shaper, schedule, service, srcaddr, srcaddr6, srcintf, status, tos, tos-mask, tos-negate, traffic-shaper, traffic-shaper-reverse, url-category, users]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FOOTER/SHAPING-POLICY
      fmgr_pm_config_pkg_footer_shaping_policy:
         method: <value in [add, set, update]>
         url_params:
            pkg: <value of string>
         params:
            -
               data:
                 -
                     app-category: <value of string>
                     app-group: <value of string>
                     application:
                       - <value of integer>
                     class-id: <value of integer>
                     comment: <value of string>
                     diffserv-forward: <value in [disable, enable]>
                     diffserv-reverse: <value in [disable, enable]>
                     diffservcode-forward: <value of string>
                     diffservcode-rev: <value of string>
                     dstaddr: <value of string>
                     dstaddr6: <value of string>
                     dstintf: <value of string>
                     groups: <value of string>
                     id: <value of integer>
                     internet-service: <value in [disable, enable]>
                     internet-service-custom: <value of string>
                     internet-service-custom-group: <value of string>
                     internet-service-group: <value of string>
                     internet-service-id: <value of string>
                     internet-service-src: <value in [disable, enable]>
                     internet-service-src-custom: <value of string>
                     internet-service-src-custom-group: <value of string>
                     internet-service-src-group: <value of string>
                     internet-service-src-id: <value of string>
                     ip-version: <value in [4, 6]>
                     name: <value of string>
                     per-ip-shaper: <value of string>
                     schedule: <value of string>
                     service: <value of string>
                     srcaddr: <value of string>
                     srcaddr6: <value of string>
                     srcintf: <value of string>
                     status: <value in [disable, enable]>
                     tos: <value of string>
                     tos-mask: <value of string>
                     tos-negate: <value in [disable, enable]>
                     traffic-shaper: <value of string>
                     traffic-shaper-reverse: <value of string>
                     url-category: <value of string>
                     users: <value of string>

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FOOTER/SHAPING-POLICY
      fmgr_pm_config_pkg_footer_shaping_policy:
         method: <value in [get]>
         url_params:
            pkg: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [app-category, app-group, application, ...]>
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
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/global/pkg/{pkg}/global/footer/shaping-policy</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> app-category </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> app-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> application </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> class-id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comment </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> diffserv-forward </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> diffserv-reverse </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> diffservcode-forward </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> diffservcode-rev </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstaddr </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstaddr6 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstintf </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> groups </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> internet-service </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-custom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-custom-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-id </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-src </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-src-custom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-src-custom-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-src-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> internet-service-src-id </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip-version </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> per-ip-shaper </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> schedule </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> service </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcaddr </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcaddr6 </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> srcintf </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tos </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tos-mask </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tos-negate </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> traffic-shaper </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> traffic-shaper-reverse </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> url-category </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> users </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/global/pkg/{pkg}/global/footer/shaping-policy</span>  </li>
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



