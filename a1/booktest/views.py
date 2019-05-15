from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import aaa,bbb

# Create your views here.

def index(request):



    temp = loader.get_template('booktest/shouye.html')

    xur =temp.render({})

    return HttpResponse(xur)

    # return HttpResponse('首页')


def list(request):

    aa = aaa.objects.all()
    # print(aa)


    temp = loader.get_template('booktest/list.html')

    xur = temp.render({'aa':aa})

    return HttpResponse(xur)

def xq(request,id):
    try:
        bb = aaa.objects.get(pk=id)
        # print(bb)

    except Exception as e:
        return HttpResponse('没有这本书')

    temp = loader.get_template('booktest/xiangqing.html')

    xur = temp.render({'bb': bb})

    return HttpResponse(xur)







