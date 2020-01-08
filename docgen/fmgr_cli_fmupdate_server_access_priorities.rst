:source: fmgr_cli_fmupdate_server_access_priorities.py

:orphan:

.. _fmgr_cli_fmupdate_server_access_priorities:

fmgr_cli_fmupdate_server_access_priorities -- Configure priorities for FortiGate units accessing antivirus updates and web filtering services.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/fmupdate/server-access-priorities`
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
 <li><span class="li-head">parameters for method: [get]</span> - Configure priorities for FortiGate units accessing antivirus updates and web filtering services.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Configure priorities for FortiGate units accessing antivirus updates and web filtering services.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">access-public</span> - Enable/disable FortiGates to Access Public FortiGuard Servers when Private Servers are Unavailable (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">av-ips</span> - Enable/disable Antivirus and IPS Update Service for Private Server(default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">private-server</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - Private server ID (1 - 10). <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">ip</span> - IPv4 address of the FortiManager unit or private server. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">ip6</span> - IPv6 address of the FortiManager unit or private server. <span class="li-normal">type: str</span>  <span class="li-normal">default: ::</span> </li>
 <li><span class="li-head">time_zone</span> - Time zone of the private server (-24 = local time zone, default = -24). <span class="li-normal">type: int</span>  <span class="li-normal">default: -24</span> </li>
 </ul>
 <li><span class="li-head">web-spam</span> - Enable/disable Web Filter and Email Filter Update Service for Private Server (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
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

    - name: REQUESTING /CLI/FMUPDATE/SERVER-ACCESS-PRIORITIES
      fmgr_cli_fmupdate_server_access_priorities:
         method: <value in [set, update]>
         params:
            -
               data:
                  access-public: <value in [disable, enable] default: 'disable'>
                  av-ips: <value in [disable, enable] default: 'disable'>
                  private-server:
                    -
                        id: <value of integer default: 0>
                        ip: <value of string default: '0.0.0.0'>
                        ip6: <value of string default: '::'>
                        time_zone: <value of integer default: -24>
                  web-spam: <value in [disable, enable] default: 'enable'>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> access-public </span> - Enable/disable FortiGates to Access Public FortiGuard Servers when Private Servers are Unavailable (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> av-ips </span> - Enable/disable Antivirus and IPS Update Service for Private Server(default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> private-server </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - Private server ID (1 - 10). <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> ip </span> - IPv4 address of the FortiManager unit or private server. <span class="li-normal">type: str</span>  <span class="li-normal">example: 0.0.0.0</span>  </li>
 <li> <span class="li-return"> ip6 </span> - IPv6 address of the FortiManager unit or private server. <span class="li-normal">type: str</span>  <span class="li-normal">example: ::</span>  </li>
 <li> <span class="li-return"> time_zone </span> - Time zone of the private server (-24 = local time zone, default = -24). <span class="li-normal">type: int</span>  <span class="li-normal">example: -24</span>  </li>
 </ul>
 <li> <span class="li-return"> web-spam </span> - Enable/disable Web Filter and Email Filter Update Service for Private Server (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/fmupdate/server-access-priorities</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/fmupdate/server-access-priorities</span>  </li>
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



