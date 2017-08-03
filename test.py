# coding: UTF-8
import os
import mail.send as send 
import utils.loadcvs as loadcvs


'''
account = [
            {'id':0,
            'account': 'a91014672@163.com',
            'passwd': 'aa77888',
            'smtp': 'smtp.163.com',
            'mini_interval': 20,
            'maxtimepeday': 40,
            'status': 1,                    #0:dead 1:live
            'ip_map': 110001010001000000...,#ip mapping 0:dead 1:live
            },
            {'id':1,
            'account': 'a91014672@163.com',
            'passwd': 'aa77888',
            'smtp': 'smtp.163.com',
            'mini_interval': 20,
            'maxtimepeday': 40,
            'status': 0,
            'ip_map': 011010100010000000...,
            },
        ]

consumer = [
            {'email': '3345214321.qq.com',
             'status': 0,                   #0:dead 1:live
             'account_map': 00000101001..., #account mapping 0:dead 1:live
            },
        ]
ip = [
        {
            'id':0,
            'addr':'192.168.1.1',
            'status':0,
        },
        {
            'id':1,
            'addr':'192.168.1.2',
            'status':1,
        },
    ]
'''

if __name__ == "__main__":
 
    #loadcvs.loadtojson(os.getcwd() + u"/邮箱.cvs")

    import lib.ownsmtplib as smtplib
    from email.header import Header
    from email.utils import parseaddr, formataddr
    from email.mime.text import MIMEText

    from_addr = 'a91014672@163.com'
    password = 'aa777888'
    smtp_server = 'smtp.163.com'
    m = send.mail(from_addr, password, smtp_server)

    ip = '192.168.1.8' 
    to = 'jdic@qq.com'
    text_type = 'html'
    content = '<html><body><h1>隆,您好，请给我回一封你最近做的程序代码， 谢谢~ </h1>' + '<br>---</br>'+ '<p>来自 <a href="http://www.raininsun.cn">rain</a>...</p>' + '</body></html>'.encode('gbk')
    msg = MIMEText(content, 'html', 'utf-8')
    name, addr = parseaddr('lei <%s>' % from_addr)
    msg['From'] = formataddr((Header(name, 'utf-8').encode(), addr))
    name, addr = parseaddr('lll <%s>' % to)
    msg['To'] = formataddr((Header(name, 'utf-8').encode(), addr))
    msg['Subject'] = Header('返回值', 'utf-8').encode()

    server = smtplib.SMTP(ip, smtp_server, 25)
    server.set_debuglevel(1)
    try:
        server.login(from_addr, password)
    except smtplib.SMTPException, e:
            print e
   # except  smtplib.SMTPAuthenticationError, e:
   #         print 'smtplib.SMTPAuthenticationError:', e
    try:
        server.sendmail(from_addr, [to], msg.as_string())
    except smtplib.SMTPException, e:
            print e
   # except  smtplib.SMTPAuthenticationError, e:
   #         print 'smtplib.SMTPAuthenticationError:', e
   # except smtplib.SMTPHeloError:
   #         print 'smtplib.SMTPHeloError'
   # except smtplib.SMTPRecipientsRefused:
   #         print 'smtplib.SMTPRecipientsRefused'
   # except smtplib.SMTPSenderRefused, e:
   #         print 'smtplib.SMTPSenderRefused', e
   # except smtplib.SMTPDataError:
   #         print 'smtplib.SMTPDataError'
   # except smtplib.SMTPServerDisconnected:
   #         print 'smtplib.SMTPServerDisconnected'
   # except smtplib.SMTPResponseException:
   #         print 'smtplib.SMTPResponseException'
   # except smtplib.SMTPConnectError:
   #         print 'smtplib.SMTPConnectError'
    server.quit()
