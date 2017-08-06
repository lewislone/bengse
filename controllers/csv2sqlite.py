# coding: UTF-8
import csv
import os
import sqlite3
from config import settings

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
	def open_csv(self, csvfile):
		with  open(csvfile, 'rb') as handle:
			#print csv.reader(handle)
			for rows in ipager(csv.reader(handle,delimiter=','), 1):
				print rows
		'''
		cf=open(csvfile, 'rb')
		self.DictReader=csv.DictReader(cf)
		print self.DictReader
		'''
	def create_db(dbname):
		#with sqlite3.connect(dbname) as conn:
    		#	cursor = conn.cursor()
		self.dbConn = sqlite3.connect(dbname)

	def close_db(dbname):
		self.dbConn.close()

	def execute_script(self, cur, sqlscript):
        	return cur.executescript(sqlscript)

	def execute_sql_script(self, sqlScript):
        	cur = None
        	try:
            		cur = self.dbConn.cursor()
            		self.execute_script(cur, sqlScript)
            		self.dbConn.commit()
        	finally :
            		if cur :
                		self.dbConn.rollback()

	def execute_sql_string(self, sqlString, parameters=None):
        	cur = None
        	try:
            		cur = self._dbConn.cursor()
            		self.executemany_sql(cur, sqlString, parameters)
            		self.dbConn.commit()
        	finally :
            		if cur :
                		self.dbConn.rollback()

    	def create_table(self, tableName, fields):
        	#fields = ",".join(self._fields())
        	sqlString = """DROP TABLE IF EXISTS [{0}];
                	CREATE TABLE [{0}] ({1});""".format(tableName, fields)
        	self.execute_sql_script(sqlString)

	def execute_sql(self, cur, sqlStatement):
		return cur.execute(sqlStatement)

	def executemany_sql(self, cur, sqlStatement, parameters=None):
		return cur.executemany(sqlStatement, parameters)
'''
	def select_table(conn, tablename):
		sqlString = """
                	SELECT *  FROM TABLE [{0}];""".format(tableName)
        	self.execute_sql_script(sqlString)


	def insert_table(conn, tablename, fields):
		
	def delete_table(conn, tablename, fields):
		
	def delete_db(dbname):

	def update_db(conn, tablename):
'''

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
	#c2s=csv2sqlite()	
	#c2s.open_csv('./receiver.csv')
	#c2s.open_csv('/Users/liaozq/work/mail/receiver.csv')

    loader = csvSQLiteConvert(setting.c['db_url'])
    loader.loadCSVtoTable('./tmp/receiver.csv', 'receiver')
    loader.loadCSVtoTable('./tmp/account.csv', 'account')
    loader.close()

