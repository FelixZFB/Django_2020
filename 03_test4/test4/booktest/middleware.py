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

# 中间件类，需要继承MiddlewareMixin类
# 该类需要进settings里面的MIDDLEWARE_CLASSES注册
class BlockIPSMiddleware(MiddlewareMixin):
    # 测试完成后，我们将IP地址修改掉，不然本地IP所有网页都不能访问了
    # EXCLUDE_IPS = ['127.0.0.1']
    EXCLUDE_IPS = ['128.0.0.1']
    # 中间件函数，名称是固定的
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        '''视图函数调用之前会调用该函数'''
        # 浏览器用户的ip地址
        user_ip = request.META['REMOTE_ADDR']
        # 可以设置禁止访问的IP地址
        if user_ip in BlockIPSMiddleware.EXCLUDE_IPS:
            return HttpResponse('<h1>用户IP禁止访问</h1>')
    # 如果执行if语句，就会继续执行视图函数

class TestMiddleware(MiddlewareMixin):
    '''中间件类'''
    # def __init__(self):
    #     '''服务器重启之后，接收第一个请求时候调用该函数'''
    #     print('-----init-----')

    def process_request(self, request):
        '''在产生request对象，进行url匹配之前调用该函数'''
        print('-----process_request-----')
        # 此处可以直接返回response对象，后面要执行的函数就直接跳过了,网页页面直接显示该处返回的内容
        # return HttpResponse('-----process_request-----')

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        '''url匹配之后，调用视图函数之前调用该函数'''
        # view_func，视图函数名称，后面是视图函数的位置参数和关键字参数
        print('-----process_view-----')
        # 此处可以直接返回response对象，后面要执行的函数就直接跳过了,网页页面直接显示该处返回的内容
        # return HttpResponse('-----process_view-----')

    def process_response(self, request, response):
        '''视图函数调用之后，内容返回给浏览器之前调用该函数'''
        print('-----process_response-----')
        # 该函数调用后需要有返回值，此处默认直接返回视图函数处理后的response
        return response

    def process_exception(self, request, exception):
        '''视图函数出现异常，会调用这个函数'''
        pass