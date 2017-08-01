#-*-coding:utf-8-*-
import os
import json

from config import settings
import web

web.config.debug = True

class UploadFile:
	def __init__(self):
        	self.render = settings.render 
	""" 文件上传 """
	def GET(self):
		return self.render.file_upload()

	def POST(self):
		x = web.input(file_upload={})
		#FIXME, save path#
        	filedir = '/Users/work/mail/' # change this to the directory you want to store the file in.
        	if 'file_upload' in x: # to check if the file-object is created
            		filepath=x.file_upload.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            		filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
			try:
            			fout = open(filedir +'/'+ filename,'w') # creates the file where the uploaded file should be stored
            			fout.write(x.file_upload.file.read()) # writes the uploaded file to the newly created file.
            			fout.close() # closes the file, upload complete.
            		except Exception, e:
				traceback.print_exc()
				json.dumps({'success':0, 'msg':u'文件上传失败！ %s...' % e[1]})
			else:
				json.dumps({'success':1, 'msg':u'文件上传成功！'})


        	raise web.seeother('/upload')

if __name__ == "__main__":
	app.run()

