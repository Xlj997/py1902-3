from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import aaa,bbb

# Create your views here.

def index(request):

    return render(request,'booktest/shouye.html',{})

    # temp = loader.get_template('booktest/shouye.html')
    #
    # xur =temp.render({})
    #
    # return HttpResponse(xur)

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

def deletebook(request,id):

    aaa.objects.get(pk=id).delete()


    return HttpResponseRedirect('/a1/list')


def deletehero(request,id):

    print(id)

    ccc = bbb.objects.get(pk=id)
    cc = ccc.boot_id.id
    ccc.delete()

    return HttpResponseRedirect('/a1/xq/%s/'%(cc,))






