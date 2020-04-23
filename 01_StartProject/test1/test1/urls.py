"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# 项目的urls文件，django2.0以前路径是使用的url，后面版本都使用path
urlpatterns = [
    path('admin/', admin.site.urls), # 配置项目，默认的后台管理请求
    # r表示一个纯字符串，''空白表示匹配任何内容，就可以匹配到index
    # 第一个参数是一个正则表达式，第二个参数是包含的应用的urls文件
    path(r'', include('booktest.urls')), # 包含booktest应用下的urls文件
]

# 访问http://127.0.0.1:8000/index网页的步骤如下：
# 1.浏览器访问网址，django会自动提取地址/后面的 index
# 2.index 先到项目下的test1/urls中的urlpatterns中依次匹配
# 3.r''可以匹配任何内容，然后进booktest.urls中继续匹配
# 4.url(r'^index', views.index)匹配成功，然后调用的是视图views.index方法
# 5.返回index方法的结果，将内容显示在网页上


# 先启动服务器：python manage.py runserver
# 然后打开上面网页：http://127.0.0.1:8000/index