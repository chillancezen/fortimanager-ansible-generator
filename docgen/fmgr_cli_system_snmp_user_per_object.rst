:source: fmgr_cli_system_snmp_user_per_object.py

:orphan:

.. _fmgr_cli_system_snmp_user_per_object:

fmgr_cli_system_snmp_user_per_object -- SNMP user configuration.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[delete, get, set, update]** the following FortiManager json-rpc urls.
- `/cli/global/system/snmp/user/{user}`
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
 <li><span class="li-head">user</span> - the object name <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">parameters for method: [delete, get]</span> - SNMP user configuration.</li>
 <ul class="ul-self">
 </ul>
 <li><span class="li-head">parameters for method: [set, update]</span> - SNMP user configuration.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li><span class="li-head">auth-proto</span> - Authentication protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [md5, sha]</span>  <span class="li-normal">default: sha</span> </li>
 <li><span class="li-head">auth-pwd</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC NjAyNzczNjcyNzY3Nzg1Of2B29hwP1lYq82MXmrQ1PG7EGaRNDqkrqYFYL1NNEgm54idZER+oDi44SCyPKkvrPPrxgkkBtYnh1uQ3hobimfdeMd2rooTubF9B+lKXyq06wTtneMsxzjLK1SP1NNDy91keEpVFpDTpHpRtZ1meW8+NS8k</span> </li>
 </ul>
 <li><span class="li-head">events</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disk_low, ha_switch, intf_ip_chg, sys_reboot, cpu_high, mem_low, log-alert, log-rate, log-data-rate, lic-gbday, lic-dev-quota, cpu-high-exclude-nice]</span> </li>
 </ul>
 <li><span class="li-head">name</span> - SNMP user name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">notify-hosts</span> - Hosts to send notifications (traps) to. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">notify-hosts6</span> - IPv6 hosts to send notifications (traps) to. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">priv-proto</span> - Privacy (encryption) protocol. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [aes, des]</span>  <span class="li-normal">default: aes</span> </li>
 <li><span class="li-head">priv-pwd</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">default: ENC OTA3MDU5Nzg1ODQ2MDM2NInoPzPSYfTulrcxKZ65Re1ROZUOMQVvU4dqPX5WkABZ8PkpLAOtCEZJPjCcJbybir6Dw9yptXUDyKN4hUHbzauIOAQ2Az8BlB5n4ifkMNTkDDDxZ7r6oB0GK+QmJM9n2wjUGMCcVi0sG9l4bc9sFFuBi4mJ</span> </li>
 </ul>
 <li><span class="li-head">queries</span> - Enable/disable queries for this user. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span>  <span class="li-normal">default: enable</span> </li>
 <li><span class="li-head">query-port</span> - SNMPv3 query port. <span class="li-normal">type: int</span>  <span class="li-normal">default: 161</span> </li>
 <li><span class="li-head">security-level</span> - Security level for message authentication and encryption. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [no-auth-no-priv, auth-no-priv, auth-priv]</span>  <span class="li-normal">default: no-auth-no-priv</span> </li>
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

    - name: REQUESTING /CLI/SYSTEM/SNMP/USER/{USER}
      fmgr_cli_system_snmp_user_per_object:
         method: <value in [set, update]>
         url_params:
            user: <value of string>
         params:
            -
               data:
                  auth-proto: <value in [md5, sha] default: 'sha'>
                  auth-pwd:
                    - <value of string default: 'ENC NjAyNzczNjcyNzY3Nzg1Of2B29hwP1lYq82MXmrQ1PG7EGaRNDqkrqYFYL1NNEgm54idZER+...'>
                  events:
                    - <value in [disk_low, ha_switch, intf_ip_chg, ...]>
                  name: <value of string>
                  notify-hosts: <value of string>
                  notify-hosts6: <value of string>
                  priv-proto: <value in [aes, des] default: 'aes'>
                  priv-pwd:
                    - <value of string default: 'ENC OTA3MDU5Nzg1ODQ2MDM2NInoPzPSYfTulrcxKZ65Re1ROZUOMQVvU4dqPX5WkABZ8PkpLAOt...'>
                  queries: <value in [disable, enable] default: 'enable'>
                  query-port: <value of integer default: 161>
                  security-level: <value in [no-auth-no-priv, auth-no-priv, auth-priv] default: 'no-auth-no-priv'>



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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/snmp/user/{user}</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> auth-proto </span> - Authentication protocol. <span class="li-normal">type: str</span>  <span class="li-normal">example: sha</span>  </li>
 <li> <span class="li-return"> auth-pwd </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC NjAyNzczNjcyNzY3Nzg1Of2B29hwP1lYq82MXmrQ1PG7EGaRNDqkrqYFYL1NNEgm54idZER+oDi44SCyPKkvrPPrxgkkBtYnh1uQ3hobimfdeMd2rooTubF9B+lKXyq06wTtneMsxzjLK1SP1NNDy91keEpVFpDTpHpRtZ1meW8+NS8k</span>  </li>
 </ul>
 <li> <span class="li-return"> events </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> name </span> - SNMP user name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> notify-hosts </span> - Hosts to send notifications (traps) to. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> notify-hosts6 </span> - IPv6 hosts to send notifications (traps) to. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> priv-proto </span> - Privacy (encryption) protocol. <span class="li-normal">type: str</span>  <span class="li-normal">example: aes</span>  </li>
 <li> <span class="li-return"> priv-pwd </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: ENC OTA3MDU5Nzg1ODQ2MDM2NInoPzPSYfTulrcxKZ65Re1ROZUOMQVvU4dqPX5WkABZ8PkpLAOtCEZJPjCcJbybir6Dw9yptXUDyKN4hUHbzauIOAQ2Az8BlB5n4ifkMNTkDDDxZ7r6oB0GK+QmJM9n2wjUGMCcVi0sG9l4bc9sFFuBi4mJ</span>  </li>
 </ul>
 <li> <span class="li-return"> queries </span> - Enable/disable queries for this user. <span class="li-normal">type: str</span>  <span class="li-normal">example: enable</span>  </li>
 <li> <span class="li-return"> query-port </span> - SNMPv3 query port. <span class="li-normal">type: int</span>  <span class="li-normal">example: 161</span>  </li>
 <li> <span class="li-return"> security-level </span> - Security level for message authentication and encryption. <span class="li-normal">type: str</span>  <span class="li-normal">example: no-auth-no-priv</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /cli/global/system/snmp/user/{user}</span>  </li>
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



