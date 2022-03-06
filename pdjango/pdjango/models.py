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

class ProdutoDAO:
    def __init__(self):

        produto1 = Produtos('1',"Product Number 1",
            "//imagens.pontofrio.com.br/Control/ArquivoExibir.aspx?IdArquivo=6670538","332",
            "Product long description number 1 just to make more than one like of text.")

        produto2 = Produtos('2',"Product Number 2",
                "//imagens.pontofrio.com.br/Control/ArquivoExibir.aspx?IdArquivo=6829307", "76",
                "Product long description number 2 just to make more than one like of text.")

        produto3 = Produtos('3',"Product Number 3",
                "//imagens.pontofrio.com.br/Control/ArquivoExibir.aspx?IdArquivo=6506376","154",
                "Product long description number 3 just to make more than one like of text.")

        produto4 = Produtos('4',"Product Number 4",
                "//imagens.pontofrio.com.br/Control/ArquivoExibir.aspx?IdArquivo=6584703","272",
                "Product long description number 4 just to make more than one like of text.")

        produto5 = Produtos('5',"Product Number 5",
                "//imagens.pontofrio.com.br/Control/ArquivoExibir.aspx?IdArquivo=6875461","92",
                "Product long description number 5 just to make more than one like of text.")

        produto6 = Produtos('6',"Product Number 6",
                "//imagens.pontofrio.com.br/Control/ArquivoExibir.aspx?IdArquivo=6624363","68",
                "Product long description number 6 just to make more than one like of text.")

        produto7 = Produtos('7',"Product Number 7",
                "//imagens.pontofrio.com.br/Control/ArquivoExibir.aspx?IdArquivo=6670538","140",
                "Product long description number 7 just to make more than one like of text.")

        produto8 = Produtos('8',"Product Number 8",
                "//imagens.pontofrio.com.br/Control/ArquivoExibir.aspx?IdArquivo=6584703","213",
                "Product long description number 8 just to make more than one like of text.")

        self.__produtinhos = [produto1,produto2,produto3,produto4,produto5,produto6,produto7,produto8]

    def listar_produtos(self):
        return self.__produtinhos