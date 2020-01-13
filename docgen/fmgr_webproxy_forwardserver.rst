:source: fmgr_webproxy_forwardserver.py

:orphan:

.. _fmgr_webproxy_forwardserver:

fmgr_webproxy_forwardserver -- Configure forward-server addresses.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/web-proxy/forward-server`
- `/pm/config/global/obj/web-proxy/forward-server`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure forward-server addresses.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">addr-type</span> - Address type of the forwarding proxy server: IP or FQDN. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [fqdn, ip]</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fqdn</span> - Forward server Fully Qualified Domain Name (FQDN). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">healthcheck</span> - Enable/disable forward server health checking. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ip</span> - Forward proxy server IP address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">monitor</span> - URL for forward server health check monitoring (default = http://www. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Server name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port</span> - Port number that the forwarding server expects to receive HTTP sessions on (1 - 65535, default = 3128). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">server-down-option</span> - Action to take when the forward server is found to be down: block sessions until the server is back up or pass sessions to their destination. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [block, pass]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure forward-server addresses.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [addr-type, comment, fqdn, healthcheck, ip, monitor, name, port, server-down-option]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WEB-PROXY/FORWARD-SERVER
      fmgr_webproxy_forwardserver:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     addr-type: <value in [fqdn, ip]>
                     comment: <value of string>
                     fqdn: <value of string>
                     healthcheck: <value in [disable, enable]>
                     ip: <value of string>
                     monitor: <value of string>
                     name: <value of string>
                     port: <value of integer>
                     server-down-option: <value in [block, pass]>

    - name: REQUESTING /PM/CONFIG/OBJ/WEB-PROXY/FORWARD-SERVER
      fmgr_webproxy_forwardserver:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [addr-type, comment, fqdn, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/web-proxy/forward-server</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> addr-type </span> - Address type of the forwarding proxy server: IP or FQDN. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> comment </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fqdn </span> - Forward server Fully Qualified Domain Name (FQDN). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> healthcheck </span> - Enable/disable forward server health checking. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip </span> - Forward proxy server IP address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> monitor </span> - URL for forward server health check monitoring (default = http://www. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Server name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port </span> - Port number that the forwarding server expects to receive HTTP sessions on (1 - 65535, default = 3128). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> server-down-option </span> - Action to take when the forward server is found to be down: block sessions until the server is back up or pass sessions to their destination. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/web-proxy/forward-server</span>  </li>
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



