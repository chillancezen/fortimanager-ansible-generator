#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019-2020 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fmgr_system_sdnconnector
short_description: Configure connection to SDN Connector.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/system/sdn-connector
    - /pm/config/global/obj/system/sdn-connector
    - Examples include all parameters and values need to be adjusted to data sources before usage.

version_added: "2.10"
author:
    - Frank Shen (@fshen01)
    - Link Zheng (@zhengl)
notes:
    - There are only three top-level parameters where 'method' is always required
      while other two 'params' and 'url_params' can be optional
    - Due to the complexity of fortimanager api schema, the validation is done
      out of Ansible native parameter validation procedure.
    - The syntax of OPTIONS doen not comply with the standard Ansible argument
      specification, but with the structure of fortimanager API schema, we need
      a trivial transformation when we are filling the ansible playbook
options:
    workspace_locking_adom:
        description: the adom to lock in case FortiManager running in workspace mode
        required: False
        type: string
        choices:
          - global
          - custom adom
    workspace_locking_timeout:
        description: teh maximum time in seconds to wait for other user to release the workspace lock
        required: False
        type: integer
        default: 300
    url_params:
        description: the parameters in url path
        required: True
        type: dict
        suboptions:
            adom:
                type: str
                description: the domain prefix, the none and global are reserved
                choices:
                  - none
                  - global
                  - custom dom
    schema_object0:
        methods: [add, set, update]
        description: 'Configure connection to SDN Connector.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    _local_cert:
                        type: str
                    access-key:
                        type: str
                        description: 'AWS access key ID.'
                    azure-region:
                        type: str
                        description: 'Azure server region.'
                        choices:
                            - 'global'
                            - 'china'
                            - 'germany'
                            - 'usgov'
                            - 'local'
                    client-id:
                        type: str
                        description: 'Azure client ID (application ID).'
                    client-secret:
                        -
                            type: str
                    compartment-id:
                        type: str
                        description: 'Compartment ID.'
                    external-ip:
                        -
                            name:
                                type: str
                                description: 'External IP name.'
                    gcp-project:
                        type: str
                        description: 'GCP project name.'
                    key-passwd:
                        -
                            type: str
                    login-endpoint:
                        type: str
                        description: 'Azure Stack login enpoint.'
                    name:
                        type: str
                        description: 'SDN connector name.'
                    nic:
                        -
                            ip:
                                -
                                    name:
                                        type: str
                                        description: 'IP configuration name.'
                                    public-ip:
                                        type: str
                                        description: 'Public IP name.'
                            name:
                                type: str
                                description: 'Network interface name.'
                    nsx-cert-fingerprint:
                        type: str
                        description: 'NSX certificate fingerprint.'
                    oci-cert:
                        type: str
                        description: 'OCI certificate.'
                    oci-fingerprint:
                        type: str
                    oci-region:
                        type: str
                        description: 'OCI server region.'
                        choices:
                            - 'phoenix'
                            - 'ashburn'
                            - 'frankfurt'
                            - 'london'
                            - 'toronto'
                    password:
                        -
                            type: str
                    private-key:
                        type: str
                        description: 'Private key of GCP service account.'
                    region:
                        type: str
                        description: 'AWS region name.'
                    resource-group:
                        type: str
                        description: 'Azure resource group.'
                    resource-url:
                        type: str
                        description: 'Azure Stack resource URL.'
                    rest-interface:
                        type: str
                        description: 'Interface name for REST service to listen on.'
                        choices:
                            - 'mgmt'
                            - 'sync'
                    rest-password:
                        -
                            type: str
                    rest-sport:
                        type: int
                        description: 'REST service access port (1 - 65535).'
                    rest-ssl:
                        type: str
                        choices:
                            - 'disable'
                            - 'enable'
                    route:
                        -
                            name:
                                type: str
                                description: 'Route name.'
                    route-table:
                        -
                            name:
                                type: str
                                description: 'Route table name.'
                            route:
                                -
                                    name:
                                        type: str
                                        description: 'Route name.'
                                    next-hop:
                                        type: str
                                        description: 'Next hop address.'
                    secret-key:
                        -
                            type: str
                    server:
                        type: str
                        description: 'Server address of the remote SDN connector.'
                    server-port:
                        type: int
                        description: 'Port number of the remote SDN connector.'
                    service-account:
                        type: str
                        description: 'GCP service account email.'
                    status:
                        type: str
                        description: 'Enable/disable connection to the remote SDN connector.'
                        choices:
                            - 'disable'
                            - 'enable'
                    subscription-id:
                        type: str
                        description: 'Azure subscription ID.'
                    tenant-id:
                        type: str
                        description: 'Tenant ID (directory ID).'
                    type:
                        type: str
                        description: 'Type of SDN connector.'
                        choices:
                            - 'aci'
                            - 'aws'
                            - 'nsx'
                            - 'nuage'
                            - 'azure'
                            - 'gcp'
                            - 'oci'
                            - 'openstack'
                            - 'kubernetes'
                            - 'vmware'
                            - 'acs'
                            - 'alicloud'
                    update-interval:
                        type: int
                        description: 'Dynamic object update interval (0 - 3600 sec, 0 means disabled, default = 60).'
                    use-metadata-iam:
                        type: str
                        description: 'Enable/disable using IAM role from metadata to call API.'
                        choices:
                            - 'disable'
                            - 'enable'
                    user-id:
                        type: str
                        description: 'User ID.'
                    username:
                        type: str
                        description: 'Username of the remote SDN connector as login credentials.'
                    vmx-image-url:
                        type: str
                        description: 'URL of web-hosted VMX image.'
                    vmx-service-name:
                        type: str
                        description: 'VMX Service name.'
                    vpc-id:
                        type: str
                        description: 'AWS VPC ID.'
    schema_object1:
        methods: [get]
        description: 'Configure connection to SDN Connector.'
        api_categories: [api_tag0]
        api_tag0:
            attr:
                type: str
                description: 'The name of the attribute to retrieve its datasource. Only used with &lt;i&gt;datasrc&lt;/i&gt; option.'
            fields:
                -
                    -
                        type: str
                        choices:
                            - '_local_cert'
                            - 'access-key'
                            - 'azure-region'
                            - 'client-id'
                            - 'client-secret'
                            - 'compartment-id'
                            - 'gcp-project'
                            - 'key-passwd'
                            - 'login-endpoint'
                            - 'name'
                            - 'nsx-cert-fingerprint'
                            - 'oci-cert'
                            - 'oci-fingerprint'
                            - 'oci-region'
                            - 'password'
                            - 'private-key'
                            - 'region'
                            - 'resource-group'
                            - 'resource-url'
                            - 'rest-interface'
                            - 'rest-password'
                            - 'rest-sport'
                            - 'rest-ssl'
                            - 'secret-key'
                            - 'server'
                            - 'server-port'
                            - 'service-account'
                            - 'status'
                            - 'subscription-id'
                            - 'tenant-id'
                            - 'type'
                            - 'update-interval'
                            - 'use-metadata-iam'
                            - 'user-id'
                            - 'username'
                            - 'vmx-image-url'
                            - 'vmx-service-name'
                            - 'vpc-id'
            filter:
                -
                    type: str
            get used:
                type: int
            loadsub:
                type: int
                description: 'Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.'
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.'
                 - 'count - Return the number of matching entries instead of the actual entry data.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'datasrc - Return all objects that can be referenced by an attribute. Require <i>attr</i> parameter.'
                 - 'get reserved - Also return reserved objects in the result.'
                 - 'syntax - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.'
                choices:
                    - 'count'
                    - 'object member'
                    - 'datasrc'
                    - 'get reserved'
                    - 'syntax'
            range:
                -
                    type: int
            sortings:
                -
                    varidic.attr_name:
                        type: int
                        choices:
                            - 1
                            - -1

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/SYSTEM/SDN-CONNECTOR
      fmgr_system_sdnconnector:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
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

    - name: REQUESTING /PM/CONFIG/OBJ/SYSTEM/SDN-CONNECTOR
      fmgr_system_sdnconnector:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
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
                     varidic.attr_name: <value in [1, -1]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[add, set, update]
   returned: always
   suboptions:
      id:
         type: int
      result:
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/system/sdn-connector'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            type: array
            suboptions:
               _local_cert:
                  type: str
               access-key:
                  type: str
                  description: 'AWS access key ID.'
               azure-region:
                  type: str
                  description: 'Azure server region.'
               client-id:
                  type: str
                  description: 'Azure client ID (application ID).'
               client-secret:
                  type: array
                  suboptions:
                     type: str
               compartment-id:
                  type: str
                  description: 'Compartment ID.'
               external-ip:
                  type: array
                  suboptions:
                     name:
                        type: str
                        description: 'External IP name.'
               gcp-project:
                  type: str
                  description: 'GCP project name.'
               key-passwd:
                  type: array
                  suboptions:
                     type: str
               login-endpoint:
                  type: str
                  description: 'Azure Stack login enpoint.'
               name:
                  type: str
                  description: 'SDN connector name.'
               nic:
                  type: array
                  suboptions:
                     ip:
                        type: array
                        suboptions:
                           name:
                              type: str
                              description: 'IP configuration name.'
                           public-ip:
                              type: str
                              description: 'Public IP name.'
                     name:
                        type: str
                        description: 'Network interface name.'
               nsx-cert-fingerprint:
                  type: str
                  description: 'NSX certificate fingerprint.'
               oci-cert:
                  type: str
                  description: 'OCI certificate.'
               oci-fingerprint:
                  type: str
               oci-region:
                  type: str
                  description: 'OCI server region.'
               password:
                  type: array
                  suboptions:
                     type: str
               private-key:
                  type: str
                  description: 'Private key of GCP service account.'
               region:
                  type: str
                  description: 'AWS region name.'
               resource-group:
                  type: str
                  description: 'Azure resource group.'
               resource-url:
                  type: str
                  description: 'Azure Stack resource URL.'
               rest-interface:
                  type: str
                  description: 'Interface name for REST service to listen on.'
               rest-password:
                  type: array
                  suboptions:
                     type: str
               rest-sport:
                  type: int
                  description: 'REST service access port (1 - 65535).'
               rest-ssl:
                  type: str
               route:
                  type: array
                  suboptions:
                     name:
                        type: str
                        description: 'Route name.'
               route-table:
                  type: array
                  suboptions:
                     name:
                        type: str
                        description: 'Route table name.'
                     route:
                        type: array
                        suboptions:
                           name:
                              type: str
                              description: 'Route name.'
                           next-hop:
                              type: str
                              description: 'Next hop address.'
               secret-key:
                  type: array
                  suboptions:
                     type: str
               server:
                  type: str
                  description: 'Server address of the remote SDN connector.'
               server-port:
                  type: int
                  description: 'Port number of the remote SDN connector.'
               service-account:
                  type: str
                  description: 'GCP service account email.'
               status:
                  type: str
                  description: 'Enable/disable connection to the remote SDN connector.'
               subscription-id:
                  type: str
                  description: 'Azure subscription ID.'
               tenant-id:
                  type: str
                  description: 'Tenant ID (directory ID).'
               type:
                  type: str
                  description: 'Type of SDN connector.'
               update-interval:
                  type: int
                  description: 'Dynamic object update interval (0 - 3600 sec, 0 means disabled, default = 60).'
               use-metadata-iam:
                  type: str
                  description: 'Enable/disable using IAM role from metadata to call API.'
               user-id:
                  type: str
                  description: 'User ID.'
               username:
                  type: str
                  description: 'Username of the remote SDN connector as login credentials.'
               vmx-image-url:
                  type: str
                  description: 'URL of web-hosted VMX image.'
               vmx-service-name:
                  type: str
                  description: 'VMX Service name.'
               vpc-id:
                  type: str
                  description: 'AWS VPC ID.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/system/sdn-connector'

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FAIL_SOCKET_MSG
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import DEFAULT_RESULT_OBJ
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FMGRCommon
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FMGBaseException
from ansible_collections.fortinet.fortimanager.plugins.module_utils.fortimanager import FortiManagerHandler


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/system/sdn-connector',
        '/pm/config/global/obj/system/sdn-connector'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        '_local_cert': {
                            'type': 'string'
                        },
                        'access-key': {
                            'type': 'string'
                        },
                        'azure-region': {
                            'type': 'string',
                            'enum': [
                                'global',
                                'china',
                                'germany',
                                'usgov',
                                'local'
                            ]
                        },
                        'client-id': {
                            'type': 'string'
                        },
                        'client-secret': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'compartment-id': {
                            'type': 'string'
                        },
                        'external-ip': {
                            'type': 'array',
                            'items': {
                                'name': {
                                    'type': 'string'
                                }
                            }
                        },
                        'gcp-project': {
                            'type': 'string'
                        },
                        'key-passwd': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'login-endpoint': {
                            'type': 'string'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'nic': {
                            'type': 'array',
                            'items': {
                                'ip': {
                                    'type': 'array',
                                    'items': {
                                        'name': {
                                            'type': 'string'
                                        },
                                        'public-ip': {
                                            'type': 'string'
                                        }
                                    }
                                },
                                'name': {
                                    'type': 'string'
                                }
                            }
                        },
                        'nsx-cert-fingerprint': {
                            'type': 'string'
                        },
                        'oci-cert': {
                            'type': 'string'
                        },
                        'oci-fingerprint': {
                            'type': 'string'
                        },
                        'oci-region': {
                            'type': 'string',
                            'enum': [
                                'phoenix',
                                'ashburn',
                                'frankfurt',
                                'london',
                                'toronto'
                            ]
                        },
                        'password': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'private-key': {
                            'type': 'string'
                        },
                        'region': {
                            'type': 'string'
                        },
                        'resource-group': {
                            'type': 'string'
                        },
                        'resource-url': {
                            'type': 'string'
                        },
                        'rest-interface': {
                            'type': 'string',
                            'enum': [
                                'mgmt',
                                'sync'
                            ]
                        },
                        'rest-password': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'rest-sport': {
                            'type': 'integer'
                        },
                        'rest-ssl': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'route': {
                            'type': 'array',
                            'items': {
                                'name': {
                                    'type': 'string'
                                }
                            }
                        },
                        'route-table': {
                            'type': 'array',
                            'items': {
                                'name': {
                                    'type': 'string'
                                },
                                'route': {
                                    'type': 'array',
                                    'items': {
                                        'name': {
                                            'type': 'string'
                                        },
                                        'next-hop': {
                                            'type': 'string'
                                        }
                                    }
                                }
                            }
                        },
                        'secret-key': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'server': {
                            'type': 'string'
                        },
                        'server-port': {
                            'type': 'integer'
                        },
                        'service-account': {
                            'type': 'string'
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'subscription-id': {
                            'type': 'string'
                        },
                        'tenant-id': {
                            'type': 'string'
                        },
                        'type': {
                            'type': 'string',
                            'enum': [
                                'aci',
                                'aws',
                                'nsx',
                                'nuage',
                                'azure',
                                'gcp',
                                'oci',
                                'openstack',
                                'kubernetes',
                                'vmware',
                                'acs',
                                'alicloud'
                            ]
                        },
                        'update-interval': {
                            'type': 'integer'
                        },
                        'use-metadata-iam': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'user-id': {
                            'type': 'string'
                        },
                        'username': {
                            'type': 'string'
                        },
                        'vmx-image-url': {
                            'type': 'string'
                        },
                        'vmx-service-name': {
                            'type': 'string'
                        },
                        'vpc-id': {
                            'type': 'string'
                        }
                    }
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object1': [
                {
                    'type': 'string',
                    'name': 'attr',
                    'api_tag': 0
                },
                {
                    'name': 'fields',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'enum': [
                                '_local_cert',
                                'access-key',
                                'azure-region',
                                'client-id',
                                'client-secret',
                                'compartment-id',
                                'gcp-project',
                                'key-passwd',
                                'login-endpoint',
                                'name',
                                'nsx-cert-fingerprint',
                                'oci-cert',
                                'oci-fingerprint',
                                'oci-region',
                                'password',
                                'private-key',
                                'region',
                                'resource-group',
                                'resource-url',
                                'rest-interface',
                                'rest-password',
                                'rest-sport',
                                'rest-ssl',
                                'secret-key',
                                'server',
                                'server-port',
                                'service-account',
                                'status',
                                'subscription-id',
                                'tenant-id',
                                'type',
                                'update-interval',
                                'use-metadata-iam',
                                'user-id',
                                'username',
                                'vmx-image-url',
                                'vmx-service-name',
                                'vpc-id'
                            ]
                        }
                    }
                },
                {
                    'name': 'filter',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'example': [
                                '<attr>',
                                '==',
                                'test'
                            ]
                        }
                    },
                    'api_tag': 0
                },
                {
                    'type': 'integer',
                    'name': 'get used',
                    'api_tag': 0
                },
                {
                    'type': 'integer',
                    'name': 'loadsub',
                    'api_tag': 0
                },
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'count',
                            'object member',
                            'datasrc',
                            'get reserved',
                            'syntax'
                        ]
                    },
                    'api_tag': 0
                },
                {
                    'name': 'range',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            'type': 'integer',
                            'example': [
                                2,
                                5
                            ]
                        }
                    },
                    'api_tag': 0
                },
                {
                    'name': 'sortings',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            '{attr_name}': {
                                'type': 'integer',
                                'enum': [
                                    1,
                                    -1
                                ]
                            }
                        }
                    },
                    'api_tag': 0
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ]
        },
        'method_mapping': {
            'add': 'object0',
            'get': 'object1',
            'set': 'object0',
            'update': 'object0'
        }
    }

    module_arg_spec = {
        'loose_validation': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'workspace_locking_adom': {
            'type': 'str',
            'required': False
        },
        'workspace_locking_timeout': {
            'type': 'int',
            'required': False,
            'default': 300
        },
        'params': {
            'type': 'list',
            'required': False
        },
        'method': {
            'type': 'str',
            'required': True,
            'choices': [
                'add',
                'get',
                'set',
                'update'
            ]
        },
        'url_params': {
            'type': 'dict',
            'required': False
        }
    }
    module = AnsibleModule(argument_spec=module_arg_spec,
                           supports_check_mode=False)
    method = module.params['method']
    loose_validation = module.params['loose_validation']

    fmgr = None
    payload = None
    response = DEFAULT_RESULT_OBJ

    if module._socket_path:
        connection = Connection(module._socket_path)
        tools = FMGRCommon()
        if loose_validation == False:
            tools.validate_module_params(module, body_schema)
        tools.validate_module_url_params(module, jrpc_urls, url_schema)
        full_url = tools.get_full_url_path(module, jrpc_urls)
        payload = tools.get_full_payload(module, full_url)
        fmgr = FortiManagerHandler(connection, module)
        fmgr.tools = tools
    else:
        module.fail_json(**FAIL_SOCKET_MSG)

    try:
        response = fmgr._conn.send_request(method, payload)
        fmgr.govern_response(module=module, results=response,
                             msg='Operation Finished',
                             ansible_facts=fmgr.construct_ansible_facts(response, module.params, module.params))
    except Exception as e:
        raise FMGBaseException(e)

    module.exit_json(meta=response[1])


if __name__ == '__main__':
    main()
