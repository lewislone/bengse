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
    def __init__(self, title=' ', content=' '):
        self.db = dao.Dao()
        self.db.init_tables()
        self.content = content
        self.title = title
        self.temp = template.Template('./templates/temp1.htm')
        jsonfile = os.getcwd() + u"/tmp/status.json"
        if os.path.exists(jsonfile):
            self.status = loadjson.loadfromjson(os.getcwd() + u"/tmp/status.json")
        else:
            self.status = {}
            self.status['accounts'] = {}
            self.status['receivers'] = {}
            self.status['ip'] = {}

        if os.path.exists(os.getcwd() + '/tmp/tmp.json'):
            os.remove(os.getcwd() + '/tmp/tmp.json')


    def __save_count(self, ok):
        path = os.getcwd() + '/tmp/tmp.json'
        data = {}
        try:
            if os.path.exists(path):
                data = loadjson.loadfromjson(path)
            else:
                data = {'sent_count': 0, 'succeed': 0}
        except:
            data = {'sent_count': 0, 'succeed': 0}
        data['sent_count'] = data['sent_count'] + 1
        if ok == 0:
            data['succeed'] = data['succeed'] + 1
        loadjson.loadtojson(data, path)

    def __get_contain(self, receiver):
        return self.temp.get_html(self.content, receiver)

    def __get_subject(self):
        return self.temp.get_subject()

    def __get_toname(self):
        return self.temp.get_toname()

    def __get_fromname(self):
        return self.temp.get_fromname()

    def __get_reciver(self, rcv_index):
        if rcv_index == 0:
            rcv_index = 1
        receiver = self.db.fetchone_by_id('receiver', rcv_index)
        if len(receiver):
            return receiver[0]
        else:
            return 'actiontec_test@qq.com'

    def __get_account(self):
        accounts = self.db.fetchall('account')
        return accounts

    def __get_ip(self, id):
        if id == 0:
            id = 1
        ip = self.db.fetchone_by_id('ip', id) 
        return ip[0]

    def __update_status(self, type, key, code):
        if type != 'accounts' or type != 'receivers' or type != 'ip':
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
        ret = 0
        addr = account[1]
        if addr in self.status['accounts'].keys() and 'count' in self.status['accounts'][addr].keys():
            if self.status['accounts'][addr]['count'] >= account_type['max']:
                return ret
        if addr[-6:] == 'qq.com' and account[10] != '':
            pw = account[10]
        else:
            pw = account[2]
        print 'passwd: ', pw
        smpt = account[3]
        try:
            if account[9]:
                mail = send.Mail(addr, pw, smpt, account[9], account_type['port']) #use last_ip
            else:
                try:
                    mail = send.Mail(addr, pw, smpt, ip[1], account_type['port'])
                    self.db.update_last_by_key_value('account', 'account', addr, ip)
                except:
                    print 'connect to smtp server failed with new ip'
        except:
            try:
                if account[9]:
                    mail = send.Mail(addr, pw, smpt, ip[1], account_type['port'])
                    self.db.update_last_by_key_value('account', 'account', addr, ip)
            except:
                self.__update_status('accounts', addr, -1)
                print 'connect to smtp server failed!!!!'
                return -1
        ret = mail.loginsmtp()
        if ret:
            print 'login smtp failed!!!  %d'%ret
            mail.quit()
            self.__update_status('accounts', addr, ret)
            return ret
        content = self.__get_contain(receiver[1])
        subject = self.title+' '+self.__get_subject()
        toname = self.__get_toname()
        fromname = self.__get_fromname()
        #mail.send_html_with_attachment(receiver, content, attachment_path):
        ret = mail.send_text(receiver[1], toname, fromname, content, 'html', subject)
        self.__update_status('receivers', receiver[1], ret)
        if ret:
            print 'send email failed!!!'
        mail.quit()
        return ret

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

        #for (key, account_type) in settings.c['account_type'].items(): #list all account type one by one
        #    if not os.path.exists(os.getcwd() + "/tmp/senderrunning"):
        #        break;
        #    accounts = self.__get_account(account_type['smtp'])
        #    if len(accounts) == 0:
        #        continue
        #    last_account = ''
        accounts = self.__get_account()
        if len(accounts) == 0:
            print "fatch account failed , there is 0 account!!!!!!!!!!"
            self.db.close()
            return
        last_account = ''
        for rcv_index in rcv_indexs: #random get a receiver
            if not os.path.exists(os.getcwd() + "/tmp/senderrunning"):
                break;
            account = self.__get_a_account(accounts)#random get a account belong account_type['smtp']
            receiver = self.__get_reciver(rcv_index)
            account_type = settings.c['account_type'][account[1][-6:]]
            ip = self.__get_ip(ip_indexs[rcv_index%len(ip_indexs)]) #random get a ip
            print 'account: ', account[1]
            print 'receiver: ', receiver[1]
            print 'ip: ', ip[1]
            if account[1] in self.status['accounts'].keys():
                print '###count: ', self.status['accounts'][account[1]]['count']
                if self.status['accounts'][account[1]]['count'] > account_type['max']:
                    print account[1], ' sent too many email ', account_type['max']
                    continue
            try:
                ret = self.sent_mail(ip, receiver, account, account_type)
                if ret < 0:
                    account = self.__get_a_account(accounts)#random get a account belong account_type['smtp']
                    print 'account: ', account[1]
                    print 'receiver: ', receiver[1]
                    print 'ip: ', ip[1]
                    ret = self.sent_mail(ip, receiver, account, account_type)
            except:
                ret = -1
                print 'sent_mail failed!!!'
            self.__save_count(ret)
            if last_account == account[1]:
                time.sleep(account_type['interval']*10)
            time.sleep(5)
            last_account = account[1]

        self.db.close()

    def stop(self):
        os.remove(os.getcwd() + "/tmp/senderrunning")
        print("stop...")

if __name__ == "__main__":

    batchsend = Batchsend()
    batchsend.run()
