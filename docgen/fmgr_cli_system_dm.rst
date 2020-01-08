:source: fmgr_cli_system_dm.py

:orphan:

.. _fmgr_cli_system_dm:

fmgr_cli_system_dm -- Configure dm.
+++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/dm`
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
 <li><span class="li-head">parameters for method: [get]</span> - Configure dm.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Configure dm.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">concurrent-install-image-limit</span> - Maximum number of concurrent install image (1 - 1000). <span class="li-normal">type: int</span>  <span class="li-normal">default: 500</span> </li>
 <li><span class="li-head">concurrent-install-limit</span> - Maximum number of concurrent installs (5 - 2000). <span class="li-normal">type: int</span>  <span class="li-normal">default: 480</span> </li>
 <li><span class="li-head">concurrent-install-script-limit</span> - Maximum number of concurrent install scripts (5 - 2000). <span class="li-normal">type: int</span>  <span class="li-normal">default: 480</span> </li>
 <li><span class="li-head">discover-timeout</span> - Check connection timeout when discover device (3 - 15). <span class="li-normal">type: int</span>  <span class="li-normal">default: 6</span> </li>
 <li><span class="li-head">dpm-logsize</span> - Maximum dpm log size per device (1 - 10000K). <span class="li-normal">type: int</span>  <span class="li-normal">default: 10000</span> </li>
 <li><span class="li-head">fgfm-sock-timeout</span> - Maximum FGFM socket idle time (90 - 1800 sec). <span class="li-normal">type: int</span>  <span class="li-normal">default: 360</span> </li>
 <li><span class="li-head">fgfm_keepalive_itvl</span> - FGFM protocol keep alive interval (30 - 600 sec). <span class="li-normal">type: int</span>  <span class="li-normal">default: 120</span> </li>
 <li><span class="li-head">force-remote-diff</span> - Always use remote diff when installing. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">fortiap-refresh-cnt</span> - Max auto refresh FortiAP number each time (1 - 10000). <span class="li-normal">type: int</span>  <span class="li-normal">default: 500</span> </li>
 <li><span class="li-head">fortiap-refresh-itvl</span> - Auto refresh FortiAP status interval (0 - 1440) minutes, set to 0 will disable auto refresh. <span class="li-normal">type: int</span>  <span class="li-normal">default: 10</span> </li>
 <li><span class="li-head">fortiext-refresh-cnt</span> - Max device number for FortiExtender auto refresh (1 - 10000). <span class="li-normal">type: int</span>  <span class="li-normal">default: 50</span> </li>
 <li><span class="li-head">install-image-timeout</span> - Maximum waiting time for image transfer and device upgrade (600 - 7200 sec). <span class="li-normal">type: int</span>  <span class="li-normal">default: 3600</span> </li>
 <li><span class="li-head">install-tunnel-retry-itvl</span> - Time to re-establish tunnel during install (10 - 60 sec). <span class="li-normal">type: int</span>  <span class="li-normal">default: 60</span> </li>
 <li><span class="li-head">max-revs</span> - Maximum number of revisions saved (1 - 250). <span class="li-normal">type: int</span>  <span class="li-normal">default: 100</span> </li>
 <li><span class="li-head">nr-retry</span> - Number of retries. <span class="li-normal">type: int</span>  <span class="li-normal">default: 1</span> </li>
 <li><span class="li-head">retry</span> - Enable/disable configuration install retry. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">retry-intvl</span> - Retry interval. <span class="li-normal">type: int</span>  <span class="li-normal">default: 15</span> </li>
 <li><span class="li-head">rollback-allow-reboot</span> - Enable/disable FortiGate reboot to rollback when installing script/config. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">script-logsize</span> - Maximum script log size per device (1 - 10000K). <span class="li-normal">type: int</span>  <span class="li-normal">default: 100</span> </li>
 <li><span class="li-head">skip-scep-check</span> - Enable/disable installing scep related objects even if scep url is configured. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">skip-tunnel-fcp-req</span> - Enable/disable skip the fcp request sent from fgfm tunnel <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">verify-install</span> - Verify install against remote configuration. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, optimal, enable]</span>  <span class="li-normal">default: enable</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/DM
      fmgr_cli_system_dm:
         method: <value in [set, update]>
         params:
            -
               data:
                  concurrent-install-image-limit: <value of integer default: 500>
                  concurrent-install-limit: <value of integer default: 480>
                  concurrent-install-script-limit: <value of integer default: 480>
                  discover-timeout: <value of integer default: 6>
                  dpm-logsize: <value of integer default: 10000>
                  fgfm-sock-timeout: <value of integer default: 360>
                  fgfm_keepalive_itvl: <value of integer default: 120>
                  force-remote-diff: <value in [disable, enable] default: 'disable'>
                  fortiap-refresh-cnt: <value of integer default: 500>
                  fortiap-refresh-itvl: <value of integer default: 10>
                  fortiext-refresh-cnt: <value of integer default: 50>
                  install-image-timeout: <value of integer default: 3600>
                  install-tunnel-retry-itvl: <value of integer default: 60>
                  max-revs: <value of integer default: 100>
                  nr-retry: <value of integer default: 1>
                  retry: <value in [disable, enable] default: 'enable'>
                  retry-intvl: <value of integer default: 15>
                  rollback-allow-reboot: <value in [disable, enable] default: 'disable'>
                  script-logsize: <value of integer default: 100>
                  skip-scep-check: <value in [disable, enable] default: 'disable'>
                  skip-tunnel-fcp-req: <value in [disable, enable] default: 'enable'>
                  verify-install: <value in [disable, optimal, enable] default: 'enable'>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> concurrent-install-image-limit </span> - Maximum number of concurrent install image (1 - 1000). <span class="li-normal">type: int</span>  <span class="li-normal">example: 500</span>  </li>
 <li> <span class="li-return"> concurrent-install-limit </span> - Maximum number of concurrent installs (5 - 2000). <span class="li-normal">type: int</span>  <span class="li-normal">example: 480</span>  </li>
 <li> <span class="li-return"> concurrent-install-script-limit </span> - Maximum number of concurrent install scripts (5 - 2000). <span class="li-normal">type: int</span>  <span class="li-normal">example: 480</span>  </li>
 <li> <span class="li-return"> discover-timeout </span> - Check connection timeout when discover device (3 - 15). <span class="li-normal">type: int</span>  <span class="li-normal">example: 6</span>  </li>
 <li> <span class="li-return"> dpm-logsize </span> - Maximum dpm log size per device (1 - 10000K). <span class="li-normal">type: int</span>  <span class="li-normal">example: 10000</span>  </li>
 <li> <span class="li-return"> fgfm-sock-timeout </span> - Maximum FGFM socket idle time (90 - 1800 sec). <span class="li-normal">type: int</span>  <span class="li-normal">example: 360</span>  </li>
 <li> <span class="li-return"> fgfm_keepalive_itvl </span> - FGFM protocol keep alive interval (30 - 600 sec). <span class="li-normal">type: int</span>  <span class="li-normal">example: 120</span>  </li>
 <li> <span class="li-return"> force-remote-diff </span> - Always use remote diff when installing. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> fortiap-refresh-cnt </span> - Max auto refresh FortiAP number each time (1 - 10000). <span class="li-normal">type: int</span>  <span class="li-normal">example: 500</span>  </li>
 <li> <span class="li-return"> fortiap-refresh-itvl </span> - Auto refresh FortiAP status interval (0 - 1440) minutes, set to 0 will disable auto refresh. <span class="li-normal">type: int</span>  <span class="li-normal">example: 10</span>  </li>
 <li> <span class="li-return"> fortiext-refresh-cnt </span> - Max device number for FortiExtender auto refresh (1 - 10000). <span class="li-normal">type: int</span>  <span class="li-normal">example: 50</span>  </li>
 <li> <span class="li-return"> install-image-timeout </span> - Maximum waiting time for image transfer and device upgrade (600 - 7200 sec). <span class="li-normal">type: int</span>  <span class="li-normal">example: 3600</span>  </li>
 <li> <span class="li-return"> install-tunnel-retry-itvl </span> - Time to re-establish tunnel during install (10 - 60 sec). <span class="li-normal">type: int</span>  <span class="li-normal">example: 60</span>  </li>
 <li> <span class="li-return"> max-revs </span> - Maximum number of revisions saved (1 - 250). <span class="li-normal">type: int</span>  <span class="li-normal">example: 100</span>  </li>
 <li> <span class="li-return"> nr-retry </span> - Number of retries. <span class="li-normal">type: int</span>  <span class="li-normal">example: 1</span>  </li>
 <li> <span class="li-return"> retry </span> - Enable/disable configuration install retry. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> retry-intvl </span> - Retry interval. <span class="li-normal">type: int</span>  <span class="li-normal">example: 15</span>  </li>
 <li> <span class="li-return"> rollback-allow-reboot </span> - Enable/disable FortiGate reboot to rollback when installing script/config. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> script-logsize </span> - Maximum script log size per device (1 - 10000K). <span class="li-normal">type: int</span>  <span class="li-normal">example: 100</span>  </li>
 <li> <span class="li-return"> skip-scep-check </span> - Enable/disable installing scep related objects even if scep url is configured. <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> skip-tunnel-fcp-req </span> - Enable/disable skip the fcp request sent from fgfm tunnel <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> verify-install </span> - Verify install against remote configuration. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/dm</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/dm</span>  </li>
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



