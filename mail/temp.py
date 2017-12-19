# coding: UTF-8
import os
import time
import hashlib
import socket
import struct
import random
from random import choice
import controllers.dao as dao

line = [u'TTTTTTTTTT', u'++++++++++', u'-+-+-+-+-+-', u'=-=-=-=-=-=', u'-------', u'=======', u'_______', u'........', u'********', u'#########', u'````````', u'~~~~~~~~~~', u'.....']
country_code = [u'CN', u'JP', u'US', u'KR', u'IN', u'GR', u'GB', u'FR', u'ES', u'DE', u'BY', u'RU', u'SG', u'IT']

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

def get_random_country():
    return choice(country_code)

def get_random_int(max):
    return random.randint(0, max)

def get_random_token():
    m=hashlib.md5()
    m.update(bytes(str(time.time())))
    a0 = m.hexdigest()
    m.update(bytes(str(time.time())))
    a1 = m.hexdigest()
    m.update(bytes(str(time.time())))
    a2 = m.hexdigest()
    return a0+a1+a2

def get_random_token2(len):
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ%"
    sa = []
    for i in range(len):
        sa.append(choice(seed))
    return ''.join(sa)

def get_random_code(len):
    seed = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(len):
        sa.append(choice(seed))
    return  ''.join(sa)

def get_random_ip():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

def insert_comment(old_html, db):
    count = old_html.count('>')
    index = random.randint(0, count)
    index = len(old_html.split('>', index)[-1])
    html = old_html[:-index] + "<br>" + old_html[-index:]

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

class Temp1:
    def __init__(self):
        print "Temp1 init..."
        id = get_random_int(10000)%2 + 2 
        self.tempfile = os.getcwd() + u"/templates/temp%d.htm"%id
        self.db = dao.Dao()

    #parameters: name,contain,code(B9KT7),tocken(3cf70a783ad33799e83abe02317cfd8f7ba574ff3016f47612255afe26f1e9db5d7e847ffc86ee85247d132f7ffb22fc),ip,country(CN),tocken(wJDoeuPyD9zfHUvJtkE7gRfGBKSopxbbARn%2FpwEZR0yN68Ey%2BJWfBNVtxIT1reg%2BvZHXmhDUZvcbmZEj58fjNQ%3D%3D)
    def format_html(self, contain, receiver):
        print 'temp1 start...'
        html = get_temp(self.tempfile).decode('utf-8')
        inject = insert_comment(contain, self.db)
        name = get_fromname(self.db)
        code = get_random_code(5)
        print code
        token = get_random_token()
        print token
        token2 = get_random_token2(98)
        print token2
        ip = get_random_ip()
        print ip
        country = get_random_country()
        print country
        return html%(receiver, inject, code, token, ip, country, token2)
