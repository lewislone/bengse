# coding: UTF-8
import os
import time
import DEBUG
import send
import random
from random import choice
from config import settings
import controllers.dao as dao
import utils.loadjson as loadjson
import template

class Batchsend:
    def __init__(self):
        self.db = dao.Dao()
        self.db.init_tables()
        self.temp  = template.Template()
        jsonfile = os.getcwd() + u"/tmp/status.json"
        if os.path.exists(jsonfile):
            self.status = loadjson.loadfromjson(os.getcwd() + u"/tmp/status.json")
        else:
            self.status = {}
            self.status['accounts'] = {}
            self.status['receivers'] = {}
            self.status['ip'] = {}

    def __get_contain(self):
        return self.temp.get_contain()

    def __get_subject(self):
        return self.temp.get_subject()

    def __get_toname(self):
        return self.temp.get_toname()

    def __get_fromname(self):
        return self.temp.get_fromname()

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

    def __update_status(self, type, key, code):
        if type != 'account' or type != 'receiver' or type != 'ip':
            print 'unknown type'
            return
        if key not in self.status[type].keys():
            self.status[type][key] = {}
            self.status[type][key]['ok'] = 0
            self.status[type][key]['failed'] = 0
            self.status[type][key]['count'] = 0
        if code:
            self.status[type][key]['failed'] += 1
        else:
            self.status[type][key]['ok'] += 1
        self.status[type][key]['count'] += 1

    def sent_mail(self, ip, receiver, account, account_type):
        addr = account[1]
        if 'count' in self.status['account'][addr].keys():
            if self.status['account'][addr]['count'] >= account_type['max']:
                return
        if addr[-6:] == 'qq.com' and account[10] != '':
            pw = account[10]
        else:
            pw = account[2]
        smpt = account[3]
        if account[9]:
            mail = send.Mail(addr, pw, smpt, account[9], account_type['port']) #use last_ip
        else:
            mail = send.Mail(addr, pw, smpt, ip[1], account_type['port'])
            self.db.update_last_by_key_value('account', 'account', addr, ip)
        ret = mail.loginsmtp()
        self.__update_status('account', addr, ret)
        if ret:
            print 'login smtp failed!!!  %d'%ret
            mail.quit()
            return
        content = self.__get_contain()
        subject = self.__get_subject()
        toname = self.__get_toname()
        fromname = self.__get_fromname()
        #mail.send_html_with_attachment(receiver, content, attachment_path):
        ret = mail.send_text(receiver[1], toname, fromname, content, 'html', subject)
        self.__update_status('receiver', receiver[1], ret)
        if ret:
            print 'send email failed!!!  %d'%ret
        mail.quit()

    def __random_get_index(self, max):
        return choice(range(max))

    def __get_a_account(self, accounts):
        index = self.__random_get_index(len(accounts))
        return accounts[index]

    def run(self):
        #init
        print 'total ip row: ', self.db.total_row('ip')
        print 'total accounts row: ', self.db.total_row('account')
        print 'total receivers row: ', self.db.total_row('receiver')
        rcv_indexs = range(self.db.total_row('receiver'))
        random.shuffle(rcv_indexs)
        ip_indexs = range(self.db.total_row('ip'))
        random.shuffle(ip_indexs)

        for (key, account_type) in settings.c['account_type'].items(): #list all account type one by one
            accounts = self.__get_account(account_type['smtp'])
            if len(accounts) == 0:
                continue
            last_account = ''
            for rcv_index in rcv_indexs: #random get a receiver
                account = self.__get_a_account(accounts)#random get a account belong account_type['smtp']
                receiver = self.__get_reciver(rcv_index)
                ip = self.__get_ip(ip_indexs[rcv_index%len(ip_indexs)]) #random get a ip
                print 'receiver: ', receiver
                print 'ip: ', ip
                self.sent_mail(ip, receiver, account, account_type)
                if last_account == account[1]:
                    time.sleep(account_type['interval']*2/1000.0)
                last_account = account[1]
                break
            break

    def stop(self):
        print("stop...")

if __name__ == "__main__":

    batchsend = Batchsend()
    batchsend.run()
