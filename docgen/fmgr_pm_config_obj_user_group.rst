:source: fmgr_pm_config_obj_user_group.py

:orphan:

.. _fmgr_pm_config_obj_user_group:

fmgr_pm_config_obj_user_group -- Configure user groups.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/user/group`
- `/pm/config/global/obj/user/group`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure user groups.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">auth-concurrent-override</span> - Enable/disable overriding the global number of concurrent authentication sessions for this user group. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">auth-concurrent-value</span> - Maximum number of concurrent authenticated connections per user (0 - 100). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">authtimeout</span> - Authentication timeout in minutes for this user group. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">company</span> - Set the action for the company guest user field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [optional, mandatory, disabled]</span> </li>
 <li><span class="li-head">email</span> - Enable/disable the guest user email address field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">expire</span> - Time in seconds before guest user accounts expire. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">expire-type</span> - Determine when the expiration countdown begins. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [immediately, first-successful-login]</span> </li>
 <li><span class="li-head">group-type</span> - Set the group to be for firewall authentication, FSSO, RSSO, or guest users. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [firewall, directory-service, fsso-service, guest, rsso]</span> </li>
 <li><span class="li-head">guest</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">comment</span> - Comment. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">company</span> - Set the action for the company guest user field. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">email</span> - Email. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">expiration</span> - Expire time. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mobile-phone</span> - Mobile phone. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - Guest name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">sponsor</span> - Set the action for the sponsor guest user field. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">user-id</span> - Guest ID. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">http-digest-realm</span> - Realm attribute for MD5-digest authentication. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - Group ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">match</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_gui_meta</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">group-name</span> - Name of matching group on remote authentication server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">id</span> - ID. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">server-name</span> - Name of remote auth server. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">max-accounts</span> - Maximum number of guest accounts that can be created for this group (0 means unlimited). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">member</span> - Names of users, peers, LDAP severs, or RADIUS servers to add to the user group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">mobile-phone</span> - Enable/disable the guest user mobile phone number field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">multiple-guest-add</span> - Enable/disable addition of multiple guests. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">name</span> - Group name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">password</span> - Guest user password type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auto-generate, specify, disable]</span> </li>
 <li><span class="li-head">sms-custom-server</span> - SMS server. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">sms-server</span> - Send SMS through FortiGuard or other external server. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [fortiguard, custom]</span> </li>
 <li><span class="li-head">sponsor</span> - Set the action for the sponsor guest user field. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [optional, mandatory, disabled]</span> </li>
 <li><span class="li-head">sso-attribute-value</span> - Name of the RADIUS user group that this local user group represents. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">user-id</span> - Guest user ID type. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [email, auto-generate, specify]</span> </li>
 <li><span class="li-head">user-name</span> - Enable/disable the guest user name entry. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure user groups.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [auth-concurrent-override, auth-concurrent-value, authtimeout, company, email, expire, expire-type, group-type, http-digest-realm, id, max-accounts, member, mobile-phone, multiple-guest-add, name, password, sms-custom-server, sms-server, sponsor, sso-attribute-value, user-id, user-name]</span> </li>
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

    - name: REQUESTING /PM/CONFIG/OBJ/USER/GROUP
      fmgr_pm_config_obj_user_group:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     auth-concurrent-override: <value in [disable, enable]>
                     auth-concurrent-value: <value of integer>
                     authtimeout: <value of integer>
                     company: <value in [optional, mandatory, disabled]>
                     email: <value in [disable, enable]>
                     expire: <value of integer>
                     expire-type: <value in [immediately, first-successful-login]>
                     group-type: <value in [firewall, directory-service, fsso-service, ...]>
                     guest:
                       -
                           comment: <value of string>
                           company: <value of string>
                           email: <value of string>
                           expiration: <value of string>
                           mobile-phone: <value of string>
                           name: <value of string>
                           password:
                             - <value of string>
                           sponsor: <value of string>
                           user-id: <value of string>
                     http-digest-realm: <value of string>
                     id: <value of integer>
                     match:
                       -
                           _gui_meta: <value of string>
                           group-name: <value of string>
                           id: <value of integer>
                           server-name: <value of string>
                     max-accounts: <value of integer>
                     member: <value of string>
                     mobile-phone: <value in [disable, enable]>
                     multiple-guest-add: <value in [disable, enable]>
                     name: <value of string>
                     password: <value in [auto-generate, specify, disable]>
                     sms-custom-server: <value of string>
                     sms-server: <value in [fortiguard, custom]>
                     sponsor: <value in [optional, mandatory, disabled]>
                     sso-attribute-value: <value of string>
                     user-id: <value in [email, auto-generate, specify]>
                     user-name: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/USER/GROUP
      fmgr_pm_config_obj_user_group:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [auth-concurrent-override, auth-concurrent-value, authtimeout, ...]>
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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/user/group</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> auth-concurrent-override </span> - Enable/disable overriding the global number of concurrent authentication sessions for this user group. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> auth-concurrent-value </span> - Maximum number of concurrent authenticated connections per user (0 - 100). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> authtimeout </span> - Authentication timeout in minutes for this user group. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> company </span> - Set the action for the company guest user field. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> email </span> - Enable/disable the guest user email address field. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> expire </span> - Time in seconds before guest user accounts expire. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> expire-type </span> - Determine when the expiration countdown begins. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> group-type </span> - Set the group to be for firewall authentication, FSSO, RSSO, or guest users. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> guest </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> comment </span> - Comment. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> company </span> - Set the action for the company guest user field. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> email </span> - Email. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> expiration </span> - Expire time. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mobile-phone </span> - Mobile phone. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Guest name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> sponsor </span> - Set the action for the sponsor guest user field. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> user-id </span> - Guest ID. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> http-digest-realm </span> - Realm attribute for MD5-digest authentication. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - Group ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> match </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> _gui_meta </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> group-name </span> - Name of matching group on remote authentication server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> id </span> - ID. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> server-name </span> - Name of remote auth server. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> max-accounts </span> - Maximum number of guest accounts that can be created for this group (0 means unlimited). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> member </span> - Names of users, peers, LDAP severs, or RADIUS servers to add to the user group. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> mobile-phone </span> - Enable/disable the guest user mobile phone number field. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> multiple-guest-add </span> - Enable/disable addition of multiple guests. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - Group name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> password </span> - Guest user password type. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sms-custom-server </span> - SMS server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sms-server </span> - Send SMS through FortiGuard or other external server. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sponsor </span> - Set the action for the sponsor guest user field. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> sso-attribute-value </span> - Name of the RADIUS user group that this local user group represents. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> user-id </span> - Guest user ID type. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> user-name </span> - Enable/disable the guest user name entry. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/user/group</span>  </li>
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



