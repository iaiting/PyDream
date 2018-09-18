#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# Author        : iaiting
#
# Contact       : iaiting@aliyun.com
#
# Generate Data : 2018-06-05
#
# Copyright     : 本文件隶属iaiting，欢迎转载无须知会
#
# Desciption    : Python基础教程（第2版）
#                 - 第 9 章 魔法方法、属性和迭代器
#
################################################################################
def checkIndex(key):
    if not isinstance(key, int):
        raise TypeError


    if key < 0:
        raise IndexError

class ArithmeticSequence(object):
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        checkIndex(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        checkIndex(key)
        self.changed[key] = value

def chap0901_01():
    ars = ArithmeticSequence(1, 2)
    print(ars[4])
    ars[4] = 'a'
    print(ars[4])



################################################################################
def chap09_01():
    pass

################################################################################
def main_chap09():
    chap0901_01()
    chap09_01()

################################################################################
if __name__ == '__main__':
    main_chap09()