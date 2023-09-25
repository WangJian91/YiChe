from django.shortcuts import render, HttpResponse

# Create your views here.

# django中的视图函数必须带request这个参数
# 视图函数必须return，一般返回的都是要传给前端的数据


def index(request):
    return HttpResponse('Hello World!')


def add_user(request):
    return render(request, 'add_user.html')


def del_user(request):
    return render(request, 'del_user.html')


def user_list(request):
    return render(request, 'user_list.html')


