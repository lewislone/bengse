#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import random
import netifaces as ni

true_socket = socket.socket
ipList=[]

class getLocalIps():
    global ipList
    def getLocalEthIps(self):
        for dev in ni.interfaces():
            if dev.startswith('eth1'):
                ip=ni.ifaddresses(dev)[2][0]['addr']
                if ip not in ipList:
                    ipList.append(ip)

class bindIp():
    ip=''
    global true_socket,ipList
    '''
    def bound_socket(self,*a, **k):
        sock = true_socket(*a, **k)
        sock.bind((self.ip, 0))
        return sock

    def changeIp(self,ipaddress):
        self.ip=ipaddress
        if not self.ip=='':
            socket.socket = self.bound_socket
        else:
            socket.socket = true_socket
    '''
    def randomIp(self):
        if len(ipList)==0:
            getLocalIpsFunction=getLocalIps()
            getLocalIpsFunction.getLocalEthIps()
        if len(ipList)==0:
            return
        _ip=random.choice(ipList)
        print "$$$$$$$$$$$$"
        print _ip
        self.ip=_ip
        #if not _ip==self.ip:
            #self.changeIp(_ip)

    def getIp(self):
        return self.ip

    def getIpsCount(self):
        return len(ipList)



if __name__ == '__main__':
    bindIpObj=bindIp()
#随机切换IP
    bindIpObj.randomIp()
#得到当前IP
    print bindIpObj.getIp()
#得到本机IP数
    print bindIpObj.getIpsCount()
#切换到指定IP
    #print bindIpObj.changeIp('xxx.xx.xx.xxx')
