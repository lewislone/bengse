# coding: UTF-8
import os

class Template:
    def __init__(self, tempfile):
        if os.path.exists(tempfile):
            self.tempfile = tempfile
        else:
            self.tempfile = os.getcwd() + u"/tempfile/temp1.htm"


    def __get_temp(self):
        with open(self.tempfile) as f:
            return f.read()
        
    def get_subject(self):
        return u'3Q'

    def get_toname(self):
        return 'lll'

    def get_fromname(self):
        return 'suinrain'

    def get_html(self):
        temp = self.__get_temp()
        print temp
        contain = u'Hi lll, sorry, this attachment is ok, 3Q for you help, and your ice'
        fromname = self.get_fromname()
        return temp%(contain, '名人名言', 'www.lll.com', fromname)
