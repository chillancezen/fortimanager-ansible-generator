:source: fmgr_pm_config_obj_switch_controller_qos_dot1p_map.py

:orphan:

.. _fmgr_pm_config_obj_switch_controller_qos_dot1p_map:

fmgr_pm_config_obj_switch_controller_qos_dot1p_map -- Configure FortiSwitch QoS 802.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/switch-controller/qos/dot1p-map`
- `/pm/config/global/obj/switch-controller/qos/dot1p-map`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure FortiSwitch QoS 802.1p.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">description</span> - Description of the 802. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Dot1p map name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priority-0</span> - COS queue mapped to dot1p priority number. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [queue-0, queue-1, queue-2, queue-3, queue-4, queue-5, queue-6, queue-7]</span> </li>
 <li><span class="li-head">priority-1</span> - COS queue mapped to dot1p priority number. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [queue-0, queue-1, queue-2, queue-3, queue-4, queue-5, queue-6, queue-7]</span> </li>
 <li><span class="li-head">priority-2</span> - COS queue mapped to dot1p priority number. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [queue-0, queue-1, queue-2, queue-3, queue-4, queue-5, queue-6, queue-7]</span> </li>
 <li><span class="li-head">priority-3</span> - COS queue mapped to dot1p priority number. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [queue-0, queue-1, queue-2, queue-3, queue-4, queue-5, queue-6, queue-7]</span> </li>
 <li><span class="li-head">priority-4</span> - COS queue mapped to dot1p priority number. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [queue-0, queue-1, queue-2, queue-3, queue-4, queue-5, queue-6, queue-7]</span> </li>
 <li><span class="li-head">priority-5</span> - COS queue mapped to dot1p priority number. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [queue-0, queue-1, queue-2, queue-3, queue-4, queue-5, queue-6, queue-7]</span> </li>
 <li><span class="li-head">priority-6</span> - COS queue mapped to dot1p priority number. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [queue-0, queue-1, queue-2, queue-3, queue-4, queue-5, queue-6, queue-7]</span> </li>
 <li><span class="li-head">priority-7</span> - COS queue mapped to dot1p priority number. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [queue-0, queue-1, queue-2, queue-3, queue-4, queue-5, queue-6, queue-7]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure FortiSwitch QoS 802.1p.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [description, name, priority-0, priority-1, priority-2, priority-3, priority-4, priority-5, priority-6, priority-7]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/SWITCH-CONTROLLER/QOS/DOT1P-MAP
      fmgr_pm_config_obj_switch_controller_qos_dot1p_map:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     description: <value of string>
                     name: <value of string>
                     priority-0: <value in [queue-0, queue-1, queue-2, ...]>
                     priority-1: <value in [queue-0, queue-1, queue-2, ...]>
                     priority-2: <value in [queue-0, queue-1, queue-2, ...]>
                     priority-3: <value in [queue-0, queue-1, queue-2, ...]>
                     priority-4: <value in [queue-0, queue-1, queue-2, ...]>
                     priority-5: <value in [queue-0, queue-1, queue-2, ...]>
                     priority-6: <value in [queue-0, queue-1, queue-2, ...]>
                     priority-7: <value in [queue-0, queue-1, queue-2, ...]>

    - name: REQUESTING /PM/CONFIG/OBJ/SWITCH-CONTROLLER/QOS/DOT1P-MAP
      fmgr_pm_config_obj_switch_controller_qos_dot1p_map:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [description, name, priority-0, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/switch-controller/qos/dot1p-map</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> description </span> - Description of the 802. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Dot1p map name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> priority-0 </span> - COS queue mapped to dot1p priority number. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> priority-1 </span> - COS queue mapped to dot1p priority number. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> priority-2 </span> - COS queue mapped to dot1p priority number. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> priority-3 </span> - COS queue mapped to dot1p priority number. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> priority-4 </span> - COS queue mapped to dot1p priority number. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> priority-5 </span> - COS queue mapped to dot1p priority number. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> priority-6 </span> - COS queue mapped to dot1p priority number. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> priority-7 </span> - COS queue mapped to dot1p priority number. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/switch-controller/qos/dot1p-map</span>  </li>
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



