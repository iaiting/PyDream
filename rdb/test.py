#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import gsocketpool.pool
from mprpc import RPCPoolClient

# print(client.call('tableDrop'))
# print(client.call('tableCreate'))
import tornado.gen


def async_userRetrieve(client_pool):
    with client_pool.connection() as client:
        json_user = '{"phone": "18655590094"}'
        result = client.call('userRetrieve', json_user)
    client.close()
    print(result)


def main():
    client_pool = gsocketpool.pool.Pool(RPCPoolClient, dict(host='127.0.0.1', port=5021))

    async_userRetrieve(client_pool)


if __name__ == '__main__':
    main()
