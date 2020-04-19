from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext
from booktest.models import BookInfo # 导入图书模型类
from datetime import date

# Create your views here.
# 展示数据库中的图书信息
# 用于处理该url请求：http://127.0.0.1:8000/index
def index(request):
    '''显示图书的信息'''
    # 1.通过M查找图书表中的的数据
    books = BookInfo.objects.all()
    # 2.使用模板，返回要展示的内容
    return render(request, 'booktest/index.html', {'books':books})

# 显示某本图书的详细信息
# 用于处理该url请求：http://127.0.0.1:8000/books/1
def detail(request, bid):
    '''查询图书详细信息'''
    # 1.根据bid查询图书详细信息，获取到book对象
    book = BookInfo.objects.get(id=bid)
    # 2.查询图书关联的所有英雄信息，通过图书book对象关联的英雄对象
    heros = book.heroinfo_set.all()
    # 3.使用模板，返回要展示的内容
    return render(request, 'booktest/detail.html', {'book':book, 'heros':heros})

# 创建新图书
# 点击新增时候，即处理url请求：http://127.0.0.1:8000/create
def create(request):
    '''新增一本图书'''
    # 1.创建BookInfo()模型对象
    book=BookInfo()
    # 2.新增一本图书
    book.btitle = '流星蝴蝶剑'
    book.bpub_date = date(1995,12,30)
    # 3.保存到数据库中
    book.save()
    # 4.不返回应答，直接转向到首页，重定向到/index
    # return HttpResponseRedirect('/index')
    # 可以直接使用以下简写，redirect内部封装了HttpResponseRedirect
    return redirect('/index')

# 逻辑删除指定编号的图书
def delete(request,bid):
    '''删除一本图书'''
    # 1.创建BookInfo()模型对象
    book=BookInfo.objects.get(id=int(bid))
    # 2.删除图书对象
    book.delete()
    # 3.不返回应答，直接转向到首页，重定向到/index
    # return HttpResponseRedirect('/index')
    return redirect('/index')