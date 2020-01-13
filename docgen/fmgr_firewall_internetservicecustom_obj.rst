:source: fmgr_firewall_internetservicecustom_obj.py

:orphan:

.. _fmgr_firewall_internetservicecustom_obj:

fmgr_firewall_internetservicecustom_obj -- Configure custom Internet Services.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/internet-service-custom/{internet-service-custom}`
- `/pm/config/global/obj/firewall/internet-service-custom/{internet-service-custom}`
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
 <li><span class="li-head">internet-service-custom</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure custom Internet Services.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">disable-entry</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - Disable entry ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip-range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">end-ip</span> - End IP address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Disable entry range ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">start-ip</span> - Start IP address. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">port</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">protocol</span> - Integer value for the protocol type as defined by IANA (0 - 255). <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">entry</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">dst</span> - Destination address or address group name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Entry ID(1-255). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">port-range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">end-port</span> - Integer value for ending TCP/UDP/SCTP destination port in range (1 to 65535). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">id</span> - Custom entry port range ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">start-port</span> - Integer value for starting TCP/UDP/SCTP destination port in range (1 to 65535). <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">protocol</span> - Integer value for the protocol type as defined by IANA (0 - 255). <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">master-service-id</span> - Internet Service ID in the Internet Service database. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Internet Service name. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure custom Internet Services.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure custom Internet Services.</li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/INTERNET-SERVICE-CUSTOM/{INTERNET-SERVICE-CUSTOM}
      fmgr_firewall_internetservicecustom_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            internet-service-custom: <value of string>
         params:
            -
               data:
                  comment: <value of string>
                  disable-entry:
                    -
                        id: <value of integer>
                        ip-range:
                          -
                              end-ip: <value of string>
                              id: <value of integer>
                              start-ip: <value of string>
                        port:
                          - <value of integer>
                        protocol: <value of integer>
                  entry:
                    -
                        dst: <value of string>
                        id: <value of integer>
                        port-range:
                          -
                              end-port: <value of integer>
                              id: <value of integer>
                              start-port: <value of integer>
                        protocol: <value of integer>
                  master-service-id: <value of string>
                  name: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/INTERNET-SERVICE-CUSTOM/{INTERNET-SERVICE-CUSTOM}
      fmgr_firewall_internetservicecustom_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            internet-service-custom: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/internet-service-custom/{internet-service-custom}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> comment </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> disable-entry </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - Disable entry ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip-range </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> end-ip </span> - End IP address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Disable entry range ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> start-ip </span> - Start IP address. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> port </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> protocol </span> - Integer value for the protocol type as defined by IANA (0 - 255). <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> entry </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> dst </span> - Destination address or address group name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Entry ID(1-255). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> port-range </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> end-port </span> - Integer value for ending TCP/UDP/SCTP destination port in range (1 to 65535). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> id </span> - Custom entry port range ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> start-port </span> - Integer value for starting TCP/UDP/SCTP destination port in range (1 to 65535). <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> protocol </span> - Integer value for the protocol type as defined by IANA (0 - 255). <span class="li-normal">type: int</span>  </li>
 </ul>
 <li> <span class="li-return"> master-service-id </span> - Internet Service ID in the Internet Service database. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Internet Service name. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/internet-service-custom/{internet-service-custom}</span>  </li>
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



