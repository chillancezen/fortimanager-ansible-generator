:source: fmgr_pm_config_obj_system_sdn_connector.py

:orphan:

.. _fmgr_pm_config_obj_system_sdn_connector:

fmgr_pm_config_obj_system_sdn_connector -- Configure connection to SDN Connector.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.10

.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is able to configure a FortiManager device by allowing the user to **[add, get, set, update]** the following FortiManager json-rpc urls.
- `/pm/config/adom/{adom}/obj/system/sdn-connector`
- `/pm/config/global/obj/system/sdn-connector`
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
 <li><span class="li-head">parameters for method: [add, set, update]</span> - Configure connection to SDN Connector.</li>
 <ul class="ul-self">
 <li><span class="li-head">data</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">_local_cert</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">access-key</span> - AWS access key ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">azure-region</span> - Azure server region. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [global, china, germany, usgov, local]</span> </li>
 <li><span class="li-head">client-id</span> - Azure client ID (application ID). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">client-secret</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">compartment-id</span> - Compartment ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">external-ip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - External IP name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">gcp-project</span> - GCP project name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">key-passwd</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">login-endpoint</span> - Azure Stack login enpoint. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">name</span> - SDN connector name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">nic</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">ip</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - IP configuration name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">public-ip</span> - Public IP name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">name</span> - Network interface name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">nsx-cert-fingerprint</span> - NSX certificate fingerprint. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">oci-cert</span> - OCI certificate. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">oci-fingerprint</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">oci-region</span> - OCI server region. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [phoenix, ashburn, frankfurt, london, toronto]</span> </li>
 <li><span class="li-head">password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">private-key</span> - Private key of GCP service account. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">region</span> - AWS region name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">resource-group</span> - Azure resource group. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">resource-url</span> - Azure Stack resource URL. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">rest-interface</span> - Interface name for REST service to listen on. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [mgmt, sync]</span> </li>
 <li><span class="li-head">rest-password</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">rest-sport</span> - REST service access port (1 - 65535). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">rest-ssl</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">route</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - Route name. <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">route-table</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - Route table name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">route</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">name</span> - Route name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">next-hop</span> - Next hop address. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">secret-key</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span> </li>
 </ul>
 <li><span class="li-head">server</span> - Server address of the remote SDN connector. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">server-port</span> - Port number of the remote SDN connector. <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">service-account</span> - GCP service account email. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">status</span> - Enable/disable connection to the remote SDN connector. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">subscription-id</span> - Azure subscription ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">tenant-id</span> - Tenant ID (directory ID). <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">type</span> - Type of SDN connector. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [aci, aws, nsx, nuage, azure, gcp, oci, openstack, kubernetes, vmware, acs, alicloud]</span> </li>
 <li><span class="li-head">update-interval</span> - Dynamic object update interval (0 - 3600 sec, 0 means disabled, default = 60). <span class="li-normal">type: int</span> </li>
 <li><span class="li-head">use-metadata-iam</span> - Enable/disable using IAM role from metadata to call API. <span class="li-normal">type: str</span>  <span class="li-normal">choices: [disable, enable]</span> </li>
 <li><span class="li-head">user-id</span> - User ID. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">username</span> - Username of the remote SDN connector as login credentials. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vmx-image-url</span> - URL of web-hosted VMX image. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vmx-service-name</span> - VMX Service name. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">vpc-id</span> - AWS VPC ID. <span class="li-normal">type: str</span> </li>
 </ul>
 </ul>
 <li><span class="li-head">parameters for method: [get]</span> - Configure connection to SDN Connector.</li>
 <ul class="ul-self">
 <li><span class="li-head">attr</span> - The name of the attribute to retrieve its datasource. <span class="li-normal">type: str</span> </li>
 <li><span class="li-head">fields</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-head">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">choices: [_local_cert, access-key, azure-region, client-id, client-secret, compartment-id, gcp-project, key-passwd, login-endpoint, name, nsx-cert-fingerprint, oci-cert, oci-fingerprint, oci-region, password, private-key, region, resource-group, resource-url, rest-interface, rest-password, rest-sport, rest-ssl, secret-key, server, server-port, service-account, status, subscription-id, tenant-id, type, update-interval, use-metadata-iam, user-id, username, vmx-image-url, vmx-service-name, vpc-id]</span> </li>
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
    - name: send request to /pm/config/obj/system/sdn-connector
      fmgr_pm_config_obj_system_sdn_connector:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            - 
               data: 
                - 
                     _local_cert: <value of string>
                     access-key: <value of string>
                     azure-region: <value in [global, china, germany, ...]>
                     client-id: <value of string>
                     client-secret: 
                      - <value of string>
                     compartment-id: <value of string>
                     external-ip: 
                      - 
                           name: <value of string>
                     gcp-project: <value of string>
                     key-passwd: 
                      - <value of string>
                     login-endpoint: <value of string>
                     name: <value of string>
                     nic: 
                      - 
                           ip: 
                            - 
                                 name: <value of string>
                                 public-ip: <value of string>
                           name: <value of string>
                     nsx-cert-fingerprint: <value of string>
                     oci-cert: <value of string>
                     oci-fingerprint: <value of string>
                     oci-region: <value in [phoenix, ashburn, frankfurt, ...]>
                     password: 
                      - <value of string>
                     private-key: <value of string>
                     region: <value of string>
                     resource-group: <value of string>
                     resource-url: <value of string>
                     rest-interface: <value in [mgmt, sync]>
                     rest-password: 
                      - <value of string>
                     rest-sport: <value of integer>
                     rest-ssl: <value in [disable, enable]>
                     route: 
                      - 
                           name: <value of string>
                     route-table: 
                      - 
                           name: <value of string>
                           route: 
                            - 
                                 name: <value of string>
                                 next-hop: <value of string>
                     secret-key: 
                      - <value of string>
                     server: <value of string>
                     server-port: <value of integer>
                     service-account: <value of string>
                     status: <value in [disable, enable]>
                     subscription-id: <value of string>
                     tenant-id: <value of string>
                     type: <value in [aci, aws, nsx, ...]>
                     update-interval: <value of integer>
                     use-metadata-iam: <value in [disable, enable]>
                     user-id: <value of string>
                     username: <value of string>
                     vmx-image-url: <value of string>
                     vmx-service-name: <value of string>
                     vpc-id: <value of string>
    - name: send request to /pm/config/obj/system/sdn-connector
      fmgr_pm_config_obj_system_sdn_connector:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            - 
               attr: <value of string>
               fields: 
                - 
                   - <value in [_local_cert, access-key, azure-region, ...]>
               filter: 
                - <value of string>
               get used: <value of integer>
               loadsub: <value of integer>
               option: <value in [count, object member, datasrc, ...]>
               range: 
                - <value of integer>
               sortings: 
                - 
                     \{attr_name\}: <value in [1, -1]>



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
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/system/sdn-connector</span>  </li>
 </ul>
 <li><span class="li-return"> return values for method: [get]</span> </li>
 <ul class="ul-self">
 <li><span class="li-return">data</span>
 - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> _local_cert </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> access-key </span> - AWS access key ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> azure-region </span> - Azure server region. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> client-id </span> - Azure client ID (application ID). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> client-secret </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> compartment-id </span> - Compartment ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> external-ip </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - External IP name. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> gcp-project </span> - GCP project name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> key-passwd </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> login-endpoint </span> - Azure Stack login enpoint. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> name </span> - SDN connector name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> nic </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> ip </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - IP configuration name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> public-ip </span> - Public IP name. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> name </span> - Network interface name. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> nsx-cert-fingerprint </span> - NSX certificate fingerprint. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> oci-cert </span> - OCI certificate. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> oci-fingerprint </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> oci-region </span> - OCI server region. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> private-key </span> - Private key of GCP service account. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> region </span> - AWS region name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> resource-group </span> - Azure resource group. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> resource-url </span> - Azure Stack resource URL. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rest-interface </span> - Interface name for REST service to listen on. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> rest-password </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> rest-sport </span> - REST service access port (1 - 65535). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> rest-ssl </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> route </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - Route name. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> route-table </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - Route table name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> route </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li> <span class="li-return"> name </span> - Route name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> next-hop </span> - Next hop address. <span class="li-normal">type: str</span>  </li>
 </ul>
 </ul>
 <li> <span class="li-return"> secret-key </span> - No description for the parameter <span class="li-normal">type: array</span> <ul class="ul-self">
 <li><span class="li-return">{no-name}</span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li> <span class="li-return"> server </span> - Server address of the remote SDN connector. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> server-port </span> - Port number of the remote SDN connector. <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> service-account </span> - GCP service account email. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> status </span> - Enable/disable connection to the remote SDN connector. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> subscription-id </span> - Azure subscription ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> tenant-id </span> - Tenant ID (directory ID). <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> type </span> - Type of SDN connector. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> update-interval </span> - Dynamic object update interval (0 - 3600 sec, 0 means disabled, default = 60). <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> use-metadata-iam </span> - Enable/disable using IAM role from metadata to call API. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> user-id </span> - User ID. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> username </span> - Username of the remote SDN connector as login credentials. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vmx-image-url </span> - URL of web-hosted VMX image. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vmx-service-name </span> - VMX Service name. <span class="li-normal">type: str</span>  </li>
 <li> <span class="li-return"> vpc-id </span> - AWS VPC ID. <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">status</span>
 - No description for the parameter <span class="li-normal">type: dict</span> <ul class="ul-self">
 <li> <span class="li-return"> code </span> - No description for the parameter <span class="li-normal">type: int</span>  </li>
 <li> <span class="li-return"> message </span> - No description for the parameter <span class="li-normal">type: str</span>  </li>
 </ul>
 <li><span class="li-return">url</span>
 - No description for the parameter <span class="li-normal">type: str</span>  <span class="li-normal">example: /pm/config/adom/{adom}/obj/system/sdn-connector</span>  </li>
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



