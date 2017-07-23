#coding: UTF-8
import os
import sys
import lib.ownsmtplib as smtplib
import lib.bindip as bindip
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import utils.test as test


class mail()
    def __init__(self, addr, pw, smpt):
        self.from_addr = "jdicisyesterday@163.com"
        self.password = "xxx"
        self.smtp_server = "smtp.163.com"


    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def send_plain(self, ip, to, content):
        msg = MIMEText(content)
        msg['From'] = self._format_addr('fri <%s>' % self.from_addr)
        msg['To'] = self._format_addr('lll <%s>' % to)
        msg['Subject'] = Header('接冰……', 'utf-8').encode()

        server = smtplib.SMTP(ip, self.smtp_server, 25)
        server.set_debuglevel(1)
        server.login(self.from_addr, password)
        server.sendmail(self.from_addr, [to], msg.as_string())
        server.quit()

    def send_both(self, ip, to, content):

        msg = MIMEMultipart('alternative')
        msg['From'] = self._format_addr('fri <%s>' % self.from_addr)
        msg['To'] = self._format_addr('lll <%s>' % to)
        msg['Subject'] = Header('谢谢……', 'utf-8').encode()

        msg.attach(MIMEText(content))
        #msg.attach(MIMEText('Hi lll, sorry, this photo is ok, and your ice ', 'plain', 'utf-8'))
        #msg.attach(MIMEText('<html><body><h1>Hi lll, sorry, this attachment is ok, 3Q for you help, and your ice </h1>' + '<br>---</br>'+ '<p>send by <a href="http://www.python.org">fri</a>...</p>' + '</body></html>', 'html', 'utf-8'))

        server = smtplib.SMTP(ip, self.smtp_server, 25)
        server.set_debuglevel(1)
        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, [to], msg.as_string())
        server.quit()

    def send_html_with_attachment(self, ip, to, content, attachment_path):
        msg = MIMEMultipart()
        msg['From'] = self._format_addr('fri <%s>' % self.from_addr)
        msg['To'] = self._format_addr('lll <%s>' % to)
        msg['Subject'] = Header('接冰……', 'utf-8').encode()

        f = open(attachment_path, 'rb')
        # set attachment type and name:
        mime = MIMEBase('image', 'jpg', filename='IMG_1452.jpg')
        # add header:
        mime.add_header('Content-Disposition', 'attachment', filename='IMG_1452.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # read attachement:
        mime.set_payload(f.read())
        #encode with Base64:
        encoders.encode_base64(mime)
        # add mine to multipart:
        msg.attach(mime)

        msg.attach(MIMEText(content))

        server = smtplib.SMTP(self.smtp_server, 25)
        server.set_debuglevel(1)
        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, [to], msg.as_string())
        server.quit()


if __name__ == '__main__':

    print "start ##############################################"
    bindipobj = bindip.bindIp()
    bindipobj.randomIp()
    #socket.socket = bindipobj.changeIp(bindipobj.getIp()) 
    print "end ##################################"
    print bindipobj.getIp()
    print bindipobj.ip
    #send_html()
    #send_plain()
    #send_both(bindipobj.ip)
    #send_html_with_attachment()
    test.func_test(22)
