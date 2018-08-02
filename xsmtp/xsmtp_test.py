#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.path.append('..')

import xsmtp

from xsmtp.headers import resolve_addresses
from xsmtp.headers import make_addr_alias_user

#  addresses = resolve_addresses(self.user, self.useralias, to, cc, bcc)
################################################################################
def resolve_addresses_test():
    # addresses = resolve_addresses('abb@126.com', 'abb', 'bcc@126.com', 'cdd@126.com', 'dee@26.com')
    addresses = resolve_addresses('abb@126.com', 'abb', None, 'cdd@126.com', 'dee@26.com')
    print(addresses)


def make_addr_alias_user_test():
    u1, a1 = make_addr_alias_user('abb@263.com')
    u2, a2 = make_addr_alias_user({'abb@263.com':"带头大哥"})
    print("u1 = {0}, a1 = {1}".format(u1,a1))
    print("u2 = {0}, a2 = {1}".format(u2,a2))
    u2, a2 = make_addr_alias_user('abb')


################################################################################
def xsmtp_test():
    to = '790720555@qq.com'

    subject = 'abc123'

    body = '123abc'

    html = '<a href="https://pypi.python.org/pypi/sky/">Click me!</a>'

    img = '/local/file/bunny.png'

    attachments = ['C:\\tmp\\test.log']

    xs = xsmtp.CSMTP('jsxyja@aliyun.com', 'jsxyja123', 'smtp.aliyun.com')
    xs.send(attachments = None, to=to, subject=subject, contents=body)



################################################################################
if __name__ == '__main__':
    # make_addr_alias_user_test()
    # resolve_addresses_test()

    xsmtp_test()