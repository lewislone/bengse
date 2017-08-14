# coding: UTF-8
import DEBUG
import send
import random
from config import settings
import controllers.dao as dao

class Batchsend:
    def __init__(self):
        self.db = dao.Dao()
        self.db.init_tables()

    def __get_contain(self):
        return '<html><body><h1>Hi lll, sorry, this attachment is ok, 3Q for you help, and your ice </h1>' + '<br>---</br>'+ '<p>send by <a href="http://www.python.org">fri</a>...</p>' + '</body></html>'

    def __get_reciver(self, rcv_index):
        receiver = self.db.fetchone_by_id('receiver', rcv_index)
        DEBUG.pd(receiver)
        return receiver[0]

    def __get_account(self, smtp):
        accounts = self.db.fetchone_by_key_value('account', 'smtp', smtp)
        return accounts

    def __get_ip(self, id):
        ip = self.db.fetchone_by_id('ip', id) 
        return ip[0]

    def sent_mail(self, ip, receiver, account):
        print receiver
        addr = account[1]
        pw = account[2]
        smpt = account[3]
        if account[9]:
            mail = send.Mail(addr, pw, smpt, account[9])
        else:
            mail = send.Mail(addr, pw, smpt, ip[1])
            self.db.update_last_by_key_value('account', 'account', addr, ip)
        mail.loginsmtp()
        content = self.__get_contain()
        subject = u'3Q'
        #mail.send_html_with_attachment(receiver, content, attachment_path):
        mail.send_text(receiver[1], 'lll', 'suninrain', content, 'html', subject)
        mail.quit()

    def run(self):
        #init
        print 'total ip row: ', self.db.total_row('ip')
        print 'total accounts row: ', self.db.total_row('account')
        print 'total receivers row: ', self.db.total_row('receiver')
        rcv_indexs = range(self.db.total_row('receiver'))
        random.shuffle(rcv_indexs)
        ip_indexs = range(self.db.total_row('ip'))
        random.shuffle(ip_indexs)
        print rcv_indexs, ip_indexs
        status = {}
        status['accounts'] = {}
        status['receivers'] = {}
        status['ip'] = {}

        for (key, type) in settings.c['account_type'].items():
            accounts = self.__get_account(type['smtp'])
            if len(accounts) == 0:
                continue
            acu_indexs = range(len(accounts))
            random.shuffle(acu_indexs)
            for i in acu_indexs:
                for rcv_index in rcv_indexs:
                    receiver = self.__get_reciver(rcv_index)
                    print 'receiver: ', receiver
                    ip = self.__get_ip(ip_indexs[i%len(ip_indexs)])
                    print 'ip: ', ip
                    self.sent_mail(ip, receiver, accounts[i])
                    break
                break
            break

if __name__ == "__main__":

    batchsend = Batchsend()
    batchsend.run()
