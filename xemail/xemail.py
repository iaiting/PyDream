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

################################################################################
def f_receive_mail():

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

    print(server.list())

    messages = [server.retr(i) for i in range(1, 2) ]

    #print (messages)

def main():
    #f_send_mail()
    f_receive_mail()

################################################################################
if __name__ == "__main__":
    main()
