# coding: UTF-8
import web
import os
import DEBUG

from config import settings

class Test:
    def __init__(self):
        self.render = settings.render 

    def GET(self):
        return self.render.test()

    def POST(self):
        data = web.input(path={}) 
        if data.limit:
            limit = int(data.limit)
            DEBUG.p('get limit: %s' % (data.limit))
        if data.album_name:
            DEBUG.p('get album name: %s' % (data.album_name))
        if data.artist_name:
            DEBUG.p('get artist_name: %s' % (data.artist_name))
        if data.country == 'deep':
            DEBUG.p('get conuntry %s' % (data.country))
        return self.render.test()
