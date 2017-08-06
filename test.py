# coding: UTF-8
import os
import utils.loadcvs as loadcvs
import controllers.dao as dao


'''
account = [
            {'id':0,
            'account': 'a91014672@163.com',
            'passwd': 'aa77888',
            'smtp': 'smtp.163.com',
            'mini_interval': 20,
            'maxtimepeday': 40,
            'status': 1,                    #0:dead 1:live
            'ip_map': 110001010001000000...,#ip mapping 0:dead 1:live
            },
            {'id':1,
            'account': 'a91014672@163.com',
            'passwd': 'aa77888',
            'smtp': 'smtp.163.com',
            'mini_interval': 20,
            'maxtimepeday': 40,
            'status': 0,
            'ip_map': 011010100010000000...,
            },
        ]

consumer = [
            {'email': '3345214321.qq.com',
             'status': 0,                   #0:dead 1:live
             'account_map': 00000101001..., #account mapping 0:dead 1:live
            },
        ]
ip = [
        {
            'id':0,
            'addr':'192.168.1.1',
            'status':0,
        },
        {
            'id':1,
            'addr':'192.168.1.2',
            'status':1,
        },
    ]
'''

if __name__ == "__main__":
 
    #loadcvs.loadtojson(os.getcwd() + u"/邮箱.cvs")
    db = dao.Dao()
    db.init_tables()
    print db.__total_row("account")
