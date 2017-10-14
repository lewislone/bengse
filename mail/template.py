# coding: UTF-8
import os
import DEBUG
import controllers.dao as dao
import random
from random import choice

class Template:
    def __init__(self, tempfile):
        self.db = dao.Dao()
        #self.db.init_tables()
        self.line = [u'TTTTTTTTTT', u'++++++++++', u'-+-+-+-+-+-', u'=-=-=-=-=-=', u'-------', u'=======', u'_______', u'........', u'********', u'#########', u'````````', u'~~~~~~~~~~', u'.....']
        if os.path.exists(tempfile):
            self.tempfile = tempfile
        else:
            self.tempfile = os.getcwd() + u"/tempfile/temp1.htm"


    def __get_temp(self):
        with open(self.tempfile) as f:
            return f.read()

    def get_quote(self):
        quote = self.db.get_random('quotes')
        #DEBUG.pd(quote)
        return quote[0][1]
        
    def get_subject(self):
        subject = self.db.get_random('subjects')
        #DEBUG.pd(subject)
        return subject[0][1]

    def get_toname(self):
        name = self.db.get_random('names')
        #DEBUG.pd(name)
        return name[0][1]

    def get_fromname(self):
        name = self.db.get_random('names')
        #DEBUG.pd(name)
        return name[0][1]

    def get_line(self):
        return choice(self.line)

    def insert_comment(self, old_html):
        count = old_html.count('>')
        index = random.randint(0, count)
        index = len(old_html.split('>', index)[-1])
        html = old_html[:-index] + "<br>" + old_html[-index:]

        count = html.count('>')
        index = random.randint(0, count)
        index = len(html.split('>', index)[-1])
        html = html[:-index] + "<br>" + html[-index:]

        count = html.count('>')
        index = random.randint(0, count)
        index = len(html.split('>', index)[-1])
        html = html[:-index] + "<a hidden>" + self.get_toname() + "</a>" + html[-index:]

        count = html.count('>')
        index = random.randint(0, count)
        index = len(html.split('>', index)[-1])
        html = html[:-index] + '<span style="visibility:hidden">' + self.get_quote() + self.get_quote() + "</span>" + html[-index:]

        count = html.count('>')
        index = random.randint(0, count)
        index = len(html.split('>', index)[-1])
        html = html[:-index] + '<span style="visibility:hidden">' + self.get_quote() + "</span>" + html[-index:]

        count = html.count('>')
        index = random.randint(0, count)
        index = len(html.split('>', index)[-1])
        html = html[:-index] + "<p hidden>" + self.get_toname() + "</p>" + html[-index:]

        count = html.count('>')
        index = random.randint(0, count)
        index = len(html.split('>', index)[-1])
        html = html[:-index] + "<p hidden>" + self.get_toname() + "</p>" + html[-index:]

        count = html.count('>')
        index = random.randint(0, count)
        index = len(html.split('>', index)[-1])
        html = html[:-index] + '<div style="display:none;">' + self.get_quote() + "</div>" + html[-index:]

        count = html.count('>')
        index = random.randint(0, count)
        index = len(html.split('>', index)[-1])
        html = html[:-index] + '<div>' + "</div>" + html[-index:]

        count = html.count('>')
        index = random.randint(0, count)
        index = len(html.split('>', index)[-1])
        html = html[:-index] + '<div>' + "</div>" + html[-index:]
        return html


    def get_html(self, contain, receiver):
        temp = self.__get_temp()
        #print temp
        name = self.get_fromname()
        #contain = u'Hi %s, sorry, this quote si for you, thank for you help'%name
        fromname = self.get_fromname()
        homeurl=u'wwww.%s.com'%fromname
        quote = self.get_quote()
        line = self.get_line()
        hi = u'亲爱的【%s】 您好：'%receiver[:receiver.index('@')]
        html = temp%(hi, contain, line, quote, homeurl, fromname)
        return self.insert_comment(html)
        #return temp%(hi, contain, line, quote, homeurl, fromname)

if __name__ == '__main__':
    temp = Template()
    temp.get_subject()
