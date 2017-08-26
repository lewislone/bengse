# coding: UTF-8
import sys
sys.path.insert(0,'../lib/webpy')
import web
import os
import dao
import time
import shutil
import DEBUG
from config import settings
import mail.send as send
import mail.template as template 
import controllers.csv2sqlite as csv2sqlite

class Show:
    def __init__(self):
        self.render = settings.render
        self.db = dao.Dao()
        self.db.init_tables()
        self.datas = {}
        self.datas['account'] = ["xxx@163.com, 12345", "xxx@126.com, 12345", "xxx@qq.com, 12345"]
        self.datas['receiver'] = ["123@qq.com", '3143431@qq.com', '1243827@qq.com']
        self.datas['name'] = ['lewis', 'lll', 'lone366200']
        self.datas['title'] = ['hello', 'thanks', 'hi']
        self.datas['quote'] = ['xxooxooo', 'xxooxoooxoo']
        self.tmpfiledir = '/tmp'

    def __store_file(self, field_storage, filename):
        #filepath=field_storage.filename.replace('\\','/')
        #filename=filepath.split('/')[-1]
        fout = open(self.tmpfiledir +'/'+ filename,'w')
        fout.write(field_storage.file.read())
        fout.close()

    def __to_db(self, type, csvfile):
        try:
            c2s = csv2sqlite.csv2sqlite(csvfile)
            c2s.csv2db(type)
            c2s.close_db()
            return 1
        except:
            return 0

    def GET(self):
        return self.render.show(self.datas)

    def POST(self):
        #data = web.input()
        data = web.input(quotelist={}, namelist={}, titlelist={}, receiverlist={}, accountlist={})
        DEBUG.pd(data)
        if "addaccount" in data:
            print "add account: ", data['account'], "passwd: ", data['passwd'], "idcode: ", data['idcode']
            if data['account'] and (data['passwd'] or data['idcode']):
                self.db.insertone('account', {'account':data['account'], 'passwd':data['passwd'], 'idcode':data['idcode']})
        if "addreceiver" in data:
            print "add receiver: ", data['receiver']
            self.db.insertone('receiver', {'email':data['receiver']})
        if "addname" in data:
            print "add name: ", data['name']
            self.db.insertone('names', {'name':data['name']})
        if "addtitle" in data:
            print "add title: ", data['title']
            self.db.insertone('subjects', {'subject':data['title']})
        if "addquote" in data:
            print "add quote: ", data['quote']
            self.db.insertone('quotes', {'quote':data['quote']})
        if "addrandom" in data:
            print "add random: ", data['random']
            self.db.insertone('randoms', {'random':data['random']})
        if "addip" in data:
            print "add ip: ", data['ip']
            self.db.insertone('ip', {'addr':data['ip']})

        if 'accountlist' in data and data.accountlist.filename:
            print 'in accountlist'
            self.__store_file(data.accountlist, 'account.csv')
            if self.__to_db(2, self.tmpfiledir + '/account.csv'):
                shutil.move(self.tmpfiledir + '/account.csv', './tmp/account.csv.'+time.asctime())
        if 'receiverlist' in data and data.receiverlist.filename:
            print 'in receiverlist'
            self.__store_file(data.receiverlist, 'receiver.csv')
            if self.__to_db(1, self.tmpfiledir + '/receiver.csv'):
                shutil.move(self.tmpfiledir + '/receiver.csv', './tmp/receiver.csv.'+time.asctime())
        if 'quotelist' in data and data.quotelist.filename:
            print 'in quotelist'
            self.__store_file(data.quotelist, 'quote.csv')
            if self.__to_db(6, self.tmpfiledir + '/quote.csv'):
                shutil.move(self.tmpfiledir + '/quote.csv', './tmp/quote.csv.'+time.asctime())
        if 'namelist' in data and data.namelist.filename:
            print 'in namelist'
            self.__store_file(data.namelist, 'name.csv')
            if self.__to_db(3, self.tmpfiledir + '/name.csv'):
                shutil.move(self.tmpfiledir + '/name.csv', './tmp/name.csv.'+time.asctime())
        if 'titlelist' in data and data.titlelist.filename:
            print 'in titlelist'
            self.__store_file(data.titlelist, 'title.csv')
            if self.__to_db(4, self.tmpfiledir + '/title.csv'):
                shutil.move(self.tmpfiledir + '/title.csv', './tmp/title.csv.'+time.asctime())

        return self.render.show(self.datas)

class New:
    def __init__(self):
        self.render = settings.render
        self.form = web.form.Form(
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
        print self.form.d.title
        print self.form.d.content
        temp = template.Template('./templates/temp1.htm')
        print temp.get_quote()
        print temp.get_toname()
        print temp.get_subject()
        print temp.get_html(self.form.d.content)
        raise web.seeother('/new')

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
        c2s = csv2sqlite.csv2sqlite('./tmp/account.csv')
        c2s.csv2db(2)
        c2s.close_db()
        c2s = csv2sqlite.csv2sqlite('./tmp/receiver.csv')
        c2s.csv2db(1)
        c2s.close_db()

        '''
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

class StopSend:
    def __init__(self):
        self.render = settings.render
    def GET(self):
        return self.render.stop()

 
