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

import email
#.decodebytes(s.encode(encoding=charset)), encoding=charset)

################################################################################

# 阿里云个人邮箱服务器
################################################################################
#sender = 'unifortran@aliyun.com'

#mailpass = 'g00gle2o1o'


UserInfo={
    'email' : 'unifortran@aliyun.com',
    'emailpassword' : 'g00gle2o1o'
}

################################################################################
def get_smtphost(email):

    try:

        smtp_host='smtp.'+email.split('@')[-1]

        return smtp_host

    except:

        return ''


################################################################################
def get_pop3host(email):

    try:
        pop3_host = 'pop3.%s' % (email.split('@')[-1])

        return pop3_host

    except:

        return ''


################################################################################
class CEmail(object):

    def __init__(self, str_email, str_password):

        self.m_email = str_email

        self.m_password = str_password

        self.m_smtphost = get_smtphost(str_email)

        self.m_pop3host = get_pop3host(str_email)

        self.m_smtp = smtplib.SMTP()

        self.m_sslsmtp = smtplib.SMTP_SSL()

        self.m_pop3 = poplib.POP3(self.m_pop3host)

        

    def PrintEmailDetailInfo(self):

        print('email address = ', self.m_email)

        print('email password = ', self.m_password)

        print('email smtphost = ', self.m_smtphost)


    def auth(self, debug = 0):
        # smtp auth
        self.m_smtp.set_debuglevel(debug)

        self.m_smtp.connect(self.m_smtphost)

        self.m_smtp.login(self.m_email, self.m_password)

        # pop3 auth
        self.m_pop3.set_debuglevel(debug)

        self.m_pop3.user(self.m_email)

        self.m_pop3.pass_(self.m_password)


    def send(self, to_email, subject, content):

        msg = email.mime.multipart.MIMEMultipart()

        msg['from'] = self.m_email

        msg['to'] = to_email

        msg['subject'] = subject

        msg.attach(email.mime.text.MIMEText(content))

        self.m_smtp.sendmail(msg['from'], msg['to'], msg.as_string())


        print(msg)
        print('************************************************t101:\n')
        #self.m_smtp.quit()



    def recevive(self):
        resp, mails,octets = self.m_pop3.list()

        mail_nums = len(mails)

        response_status, mail_message_lines, octets = self.m_pop3.retr(mail_nums)


        print("====================== 第",mail_nums)

        msg_content = b'\r\n'.join(mail_message_lines).decode('gbk')
        # 邮件原始数据没法正常浏览，因此需要相应的进行解码操作
        msg = Parser().parsestr(text=msg_content)




        subject = msg.get('subject')

        print('Subject: ', subject)
        h = email.header.Header(subject)

        
        print('h = ', h)

        dh = email.header.decode_header(h)
        print('dh = ', dh)



        subject =dh[0][0].decode(dh[0][1]).encode('utf8')
        

        #subject = unicode(dh[0][0], dh[0][1]).encode('utf8')

        #subject = h.encode('utf8')


        print('Subject: ', subject)
#        print('Subject: ', s)
        

        

        


        #print('解码后的邮件信息:\n{}'.format(msg))
        #print_info(msg)


################################################################################
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

    #server = poplib.POP3_SSL(pop3_host)
    #print(server.getwelcome().decode("utf-8"))

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



################################################################################
def TEST_get_smtphost():
    print('\n==== Enter get_smtphost test:')

    email_address = 'abb@aliyun.com'
    smtphost = get_smtphost(email_address)

    print("email address = ", email_address)
    print("smtp host = ", smtphost)


def TEST_get_pop3host(email):
    print('\n==== Enter get_pop3host test:')

    email_address = 'abb@aliyun.com'
    pop3host = get_pop3host(email_address)

    print("email address = ", email_address)
    print("pop3host host = ", pop3host)


def TEST_CEmail():
    print('\n==== Enter CEmail test:')
    myemail = CEmail('unifortran@aliyun.com', 'g00gle2o1o')

    myemail.PrintEmailDetailInfo()

    myemail.auth(1)

    #myemail.send('790720555@qq.com', '我爱中华1111112', '11111112')

    #myemail.send('790720555@qq.com', '我爱中华2222221', '22222221')

    myemail.recevive()






def main():
    TEST_get_pop3host(email)

    TEST_get_smtphost()

    TEST_CEmail()
    return 
    #print('============= main:\n')
    #f_send_mail()
    #f_receive_mail()

################################################################################
if __name__ == "__main__":
    main()
