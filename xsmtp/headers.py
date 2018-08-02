#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from xsmtp.compat import text_type
from xsmtp.error import XsmtpAddressError


from email.header import Header
import time
# {'recipients': ['abb@163.com'], 'To': 'abb@163.com'}
def resolve_addresses(user, useralias, to, cc=None, bcc=None):
    addresses = {"recipients": []}

    if to is not None:
        make_addr_alias_target(to, addresses, "To")

    if cc is not None:
        make_addr_alias_target(cc, addresses, "Cc")

    if bcc is not None:
        make_addr_alias_target(bcc, addresses, "Bcc")


    return addresses

# 支持两种数据格式传递参数
# {'abb@163.com', '北乔峰'}
# 'abb@163.com'
def make_addr_alias_user(email_addr):
    if isinstance(email_addr, text_type):
        if "@" in email_addr:
            return (email_addr, email_addr.split('@')[0])

    if isinstance(email_addr, dict):
        if len(email_addr) == 1:
            return (list(email_addr.keys())[0], list(email_addr.values())[0])

    raise XsmtpAddressError

def make_addr_alias_target(x, addresses, which):
    if isinstance(x, text_type):
        addresses["recipients"].append(x)
        addresses[which] = x



def add_date(msg):
    mailDate = Header(time.ctime())
    msg["Date"] = mailDate



def add_subject(msg, subject):
    if not subject:
        return
    if isinstance(subject, list):
        subject = " ".join(subject)

    mailSubject = Header(subject, 'utf-8')

    msg["Subject"] = mailSubject


def add_recipients_headers(user, useralias, msg, addresses):
    msg["From"] = '"{0}" <{1}>'.format(useralias.replace("\\", "\\\\").replace('"', '\\"'), user)

    if "To" in addresses:
        msg["To"] = addresses["To"]
    else:
        msg["To"] = useralias

    if "Cc" in addresses:
        msg["Cc"] = addresses["Cc"]