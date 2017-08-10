# coding: UTF-8
import os
import utils.loadcvs as loadcvs
import controllers.dao as dao
import controllers.csv2sqlite as csv2sqlite


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

'''
    c2s = csv2sqlite.csv2sqlite('./tmp/account.csv')
    c2s.csv2db(2)
    c2s.close_db()
    c2s = csv2sqlite.csv2sqlite('./tmp/receiver.csv')
    c2s.csv2db(1)
    c2s.close_db()
    c2s = csv2sqlite.csv2sqlite('./tmp/ip.csv')
    c2s.csv2db(0)
    c2s.close_db()
'''
