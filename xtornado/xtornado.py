#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tornado.web
import signal


class CurdHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is CurdHandler's GetHandler")

    def post(self):
        self.write("This is CurdHandler's PostHandler")

    def put(self):
        self.write("This is CurdHandler's PutHandler")

    def delete(self):
        self.write("This is CurdHandler's DeleteHandler")


def xtornado():

    signal.signal(signal.SIGINT, signal.SIG_DFL)

    print("This is tornado application...")
    application = tornado.web.Application([
        (r"/curd", CurdHandler),
        ])
    application.listen(8888)

    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    xtornado()