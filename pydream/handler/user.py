#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tornado.web
import tornado.gen
import gsocketpool.pool
from tornado.concurrent import Future


class UserHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self):
        result = yield self.async_get()
        self.finish(result)

    def async_get(self):
        future = Future()
        json_user = '{"phone": "18655590094"}'
        with self.application.rdbpool.connection() as client:
            result = client.call('userRetrieve', json_user)
        future.set_result(result)
        return future

    def post(self):
        resp_data = {"msg": "", "status_code": "200", "data": ""}
        self.write(resp_data)
