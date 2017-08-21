# coding: UTF-8
import os
import DEBUG
import controllers.dao as dao

class Template:
    def __init__(self, tempfile):
        self.db = dao.Dao()
        #self.db.init_tables()
        if os.path.exists(tempfile):
            self.tempfile = tempfile
        else:
            self.tempfile = os.getcwd() + u"/tempfile/temp1.htm"


    def __get_temp(self):
        with open(self.tempfile) as f:
            return f.read()

    def get_quote(self):
        quote = self.db.get_random('quotes')
        DEBUG.pd(quote)
        return quote[0][1]
        
    def get_subject(self):
        subject = self.db.get_random('subjects')
        DEBUG.pd(subject)
        return subject[0][1]

    def get_toname(self):
        name = self.db.get_random('names')
        DEBUG.pd(name)
        return name[0][1]

    def get_fromname(self):
        name = self.db.get_random('names')
        DEBUG.pd(name)
        return name[0][1]

    def get_html(self):
        temp = self.__get_temp()
        print temp
        contain = u'Hi lll, sorry, this attachment is ok, 3Q for you help, and your ice'
        fromname = self.get_fromname()
        return temp%(contain, '名人名言', 'www.lll.com', fromname)

if __name__ == '__main__':
    temp = Template()
    temp.get_subject()
