:source: fmgr_cli_system_mail_mail.py

:orphan:

.. _fmgr_cli_system_mail_mail:

fmgr_cli_system_mail_mail -- Alert emails.
++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[delete, get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/mail/{mail}`
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
 <li><span class="li-head">mail</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [delete, get]</span> - Alert emails.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Alert emails.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">auth</span> - Enable authentication. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">id</span> - Mail Service ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">passwd</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC MTI3MTE1Mzc2NTkxNzM3My6VraLxNsD7/K6FZ6oYkYSCjr1/h55a1R9hSJwHMCRyMEgllLUQEhRyvo6NfN3em5zkIyjoe2lL1IiVMHB7akT/z/3KthjsAi7XxuoMxrrTCD22xfmlCWUL9Ic7XgFbGqD4FPOGs6XKMCTZ0SdI+YEcf+pp</span> </li>
 </ul>
 <li><span class="li-head">port</span> - SMTP server port. <span class="li-normal">type: int</span>  <span class="li-normal">default: 25</span> </li>
 <li><span class="li-head">secure-option</span> - Communication secure option. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, none, smtps, starttls]</span>  <span class="li-normal">default: default</span> </li>
 <li><span class="li-head">server</span> - SMTP server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">user</span> - SMTP account username. <span class="li-normal">type: str</span> </li>
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
    - name: send request to /cli/system/mail/{mail}
      fmgr_cli_system_mail_mail:
         method: <value in [set, update]>
         url_params:
            mail: <value of string>
         params:
            - 
               data: 
                  auth: <value in [disable, enable] default: disable>
                  id: <value of string>
                  passwd: 
                   - <value of string default: ENC MTI3MTE1Mzc2NTkxNzM3My6VraLxNsD7/K6FZ6oYkYSCjr1/h55a1R9hSJwHMCRyMEgllLUQEhRyvo6NfN3em5zkIyjoe2lL1IiVMHB7akT/z/3KthjsAi7XxuoMxrrTCD22xfmlCWUL9Ic7XgFbGqD4FPOGs6XKMCTZ0SdI+YEcf+pp>
                  port: <value of integer default: 25>
                  secure-option: <value in [default, none, smtps, ...] default: default>
                  server: <value of string>
                  user: <value of string>



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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/mail/{mail}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> auth </span> - Enable authentication. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> id </span> - Mail Service ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> passwd </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC MTI3MTE1Mzc2NTkxNzM3My6VraLxNsD7/K6FZ6oYkYSCjr1/h55a1R9hSJwHMCRyMEgllLUQEhRyvo6NfN3em5zkIyjoe2lL1IiVMHB7akT/z/3KthjsAi7XxuoMxrrTCD22xfmlCWUL9Ic7XgFbGqD4FPOGs6XKMCTZ0SdI+YEcf+pp</span>  </li>
 </ul>
 <li> <span class="li-return"> port </span> - SMTP server port. <span class="li-normal">type: int</span>  <span class="li-normal">example: 25</span>  </li>
 <li> <span class="li-return"> secure-option </span> - Communication secure option. <span class="li-normal">type: str</span>  <span class="li-normal">example: default</span>  </li>
 <li> <span class="li-return"> server </span> - SMTP server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> user </span> - SMTP account username. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/mail/{mail}</span>  </li>
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



