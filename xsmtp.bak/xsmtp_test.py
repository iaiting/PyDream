#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

import xsmtp
import smtplib

################################################################################
def xsmtp_test():
    to = 'santa@someone.com'
    to2 = 'easterbunny@someone.com'
    to3 = 'sky@pip-package.com'
    subject = 'This is obviously the subject'
    body = 'This is obviously the body'
    html = '<a href="https://pypi.python.org/pypi/sky/">Click me!</a>'
    img = '/local/file/bunny.png'

    # xsmtp.register()
    # xs = xsmtp.CSMTP('jsxyja@aliyun.com', "jsxyja123",'smtp.aliyun.com')
    smtp_connection = xsmtp.CSMTP(user='jsxyja@aliyun.com', password='jsxyja123', host='smtp.aliyun.com')



    # xs.send(to = to, subject = subject, contents = body)
    smtp_connection.send()


################################################################################
if __name__ == '__main__':
    xsmtp_test()