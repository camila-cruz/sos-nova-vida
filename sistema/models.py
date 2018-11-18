from django.db import models
from datetime import date

# Create your models here.

# Model do Acolhido da instituicao
class Acolhido(models.Model):
    nome = models.CharField(max_length=40)
    data_nasc = models.DateField(default=date.today)
    data_entrada = models.DateField(default=date.today)
    cid_natal = models.CharField(max_length=50)
    uf = models.CharField(max_length=2, default="SP")
    imagem = models.ImageField(upload_to='img_acolhidos', default='media/default.png')
    nome_mae = models.CharField(max_length=40, default="")
    resp_mae = models.BooleanField(default=False)
    nome_pai = models.CharField(max_length=40, default="")
    resp_pai = models.BooleanField(default=False)
    nome_resp = models.CharField(max_length=40, default="")
    resp_resp = models.BooleanField(default=False)

class Doador(models.Model):
    nome = models.CharField(max_length=40)
    data_entrada = models.DateField(default=date.today)
    email = models.EmailField(max_length=30)
    #imagem = models.ImageField(upload_to='img_doadores', default='media/default.png')
    tel_residencial = models.CharField(max_length=10)
    tel_celular = models.CharField(max_length=10)
    tel_comercial = models.CharField(max_length=10)
    voluntario = models.BooleanField(default=False)
    financeiro = models.BooleanField(default=False)
    vestuario = models.BooleanField(default=False)
    alimenticio = models.BooleanField(default=False)

class Movimentacao(models.Model):
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    CHOICES = (
                ('ENTRADA', 'Entrada'),
                ('SAIDA', 'Saída'),
                ('DOACAO', 'Doação'),
              )
    tipo = models.CharField(choices=CHOICES, max_length=7)
    descricao = models.CharField(max_length=150)
    data = models.DateField(default=date.today)
    qtd = models.IntegerField()

#class Doacao(Movimentacao):
    #qtd = models.IntegerField()
    # Doador
    #tipo_doacao = models.CharField(max_length=10)   # Bens, Dinheiro e Tempo

class Produto(models.Model):
    descricao = models.CharField(max_length=150)
    qtd = models.IntegerField()
    unidade = models.CharField(max_length=20)
    data_validade = models.DateField(default=date.today)
    preco_entrada = models.DecimalField(max_digits=7, decimal_places=2)

class Caixa(models.Model):
    vlr_disponivel = models.DecimalField(max_digits=7, decimal_places=2)
    # Set de Movimentacao

class Configuracao(models.Model):
    novo_nome = models.CharField(max_length=20)

# Classe de Usuario
