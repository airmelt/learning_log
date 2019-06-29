#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@description: 创建表单
@file_name: forms.py
@project: learning_log
@version: 1.0
@date: 2019/06/29 22:44
@author: air
"""

__author__ = 'air'
from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
