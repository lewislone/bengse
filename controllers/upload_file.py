#-*-coding:utf-8-*-
import os
import sys
import json
from config import settings
sys.path.insert(0,'../lib/webpy')
import web

web.config.debug = True

class UploadFile:
	def __init__(self):
        	self.render = settings.render
	""" 文件上传 """
	def GET(self):
		return self.render.file_upload()

	def POST(self):
        return web.seeother('/upload')

if __name__ == "__main__":
	app.run()

