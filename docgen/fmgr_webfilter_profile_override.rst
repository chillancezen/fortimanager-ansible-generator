:source: fmgr_webfilter_profile_override.py

:orphan:

.. _fmgr_webfilter_profile_override:

fmgr_webfilter_profile_override -- Web Filter override settings.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/webfilter/profile/{profile}/override`
- `/pm/config/global/obj/webfilter/profile/{profile}/override`
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
 <li><span class="li-head">profile</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Web Filter override settings.</li>
 <ul class="ul-self">
 <li><span class="li-head">option</span> - Set fetch option for the request. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [object member, chksum, datasrc]</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Web Filter override settings.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">ovrd-cookie</span> - Allow/deny browser-based (cookie) overrides. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [deny, allow]</span> </li>
 <li><span class="li-head">ovrd-dur</span> - Override duration. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">ovrd-dur-mode</span> - Override duration mode. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [constant, ask]</span> </li>
 <li><span class="li-head">ovrd-scope</span> - Override scope. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [user, user-group, ip, ask, browser]</span> </li>
 <li><span class="li-head">ovrd-user-group</span> - User groups with permission to use the override. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile</span> - Web filter profile with permission to create overrides. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">profile-attribute</span> - Profile attribute to retrieve from the RADIUS server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [User-Name, User-Password, CHAP-Password, NAS-IP-Address, NAS-Port, Service-Type, Framed-Protocol, Framed-IP-Address, Framed-IP-Netmask, Framed-Routing, Filter-Id, Framed-MTU, Framed-Compression, Login-IP-Host, Login-Service, Login-TCP-Port, Reply-Message, Callback-Number, Callback-Id, Framed-Route, Framed-IPX-Network, State, Class, Vendor-Specific, Session-Timeout, Idle-Timeout, Termination-Action, Called-Station-Id, Calling-Station-Id, NAS-Identifier, Proxy-State, Login-LAT-Service, Login-LAT-Node, Login-LAT-Group, Framed-AppleTalk-Link, Framed-AppleTalk-Network, Framed-AppleTalk-Zone, Acct-Status-Type, Acct-Delay-Time, Acct-Input-Octets, Acct-Output-Octets, Acct-Session-Id, Acct-Authentic, Acct-Session-Time, Acct-Input-Packets, Acct-Output-Packets, Acct-Terminate-Cause, Acct-Multi-Session-Id, Acct-Link-Count, CHAP-Challenge, NAS-Port-Type, Port-Limit, Login-LAT-Port]</span> </li>
 <li><span class="li-head">profile-type</span> - Override profile type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [list, radius]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/WEBFILTER/PROFILE/{PROFILE}/OVERRIDE
      fmgr_webfilter_profile_override:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/WEBFILTER/PROFILE/{PROFILE}/OVERRIDE
      fmgr_webfilter_profile_override:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               data:
                  ovrd-cookie: <value in [deny, allow]>
                  ovrd-dur: <value of string>
                  ovrd-dur-mode: <value in [constant, ask]>
                  ovrd-scope: <value in [user, user-group, ip, ...]>
                  ovrd-user-group: <value of string>
                  profile: <value of string>
                  profile-attribute: <value in [User-Name, User-Password, CHAP-Password, ...]>
                  profile-type: <value in [list, radius]>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> ovrd-cookie </span> - Allow/deny browser-based (cookie) overrides. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ovrd-dur </span> - Override duration. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ovrd-dur-mode </span> - Override duration mode. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ovrd-scope </span> - Override scope. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> ovrd-user-group </span> - User groups with permission to use the override. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> profile </span> - Web filter profile with permission to create overrides. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> profile-attribute </span> - Profile attribute to retrieve from the RADIUS server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> profile-type </span> - Override profile type. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/webfilter/profile/{profile}/override</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/webfilter/profile/{profile}/override</span>  </li>
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



