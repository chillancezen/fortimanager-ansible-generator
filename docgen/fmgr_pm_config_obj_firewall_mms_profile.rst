:source: fmgr_pm_config_obj_firewall_mms_profile.py

:orphan:

.. _fmgr_pm_config_obj_firewall_mms_profile:

fmgr_pm_config_obj_firewall_mms_profile -- Configure MMS profiles.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/mms-profile`
- `/pm/config/global/obj/firewall/mms-profile`
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
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure MMS profiles.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">avnotificationtable</span> - AntiVirus notification table ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">bwordtable</span> - MMS banned word table ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">carrier-endpoint-prefix</span> - Enable/disable prefixing of end point values. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">carrier-endpoint-prefix-range-max</span> - Maximum length of end point value that can be prefixed (1 - 48). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">carrier-endpoint-prefix-range-min</span> - Minimum end point length to be prefixed (1 - 48). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">carrier-endpoint-prefix-string</span> - String with which to prefix End point values. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">carrierendpointbwltable</span> - Carrier end point filter table ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">extended-utm-log</span> - Enable/disable detailed UTM log messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mm1</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [avmonitor, block, oversize, quarantine, scan, avquery, bannedword, no-content-summary, archive-summary, archive-full, carrier-endpoint-bwl, remove-blocked, chunkedbypass, clientcomfort, servercomfort, strict-file, mms-checksum]</span> </li>
 </ul>
 <li><span class="li-head">mm1-addr-hdr</span> - HTTP header field (for MM1) containing user address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mm1-addr-source</span> - Source for MM1 user address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [http-header, cookie]</span> </li>
 <li><span class="li-head">mm1-convert-hex</span> - Enable/disable converting user address from HEX string for MM1. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mm1-outbreak-prevention</span> - Enable FortiGuard Virus Outbreak Prevention service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, files, full-archive]</span> </li>
 <li><span class="li-head">mm1-retr-dupe</span> - Enable/disable duplicate scanning of MM1 retr. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mm1-retrieve-scan</span> - Enable/disable scanning on MM1 retrieve configuration messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mm1comfortamount</span> - MM1 comfort amount (0 - 4294967295). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mm1comfortinterval</span> - MM1 comfort interval (0 - 4294967295). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mm1oversizelimit</span> - Maximum file size to scan (1 - 819200 kB). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mm3</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [avmonitor, block, oversize, quarantine, scan, avquery, bannedword, no-content-summary, archive-summary, archive-full, carrier-endpoint-bwl, remove-blocked, fragmail, splice, mms-checksum]</span> </li>
 </ul>
 <li><span class="li-head">mm3-outbreak-prevention</span> - Enable FortiGuard Virus Outbreak Prevention service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, files, full-archive]</span> </li>
 <li><span class="li-head">mm3oversizelimit</span> - Maximum file size to scan (1 - 819200 kB). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mm4</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [avmonitor, block, oversize, quarantine, scan, avquery, bannedword, no-content-summary, archive-summary, archive-full, carrier-endpoint-bwl, remove-blocked, fragmail, splice, mms-checksum]</span> </li>
 </ul>
 <li><span class="li-head">mm4-outbreak-prevention</span> - Enable FortiGuard Virus Outbreak Prevention service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, files, full-archive]</span> </li>
 <li><span class="li-head">mm4oversizelimit</span> - Maximum file size to scan (1 - 819200 kB). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mm7</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [avmonitor, block, oversize, quarantine, scan, avquery, bannedword, no-content-summary, archive-summary, archive-full, carrier-endpoint-bwl, remove-blocked, chunkedbypass, clientcomfort, servercomfort, strict-file, mms-checksum]</span> </li>
 </ul>
 <li><span class="li-head">mm7-addr-hdr</span> - HTTP header field (for MM7) containing user address. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mm7-addr-source</span> - Source for MM7 user address. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [http-header, cookie]</span> </li>
 <li><span class="li-head">mm7-convert-hex</span> - Enable/disable conversion of user address from HEX string for MM7. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mm7-outbreak-prevention</span> - Enable FortiGuard Virus Outbreak Prevention service. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disabled, files, full-archive]</span> </li>
 <li><span class="li-head">mm7comfortamount</span> - MM7 comfort amount (0 - 4294967295). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mm7comfortinterval</span> - MM7 comfort interval (0 - 4294967295). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mm7oversizelimit</span> - Maximum file size to scan (1 - 819200 kB). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">mms-antispam-mass-log</span> - Enable/disable logging for MMS antispam mass. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-av-block-log</span> - Enable/disable logging for MMS antivirus file blocking. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-av-oversize-log</span> - Enable/disable logging for MMS antivirus oversize file blocking. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-av-virus-log</span> - Enable/disable logging for MMS antivirus scanning. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-carrier-endpoint-filter-log</span> - Enable/disable logging for MMS end point filter blocking. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-checksum-log</span> - Enable/disable MMS content checksum logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-checksum-table</span> - MMS content checksum table ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mms-notification-log</span> - Enable/disable logging for MMS notification messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mms-web-content-log</span> - Enable/disable logging for MMS web content blocking. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">mmsbwordthreshold</span> - MMS banned word threshold. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - Profile name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">notif-msisdn</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">msisdn</span> - Recipient MSISDN. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">threshold</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [flood-thresh-1, flood-thresh-2, flood-thresh-3, dupe-thresh-1, dupe-thresh-2, dupe-thresh-3]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">remove-blocked-const-length</span> - Enable/disable MMS replacement of blocked file constant length. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">replacemsg-group</span> - Replacement message group. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure MMS profiles.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [avnotificationtable, bwordtable, carrier-endpoint-prefix, carrier-endpoint-prefix-range-max, carrier-endpoint-prefix-range-min, carrier-endpoint-prefix-string, carrierendpointbwltable, comment, extended-utm-log, mm1, mm1-addr-hdr, mm1-addr-source, mm1-convert-hex, mm1-outbreak-prevention, mm1-retr-dupe, mm1-retrieve-scan, mm1comfortamount, mm1comfortinterval, mm1oversizelimit, mm3, mm3-outbreak-prevention, mm3oversizelimit, mm4, mm4-outbreak-prevention, mm4oversizelimit, mm7, mm7-addr-hdr, mm7-addr-source, mm7-convert-hex, mm7-outbreak-prevention, mm7comfortamount, mm7comfortinterval, mm7oversizelimit, mms-antispam-mass-log, mms-av-block-log, mms-av-oversize-log, mms-av-virus-log, mms-carrier-endpoint-filter-log, mms-checksum-log, mms-checksum-table, mms-notification-log, mms-web-content-log, mmsbwordthreshold, name, remove-blocked-const-length, replacemsg-group]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">get used</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">loadsub</span> - Enable or disable the return of any sub-objects. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [count, object member, datasrc, get reserved, syntax]</span> </li>
 <li><span class="li-head">range</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: int</span> </li>
 </ul>
 <li><span class="li-head">sortings</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{attr_name}</span> - No description for the parameter <span class="li-normal">type: int</span>  <span class="li-normal">choices: [1, -1]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/MMS-PROFILE
      fmgr_pm_config_obj_firewall_mms_profile:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     avnotificationtable: <value of string>
                     bwordtable: <value of string>
                     carrier-endpoint-prefix: <value in [disable, enable]>
                     carrier-endpoint-prefix-range-max: <value of integer>
                     carrier-endpoint-prefix-range-min: <value of integer>
                     carrier-endpoint-prefix-string: <value of string>
                     carrierendpointbwltable: <value of string>
                     comment: <value of string>
                     extended-utm-log: <value in [disable, enable]>
                     mm1:
                       - <value in [avmonitor, block, oversize, ...]>
                     mm1-addr-hdr: <value of string>
                     mm1-addr-source: <value in [http-header, cookie]>
                     mm1-convert-hex: <value in [disable, enable]>
                     mm1-outbreak-prevention: <value in [disabled, files, full-archive]>
                     mm1-retr-dupe: <value in [disable, enable]>
                     mm1-retrieve-scan: <value in [disable, enable]>
                     mm1comfortamount: <value of integer>
                     mm1comfortinterval: <value of integer>
                     mm1oversizelimit: <value of integer>
                     mm3:
                       - <value in [avmonitor, block, oversize, ...]>
                     mm3-outbreak-prevention: <value in [disabled, files, full-archive]>
                     mm3oversizelimit: <value of integer>
                     mm4:
                       - <value in [avmonitor, block, oversize, ...]>
                     mm4-outbreak-prevention: <value in [disabled, files, full-archive]>
                     mm4oversizelimit: <value of integer>
                     mm7:
                       - <value in [avmonitor, block, oversize, ...]>
                     mm7-addr-hdr: <value of string>
                     mm7-addr-source: <value in [http-header, cookie]>
                     mm7-convert-hex: <value in [disable, enable]>
                     mm7-outbreak-prevention: <value in [disabled, files, full-archive]>
                     mm7comfortamount: <value of integer>
                     mm7comfortinterval: <value of integer>
                     mm7oversizelimit: <value of integer>
                     mms-antispam-mass-log: <value in [disable, enable]>
                     mms-av-block-log: <value in [disable, enable]>
                     mms-av-oversize-log: <value in [disable, enable]>
                     mms-av-virus-log: <value in [disable, enable]>
                     mms-carrier-endpoint-filter-log: <value in [disable, enable]>
                     mms-checksum-log: <value in [disable, enable]>
                     mms-checksum-table: <value of string>
                     mms-notification-log: <value in [disable, enable]>
                     mms-web-content-log: <value in [disable, enable]>
                     mmsbwordthreshold: <value of integer>
                     name: <value of string>
                     notif-msisdn:
                       -
                           msisdn: <value of string>
                           threshold:
                             - <value in [flood-thresh-1, flood-thresh-2, flood-thresh-3, ...]>
                     remove-blocked-const-length: <value in [disable, enable]>
                     replacemsg-group: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/MMS-PROFILE
      fmgr_pm_config_obj_firewall_mms_profile:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [avnotificationtable, bwordtable, carrier-endpoint-prefix, ...]>
               filter:
                 - <value of string>
               get used: <value of integer>
               loadsub: <value of integer>
               option: <value in [count, object member, datasrc, ...]>
               range:
                 - <value of integer>
               sortings:
                 -
                     varidic.attr_name: <value in [1, -1]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [add, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/mms-profile</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> avnotificationtable </span> - AntiVirus notification table ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> bwordtable </span> - MMS banned word table ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> carrier-endpoint-prefix </span> - Enable/disable prefixing of end point values. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> carrier-endpoint-prefix-range-max </span> - Maximum length of end point value that can be prefixed (1 - 48). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> carrier-endpoint-prefix-range-min </span> - Minimum end point length to be prefixed (1 - 48). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> carrier-endpoint-prefix-string </span> - String with which to prefix End point values. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> carrierendpointbwltable </span> - Carrier end point filter table ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> comment </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> extended-utm-log </span> - Enable/disable detailed UTM log messages. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mm1 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> mm1-addr-hdr </span> - HTTP header field (for MM1) containing user address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mm1-addr-source </span> - Source for MM1 user address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mm1-convert-hex </span> - Enable/disable converting user address from HEX string for MM1. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mm1-outbreak-prevention </span> - Enable FortiGuard Virus Outbreak Prevention service. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mm1-retr-dupe </span> - Enable/disable duplicate scanning of MM1 retr. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mm1-retrieve-scan </span> - Enable/disable scanning on MM1 retrieve configuration messages. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mm1comfortamount </span> - MM1 comfort amount (0 - 4294967295). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mm1comfortinterval </span> - MM1 comfort interval (0 - 4294967295). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mm1oversizelimit </span> - Maximum file size to scan (1 - 819200 kB). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mm3 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> mm3-outbreak-prevention </span> - Enable FortiGuard Virus Outbreak Prevention service. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mm3oversizelimit </span> - Maximum file size to scan (1 - 819200 kB). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mm4 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> mm4-outbreak-prevention </span> - Enable FortiGuard Virus Outbreak Prevention service. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mm4oversizelimit </span> - Maximum file size to scan (1 - 819200 kB). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mm7 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> mm7-addr-hdr </span> - HTTP header field (for MM7) containing user address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mm7-addr-source </span> - Source for MM7 user address. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mm7-convert-hex </span> - Enable/disable conversion of user address from HEX string for MM7. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mm7-outbreak-prevention </span> - Enable FortiGuard Virus Outbreak Prevention service. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mm7comfortamount </span> - MM7 comfort amount (0 - 4294967295). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mm7comfortinterval </span> - MM7 comfort interval (0 - 4294967295). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mm7oversizelimit </span> - Maximum file size to scan (1 - 819200 kB). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> mms-antispam-mass-log </span> - Enable/disable logging for MMS antispam mass. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mms-av-block-log </span> - Enable/disable logging for MMS antivirus file blocking. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mms-av-oversize-log </span> - Enable/disable logging for MMS antivirus oversize file blocking. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mms-av-virus-log </span> - Enable/disable logging for MMS antivirus scanning. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mms-carrier-endpoint-filter-log </span> - Enable/disable logging for MMS end point filter blocking. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mms-checksum-log </span> - Enable/disable MMS content checksum logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mms-checksum-table </span> - MMS content checksum table ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mms-notification-log </span> - Enable/disable logging for MMS notification messages. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mms-web-content-log </span> - Enable/disable logging for MMS web content blocking. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mmsbwordthreshold </span> - MMS banned word threshold. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> name </span> - Profile name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> notif-msisdn </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> msisdn </span> - Recipient MSISDN. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> threshold </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 </ul>
 <li> <span class="li-return"> remove-blocked-const-length </span> - Enable/disable MMS replacement of blocked file constant length. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> replacemsg-group </span> - Replacement message group. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/mms-profile</span>  </li>
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



