# coding: UTF-8
import os
import sqlite3
import time
from config import settings

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
        ]

receiver = [
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
    ]
'''


class Dao:
    def __init__(self):
        '''
        Initialise CSQliteloader Class
        '''

        #Initialise connection and Class Variables
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
            count = self.cursor.execute(sql)
        return count

    def fetchall(self, table):
        if table is not None and table != '':
            sql = 'select * from %s' % table
            self.cursor.execute(sql)
            re = self.cursor.fetchall()
            print len(re)
        return count

    def fetchone_by_id(self, table, id):
        if table is not None and table != '':
            sql = 'SELECT * FROM %s WHERE ID = ?'%(table)
            fetchone(conn, sql, id)

    def delete_by_id(self, table, id):
        if table is not None and table != '':
            sql = 'DELETE FROM %s WHERE ID = %d' % (table, id)
            self.cursor.execute(sql)
            conn.commit()

    def delete_by_key_value(self, table, key, value):
        if table is not None and table != '':
            sql = 'DELETE FROM %s WHERE %s = %s' % (table, key, str(value))
            self.cursor.execute(sql)
            conn.commit()

    def delete_by_primary_key(self, table, value):
        if table is not None and table != '':
            if table is "account":
                key = 'account'
            elif tables is "ip":
                key = 'addr'
            elif tables is "receiver":
                key = 'email'
            else:
                print "table %s is not exist"%table
                return
            self.delete_by_key_value(table, key, value)

    def update_by_key_value(self, table, update_key, new_value, key, value):
        if table is not None and table != '':
            sql = 'UPDATE %s SET %s = %s WHERE %s = %s'%(table, update_key, str(new_value), key, str(value))
            self.cursor.execute(sql)
            conn.commit()

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
            elif tables is "ip":
                key = 'addr'
            elif tables is "receiver":
                key = 'email'
            else:
                print "table %s is not exist"%table
                return
            self.update_status_by_key_value(table, key, value, status)

    def update_map_by_id(self, table, id, map):
        if table is not None and table != '':
            if table is "account":
                key_map = 'ip_map'
            elif tables is "receiver":
                key_map = 'account_map'
            else:
                print "table %s is not exist"%table
            self.update_by_key_value(table, key_map, map, 'ID', id)

    def update_map_by_primary_key(self, table, value, map):
        if table is not None and table != '':
            if table is "account":
                key = 'account'
                key_map = 'ip_map'
            elif tables is "receiver":
                key = 'email'
                key_map = 'account_map'
            else:
                print "table %s is not exist"%table
            self.update_by_key_value(table, key_map, map, key, value)

    def insertone(self, table, new):
        row = {}
        count = self.__total_row(table)
        row['id'] = count+1 
        row['status'] = 1
        if table is "account":
            row['account'] = new['account']
            row['passwd'] = new['passwd']
            row['last_time'] = int(time.time()) 
            row['ip_map'] = []
            for i in range(256):
                row['ip_map'].append(0)
            if 
            com = row['account'][-6:]
            if com in settings.c['smtp'].keys():
                row['smtp'] = settings.c['smtp_mapping'][com]['smtp']
                row['mini_interval'] = settings.c['smtp_mapping'][com]['interval']
                row['max_times_per_day'] = settings.c['smtp_mapping'][com]['max']
            else:
                print row['account'], ' can not be config'
        elif tables is "ip":
            row['addr'] = new['addr']
        elif tables is "receiver":
            row['email'] = new['email']
            row['last_time'] = int(time.time()) 
            row['account_map'] = []
            for i in range(1024):
                row['account_map'].append(0)
        else:
            print "table %s is not exist"%table

    def drop_table(self, table):
        if table is not None and table != '':
            sql = 'DROP TABLE IF EXISTS ' + table
            self.cursor.execute(sql)
            conn.commit()

    def init_tables(self):
        for i in range(len(settings.c['db_name'])):
            self.cursor.execute(settings.c['db_name'][i]['sql'])

        conn.commit()

    def close(self):
        self.conn.close()
