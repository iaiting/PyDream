#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import signal
import msgpackrpc
import ..libpy.config
import table.user
import gobject.selfconfig
import time


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    rc = libpy.config.readConfig('config.ini')
    config = {
        'SELF': {
            'host': rc.get_skv('SELF', 'host'),
            'port': rc.get_skv('SELF', 'port')
        },
        'RDB': {
            'host': rc.get_skv('RDB', 'host'),
            'port': rc.get_skv('RDB', 'port'),
            'user': rc.get_skv('RDB', 'user'),
            'password': rc.get_skv('RDB', 'password'),
            'dbname': rc.get_skv('RDB', 'dbname')
        }
    }
    sc = gobject.selfconfig.SelfConfig(**config)
    tuser = table.user.User()
    server = msgpackrpc.Server(tuser)
    server.listen(msgpackrpc.Address(sc.SELF['host'], sc.SELF['port']))
    server.start()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.run_forever()
