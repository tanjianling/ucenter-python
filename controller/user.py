# -*- coding: utf-8 -*-
from ucenter.controller.controller import Controller
from ucenter.start import web
from ucenter.models import user
import json


class User(Controller):
    def __init__(self):
        # 调用controller类的构造
        super(User, self).__init__()
        self.userModel = user.User()


class Login(User):
    def GET(self):
        return self.renderBase('login', ())

    def POST(self):
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        username = web.input().get('username')
        password = web.input().get('password')
        password = self.function.md5(password)
        user = self.userModel.getUser(username=username, password=password)
        if user == []:
            msg = {
                'state': 0,
                'msg': '用户名或密码有误！'
            }
            return json.dumps(msg)
        else:
            self._registerSession(username=user[0].get('username'), name=user[0].get('name'))
            msg = {
                'state': 1,
                'msg': '%s 登录成功！ ' % (web.ctx.session.name),
                'url': '/user/list'
            }
            return json.dumps(msg)

    def _registerSession(self, **keyValue):
        web.ctx.session.username = keyValue.get('username')
        web.ctx.session.name = keyValue.get('name')


class List(User):
    def GET(self):
        if web.ctx.session.name is None:
            return web.seeother('/user/login')
        userList = self.userModel.getUserList(web.ctx.session.username)
        return self.render('center', userList)


class Logout(User):
    def GET(self):
        web.ctx.session.kill()
        web.seeother('/user/login')


class Update(User):
    def GET(self, userId):
        user = self.userModel.getUserForId(int(userId))
        if user == []:
            return web.seeother('/user/list')
        return self.render('edit', user[0])

    def POST(self, userId):
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        upData = web.input()
        # self.userModel.attributes = upData 第一种方式验证模型

        # self.userModel.validate(upData) 第二种方式验证模型

        # self.userModel.username='' 第三种方式验证模型
        # self.userModel.password='' 第三种方式验证模型
        # self.userModel.email='' 第三种方式验证模型

        #使用第一种方式验证模型
        self.userModel.attributes = upData
        self.userModel.validate()

        #如果模型有错误
        if self.userModel.validateError:
            return json.dumps(self.userModel.validateError)

        upData['password'] = self.function.md5(upData.get('password'))
        self.userModel.updateUserForId(userId, upData)


class Add(User):
    def GET(self):
        return self.render('add')

    def POST(self):
        pass
