:source: fmgr_webproxy_wisp_obj.py

:orphan:

.. _fmgr_webproxy_wisp_obj:

fmgr_webproxy_wisp_obj -- Configure Wireless Internet service provider (WISP) servers.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/web-proxy/wisp/{wisp}`
- `/pm/config/global/obj/web-proxy/wisp/{wisp}`
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
 <li><span class="li-head">wisp</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure Wireless Internet service provider (WISP) servers.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">max-connections</span> - Maximum number of web proxy WISP connections (4 - 4096, default = 64). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - Server name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">outgoing-ip</span> - WISP outgoing IP address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server-ip</span> - WISP server IP address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server-port</span> - WISP server port (1 - 65535, default = 15868). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">timeout</span> - Period of time before WISP requests time out (1 - 15 sec, default = 5). <span class="li-normal">type: int</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure Wireless Internet service provider (WISP) servers.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure Wireless Internet service provider (WISP) servers.</li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WEB-PROXY/WISP/{WISP}
      fmgr_webproxy_wisp_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wisp: <value of string>
         params:
            -
               data:
                  comment: <value of string>
                  max-connections: <value of integer>
                  name: <value of string>
                  outgoing-ip: <value of string>
                  server-ip: <value of string>
                  server-port: <value of integer>
                  timeout: <value of integer>

    - name: REQUESTING /PM/CONFIG/OBJ/WEB-PROXY/WISP/{WISP}
      fmgr_webproxy_wisp_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wisp: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [clone, delete, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/web-proxy/wisp/{wisp}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> comment </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> max-connections </span> - Maximum number of web proxy WISP connections (4 - 4096, default = 64). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> name </span> - Server name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> outgoing-ip </span> - WISP outgoing IP address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server-ip </span> - WISP server IP address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server-port </span> - WISP server port (1 - 65535, default = 15868). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> timeout </span> - Period of time before WISP requests time out (1 - 15 sec, default = 5). <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/web-proxy/wisp/{wisp}</span>  </li>
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



