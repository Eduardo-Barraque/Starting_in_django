from typing import List


class Video:
    def __init__(self, id, url_video, url_image, title, descript, visu, likes, data):
        self.__id = id
        self.__url_video = url_video
        self.__url_image = url_image
        self.__title = title
        self.__descript = descript
        self.__visu = visu
        self.__likes = likes
        self.__data = data

    @property
    def id(self):
        return self.__id

    @property
    def url_video(self):
        return self.__url_video

    @property
    def url_image(self):
        return self.__url_image

    @property
    def title(self):
        return self.__title

    @property
    def descript(self):
        return self.__descript

    @property
    def visu(self):
        return self.__visu

    @property
    def likes(self):
        return self.__likes

    @property
    def data(self):
        return self.__data


class Categoria:
    def __init__(self, nome, listaVideos: List[Video]):
        self.__nome = nome
        self.__listaVideos = listaVideos

    @property
    def nome(self):
        return self.__nome

    @property
    def listaVideos(self):
        return self.__listaVideos


class CategoriaDao:
    def __init__(self):
        self.__categorias = []

        video_acao1 = Video(1, "FreeGuy.mp4", 'img/Free_Guy_poster.jpg', "Free Guy - Assumindo Controle",
                           "Um caixa de banco preso a uma entediante rotina tem sua vida virada de cabeça para baixo quando descobre que é um personagem em um jogo interativo. Agora ele precisa aceitar sua realidade e lidar com o fato de que é o único que pode salvar o mundo."
                           , "18.578.058", "1.099.999", '19/08/2021')
        video_acao2 = Video(2, "DeadPool.mp4", "img/DeadPool.jpg", "DeadPool",
                           "Wade Wilson é um ex-agente especial que passou a trabalhar como mercenário. Seu mundo é destruído quando um cientista maligno o tortura e o desfigura completamente. O experimento brutal transforma Wade em Deadpool, que ganha poderes especiais de cura e uma força aprimorada. Com a ajuda de aliados poderosos e um senso de humor mais desbocado e cínico do que nunca, o irreverente anti-herói usa habilidades e métodos violentos para se vingar do homem que quase acabou com a sua vida."
                           , "24.670.369", "1.877.547", '11/02/2016')
        acao = Categoria("Ação", [video_acao1])
        aventura = Categoria("Aventura", [video_acao2])
        self.__categorias = [acao, aventura]

    def categorias(self):
        return self.__categorias
