:source: fmgr_firewall_internetservice.py

:orphan:

.. _fmgr_firewall_internetservice:

fmgr_firewall_internetservice -- Show Internet Service application.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/internet-service`
- `/pm/config/global/obj/firewall/internet-service`
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
 <li><span class="li-head">parameters for method: [get]</span> - Show Internet Service application.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Show Internet Service application.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">database</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [isdb, irdb]</span> </li>
 <li><span class="li-head">direction</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [src, dst, both]</span> </li>
 <li><span class="li-head">entry</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - Entry ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip-number</span> - Total number of IP addresses. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip-range-number</span> - Total number of IP ranges. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">port</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">protocol</span> - Integer value for the protocol type as defined by IANA (0 - 255). <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">icon-id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">offset</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">reputation</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">sld-id</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/INTERNET-SERVICE
      fmgr_firewall_internetservice:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/INTERNET-SERVICE
      fmgr_firewall_internetservice:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                  database: <value in [isdb, irdb]>
                  direction: <value in [src, dst, both]>
                  entry:
                    -
                        id: <value of integer>
                        ip-number: <value of integer>
                        ip-range-number: <value of integer>
                        port:
                          - <value of integer>
                        protocol: <value of integer>
                  icon-id: <value of integer>
                  id: <value of integer>
                  name: <value of string>
                  offset: <value of integer>
                  reputation: <value of integer>
                  sld-id: <value of integer>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> database </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> direction </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> entry </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - Entry ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip-number </span> - Total number of IP addresses. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip-range-number </span> - Total number of IP ranges. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> port </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> protocol </span> - Integer value for the protocol type as defined by IANA (0 - 255). <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> icon-id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> offset </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> reputation </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> sld-id </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/internet-service</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/internet-service</span>  </li>
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



