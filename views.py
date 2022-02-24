from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request, name):
    return render(request, "index.html",{'name':name})

def produtinhos():
    produto1 = ()