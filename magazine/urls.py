# coding:utf-8
from django.conf.urls import patterns, url, include
from .views import *
from minicms import settings
urlpatterns = patterns('',
    url(r'^(?P<magacolumn>[^/]+)/$', index, name='index1'),
    url(r'^(?P<magacolumn>[^/]+)/(?P<column>[^/]+)/$', article, name='article'),
    url(r'^(?P<magacolumn>[^/]+)/(?P<column>[^/]+)/(?P<pk>\d+)/$', article_detail, name='article_detail'),
)
