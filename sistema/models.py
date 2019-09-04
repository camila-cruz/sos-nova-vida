from django.db import models
from datetime import date
from localflavor.br.models import *

# Create your models here.

# Model do Acolhido da instituicao
class Acolhido(models.Model):
    TIPO_SANGUINEO = (
        ('', 'Selecione'),
        ('NI', 'Não informado'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    GRAU_PARENTESCO = (
        ('MÃE', 'Mãe'),
        ('PAI', 'Pai'),
        ('AVÓ', 'Avó'),
        ('AVÔ', 'Avô'),
        ('OUT', 'Outro'),
        ('NEN', 'Nenhum')
    )
    nome = models.CharField(max_length=40, blank=True)
    data_nasc = models.DateField(default=date.today)
    data_entrada = models.DateField(default=date.today)
    cid_natal = models.CharField(max_length=50, blank=True)
    uf = BRStateField(max_length=2, default="SP", blank=True)
    imagem = models.ImageField(upload_to='img_acolhidos', default='media/default.png', blank=True)
    nome_mae = models.CharField(max_length=40, default="", blank=True)
    resp_mae = models.BooleanField(default=False, blank=True)
    nome_pai = models.CharField(max_length=40, default="", blank=True)
    resp_pai = models.BooleanField(default=False, blank=True)
    nome_resp = models.CharField(max_length=40, default="", blank=True)
    grau_resp = models.CharField(max_length=3, choices=GRAU_PARENTESCO, blank=True)
    cpf = models.CharField(max_length=14, blank=True)
    rg = models.CharField(max_length=11, blank=True)
    ssp = BRStateField(max_length=2, blank=True)
    renda = models.DecimalField(max_digits=6, decimal_places=2, default=0, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True)
    camiseta = models.CharField(max_length=2, blank=True)
    calca = models.CharField(max_length=2, blank=True)
    intima = models.CharField(max_length=1, blank=True)
    calcado = models.CharField(max_length=2, blank=True)
    alergias = models.TextField(blank=True)
    sangue = models.CharField(max_length=3, choices=TIPO_SANGUINEO, blank=True)
    qtd_aborto = models.IntegerField(blank=True, null=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):  # Equivalente ao .toString do Java
        return self.nome

class Residencia(models.Model):
    acolhido = models.ForeignKey(Acolhido, on_delete=models.CASCADE)
    cep = models.CharField(max_length=9, blank=True)
    logradouro = models.CharField(max_length=65, blank=True)
    numero = models.CharField(max_length=4, blank=True)
    complemento = models.CharField(max_length=15, blank=True)
    bairro = models.CharField(max_length=30, blank=True)
    cidade = models.CharField(max_length=30, blank=True)
    uf = models.CharField(max_length=2, blank=True)

    def __str__(self):
        return str(self.id) + str(self.acolhido.id) + self.acolhido.nome

class Juridico(models.Model):
    acolhido = models.ForeignKey(Acolhido, on_delete=models.CASCADE)
    processo = models.CharField(max_length=25, blank=True)
    comarca = models.CharField(max_length=30, blank=True)
    nro_vara = models.CharField(max_length=2, blank=True)
    vara = models.CharField(max_length=20, blank=True)

class Doador(models.Model):
    nome = models.CharField(max_length=40)
    data_entrada = models.DateField(default=date.today)
    email = models.EmailField(max_length=30, blank=True)
    #imagem = models.ImageField(upload_to='img_doadores', default='media/default.png')
    tel_1 = models.CharField(max_length=14, blank=True)
    tel_2 = models.CharField(max_length=14, blank=True)
    voluntario = models.BooleanField(default=False)
    financeiro = models.BooleanField(default=False)
    vestuario = models.BooleanField(default=False)
    alimenticio = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

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

class Produto(models.Model):
    descricao = models.CharField(max_length=150)
    qtd = models.IntegerField()
    # unidade = models.CharField(max_length=20)
    # data_validade = models.DateField(default=date.today)
    # preco_entrada = models.DecimalField(max_digits=7, decimal_places=2)
    
class Doacao(models.Model):
    doador = models.ForeignKey(Doador, on_delete=models.SET_NULL, null=True)
    data = models.DateField(default=date.today)
    descricao = models.CharField(max_length=60)

class ItemDoacao(models.Model):
    id_doacao = models.ForeignKey(Doacao, on_delete=models.CASCADE, related_name='itens')
    tipo = models.CharField(max_length=10)   # Roupa ou Alimento
    nome = models.CharField(max_length=30)
    qtd = models.IntegerField()

    def __str__(self):
        return "Um(a) " + self.tipo + " com nome de " + self.nome + " foi doado com qtde de " + self.qtd

class DinheiroDoacao(models.Model):
    id_doacao = models.ForeignKey(Doacao, on_delete=models.CASCADE, related_name='dinheiro')
    valor = models.DecimalField(max_digits=7, decimal_places=2)

class Caixa(models.Model):
    vlr_disponivel = models.DecimalField(max_digits=7, decimal_places=2)
    # Set de Movimentacao

class Configuracao(models.Model):
    novo_nome = models.CharField(max_length=20)

# Classe de Usuario
