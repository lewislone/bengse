#coding: UTF-8
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


class Mail():
    def __init__(self, addr, pw, smpt, ip):
        self.from_addr = addr
        self.password = pw
        self.server = smtplib.SMTP(ip, smpt, 25)
        self.server.set_debuglevel(1)


    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def loginsmtp(self):
        try:
            self.server.login(self.from_addr, self.password)
        except smtplib.SMTPException, e:
            print e
            return e[0]
        return 0

    def send_text(self, to, to_name, from_name, content, content_type, subject):#content_type: 'html', 'plain'
        #msg.attach(MIMEText('<html><body><h1>Hi lll, sorry, this attachment is ok, 3Q for you help, and your ice </h1>' + '<br>---</br>'+ '<p>send by <a href="http://www.python.org">fri</a>...</p>' + '</body></html>', 'html', 'utf-8'))
        msg = MIMEText(content, content_type, 'utf-8')
        msg['From'] = self._format_addr('%s <%s>' % (from_name, self.from_addr))
        msg['To'] = self._format_addr('%s <%s>' % (to_name, to))
        msg['Subject'] = Header(subject, 'utf-8').encode()

        self.server.sendmail(self.from_addr, [to], msg.as_string())
        self.server.quit()

    def send_both(self, to, content):

        msg = MIMEMultipart('alternative')
        msg['From'] = self._format_addr('fri <%s>' % self.from_addr)
        msg['To'] = self._format_addr('lll <%s>' % to)
        msg['Subject'] = Header('谢谢……', 'utf-8').encode()

        msg.attach(MIMEText(content, 'plain', 'utf-8'))
        msg.attach(MIMEText(content, 'html', 'utf-8'))
        #msg.attach(MIMEText('Hi lll, sorry, this photo is ok, and your ice ', 'plain', 'utf-8'))
        #msg.attach(MIMEText('<html><body><h1>Hi lll, sorry, this attachment is ok, 3Q for you help, and your ice </h1>' + '<br>---</br>'+ '<p>send by <a href="http://www.python.org">fri</a>...</p>' + '</body></html>', 'html', 'utf-8'))

        try:
            self.server.sendmail(self.from_addr, [to], msg.as_string())
        except smtplib.SMTPException, e:
            print e
            return e[0]
        return 0

    def send_html_with_attachment(self, to, content, attachment_path):
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

        #msg.attach(MIMEText('<html><body><h1>Hi this my photo: </h1>' + '<p><img src="cid:0"></p>' + '</body></html>', 'html', 'utf-8'))
        msg.attach(MIMEText(content, 'html', 'utf-8'))

        try:
            self.server.sendmail(self.from_addr, [to], msg.as_string())
        except smtplib.SMTPException, e:
            print e
            return e[0]
        return 0

    def quit(self):
        self.server.quit()

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
