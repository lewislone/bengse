#coding: UTF-8
import os
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_plain():
        from_addr = "jdicisyesterday@163.com"
        password = "xxx"
        to_addr = "jdic@qq.com"
        smtp_server = "smtp.163.com"

        msg = MIMEText('hello, this after is hot, can you give me some ice', 'plain', 'utf-8')
        msg['From'] = _format_addr('fri <%s>' % from_addr)
        msg['To'] = _format_addr('lll <%s>' % to_addr)
        msg['Subject'] = Header('接冰……', 'utf-8').encode()

        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()

def send_both():
        from_addr = "jdicisyesterday@163.com"
        password = "xxx"
        to_addr = "jdic@qq.com"
        smtp_server = "smtp.163.com"


        msg = MIMEMultipart('alternative')
        msg['From'] = _format_addr('fri <%s>' % from_addr)
        msg['To'] = _format_addr('lll <%s>' % to_addr)
        msg['Subject'] = Header('谢谢……', 'utf-8').encode()

        msg.attach(MIMEText('Hi lll, sorry, this photo is ok, and your ice ', 'plain', 'utf-8'))
        msg.attach(MIMEText('<html><body><h1>Hi lll, sorry, this attachment is ok, 3Q for you help, and your ice </h1>' + '<br>---</br>'+ '<p>send by <a href="http://www.python.org">fri</a>...</p>' + '</body></html>', 'html', 'utf-8'))

        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()

def send_html_with_attachment():
        from_addr = "jdicisyesterday@163.com"
        password = "xxx"
        to_addr = "jdic@qq.com"
        smtp_server = "smtp.163.com"

        msg = MIMEMultipart()
        msg['From'] = _format_addr('fri <%s>' % from_addr)
        msg['To'] = _format_addr('lll <%s>' % to_addr)
        msg['Subject'] = Header('接冰……', 'utf-8').encode()

        f = open('/Users/apple/Desktop/IMG_1452.jpg', 'rb')
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

        msg.attach(MIMEText('<html><body><h1>Hi lll, attachement is a photo for you help, by the way ice is perfect </h1>' + '<p><img src="cid:0"></p>' + '<br>---</br>'+ '<p>send by <a href="http://www.python.org">fri</a>...</p>' + '</body></html>', 'html', 'utf-8'))

        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()


if __name__ == '__main__':

    #send_plain()
    #send_html()
    send_both()
    #send_html_with_attachment()
