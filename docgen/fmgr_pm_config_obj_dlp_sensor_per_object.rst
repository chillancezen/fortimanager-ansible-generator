:source: fmgr_pm_config_obj_dlp_sensor_per_object.py

:orphan:

.. _fmgr_pm_config_obj_dlp_sensor_per_object:

fmgr_pm_config_obj_dlp_sensor_per_object -- Configure DLP sensors.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/dlp/sensor/{sensor}`
- `/pm/config/global/obj/dlp/sensor/{sensor}`
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
 <li><span class="li-head">sensor</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure DLP sensors.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">dlp-log</span> - Enable/disable DLP logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">extended-log</span> - Enable/disable extended logging for data leak prevention. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Action to take with content that this DLP sensor matches. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [log-only, block, exempt, ban, ban-sender, quarantine-ip, quarantine-port, none, allow]</span> </li>
 <li><span class="li-head">archive</span> - Enable/disable DLP archiving. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable, summary-only]</span> </li>
 <li><span class="li-head">company-identifier</span> - Enter a company identifier watermark to match. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">expiry</span> - Quarantine duration in days, hours, minutes format (dddhhmm). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">file-size</span> - Match files this size or larger (0 - 4294967295 kbytes). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">file-type</span> - Select the number of a DLP file pattern table to match. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">filter-by</span> - Select the type of content to match. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [credit-card, ssn, regexp, file-type, file-size, fingerprint, watermark, encrypted]</span> </li>
 <li><span class="li-head">fp-sensitivity</span> - Select a DLP file pattern sensitivity to match. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">match-percentage</span> - Percentage of fingerprints in the fingerprint databases designated with the selected fp-sensitivity to match. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - Filter name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">proto</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post]</span> </li>
 </ul>
 <li><span class="li-head">regexp</span> - Enter a regular expression to match (max. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">severity</span> - Select the severity or threat level that matches this filter. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [info, low, medium, high, critical]</span> </li>
 <li><span class="li-head">type</span> - Select whether to check the content of messages (an email message) or files (downloaded files or email attachments). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [file, message]</span> </li>
 </ul>
 <li><span class="li-head">flow-based</span> - Enable/disable flow-based DLP. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">full-archive-proto</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post]</span> </li>
 </ul>
 <li><span class="li-head">nac-quar-log</span> - Enable/disable NAC quarantine logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - Name of the DLP sensor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">options</span> - Configure DLP options. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [strict-file]</span> </li>
 <li><span class="li-head">replacemsg-group</span> - Replacement message group used by this DLP sensor. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">summary-proto</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [imap, smtp, pop3, ftp, nntp, mm1, mm3, mm4, mm7, mapi, aim, icq, msn, yahoo, http-get, http-post]</span> </li>
 </ul>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure DLP sensors.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure DLP sensors.</li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/DLP/SENSOR/{SENSOR}
      fmgr_pm_config_obj_dlp_sensor_per_object:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            sensor: <value of string>
         params:
            -
               data:
                  comment: <value of string>
                  dlp-log: <value in [disable, enable]>
                  extended-log: <value in [disable, enable]>
                  filter:
                    -
                        action: <value in [log-only, block, exempt, ...]>
                        archive: <value in [disable, enable, summary-only]>
                        company-identifier: <value of string>
                        expiry: <value of string>
                        file-size: <value of integer>
                        file-type: <value of string>
                        filter-by: <value in [credit-card, ssn, regexp, ...]>
                        fp-sensitivity: <value of string>
                        id: <value of integer>
                        match-percentage: <value of integer>
                        name: <value of string>
                        proto:
                          - <value in [imap, smtp, pop3, ...]>
                        regexp: <value of string>
                        severity: <value in [info, low, medium, ...]>
                        type: <value in [file, message]>
                  flow-based: <value in [disable, enable]>
                  full-archive-proto:
                    - <value in [imap, smtp, pop3, ...]>
                  nac-quar-log: <value in [disable, enable]>
                  name: <value of string>
                  options: <value in [strict-file]>
                  replacemsg-group: <value of string>
                  summary-proto:
                    - <value in [imap, smtp, pop3, ...]>

    - name: REQUESTING /PM/CONFIG/OBJ/DLP/SENSOR/{SENSOR}
      fmgr_pm_config_obj_dlp_sensor_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            sensor: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [clone, delete, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/dlp/sensor/{sensor}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> comment </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> dlp-log </span> - Enable/disable DLP logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> extended-log </span> - Enable/disable extended logging for data leak prevention. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> filter </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - Action to take with content that this DLP sensor matches. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> archive </span> - Enable/disable DLP archiving. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> company-identifier </span> - Enter a company identifier watermark to match. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> expiry </span> - Quarantine duration in days, hours, minutes format (dddhhmm). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> file-size </span> - Match files this size or larger (0 - 4294967295 kbytes). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> file-type </span> - Select the number of a DLP file pattern table to match. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> filter-by </span> - Select the type of content to match. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> fp-sensitivity </span> - Select a DLP file pattern sensitivity to match. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> match-percentage </span> - Percentage of fingerprints in the fingerprint databases designated with the selected fp-sensitivity to match. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> name </span> - Filter name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> proto </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> regexp </span> - Enter a regular expression to match (max. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> severity </span> - Select the severity or threat level that matches this filter. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - Select whether to check the content of messages (an email message) or files (downloaded files or email attachments). <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> flow-based </span> - Enable/disable flow-based DLP. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> full-archive-proto </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> nac-quar-log </span> - Enable/disable NAC quarantine logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Name of the DLP sensor. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> options </span> - Configure DLP options. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> replacemsg-group </span> - Replacement message group used by this DLP sensor. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> summary-proto </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/dlp/sensor/{sensor}</span>  </li>
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



