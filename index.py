# coding: UTF-8
import sys
sys.path.insert(0,'./utils/webpy')
#sys.path.insert(0,'/home/ubuntu/.test/webpy')
#sys.path.append('/home/ubuntu/.test/webpy')
#sys.path.append('/home/ubuntu/.test/webpy')
#sys.path.append('/home/ubuntu/.test/webpy0.37/web')
import web
from config.url import urls

app = web.application(urls, globals())

if __name__ == "__main__":
        app.run()

