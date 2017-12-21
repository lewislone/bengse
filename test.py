# coding: UTF-8
import os
import sys
sys.path.insert(0,'./lib/webpy')
import web
import utils.loadjson as loadjson
import controllers.dao as dao
import controllers.csv2sqlite as csv2sqlite
import mail.batch_send as batch_send
import mail.send as send
import mail.contain as contain
import mail.template as template 
import DEBUG
import logging
import time
import socket
import struct
import random

def sendtest():
    temp = template.Template('./templates/temp1.htm')
    #content = u'<html><body><h1>Hi lll, Have you ever heard that the loveliest girls in the world live in my country? I long for finding a special person for serious relations or even family life </h1><br>---</br><p>send by <a href="http://www.fdaicid.com">fdsic</a>......</p></body></html>'
    text = u'Hi lll, 您获得了进入379442741VIP优惠总群资格, <a href="https://jq.qq.com/?_wv=1027&k=5fzqAx0" target="_blank" style="outline: none; cursor: pointer; color: rgb(30, 84, 148);">点我一键进群</a>'
    #text = u'Nearly a dozen years ago, a local contractor was building an underpass near my home. It was constructed by the open method, employing concrete piles driven into the soil with a diesel headframe. The operation usually has been started at 7 am and lasted until 10 pm. The uproar was such that it was impossible to remain at home. The work was scheduled for three years, continued four years, and finally, a charming 50 meters long 2.5 meters tall passageway emerged to the neighbors'
    #content = temp.get_html(text, '2402156431@qq.com')
    cn = contain.Contain()
    content = cn.get_html(text, '2402156431@qq.com')
    print content
    subject = u'love paradise '
    mail = send.Mail('lawz7q5q44vid@mail.ua', 'Zz4igBe4Ze', 'smtp.mail.ru', '108.187.61.74', 587)
    #mail = send.Mail('l5ahlxuvnfzdo@inbox.ru', 'cu0B4f40N', 'smtp.mail.ru', '10.0.0.2', 587)
    #mail = send.Mail('eqnvrimpi437@mail.ru', 'gTGR1B5T4l46', 'smtp.mail.ru', '10.0.0.2', 587)
    mail.loginsmtp()
    mail.send_text('2402156431@qq.com', 'suninrain', 'suninrain', content, 'html', subject)
    #mail.send_html_with_attachment(receiver, content, attachment_path):

def initDB():
    db = dao.Dao()
    db.init_tables()
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

def clearDB():
    db = dao.Dao()
    print db.get_all_ip()
    db.clear_table('ip')
    print "after clear"
    print db.get_all_ip()

def clearDB2():
    db = dao.Dao()
    print db.get_all_account()
    db.clear_table('account')
    print "after clear"
    print db.get_all_account()


def batchsend():
    title = u'xxoo'
    contain = u'Hi lll, sorry, this attachment is ok, 3Q for you help, and your ice'
    batchsend = batch_send.Batchsend(title, contain)
    batchsend.run()

def temp():
    with open('./templates/temp1.htm') as f:
        contain = u'Hi lll, sorry, this attachment is ok, 3Q for you help, and your ice'
        fromname = u'lewis'
        print f.read()%(contain, u'名人名言', u'www.lll.com', fromname)

        temp = template.Template('./templates/temp1.htm')
        temp.get_quote()
        temp.get_toname()
        temp.get_subject()
        print temp.get_html(contain)

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

    #initDB()

    #clearDB()
    #c2s = csv2sqlite.csv2sqlite('./tmp/ip.csv')
    #c2s.csv2db(0)
    #c2s.close_db()

    t0 = time.time()
    clearDB()
    new = {'addr': '144.117.143.172'}
    db = dao.Dao()
    db.insertone('ip', new)
    clearDB()
    t1 = time.time()
    c2s = csv2sqlite.csv2sqlite('./tmp/ip.csv')
    c2s.csv2db(0)
    t2 = time.time()
    print t1-t0
    print t2-t1
    c2s.close_db()

    #count = 10000
    #while count > 0:
    #    print socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    #    count = count - 1

    #batchsend()

    #sendtest()

    #loadjsonfile()

    #temp()

    #cn = contain.Contain()
    #print cn.get_html("this is contain", 'xxx@qq.com')


    #logging.basicConfig(level=logging.DEBUG,
    #            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #            datefmt='%a, %d %b %Y %H:%M:%S',
    #            filename='myapp.log',
    #            filemode='w')
    #
    #logging.debug('This is debug message')
    #logging.info('This is info message')
    #logging.warning('This is warning message')
