#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ##############################################################################
#
# Author        : iaiting
#
# Contact       : iaiting@aliyun.com
#
# Generate Data : 2018-03-22
#
# Copyright     : 本文件隶属iaiting，欢迎转载无须知会
#
# Desciption    : Python基础教程（第2版）第二章书本例题
#
# ##############################################################################

def chap02_01(year=None, month_num=None, day_num=None):
    '''
    索引示例
    根据给定的年月日以数字形式打印日期
    '''
    # d_months = {
    #     '1': 'JAN',
    #     '2': 'FEB',
    #     '3': 'MAR',
    #     '4': 'APR',
    #     '5': 'MAY',
    #     '6': 'JUN',
    #     '7': 'JUL',
    #     '8': 'AUG',
    #     '9': 'SEP',
    #     '10': 'OCT',
    #     '11': 'NOV',
    #     '12': 'DEC'
    # }
    l_months = [None,
        'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT',
        'NOV', 'DEC'
    ]

    l_day_endings = [None] + ['st', 'nd', 'rd'] + 17 * ['th'] + [
        'st', 'nd', 'rd'
    ] + 7 * ['th'] + ['st']

    if (year is None or year == ''):
        year = input('Year : ')
    if (month_num is None or month_num == ''):
        month_num = input('Month (1-12): ')
    if (day_num is None or day_num == ''):
        day_num = input('Day (1-31) : ')

    month_name = l_months[int(month_num)]

    day_name = day_num + l_day_endings[int(day_num)]

    print("日期 = {0} {1} {2}\n".format(month_name, day_name, year))


################################################################################
def chap02_02(url=None):
    '''
    分片(切片)示例
    '''

    if url is None:
        url = input('Please Enter Your URL: ')

    domain = url[11:-4]

    print("域名 = {0}".format(domain))


################################################################################
def chap02_03():
    print('---------------')
    sentence = input('Sentence:')
    screen_width = 80
    text_width = len(sentence)
    box_width = text_width + 6
    left_margin = (screen_width - box_width) // 2
    print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')
    print(' ' * left_margin + '|' + ' ' * (box_width - 2) + '|')
    print(' ' * left_margin + '|' + ' ' * 2 + sentence + ' ' * 2 + '|')
    print(' ' * left_margin + '|' + ' ' * (box_width - 2) + '|')
    print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')


################################################################################
def chap02_04():
    database = [['albert', '1234'], ['dilbert', '2341'], ['smith', '8754'],
                ['dd', '333']]
    username = input('User Name: ')
    pin = input("PIN code: ")
    if [username, pin] in database:
        print('Access Granted')
    else:
        print('No Access')


################################################################################
def main_chap02():
    chap02_01(day_num='18', month_num='8', year='2018')

    chap02_02('http://www.python.org')


    # chap02_01()
    # chap02_02()
    # schap02_03()
    # chap02_04()


################################################################################
if __name__ == '__main__':
    main_chap02()
