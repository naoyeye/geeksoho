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
# from jinja2 import Environment,FileSystemLoader
from web.contrib.template import render_jinja

render = render_jinja(
    'templates',   # 设置模板路径.
    encoding = 'utf-8', # 编码.
)

# def render_template(template_name, **context):
#     extensions = context.pop('extensions', [])
#     globals = context.pop('globals', {})

#     jinja_env = Environment(
#             loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
#             extensions=extensions,
#             )
#     jinja_env.globals.update(globals)
#     return jinja_env.get_template(template_name).render(context)



urls = (
    '/',         'index',
    '/test',     'test'
)

# def pjax(template):
#     """Test whether the request was with PJAX or not."""
#     if web.ctx.environ.get('HTTP_X_PJAX'):
#         return render_template(template)
#     else:
#         return render_template("layout.html", template=template)


class index:
    """Home"""
    def GET(self):
        # return pjax('jobs.html')
        return render.jobs()

class test:
    """test"""
    def GET(self):
        # return pjax('test.html')
        return render.test()

app = web.application(urls, globals())
web.config.debug = True
session = web.session.Session(app, rediswebpy.RedisStore(), initializer={'count': 0})

if __name__ == "__main__":
    
    # web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()