# coding: UTF-8
import sys
from config.url import urls
sys.path.insert(0,'./lib/webpy')
import web

app = web.application(urls, globals())

if __name__ == "__main__":
        app.run()

