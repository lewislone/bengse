#coding: UTF-8
import sys, os
import lib.ownsmtplib as smtplib
import DEBUG

def func_test(var):
    ip = "192.168.1.8"
    smtp_server = "smtp.163.com"
    server = smtplib.SMTP(ip, smtp_server, 25)
    print var

def new_file(path):
    f = open(path, "w")
    f.close()

if __name__ == '__main__':
    #make_dir()
    new_file("xxoo")

