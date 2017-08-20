# coding: UTF-8
import os
import utils.loadjson as loadjson
import controllers.dao as dao
import controllers.csv2sqlite as csv2sqlite
import mail.batch_send as batch_send
import mail.send as send
from config import settings
import DEBUG

def sendtest():
    content = u'<html><body><h1>Hi lll, sorry, this attachment is ok, 3Q for you help, and your ice </h1><br>---</br><p>send by <a href="http://www.python.org">suninrain</a>...</p></body></html>'
    subject = u'3Q'
    mail = send.Mail('2371433957@qq.com', 'ojjbenmnnunneabc', 'smtp.qq.com', '192.168.1.8', 587)
    mail.loginsmtp()
    mail.send_text('jdic@qq.com', 'lll', 'suninrain', content, 'html', subject)
    #mail.send_html_with_attachment(receiver, content, attachment_path):

def initDB():
    c2s = csv2sqlite.csv2sqlite('./tmp/account.csv')
    c2s.csv2db(2)
    c2s.close_db()
    c2s = csv2sqlite.csv2sqlite('./tmp/receiver.csv')
    c2s.csv2db(1)
    c2s.close_db()
    c2s = csv2sqlite.csv2sqlite('./tmp/ip.csv')
    c2s.csv2db(0)
    c2s.close_db()
    c2s = csv2sqlite.csv2sqlite('./tmp/name.csv')
    c2s.csv2db(3)
    c2s.close_db()
    c2s = csv2sqlite.csv2sqlite('./tmp/subject.csv')
    c2s.csv2db(4)
    c2s.close_db()
    c2s = csv2sqlite.csv2sqlite('./tmp/quote.csv')
    c2s.csv2db(6)
    c2s.close_db()

def batchsend():
    batchsend = batch_send.Batchsend()
    batchsend.run()

def loadjsonfile():
    data = settings.c['db_name'][0]
    loadjson.loadtojson(data, os.getcwd() + u"/tmp/test.json")
    d = loadjson.loadfromjson(os.getcwd() + u"/tmp/test.json")
    print d['name']
    DEBUG.pd(d)

def template():
    with open('./templates/temp1.htm') as f:
        contain = u'Hi lll, sorry, this attachment is ok, 3Q for you help, and your ice'
        fromname = u'lewis'
        print f.read()%(contain, '名人名言', 'www.lll.com', fromname)

if __name__ == "__main__":
 
    #db = dao.Dao()
    #db.init_tables()
    #new = {'account':'a91008950@163.com', 'passwd':'aa777888'}

    #db.insertone('account', new)
    #db.delete_by_key_value('account', 'account', 'a91008950@163.com')
    #db.fetchall("account")
    #db.delete_by_id('account', 2)
    #db.update_status_by_key_value('account', 'account', 'a91008950@163.com', 0)

    #db.fetchall("account")
    #db.fetchone_by_id("account", 1)
    #db.fetchone_by_key_value("account", "account", "a91008950@163.com" )

    initDB()

    #batchsend()

    #sendtest()

    #loadjsonfile()

    #template()
