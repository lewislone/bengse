# coding: UTF-8
import web
from config.url import urls

app = web.application(urls, globals())

if __name__ == "__main__":
        app.run()

