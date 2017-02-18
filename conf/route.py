# -*- coding: utf-8 -*-
#路由映射
urls=(
	'/user/login', 'controller.user.Login',
	'/user/logout', 'controller.user.Logout',
	'/user/list', 'controller.user.List',
	'/user/add', 'controller.user.Add',
	'/user/update/(\d+)', 'controller.user.Update',

	'/', 	'controller.user.Login',
)