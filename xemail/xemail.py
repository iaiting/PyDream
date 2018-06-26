#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
# 发送邮件 相关库
################################################################################
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import smtplib
import email.mime.multipart

################################################################################
# 接收邮件 相关库
################################################################################
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib
import base64

#.decodebytes(s.encode(encoding=charset)), encoding=charset)


################################################################################

# 阿里云个人邮箱服务器
################################################################################
smtp_host =  'smtp.aliyun.com'

sender = 'unifortran@aliyun.com'

mailpass = 'g00gle2o1o'



################################################################################
class CMail(object):
    def __init__(self):
        pass

    def auth(self, debug=0):
        from smtplib import SMTP_SSL
        smtp = SMTP_SSL()
        try:
            smtp.set_debuglevel(debug)
            smtp.connect(self.smtp_server, self.smtp_port)

        except ssl.SSLError:
            from smtplib import SMTP
            smtp = SMTP()
            smtp.set_debuglevel(debug)
            smtp.connect(self.smtp_server, self.smtp_port)

        smtp.login(self.smtp_auth_user, self.smtp_auth_password)

        return smtp


    def send(self):
        pass


################################################################################
def f_send_mail():
    msg = email.mime.multipart.MIMEMultipart()
    msgFrom = sender
    msgTo = '790720555@qq.com'
    smtpSever = smtp_host

    msg['from'] = sender
    msg['to'] = msgTo
    msg['subject'] = '我爱中华666'
    content = '''
    你好:
        我爱中华666
    '''

    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)

    smtp = smtplib.SMTP()

#    smtp.set_debuglevel(1)

    smtp.connect(smtp_host)
    smtp.login(msgFrom, mailpass)

    smtp.sendmail(msg['from'], msg['to'], msg.as_string())

    print(msg)
    print('************************************************t101:\n')
    print(msg.as_string())
    smtp.quit()



# 邮件的Subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须decode
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
        return value

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()

    return charset


def print_info(msg, indent=0):
    if indent ==0:
        for header in ["From", "To", "Subject"]:
            value = msg.get(header, "")
            if value:
                if header == "Subject":
                    vaule = decode_str(value)
                else:
                    hdr, addr =parseaddr(value)
                    name = decode_str(hdr)
                    value = u"%s <%s>" % (name, addr)
            print("%s%s:%s" % ("  " * indent, header, value))
        if (msg .is_multipart()):
            parts = msg.get_payload()
            for n, part in enumerate(parts):
                print('%spart %s' % ('  ' * indent, n))
                print('%s--------------------' % ('  ' * indent))
                print_info(part, indent + 1)
        else:
            content_type = msg.get_content_type()

            print('**************t101:',content_type)

            if content_type=='text/plain' or content_type=='text/html':
                content = msg.get_payload(decode=True)
                charset = guess_charset(msg)
                if charset:
                    content = content.decode(charset)
                print('%sText: %s' % ('  ' * indent, content + '...'))
            else:
                print('%sAttachment: %s' % ('  ' * indent, content_type))


def decode_base64(s, charset='utf8'):
    return str(base64.decodebytes(s.encode(encoding=charset)), encoding=charset)

################################################################################
def f_receive_mail():

    print(decode_base64('ufnosQ==','gb18030'))

    #smtp_host =  'smtp.aliyun.com'
    pop3_host =  'pop3.aliyun.com'
    #sender = 'unifortran@aliyun.com'

    #mailpass = 'g00gle2o1o'

    #server = poplib.POP3_SSL(pop3_host)
    server = poplib.POP3(pop3_host)

    #print(server.getwelcome().decode("utf-8"))

#    server.set_debuglevel(1)
    server.user(sender)
    server.pass_(mailpass)

    #ret = server.stat()
    #print(ret)
    print("信息数量：%s 占用空间 %s" % server.stat())
    #print("邮件数量: {0}, 占用空间: {0}".format(server.stat()))

    resp, mails, octets = server.list()
    print("list:",server.list())

    print(server.list())
    print(mails)

    index = len(mails)
    resp, lines, ocetes = server.retr(index)

    msg_content = b"\r\n".join(lines).decode("utf-8")
    msg = Parser().parsestr(msg_content)
    #print_info(msg)
    #print(msg)

    text = """
    From: Santa Claus <santa@aintreal.no>
    To: Some Dude <some@du.de>
    key: value
    Subject: I have lost your presents.
    Dude, i am so sorry.
"""
    parser = Parser().parsestr(text)
    print(parser.keys())
    print(parser)

    #messages = [server.retr(i) for i in range(1, 2) ]
    #print (messages)

    server.close()

def main():
    #f_send_mail()
    f_receive_mail()

################################################################################
if __name__ == "__main__":
    main()
