# coding: UTF-8
import os
import sys
sys.path.insert(0,'../lib/webpy')
import web
import logging

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

log = logging
logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

c = {
        'debug'     : True,
        'debuglevel': 1,
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
                        {
                         'name': 'names',
                         'keys': ['id', 'name', 'status', 'reserve1', 'reserve2', 'reserve3'],
                         'sql' : '''
                                CREATE TABLE IF NOT EXISTS names (
                                  'id' int(11) NOT NULL,
                                  `name` varchar(40) NOT NULL,
                                  `status` int NOT NULL,
                                  `reserve1` varchar(20) DEFAULT NULL,
                                  `reserve2` varchar(20) DEFAULT NULL,
                                  `reserve3` varchar(20) DEFAULT NULL,
                                   PRIMARY KEY (`name`)
                                )
                                ''',
                        },
                        {
                         'name': 'subjects',
                         'keys': ['id', 'subject', 'status', 'reserve1', 'reserve2', 'reserve3'],
                         'sql' : '''
                                CREATE TABLE IF NOT EXISTS subjects (
                                  'id' int(11) NOT NULL,
                                  `subject` varchar(128) NOT NULL,
                                  `status` int NOT NULL,
                                  `reserve1` varchar(20) DEFAULT NULL,
                                  `reserve2` varchar(20) DEFAULT NULL,
                                  `reserve3` varchar(20) DEFAULT NULL,
                                   PRIMARY KEY (`subject`)
                                )
                                ''',
                        },
                        {
                         'name': 'randoms',
                         'keys': ['id', 'random', 'status', 'reserve1', 'reserve2', 'reserve3'],
                         'sql' : '''
                                CREATE TABLE IF NOT EXISTS randoms (
                                  'id' int(11) NOT NULL,
                                  `random` varchar(40) NOT NULL,
                                  `status` int NOT NULL,
                                  `reserve1` varchar(20) DEFAULT NULL,
                                  `reserve2` varchar(20) DEFAULT NULL,
                                  `reserve3` varchar(20) DEFAULT NULL,
                                   PRIMARY KEY (`random`)
                                )
                                ''',
                        },
                        {
                         'name': 'quotes',
                         'keys': ['id', 'quote', 'status', 'reserve1', 'reserve2', 'reserve3'],
                         'sql' : '''
                                CREATE TABLE IF NOT EXISTS quotes (
                                  'id' int(11) NOT NULL,
                                  `quote` varchar(1024) NOT NULL,
                                  `status` int NOT NULL,
                                  `reserve1` varchar(20) DEFAULT NULL,
                                  `reserve2` varchar(20) DEFAULT NULL,
                                  `reserve3` varchar(20) DEFAULT NULL,
                                   PRIMARY KEY (`quote`)
                                )
                                ''',
                        },
                      ],
        'account_type': {
                            '189.cn': {
                                        'smtp': 'smtp.189.cn',
                                        'max' : 10,
                                        'interval' : 300,
                                        'port': 25,
                                    },
                            'cn.com': {
                                        'smtp': 'smtp.21cn.com',
                                        'max' : 10,
                                        'interval' : 300,
                                        'port': 25,
                                    },
                            'box.ru': {
                                        'smtp': 'smtp.inbox.ru',
                                        'max' : 10,
                                        'interval' : 300,
                                        'port': 587,
                                    },
                            '@bk.ru': {
                                        'smtp': 'smtp.bk.ru',
                                        'max' : 10,
                                        'interval' : 300,
                                        'port': 587,
                                    },
                            'ist.ru': {
                                        'smtp': 'smtp.list.ru',
                                        'max' : 10,
                                        'interval' : 300,
                                        'port': 587,
                                    },
                            'ail.ua': {
                                        'smtp': 'smtp.mail.ru',
                                        'max' : 10,
                                        'interval' : 300,
                                        'port': 587,
                                    },
                            'ail.ru': {
                                        'smtp': 'smtp.mail.ru',
                                        'max' : 3,
                                        'interval' : 100,
                                        'port': 587,
                                    },
                            'il.com': {
                                        'smtp': 'smtp.gmail.com',
                                        'max' : 3,
                                        'interval' : 10,
                                        'port': 587,
                                    },
                            'qq.com': {
                                        'smtp': 'smtp.qq.com',
                                        'max' : 3,
                                        'interval' : 45,
                                        'port': 587,
                                    },
                            'mx.com': {
                                        'smtp': 'smtp.gmx.com',
                                        'max' : 3,
                                        'interval' : 100,
                                        'port': 25,
                                    },
                            'ab.com': {
                                        'smtp': 'smtp.gawab.com',
                                        'max' : 3,
                                        'interval' : 10,
                                        'port': 25,
                                    },
                            '63.com': {
                                        'smtp': 'smtp.163.com',
                                        'max' : 3,
                                        'interval' : 20,
                                        'port': 25,
                                    },
                            '26.com': {
                                        'smtp': 'smtp.126.com',
                                        'max' : 3,
                                        'interval' : 20,
                                        'port': 25,
                                    },
                            'ah.net': {
                                        'smtp': 'smtp.yeah.net',
                                        'max' : 3,
                                        'interval' : 20,
                                        'port': 25,
                                    },
                            'ol.com': {
                                        'smtp': 'smtp.aol.com',
                                        'max' : 3,
                                        'interval' : 5,
                                        'port': 25,
                                    },
                            'hu.com': {
                                        'smtp': 'smtp.sohu.com',
                                        'max' : 3,
                                        'interval' : 140,
                                        'port': 25,
                                    },
                            '39.com': {
                                        'smtp': 'smtp.139.com',
                                        'max' : 3,
                                        'interval' : 15,
                                        'port': 25,
                                    },
                            'na.com': {
                                        'smtp': 'smtp.sina.com',
                                        'max' : 3,
                                        'interval' : 130,
                                        'port': 25,
                                    },
                            've.com': {
                                        'smtp': 'smtp.live.com',
                                        'max' : 3,
                                        'interval' : 10,
                                        'port': 25,
                                    },
                        }
    }
