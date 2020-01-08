:source: fmgr_pm_config_obj_vpn_ssl_web_portal_bookmark_group.py

:orphan:

.. _fmgr_pm_config_obj_vpn_ssl_web_portal_bookmark_group:

fmgr_pm_config_obj_vpn_ssl_web_portal_bookmark_group -- Portal bookmark group.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/vpn/ssl/web/portal/{portal}/bookmark-group`
- `/pm/config/global/obj/vpn/ssl/web/portal/{portal}/bookmark-group`
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
 <li><span class="li-head">portal</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Portal bookmark group.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">bookmarks</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">additional-params</span> - Additional parameters. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">apptype</span> - Application type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [web, telnet, ssh, ftp, smb, vnc, rdp, citrix, rdpnative, portforward, sftp]</span> </li>
 <li><span class="li-head">description</span> - Description. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">folder</span> - Network shared file folder parameter. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">form-data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - Name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">value</span> - Value. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">host</span> - Host name/IP parameter. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">listening-port</span> - Listening port (0 - 65535). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">load-balancing-info</span> - The load balancing information or cookie which should be provided to the connection broker. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">logon-password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">logon-user</span> - Logon user. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Bookmark name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">port</span> - Remote port. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">preconnection-blob</span> - An arbitrary string which identifies the RDP source. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">preconnection-id</span> - The numeric ID of the RDP source (0-2147483648). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">remote-port</span> - Remote port (0 - 65535). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">security</span> - Security mode for RDP connection. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [rdp, nla, tls, any]</span> </li>
 <li><span class="li-head">server-layout</span> - Server side keyboard layout. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [en-us-qwerty, de-de-qwertz, fr-fr-azerty, it-it-qwerty, sv-se-qwerty, failsafe, en-gb-qwerty, es-es-qwerty, fr-ch-qwertz, ja-jp-qwerty, pt-br-qwerty, tr-tr-qwerty]</span> </li>
 <li><span class="li-head">show-status-window</span> - Enable/disable showing of status window. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sso</span> - Single Sign-On. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, static, auto]</span> </li>
 <li><span class="li-head">sso-credential</span> - Single sign-on credentials. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [sslvpn-login, alternative]</span> </li>
 <li><span class="li-head">sso-credential-sent-once</span> - Single sign-on credentials are only sent once to remote server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">sso-password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">sso-username</span> - SSO user name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">url</span> - URL parameter. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">name</span> - Bookmark group name. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Portal bookmark group.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [name]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/VPN/SSL/WEB/PORTAL/{PORTAL}/BOOKMARK-GROUP
      fmgr_pm_config_obj_vpn_ssl_web_portal_bookmark_group:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            portal: <value of string>
         params:
            -
               data:
                 -
                     bookmarks:
                       -
                           additional-params: <value of string>
                           apptype: <value in [web, telnet, ssh, ...]>
                           description: <value of string>
                           folder: <value of string>
                           form-data:
                             -
                                 name: <value of string>
                                 value: <value of string>
                           host: <value of string>
                           listening-port: <value of integer>
                           load-balancing-info: <value of string>
                           logon-password:
                             - <value of string>
                           logon-user: <value of string>
                           name: <value of string>
                           port: <value of integer>
                           preconnection-blob: <value of string>
                           preconnection-id: <value of integer>
                           remote-port: <value of integer>
                           security: <value in [rdp, nla, tls, ...]>
                           server-layout: <value in [en-us-qwerty, de-de-qwertz, fr-fr-azerty, ...]>
                           show-status-window: <value in [disable, enable]>
                           sso: <value in [disable, static, auto]>
                           sso-credential: <value in [sslvpn-login, alternative]>
                           sso-credential-sent-once: <value in [disable, enable]>
                           sso-password:
                             - <value of string>
                           sso-username: <value of string>
                           url: <value of string>
                     name: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/VPN/SSL/WEB/PORTAL/{PORTAL}/BOOKMARK-GROUP
      fmgr_pm_config_obj_vpn_ssl_web_portal_bookmark_group:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            portal: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [name]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/vpn/ssl/web/portal/{portal}/bookmark-group</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> bookmarks </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> additional-params </span> - Additional parameters. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> apptype </span> - Application type. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> description </span> - Description. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> folder </span> - Network shared file folder parameter. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> form-data </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - Name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> value </span> - Value. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> host </span> - Host name/IP parameter. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> listening-port </span> - Listening port (0 - 65535). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> load-balancing-info </span> - The load balancing information or cookie which should be provided to the connection broker. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> logon-password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> logon-user </span> - Logon user. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Bookmark name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> port </span> - Remote port. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> preconnection-blob </span> - An arbitrary string which identifies the RDP source. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> preconnection-id </span> - The numeric ID of the RDP source (0-2147483648). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> remote-port </span> - Remote port (0 - 65535). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> security </span> - Security mode for RDP connection. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server-layout </span> - Server side keyboard layout. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> show-status-window </span> - Enable/disable showing of status window. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sso </span> - Single Sign-On. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sso-credential </span> - Single sign-on credentials. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sso-credential-sent-once </span> - Single sign-on credentials are only sent once to remote server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sso-password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> sso-username </span> - SSO user name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> url </span> - URL parameter. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> name </span> - Bookmark group name. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/vpn/ssl/web/portal/{portal}/bookmark-group</span>  </li>
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



