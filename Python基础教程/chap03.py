#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
#
# Author        : iaiting
#
# Contact       : iaiting@aliyun.com
#
# Generate Data : 2018-03-22
#
# Copyright     : 本文件隶属于iaiting，欢迎转载无须知会
#
# Desciption    : Python基础教程（第2版）
#                 - 第 3 章 使用字符串
#
################################################################################
def chap03_01(width=None):
    '''
    字符串格式化示例
    使用给定的宽度打印格式化后的价格列表
    '''
    if width is None:
        width = int(input("Please enter width: "))

    price_width = 10
    item_width = width - price_width

    head_format = '%-*s%*s'
    item_format = '%-*s%*.2f'

    print("chap03_01 :") 
    print('=' * width)
    print(head_format % (item_width, 'Item', price_width, 'Price'))
    print('-' * width)

    print(item_format % (item_width, 'Apples', price_width, 0.4))
    print(item_format % (item_width, 'Pears', price_width, 0.5))
    print(item_format % (item_width, 'Cantaloupes', price_width, 1.92))
    print(item_format % (item_width, 'Dried Apricots', price_width, 8))
    print(item_format % (item_width, 'Prunes', price_width, 12))
    print("")

################################################################################
def chap03_02():
    '''
    translate 字符替换，补充lower()等只是针对英文字符函数的不足
    '''

    translate_table = str.maketrans('cs', 'kz')
    s = "this is string example....wow!!!"

    print("chap03_02 :") 
    print ("替换字符表: {0}".format(translate_table))
    print ("替换前字符串: {0}".format(s))
    print ("替换后字符串: {0}".format(s.translate(translate_table)))

################################################################################
def main_chap03():
    chap03_01(80)
    chap03_02()


################################################################################
if __name__ == '__main__':
    main_chap03()
