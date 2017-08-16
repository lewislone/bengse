# coding: UTF-8
import sys
sys.path.insert(0,'../lib/webpy')
import web
import os
import DEBUG

from config import settings
import mail.send as send
import controllers.csv2sqlite as csv2sqlite

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
        self.form = web.form.Form(
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
        return self.render.new(self.form)

    def POST(self):
        if not self.form.validates():
            return self.render.new(self.form)
        #pass
        #model.new_post(form.d.title, form.d.content)
        print self.form.d.title
        print self.form.d.sender
        print self.form.d.receiver
        print self.form.d.content
        raise web.seeother('/newbatch')

class NewBatch:
    def __init__(self):
        self.render = settings.render
        self.form = web.form.Form(
		
                web.form.File('senderlist', web.form.notnull,
                                 size=30,
                                 description=u'发件人列表'),
                web.form.File('receiverlist', web.form.notnull,
                                 size=30,
                                 description=u'收件人列表'),
                web.form.Textbox('title', web.form.notnull,
                                 size=30,
                                 description=u'邮件标题'),
                web.form.Textarea('content', web.form.notnull,
                                  rows=30, cols=80,
                                  description=u'邮件内容'),
                web.form.Button(u'发送')
            )
    def GET(self):
        return self.render.newbatch(self.form)

    def POST(self):
        if not self.form.validates():
            return self.render.newbatch(self.form)
        x = web.input(senderlist={})
        #FIXME, save path, OK ?#
        filedir = '/tmp' # change this to the directory you want to store the file in.
        if 'senderlist' in x: # to check if the file-object is created
            filepath=x.senderlist.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
            #try:
            fout = open(filedir +'/'+ filename,'w') # creates the file where the uploaded file should be stored
            fout.write(x.senderlist.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.

        web.debug(x['senderlist'].filename)
        web.debug(x['senderlist'].value)
        x = web.input(receiverlist={})
        if 'receiverlist' in x: # to check if the file-object is created
            filepath=x.receiverlist.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
            #try:
            fout = open(filedir +'/'+ filename,'w') # creates the file where the uploaded file should be stored
            fout.write(x.receiverlist.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.

        print self.form.d.title
        print self.form.d.content
        web.debug(x['receiverlist'].filename)
        web.debug(x['receiverlist'].value)
        '''
        FIMXE, if upload ok, then /tmp/account.csv and /tmp/receiver.csv exits and not empty
        '''
        c2s = csv2sqlite.csv2sqlite('./tmp/account.csv')
        c2s.csv2db(2)
        c2s.close_db()
        c2s = csv2sqlite.csv2sqlite('./tmp/receiver.csv')
        c2s.csv2db(1)
        c2s.close_db()

        raise web.seeother('/')
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


