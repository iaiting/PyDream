#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import signal
import tornado.web
import tornado.options
import libpy.config
import gobject.selfconfig
import handler.route


def main():
    # windows can not use ctrl + c exit process
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    tornado.options.parse_command_line()
    sc = gobject.selfconfig.SelfConfig('config.ini')
    handlers = handler.route.get_handlers()
    application = handler.route.Application(sc.rdbpool, handlers=handlers)
    application.listen(sc.port)

    print('tornado web application start at: %s:%s' % (sc.host, sc.port))
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
