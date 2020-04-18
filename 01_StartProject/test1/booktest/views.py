from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from booktest.models import BookInfo # 导入图书模型类

# Create your views here.
# 定义视图函数，必须有一个request参数，及HttpRequest对象

# 1.定义视图函数，HttpRequest
# 2.进行url配置，建立url地址和视图的对应关系
# 用于处理该url请求：http://127.0.0.1:8000/index
def index(request):
    # index请求处理方式1：直接返回内容
    # 进行处理，和M(Model 数据库交互 数据处理)和T(Template 封装返回HTML)进行交互，进行一系列处理......然后返回结果
    # return HttpResponse('此处是index返回的结果')

    # index请求处理方式2：使用模板文件
    # 1.获取模板，即加载模板文件，路径是从templates模板文件夹下开始
    # template = loader.get_template('booktest/index.html')
    # 2.定义模板上下文
    # context = RequestContext(request, {})
    # 3.模板渲染后返回给浏览器,将模板上下文渲染为标准的html文件template.render(context)返回给浏览器
    # return HttpResponse(template.render(context))

    # 上面3步可以直接使用render封装函数简写：
    context = {'title':'图书列表','list':range(10)} # context是一个字典对象，可以传入多个键和值
    # render接收三个参数：
    # 第一个参数为request对象
    # 第二个参数为模板文件路径
    # 第三个参数为字典，表示向模板中传递的上下文数据
    return render(request, 'booktest/index.html', context)


# 用于处理该url请求：http://127.0.0.1:8000/index
def index2(request):
    # 进行处理，和M(Model 数据库交互 数据处理)和T(Template 封装返回HTML)进行交互，进行一系列处理......然后返回结果
    return HttpResponse('此处是indx2返回的结果')


# 展示数据库中的图书信息
# 用于处理该url请求：http://127.0.0.1:8000/show_books
def show_books(request):
    '''显示图书的信息'''
    # 1.通过M查找图书表中的的数据
    books = BookInfo.objects.all()
    # 2.使用模板，返回要展示的内容
    return render(request, 'booktest/show_books.html', {'books':books})

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