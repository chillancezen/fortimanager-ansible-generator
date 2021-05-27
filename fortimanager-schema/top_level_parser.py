#! /usr/bin/python3
import json
import sys
import urllib.parse

config_db_whitelist = ['Database Modules', 'Daemon Modules']

def usage():
    print('usage: top_level_parser.py top_level_apipath.json [6.2.0|6.4.0|7.0.0]')
    sys.exit(1)

import sys
if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()

    json_file = sys.argv[1]
    config_db_version = sys.argv[2]
    if len(config_db_version.split('.')) != 3:
        usage()

    f_out = open('top_level_apipath.metadata.%s' % (config_db_version), 'w')
    modules = list()
    with open(json_file) as f:
        data = json.load(f)
        assert("sideMenuData" in data)
        assert("submenu" in data["sideMenuData"])
        for i in data["sideMenuData"]["submenu"]:
            title = i['title']
            if title == 'FortiManager %s' % (config_db_version):
                assert('submenu' in i)
                modules = i['submenu']
                break

    for mod in modules:
        title = mod['title']
        if title not in config_db_whitelist:
            assert('Configuration Database ' in title)
            ver = title[len('Configuration Database '):]
            if ver != 'v%s.%s' % (config_db_version[0], config_db_version[2]):
                continue
        sub_modules = mod['submenu']
        for sub_mod in sub_modules:
            paths = sub_mod['submenu']
            for path in paths:
                f_out.write('%s %s %s\n' % (path['path'], path['handler'], urllib.parse.quote(path['path'], safe='')))
    f_out.close()
