# coding: UTF-8
import csv
import os
import sqlite3
import dao

#read pagesize at a time
def ipager(serial, pagesize):
	buff = []
	for row in serial:
		buff.append(row)
		if(len(buff)) >= pagesize:
			send,buff, = buff, []
			yield send
	if(len(buff)):
		yield buff


class csv2sqlite:
    def __init__(self, csvfile):
        self.csvfile = csvfile 
        self.db = dao.Dao()
        self.db.init_tables()

    def __readFile(self):
        try:

            csv.register_dialect('lines', quotechar="'", delimiter=',',
                     quoting=csv.QUOTE_NONNUMERIC, skipinitialspace=True)

            #This will make sure to close file even if exception is raised
            with open(self.csvfile, 'rb') as f:
                reader = csv.DictReader(f)
                for row in reader:
                # treat the file object as an iterable,and automatically
                # use buffered IO and memory management to help with large files
                    yield row
        except Exception as e:
            #print "I/O error({0}): {1}".format(e.errno, e.strerror)
            print e
            print "File {} NOT found".format(self.csvfile)

    def csv2db(self, type):
        fd = open(self.csvfile, 'rb')
        self.db.db_transaction()
        for row in self.__readFile():
            #print row.keys()
            #print row.values()
            if type is 6: #quotes
                new = {row.keys()[0]:row.values()[0]}
                self.db.insertone('quotes', new)
            if type is 5: #randoms
                new = {row.keys()[0]:row.values()[0]}
                self.db.insertone('randoms', new)
            if type is 4: #subjects
                #new = {row.keys()[0]:row.values()[0]}
                new = {'subject':row.values()[0]}
                self.db.insertone('subjects', new)
            if type is 3: #names
                new = {row.keys()[0]:row.values()[0]}
                self.db.insertone('names', new)
            if type is 2: #account
                #if row.values()[0][-6:] == 'qq.com':
                if len(row.keys()) > 2:
                    new = {row.keys()[0]:row.values()[0], row.keys()[1]:row.values()[1], row.keys()[2]:row.values()[2]}
                else:
                    new = {row.keys()[0]:row.values()[0], row.keys()[1]:row.values()[1]}
                self.db.insertone('account', new)
            if type is 1: #receiver
                new = {row.keys()[0]:row.values()[0]}
                self.db.insertone('receiver', new)
            if type is 0: #ip
                new = {row.keys()[0]:row.values()[0]}
                self.db.insertone('ip', new)
        self.db.db_commit()
        fd.close()

    def close_db(self):
        self.db.close()


class csvSQLiteConvert:
    '''

    This class takes a csv file and puts the contents into an SQLite database table.
    This pre--population is important in cases where you have to convert a csv file into an SQLite database and also
    when there is the need to have a prepopulated SQLite DB to use as a resource in mobile development.

    '''

    def __init__(self, SQLiteDBfileName='csvSQLiteloader.db'):
        '''
        Initialise CSQliteloader Class

        :param SQLiteDBfileName:
        :return:
        '''

        #remove any previously created file to avoid conflicts
        try:
            os.remove(self.__fullFilename(SQLiteDBfileName))
        except OSError:
            pass

        #Initialise connection and Class Variables
        self.SQLiteDBfileName = SQLiteDBfileName
        self.conn = sqlite3.connect(SQLiteDBfileName)
        self.cursor = self.conn.cursor()
        self.tableFields = []


    def __insertRow(self, tableName, rowDict):
        '''
        Insert a single row into DB

        :param tableName:
        :param rowDict:
        :return:
        '''

        #Quote values to allow smooth insertion of values
        row = ['"'+v.strip().strip('"')+'"' for v in rowDict.values()]

        #Create sql statement to insert data into database table
        statement = "insert into %s (%s) values (%s)" %(tableName, ", ".join(self.tableFields), ", ".join(row))
        print(statement)
        self.cursor.execute(statement)


    def __createTable(self, tableName):

        '''
        Creates tables based on names of tables and fields

        :param tableName:
        :return:
        '''

        #Create sql statement to create database table
        print 'Table with name: %s created' % tableName
        print self.tableFields
        statement = 'CREATE TABLE IF NOT EXISTS %s (%s text primary key);' %(tableName, " text,".join(self.tableFields))
        #statement = 'CREATE TABLE IF NOT EXISTS %s (_id integer primary key,%s text);' %(tableName, " text,".join(self.tableFields))
        print 'Table with name: %s created' % tableName
        self.cursor.execute(statement)


    def __fullFilename(self, filename):
        '''
        Get full file path

        :param filename:
        :return:
        '''
        return os.path.dirname(os.path.realpath(__file__))+'/'+filename


    def __readFile(self, csvPath):
        '''
        Reads contents of CSV files

        :param csvPath:
        :return:
        '''

        try:

            csv.register_dialect('lines', quotechar="'", delimiter=',',
                     quoting=csv.QUOTE_NONNUMERIC, skipinitialspace=True)

            #This will make sure to close file even if exception is raised
            with open(csvPath, 'rb') as f:
                reader = csv.DictReader(f)
                for row in reader:
                # treat the file object as an iterable,and automatically
                # use buffered IO and memory management to help with large files
                    yield row
        except Exception as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
            print "File {} NOT found".format(csvPath)
            exit()


    def setTableFields(self,csvFile, customFields = []):

        '''
            Initialise list of fields; If list is not available use first row of csv
        :param fields:
        :return:
        '''

        if len(customFields) == 0:

            for row in self.__readFile(csvFile):
                self.tableFields = row.keys()
                break
        else:
            self.tableFields = customFields


    def loadCSVtoTable(self, csvFile, tableName):

        '''
        Load data into SLQlite Database
        :return:
        '''

        #set table fields from CSV it is not explicitly set
        self.setTableFields(csvFile)

        #Create Database table and make it ready for insertion of data
        self.__createTable(tableName)

        #Read and insert each live in to the created table
        for row in self.__readFile(csvFile):
            self.__insertRow(tableName, row)

        #commit records when done
        self.conn.commit()


    def close(self):
        self.conn.close()
        print('Connection Closed')


if __name__ == '__main__':
	c2s=csv2sqlite('./tmp/account.csv')	
	c2s.csv2db(2)

    #loader = csvSQLiteConvert(setting.c['db_url'])
    #loader.loadCSVtoTable('./tmp/receiver.csv', 'receiver')
    #loader.loadCSVtoTable('./tmp/account.csv', 'account')
    #loader.close()

