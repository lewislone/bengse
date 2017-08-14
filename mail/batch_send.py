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

    def __get_reciver(self, rcv_index):
        receiver = self.db.fetchone_by_id('receivers', rcv_index)
        DEBUG.pd(receiver)
        return receiver

    def __get_account(self, smtp):
        accounts = self.db.fetchone_by_key_value('account', 'smtp', smtp):
        return accounts

    def __get_ip(self, id):
        ip = self.db.fetchon_by_id('ip', id) 
        return ip

    def sent_mail(self, ip, accounts):
        addr = accounts['account']
        pw = accounts['passwd']
        smpt = accounts['smpt']
        if accounts['last_ip']:
            mail = sent.Mail(addr, pw, smpt, accounts['last_ip'])
        else:
            mail = sent.Mail(addr, pw, smpt, ip)
            self.db.update_last_by_key_value('account', 'account', addr, ip)
        mail.loginsmtp()
        mail.send_html_with_attachment(self, receiver, content, attachment_path):
        mail.quit()

    def run(self):
        #init
        print 'total ip row: ', self.db.total_row('ip')
        print 'total accounts row: ', self.db.total_row('account')
        print 'total receivers row: ', self.db.total_row('receiver')
        total = random.shuffle(items) 
        rcv_indexs = random.shuffle(range(self.db.total_row('receiver')))
        ip_indexs = random.shuffle(range(self.db.total_row('ip')))
        status = {}
        status['accounts'] = {}
        status['receivers'] = {}
        status['ip'] = {}

        for (key, type) in setting.c['account_type'].items():
            accounts = self.__get_account(smtp)
            acu_indexs = random.shuffle(range(len(accounts)))
            for i in range(len(acu_indexs)):
                for rcv_index in rcv_indexs:
                    receiver = self.__get_reciver(rcv_index):
                    ip = self.__get_ip(ip_indexs[i%len(ip_indexs)]):
                    self.sent_mail(ip, accounts[i])

if __name__ == "__main__":

    batchsend = Batchsend()
    batchsend.run()
