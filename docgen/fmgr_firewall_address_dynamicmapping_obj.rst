:source: fmgr_firewall_address_dynamicmapping_obj.py

:orphan:

.. _fmgr_firewall_address_dynamicmapping_obj:

fmgr_firewall_address_dynamicmapping_obj
++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/address/{address}/dynamic_mapping/{dynamic_mapping}`
- `/pm/config/global/obj/firewall/address/{address}/dynamic_mapping/{dynamic_mapping}`
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
 <li><span class="li-head">address</span> - the object name <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dynamic_mapping</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - </li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">_scope</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vdom</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">allow-routing</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">associated-interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cache-ttl</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">color</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">comment</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">country</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">end-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">end-mac</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">epg-name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fqdn</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">interface</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">obj-id</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">organization</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">policy-group</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sdn</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [aci, aws, nsx, nuage, azure, gcp, oci, openstack]</span> </li>
 <li><span class="li-head">sdn-addr-type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [private, public, all]</span> </li>
 <li><span class="li-head">sdn-tag</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">start-ip</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">start-mac</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">subnet</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">subnet-name</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tags</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tenant</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipmask, iprange, fqdn, wildcard, geography, url, wildcard-fqdn, nsx, aws, dynamic, interface-subnet, mac]</span> </li>
 <li><span class="li-head">url</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">uuid</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">visibility</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">wildcard</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">wildcard-fqdn</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - </li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/ADDRESS/{ADDRESS}/DYNAMIC_MAPPING/{DYNAMIC_MAPPING}
      fmgr_firewall_address_dynamicmapping_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            address: <value of string>
            dynamic_mapping: <value of string>
         params:
            -
               data:
                  _scope:
                    -
                        name: <value of string>
                        vdom: <value of string>
                  allow-routing: <value in [disable, enable]>
                  associated-interface: <value of string>
                  cache-ttl: <value of integer>
                  color: <value of integer>
                  comment: <value of string>
                  country: <value of string>
                  end-ip: <value of string>
                  end-mac: <value of string>
                  epg-name: <value of string>
                  filter: <value of string>
                  fqdn: <value of string>
                  interface: <value of string>
                  obj-id: <value of string>
                  organization: <value of string>
                  policy-group: <value of string>
                  sdn: <value in [aci, aws, nsx, ...]>
                  sdn-addr-type: <value in [private, public, all]>
                  sdn-tag: <value of string>
                  start-ip: <value of string>
                  start-mac: <value of string>
                  subnet: <value of string>
                  subnet-name: <value of string>
                  tags: <value of string>
                  tenant: <value of string>
                  type: <value in [ipmask, iprange, fqdn, ...]>
                  url: <value of string>
                  uuid: <value of string>
                  visibility: <value in [disable, enable]>
                  wildcard: <value of string>
                  wildcard-fqdn: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/ADDRESS/{ADDRESS}/DYNAMIC_MAPPING/{DYNAMIC_MAPPING}
      fmgr_firewall_address_dynamicmapping_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            address: <value of string>
            dynamic_mapping: <value of string>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/address/{address}/dynamic_mapping/{dynamic_mapping}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> _scope </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vdom </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> allow-routing </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> associated-interface </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> cache-ttl </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> color </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> comment </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> country </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> end-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> end-mac </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> epg-name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> filter </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fqdn </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> interface </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> obj-id </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> organization </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> policy-group </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sdn </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sdn-addr-type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sdn-tag </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> start-ip </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> start-mac </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> subnet </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> subnet-name </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tags </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tenant </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> url </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> uuid </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> visibility </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wildcard </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> wildcard-fqdn </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/address/{address}/dynamic_mapping/{dynamic_mapping}</span>  </li>
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



