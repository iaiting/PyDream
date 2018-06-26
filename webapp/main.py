#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==============================================================================
#
# Author        : iaiting@aliyun.com
# Generate Data : 2018-03-22
# Desciption    : 基于tornado框架下的web应用开发
#
# ==============================================================================

import os
import signal
import tornado.ioloop
import tornado.web

import handler.restapi

# ------------------------------------------------------------------------------
def set_app_option():
    template_path=os.path.join(os.path.dirname(__file__), "template"),

# ------------------------------------------------------------------------------
def register_signal():
    signal.signal(signal.SIGINT,  signal.SIG_DFL)


#-------------------------------------------------------------------------------
def register_app():
    handlers = [
        (r"/user", handler.restapi.user.Handler),
        (r"/firend", handler.restapi.firend.Handler),
    ]

    settings = dict(
           debug=True,
    )
    application = tornado.web.Application(handlers, **settings)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


def get_handlers():
    return  [
        (r"/user/(\w+)", handler.restapi.user.Handler),
        (r"/firend", handler.restapi.firend.Handler),

        # my study test
        (r"/", handler.restapi.test.IndexHandler),
        (r"/wrap", handler.restapi.test.WrapHandler),
        (r"/reverse/(\w+)", handler.restapi.test.ReverseHandler),
    ]
################################################################################
def register_myaapp(handlers):
    application = tornado.web.Application(handlers)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

################################################################################
def webapp():
    print('**************')
    register_signal()
    # //register_app()
    register_myaapp(get_handlers())

################################################################################
if __name__ == '__main__':
    set_app_option()
    webapp()
