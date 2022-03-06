class Produtos:
    def __init__( self, id:int, nome:str, imagem:str, price:float, description:str):
        self._nome = nome
        self._id = id
        self._imagem = imagem
        self._price = price
        self._description = description
    
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def imagem(self):
        return self._imagem
    @imagem.setter
    def imagem(self, value):
        self._imagem = value

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, value):
        self._description = value