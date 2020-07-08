# This code is part of Ansible, but is an independent component.
# This particular file snippet, and this file snippet only, is BSD licensed.
# Modules you write using this snippet, which is embedded dynamically by Ansible
# still belong to the author of the module, and may assign their own license
# to the complete work.
#
# (c) 2020 Fortinet, Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class NAPIManager(object):
    jrpc_urls = None
    perobject_jrpc_urls = None
    module_primary_key = None
    url_params = None
    module = None
    conn = None
    module_name = None
    module_level2_name = None

    def __init__(self, jrpc_urls, perobject_jrpc_urls, module_primary_key, url_params, module, conn):
        self.jrpc_urls = jrpc_urls
        self.perobject_jrpc_urls = perobject_jrpc_urls
        self.module_primary_key = module_primary_key
        self.url_params = url_params
        self.module = module
        self.conn = conn
        self.process_workspace_lock()
        self.module_name = self.module._name
        self.module_level2_name = self.module_name[5:]

    def process_workspace_lock(self):
        self.conn.process_workspace_locking(self.module.params)

    def _get_basic_url(self, is_perobject):
        url_libs = None
        if is_perobject:
            url_libs = [i for i in self.perobject_jrpc_urls]
        else:
            url_libs = [i for i in self.jrpc_urls]
        for uparam in self.url_params:
            assert(self.module.params[uparam])
        the_url = None
        if 'adom' in self.url_params:
            adom = self.module.params['adom']
            if adom == 'global':
                for url in url_libs:
                    if '/global/' in url:
                        the_url = url
                        break
                if not the_url:
                    self.module.fail_json(msg='No global url for the request, please use other adom.')
            else:
                for url in url_libs:
                    if '/adom/{adom}/' in url:
                        the_url = url
                        break
                if not the_url:
                    self.module.fail_json(msg='No url for the requested adom:%s, please use other adom.' % (adom))
        else:
            the_url = url_libs[0]
        assert(the_url)
        for uparam in self.url_params:
            token_hint = '/%s/{%s}/' % (uparam, uparam)
            token = '/%s/%s/' % (uparam, self.module.params[uparam])
            the_url = the_url.replace(token_hint, token)
        return the_url

    def _get_base_perobject_url(self, mvalue):
        url_getting = self._get_basic_url(True)
        last_token = url_getting.split('/')[-1]
        second_last_token = url_getting.split('/')[-2]
        assert(last_token == ('{' + second_last_token + '}'))
        return url_getting.replace('{' + second_last_token + '}', str(mvalue))

    def get_object(self, mvalue):
        url_getting = self._get_base_perobject_url(mvalue)
        params = [{'url': url_getting}]
        response = self.conn.send_request('get', params)
        return response

    def update_object(self, mvalue):
        url_updating = self._get_base_perobject_url(mvalue)
        params = [{'url': url_updating, 'data': self.module.params[self.module_level2_name]}]
        response = self.conn.send_request('update', params)
        return response

    def create_objejct(self):
        url_creating = self._get_basic_url(False)
        params = [{'url': url_creating, 'data': self.module.params[self.module_level2_name]}]
        return self.conn.send_request('add', params)
    
    def delete_object(self, mvalue):
        url_deleting = self._get_base_perobject_url(mvalue)
        params = [{'url': url_deleting}]
        return self.conn.send_request('delete', params)

    def _process_with_mkey(self, mvalue):
        mobject = self.get_object(mvalue)
        if self.module.params['state'] == 'present':
            if mobject[0] == 0:
                return self.update_object(mvalue)
            else:
                return self.create_objejct()
        elif self.module.params['state'] == 'absent':
            if mobject[0] == 0:
                return self.delete_object(mvalue)
            else:
                self.do_nonexist_exit()
        else:
            assert(False)

    def _process_without_mkey(self):
        if self.module.params['state'] == 'absent':
            self.module.fail_json(msg='this module doesn\'t not support state:absent because of no primary key.')
        return self.create_objejct()

    def process_fact(self, metadata):
        assert(self.module.params['facts']['selector'] in metadata)
        selector = self.module.params['facts']['selector']
        fact_params = metadata[selector]['params']
        fact_urls = metadata[selector]['urls']
        assert(len(fact_urls))

        real_params_keys = set()
        if self.module.params['facts']['params']:
            real_params_keys = set(self.module.params['facts']['params'].keys())
        if real_params_keys != set(fact_params):
            self.module.fail_json(msg = 'expect params:%s, real params:%s' % (list(fact_params), list(real_params_keys)))
        url = None
        if 'adom' in fact_params and not fact_urls[0].endswith('{adom}'):
            if self.module.params['facts']['params']['adom'] == 'global':
                for _url in fact_urls:
                    if '/global/' in _url:
                        url = _url
                        break
            else:
                for _url in fact_urls:
                    if '/adom/{adom}/' in _url:
                        url = _url
                        #url = _url.replace('/adom/{adom}/', '/adom/%s/' % (self.module.params['facts']['params']['adom']))
                        break
        else:
            url = fact_urls[0]
        if not url:
            self.module.fail_json(msg='can not find url in following sets:%s! please check params: adom' % (fact_urls))
        for _param in fact_params:
            token_hint = '/%s/{%s}' % (_param, _param)
            token = '/%s/%s' % (_param, self.module.params['facts']['params'][_param])
            url = url.replace(token_hint, token)

        # Now issue the request.
        api_params = [{'url': url}]
        response = self.conn.send_request('get', api_params)
        self.do_exit(response)

    def process_curd(self):
        assert('state' in self.module.params)
        has_mkey = self.module_primary_key is not None
        if has_mkey:
            mvalue = self.module.params[self.module_level2_name][self.module_primary_key]
            self.do_exit(self._process_with_mkey(mvalue))
        else:
            self.do_exit(self._process_without_mkey())

    def _do_final_exit(self, rc, result):
        # XXX: as with https://github.com/fortinet/ansible-fortimanager-generic.
        # the failing conditions priority: failed_when > rc_failed > rc_succeeded.
        failed = rc != 0
        changed = rc == 0

        assert('response_code' in result)
        if self.module.params['rc_failed']:
            for rc_code in self.module.params['rc_failed']:
                if str(result['response_code']) == str(rc_code):
                    failed = True
                    result['result_code_overriding'] = 'rc code:%s is overridden to failure' % (rc_code)
        elif self.module.params['rc_succeeded']:
            for rc_code in self.module.params['rc_succeeded']:
                if str(result['response_code']) == str(rc_code):
                    failed = False
                    result['result_code_overriding'] = 'rc code:%s is overridden to success' % (rc_code)
        self.module.exit_json(rc=rc, meta=result, failed=failed, changed=changed)

    def do_nonexist_exit(self):
        rc = 0
        result = dict()
        result['response_code'] = -3
        result['response_message'] = 'object not exist'
        self._do_final_exit(rc, result)


    def do_exit(self, response):
        rc = response[0]
        result = dict()
        if 'data' in response[1]:
            result['response_data'] = response[1]['data']
        result['response_code'] = response[1]['status']['code']
        result['response_message'] = response[1]['status']['message']
        result['request_url'] = response[1]['url']
        # XXX:Do further status mapping
        self._do_final_exit(rc, result)
