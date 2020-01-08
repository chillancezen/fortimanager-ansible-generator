:source: fmgr_cli_system_metadata_admins.py

:orphan:

.. _fmgr_cli_system_metadata_admins:

fmgr_cli_system_metadata_admins -- Configure admins.
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/metadata/admins`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure admins.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">fieldlength</span> - Field length. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [20, 50, 255]</span>  <span class="li-normal">default: 50</span> </li>
 <li><span class="li-head">fieldname</span> - Field name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">importance</span> - Field importance. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [optional, required]</span>  <span class="li-normal">default: required</span> </li>
 <li><span class="li-head">status</span> - Field status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, enabled]</span>  <span class="li-normal">default: enabled</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure admins.</li>
 <ul class="ul-self">
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [fieldlength, fieldname, importance, status]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">loadsub</span> - Enable or disable the return of any sub-objects. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [count, syntax]</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/METADATA/ADMINS
      fmgr_cli_system_metadata_admins:
         method: <value in [add, set, update]>
         params:
            -
               data:
                 -
                     fieldlength: <value in [20, 50, 255] default: '50'>
                     fieldname: <value of string>
                     importance: <value in [optional, required] default: 'required'>
                     status: <value in [disabled, enabled] default: 'enabled'>

    - name: REQUESTING /CLI/SYSTEM/METADATA/ADMINS
      fmgr_cli_system_metadata_admins:
         method: <value in [get]>
         params:
            -
               fields:
                 -
                    - <value in [fieldlength, fieldname, importance, ...]>
               filter:
                 - <value of string>
               loadsub: <value of integer>
               option: <value in [count, syntax]>



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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/metadata/admins</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> fieldlength </span> - Field length. <span class="li-normal">type: str</span>  <span class="li-normal">example: 50</span>  </li>
 <li> <span class="li-return"> fieldname </span> - Field name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> importance </span> - Field importance. <span class="li-normal">type: str</span>  <span class="li-normal">example: required</span>  </li>
 <li> <span class="li-return"> status </span> - Field status. <span class="li-normal">type: str</span>  <span class="li-normal">example: enabled</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/metadata/admins</span>  </li>
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



