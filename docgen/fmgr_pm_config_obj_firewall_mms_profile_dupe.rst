:source: fmgr_pm_config_obj_firewall_mms_profile_dupe.py

:orphan:

.. _fmgr_pm_config_obj_firewall_mms_profile_dupe:

fmgr_pm_config_obj_firewall_mms_profile_dupe -- Duplicate configuration.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/firewall/mms-profile/{mms-profile}/dupe`
- `/pm/config/global/obj/firewall/mms-profile/{mms-profile}/dupe`
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
 <li><span class="li-head">mms-profile</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Duplicate configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Duplicate configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">action1</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [log, archive, intercept, block, archive-first, alert-notif]</span> </li>
 </ul>
 <li><span class="li-head">action2</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [log, archive, intercept, block, archive-first, alert-notif]</span> </li>
 </ul>
 <li><span class="li-head">action3</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [log, archive, intercept, block, archive-first, alert-notif]</span> </li>
 </ul>
 <li><span class="li-head">block-time1</span> - Duration for which action takes effect (0 - 35791 min). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">block-time2</span> - Duration for which action takes effect (0 - 35791 min). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">block-time3</span> - Duration action takes effect (0 - 35791 min). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">limit1</span> - Maximum number of messages allowed. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">limit2</span> - Maximum number of messages allowed. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">limit3</span> - Maximum number of messages allowed. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">protocol</span> - Protocol. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status1</span> - Enable/disable status1 detection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">status2</span> - Enable/disable status2 detection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">status3</span> - Enable/disable status3 detection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">window1</span> - Window to count messages over (1 - 2880 min). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">window2</span> - Window to count messages over (1 - 2880 min). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">window3</span> - Window to count messages over (1 - 2880 min). <span class="li-normal">type: int</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/MMS-PROFILE/{MMS-PROFILE}/DUPE
      fmgr_pm_config_obj_firewall_mms_profile_dupe:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            mms-profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/MMS-PROFILE/{MMS-PROFILE}/DUPE
      fmgr_pm_config_obj_firewall_mms_profile_dupe:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            mms-profile: <value of string>
         params:
            -
               data:
                  action1:
                    - <value in [log, archive, intercept, ...]>
                  action2:
                    - <value in [log, archive, intercept, ...]>
                  action3:
                    - <value in [log, archive, intercept, ...]>
                  block-time1: <value of integer>
                  block-time2: <value of integer>
                  block-time3: <value of integer>
                  limit1: <value of integer>
                  limit2: <value of integer>
                  limit3: <value of integer>
                  protocol: <value of string>
                  status1: <value in [disable, enable]>
                  status2: <value in [disable, enable]>
                  status3: <value in [disable, enable]>
                  window1: <value of integer>
                  window2: <value of integer>
                  window3: <value of integer>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> action1 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> action2 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> action3 </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> block-time1 </span> - Duration for which action takes effect (0 - 35791 min). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> block-time2 </span> - Duration for which action takes effect (0 - 35791 min). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> block-time3 </span> - Duration action takes effect (0 - 35791 min). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> limit1 </span> - Maximum number of messages allowed. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> limit2 </span> - Maximum number of messages allowed. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> limit3 </span> - Maximum number of messages allowed. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> protocol </span> - Protocol. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status1 </span> - Enable/disable status1 detection. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status2 </span> - Enable/disable status2 detection. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status3 </span> - Enable/disable status3 detection. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> window1 </span> - Window to count messages over (1 - 2880 min). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> window2 </span> - Window to count messages over (1 - 2880 min). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> window3 </span> - Window to count messages over (1 - 2880 min). <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/mms-profile/{mms-profile}/dupe</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/firewall/mms-profile/{mms-profile}/dupe</span>  </li>
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



