#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import configobj
import os


class readConfig():

    def __init__(self, filename):
        # [bug] 文件不存时没有报错，直接返回空字典,做个文件是否存在的判断
        if not os.path.exists(filename):
            raise Exception('%s is not found' % filename)
        self.config = configobj.ConfigObj(filename, encoding='UTF8')

    def get_skv(self, section, key):
        return self.config[section][key]


def test():
    print('This is [%s] file testing ...' % __file__)
    rc = readConfig('../config.ini')
    host = rc.get_skv('SELF', 'host')
    print(host)

if __name__ == '__main__':
    test()
