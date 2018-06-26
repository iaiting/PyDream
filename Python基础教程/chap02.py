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
# Desciption    : Python基础教程（第2版）第二章书本例题
#
# ==============================================================================

def chap02_01():
    months = [
        'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
        'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'
    ]

    endings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] \
            + 7 * ['th'] + ['st']

    year = input('Year: ')
    month = input('Month (1-12): ')
    day = input('Day (1-31): ')

    month_num = int(month)
    day_num = int(day)

    month_name = months[month_num - 1]
    day_name = day + endings[day_num - 1]

    print(month_name + '.' + day_name + '.' + year)

def chap02_02():
    url = input('Please Enter the URL: ')
    domain = url[11:-4]
    print(domain)

def chap02_03():
    print('---------------')
    sentence = input('Sentence:')
    screen_width = 80
    text_width = len(sentence)
    box_width = text_width + 6
    left_margin = (screen_width-box_width)//2
    print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')
    print(' ' * left_margin + '|' + ' ' * (box_width-2) + '|')
    print(' ' * left_margin + '|' + ' ' * 2 + sentence + ' ' * 2 + '|')
    print(' ' * left_margin + '|' + ' ' * (box_width-2) + '|')
    print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')

def chap02_04():
    database = [['albert', '1234'], ['dilbert', '2341'], ['smith', '8754'],
                ['dd', '333']]
    username = input('User Name: ')
    pin = input("PIN code: ")
    if [username, pin] in database:
        print('Access Granted')
    else:
        print('No Access')


def chap02():
    # chap02_01()
    # chap02_02()
    # schap02_03()
    chap02_04()
chap



if __name__ == '__main__':
    chap02()
