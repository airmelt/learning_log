#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@description: user_url 为应用程序users定义URL模式
@file_name: urls.py
@project: learning_log
@version: 1.0
@date: 2019/06/29 23:17
@author: air
"""

__author__ = 'air'

from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'
urlpatterns = [
    # 登录页面
    url(r'^login/$', LoginView.as_view(), name='login'),

    # 注销
    url(r'^logout/$', views.logout_view, name='logout'),

    # 注册页面
    url(r'^register/$', views.register, name='register'),
]