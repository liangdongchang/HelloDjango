# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
@contact: 微信 1257309054
@file: urls.py
@time: 2022/1/23 22:01
@author: LDC
"""

from django.conf.urls import url
from MyApp import views


urlpatterns = [
    # http://127.0.0.1:8000/请求交由HelloDjango下的views中的index函数处理
    url(r'^wolf', views.wolf),
    url(r'^welcome', views.welcome),
]