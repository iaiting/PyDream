#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import rdb.table as table
import tornado.gen
import asyncio


def user_create(rdbsession, json_user):
    session = rdbsession()
    result = {'code': '0', 'msg': '', 'data': []}
    try:
        dict_user = json.loads(json_user)
        user = table.User(**dict_user)
        session.add(user)
        session.commit()
    except Exception as e:
        result['msg'], result['code'] = e, '-1'
    finally:
        session.close()

    return json.dumps(result)


def user_retrieve(rdbsession, json_user):
    session = rdbsession()
    result = {'code': '0', 'msg': '', 'data': []}
    try:
        dict_user = json.loads(json_user)
        phone = dict_user['phone']
        users = session.query(table.User).filter(table.User.phone == phone).all()
        for user in users:
            dict_user = user.__dict__
            del dict_user['_sa_instance_state']
            result['data'].append(dict_user)

    except Exception as e:
        result['msg'], result['code'] = e, '-1'
    finally:
        session.close()
    return json.dumps(result)
