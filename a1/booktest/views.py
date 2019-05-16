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


def addhero(request,id):
    if request.method =='GET':
        bb = bbb.objects.get(pk=id)
        bb1 = bb.boot_id
        return render(request, 'booktest/addhero.html', {'book': bb1, 'bookid': id})
    elif request.method =='POST':
        bbbb = bbb.objects.get(pk=id)
        print(id)
        hero = bbb()
        hero.name = request.POST['username']
        hero.gender = request.POST['sex']
        hero.skill = request.POST['skill']
        hero.boot_id = bbbb.boot_id
        hero.save()
        return HttpResponseRedirect('/a1/xq/%s'%(bbbb.boot_id.id))


def addbook(request):
    if request.method == 'GET':
        aa = aaa.objects.all()
        return render(request, 'booktest/addbook.html')

    elif request.method == 'POST':
        book = aaa()
        book.title = request.POST['bookname']
        book.pub_date = request.POST['time']
        book.save()
        return HttpResponseRedirect('/a1/list/')


def upbook(request):
    if request.method =='GET':
        return render(request,'booktest/upbook.html')
    else:
        try:
            aa = aaa.objects.get(title=request.POST['name'])

            aa.title = request.POST['xname']
            aa.save()
            return HttpResponseRedirect('/a1/list')
        except Exception as e:
            return HttpResponse('没有这本书')

def uphero(request,id):
    if request.method =='GET':

        bb = bbb.objects.get(pk=id)

        if bb.gender=='wan':
            cc = '男'
        else:
            cc = '女'


        return render(request, 'booktest/uphero.html', {'bb': bb,'cc':cc})
    elif request.method =='POST':

        bb = bbb.objects.get(pk=id)
        dd = bb.boot_id.id
        try:

            aa = aaa.objects.get(title=request.POST['book'])

            bb.boot_id = aa

        except Exception as e:
            pass

        bb.name = request.POST['heroname']

        if request.POST['gender'] != bb.gender:

            if request.POST['gender'] == '男':
                bb.gender = 'wan'
            elif request.POST['gender'] == '女':
                bb.gender = 'women'
            else:
                pass

        bb.skill = request.POST['skill']

        bb.save()

        return HttpResponseRedirect('/a1/xq/%s'%(dd))



