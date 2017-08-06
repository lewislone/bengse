# coding: UTF-8
import os
import web

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, '../templates')
render = web.template.render(templates_root, cache=False)

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
                         'keys': ['id', 'account', 'passwd', 'smtp', 'mini_interval', 'max_times_per_day', 'status', 'ip_map', 'reserve1', 'reserve2', 'reserve3'],
                         'sql' : '''
                                CREATE TABLE IF NOT EXISTS account (
                                  'id' int(11) NOT NULL,
                                  `account` varchar(40) NOT NULL,
                                  `passwd` varchar(20) NOT NULL,
                                  `smtp` varchar(20) NOT NULL,
                                  `min_interval` int(8) NOT NULL,
                                  `max_times_per_day` int(8) NOT NULL,
                                  `status` int NOT NULL,
                                  `ip_map` char(32) NOT NULL,
                                  `reserve1` varchar(20) DEFAULT NULL,
                                  `reserve2` varchar(20) DEFAULT NULL,
                                  `reserve3` varchar(20) DEFAULT NULL,
                                   PRIMARY KEY (`account`)
                                )
                                ''',
                        },
                        {
                         'name': 'receiver',
                         'keys': ['id', 'email', 'status', 'account_map', 'reserve1', 'reserve2', 'reserve3'],
                         'sql' : '''
                                CREATE TABLE IF NOT EXISTS receiver (
                                  'id' int(11) NOT NULL,
                                  `email` varchar(40) NOT NULL,
                                  `status` int NOT NULL,
                                  `account_map` char(32) NOT NULL,
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
                                  `addr` varchar(40) NOT NULL,
                                  `status` int NOT NULL,
                                  `reserve1` varchar(20) DEFAULT NULL,
                                  `reserve2` varchar(20) DEFAULT NULL,
                                  `reserve3` varchar(20) DEFAULT NULL,
                                   PRIMARY KEY (`addr`)
                                )
                                ''',
                        },
                      ],
    }
