#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render

# For redirection
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

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
    return HttpResponseRedirect(
        reverse('add_rest', args=(a, b))
    )

# Redirect
def new_add_rest(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

# Render from template
def home(request):
    return render(request, 'home.html')
