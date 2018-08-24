#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

################################################################################
def jsonEncode(d):
    return json.dumps(d)


def jsonFileEncode(f):
    return json.dumps(f)

################################################################################
def jsonDecode(s):
    return json.loads(s)

################################################################################
class CXJson(object):
    pass


################################################################################
def xjson_test():
    d = {'name': "abb", "age":16}
    ret = jsonEncode(d)
    print(ret,len(ret),type(ret))

    ret = jsonDecode(ret)
    print(ret,len(ret),type(ret))

################################################################################
if __name__ == "__main__":
    xjson_test()
