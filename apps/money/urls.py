# -*- coding:utf-8 -*-
from django.conf.urls import patterns,include, url

from money import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
)
