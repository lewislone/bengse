# coding: UTF-8
import os
import sys
sys.path.insert(0,'../utils/webpy')
import web

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, '../templates')
render = web.template.render(templates_root, base='../templates/base', cache=False)

#db = web.database(dbn='mysql', db='cover', user='root', pw='lewis')

config = web.storage(
    email='lone.un@gmail.com',
    site_name = 'lll',
    site_desc = 'lll',
    static = '/static',
)

web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render


c = {
        'debug'     : True,
        'db_url'    : './tmp/main.db',
        'db_name'   : [
                        { 
                         'name': 'account',
                         'keys': ['id', 'account', 'passwd', 'smtp', 'min_interval', 'max_times_per_day', 'status', 'ip_map', 'last_time', 'last_ip', 'code', 'reserve1', 'reserve2', 'reserve3'],
                         'sql' : '''
                                CREATE TABLE IF NOT EXISTS account (
                                  'id' int(11) NOT NULL,
                                  `account` varchar(40) NOT NULL,
                                  `passwd` varchar(20) NOT NULL,
                                  `smtp` varchar(20) NOT NULL,
                                  `min_interval` int(8) NOT NULL,
                                  `max_times_per_day` int(8) NOT NULL,
                                  `status` int NOT NULL,
                                  `ip_map` char(256) NOT NULL,
                                  `last_time` int(11) NOT NULL,
                                  `last_ip` varchar(20)  DEFAULT NULL,
                                  `code` varchar(20) DEFAULT NULL,
                                  `reserve1` varchar(20) DEFAULT NULL,
                                  `reserve2` varchar(20) DEFAULT NULL,
                                  `reserve3` varchar(20) DEFAULT NULL,
                                   PRIMARY KEY (`account`)
                                )
                                ''',
                        },
                        {
                         'name': 'receiver',
                         'keys': ['id', 'email', 'status', 'account_map', 'last_time', 'last_account', 'reserve1', 'reserve2', 'reserve3'],
                         'sql' : '''
                                CREATE TABLE IF NOT EXISTS receiver (
                                  'id' int(11) NOT NULL,
                                  `email` varchar(40) NOT NULL,
                                  `status` int NOT NULL,
                                  `account_map` char(1024) NOT NULL,
                                  `last_time` int(11) NOT NULL,
                                  `last_account` varchar(40) DEFAULT NULL,
                                  `reserve1` varchar(20) DEFAULT NULL,
                                  `reserve2` varchar(20) DEFAULT NULL,
                                  `reserve3` varchar(20) DEFAULT NULL,
                                   PRIMARY KEY (`email`)
                                )
                                ''',
                        },
                        {
                         'name': 'ip',
                         'keys': ['id', 'addr', 'status', 'reserve1', 'reserve2', 'reserve3'],
                         'sql' : '''
                                CREATE TABLE IF NOT EXISTS ip (
                                  'id' int(11) NOT NULL,
                                  `addr` varchar(20) NOT NULL,
                                  `status` int NOT NULL,
                                  `reserve1` varchar(20) DEFAULT NULL,
                                  `reserve2` varchar(20) DEFAULT NULL,
                                  `reserve3` varchar(20) DEFAULT NULL,
                                   PRIMARY KEY (`addr`)
                                )
                                ''',
                        },
                      ],
        'account_type': {
                            'il.com': {
                                        'smtp': 'smtp.gmail.com',
                                        'max' : 50,
                                        'interval' : 100,
                                        'port': 587,
                                    },
                            'qq.com': {
                                        'smtp': 'smtp.qq.com',
                                        'max' : 50,
                                        'interval' : 100,
                                        'port': 587,
                                    },
                            'mx.com': {
                                        'smtp': 'smtp.gmx.com',
                                        'max' : 100,
                                        'interval' : 100,
                                        'port': 25,
                                    },
                            'ab.com': {
                                        'smtp': 'smtp.gawab.com',
                                        'max' : 100,
                                        'interval' : 100,
                                        'port': 25,
                                    },
                            '63.com': {
                                        'smtp': 'smtp.163.com',
                                        'max' : 50,
                                        'interval' : 100,
                                        'port': 25,
                                    },
                            '26.com': {
                                        'smtp': 'smtp.126.com',
                                        'max' : 50,
                                        'interval' : 100,
                                        'port': 25,
                                    },
                            'ah.com': {
                                        'smtp': 'smtp.yeah.com',
                                        'max' : 50,
                                        'interval' : 100,
                                        'port': 25,
                                    },
                            'ol.com': {
                                        'smtp': 'smtp.aol.com',
                                        'max' : 100,
                                        'interval' : 100,
                                        'port': 25,
                                    },
                            'hu.com': {
                                        'smtp': 'smtp.sohu.com',
                                        'max' : 100,
                                        'interval' : 200,
                                        'port': 25,
                                    },
                            '39.com': {
                                        'smtp': 'smtp.139.com',
                                        'max' : 100,
                                        'interval' : 100,
                                        'port': 25,
                                    },
                            'na.com': {
                                        'smtp': 'smtp.sina.com',
                                        'max' : 30,
                                        'interval' : 200,
                                        'port': 25,
                                    },
                            've.com': {
                                        'smtp': 'smtp.live.com',
                                        'max' : 100,
                                        'interval' : 100,
                                        'port': 25,
                                    },
                        }
    }
