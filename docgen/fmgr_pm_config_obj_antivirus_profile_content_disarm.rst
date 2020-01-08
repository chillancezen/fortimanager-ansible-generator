:source: fmgr_pm_config_obj_antivirus_profile_content_disarm.py

:orphan:

.. _fmgr_pm_config_obj_antivirus_profile_content_disarm:

fmgr_pm_config_obj_antivirus_profile_content_disarm -- AV Content Disarm and Reconstruction settings.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/antivirus/profile/{profile}/content-disarm`
- `/pm/config/global/obj/antivirus/profile/{profile}/content-disarm`
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
 <li><span class="li-head">profile</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - AV Content Disarm and Reconstruction settings.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - AV Content Disarm and Reconstruction settings.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">cover-page</span> - Enable/disable inserting a cover page into the disarmed document. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">detect-only</span> - Enable/disable only detect disarmable files, do not alter content. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">office-embed</span> - Enable/disable stripping of embedded objects in Microsoft Office documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">office-hylink</span> - Enable/disable stripping of hyperlinks in Microsoft Office documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">office-linked</span> - Enable/disable stripping of linked objects in Microsoft Office documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">office-macro</span> - Enable/disable stripping of macros in Microsoft Office documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">original-file-destination</span> - Destination to send original file if active content is removed. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [fortisandbox, quarantine, discard]</span> </li>
 <li><span class="li-head">pdf-act-form</span> - Enable/disable stripping of actions that submit data to other targets in PDF documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pdf-act-gotor</span> - Enable/disable stripping of links to other PDFs in PDF documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pdf-act-java</span> - Enable/disable stripping of actions that execute JavaScript code in PDF documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pdf-act-launch</span> - Enable/disable stripping of links to external applications in PDF documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pdf-act-movie</span> - Enable/disable stripping of embedded movies in PDF documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pdf-act-sound</span> - Enable/disable stripping of embedded sound files in PDF documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pdf-embedfile</span> - Enable/disable stripping of embedded files in PDF documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pdf-hyperlink</span> - Enable/disable stripping of hyperlinks from PDF documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">pdf-javacode</span> - Enable/disable stripping of JavaScript code in PDF documents. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/ANTIVIRUS/PROFILE/{PROFILE}/CONTENT-DISARM
      fmgr_pm_config_obj_antivirus_profile_content_disarm:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/ANTIVIRUS/PROFILE/{PROFILE}/CONTENT-DISARM
      fmgr_pm_config_obj_antivirus_profile_content_disarm:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               data:
                  cover-page: <value in [disable, enable]>
                  detect-only: <value in [disable, enable]>
                  office-embed: <value in [disable, enable]>
                  office-hylink: <value in [disable, enable]>
                  office-linked: <value in [disable, enable]>
                  office-macro: <value in [disable, enable]>
                  original-file-destination: <value in [fortisandbox, quarantine, discard]>
                  pdf-act-form: <value in [disable, enable]>
                  pdf-act-gotor: <value in [disable, enable]>
                  pdf-act-java: <value in [disable, enable]>
                  pdf-act-launch: <value in [disable, enable]>
                  pdf-act-movie: <value in [disable, enable]>
                  pdf-act-sound: <value in [disable, enable]>
                  pdf-embedfile: <value in [disable, enable]>
                  pdf-hyperlink: <value in [disable, enable]>
                  pdf-javacode: <value in [disable, enable]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> cover-page </span> - Enable/disable inserting a cover page into the disarmed document. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> detect-only </span> - Enable/disable only detect disarmable files, do not alter content. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> office-embed </span> - Enable/disable stripping of embedded objects in Microsoft Office documents. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> office-hylink </span> - Enable/disable stripping of hyperlinks in Microsoft Office documents. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> office-linked </span> - Enable/disable stripping of linked objects in Microsoft Office documents. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> office-macro </span> - Enable/disable stripping of macros in Microsoft Office documents. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> original-file-destination </span> - Destination to send original file if active content is removed. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pdf-act-form </span> - Enable/disable stripping of actions that submit data to other targets in PDF documents. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pdf-act-gotor </span> - Enable/disable stripping of links to other PDFs in PDF documents. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pdf-act-java </span> - Enable/disable stripping of actions that execute JavaScript code in PDF documents. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pdf-act-launch </span> - Enable/disable stripping of links to external applications in PDF documents. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pdf-act-movie </span> - Enable/disable stripping of embedded movies in PDF documents. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pdf-act-sound </span> - Enable/disable stripping of embedded sound files in PDF documents. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pdf-embedfile </span> - Enable/disable stripping of embedded files in PDF documents. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pdf-hyperlink </span> - Enable/disable stripping of hyperlinks from PDF documents. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pdf-javacode </span> - Enable/disable stripping of JavaScript code in PDF documents. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/antivirus/profile/{profile}/content-disarm</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/antivirus/profile/{profile}/content-disarm</span>  </li>
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



