:source: fmgr_pm_config_obj_spamfilter_bwl_per_object.py

:orphan:

.. _fmgr_pm_config_obj_spamfilter_bwl_per_object:

fmgr_pm_config_obj_spamfilter_bwl_per_object -- Configure anti-spam black/white list.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[clone, delete, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/spamfilter/bwl/{bwl}`
- `/pm/config/global/obj/spamfilter/bwl/{bwl}`
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
 <li><span class="li-head">bwl</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [clone, set, update]</span> - Configure anti-spam black/white list.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">comment</span> - Optional comments. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">entries</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">action</span> - Reject, mark as spam or good email. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [spam, clear, reject]</span> </li>
 <li><span class="li-head">addr-type</span> - IP address type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ipv4, ipv6]</span> </li>
 <li><span class="li-head">email-pattern</span> - Email address pattern. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Entry ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">ip4-subnet</span> - IPv4 network address/subnet mask bits. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ip6-subnet</span> - IPv6 network address/subnet mask bits. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">pattern-type</span> - Wildcard pattern or regular expression. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [wildcard, regexp]</span> </li>
 <li><span class="li-head">status</span> - Enable/disable status. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">type</span> - Entry type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [ip, email]</span> </li>
 </ul>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">name</span> - Name of table. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [delete]</span> - Configure anti-spam black/white list.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure anti-spam black/white list.</li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/SPAMFILTER/BWL/{BWL}
      fmgr_pm_config_obj_spamfilter_bwl_per_object:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            bwl: <value of string>
         params:
            -
               data:
                  comment: <value of string>
                  entries:
                    -
                        action: <value in [spam, clear, reject]>
                        addr-type: <value in [ipv4, ipv6]>
                        email-pattern: <value of string>
                        id: <value of integer>
                        ip4-subnet: <value of string>
                        ip6-subnet: <value of string>
                        pattern-type: <value in [wildcard, regexp]>
                        status: <value in [disable, enable]>
                        type: <value in [ip, email]>
                  id: <value of integer>
                  name: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/SPAMFILTER/BWL/{BWL}
      fmgr_pm_config_obj_spamfilter_bwl_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            bwl: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [clone, set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> id </span> - ID. <span class="li-normal">type: int</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/spamfilter/bwl/{bwl}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [delete]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/spamfilter/bwl/{bwl}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> comment </span> - Optional comments. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> entries </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> action </span> - Reject, mark as spam or good email. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> addr-type </span> - IP address type. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> email-pattern </span> - Email address pattern. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Entry ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> ip4-subnet </span> - IPv4 network address/subnet mask bits. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ip6-subnet </span> - IPv6 network address/subnet mask bits. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> pattern-type </span> - Wildcard pattern or regular expression. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable status. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - Entry type. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> id </span> - ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> name </span> - Name of table. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/spamfilter/bwl/{bwl}</span>  </li>
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



