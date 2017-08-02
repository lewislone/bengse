# coding: UTF-8
import csv
import operator
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

	def insert_table(conn, tablename):
		
	def delete_table(conn, tablename):
		
	def delete_db(dbname):

	def update_db(conn, tablename):
'''


if __name__ == '__main__':
	c2s=csv2sqlite()	
	c2s.open_csv('./receiver.csv')
	#c2s.open_csv('/Users/liaozq/work/mail/receiver.csv')

