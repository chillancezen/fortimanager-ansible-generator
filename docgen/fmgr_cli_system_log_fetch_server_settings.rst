:source: fmgr_cli_system_log_fetch_server_settings.py

:orphan:

.. _fmgr_cli_system_log_fetch_server_settings:

fmgr_cli_system_log_fetch_server_settings -- Log-fetch server settings.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/log-fetch/server-settings`
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
 <li><span class="li-head">parameters for method: [get]</span> - Log-fetch server settings.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Log-fetch server settings.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">max-conn-per-session</span> - Max concurrent file download connections per session. <span class="li-normal">type: int</span>  <span class="li-normal">default: 3</span> </li>
 <li><span class="li-head">max-sessions</span> - Max concurrent fetch sessions. <span class="li-normal">type: int</span>  <span class="li-normal">default: 1</span> </li>
 <li><span class="li-head">session-timeout</span> - Fetch session timeout in minute. <span class="li-normal">type: int</span>  <span class="li-normal">default: 10</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/LOG-FETCH/SERVER-SETTINGS
      fmgr_cli_system_log_fetch_server_settings:
         method: <value in [set, update]>
         params:
            -
               data:
                  max-conn-per-session: <value of integer default: 3>
                  max-sessions: <value of integer default: 1>
                  session-timeout: <value of integer default: 10>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> max-conn-per-session </span> - Max concurrent file download connections per session. <span class="li-normal">type: int</span>  <span class="li-normal">example: 3</span>  </li>
 <li> <span class="li-return"> max-sessions </span> - Max concurrent fetch sessions. <span class="li-normal">type: int</span>  <span class="li-normal">example: 1</span>  </li>
 <li> <span class="li-return"> session-timeout </span> - Fetch session timeout in minute. <span class="li-normal">type: int</span>  <span class="li-normal">example: 10</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/log-fetch/server-settings</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/log-fetch/server-settings</span>  </li>
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



