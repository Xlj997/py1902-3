from django.conf.urls import url
from . import views


app_name = 'booktest'


urlpatterns = [
    url(r'^list/$',views.list,name='list'),
    url(r'^index/$', views.index,name='index'),
    url(r'^xq/(\d+)/$', views.xq,name='xq'),
    url(r'^deletebook/(\d+)/$',views.deletebook,name='deletebook'),
    url(r'^deletehero/(\d+)/$',views.deletehero,name='deletehero')


]


