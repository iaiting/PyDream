#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import libpy.config


class SelfConfig(object):

    def __init__(self, filename):
        rc = libpy.config.readConfig('config.ini')
        self.host = self.__getHost(rc)
        self.port = self.__getPort(rc)
        self.rdb = self.__getRdb(rc)

    def __getHost(self, rc):
        return rc.get_skv('SELF', 'host')

    def __getPort(self, rc):
        return rc.get_skv('SELF', 'port')

    def __getRdb(self, rc):
        user = rc.get_skv('RDB', 'user')
        password = rc.get_skv('RDB', 'password')
        host = rc.get_skv('RDB', 'host')
        dbname = rc.get_skv('RDB', 'dbname')
        rdb = 'postgresql://{}:{}@{}/{}'.format(user, password, host, dbname)
        return rdb


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
