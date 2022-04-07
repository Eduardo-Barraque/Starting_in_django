from django.shortcuts import render
from Lab_progamacao_frameworks.models import Video, Categoria

videoAcao1 = Video(1, "FreeGuy.mp4", 'img/Free_Guy_poster.jpg', "Free Guy - Assumindo Controle",
                "Um caixa de banco preso a uma entediante rotina tem sua vida virada de cabeça para baixo quando descobre que é um personagem em um jogo interativo. Agora ele precisa aceitar sua realidade e lidar com o fato de que é o único que pode salvar o mundo."
                   , 18578058, 1099999, '19/08/2021')
videoAcao2 = Video(2, "DeadPool.mp4", "img/DeadPool.jpg", "DeadPool",
                "Wade Wilson é um ex-agente especial que passou a trabalhar como mercenário. Seu mundo é destruído quando um cientista maligno o tortura e o desfigura completamente. O experimento brutal transforma Wade em Deadpool, que ganha poderes especiais de cura e uma força aprimorada. Com a ajuda de aliados poderosos e um senso de humor mais desbocado e cínico do que nunca, o irreverente anti-herói usa habilidades e métodos violentos para se vingar do homem que quase acabou com a sua vida."
                   , 24670369, 1877547, '11/02/2016')
acao = Categoria("Ação", [videoAcao1, videoAcao2])
aventura = Categoria("Aventura", [videoAcao1, videoAcao2])

listaCategorias = [acao, aventura]


def home(request):
    return render(request, "home.html", {'listaCategorias': listaCategorias})
