from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from pdjango.models import ProdutoDAO
from pdjango.forms import adicionar

from pdjango.models import Produtos

produtos = ProdutoDAO().listar_produtos()

def lista_produtos(request):
    return render(request, "index.html",{'produtos' : produtos})

def produto_detalhes(request,id:int):
    return render(request, "produtos.html", {'produtos': produtos,'id':id})


