# -*- coding: utf-8 -*-
from ucenter.conf import template
from ucenter.library.func import Function
from ucenter.start import web


class Controller(object):
    def __init__(self):
        # 获取模板实例
        self._baseRender = web.template.render(template.viewPath, globals={'session': web.ctx.session})
        self._render = web.template.render(template.viewPath, globals={'session': web.ctx.session},
                                           base=template.viewLayout)

        # 实例公共类
        self.function = Function()

    # 渲染带主题的模板
    def render(self, templateName, *params):
        exec '_callFunc=self._render.%s' % (templateName)
        return _callFunc(*params)

    # 渲染不带主题的模板
    def renderBase(self, templateName, *params):
        exec '_callFunc=self._baseRender.%s' % (templateName)
        return _callFunc(*params)
