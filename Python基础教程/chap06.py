#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==============================================================================
#
# Author        : iaiting
#
# Contact       : iaiting@aliyun.com
#
# Generate Data : 2018-06-05
#
# Copyright     : 本文件隶属iaiting，欢迎转载无须知会
#
# Desciption    : Python基础教程（第2版）第6章 书本例题
#
# ==============================================================================


# 斐波那契序列
# ==============================================================================
def chap0601_01(num):
    fibs = [0, 1]
    for i in range(num - 2):
        fibs.append(fibs[-1] + fibs[-2])

    print(fibs)

# 定义函数
# ==============================================================================
def chap0601_02(name):    
    print('Hello ' + name)

# 函数返回斐波那契序列
# ==============================================================================
def chap0601_03(num):
    fibs = [0, 1]
    for i in range(num - 2):
        fibs.append(fibs[-1] + fibs[-2])

    return  fibs

# 文档字符串
# ==============================================================================
def chap0601_04(x):
    '''计算x的平方'''
    print(chap0601_04.__doc__)
    return  x*x
# ==============================================================================
def Chap06_Test():
    chap0601_01(10)
    chap0601_02('abc')
    result = chap0601_03(15)
    print("result = ", result)

    chap0601_04(6)

    
    
    # chap0501_02()
    # chap0504_01()
    #chap0505_01()
    # chap0505_02()


# ==============================================================================
if __name__ == '__main__':
    Chap06_Test()
