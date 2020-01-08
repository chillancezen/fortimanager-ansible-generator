:source: fmgr_cli_system_saml.py

:orphan:

.. _fmgr_cli_system_saml:

fmgr_cli_system_saml -- Global settings for SAML authentication.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/saml`
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
 <li><span class="li-head">parameters for method: [get]</span> - Global settings for SAML authentication.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Global settings for SAML authentication.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">acs-url</span> - SP ACS(login) URL. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">cert</span> - Certificate name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">entity-id</span> - SP entity ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-cert</span> - IDP Certificate name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-entity-id</span> - IDP entity ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-single-logout-url</span> - IDP single logout url. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-single-sign-on-url</span> - IDP single sign-on URL. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">login-auto-redirect</span> - Enable/Disable auto redirect to IDP login page. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">role</span> - SAML role. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [IDP, SP]</span>  <span class="li-normal">default: SP</span> </li>
 <li><span class="li-head">server-address</span> - server address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">service-providers</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">idp-entity-id</span> - IDP Entity ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-single-logout-url</span> - IDP single logout url. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">idp-single-sign-on-url</span> - IDP single sign-on URL. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">prefix</span> - Prefix. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sp-cert</span> - SP certificate name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sp-entity-id</span> - SP Entity ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sp-single-logout-url</span> - SP single logout URL. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sp-single-sign-on-url</span> - SP single sign-on URL. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">sls-url</span> - SP SLS(logout) URL. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable SAML authentication (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/SAML
      fmgr_cli_system_saml:
         method: <value in [set, update]>
         params:
            -
               data:
                  acs-url: <value of string>
                  cert: <value of string>
                  entity-id: <value of string>
                  idp-cert: <value of string>
                  idp-entity-id: <value of string>
                  idp-single-logout-url: <value of string>
                  idp-single-sign-on-url: <value of string>
                  login-auto-redirect: <value in [disable, enable] default: 'disable'>
                  role: <value in [IDP, SP] default: 'SP'>
                  server-address: <value of string>
                  service-providers:
                    -
                        idp-entity-id: <value of string>
                        idp-single-logout-url: <value of string>
                        idp-single-sign-on-url: <value of string>
                        name: <value of string>
                        prefix: <value of string>
                        sp-cert: <value of string>
                        sp-entity-id: <value of string>
                        sp-single-logout-url: <value of string>
                        sp-single-sign-on-url: <value of string>
                  sls-url: <value of string>
                  status: <value in [disable, enable] default: 'disable'>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> acs-url </span> - SP ACS(login) URL. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> cert </span> - Certificate name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> entity-id </span> - SP entity ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> idp-cert </span> - IDP Certificate name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> idp-entity-id </span> - IDP entity ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> idp-single-logout-url </span> - IDP single logout url. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> idp-single-sign-on-url </span> - IDP single sign-on URL. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> login-auto-redirect </span> - Enable/Disable auto redirect to IDP login page. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> role </span> - SAML role. <span class="li-normal">type: str</span>  <span class="li-normal">example: SP</span>  </li>
 <li> <span class="li-return"> server-address </span> - server address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> service-providers </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> idp-entity-id </span> - IDP Entity ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> idp-single-logout-url </span> - IDP single logout url. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> idp-single-sign-on-url </span> - IDP single sign-on URL. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> prefix </span> - Prefix. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sp-cert </span> - SP certificate name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sp-entity-id </span> - SP Entity ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sp-single-logout-url </span> - SP single logout URL. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sp-single-sign-on-url </span> - SP single sign-on URL. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> sls-url </span> - SP SLS(logout) URL. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable SAML authentication (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/saml</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/saml</span>  </li>
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



