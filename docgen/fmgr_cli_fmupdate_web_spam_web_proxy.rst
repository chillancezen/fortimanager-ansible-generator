:source: fmgr_cli_fmupdate_web_spam_web_proxy.py

:orphan:

.. _fmgr_cli_fmupdate_web_spam_web_proxy:

fmgr_cli_fmupdate_web_spam_web_proxy -- Configure the web proxy for use with FortiGuard antivirus and IPS updates.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/fmupdate/web-spam/web-proxy`
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
 <li><span class="li-head">parameters for method: [get]</span> - Configure the web proxy for use with FortiGuard antivirus and IPS updates.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - Configure the web proxy for use with FortiGuard antivirus and IPS updates.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">ip</span> - IPv4 address of the web proxy. <span class="li-normal">type: str</span>  <span class="li-normal">default: 0.0.0.0</span> </li>
 <li><span class="li-head">ip6</span> - IPv6 address of the web proxy. <span class="li-normal">type: str</span>  <span class="li-normal">default: ::</span> </li>
 <li><span class="li-head">mode</span> - Web proxy mode: proxy - http proxy, tunnel - http tunnel (default = proxy). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [proxy, tunnel]</span>  <span class="li-normal">default: proxy</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC MTQ4ODM1MjcyOTk3ODExNreUBchLdkFIbIbcd8CigXCsJs8gguZ6mOjknXBH4Tm3shANGNo7nlVP8rFMUYX0OzAZMe+28CSkktL4ruOhitTk30S9SNOWireuoDy4UZdB2Dp2KCir8uYTdjFXK1Dw1YExtuDv8hnAdcTrE7EGsuayqVn5</span> </li>
 </ul>
 <li><span class="li-head">port</span> - The port number of the web proxy (1 - 65535, default = 80). <span class="li-normal">type: int</span>  <span class="li-normal">default: 80</span> </li>
 <li><span class="li-head">status</span> - Enable/disable connections through the web proxy (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: disable</span> </li>
 <li><span class="li-head">username</span> - The user name used for authentication. <span class="li-normal">type: str</span> </li>
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

    - name: REQUESTING /CLI/FMUPDATE/WEB-SPAM/WEB-PROXY
      fmgr_cli_fmupdate_web_spam_web_proxy:
         method: <value in [set, update]>
         params:
            -
               data:
                  ip: <value of string default: '0.0.0.0'>
                  ip6: <value of string default: '::'>
                  mode: <value in [proxy, tunnel] default: 'proxy'>
                  password:
                    - <value of string default: 'ENC MTQ4ODM1MjcyOTk3ODExNreUBchLdkFIbIbcd8CigXCsJs8gguZ6mOjknXBH4Tm3shANGNo7...'>
                  port: <value of integer default: 80>
                  status: <value in [disable, enable] default: 'disable'>
                  username: <value of string>



Return Values
-------------


Common return values are documented: https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values, the following are the fields unique to this module:


.. raw:: html

 <ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> ip </span> - IPv4 address of the web proxy. <span class="li-normal">type: str</span>  <span class="li-normal">example: 0.0.0.0</span>  </li>
 <li> <span class="li-return"> ip6 </span> - IPv6 address of the web proxy. <span class="li-normal">type: str</span>  <span class="li-normal">example: ::</span>  </li>
 <li> <span class="li-return"> mode </span> - Web proxy mode: proxy - http proxy, tunnel - http tunnel (default = proxy). <span class="li-normal">type: str</span>  <span class="li-normal">example: proxy</span>  </li>
 <li> <span class="li-return"> password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC MTQ4ODM1MjcyOTk3ODExNreUBchLdkFIbIbcd8CigXCsJs8gguZ6mOjknXBH4Tm3shANGNo7nlVP8rFMUYX0OzAZMe+28CSkktL4ruOhitTk30S9SNOWireuoDy4UZdB2Dp2KCir8uYTdjFXK1Dw1YExtuDv8hnAdcTrE7EGsuayqVn5</span>  </li>
 </ul>
 <li> <span class="li-return"> port </span> - The port number of the web proxy (1 - 65535, default = 80). <span class="li-normal">type: int</span>  <span class="li-normal">example: 80</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable connections through the web proxy (default = disable). <span class="li-normal">type: str</span>  <span class="li-normal">example: disable</span>  </li>
 <li> <span class="li-return"> username </span> - The user name used for authentication. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/fmupdate/web-spam/web-proxy</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [set, update]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/fmupdate/web-spam/web-proxy</span>  </li>
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



