from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request, name):
    return render(request, "index.html",{'name':name})

def lista_produtos(request):
    return render(request, "produtos.html")

def busca_produtos(request):
    return render()

def exibir_form(request):
    return render(request,"form.html", {})

def inserir(request):
    return render(request,"form.html", {})
