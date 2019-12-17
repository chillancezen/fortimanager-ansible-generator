:source: fmgr_cli_system_alertemail.py

:orphan:

.. _fmgr_cli_system_alertemail:

fmgr_cli_system_alertemail -- Configure alertemail.
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/alertemail`
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
 <li><span class="li-head">parameters for method: [get]</span> - Configure alertemail.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Configure alertemail.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">authentication</span> - Enable/disable authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">fromaddress</span> - SMTP from address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fromname</span> - SMTP from user. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">smtppassword</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC Njc5MTA0OTM4MjgwOTg5NtX0ToVkdnZh0YWA1a11KmRILNzX/SvsNRI6eyvfnHjApM/z3EzMK7RIz4Tk2qBPs5S0q5zHQLjfAJSzBe2Yfs2kceCgazkW3ea31MNNUFHVxVSESpf5MmEMfwrNNUVLeMDdcUJG4FPu7GyP9/KnOBGte1dA</span> </li>
 </ul>
 <li><span class="li-head">smtpport</span> - SMTP server port. <span class="li-normal">type: int</span>  <span class="li-normal">default: 25</span> </li>
 <li><span class="li-head">smtpserver</span> - SMTP server address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">smtpuser</span> - SMTP server user. <span class="li-normal">type: str</span> </li>
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
    - name: send request to /cli/system/alertemail
      fmgr_cli_system_alertemail:
         method: <value in [set, update]>
         params:
            - 
               data: 
                  authentication: <value in [disable, enable] default: enable>
                  fromaddress: <value of string>
                  fromname: <value of string>
                  smtppassword: 
                   - <value of string default: ENC Njc5MTA0OTM4MjgwOTg5NtX0ToVkdnZh0YWA1a11KmRILNzX/SvsNRI6eyvfnHjApM/z3EzMK7RIz4Tk2qBPs5S0q5zHQLjfAJSzBe2Yfs2kceCgazkW3ea31MNNUFHVxVSESpf5MmEMfwrNNUVLeMDdcUJG4FPu7GyP9/KnOBGte1dA>
                  smtpport: <value of integer default: 25>
                  smtpserver: <value of string>
                  smtpuser: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> authentication </span> - Enable/disable authentication. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> fromaddress </span> - SMTP from address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fromname </span> - SMTP from user. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> smtppassword </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC Njc5MTA0OTM4MjgwOTg5NtX0ToVkdnZh0YWA1a11KmRILNzX/SvsNRI6eyvfnHjApM/z3EzMK7RIz4Tk2qBPs5S0q5zHQLjfAJSzBe2Yfs2kceCgazkW3ea31MNNUFHVxVSESpf5MmEMfwrNNUVLeMDdcUJG4FPu7GyP9/KnOBGte1dA</span>  </li>
 </ul>
 <li> <span class="li-return"> smtpport </span> - SMTP server port. <span class="li-normal">type: int</span>  <span class="li-normal">example: 25</span>  </li>
 <li> <span class="li-return"> smtpserver </span> - SMTP server address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> smtpuser </span> - SMTP server user. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/alertemail</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/alertemail</span>  </li>
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



