:source: fmgr_pm_config_obj_dlp_filepattern_filepattern_entries_entries.py

:orphan:

.. _fmgr_pm_config_obj_dlp_filepattern_filepattern_entries_entries:

fmgr_pm_config_obj_dlp_filepattern_filepattern_entries_entries -- Configure file patterns used by DLP blocking.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, move, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/dlp/filepattern/{filepattern}/entries/{entries}`
- `/pm/config/global/obj/dlp/filepattern/{filepattern}/entries/{entries}`
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
 <li><span class="li-head">filepattern</span> - the object name <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">entries</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure file patterns used by DLP blocking.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">file-type</span> - Select a file type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [unknown, ignored, exe, elf, bat, javascript, html, hta, msoffice, gzip, rar, tar, lzh, upx, zip, cab, bzip2, bzip, activemime, mime, hlp, arj, base64, binhex, uue, fsg, aspack, msc, petite, jpeg, gif, tiff, png, bmp, msi, mpeg, mov, mp3, wma, wav, pdf, avi, rm, torrent, hibun, 7z, xz, msofficex, mach-o, dmg, .net, xar, chm, iso, crx, sis, prc, class, jad, cod]</span> </li>
 <li><span class="li-head">filter-type</span> - Filter by file name pattern or by file type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [pattern, type]</span> </li>
 <li><span class="li-head">pattern</span> - Add a file name pattern. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure file patterns used by DLP blocking.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure file patterns used by DLP blocking.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [move]</span> - Configure file patterns used by DLP blocking.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [before, after]</span> </li>
 <li><span class="li-head">target</span> - Key to the target entry. <span class="li-normal">type: str</span> </li>
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
    - name: send request to /pm/config/obj/dlp/filepattern/{filepattern}/entries/{entries}
      fmgr_pm_config_obj_dlp_filepattern_filepattern_entries_entries:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            filepattern: <value of string>
            entries: <value of string>
         params:
            - 
               data: 
                  file-type: <value in [unknown, ignored, exe, ...]>
                  filter-type: <value in [pattern, type]>
                  pattern: <value of string>
    - name: send request to /pm/config/obj/dlp/filepattern/{filepattern}/entries/{entries}
      fmgr_pm_config_obj_dlp_filepattern_filepattern_entries_entries:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            filepattern: <value of string>
            entries: <value of string>
         params:
            - 
               option: <value in [object member, chksum, datasrc]>
    - name: send request to /pm/config/obj/dlp/filepattern/{filepattern}/entries/{entries}
      fmgr_pm_config_obj_dlp_filepattern_filepattern_entries_entries:
         method: <value in [move]>
         url_params:
            adom: <value in [none, global, custom dom]>
            filepattern: <value of string>
            entries: <value of string>
         params:
            - 
               option: <value in [before, after]>
               target: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [clone, delete, move, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/dlp/filepattern/{filepattern}/entries/{entries}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> file-type </span> - Select a file type. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> filter-type </span> - Filter by file name pattern or by file type. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pattern </span> - Add a file name pattern. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/dlp/filepattern/{filepattern}/entries/{entries}</span>  </li>
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



