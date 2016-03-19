#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse(u"苏勇")

# GET params
# Example http://127.0.0.1:8000/add/?a=3&b=5
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

# REST
# Example http://127.0.0.1:8000/add/3/4
def add_rest(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
