#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==============================================================================
#
# Author        : iaiting
#
# Contact       : iaiting@aliyun.com 88888888@qq.com 186-8888-8888
#
# Generate Data : 2018-03-22
#
# Copyright     : 本文件隶属iaiting，欢迎转载无须知会
#
# Desciption    : Python基础教程（第2版）
#                 第3章 使用字符串 书本例题
#
# ==============================================================================

# ------------------------------------------------------------------------------
def chap03_01():
    width = int(input("Please enter width: "))
    price_width = 10
    item_width = width - price_width

    head_format = '%-*s%*s'
    item_format = '%-*s%*.2f'

    print('=' * width)
    print(head_format % (item_width, 'Item', price_width, 'Price'))
    print('-' * width)

    print(item_format % (item_width, 'Apples', price_width, 0.4))
    print(item_format % (item_width, 'Apples', price_width, 0.5))
    print(item_format % (item_width, 'Apples', price_width, 1.92))
    print(item_format % (item_width, 'Apples', price_width, 8))
    print(item_format % (item_width, 'Apples', price_width, 12))


# ------------------------------------------------------------------------------
def chap03():
    chap03_01()

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    chap03()
