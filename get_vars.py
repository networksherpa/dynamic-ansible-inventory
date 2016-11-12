#!/usr/bin/env python

import redis
import argparse
import json


def list_arg(args, redis_connection):

    return_val = json.loads(redis_connection.get("inventory"))

    return return_val


def host_arg(hostname, redis_connection):
    redis_output = json.loads(redis_connection.get(hostname))

    return redis_output["settings"]


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', action='store')
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--local', action='store_true')
    parser.add_argument('-v', action='store_true')

    return parser.parse_args()


def main():

    args = parse_arguments()
    redis_connection = redis.Redis('localhost')

    if args.host:
        print host_arg(args.host, redis_connection)
    if args.list:
        print list_arg(args, redis_connection)


if __name__ == "__main__":
    main()
