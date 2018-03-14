#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import handler.user
import handler.photo
import tornado.web


class Application(tornado.web.Application):

    def __init__(self, rdbpool, handlers):
        super(Application, self).__init__(handlers)
        self.rdbpool = rdbpool


def get_handlers():
    handlers = [
        (r"/v1/user", handler.user.UserHandler),
        (r"/v1/photo", handler.photo.PhotoHandler),
    ]
    return handlers
