from cgitb import html
from urllib import request
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from pdjango.models import ProdutoDAO
from django import forms
from pdjango.models import Produtos

produtos = ProdutoDAO().listar_produtos()

def lista_produtos(request):
    return render(request, "index.html",{'produtos' : produtos})

def produto_detalhes(request,id:int):
    for produto in produtos:
        if produto.id == id:
            return render(request, "produtos.html", {'produto': produto})
        else:
            pass
    else:
        return "Este produto não existe"


def add(request):
    if request.method == 'POST':
        form = AdicionarProduto(request.POST) # Um form com os dados de POST
        if form.is_valid(): # All validation rules pass
            # Processa os dados no form.cleaned_data
            # ...
            return HttpResponseRedirect('/add/')
    else:
        form = AdicionarProduto() # Um formulário vazio

    return render(request,'index.html')

class AdicionarProduto(forms.Form):
    id = len(produtos) + 1
    nome = forms.CharField(label='product_name', max_length=100)
    imagem = forms.CharField(label='product_image', max_length=100)
    price = forms.CharField(label='product_price', max_length=100)
    description = forms.CharField(label='product_description', widget=forms.Textarea)
    New_product = Produtos(id, nome, imagem, price, description)
    produtos.append(New_product)


