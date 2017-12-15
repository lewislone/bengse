# coding: UTF-8
import os
import sys
import DEBUG
import random
from random import choice
import controllers.dao as dao

class Contain:
    def __init__(self):
        self.db = dao.Dao()
        self.temp=['Temp0']
        path = os.getcwd()+'/mail/'
        sys.path.append(path)

    def __fetch_one_temp(self):
        index = choice(range(len(self.temp)))
        return 'Temp'+str(index)
        

    def get_html(self):
        tmp = self.__fetch_one_temp()
        module = __import__('temp')
        obj = getattr(module, tmp)
        handle = obj()
        print handle.format_html("test contain", 'xx@qq.com')
