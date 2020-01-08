:source: fmgr_cli_system_saml_service_providers_per_object.py

:orphan:

.. _fmgr_cli_system_saml_service_providers_per_object:

fmgr_cli_system_saml_service_providers_per_object -- Authorized service providers.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[delete, get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/saml/service-providers/{service-providers}`
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
 <li><span class="li-head">service-providers</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [delete, get]</span> - Authorized service providers.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Authorized service providers.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
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

    - name: REQUESTING /CLI/SYSTEM/SAML/SERVICE-PROVIDERS/{SERVICE-PROVIDERS}
      fmgr_cli_system_saml_service_providers_per_object:
         method: <value in [set, update]>
         url_params:
            service-providers: <value of string>
         params:
            -
               data:
                  idp-entity-id: <value of string>
                  idp-single-logout-url: <value of string>
                  idp-single-sign-on-url: <value of string>
                  name: <value of string>
                  prefix: <value of string>
                  sp-cert: <value of string>
                  sp-entity-id: <value of string>
                  sp-single-logout-url: <value of string>
                  sp-single-sign-on-url: <value of string>



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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/saml/service-providers/{service-providers}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
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
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/saml/service-providers/{service-providers}</span>  </li>
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



