# -*- coding: utf-8 -*-
from model import Model
import web


class User(Model):
    tableName = 'users'

    property = (
        'user_id',
        'username',
        'password',
        'name',
        'email',
        'qq',
        'phone',
        'status',
        'login_count',
    )

    #模型数据验证
    rules =(
        ['username, password, email, phone', 'required', {'name': '', 'msg': '%s必填项'}],
        ['username', 'match', r'^\w{5,20}$', {'name': '用户名', 'msg': '%s格式不正确'}],
        ['password', 'match', r'[^\n|\r|\t|\f|\b]{5,20}', {'name': '密码', 'msg': '%s格式不正确'}],
        ['password2', 'validate_password', {'name': '', 'msg': '%s两次输入密码不一样'}],
        ['email', 'email', {'name': '电子邮箱', 'msg': '%s格式不正确'}],
        ['phone', 'mobile', {'name': '手机号', 'msg': '%s格式不正确'}],
        ['qq', 'qq', {'name': 'QQ号', 'msg': '%s格式不正确'}],
    )

    #验证两次密码是否相等
    def validate_password(self, keyValue, compareKeyValue):
        if keyValue.get('password2') != compareKeyValue.get('password'):
            self.appendValidateError('password2')

    # 根据用户名和密码查询用户
    def getUser(self, **keyValue):
        if 'username' not in keyValue:
            return ''
        elif 'password' not in keyValue:
            return ''
        try:
            result = self.db.select('users',
                                    {'username': keyValue.get('username'), 'password': keyValue.get('password')},
                                    where='username=$username and password=$password')
        except Exception, e:
            print 'mysql query error:' + e.__str__()
            return False
        else:
            return result.list()

    # 根据用户名查询用户列表
    def getUserList(self, eliminate):
        if eliminate is None:
            return
        else:
            try:
                result = self.db.select('users', {'username': eliminate}, where='username!=$username')
            except Exception, e:
                print 'mysql query error:' + e.__str__()
                return False
            else:
                return result.list()

    # 根据用户id查询用户
    def getUserForId(self, userId):
        try:
            result = self.db.select('users', {'user_id': userId}, where='user_id=$user_id')
        except Exception, e:
            print 'mysql query error:' + e.__str__()
            return False
        else:
            return result.list()

    # 根据用户id查询用户
    def updateUserForId(self, userId, params):
        try:
            result = self.db.update('users', where='user_id=%s' % (userId), fields=params)
        except Exception, e:
            print 'mysql update error:' + e.__str__()
            return False
        else:
            return result
