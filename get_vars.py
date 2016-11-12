#!/usr/bin/env python

import redis
import argparse
import json

conn = redis.Redis('localhost')


def get_inventory():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', action='store')
    parser.add_argument('--list', action='store_true')
    parser.add_argument('-v', action='store_true')
    args = parser.parse_args()

    if args.host:
        return json.dumps(conn.get("inventory"))
    elif args.list:
        return_val = json.dumps(conn.get("inventory"))
        if args.v:
            print return_val
        return return_val
    else:
        return {'_meta': {'hostvars': {}}}


# get_var.py --host leaf01
# {u'network': {u'hosts': [u'spine01', u'leaf01'], u'vars': {u'ansible_ssh_pass': u'CumulusLinux!', u'ansible_user': u'cumulus', u'ansible_become_pass': u'CumulusLinux!'}}}
get_inventory()

#redis_string = conn.get("leaf02")

# blah = json.loads(redis_string)

# print blah["lo"]

# inventory = '{ \
#     "network": { \
#         "hosts": ["spine01", "leaf01"], \
#         "vars": { \
#             "ansible_user": "cumulus", \
#             "ansible_ssh_pass": "CumulusLinux!", \
#             "ansible_become_pass": "CumulusLinux!" \
#         } \
#     } \
# }'
