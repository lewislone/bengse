# coding: UTF-8
import os
import random
from random import choice
import controllers.dao as dao

line = [u'TTTTTTTTTT', u'++++++++++', u'-+-+-+-+-+-', u'=-=-=-=-=-=', u'-------', u'=======', u'_______', u'........', u'********', u'#########', u'````````', u'~~~~~~~~~~', u'.....']

def get_temp(tempfile):
    with open(tempfile) as f:
        return f.read()

def get_fromname(db):
    name = db.get_random('names')
    #DEBUG.pd(name)
    return name[0][1]

def get_quote(db):
    quote = db.get_random('quotes')
    #DEBUG.pd(quote)
    return quote[0][1]
    
def get_subject(db):
    subject = db.get_random('subjects')
    #DEBUG.pd(subject)
    return subject[0][1]

def get_toname(db):
    name = db.get_random('names')
    #DEBUG.pd(name)
    return name[0][1]

def get_line():
    return choice(line)

def insert_comment(old_html, db):
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
    html = html[:-index] + "<a hidden>" + get_toname(db) + "</a>" + html[-index:]

    count = html.count('>')
    index = random.randint(0, count)
    index = len(html.split('>', index)[-1])
    html = html[:-index] + '<span style="visibility:hidden">' + get_quote(db) + get_quote(db) + "</span>" + html[-index:]

    count = html.count('>')
    index = random.randint(0, count)
    index = len(html.split('>', index)[-1])
    html = html[:-index] + '<span style="visibility:hidden">' + get_quote(db) + "</span>" + html[-index:]

    count = html.count('>')
    index = random.randint(0, count)
    index = len(html.split('>', index)[-1])
    html = html[:-index] + "<p hidden>" + get_toname(db) + "</p>" + html[-index:]

    count = html.count('>')
    index = random.randint(0, count)
    index = len(html.split('>', index)[-1])
    html = html[:-index] + "<p hidden>" + get_toname(db) + "</p>" + html[-index:]

    count = html.count('>')
    index = random.randint(0, count)
    index = len(html.split('>', index)[-1])
    html = html[:-index] + '<div style="display:none;">' + get_quote(db) + "</div>" + html[-index:]

    count = html.count('>')
    index = random.randint(0, count)
    index = len(html.split('>', index)[-1])
    html = html[:-index] + '<div>' + "</div>" + html[-index:]

    count = html.count('>')
    index = random.randint(0, count)
    index = len(html.split('>', index)[-1])
    html = html[:-index] + '<div>' + "</div>" + html[-index:]
    return html

class Temp0:
    def __init__(self):
        print "Temp0 init..."
        self.tempfile = os.getcwd() + u"/templates/temp1.htm"
        self.db = dao.Dao()

    def format_html(self, contain, receiver):
        print 'temp0 start...'
        temp = get_temp(self.tempfile)
        #print temp
        name = get_fromname(self.db)
        #contain = u'Hi %s, sorry, this quote si for you, thank for you help'%name
        fromname = get_fromname(self.db)
        homeurl=u'wwww.%s.com'%fromname
        quote = get_quote(self.db)
        line = get_line()
        hi = u'亲爱的【%s】 您好：'%receiver[:receiver.index('@')]
        html = temp%(hi, contain, line, quote, homeurl, fromname)
        return insert_comment(html, self.db)
        #return temp%(hi, contain, line, quote, homeurl, fromname)

