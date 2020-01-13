:source: fmgr_system_ntp.py

:orphan:

.. _fmgr_system_ntp:

fmgr_system_ntp -- NTP settings.
++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/ntp`
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
 <li><span class="li-head">parameters for method: [get]</span> - NTP settings.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - NTP settings.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">ntpserver</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">authentication</span> - Enable/disable MD5 authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">id</span> - Time server ID. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">key</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC MTIwNDIxMDA1OTc0MDU5OOCz7ir5CgpbO/J3sN576PgSwbGc703sZpBwnR5CmNxRjhfSM2FPskJvCPZHAzZOjFTd7B1Ay0Ssf3MwFzNWVdOYL88mw7WTGYgcc3j/PFmJ0NiPwuFnT94rAO6yDHtO7QnVfyla+di36FC34BfdtB+S9eva</span> </li>
 </ul>
 <li><span class="li-head">key-id</span> - Key ID for authentication. <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">ntpv3</span> - Enable/disable NTPv3. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">server</span> - IP address/hostname of NTP Server. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">status</span> - Enable/disable NTP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">sync_interval</span> - NTP sync interval (min). <span class="li-normal">type: int</span>  <span class="li-normal">default: 60</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/NTP
      fmgr_system_ntp:
         method: <value in [set, update]>
         params:
            -
               data:
                  ntpserver:
                    -
                        authentication: <value in [disable, enable] default: 'disable'>
                        id: <value of integer default: 0>
                        key:
                          - <value of string default: 'ENC MTIwNDIxMDA1OTc0MDU5OOCz7ir5CgpbO/J3sN576PgSwbGc703sZpBwnR5CmNxRjhfSM2FP...'>
                        key-id: <value of integer default: 0>
                        ntpv3: <value in [disable, enable] default: 'disable'>
                        server: <value of string>
                  status: <value in [disable, enable] default: 'disable'>
                  sync_interval: <value of integer default: 60>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> ntpserver </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> authentication </span> - Enable/disable MD5 authentication. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> id </span> - Time server ID. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> key </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC MTIwNDIxMDA1OTc0MDU5OOCz7ir5CgpbO/J3sN576PgSwbGc703sZpBwnR5CmNxRjhfSM2FPskJvCPZHAzZOjFTd7B1Ay0Ssf3MwFzNWVdOYL88mw7WTGYgcc3j/PFmJ0NiPwuFnT94rAO6yDHtO7QnVfyla+di36FC34BfdtB+S9eva</span>  </li>
 </ul>
 <li> <span class="li-return"> key-id </span> - Key ID for authentication. <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> ntpv3 </span> - Enable/disable NTPv3. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> server </span> - IP address/hostname of NTP Server. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> status </span> - Enable/disable NTP. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> sync_interval </span> - NTP sync interval (min). <span class="li-normal">type: int</span>  <span class="li-normal">example: 60</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/ntp</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/ntp</span>  </li>
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



