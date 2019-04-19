from django import forms
from .models import *

class AcolhidoForm(forms.ModelForm):
    class Meta:
        model = Acolhido
        fields = ['nome', 'data_nasc', 'data_entrada', 'cid_natal', 'uf', 'nome_mae', 'nome_pai', 'nome_resp', 'imagem', 'cpf', 'rg', 'ssp', 'renda']
        
class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        fields = ['nome', 'data_entrada', 'email', 'tel_residencial', 'tel_celular', 'voluntario', 'financeiro', 'vestuario', 'alimenticio']

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        #fields = ['valor', 'tipo', 'descricao', 'data', 'qtd']
        fields = ['valor', 'tipo', 'descricao', 'data', 'qtd']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'qtd', 'unidade', 'data_validade', 'preco_entrada']

class DoacaoForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = ['descricao', 'tipo_doacao', 'qtd', 'valor']

class ConfiguracaoForm(forms.ModelForm):
    class Meta:
        model = Configuracao
        fields = []