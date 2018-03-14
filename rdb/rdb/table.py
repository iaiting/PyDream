#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlalchemy.ext.declarative
from sqlalchemy import Column, Integer, String, DateTime
Base = sqlalchemy.ext.declarative.declarative_base()


class Table(object):

    def tableCreate(self, engine):
        Base.metadata.create_all(engine)

    def tableDrop(self, engine):
        Base.metadata.drop_all(engine)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    phone = Column(String)
    name = Column(String)
    password = Column(String)
    email = Column(String)


class Photo(Base):
    __tablename__ = 'photo'
    id = Column(Integer, primary_key=True)
    url = Column(String)


class Friend(Base):
    __tablename__ = 'friend'
    id = Column(Integer, primary_key=True)
    name = Column(String)
