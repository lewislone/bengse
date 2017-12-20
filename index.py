# coding: UTF-8
import os
import sys
import affinity
from config.url import urls
sys.path.insert(0,'./lib/webpy')
import web

app = web.application(urls, globals())

if __name__ == "__main__":
        pid = os.getpid()
        print affinity.get_process_affinity_mask(pid)
        affinity.set_process_affinity_mask(pid, 2)
        print affinity.get_process_affinity_mask(pid)
        app.run()

