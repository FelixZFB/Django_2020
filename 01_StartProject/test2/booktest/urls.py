# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
GihHub: https://github.com/FelixZFB
Date: 2020/4/18 15:39
Desc:
'''

from django.conf.urls import url
# 此处导入注意，由于test1和test2项目文件都标记为了source root
# 此处搜索booktest时候开始按循序先搜到了test1文件中的，然后导入的views就是test1中的
# 解决方法，不同项目尽量不要使用相同的名称，可以避免
# 折中方法：先取消test1文件夹标记，test2标记，test1标记时候取消test2标记
from booktest import views


# 应用urls文件中的配置时候注意：
# 1.严格匹配url地址的开头和结尾
# http://127.0.0.1:8000/index 从主页/之后开始匹配

urlpatterns = [
    # r表示一个纯字符串，^表示从字符串开头开始匹配
    # 第一个参数是一个正则表达式，第二个参数网址匹配成功后调用的处理方法
    url(r'^index$', views.index), # 建立url和视图函数的联系
    url(r'^books/(\d+)$', views.detail), # 显示图书详细信息,正则表达式中的分组会自动作为参数传给views.detail视图中的参数，此处数字传给参数bid
    url(r'^create$', views.create), # 新增一本图书信息
    url(r'^detele/(\d+)$', views.delete), # 删除一本图书，图书id作为参数传递
]


# 注意：匹配时候urlpatterns中的表达式匹配网址提取的内容
# 并且从上往下匹配，匹配到一个就结束匹配
# 如果访问index2，我们用表达式中的index去匹配index2也是正确匹配的
# 因此我们需要严格匹配，匹配字符串开头^到结尾$,保证一致性

# 访问http://127.0.0.1:8000/index网页的步骤如下：
# 1.浏览器访问网址，django会自动提取地址后面的 index
# 2.index 先到项目下的test2/urls中的urlpatterns中依次匹配
# 3.r''可以匹配任何内容，然后进booktest.urls中继续匹配
# 4.url(r'^index', views.index)匹配成功，然后调用的是视图views.index方法
# 5.返回index方法的结果，将内容显示在网页上

# 先启动服务器：python manage.py runserver
# 然后打开上面网页：http://127.0.0.1:8000/index