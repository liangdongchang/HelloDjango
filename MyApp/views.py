from django.shortcuts import render

# Create your views here.

# http://127.0.0.1:8000/wolf/
def wolf(request):
# 渲染页面并呈现给用户
    return render(request,'wolf.html')