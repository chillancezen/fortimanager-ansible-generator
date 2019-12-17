:source: fmgr_cli_system_alert_event_alert_event.py

:orphan:

.. _fmgr_cli_system_alert_event_alert_event:

fmgr_cli_system_alert_event_alert_event -- Alert events.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[delete, get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/alert-event/{alert-event}`
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
 <li><span class="li-head">alert-event</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [delete, get]</span> - Alert events.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Alert events.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">alert-destination</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">from</span> - Sender email address to use in alert emails. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">smtp-name</span> - SMTP server name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">snmp-name</span> - SNMP trap name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">syslog-name</span> - Syslog server name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">to</span> - Recipient email address to use in alert emails. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - Destination type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [mail, snmp, syslog]</span>  <span class="li-normal">default: mail</span> </li>
 </ul>
 <li><span class="li-head">enable-generic-text</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [enable, disable]</span> </li>
 </ul>
 <li><span class="li-head">enable-severity-filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [enable, disable]</span> </li>
 </ul>
 <li><span class="li-head">event-time-period</span> - Time period (hours). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [0.5, 1, 3, 6, 12, 24, 72, 168]</span>  <span class="li-normal">default: 0.5</span> </li>
 <li><span class="li-head">generic-text</span> - Text that must be contained in a log to trigger alert. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Alert name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">num-events</span> - Minimum number of events required within time period. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [1, 5, 10, 50, 100]</span>  <span class="li-normal">default: 1</span> </li>
 <li><span class="li-head">severity-filter</span> - Required log severity to trigger alert. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [high, medium-high, medium, medium-low, low]</span>  <span class="li-normal">default: high</span> </li>
 <li><span class="li-head">severity-level-comp</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [>=, =, <=]</span> </li>
 </ul>
 <li><span class="li-head">severity-level-logs</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [no-check, information, notify, warning, error, critical, alert, emergency]</span> </li>
 </ul>
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
    - name: send request to /cli/system/alert-event/{alert-event}
      fmgr_cli_system_alert_event_alert_event:
         method: <value in [set, update]>
         url_params:
            alert-event: <value of string>
         params:
            - 
               data: 
                  alert-destination: 
                   - 
                        from: <value of string>
                        smtp-name: <value of string>
                        snmp-name: <value of string>
                        syslog-name: <value of string>
                        to: <value of string>
                        type: <value in [mail, snmp, syslog] default: mail>
                  enable-generic-text: 
                   - <value in [enable, disable]>
                  enable-severity-filter: 
                   - <value in [enable, disable]>
                  event-time-period: <value in [0.5, 1, 3, ...] default: 0.5>
                  generic-text: <value of string>
                  name: <value of string>
                  num-events: <value in [1, 5, 10, ...] default: 1>
                  severity-filter: <value in [high, medium-high, medium, ...] default: high>
                  severity-level-comp: 
                   - <value in [>=, =, <=]>
                  severity-level-logs: 
                   - <value in [no-check, information, notify, ...]>



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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/alert-event/{alert-event}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> alert-destination </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> from </span> - Sender email address to use in alert emails. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> smtp-name </span> - SMTP server name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> snmp-name </span> - SNMP trap name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> syslog-name </span> - Syslog server name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> to </span> - Recipient email address to use in alert emails. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - Destination type. <span class="li-normal">type: str</span>  <span class="li-normal">example: mail</span>  </li>
 </ul>
 <li> <span class="li-return"> enable-generic-text </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> enable-severity-filter </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> event-time-period </span> - Time period (hours). <span class="li-normal">type: str</span>  <span class="li-normal">example: 0.5</span>  </li>
 <li> <span class="li-return"> generic-text </span> - Text that must be contained in a log to trigger alert. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Alert name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> num-events </span> - Minimum number of events required within time period. <span class="li-normal">type: str</span>  <span class="li-normal">example: 1</span>  </li>
 <li> <span class="li-return"> severity-filter </span> - Required log severity to trigger alert. <span class="li-normal">type: str</span>  <span class="li-normal">example: high</span>  </li>
 <li> <span class="li-return"> severity-level-comp </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> severity-level-logs </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/alert-event/{alert-event}</span>  </li>
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



