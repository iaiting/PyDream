#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import tornado.web

class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is Firend Handler -> [GET METHOD]")

    def post(self):
        self.write("This is Firend Handler -> [POST METHOD]")