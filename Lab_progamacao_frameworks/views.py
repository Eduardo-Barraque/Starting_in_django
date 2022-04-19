from django.shortcuts import render
from Lab_progamacao_frameworks.models import CategoriaDao

listaCategorias = CategoriaDao().categorias()


def home(request):
    return render(request, "home.html", {'listaCategorias': listaCategorias})


def page_view(request, id):
    for categoria in listaCategorias:
        for video in categoria.listaVideos:
            if video.id == int(id):
                return render(request, "video.html", {"video": video})
