#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
"""
@description: learning_logs_url
@file_name: urls.py
@project: learning_log
@version: 1.0
@date: 2019/06/29 17:57
@author: air
"""

__author__ = 'air'
"""定义learning_logs的URL模式"""

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 显示所有的主题
    url(r'^topics/$', views.topics, name='topics'),

    # 特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # 用于添加新主题的网页
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # 用于添加新条目的页面
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # 用于编辑条目的页面
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
        name='edit_entry'),
]
