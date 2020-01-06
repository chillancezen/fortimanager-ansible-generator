#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019 Fortinet, Inc.
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
module: fmgr_pm_config_obj_footer_policy_policy
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get ] the following apis.
    - /pm/config/adom/{adom}/obj/global/footer/policy/{policy}
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
            policy:
                type: str
    schema_object0:
        methods: [get]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the object will be returned.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'chksum - Return the check-sum value instead of attributes.'
                choices:
                    - object member
                    - chksum
                    - datasrc

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: send request to /pm/config/obj/footer/policy/{policy}
      fmgr_pm_config_obj_footer_policy_policy:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            policy: <value of string>
         params:
            - 
               option: <value in [object member, chksum, datasrc]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            action:
               type: str
            active-auth-method:
               type: str
            anti-replay:
               type: str
            app-category:
               type: str
            app-group:
               type: str
            application:
               type: array
               suboptions:
                  type: int
            application-charts:
               type: array
               suboptions:
                  type: str
            application-list:
               type: str
            auth-cert:
               type: str
            auth-method:
               type: str
            auth-path:
               type: str
            auth-portal:
               type: str
            auth-redirect-addr:
               type: str
            auto-asic-offload:
               type: str
            av-profile:
               type: str
            bandwidth:
               type: str
            block-notification:
               type: str
            captive-portal-exempt:
               type: str
            capture-packet:
               type: str
            casi-profile:
               type: str
            central-nat:
               type: str
            cifs-profile:
               type: str
            client-reputation:
               type: str
            client-reputation-mode:
               type: str
            comments:
               type: str
            custom-log-fields:
               type: str
            deep-inspection-options:
               type: str
            delay-tcp-npu-session:
               type: str
            delay-tcp-npu-sessoin:
               type: str
            device-detection-portal:
               type: str
            devices:
               type: str
            diffserv-forward:
               type: str
            diffserv-reverse:
               type: str
            diffservcode-forward:
               type: str
            diffservcode-rev:
               type: str
            disclaimer:
               type: str
            dlp-sensor:
               type: str
            dnsfilter-profile:
               type: str
            dponly:
               type: str
            dscp-match:
               type: str
            dscp-negate:
               type: str
            dscp-value:
               type: str
            dsri:
               type: str
            dstaddr:
               type: str
            dstaddr-negate:
               type: str
            dstaddr6:
               type: str
            dstintf:
               type: str
            dynamic-profile:
               type: str
            dynamic-profile-access:
               type: array
               suboptions:
                  type: str
            dynamic-profile-fallthrough:
               type: str
            dynamic-profile-group:
               type: str
            email-collect:
               type: str
            email-collection-portal:
               type: str
            emailfilter-profile:
               type: str
            endpoint-check:
               type: str
            endpoint-compliance:
               type: str
            endpoint-keepalive-interface:
               type: str
            endpoint-profile:
               type: str
            failed-connection:
               type: str
            fall-through-unauthenticated:
               type: str
            firewall-session-dirty:
               type: str
            fixedport:
               type: str
            forticlient-compliance-devices:
               type: array
               suboptions:
                  type: str
            forticlient-compliance-enforcement-portal:
               type: str
            fsae:
               type: str
            fsae-server-for-ntlm:
               type: str
            fsso:
               type: str
            fsso-agent-for-ntlm:
               type: str
            geo-location:
               type: str
            geoip-anycast:
               type: str
            global-label:
               type: str
            groups:
               type: str
            gtp-profile:
               type: str
            http-policy-redirect:
               type: str
            icap-profile:
               type: str
            identity-based:
               type: str
            identity-based-policy:
               type: array
               suboptions:
                  action:
                     type: str
                  application-charts:
                     type: array
                     suboptions:
                        type: str
                  application-list:
                     type: str
                  av-profile:
                     type: str
                  capture-packet:
                     type: str
                  deep-inspection-options:
                     type: str
                  devices:
                     type: str
                  dlp-sensor:
                     type: str
                  dstaddr:
                     type: str
                  dstaddr-negate:
                     type: str
                  endpoint-compliance:
                     type: str
                  groups:
                     type: str
                  icap-profile:
                     type: str
                  id:
                     type: int
                  ips-sensor:
                     type: str
                  logtraffic:
                     type: str
                  logtraffic-app:
                     type: str
                  logtraffic-start:
                     type: str
                  mms-profile:
                     type: str
                  per-ip-shaper:
                     type: str
                  profile-group:
                     type: str
                  profile-protocol-options:
                     type: str
                  profile-type:
                     type: str
                  replacemsg-group:
                     type: str
                  schedule:
                     type: str
                  send-deny-packet:
                     type: str
                  service:
                     type: str
                  service-negate:
                     type: str
                  spamfilter-profile:
                     type: str
                  sslvpn-portal:
                     type: str
                  sslvpn-realm:
                     type: str
                  traffic-shaper:
                     type: str
                  traffic-shaper-reverse:
                     type: str
                  users:
                     type: str
                  utm-status:
                     type: str
                  voip-profile:
                     type: str
                  webfilter-profile:
                     type: str
            identity-based-route:
               type: str
            identity-from:
               type: str
            inbound:
               type: str
            inspection-mode:
               type: str
            internet-service:
               type: str
            internet-service-custom:
               type: str
            internet-service-custom-group:
               type: str
            internet-service-group:
               type: str
            internet-service-id:
               type: str
            internet-service-negate:
               type: str
            internet-service-src:
               type: str
            internet-service-src-custom:
               type: str
            internet-service-src-custom-group:
               type: str
            internet-service-src-group:
               type: str
            internet-service-src-id:
               type: str
            internet-service-src-negate:
               type: str
            ip-based:
               type: str
            ippool:
               type: str
            ips-sensor:
               type: str
            label:
               type: str
            learning-mode:
               type: str
            log-unmatched-traffic:
               type: str
            logtraffic:
               type: str
            logtraffic-app:
               type: str
            logtraffic-start:
               type: str
            match-vip:
               type: str
            mms-profile:
               type: str
            name:
               type: str
            nat:
               type: str
            natinbound:
               type: str
            natip:
               type: str
            natoutbound:
               type: str
            np-acceleration:
               type: str
            ntlm:
               type: str
            ntlm-enabled-browsers:
               type: array
               suboptions:
                  type: str
            ntlm-guest:
               type: str
            outbound:
               type: str
            per-ip-shaper:
               type: str
            permit-any-host:
               type: str
            permit-stun-host:
               type: str
            policyid:
               type: int
            poolname:
               type: str
            profile-group:
               type: str
            profile-protocol-options:
               type: str
            profile-type:
               type: str
            radius-mac-auth-bypass:
               type: str
            redirect-url:
               type: str
            replacemsg-group:
               type: str
            replacemsg-override-group:
               type: str
            reputation-direction:
               type: str
            reputation-minimum:
               type: int
            require-tfa:
               type: str
            rsso:
               type: str
            rtp-addr:
               type: str
            rtp-nat:
               type: str
            scan-botnet-connections:
               type: str
            schedule:
               type: str
            schedule-timeout:
               type: str
            send-deny-packet:
               type: str
            service:
               type: str
            service-negate:
               type: str
            session-ttl:
               type: int
            sessions:
               type: str
            spamfilter-profile:
               type: str
            srcaddr:
               type: str
            srcaddr-negate:
               type: str
            srcaddr6:
               type: str
            srcintf:
               type: str
            ssh-filter-profile:
               type: str
            ssh-policy-redirect:
               type: str
            ssl-mirror:
               type: str
            ssl-mirror-intf:
               type: str
            ssl-ssh-profile:
               type: str
            sslvpn-auth:
               type: str
            sslvpn-ccert:
               type: str
            sslvpn-cipher:
               type: str
            sso-auth-method:
               type: str
            status:
               type: str
            tags:
               type: str
            tcp-mss-receiver:
               type: int
            tcp-mss-sender:
               type: int
            tcp-reset:
               type: str
            tcp-session-without-syn:
               type: str
            timeout-send-rst:
               type: str
            tos:
               type: str
            tos-mask:
               type: str
            tos-negate:
               type: str
            traffic-shaper:
               type: str
            traffic-shaper-reverse:
               type: str
            transaction-based:
               type: str
            url-category:
               type: str
            users:
               type: str
            utm-inspection-mode:
               type: str
            utm-status:
               type: str
            uuid:
               type: str
            vlan-cos-fwd:
               type: int
            vlan-cos-rev:
               type: int
            vlan-filter:
               type: str
            voip-profile:
               type: str
            vpntunnel:
               type: str
            waf-profile:
               type: str
            wanopt:
               type: str
            wanopt-detection:
               type: str
            wanopt-passive-opt:
               type: str
            wanopt-peer:
               type: str
            wanopt-profile:
               type: str
            wccp:
               type: str
            web-auth-cookie:
               type: str
            webcache:
               type: str
            webcache-https:
               type: str
            webfilter-profile:
               type: str
            webproxy-forward-server:
               type: str
            webproxy-profile:
               type: str
            wsso:
               type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: /pm/config/adom/{adom}/obj/global/footer/policy/{policy}

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible.module_utils.network.fortimanager.common import FAIL_SOCKET_MSG
from ansible.module_utils.network.fortimanager.common import DEFAULT_RESULT_OBJ
from ansible.module_utils.network.fortimanager.common import FMGRCommon
from ansible.module_utils.network.fortimanager.common import FMGBaseException
from ansible.module_utils.network.fortimanager.fortimanager import FortiManagerHandler

def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/global/footer/policy/{policy}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'policy',
            'type': 'string'
        }
    ]

    body_schema =  {
        'schema_objects': {
            'object0': [
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
            'get': 'object0'
        }
    }


    module_arg_spec = {
        'params': {
            'type': 'list',
            'required': False
        },
        'method': {
            'type': 'str',
            'required': True,
            'choices': [
                'get'
            ]
        },
        'url_params': {
            'type': 'dict',
            'required': False
        }
    }
    module = AnsibleModule(argument_spec = module_arg_spec,
                           supports_check_mode = False)
    method = module.params['method']

    fmgr = None
    payload = None
    response = DEFAULT_RESULT_OBJ

    if module._socket_path:
        connection = Connection(module._socket_path)
        tools = FMGRCommon()
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
        fmgr.govern_response(module = module, results = response,
                             msg = 'Operation Finished',
                             ansible_facts = fmgr.construct_ansible_facts(
                                response, module.params, module.params))
    except Exception as e:
        raise FMGBaseException(e)

    module.exit_json(**response[1])

if __name__ == '__main__':
    main()