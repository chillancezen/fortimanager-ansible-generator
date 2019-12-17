:source: fmgr_pm_config_obj_webfilter_content_content.py

:orphan:

.. _fmgr_pm_config_obj_webfilter_content_content:

fmgr_pm_config_obj_webfilter_content_content -- Configure Web filter banned word table.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/webfilter/content/{content}`
- `/pm/config/global/obj/webfilter/content/{content}`
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
 <li><span class="li-head">adom</span> - the domain prefix <span class="li-normal">type: str</span> <span class="li-normal"> choices: none, global, custom dom</span></li>
 <li><span class="li-head">content</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure Web filter banned word table.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">comment</span> - Optional comments. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">entries</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Block or exempt word when a match is found. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [exempt, block]</span> </li>
 <li><span class="li-head">lang</span> - Language of banned word. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [western, simch, trach, japanese, korean, french, thai, spanish, cyrillic]</span> </li>
 <li><span class="li-head">name</span> - Banned word. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">pattern-type</span> - Banned word pattern type: wildcard pattern or Perl regular expression. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [wildcard, regexp]</span> </li>
 <li><span class="li-head">score</span> - Score, to be applied every time the word appears on a web page (0 - 4294967295, default = 10). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">status</span> - Enable/disable banned word. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - Name of table. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure Web filter banned word table.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure Web filter banned word table.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
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
    - name: send request to /pm/config/obj/webfilter/content/{content}
      fmgr_pm_config_obj_webfilter_content_content:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            content: <value of string>
         params:
            - 
               data: 
                  comment: <value of string>
                  entries: 
                   - 
                        action: <value in [exempt, block]>
                        lang: <value in [western, simch, trach, ...]>
                        name: <value of string>
                        pattern-type: <value in [wildcard, regexp]>
                        score: <value of integer>
                        status: <value in [disable, enable]>
                  id: <value of integer>
                  name: <value of string>
    - name: send request to /pm/config/obj/webfilter/content/{content}
      fmgr_pm_config_obj_webfilter_content_content:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            content: <value of string>
         params:
            - 
               option: <value in [object member, chksum, datasrc]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [clone, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/webfilter/content/{content}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [delete]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/webfilter/content/{content}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> comment </span> - Optional comments. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> entries </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - Block or exempt word when a match is found. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> lang </span> - Language of banned word. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Banned word. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pattern-type </span> - Banned word pattern type: wildcard pattern or Perl regular expression. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> score </span> - Score, to be applied every time the word appears on a web page (0 - 4294967295, default = 10). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable banned word. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> id </span> - ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> name </span> - Name of table. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/webfilter/content/{content}</span>  </li>
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



