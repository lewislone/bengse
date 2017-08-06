# coding: UTF-8
import web
import os
import DEBUG

from config import settings
import mail.send as send

class Test:
    def __init__(self):
        self.render = settings.render

    def GET(self):
        return self.render.test()

    def POST(self):
        data = web.input(path={})
        if data.type:
            DEBUG.p('get limit: %s' % (data.type))
        if data.sento:
            DEBUG.p('sent email to : %s' % (data.sento))
        if data.content:
            DEBUG.p('content: %s' % (data.content))
        if data.bindip:
            DEBUG.p('bind ip %s' % (data.bindip))

        from_addr = 'jdicisyesterday@163.com'
        password = 'lone366200'
        smtp_server = 'smtp.163.com'
        m = send.mail(from_addr, password, smtp_server)

        ip = data.bindip
        to = data.sento
        text_type = data.type
        content = data.content
        #content = '<html><body><h1>Hi lll, sorry, this attachment is ok, 3Q for you help, and your ice </h1>' + '<br>---</br>'+ '<p>send by <a href="http://www.python.org">fri</a>...</p>' + '</body></html>'
        m.send_text(ip, to, content, text_type)
        return self.render.test()
