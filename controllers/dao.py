# coding: UTF-8
import sqlite3
import time
from config import settings

'''
account = [
            {'id':0,
            'account': 'a91014672@163.com',
            'passwd': 'aa77888',
            'smtp': 'smtp.163.com',
            'min_interval': 20,
            'maxtimepeday': 40,
            'status': 1,                    #0:dead 1:live
            'last_ip': '192.168.1.1',
            'ip_map': 110001010001000000...,#ip mapping 0:dead 1:live
            },
        ]

receiver = [
            {'email': '3345214321.qq.com',
             'status': 0,                   #0:dead 1:live
             'last_account': 'xxx@163.com',
             'account_map': 00000101001..., #account mapping 0:dead 1:live
            },
        ]
ip = [
        {
            'id':0,
            'addr':'192.168.1.1',
            'status':0,
        },
    ]
'''


class Dao:
    def __init__(self, dbPath=''):
        '''
        Initialise CSQliteloader Class
        '''

        #Initialise connection and Class Variables
        if dbPath:
            self.SQLiteDBfileName = dbPath
        else:
            self.SQLiteDBfileName = settings.c['db_url']
        self.conn = sqlite3.connect(self.SQLiteDBfileName)
        self.cursor = self.conn.cursor()

    def __insertRow(self, tableName, rowDict):
        '''
        Insert a single row into DB
        '''

        #Quote values to allow smooth insertion of values
        row = ['"'+v.strip().strip('"')+'"' for v in rowDict.values()]

        #Create sql statement to insert data into database table
        statement = "insert into %s (%s) values (%s)" %(tableName, ", ".join(self.tableFields), ", ".join(row))
        print(statement)
        self.cursor.execute(statement)

    def __total_row(self, table):
        count = 0
        if table is not None and table != '':
            sql = 'select count(*) from %s' % table
            self.cursor.execute(sql)
            re = self.cursor.fetchone() 
        return re[0] 

    def fetchall(self, table):
        if table is not None and table != '':
            sql = 'select * from %s' % table
            self.cursor.execute(sql)
            re = self.cursor.fetchall()
            print len(re), re
            return re

    def fetchone(self, sql):
        if sql is not None and sql != '':
            self.cursor.execute(sql)
            re = self.cursor.fetchall()
            print re
            return re

    def fetchone_by_id(self, table, id):
        if table is not None and table != '':
            sql = 'SELECT * FROM %s WHERE ID = "%s"'%(table, str(id))
            return self.fetchone(sql)

    def fetchone_by_key_value(self, table, key, value):
        if table is not None and table != '':
            sql = 'SELECT * FROM %s WHERE %s = "%s"'%(table, key, str(value))
            return self.fetchone(sql)

    def delete_by_id(self, table, id):
        if table is not None and table != '':
            sql = 'DELETE FROM %s WHERE ID = "%s"' % (table, str(id))
            self.cursor.execute(sql)
            self.conn.commit()

    def delete_by_key_value(self, table, key, value):
        if table is not None and table != '':
            sql = 'DELETE FROM %s WHERE %s = "%s"' % (table, key, str(value))
            self.cursor.execute(sql)
            self.conn.commit()

    def delete_by_primary_key(self, table, value):
        if table is not None and table != '':
            if table is "account":
                key = 'account'
            elif table is "ip":
                key = 'addr'
            elif table is "receiver":
                key = 'email'
            else:
                print "table %s is not exist"%table
                return
            self.delete_by_key_value(table, key, value)

    def update_by_key_value(self, table, update_key, new_value, key, value):
        if table is not None and table != '':
            sql = 'UPDATE %s SET %s = "%s" WHERE %s = "%s"'%(table, update_key, str(new_value), key, str(value))
            self.cursor.execute(sql)
            self.conn.commit()

    def update_last_by_key_value(self, table, key, value, last):
        if table is not None and table != '':
            if table == 'receiver':
                self.update_by_key_value(table, 'last_account', last, key, value)
            elif tables == 'account':
                self.update_by_key_value(table, 'last_ip', last, key, value)

    def update_last_by_id(self, table, id, last):
        if table is not None and table != '':
            self.update_last_by_key_value(table, 'ID', id, last)

    def update_status_by_key_value(self, table, key, value, status):
        if table is not None and table != '':
            self.update_by_key_value(table, 'status', status, key, value)

    def update_status_by_id(self, table, id, status):
        if table is not None and table != '':
            self.update_status_by_key_value(table, 'ID', id, status)

    def update_status_by_primary_key(self, table, value, status):
        if table is not None and table != '':
            if table is "account":
                key = 'account'
            elif table is "ip":
                key = 'addr'
            elif table is "receiver":
                key = 'email'
            else:
                print "table %s is not exist"%table
                return
            self.update_status_by_key_value(table, key, value, status)

    def update_map_by_id(self, table, id, map):
        if table is not None and table != '':
            if table is "account":
                key_map = 'ip_map'
            elif table is "receiver":
                key_map = 'account_map'
            else:
                print "table %s is not exist"%table
            self.update_by_key_value(table, key_map, map, 'ID', id)

    def update_map_by_primary_key(self, table, value, map):
        if table is not None and table != '':
            if table is "account":
                key = 'account'
                key_map = 'ip_map'
            elif table is "receiver":
                key = 'email'
                key_map = 'account_map'
            else:
                print "table %s is not exist"%table
            self.update_by_key_value(table, key_map, map, key, value)

    def find_by_primary_key(self, table, value):
        if table is not None and table != '':
            if table is "account":
                key = 'account'
            elif table is "ip":
                key = 'addr'
            elif table is "receiver":
                key = 'email'
            else:
                print "table %s is not exist"%table
                return
        re = self.fetchone_by_key_value(table, key, value)
        return len(re)

    def insertone(self, table, new):
        row = {}
        count = self.__total_row(table)
        count = count + 1
        row['id'] = str(count)
        row['status'] = '1'
        if table is "account":
            if self.find_by_primary_key(table, new['account']) > 0:
                print 'account: %s exist'%new['account']
                return
            row['account'] = new['account']
            row['passwd'] = new['passwd']
            row['last_time'] = str(int(time.time()))
            row['last_ip'] = ''
            tmp = []
            for i in range(256):
                tmp.append('0')
            row['ip_map'] = ''.join(tmp) 
            com = row['account'][-6:]
            if com in settings.c['account_type'].keys():
                row['smtp'] = settings.c['account_type'][com]['smtp']
                row['min_interval'] = str(settings.c['account_type'][com]['interval'])
                row['max_times_per_day'] = str(settings.c['account_type'][com]['max'])
            else:
                print row['account'], ' can not be config'
                return
        elif table is "ip":
            if self.find_by_primary_key(table, new['addr']) > 0:
                print 'addr: %s exist'%new['addr']
                return
            row['addr'] = new['addr']
        elif table is "receiver":
            if self.find_by_primary_key(table, new['email']) > 0:
                print 'email: %s exist'%new['email']
                return
            row['email'] = new['email']
            row['last_time'] = str(int(time.time()))
            row['last_account'] = ''
            tmp = []
            for i in range(1024):
                tmp.append('0')
            row['account_map'] = ''.join(tmp)
        else:
            print "table %s is not exist"%table
            return

        row['reserve1'] = ''
        row['reserve2'] = ''
        row['reserve3'] = ''
        tmp = ['"'+v.strip().strip('"')+'"' for v in row.values()]
        sql = 'INSERT INTO %s ('%table + ','.join(row.keys()) + ') values (' + ', '.join(tmp) + ')'
        print sql
        self.cursor.execute(sql)
        self.conn.commit()

    def execute_script(self, sqlscript):
        return self.cursor.executescript(sqlscript)

    def execute_sql_script(self, sqlScript):
        try:
            self.execute_script(sqlScript)
            self.conn.commit()
        finally :
            print 'execute script done'

    def drop_table(self, table):
        if table is not None and table != '':
            sql = 'DROP TABLE IF EXISTS ' + table
            self.cursor.execute(sql)
            self.conn.commit()

    def init_tables(self):
        for i in range(len(settings.c['db_name'])):
            self.cursor.execute(settings.c['db_name'][i]['sql'])

        self.conn.commit()

    def close(self):
        self.conn.close()
