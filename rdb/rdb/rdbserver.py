#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import mprpc
import rdb.table
import rdb.user


class RdbServer(mprpc.RPCServer):

    def __init__(self, rdb):
        super(RdbServer, self).__init__()
        self.engine = create_engine(rdb)  # , echo=True)
        self.rdbsession = sessionmaker(bind=self.engine)

    def tableCreate(self):
        rdb.table.Table.tableCreate(self, self.engine)

    def tableDrop(self):
        rdb.table.Table.tableDrop(self, self.engine)

    def userCreate(self, json_user):
        return rdb.user.user_create(self.rdbsession, json_user)

    def userRetrieve(self, json_user):
        return rdb.user.user_retrieve(self.rdbsession, json_user)
