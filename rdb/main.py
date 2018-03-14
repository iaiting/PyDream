#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import signal
import gobject.selfconfig
from gevent.server import StreamServer
from rdb.rdbserver import RdbServer


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    sc = gobject.selfconfig.SelfConfig('config.ini')
    print('Welcome to %s:%s' % (sc.host, sc.port))
    server = StreamServer((sc.host, int(sc.port)), RdbServer(sc.rdb))
    server.serve_forever()

if __name__ == '__main__':
    main()
