# coding: UTF-8
import send
import random
import controllers.dao as dao

class Batchsend:
    def __init__(self):
        db = dao.Dao()
        db.init_tables()

    def __get_contain(self):

    def __get_reciver(self):

    def __get_account(self):

    def __get_ip(self):

    def run(self):
        #init
        print 'total ip row: ', db.total_row('ip')
        print 'total accounts row: ', db.total_row('accounts')
        print 'total receivers row: ', db.total_row('receivers')
        total = random.shuffle(items) 
        rcv_indexs = random.shuffle(range(db.total_row('receivers')))
        ip_indexs = random.shuffle(range(db.total_row('ip')))
        acu_indexs = random.shuffle(range(db.total_row('accounts')))

        #get all receivers

        #get all accounts

if __name__ == "__main__":

    batchsend = Batchsend()
    batchsend.run()
