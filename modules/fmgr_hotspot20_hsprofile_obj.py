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
module: fmgr_hotspot20_hsprofile_obj
short_description: Configure hotspot profile.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/wireless-controller/hotspot20/hs-profile/{hs-profile}
    - /pm/config/global/obj/wireless-controller/hotspot20/hs-profile/{hs-profile}
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
    loose_validation:
        description: Do parameter validation in a loose way
        required: False
        type: bool
        default: false
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
            hs-profile:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Configure hotspot profile.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                3gpp-plmn:
                    type: str
                    description: '3GPP PLMN name.'
                access-network-asra:
                    type: str
                    description: 'Enable/disable additional step required for access (ASRA).'
                    choices:
                        - 'disable'
                        - 'enable'
                access-network-esr:
                    type: str
                    description: 'Enable/disable emergency services reachable (ESR).'
                    choices:
                        - 'disable'
                        - 'enable'
                access-network-internet:
                    type: str
                    description: 'Enable/disable connectivity to the Internet.'
                    choices:
                        - 'disable'
                        - 'enable'
                access-network-type:
                    type: str
                    description: 'Access network type.'
                    choices:
                        - 'private-network'
                        - 'private-network-with-guest-access'
                        - 'chargeable-public-network'
                        - 'free-public-network'
                        - 'personal-device-network'
                        - 'emergency-services-only-network'
                        - 'test-or-experimental'
                        - 'wildcard'
                access-network-uesa:
                    type: str
                    description: 'Enable/disable unauthenticated emergency service accessible (UESA).'
                    choices:
                        - 'disable'
                        - 'enable'
                anqp-domain-id:
                    type: int
                    description: 'ANQP Domain ID (0-65535).'
                bss-transition:
                    type: str
                    description: 'Enable/disable basic service set (BSS) transition Support.'
                    choices:
                        - 'disable'
                        - 'enable'
                conn-cap:
                    type: str
                    description: 'Connection capability name.'
                deauth-request-timeout:
                    type: int
                    description: 'Deauthentication request timeout (in seconds).'
                dgaf:
                    type: str
                    description: 'Enable/disable downstream group-addressed forwarding (DGAF).'
                    choices:
                        - 'disable'
                        - 'enable'
                domain-name:
                    type: str
                    description: 'Domain name.'
                gas-comeback-delay:
                    type: int
                    description: 'GAS comeback delay (0 or 100 - 4000 milliseconds, default = 500).'
                gas-fragmentation-limit:
                    type: int
                    description: 'GAS fragmentation limit (512 - 4096, default = 1024).'
                hessid:
                    type: str
                    description: 'Homogeneous extended service set identifier (HESSID).'
                ip-addr-type:
                    type: str
                    description: 'IP address type name.'
                l2tif:
                    type: str
                    description: 'Enable/disable Layer 2 traffic inspection and filtering.'
                    choices:
                        - 'disable'
                        - 'enable'
                nai-realm:
                    type: str
                    description: 'NAI realm list name.'
                name:
                    type: str
                    description: 'Hotspot profile name.'
                network-auth:
                    type: str
                    description: 'Network authentication name.'
                oper-friendly-name:
                    type: str
                    description: 'Operator friendly name.'
                osu-provider:
                    type: str
                    description: 'Manually selected list of OSU provider(s).'
                osu-ssid:
                    type: str
                    description: 'Online sign up (OSU) SSID.'
                pame-bi:
                    type: str
                    description: 'Enable/disable Pre-Association Message Exchange BSSID Independent (PAME-BI).'
                    choices:
                        - 'disable'
                        - 'enable'
                proxy-arp:
                    type: str
                    description: 'Enable/disable Proxy ARP.'
                    choices:
                        - 'disable'
                        - 'enable'
                qos-map:
                    type: str
                    description: 'QoS MAP set ID.'
                roaming-consortium:
                    type: str
                    description: 'Roaming consortium list name.'
                venue-group:
                    type: str
                    description: 'Venue group.'
                    choices:
                        - 'unspecified'
                        - 'assembly'
                        - 'business'
                        - 'educational'
                        - 'factory'
                        - 'institutional'
                        - 'mercantile'
                        - 'residential'
                        - 'storage'
                        - 'utility'
                        - 'vehicular'
                        - 'outdoor'
                venue-name:
                    type: str
                    description: 'Venue name.'
                venue-type:
                    type: str
                    description: 'Venue type.'
                    choices:
                        - 'unspecified'
                        - 'arena'
                        - 'stadium'
                        - 'passenger-terminal'
                        - 'amphitheater'
                        - 'amusement-park'
                        - 'place-of-worship'
                        - 'convention-center'
                        - 'library'
                        - 'museum'
                        - 'restaurant'
                        - 'theater'
                        - 'bar'
                        - 'coffee-shop'
                        - 'zoo-or-aquarium'
                        - 'emergency-center'
                        - 'doctor-office'
                        - 'bank'
                        - 'fire-station'
                        - 'police-station'
                        - 'post-office'
                        - 'professional-office'
                        - 'research-facility'
                        - 'attorney-office'
                        - 'primary-school'
                        - 'secondary-school'
                        - 'university-or-college'
                        - 'factory'
                        - 'hospital'
                        - 'long-term-care-facility'
                        - 'rehab-center'
                        - 'group-home'
                        - 'prison-or-jail'
                        - 'retail-store'
                        - 'grocery-market'
                        - 'auto-service-station'
                        - 'shopping-mall'
                        - 'gas-station'
                        - 'private'
                        - 'hotel-or-motel'
                        - 'dormitory'
                        - 'boarding-house'
                        - 'automobile'
                        - 'airplane'
                        - 'bus'
                        - 'ferry'
                        - 'ship-or-boat'
                        - 'train'
                        - 'motor-bike'
                        - 'muni-mesh-network'
                        - 'city-park'
                        - 'rest-area'
                        - 'traffic-control'
                        - 'bus-stop'
                        - 'kiosk'
                wan-metrics:
                    type: str
                    description: 'WAN metric name.'
                wnm-sleep-mode:
                    type: str
                    description: 'Enable/disable wireless network management (WNM) sleep mode.'
                    choices:
                        - 'disable'
                        - 'enable'
    schema_object1:
        methods: [delete]
        description: 'Configure hotspot profile.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Configure hotspot profile.'
        api_categories: [api_tag0]
        api_tag0:
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the object will be returned.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'chksum - Return the check-sum value instead of attributes.'
                choices:
                    - 'object member'
                    - 'chksum'
                    - 'datasrc'

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

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/HOTSPOT20/HS-PROFILE/{HS-PROFILE}
      fmgr_hotspot20_hsprofile_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            hs-profile: <value of string>
         params:
            -
               data:
                  3gpp-plmn: <value of string>
                  access-network-asra: <value in [disable, enable]>
                  access-network-esr: <value in [disable, enable]>
                  access-network-internet: <value in [disable, enable]>
                  access-network-type: <value in [private-network, private-network-with-guest-access, chargeable-public-network, ...]>
                  access-network-uesa: <value in [disable, enable]>
                  anqp-domain-id: <value of integer>
                  bss-transition: <value in [disable, enable]>
                  conn-cap: <value of string>
                  deauth-request-timeout: <value of integer>
                  dgaf: <value in [disable, enable]>
                  domain-name: <value of string>
                  gas-comeback-delay: <value of integer>
                  gas-fragmentation-limit: <value of integer>
                  hessid: <value of string>
                  ip-addr-type: <value of string>
                  l2tif: <value in [disable, enable]>
                  nai-realm: <value of string>
                  name: <value of string>
                  network-auth: <value of string>
                  oper-friendly-name: <value of string>
                  osu-provider: <value of string>
                  osu-ssid: <value of string>
                  pame-bi: <value in [disable, enable]>
                  proxy-arp: <value in [disable, enable]>
                  qos-map: <value of string>
                  roaming-consortium: <value of string>
                  venue-group: <value in [unspecified, assembly, business, ...]>
                  venue-name: <value of string>
                  venue-type: <value in [unspecified, arena, stadium, ...]>
                  wan-metrics: <value of string>
                  wnm-sleep-mode: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/HOTSPOT20/HS-PROFILE/{HS-PROFILE}
      fmgr_hotspot20_hsprofile_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            hs-profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[clone, delete, set, update]
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
            example: '/pm/config/adom/{adom}/obj/wireless-controller/hotspot20/hs-profile/{hs-profile}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            3gpp-plmn:
               type: str
               description: '3GPP PLMN name.'
            access-network-asra:
               type: str
               description: 'Enable/disable additional step required for access (ASRA).'
            access-network-esr:
               type: str
               description: 'Enable/disable emergency services reachable (ESR).'
            access-network-internet:
               type: str
               description: 'Enable/disable connectivity to the Internet.'
            access-network-type:
               type: str
               description: 'Access network type.'
            access-network-uesa:
               type: str
               description: 'Enable/disable unauthenticated emergency service accessible (UESA).'
            anqp-domain-id:
               type: int
               description: 'ANQP Domain ID (0-65535).'
            bss-transition:
               type: str
               description: 'Enable/disable basic service set (BSS) transition Support.'
            conn-cap:
               type: str
               description: 'Connection capability name.'
            deauth-request-timeout:
               type: int
               description: 'Deauthentication request timeout (in seconds).'
            dgaf:
               type: str
               description: 'Enable/disable downstream group-addressed forwarding (DGAF).'
            domain-name:
               type: str
               description: 'Domain name.'
            gas-comeback-delay:
               type: int
               description: 'GAS comeback delay (0 or 100 - 4000 milliseconds, default = 500).'
            gas-fragmentation-limit:
               type: int
               description: 'GAS fragmentation limit (512 - 4096, default = 1024).'
            hessid:
               type: str
               description: 'Homogeneous extended service set identifier (HESSID).'
            ip-addr-type:
               type: str
               description: 'IP address type name.'
            l2tif:
               type: str
               description: 'Enable/disable Layer 2 traffic inspection and filtering.'
            nai-realm:
               type: str
               description: 'NAI realm list name.'
            name:
               type: str
               description: 'Hotspot profile name.'
            network-auth:
               type: str
               description: 'Network authentication name.'
            oper-friendly-name:
               type: str
               description: 'Operator friendly name.'
            osu-provider:
               type: str
               description: 'Manually selected list of OSU provider(s).'
            osu-ssid:
               type: str
               description: 'Online sign up (OSU) SSID.'
            pame-bi:
               type: str
               description: 'Enable/disable Pre-Association Message Exchange BSSID Independent (PAME-BI).'
            proxy-arp:
               type: str
               description: 'Enable/disable Proxy ARP.'
            qos-map:
               type: str
               description: 'QoS MAP set ID.'
            roaming-consortium:
               type: str
               description: 'Roaming consortium list name.'
            venue-group:
               type: str
               description: 'Venue group.'
            venue-name:
               type: str
               description: 'Venue name.'
            venue-type:
               type: str
               description: 'Venue type.'
            wan-metrics:
               type: str
               description: 'WAN metric name.'
            wnm-sleep-mode:
               type: str
               description: 'Enable/disable wireless network management (WNM) sleep mode.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/wireless-controller/hotspot20/hs-profile/{hs-profile}'

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
        '/pm/config/adom/{adom}/obj/wireless-controller/hotspot20/hs-profile/{hs-profile}',
        '/pm/config/global/obj/wireless-controller/hotspot20/hs-profile/{hs-profile}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'hs-profile',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        '3gpp-plmn': {
                            'type': 'string'
                        },
                        'access-network-asra': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'access-network-esr': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'access-network-internet': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'access-network-type': {
                            'type': 'string',
                            'enum': [
                                'private-network',
                                'private-network-with-guest-access',
                                'chargeable-public-network',
                                'free-public-network',
                                'personal-device-network',
                                'emergency-services-only-network',
                                'test-or-experimental',
                                'wildcard'
                            ]
                        },
                        'access-network-uesa': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'anqp-domain-id': {
                            'type': 'integer'
                        },
                        'bss-transition': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'conn-cap': {
                            'type': 'string'
                        },
                        'deauth-request-timeout': {
                            'type': 'integer'
                        },
                        'dgaf': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'domain-name': {
                            'type': 'string'
                        },
                        'gas-comeback-delay': {
                            'type': 'integer'
                        },
                        'gas-fragmentation-limit': {
                            'type': 'integer'
                        },
                        'hessid': {
                            'type': 'string'
                        },
                        'ip-addr-type': {
                            'type': 'string'
                        },
                        'l2tif': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'nai-realm': {
                            'type': 'string'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'network-auth': {
                            'type': 'string'
                        },
                        'oper-friendly-name': {
                            'type': 'string'
                        },
                        'osu-provider': {
                            'type': 'string'
                        },
                        'osu-ssid': {
                            'type': 'string'
                        },
                        'pame-bi': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'proxy-arp': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'qos-map': {
                            'type': 'string'
                        },
                        'roaming-consortium': {
                            'type': 'string'
                        },
                        'venue-group': {
                            'type': 'string',
                            'enum': [
                                'unspecified',
                                'assembly',
                                'business',
                                'educational',
                                'factory',
                                'institutional',
                                'mercantile',
                                'residential',
                                'storage',
                                'utility',
                                'vehicular',
                                'outdoor'
                            ]
                        },
                        'venue-name': {
                            'type': 'string'
                        },
                        'venue-type': {
                            'type': 'string',
                            'enum': [
                                'unspecified',
                                'arena',
                                'stadium',
                                'passenger-terminal',
                                'amphitheater',
                                'amusement-park',
                                'place-of-worship',
                                'convention-center',
                                'library',
                                'museum',
                                'restaurant',
                                'theater',
                                'bar',
                                'coffee-shop',
                                'zoo-or-aquarium',
                                'emergency-center',
                                'doctor-office',
                                'bank',
                                'fire-station',
                                'police-station',
                                'post-office',
                                'professional-office',
                                'research-facility',
                                'attorney-office',
                                'primary-school',
                                'secondary-school',
                                'university-or-college',
                                'factory',
                                'hospital',
                                'long-term-care-facility',
                                'rehab-center',
                                'group-home',
                                'prison-or-jail',
                                'retail-store',
                                'grocery-market',
                                'auto-service-station',
                                'shopping-mall',
                                'gas-station',
                                'private',
                                'hotel-or-motel',
                                'dormitory',
                                'boarding-house',
                                'automobile',
                                'airplane',
                                'bus',
                                'ferry',
                                'ship-or-boat',
                                'train',
                                'motor-bike',
                                'muni-mesh-network',
                                'city-park',
                                'rest-area',
                                'traffic-control',
                                'bus-stop',
                                'kiosk'
                            ]
                        },
                        'wan-metrics': {
                            'type': 'string'
                        },
                        'wnm-sleep-mode': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        }
                    },
                    'api_tag': 0
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
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object2': [
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'object member',
                            'chksum',
                            'datasrc'
                        ]
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
            'clone': 'object0',
            'delete': 'object1',
            'get': 'object2',
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
                'clone',
                'delete',
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
