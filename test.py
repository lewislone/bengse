# coding: UTF-8
import utils.loadcvs as loadcvs
import controllers.dao as dao
import controllers.csv2sqlite as csv2sqlite
import mail.batch_send as batch_send
import mail.send as send

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

def batchsend():
    batchsend = batch_send.Batchsend()
    batchsend.run()

if __name__ == "__main__":
 
    #loadcvs.loadtojson(os.getcwd() + u"/邮箱.cvs")

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
