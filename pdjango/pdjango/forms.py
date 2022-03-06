from django import forms

def adicionar():
    id = len(produtos) + 1
    nome = forms.CharField(label='nome', max_length=100)
    imagem = forms.CharField(label='imagem', max_length=100)
    price = forms.CharField(label='price', max_length=100)
    description = forms.CharField(label='description', widget=forms.Textarea)
    New_product = Produtos(id, nome, imagem, price, description)
    produtos.append(New_product)