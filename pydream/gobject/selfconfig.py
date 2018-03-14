#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import gsocketpool.pool
from mprpc import RPCPoolClient
import libpy.config
from mprpc import RPCClient


class SelfConfig(object):

    def __init__(self, filname):
        rc = libpy.config.readConfig(filname)
        self.host = self.__getHost(rc)
        self.port = self.__getPort(rc)
        self.rdbpool = self.__getRdbpool(rc)

    def __getHost(self, rc):
        return rc.get_skv('SELF', 'host')

    def __getPort(self, rc):
        return rc.get_skv('SELF', 'port')

    def __getRdbclient(self, rc):
        host = rc.get_skv('RDB', 'host')
        port = rc.get_skv('RDB', 'port')
        rdbpool = gsocketpool.pool.Pool(RPCPoolClient, dict(host=host, port=int(port)))
        return rdbpool


def test():
    kwds = {
        'SELF': {'host': '127.0.0.1',   'port': '5011'},
        'RDB': {'host': '127.0.0.1',   'port': '5021'},
        'MONGODB': {'host': '127.0.0.1',   'port': '5031'},
        'REDIS': {'host': '127.0.0.1',   'port': '5041'},
    }
    sc = SelfConfig(**kwds)
    print(sc.RDB)
if __name__ == '__main__':
    test()
