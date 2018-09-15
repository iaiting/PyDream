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
#                 - 第 7 章 更加抽象
#
################################################################################

################################################################################
def chap0701_01(num):
    """
    多态和方法
    """
    print("chap0701_01 :")
    arg = 'abc'
    num = arg.count('a')
    print("{0} has 'a' num is {1}".format(repr(arg), num))

    arg = ['1', 2, 'a', 'a']
    num = arg.count('a')
    print("{0} has 'a' num is {1}".format(repr(arg), num))

    print("")

################################################################################
def chap0701_02(arg1, arg2):
    print("chap0701_02 :")
    ret = arg1 + arg2
    print("{0} + {1} = {2}".format(arg1,arg2, ret))
    print('')


__metaclass__ = type
class Person:
    def setName(self, name):
        self.name = name
        pass

    def getName(self):
        return self.name

    def greet(self):
        print("Hello, World! I'm {}".format(self.name))

################################################################################
def chap0701_03():
    print("chap0701_03 :")
    p1 = Person()
    p1.setName("abc")
    p1.greet()

    Person.setName(p1, "cba")
    Person.greet(p1)



################################################################################
def main_chap07():
    chap0701_01(10)

    chap0701_02(1, 2)
    chap0701_02('a', '2')

    chap0701_03()


################################################################################
if __name__ == '__main__':
    main_chap07()
