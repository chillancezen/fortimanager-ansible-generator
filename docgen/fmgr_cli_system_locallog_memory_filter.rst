:source: fmgr_cli_system_locallog_memory_filter.py

:orphan:

.. _fmgr_cli_system_locallog_memory_filter:

fmgr_cli_system_locallog_memory_filter -- Filter for memory logging.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/locallog/memory/filter`
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
 <li><span class="li-head">parameters for method: [get]</span> - Filter for memory logging.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Filter for memory logging.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">devcfg</span> - Log device configuration message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">devops</span> - Managered devices operations messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">diskquota</span> - Log Fortianalyzer disk quota messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">dm</span> - Log deployment manager message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">dvm</span> - Log device manager messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">ediscovery</span> - Log Fortianalyzer ediscovery messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">epmgr</span> - Log endpoint manager message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">event</span> - Log event messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">eventmgmt</span> - Log Fortianalyzer event handler messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">faz</span> - Log Fortianalyzer messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">fazha</span> - Log Fortianalyzer HA messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">fazsys</span> - Log Fortianalyzer system messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">fgd</span> - Log FortiGuard service message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">fgfm</span> - Log FGFM protocol message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">fips</span> - Whether to log fips messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">fmgws</span> - Log web service messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">fmlmgr</span> - Log FortiMail manager message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">fmwmgr</span> - Log firmware manager message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">fortiview</span> - Log Fortianalyzer FortiView messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">glbcfg</span> - Log global database message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">ha</span> - Log HA message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">hcache</span> - Log Fortianalyzer hcache messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">iolog</span> - Log debug IO log message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">logd</span> - Log the status of log daemon. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">logdb</span> - Log Fortianalyzer log DB messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">logdev</span> - Log Fortianalyzer log device messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">logfile</span> - Log Fortianalyzer log file messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [enable, disable]</span> </li>
 <li><span class="li-head">logging</span> - Log Fortianalyzer logging messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">lrmgr</span> - Log log and report manager message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">objcfg</span> - Log object configuration change message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">report</span> - Log Fortianalyzer report messages. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">rev</span> - Log revision history message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">rtmon</span> - Log real-time monitor message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">scfw</span> - Log firewall objects message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">scply</span> - Log policy console message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">scrmgr</span> - Log script manager message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">scvpn</span> - Log VPN console message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">system</span> - Log system manager message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">webport</span> - Log web portal message. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/LOCALLOG/MEMORY/FILTER
      fmgr_cli_system_locallog_memory_filter:
         method: <value in [set, update]>
         params:
            -
               data:
                  devcfg: <value in [disable, enable] default: 'enable'>
                  devops: <value in [disable, enable] default: 'enable'>
                  diskquota: <value in [disable, enable] default: 'enable'>
                  dm: <value in [disable, enable] default: 'enable'>
                  dvm: <value in [disable, enable] default: 'enable'>
                  ediscovery: <value in [disable, enable] default: 'enable'>
                  epmgr: <value in [disable, enable] default: 'enable'>
                  event: <value in [disable, enable] default: 'enable'>
                  eventmgmt: <value in [disable, enable] default: 'enable'>
                  faz: <value in [disable, enable] default: 'enable'>
                  fazha: <value in [disable, enable] default: 'enable'>
                  fazsys: <value in [disable, enable] default: 'enable'>
                  fgd: <value in [disable, enable] default: 'enable'>
                  fgfm: <value in [disable, enable] default: 'enable'>
                  fips: <value in [disable, enable] default: 'enable'>
                  fmgws: <value in [disable, enable] default: 'enable'>
                  fmlmgr: <value in [disable, enable] default: 'enable'>
                  fmwmgr: <value in [disable, enable] default: 'enable'>
                  fortiview: <value in [disable, enable] default: 'enable'>
                  glbcfg: <value in [disable, enable] default: 'enable'>
                  ha: <value in [disable, enable] default: 'enable'>
                  hcache: <value in [disable, enable] default: 'enable'>
                  iolog: <value in [disable, enable] default: 'enable'>
                  logd: <value in [disable, enable] default: 'enable'>
                  logdb: <value in [disable, enable] default: 'enable'>
                  logdev: <value in [disable, enable] default: 'enable'>
                  logfile: <value in [enable, disable]>
                  logging: <value in [disable, enable] default: 'enable'>
                  lrmgr: <value in [disable, enable] default: 'enable'>
                  objcfg: <value in [disable, enable] default: 'enable'>
                  report: <value in [disable, enable] default: 'enable'>
                  rev: <value in [disable, enable] default: 'enable'>
                  rtmon: <value in [disable, enable] default: 'enable'>
                  scfw: <value in [disable, enable] default: 'enable'>
                  scply: <value in [disable, enable] default: 'enable'>
                  scrmgr: <value in [disable, enable] default: 'enable'>
                  scvpn: <value in [disable, enable] default: 'enable'>
                  system: <value in [disable, enable] default: 'enable'>
                  webport: <value in [disable, enable] default: 'enable'>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> devcfg </span> - Log device configuration message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> devops </span> - Managered devices operations messages. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> diskquota </span> - Log Fortianalyzer disk quota messages. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> dm </span> - Log deployment manager message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> dvm </span> - Log device manager messages. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> ediscovery </span> - Log Fortianalyzer ediscovery messages. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> epmgr </span> - Log endpoint manager message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> event </span> - Log event messages. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> eventmgmt </span> - Log Fortianalyzer event handler messages. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> faz </span> - Log Fortianalyzer messages. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> fazha </span> - Log Fortianalyzer HA messages. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> fazsys </span> - Log Fortianalyzer system messages. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> fgd </span> - Log FortiGuard service message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> fgfm </span> - Log FGFM protocol message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> fips </span> - Whether to log fips messages. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> fmgws </span> - Log web service messages. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> fmlmgr </span> - Log FortiMail manager message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> fmwmgr </span> - Log firmware manager message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> fortiview </span> - Log Fortianalyzer FortiView messages. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> glbcfg </span> - Log global database message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> ha </span> - Log HA message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> hcache </span> - Log Fortianalyzer hcache messages. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> iolog </span> - Log debug IO log message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> logd </span> - Log the status of log daemon. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> logdb </span> - Log Fortianalyzer log DB messages. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> logdev </span> - Log Fortianalyzer log device messages. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> logfile </span> - Log Fortianalyzer log file messages. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> logging </span> - Log Fortianalyzer logging messages. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> lrmgr </span> - Log log and report manager message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> objcfg </span> - Log object configuration change message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> report </span> - Log Fortianalyzer report messages. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> rev </span> - Log revision history message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> rtmon </span> - Log real-time monitor message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> scfw </span> - Log firewall objects message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> scply </span> - Log policy console message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> scrmgr </span> - Log script manager message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> scvpn </span> - Log VPN console message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> system </span> - Log system manager message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> webport </span> - Log web portal message. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/locallog/memory/filter</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/locallog/memory/filter</span>  </li>
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



