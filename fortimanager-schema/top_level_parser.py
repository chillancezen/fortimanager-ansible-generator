#! /usr/bin/python3
import json
import urllib.parse

config_db_whitelist = ['Configuration Database v6.0']

import sys
if __name__ == "__main__":
    assert(len(sys.argv) == 2)
    json_file = sys.argv[1]

    modules = list()
    with open(json_file) as f:
        data = json.load(f)
        assert("sideMenuData" in data)
        assert("submenu" in data["sideMenuData"])
        for i in data["sideMenuData"]["submenu"]:
            if i['title'].find('FortiManager') >= 0:
                assert('submenu' in i)
                modules = i['submenu']
                break

    for mod in modules:
        if mod['title'].find('Configuration Database') >= 0 and \
           mod['title'] not in config_db_whitelist:
            continue
        sub_modules = mod['submenu']
        for sub_mod in sub_modules:
            paths = sub_mod['submenu']
            for path in paths:
                print(path['path'], path['handler'], urllib.parse.quote(path['path'], safe=''))
