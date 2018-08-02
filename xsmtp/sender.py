#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################

import time

import smtplib

################################################################################

from xsmtp.headers import resolve_addresses

from xsmtp.message import prepare_message

from xsmtp.headers import make_addr_alias_user


################################################################################
class CSMTPBase(object):
    """ :class:`xsmtp.CSMTP` is a magic wrapper around
    ``smtplib``'s SMTP connection, and allows messages to be sent."""

    def __init__(
        self,
        user,
        password,
        host=None,
        port=None,
        smtp_ssl=False,
        smtp_set_debuglevel=1,
        encoding="utf-8",
        soft_email_validation=False,
    ):

        self.m_soft_email_validation = soft_email_validation

        self.m_user, self.m_useralias = make_addr_alias_user(user)

        self.m_is_closed = None

        self.m_host = host if host is not None else "smtp.{0}".format(self.m_user.split('@')[1])

        # gmail的端口为 "587" 而非 "25"
        self.m_port = str(port) if port is not None else "465" if smtp_ssl else "25"
        self.m_smtp_ssl = smtp_ssl
        self.m_debuglevel = smtp_set_debuglevel
        self.m_encoding = encoding

        self.m_credentials = password

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.m_is_closed:
            self.close()
        return False

    # @property
    def connection(self, host, port):
        return smtplib.SMTP_SSL(host, port) if self.m_smtp_ssl else smtplib.SMTP(host, port)

    def prepare_send(
            self,
            to=None,
            subject=None,
            contents=None,
            attachments=None,
            cc=None,
            bcc=None,
    ):

        addresses = resolve_addresses(self.m_user, self.m_useralias, to, cc,
                                      bcc)
        print('接收者邮件地址: {0}'.format(addresses))
        msg = prepare_message(
            self.m_user,
            self.m_useralias,
            addresses,
            subject,
            contents,
            attachments,
            self.m_encoding,
        )

        recipients = addresses["recipients"]
        msg_string = msg.as_string()
        print('待发送的邮件:\n{0}'.format(msg_string))
        return recipients, msg_string

    def send(
            self,
            to=None,
            subject=None,
            contents=None,
            attachments=None,
            cc=None,
            bcc=None,
            preview_only=False,
    ):

        self.login()

        recipients, msg_string = self.prepare_send(
            to, subject, contents, attachments, cc, bcc
        )

        if preview_only:
            return (recipients, msg_string)

        return self._attempt_send(recipients, msg_string)

    def _attempt_send(self, recipients, msg_string):
        try:
            result = self.smtp_connection.sendmail(self.m_user, recipients, msg_string)
            # print(result)
            print("Message sent to {0}, return code = {1}".format(recipients, result))
            return result
        except smtplib.SMTPServerDisconnected as e:
            print("发送失败:{0}".format(e))

        return False

    def close(self):
        self.m_is_closed = True
        try:
            self.smtp_connection.quit()
        except:
            pass

    def _login(self):
        self.smtp_connection = self.connection(self.m_host, self.m_port)

        self.smtp_connection.set_debuglevel(self.m_debuglevel)

        self.m_is_closed = False

        self.smtp_connection.login(self.m_user, self.m_credentials)
        print("Connected to SMTP @ {0}:{1} as {2}".format(self.m_host, self.m_port, self.m_user))

    def login(self):
        self._login()


    def _login_oauth2(self, oauth2_info):
        pass

class CSMTP(CSMTPBase):
    pass
