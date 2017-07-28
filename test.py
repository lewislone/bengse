# coding: UTF-8
import os
import mail.send as send 
import utils.loadcvs as loadcvs

if __name__ == "__main__":
 
    loadcvs.loadtojson(os.getcwd() + u"/邮箱.cvs")
'''
    from_addr = 'jdicisyesterday@163.com'
    password = 'lone366200'
    smtp_server = 'smtp.163.com'
    m = send.mail(from_addr, password, smtp_server)

    ip = '192.168.1.8' 
    to = 'jdic@qq.com'
    text_type = 'html'
    content = '<html><body><h1>Hi lll, sorry, this attachment is ok, 3Q for you help, and your ice </h1>' + '<br>---</br>'+ '<p>send by <a href="http://www.python.org">fri</a>...</p>' + '</body></html>'
    m.send_text(ip, to, content, text_type)
'''
