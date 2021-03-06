from django.shortcuts import render, redirect
from django.template import loader, RequestContext
from django.http import HttpResponse,JsonResponse
from django.template.context import Context
from booktest.models import BookInfo,PicTest,AreaInfo
from django.conf import settings

# Create your views here.

# 定义一个装饰器，用来判断用户是否已经登录
# view_func就是被装饰的视图函数，*view_args, **view_kwargs是视图函数的位置参数和关键字参数
def login_required(view_func):
    '''登陆判断装饰器'''
    def wrapper(request, *view_args, **view_kwargs):
        # 判断用户是否已经登录
        if request.session.has_key('islogin'):
            # 用户已经登录，调用对应视图函数
            return view_func(request, *view_args, **view_kwargs)
        else:
            # 用户未登录跳转到首页
            return redirect('/login')
    return wrapper


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

# 模板转义
# 用于处理该url请求：http://127.0.0.1:8000/temp_escape
def temp_escape(request):
    '''模板转义'''
    content = {'content': '<h1>Hello World</h1>'}
    return render(request, 'booktest/temp_escape.html', content)

# 用于处理该url请求：http://127.0.0.1:8000/login
def login(request):
    '''显示登录页面'''
    # 判断用户是否已经登录过
    if request.session.has_key('islogin'):
        # 用户已经登录过，直接跳转到登录后页面，即跳转到index
        # return redirect('/index')
        # 跳转到修改密码页面
        return redirect('/change_pwd')
    else:
        # 用户未登录，执行下面操作，检测cookie中是否有用户名，有的话自动填写没有就是空
        # 获取cookie值中的username
        if 'username' in request.COOKIES:
            # 访问页面时候，读取浏览器保存的cookie信息，获取里面已经保存的用户名
            username = request.COOKIES.get('username')
        else:
            username = ''
        # 将获取到的username传递给前端html页面，传递给input框的username的值中
        return render(request, 'booktest/login.html', {'username': username})

# 用于处理该url请求：http://127.0.0.1:8000/login_check
def login_check(request):
    # 1.获取提交的用户名和密码
    # print(type(request.POST)) # 查看django服务器终端，里面输出了 <class 'django.http.request.QueryDict'>
    # 获取html页面input表单name属性对应标签输入的值
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember') # 如果勾选记住用户名选框，remember的值是on

    # 2.进行登陆的校验
    # 实际开发：根据用户名和密码查找数据库，进行匹配
    # 比如： smart 123456
    if username == 'smart' and password == '123456':
        # 用户名和密码正确，跳转到一个页面，此处用首页
        # response = redirect('/index') # redirect是HttpResponseRedirect的简写
        # 跳转到修改密码修改页面
        response = redirect('/change_pwd')

        # 同时继续判断是否需要记住用户名
        if remember == 'on':
            # 设置用户名作为cookie值，设置过期时间为1周,登陆一次再登陆，就提取cookie里面的用户名
            response.set_cookie('username', username, max_age=7*24*3600)

        # 6.16节案例，设置session一个islogin的值，用于记住登陆状态
        # 只要session中有islogin即可，具体设置什么值不重要，此处直接设置值为True
        request.session['islogin'] = True
        # 记录用户的登录名
        request.session['username'] = username
        return response # return要放在if记住用户名同级，如果不勾选也是直接正常登陆
    else:
        # 用户名和密码错误，跳转到登陆页面
        return redirect('/login')

    # 3.返回结果
    # return HttpResponse('OK')

# 用于处理该url请求：http://127.0.0.1:8000/change_pwd
@login_required
def change_pwd(request):
    '''显示修改密码的页面'''
    # 该网页只有用户已经登录了才能访问，通过session进行判断
    # if not request.session.has_key('islogin'):
    #     return redirect('/login')
    # 上面登陆判断封装在一个装饰器中，直接用装饰器装饰即可
    # 我们将浏览器的cookie清楚，然后再访问该页面，就会自动跳转到login页面
    return render(request, 'booktest/change_pwd.html')


# 用于处理该url请求：http://127.0.0.1:8000/change_pwd_action
@login_required
def change_pwd_action(request):
    '''修改密码处理'''
    # 1.获取输入的新密码和用户名(登陆时候已经保存在session中)
    pwd = request.POST.get('pwd')
    username = request.session.get('username')
    # 2.实际开发中：新密码去修改数据库中的内容...
    # 3.返回一个应答
    return HttpResponse('%s密码已经修改为：%s' %(username, pwd))

# 用于处理该url请求：http://127.0.0.1:8000/url_reverse
def url_reverse(request):
    '''url反向解析'''
    return render(request, 'booktest/url_reverse.html')

# 用于处理该url请求：http://127.0.0.1:8000/show_args/1/2
def show_args(request, a, b):
    '''url反向解析,捕获位置参数'''
    return HttpResponse("位置参数分别是：" + a + "和" + b)

# 用于处理该url请求：http://127.0.0.1:8000/show_kwargs/3/4
def show_kwargs(request, num1, num2):
    '''url反向解析,捕获位置参数'''
    return HttpResponse("关键字参数分别是：" + num1 + "和" + num2)

from django.urls import reverse
# 用于处理该url请求：http://127.0.0.1:8000/test_redirect
def test_redirect(request):
    # 重定向到首页
    # return redirect('/index')
    # 如果大量网页重定向到index，但是index地址发生修改，需要修改大量视图中的重定向地址
    # url反向解析动态生成,此时首页地址会自动根据urls.py里面的配置自动反向解析生成
    url = reverse('booktest:index')
    return redirect(url)

    # 重定向使用位置参数
    #     # /show_args/1/2
    #     # url = reverse('booktest:show_args', args=(1, 2))

    # 重定向使用关键字参数
    # /show_args/3/4
    # url = reverse('booktest:show_args', kwargs={'num1': 3, 'num2': 4})


