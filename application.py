#!/usr/bin/env python
# -*- coding: utf-8 -*-

# author: J.Y Han

# start
# spawn-fcgi -d /users/hanjiyun/project/geeksoho -f /users/hanjiyun/project/geeksoho/application.py -a 127.0.0.1 -p 9001

#stop
# kill `pgrep -f "/users/hanjiyun/project/geeksoho/application.py"`


import os
import web
import rediswebpy
from web.contrib.template import render_jinja
import misc


db = web.database(dbn='mysql', db='geeksoho', user='geeksoho', passwd='geeksoho')



urls = (
    '/',         'index',
    '/test',     'test'
)



# controllers
# ===============
class index:
    """Home"""
    def GET(self):
        # return pjax('jobs.html')
        jobsList = GetJobs()
        return render.jobs(jobsList=jobsList)

    def POST(self):
        data = web.input(title='', link='', company='', company_weibo='', company_website='', city='', salary='', intro='')
        CreatNewJob(data)
        raise web.seeother('/')

class test:
    """test"""
    def GET(self):
        # return pjax('test.html')
        return render.test()


# models
# =============

def CreatNewJob(data):

    db.insert(
        'jobs',
        title = data.title,
        link = data.link,
        company = data.company,
        company_weibo = data.company_weibo,
        company_website = data.company_website,
        city = data.city,
        salary = data.salary,
        intro = data.intro)


def GetJobs():
    return  db.select('jobs', limit = 100, order='id DESC')





# globals = get_all_functions(misc)
app = web.application(urls, globals())
web.config.debug = True
cache = False
session = web.session.Session(app, rediswebpy.RedisStore(), initializer={'count': 0})

render = render_jinja(
    'templates',   # 设置模板路径.
    encoding = 'utf-8', # 编码.
    
)

myFilters = {'filter_tags': misc.filter_tags,}

render._lookup.filters.update(myFilters)



if __name__ == "__main__":
    
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()