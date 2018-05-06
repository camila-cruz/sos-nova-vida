from django.db import models
from datetime import date

# Create your models here.

# Model do Acolhido da instituicao
class Acolhido(models.Model):
    nome = models.CharField(max_length=40)
    data_nasc = models.DateField(default=date.today)
    data_entrada = models.DateField(default=date.today)
    local_nasc = models.CharField(max_length=50)
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
    imagem = models.ImageField(upload_to='img_doadores', default='media/default.png')
    tipo = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=15)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2, default="SP")
    tel_residencial = models.CharField(max_length=10)
    tel_celular = models.CharField(max_length=10)
    tel_comercial = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)

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
