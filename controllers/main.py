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
class New:
	def __init__(self):
		self.render = settings.render
	form = web.form.Form(
		web.form.Textbox('sender', web.form.notnull,
                         size=30,
                         description=u'发件人'),
		web.form.Textbox('receiver', web.form.notnull,
                         size=30,
                         description=u'收件人'),
        web.form.Textbox('title', web.form.notnull,
                         size=30,
                         description=u'邮件标题'),
        web.form.Textarea('content', web.form.notnull,
                          rows=30, cols=80,
                          description=u'邮件内容'),
        web.form.Button(u'发送')
    )
	def GET(self):
		form = self.form()
		return self.render.new(form)
	def POST(self):
		form = self.form()
		if not form.validates():
			return self.render.new(form)
		#pass
        #model.new_post(form.d.title, form.d.content)
		print form.d.title
		#print form.d.sender
		#print form.d.receiver
		#print form.d.content
		raise web.seeother('/upload')

class Imgs:
    def GET(self, name):
        ext = name.split(".")[-1]
        cType = {
            "png": "images/png",
            "jpg": "images/jpeg",
            "gif": "images/gif",
            "ico": "images/x-icon"
        }
        if name in os.listdir('imgs'):
            web.header("Content-Type", cType[ext])
            return open('imgs/%s' % name, "rb").read()
        else:
            raise web.notfound()


