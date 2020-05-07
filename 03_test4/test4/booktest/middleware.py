# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
GihHub: https://github.com/FelixZFB
Date: 2020/5/7 16:18
Desc:
'''
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

# 中间件类
# 该类需要进settings里面的MIDDLEWARE_CLASSES注册
class BlockIPSMiddleware(MiddlewareMixin):
    EXCLUDE_IPS = ['127.0.0.1']
    # 中间件函数，名称是固定的
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        '''视图函数调用之前会调用该函数'''
        # 浏览器用户的ip地址
        user_ip = request.META['REMOTE_ADDR']
        # 可以设置禁止访问的IP地址
        if user_ip in BlockIPSMiddleware.EXCLUDE_IPS:
            return HttpResponse('<h1>用户IP禁止访问</h1>')
    # 如果执行if语句，就会继续执行视图函数
