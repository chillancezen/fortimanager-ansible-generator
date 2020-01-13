:source: fmgr_pkg_firewall_centralsnatmap_obj.py

:orphan:

.. _fmgr_pkg_firewall_centralsnatmap_obj:

fmgr_pkg_firewall_centralsnatmap_obj -- Configure central SNAT policies.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, move, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/pkg/{pkg}/firewall/central-snat-map/{central-snat-map}`
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
 <li><span class="li-head">pkg</span> - the object name <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">central-snat-map</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure central SNAT policies.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">dst-addr</span> - Destination address name from available addresses. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dstintf</span> - Destination interface name from available interfaces. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nat</span> - Enable/disable source NAT. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">nat-ippool</span> - Name of the IP pools to be used to translate addresses from available IP Pools. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nat-port</span> - Translated port or port range (0 to 65535). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">orig-addr</span> - Original address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">orig-port</span> - Original TCP port (0 to 65535). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">policyid</span> - Policy ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">protocol</span> - Integer value for the protocol type (0 - 255). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">srcintf</span> - Source interface name from available interfaces. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable the active status of this policy. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure central SNAT policies.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure central SNAT policies.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [move]</span> - Configure central SNAT policies.</li>
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

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/CENTRAL-SNAT-MAP/{CENTRAL-SNAT-MAP}
      fmgr_pkg_firewall_centralsnatmap_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            central-snat-map: <value of string>
         params:
            -
               data:
                  dst-addr: <value of string>
                  dstintf: <value of string>
                  nat: <value in [disable, enable]>
                  nat-ippool: <value of string>
                  nat-port: <value of string>
                  orig-addr: <value of string>
                  orig-port: <value of integer>
                  policyid: <value of integer>
                  protocol: <value of integer>
                  srcintf: <value of string>
                  status: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/CENTRAL-SNAT-MAP/{CENTRAL-SNAT-MAP}
      fmgr_pkg_firewall_centralsnatmap_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            central-snat-map: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/PKG/{PKG}/FIREWALL/CENTRAL-SNAT-MAP/{CENTRAL-SNAT-MAP}
      fmgr_pkg_firewall_centralsnatmap_obj:
         method: <value in [move]>
         url_params:
            adom: <value in [none, global, custom dom]>
            pkg: <value of string>
            central-snat-map: <value of string>
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
 <li> <span class="li-return"> policyid </span> - Policy ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/central-snat-map/{central-snat-map}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [delete]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/central-snat-map/{central-snat-map}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> dst-addr </span> - Destination address name from available addresses. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dstintf </span> - Destination interface name from available interfaces. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> nat </span> - Enable/disable source NAT. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> nat-ippool </span> - Name of the IP pools to be used to translate addresses from available IP Pools. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> nat-port </span> - Translated port or port range (0 to 65535). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> orig-addr </span> - Original address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> orig-port </span> - Original TCP port (0 to 65535). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> policyid </span> - Policy ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> protocol </span> - Integer value for the protocol type (0 - 255). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> srcintf </span> - Source interface name from available interfaces. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable the active status of this policy. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/pkg/{pkg}/firewall/central-snat-map/{central-snat-map}</span>  </li>
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



