#!/usr/bin/evn python3
# -*- coding: utf-8 -*-
import tornado.web

import textwrap

#########################################################################################
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')

#########################################################################################
class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1])

#########################################################################################
class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        print("****************")
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, width))