# 静态文件使用
# 用于处理该url请求：http://127.0.0.1:8000/static_test
def static_test(request):
    '''静态文件使用'''
    return render(request, 'booktest/static_test.html')

# 用于处理该url请求：http://127.0.0.1:8000/index2
# 禁止访问单个网址
EXCLUDE_IPS = ['127.0.0.1']
def index2(request):
    '''首页2'''
    # 浏览器用户的ip地址
    user_ip = request.META['REMOTE_ADDR']
    # 本地访问就是127.0.0.1
    print(user_ip)
    # 可以设置禁止访问的IP地址
    if user_ip in EXCLUDE_IPS:
        return HttpResponse('<h1>用户IP禁止访问</h1>')
    else:
        return render(request, 'booktest/index2.html')

# 用于处理该url请求：http://127.0.0.1:8000/index3
def index3(request):
    '''首页3'''
    print('-----index3-----')
    return render(request, 'booktest/index3.html')

# 上传保存图片
# 用于处理该url请求：http://127.0.0.1:8000/pic_upload
def pic_upload(request):
    '''上传图片页面'''
    return render(request,'booktest/pic_upload.html')

# 用于处理该url请求：http://127.0.0.1:8000/pic_handle
def pic_handle(request):
    '''用于接收表单提交的图片保存图片'''
    # request对象的FILES属性用于接收请求的文件，包括图片

    # 1.获取表单上传的图片，获取上传文件的处理对象
    # pic是input的文件类型表单name属性的值
    f1=request.FILES.get('pic')

    # 2.创建文件保存路径
    fname='%s/booktest/%s' % (settings.MEDIA_ROOT, f1.name)

    # 3.打开文件写入上传文件的内容
    # 打开文件已二进制方式写入
    with open(fname,'wb') as pic:
        # f1.chunks()返回文件的一块内容，循环遍历获取所有内容
        for c in f1.chunks():
            pic.write(c)

    # 4.在数据库中保存上传的文件记录
    PicTest.objects.create(goods_pic='booktest/%s' % f1.name)

    # 5.返回内容
    return HttpResponse('OK,图片上传完成！')


# 分页显示地区内容
# 用于处理该url请求：http://127.0.0.1:8000/show_area/1
# pageindex 是url地址传递过来的页码参数
from django.core.paginator import Paginator
def show_area(request, pageindex):
    '''分页显示地区信息'''
    # 1.查出所有省级地区信息,省份的aParent_id的值为NULL,具体查看mysql数据表,可以简写为aParent__isnull=True
    areas = AreaInfo.objects.filter(aParent_id__isnull=True)
    # 2.分页，每页显示5条，返回Paginator类的实例对象paginator(名称自定义)
    paginator = Paginator(areas, 5)
    # 3.获取某一页的内容
    if pageindex == '':
        # 没有指定页码，获取第一页内容
        # 访问：http://127.0.0.1:8000/show_area/
        pageindex = 1
        # 注意：下面的page是Page类的实例对象，即具体某一页内容的实例对象
        # 调用Paginator实例对象即paginator的page()方法返回Page实例对象即page
        # paginator是所有分页内容的实例对象，取出某一页，得到page实例对象
        # page有很多属性，具体查看笔记里面内容和show_area.html代码
        page = paginator.page(pageindex)
    else:
        pageindex = int(pageindex)
        page = paginator.page(int(pageindex))

    # 4.使用模板
    return render(request, 'booktest/show_area.html',
                  {'areas': areas, 'page': page})


# 省市区选择
# 用于处理该url请求：http://127.0.0.1:8000/areas
def areas(request):
    '''省市区选择'''
    return render(request, 'booktest/areas.html')

# 用于处理该url请求：http://127.0.0.1:8000/prov
def prov(request):
    '''获取所有省级地区信息'''
    # 1.获取所有省级地区信息
    areas = AreaInfo.objects.filter(aParent__isnull=True)

    # 2.areas是一个查询集QuerySet,转换为json数据
    areas_list = []
    for area in areas:
        areas_list.append((area.id, area.atitle))
    # print(areas_list)
    # 下面返回为json数据时候，元组自动转变为列表，可以查看网址请求后的原始数据

    # 3.返回数据，HTML发过来是ajax请求，返回数据是json数据
    # areas是一个查询集QuerySet
    return JsonResponse({'data': areas_list})

# 市 县级 地区选择
# 用于处理该url请求：http://127.0.0.1:8000/city/pid 或者http://127.0.0.1:8000/dis/pid
def city(request, pid):
    '''获取省(pid)下级市级信息'''
    # 1.获取pid对应的下级市的信息
    # 方式1：
    # area = AreaInfo.objects.get(id=pid)
    # areas = area.areainfo_set.all()
    # 方式2：
    # 根据父级ID查询下级地区信息
    areas = AreaInfo.objects.filter(aParent__id=pid)

    # 2.变量areas并拼接出json数据：areas是一个查询集QuerySet,转换为json数据
    areas_list = []
    for area in areas:
        areas_list.append((area.id, area.atitle))

    # 3.返回数据，HTML发过来是ajax请求，返回数据是json数据
    # areas是一个查询集QuerySet
    return JsonResponse({'data': areas_list})