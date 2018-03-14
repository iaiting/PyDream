#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tornado.web


class PhotoHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("PhotoHandler: GET Request")

    def post(self):
        self.write("PhotoHandler: POST Request")
