:source: fmgr_system_connector.py

:orphan:

.. _fmgr_system_connector:

fmgr_system_connector -- Configure connector.
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/connector`
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
 <li><span class="li-head">parameters for method: [get]</span> - Configure connector.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Configure connector.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">fsso-refresh-interval</span> - FSSO refresh interval (60 - 1800 seconds). <span class="li-normal">type: int</span>  <span class="li-normal">default: 180</span> </li>
 <li><span class="li-head">fsso-sess-timeout</span> - FSSO session timeout (30 - 600 seconds). <span class="li-normal">type: int</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">px-refresh-interval</span> - pxGrid refresh interval (60 - 1800 seconds). <span class="li-normal">type: int</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">px-svr-timeout</span> - pxGrid server timeout (30 - 600 seconds). <span class="li-normal">type: int</span>  <span class="li-normal">default: 900</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/CONNECTOR
      fmgr_system_connector:
         method: <value in [set, update]>
         params:
            -
               data:
                  fsso-refresh-interval: <value of integer default: 180>
                  fsso-sess-timeout: <value of integer default: 300>
                  px-refresh-interval: <value of integer default: 300>
                  px-svr-timeout: <value of integer default: 900>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> fsso-refresh-interval </span> - FSSO refresh interval (60 - 1800 seconds). <span class="li-normal">type: int</span>  <span class="li-normal">example: 180</span>  </li>
 <li> <span class="li-return"> fsso-sess-timeout </span> - FSSO session timeout (30 - 600 seconds). <span class="li-normal">type: int</span>  <span class="li-normal">example: 300</span>  </li>
 <li> <span class="li-return"> px-refresh-interval </span> - pxGrid refresh interval (60 - 1800 seconds). <span class="li-normal">type: int</span>  <span class="li-normal">example: 300</span>  </li>
 <li> <span class="li-return"> px-svr-timeout </span> - pxGrid server timeout (30 - 600 seconds). <span class="li-normal">type: int</span>  <span class="li-normal">example: 900</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/connector</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/connector</span>  </li>
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



