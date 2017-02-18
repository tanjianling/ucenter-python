# -*- coding: utf-8 -*-
import sys
import web

from ucenter.conf import route

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

# 载入路由，实例化app
app = web.application(route.urls, globals())

# 使用磁盘文件存储session
session = web.session.Session(app, web.session.DiskStore('sessions'))


# 用webhook 重写session，默认的好像不好使
def session_hook():
    web.ctx.session = session


app.add_processor(web.loadhook(session_hook))

# 关闭debug模式，要不session不能用
web.config.debug = False

if __name__ == '__main__':
    app.run()
