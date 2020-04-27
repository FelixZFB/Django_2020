from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse
from django.template.context import Context
from booktest.models import BookInfo

# Create your views here.

# 模板使标准步骤演示
# 用于处理该url请求：http://127.0.0.1:8000/index
def index(request):
    # 1.加载模板文件(loader.get_template)，获取模板文件的内容，获取一个模板对象
    temp = loader.get_template('booktest/index.html')  # 文件夹路径是templates下开始
    # 2.定义模板上下文(RequestContext),给模板文件传递数据
    # context = RequestContext(request, {})
    # 由于版本更新问题，新的版本context必须是一个字典对象，就是要传递给模板的参数,没有参数就是空
    context = {}
    # 3.模板渲染产生html页面内容 render, 用传递的数据替换相应的变量，产生一个替换后的标准的html内容
    res_html = temp.render(context)
    # 4.返回内容给浏览器
    return HttpResponse(res_html)

    # 上面4步由于版本升级问题，在第3步报错，传入的context必须是字典对象不能是RequestContext对象
    # 参考网址：https://www.cnblogs.com/xiyu714/p/9091619.html

    # 上面4步可以直接进行以下简写，django已经封装好了一个render方法
    # 上面四步也可以定义为一个my_render方法,查看下面
    # return render(request, 'booktest/index.html', {})

def my_render(request, template_path, context={}):
    temp = loader.get_template('booktest/index.html')  # 文件夹路径是templates下开始
    context = {}
    res_html = temp.render(context)
    return HttpResponse(res_html)

# 用于处理该url请求：http://127.0.0.1:8000/index1
def index1(request):
    return my_render(request, 'booktest/index.html')

# 模板标签使用
# 用于处理该url请求：http://127.0.0.1:8000/temp_tags
def temp_tags(request):
    '''模板标签'''
    # 1. 获取所有图书,通过模型类查询
    books = BookInfo.objects.all()
    return render(request, 'booktest/temp_tags.html', {'books': books})

# 模板继承
# 用于处理该url请求：http://127.0.0.1:8000/temp_inherit
def temp_inherit(request):
    '''模板继承'''
    return render(request, 'booktest/child.html')