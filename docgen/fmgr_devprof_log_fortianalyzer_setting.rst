:source: fmgr_devprof_log_fortianalyzer_setting.py

:orphan:

.. _fmgr_devprof_log_fortianalyzer_setting:

fmgr_devprof_log_fortianalyzer_setting -- Global FortiAnalyzer settings.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/devprof/{devprof}/log/fortianalyzer/setting`
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
 <li><span class="li-head">devprof</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Global FortiAnalyzer settings.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Global FortiAnalyzer settings.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">certificate</span> - Certificate used to communicate with FortiAnalyzer. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">conn-timeout</span> - FortiAnalyzer connection time-out in seconds (for status and log buffer). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">enc-algorithm</span> - Enable/disable sending FortiAnalyzer log data with SSL encryption. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, high, low, disable, high-medium, low-medium]</span> </li>
 <li><span class="li-head">hmac-algorithm</span> - FortiAnalyzer IPsec tunnel HMAC algorithm. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sha256, sha1]</span> </li>
 <li><span class="li-head">ips-archive</span> - Enable/disable IPS packet archive logging. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">monitor-failure-retry-period</span> - Time between FortiAnalyzer connection retries in seconds (for status and log buffer). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">monitor-keepalive-period</span> - Time between OFTP keepalives in seconds (for status and log buffer). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">reliable</span> - Enable/disable reliable logging to FortiAnalyzer. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">ssl-min-proto-version</span> - Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [default, TLSv1, TLSv1-1, TLSv1-2, SSLv3]</span> </li>
 <li><span class="li-head">upload-day</span> - Day of week (month) to upload logs. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">upload-interval</span> - Frequency to upload log files to FortiAnalyzer. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [daily, weekly, monthly]</span> </li>
 <li><span class="li-head">upload-option</span> - Enable/disable logging to hard disk and then uploading to FortiAnalyzer. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [store-and-upload, realtime, 1-minute, 5-minute]</span> </li>
 <li><span class="li-head">upload-time</span> - Time to upload logs (hh:mm). <span class="li-normal">type: str</span> </li>
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

    - name: REQUESTING /PM/CONFIG/DEVPROF/{DEVPROF}/LOG/FORTIANALYZER/SETTING
      fmgr_devprof_log_fortianalyzer_setting:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            devprof: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/DEVPROF/{DEVPROF}/LOG/FORTIANALYZER/SETTING
      fmgr_devprof_log_fortianalyzer_setting:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            devprof: <value of string>
         params:
            -
               data:
                  certificate: <value of string>
                  conn-timeout: <value of integer>
                  enc-algorithm: <value in [default, high, low, ...]>
                  hmac-algorithm: <value in [sha256, sha1]>
                  ips-archive: <value in [disable, enable]>
                  monitor-failure-retry-period: <value of integer>
                  monitor-keepalive-period: <value of integer>
                  reliable: <value in [disable, enable]>
                  ssl-min-proto-version: <value in [default, TLSv1, TLSv1-1, ...]>
                  upload-day: <value of string>
                  upload-interval: <value in [daily, weekly, monthly]>
                  upload-option: <value in [store-and-upload, realtime, 1-minute, ...]>
                  upload-time: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> certificate </span> - Certificate used to communicate with FortiAnalyzer. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> conn-timeout </span> - FortiAnalyzer connection time-out in seconds (for status and log buffer). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> enc-algorithm </span> - Enable/disable sending FortiAnalyzer log data with SSL encryption. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> hmac-algorithm </span> - FortiAnalyzer IPsec tunnel HMAC algorithm. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ips-archive </span> - Enable/disable IPS packet archive logging. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> monitor-failure-retry-period </span> - Time between FortiAnalyzer connection retries in seconds (for status and log buffer). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> monitor-keepalive-period </span> - Time between OFTP keepalives in seconds (for status and log buffer). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> reliable </span> - Enable/disable reliable logging to FortiAnalyzer. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ssl-min-proto-version </span> - Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> upload-day </span> - Day of week (month) to upload logs. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> upload-interval </span> - Frequency to upload log files to FortiAnalyzer. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> upload-option </span> - Enable/disable logging to hard disk and then uploading to FortiAnalyzer. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> upload-time </span> - Time to upload logs (hh:mm). <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/devprof/{devprof}/log/fortianalyzer/setting</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/devprof/{devprof}/log/fortianalyzer/setting</span>  </li>
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



