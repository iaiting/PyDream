import smtplib

class CSMTPBase(object):
    ''' class CSMTPBase
    ``smtplib``'s SMTP connection, and allows messages to be sent.'''

    def __init__(self, user, password, host, port=None, smtp_ssl=True,**kwargs):
        self.m_user=user
        self.m_useralias='jsxyja'
        self.m_host = host
        self.m_port = str(port) if port is not None else "465" if smtp_ssl else "587"
        self.m_credentials = password
        self.m_ssl = smtp_ssl
        self.m_kwargs = kwargs


    @property
    def connection(self):
        return smtplib.SMTP_SSL if self.m_ssl else smtplib.SMTP

    def send(self):
        self.login()

    def _login(self, password):
        self.m_smtp_connection = self.connection(self.m_host, self.m_port, **self.m_kwargs)
        self.m_smtp_connection.set_debuglevel(1)
        self.m_smtp_connection.login(self.m_user, password)
        pass



class CSMTP(CSMTPBase):
    def login(self):
        self._login(self.m_credentials)