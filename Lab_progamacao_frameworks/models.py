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
