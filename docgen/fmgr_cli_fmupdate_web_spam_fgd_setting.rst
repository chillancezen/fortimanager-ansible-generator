:source: fmgr_cli_fmupdate_web_spam_fgd_setting.py

:orphan:

.. _fmgr_cli_fmupdate_web_spam_fgd_setting:

fmgr_cli_fmupdate_web_spam_fgd_setting -- Configure the FortiGuard run parameters.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/fmupdate/web-spam/fgd-setting`
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
 <li><span class="li-head">parameters for method: [get]</span> - Configure the FortiGuard run parameters.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Configure the FortiGuard run parameters.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">as-cache</span> - Antispam service maximum memory usage in megabytes (Maximum = Physical memory-1024, 0: no limit, default = 300). <span class="li-normal">type: int</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">as-log</span> - Antispam log setting (default = nospam). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, nospam, all]</span>  <span class="li-normal">default: nospam</span> </li>
 <li><span class="li-head">as-preload</span> - Enable/disable preloading antispam database to memory (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">av-cache</span> - Antivirus service maximum memory usage, in megabytes (100 - 500, default = 300). <span class="li-normal">type: int</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">av-log</span> - Antivirus log setting (default = novirus). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, novirus, all]</span>  <span class="li-normal">default: novirus</span> </li>
 <li><span class="li-head">av-preload</span> - Enable/disable preloading antivirus database to memory (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">av2-cache</span> - Antispam service maximum memory usage in megabytes (Maximum = Physical memory-1024, 0: no limit, default = 800). <span class="li-normal">type: int</span>  <span class="li-normal">default: 800</span> </li>
 <li><span class="li-head">av2-log</span> - Outbreak prevention log setting (default = noav2). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, noav2, all]</span>  <span class="li-normal">default: noav2</span> </li>
 <li><span class="li-head">av2-preload</span> - Enable/disable preloading outbreak prevention database to memory (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">eventlog-query</span> - Enable/disable record query to event-log besides fgd-log (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">fgd-pull-interval</span> - Fgd pull interval setting, in minutes (1 - 1440, default = 10). <span class="li-normal">type: int</span>  <span class="li-normal">default: 10</span> </li>
 <li><span class="li-head">fq-cache</span> - File query service maximum memory usage, in megabytes (100 - 500, default = 300). <span class="li-normal">type: int</span>  <span class="li-normal">default: 300</span> </li>
 <li><span class="li-head">fq-log</span> - File query log setting (default = nofilequery). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, nofilequery, all]</span>  <span class="li-normal">default: nofilequery</span> </li>
 <li><span class="li-head">fq-preload</span> - Enable/disable preloading file query database to memory (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">linkd-log</span> - Linkd log setting (default = debug). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [emergency, alert, critical, error, warn, notice, info, debug, disable]</span>  <span class="li-normal">default: debug</span> </li>
 <li><span class="li-head">max-client-worker</span> - max worker for tcp client connection (0~16: 0 means use cpu number up to 4). <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">max-log-quota</span> - Maximum log quota setting, in megabytes (100 - 20480, default = 6144). <span class="li-normal">type: int</span>  <span class="li-normal">default: 6144</span> </li>
 <li><span class="li-head">max-unrated-site</span> - Maximum number of unrated site in memory, in kilobytes(10 - 5120, default = 500). <span class="li-normal">type: int</span>  <span class="li-normal">default: 500</span> </li>
 <li><span class="li-head">restrict-as1-dbver</span> - Restrict system update to indicated antispam(1) database version (character limit = 127). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">restrict-as2-dbver</span> - Restrict system update to indicated antispam(2) database version (character limit = 127). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">restrict-as4-dbver</span> - Restrict system update to indicated antispam(4) database version (character limit = 127). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">restrict-av-dbver</span> - Restrict system update to indicated antivirus database version (character limit = 127). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">restrict-av2-dbver</span> - Restrict system update to indicated outbreak prevention database version (character limit = 127). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">restrict-fq-dbver</span> - Restrict system update to indicated file query database version (character limit = 127). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">restrict-wf-dbver</span> - Restrict system update to indicated web filter database version (character limit = 127). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server-override</span> <li><span class="li-head">servlist</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">id</span> - Override server ID (1 - 10). <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">ip</span> - IPv4 address of the override server. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">ip6</span> - IPv6 address of the override server. <span class="li-normal">type: str</span>  <span class="li-normal">default: ::</span> </li>
 <li><span class="li-head">port</span> - Port number to use when contacting FortiGuard (1 - 65535, default = 443). <span class="li-normal">type: int</span>  <span class="li-normal">default: 443</span> </li>
 <li><span class="li-head">service-type</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [fgd, fgc, fsa]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">status</span> - Override status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">stat-log-interval</span> - Statistic log interval setting, in minutes (1 - 1440, default = 60). <span class="li-normal">type: int</span>  <span class="li-normal">default: 60</span> </li>
 <li><span class="li-head">stat-sync-interval</span> - Synchronization interval for statistic of unrated site in minutes (1 - 60, default = 60). <span class="li-normal">type: int</span>  <span class="li-normal">default: 60</span> </li>
 <li><span class="li-head">update-interval</span> - FortiGuard database update wait time if not enough delta files, in hours (2 - 24, default = 6). <span class="li-normal">type: int</span>  <span class="li-normal">default: 6</span> </li>
 <li><span class="li-head">update-log</span> - Enable/disable update log setting (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">wf-cache</span> - Web filter service maximum memory usage, in megabytes (maximum = Physical memory-1024, 0 = no limit, default = 600). <span class="li-normal">type: int</span>  <span class="li-normal">default: 0</span> </li>
 <li><span class="li-head">wf-dn-cache-expire-time</span> - Web filter DN cache expire time, in minutes (1 - 1440, 0 = never, default = 30). <span class="li-normal">type: int</span>  <span class="li-normal">default: 30</span> </li>
 <li><span class="li-head">wf-dn-cache-max-number</span> - Maximum number of Web filter DN cache (0 = disable, default = 10000). <span class="li-normal">type: int</span>  <span class="li-normal">default: 10000</span> </li>
 <li><span class="li-head">wf-log</span> - Web filter log setting (default = nour1) <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, nourl, all]</span>  <span class="li-normal">default: nourl</span> </li>
 <li><span class="li-head">wf-preload</span> - Enable/disable preloading the web filter database into memory (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
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

    - name: REQUESTING /CLI/FMUPDATE/WEB-SPAM/FGD-SETTING
      fmgr_cli_fmupdate_web_spam_fgd_setting:
         method: <value in [set, update]>
         params:
            -
               data:
                  as-cache: <value of integer default: 300>
                  as-log: <value in [disable, nospam, all] default: 'nospam'>
                  as-preload: <value in [disable, enable] default: 'disable'>
                  av-cache: <value of integer default: 300>
                  av-log: <value in [disable, novirus, all] default: 'novirus'>
                  av-preload: <value in [disable, enable] default: 'disable'>
                  av2-cache: <value of integer default: 800>
                  av2-log: <value in [disable, noav2, all] default: 'noav2'>
                  av2-preload: <value in [disable, enable] default: 'disable'>
                  eventlog-query: <value in [disable, enable] default: 'disable'>
                  fgd-pull-interval: <value of integer default: 10>
                  fq-cache: <value of integer default: 300>
                  fq-log: <value in [disable, nofilequery, all] default: 'nofilequery'>
                  fq-preload: <value in [disable, enable] default: 'disable'>
                  linkd-log: <value in [emergency, alert, critical, ...] default: 'debug'>
                  max-client-worker: <value of integer default: 0>
                  max-log-quota: <value of integer default: 6144>
                  max-unrated-site: <value of integer default: 500>
                  restrict-as1-dbver: <value of string>
                  restrict-as2-dbver: <value of string>
                  restrict-as4-dbver: <value of string>
                  restrict-av-dbver: <value of string>
                  restrict-av2-dbver: <value of string>
                  restrict-fq-dbver: <value of string>
                  restrict-wf-dbver: <value of string>
                  server-override:
                     servlist:
                       -
                           id: <value of integer default: 0>
                           ip: <value of string default: '0.0.0.0'>
                           ip6: <value of string default: '::'>
                           port: <value of integer default: 443>
                           service-type:
                             - <value in [fgd, fgc, fsa]>
                     status: <value in [disable, enable] default: 'disable'>
                  stat-log-interval: <value of integer default: 60>
                  stat-sync-interval: <value of integer default: 60>
                  update-interval: <value of integer default: 6>
                  update-log: <value in [disable, enable] default: 'enable'>
                  wf-cache: <value of integer default: 0>
                  wf-dn-cache-expire-time: <value of integer default: 30>
                  wf-dn-cache-max-number: <value of integer default: 10000>
                  wf-log: <value in [disable, nourl, all] default: 'nourl'>
                  wf-preload: <value in [disable, enable] default: 'enable'>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> as-cache </span> - Antispam service maximum memory usage in megabytes (Maximum = Physical memory-1024, 0: no limit, default = 300). <span class="li-normal">type: int</span>  <span class="li-normal">example: 300</span>  </li>
 <li> <span class="li-return"> as-log </span> - Antispam log setting (default = nospam). <span class="li-normal">type: str</span>  <span class="li-normal">example: nospam</span>  </li>
 <li> <span class="li-return"> as-preload </span> - Enable/disable preloading antispam database to memory (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> av-cache </span> - Antivirus service maximum memory usage, in megabytes (100 - 500, default = 300). <span class="li-normal">type: int</span>  <span class="li-normal">example: 300</span>  </li>
 <li> <span class="li-return"> av-log </span> - Antivirus log setting (default = novirus). <span class="li-normal">type: str</span>  <span class="li-normal">example: novirus</span>  </li>
 <li> <span class="li-return"> av-preload </span> - Enable/disable preloading antivirus database to memory (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> av2-cache </span> - Antispam service maximum memory usage in megabytes (Maximum = Physical memory-1024, 0: no limit, default = 800). <span class="li-normal">type: int</span>  <span class="li-normal">example: 800</span>  </li>
 <li> <span class="li-return"> av2-log </span> - Outbreak prevention log setting (default = noav2). <span class="li-normal">type: str</span>  <span class="li-normal">example: noav2</span>  </li>
 <li> <span class="li-return"> av2-preload </span> - Enable/disable preloading outbreak prevention database to memory (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> eventlog-query </span> - Enable/disable record query to event-log besides fgd-log (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> fgd-pull-interval </span> - Fgd pull interval setting, in minutes (1 - 1440, default = 10). <span class="li-normal">type: int</span>  <span class="li-normal">example: 10</span>  </li>
 <li> <span class="li-return"> fq-cache </span> - File query service maximum memory usage, in megabytes (100 - 500, default = 300). <span class="li-normal">type: int</span>  <span class="li-normal">example: 300</span>  </li>
 <li> <span class="li-return"> fq-log </span> - File query log setting (default = nofilequery). <span class="li-normal">type: str</span>  <span class="li-normal">example: nofilequery</span>  </li>
 <li> <span class="li-return"> fq-preload </span> - Enable/disable preloading file query database to memory (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> linkd-log </span> - Linkd log setting (default = debug). <span class="li-normal">type: str</span>  <span class="li-normal">example: debug</span>  </li>
 <li> <span class="li-return"> max-client-worker </span> - max worker for tcp client connection (0~16: 0 means use cpu number up to 4). <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> max-log-quota </span> - Maximum log quota setting, in megabytes (100 - 20480, default = 6144). <span class="li-normal">type: int</span>  <span class="li-normal">example: 6144</span>  </li>
 <li> <span class="li-return"> max-unrated-site </span> - Maximum number of unrated site in memory, in kilobytes(10 - 5120, default = 500). <span class="li-normal">type: int</span>  <span class="li-normal">example: 500</span>  </li>
 <li> <span class="li-return"> restrict-as1-dbver </span> - Restrict system update to indicated antispam(1) database version (character limit = 127). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> restrict-as2-dbver </span> - Restrict system update to indicated antispam(2) database version (character limit = 127). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> restrict-as4-dbver </span> - Restrict system update to indicated antispam(4) database version (character limit = 127). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> restrict-av-dbver </span> - Restrict system update to indicated antivirus database version (character limit = 127). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> restrict-av2-dbver </span> - Restrict system update to indicated outbreak prevention database version (character limit = 127). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> restrict-fq-dbver </span> - Restrict system update to indicated file query database version (character limit = 127). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> restrict-wf-dbver </span> - Restrict system update to indicated web filter database version (character limit = 127). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server-override </span> <li> <span class="li-return"> servlist </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - Override server ID (1 - 10). <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> ip </span> - IPv4 address of the override server. <span class="li-normal">type: str</span>  <span class="li-normal">example: 0.0.0.0</span>  </li>
 <li> <span class="li-return"> ip6 </span> - IPv6 address of the override server. <span class="li-normal">type: str</span>  <span class="li-normal">example: ::</span>  </li>
 <li> <span class="li-return"> port </span> - Port number to use when contacting FortiGuard (1 - 65535, default = 443). <span class="li-normal">type: int</span>  <span class="li-normal">example: 443</span>  </li>
 <li> <span class="li-return"> service-type </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 </ul>
 <li> <span class="li-return"> status </span> - Override status. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> stat-log-interval </span> - Statistic log interval setting, in minutes (1 - 1440, default = 60). <span class="li-normal">type: int</span>  <span class="li-normal">example: 60</span>  </li>
 <li> <span class="li-return"> stat-sync-interval </span> - Synchronization interval for statistic of unrated site in minutes (1 - 60, default = 60). <span class="li-normal">type: int</span>  <span class="li-normal">example: 60</span>  </li>
 <li> <span class="li-return"> update-interval </span> - FortiGuard database update wait time if not enough delta files, in hours (2 - 24, default = 6). <span class="li-normal">type: int</span>  <span class="li-normal">example: 6</span>  </li>
 <li> <span class="li-return"> update-log </span> - Enable/disable update log setting (default = enable). <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> wf-cache </span> - Web filter service maximum memory usage, in megabytes (maximum = Physical memory-1024, 0 = no limit, default = 600). <span class="li-normal">type: int</span>  <span class="li-normal">example: 0</span>  </li>
 <li> <span class="li-return"> wf-dn-cache-expire-time </span> - Web filter DN cache expire time, in minutes (1 - 1440, 0 = never, default = 30). <span class="li-normal">type: int</span>  <span class="li-normal">example: 30</span>  </li>
 <li> <span class="li-return"> wf-dn-cache-max-number </span> - Maximum number of Web filter DN cache (0 = disable, default = 10000). <span class="li-normal">type: int</span>  <span class="li-normal">example: 10000</span>  </li>
 <li> <span class="li-return"> wf-log </span> - Web filter log setting (default = nour1) <span class="li-normal">type: str</span>  <span class="li-normal">example: nourl</span>  </li>
 <li> <span class="li-return"> wf-preload </span> - Enable/disable preloading the web filter database into memory (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/fmupdate/web-spam/fgd-setting</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/fmupdate/web-spam/fgd-setting</span>  </li>
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



