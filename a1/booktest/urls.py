from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^list/$',views.list),
    url(r'^index/$', views.index),
    url(r'^xq/(\d+)/$', views.xq),


]


