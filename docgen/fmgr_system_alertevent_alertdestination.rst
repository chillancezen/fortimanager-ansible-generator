:source: fmgr_system_alertevent_alertdestination.py

:orphan:

.. _fmgr_system_alertevent_alertdestination:

fmgr_system_alertevent_alertdestination -- Alert destination.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/alert-event/{alert-event}/alert-destination`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Alert destination.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">from</span> - Sender email address to use in alert emails. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">smtp-name</span> - SMTP server name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">snmp-name</span> - SNMP trap name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">syslog-name</span> - Syslog server name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">to</span> - Recipient email address to use in alert emails. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - Destination type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [mail, snmp, syslog]</span>  <span class="li-normal">default: mail</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Alert destination.</li>
 <ul class="ul-self">
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [from, smtp-name, snmp-name, syslog-name, to, type]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">filter</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">loadsub</span> - Enable or disable the return of any sub-objects. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [count, syntax]</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/ALERT-EVENT/{ALERT-EVENT}/ALERT-DESTINATION
      fmgr_system_alertevent_alertdestination:
         method: <value in [add, set, update]>
         url_params:
            alert-event: <value of string>
         params:
            -
               data:
                 -
                     from: <value of string>
                     smtp-name: <value of string>
                     snmp-name: <value of string>
                     syslog-name: <value of string>
                     to: <value of string>
                     type: <value in [mail, snmp, syslog] default: 'mail'>

    - name: REQUESTING /CLI/SYSTEM/ALERT-EVENT/{ALERT-EVENT}/ALERT-DESTINATION
      fmgr_system_alertevent_alertdestination:
         method: <value in [get]>
         url_params:
            alert-event: <value of string>
         params:
            -
               fields:
                 -
                    - <value in [from, smtp-name, snmp-name, ...]>
               filter:
                 - <value of string>
               loadsub: <value of integer>
               option: <value in [count, syntax]>



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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/alert-event/{alert-event}/alert-destination</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> from </span> - Sender email address to use in alert emails. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> smtp-name </span> - SMTP server name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> snmp-name </span> - SNMP trap name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> syslog-name </span> - Syslog server name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> to </span> - Recipient email address to use in alert emails. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - Destination type. <span class="li-normal">type: str</span>  <span class="li-normal">example: mail</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/alert-event/{alert-event}/alert-destination</span>  </li>
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



