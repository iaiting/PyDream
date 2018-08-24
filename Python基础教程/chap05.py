#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#################################################################################
# Author        : iaiting
#
# Contact       : iaiting@aliyun.com
#
# Generate Data : 2018-04-04
#
# Copyright     : 本文件隶属iaiting，欢迎转载无须知会
#
# Desciption    : Python基础教程（第2版）
#                 - 第 4 章 条件、循环和其他语句
#
################################################################################

################################################################################
def chap0501_01():
    '''
    逗号隔开输出多个值
    '''
    print("chap0501_01 :")
    print(1,2,3)
    print("")


################################################################################
def chap0501_02():
    '''
    序列解包
    '''
    x, y, *z = 12, 34, 56, 78, 90, 12

    *xx, = (112, 234, 356, 478, 590, 612)

    print("chap0501_02 :")
    print("x = {0}, y = {1}, z = {2}".format(x, y, z))
    print("xx = {0}".format(xx))
    print("")

################################################################################
def chap0504_01():
    '''
    if-elif-else
    '''
    print("chap0504_01 :")
    num = 99
    if num > 0:
        print('The number is > 0')
    elif num < 0:
        print('The number is < 0')
    else:
        print('The number is = 0')

    print('')        

################################################################################
def chap0504_02():
    '''
    is 与 == 的区别
    '''
    x = y = [1, 2, 3]
    z = [1, 2, 3]
    print("chap0504_02 :")
    if x is y:
        print("x is y")

    if x is not z:
        print("x is not z")

    print('')
################################################################################
def chap0504_03():
    '''
    断言
    '''
    print("chap0504_03 :")
    age = 10
    assert 0 < age < 100

    age = -10
    # assert 0 < age < 100, '{0} 不在取值范围之内'.format(age)
    print("")

################################################################################
import math
def chap0505_01():
    '''
    beak 跳出循环
    找出100以内的最大平方数
    '''
    print("chap0505_01 :")
    for n in range(99, 0, -1):
        root = math.sqrt(n)
        if root == int(root):
            print(n)
            break

    print("")


################################################################################
def chap0505_02(start, end):
    '''
    for-else
    '''
    print("chap0505_02 :")
    for n in range(end, start, -1):
        root = math.sqrt(n)
        if root == int(root):
            print(n)
            break
    else:
        print("Did not find it from {0} - {1}".format(start,end))

    print("")

################################################################################
def main_chap05():
    chap0501_01()

    chap0501_02()

    chap0504_01()

    chap0504_02()

    chap0504_03()

    chap0505_01()

    chap0505_02(90,99)

    chap0505_02(90,100)

################################################################################
if __name__ == '__main__':
    main_chap05()
