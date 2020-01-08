:source: fmgr_cli_system_workflow_approval_matrix_per_object.py

:orphan:

.. _fmgr_cli_system_workflow_approval_matrix_per_object:

fmgr_cli_system_workflow_approval_matrix_per_object -- workflow approval matrix.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[delete, get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/workflow/approval-matrix/{approval-matrix}`
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
 <li><span class="li-head">approval-matrix</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [delete, get]</span> - workflow approval matrix.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - workflow approval matrix.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">adom-name</span> - Adom Name <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">approver</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">member</span> - Member of approver. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">seq_num</span> - Entry number. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 </ul>
 <li><span class="li-head">mail-server</span> - Notify mail server id. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">notify</span> - Notify users <span class="li-normal">type: str</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/WORKFLOW/APPROVAL-MATRIX/{APPROVAL-MATRIX}
      fmgr_cli_system_workflow_approval_matrix_per_object:
         method: <value in [set, update]>
         url_params:
            approval-matrix: <value of string>
         params:
            -
               data:
                  adom-name: <value of string>
                  approver:
                    -
                        member: <value of string>
                        seq_num: <value of integer default: 0>
                  mail-server: <value of string>
                  notify: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [delete, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/workflow/approval-matrix/{approval-matrix}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> adom-name </span> - Adom Name <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> approver </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> member </span> - Member of approver. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> seq_num </span> - Entry number. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 </ul>
 <li> <span class="li-return"> mail-server </span> - Notify mail server id. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> notify </span> - Notify users <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/workflow/approval-matrix/{approval-matrix}</span>  </li>
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



