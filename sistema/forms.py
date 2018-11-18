from django import forms
from .models import *

class AcolhidoForm(forms.ModelForm):
    class Meta:
        model = Acolhido
        fields = ['nome', 'data_nasc', 'data_entrada', 'cid_natal', 'uf', 'nome_mae', 'nome_pai', 'nome_resp', 'imagem']
        
class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        fields = ['nome', 'data_entrada', 'email', 'tel_residencial', 'tel_celular', 'voluntario', 'financeiro', 'vestuario', 'alimenticio']

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        #fields = ['valor', 'tipo', 'descricao', 'data', 'qtd']
        fields = ['valor', 'tipo', 'descricao', 'data', 'qtd']
#class DoacaoForm(forms.ModelForm):
#    class Meta:
#        model = Doacao
#        fields = ['qtd']    # Falta o tipo da doacao

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'qtd', 'unidade', 'data_validade', 'preco_entrada']

class ConfiguracaoForm(forms.ModelForm):
    class Meta:
        model = Configuracao
        fields = []