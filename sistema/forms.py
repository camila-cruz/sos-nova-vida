from django import forms
from .models import *
from localflavor.br.forms import *
from localflavor.br.br_states import *

class AcolhidoForm(forms.ModelForm):
    cpf = BRCPFField(required=False)
    uf = BRStateSelect()
    data_nasc = forms.DateField(input_formats=["%d/%m/%Y"])
    data_entrada = forms.DateField(input_formats=["%d/%m/%Y"])
    class Meta:
        model = Acolhido
        fields = ['nome', 'data_nasc', 'data_entrada', 'cid_natal', 'uf', 'cpf', 'rg', 'ssp', 'nome_mae', 
        'nome_pai', 'nome_resp', 'grau_resp', 'imagem', 'sangue', 'renda', 'camiseta', 'calca', 'intima', 'calcado', 'qtd_aborto']
        
class ResidenciaForm(forms.ModelForm):
    class Meta:
        model = Residencia
        fields = ['cep', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'uf']

class JuridicoForm(forms.ModelForm):
    processo = BRProcessoField(required=False)
    class Meta:
        model = Juridico
        fields = ['processo', 'comarca', 'nro_vara', 'vara']

class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        fields = ['nome', 'data_entrada', 'email', 'tel_1', 'tel_2', 'voluntario', 'financeiro', 'vestuario', 'alimenticio']

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