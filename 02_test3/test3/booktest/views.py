from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.

# 用于处理该url请求：http://127.0.0.1:8000/index
def index(request):
    return render(request, 'booktest/index.html')

# 捕获url参数，并返回参数到页面显示
# 用于处理该url请求：http://127.0.0.1:8000/delete222
def show_arg(request,id):
    return HttpResponse('show arg %s'%id)

# 用于处理该url请求：http://127.0.0.1:8000/login
def login(request):
    '''显示登录页面'''
    return render(request, 'booktest/login.html')

# 用于处理该url请求：http://127.0.0.1:8000/login_check
def login_check(request):
    # 1.获取提交的用户名和密码
    # print(type(request.POST)) # 查看django服务器终端，里面输出了 <class 'django.http.request.QueryDict'>
    username = request.POST.get('username')  # 获取html页面表单name属性对应的值
    password = request.POST.get('password')

    # 2.进行登陆的校验
    # 实际开发：根据用户名和密码查找数据库，进行匹配
    # 比如： smart 123456
    if username == 'smart' and password == '123456':
        # 用户名和密码正确，跳转到一个页面，此处用首页
        return redirect('/index')
    else:
        # 用户名和密码错误，跳转到登陆页面
        return redirect('/login')

    # 3.返回结果
    # return HttpResponse('OK')


# http://127.0.0.1:8000/ajax_test
def ajax_test(request):
    '''显示test_ajax.html页面'''
    return render(request, 'booktest/ajax_test.html')

def ajax_handle(request):
    '''ajax请求的具体处理'''
    # 返回的json数据，字典形式，返回时候会自动转换为json格式数据
    return JsonResponse({'res': 1})


# http://127.0.0.1:8000/ajax_login
def login_ajax(request):
    '''显示ajax登陆页面'''
    return render(request, 'booktest/login_ajax.html')