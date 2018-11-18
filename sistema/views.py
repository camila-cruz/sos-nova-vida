from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *


# Create your views here.

# Pagina principal
def index(request):
    HttpResponseRedirect('/')
    return render(request, 'index.html')

# Acolhidos
def form_acolhido(request):
    form = AcolhidoForm()
    return render(request, 'formAcolhido.html', {'form': form})

def post_acolhido(request):
    form = AcolhidoForm(request.POST, request.FILES)
    if form.is_valid():
        form.save(commit = True)
    return HttpResponseRedirect('/')

def cons_acolhido(request):
    acolhidos = {} # Acolhido.objects.all()
    return render(request, 'consultaAcolhido.html', {'acolhidos': acolhidos})

# PIA
def form_pia(request):
    return render(request, 'formPIA.html')

def get_pia(request, acolhido_id):
    acolhido = Acolhido.objects.get(id=acolhido_id)
    return render(request, 'formPIA.html', {'acolhido': acolhido})

def post_pia(request):
    #form = PiaForm(request.POST)
    """response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pia.pdf"'
    
    p = canvas.Canvas(response)

    p.drawString(100, 100, 'Hello Worldzinho de merda')

    p.showPage()
    p.save()
    return response"""

# Doadores
def form_doador(request):
    form = DoadorForm()
    return render(request, 'formDoador.html', {'form': form})

def post_doador(request):
    form = DoadorForm(request.POST, request.FILES)
    print(form.errors)
    if form.is_valid():
        form.save(commit = True)
    return HttpResponseRedirect('/')

def cons_doador(request):
    doadores = {} # Doador.objects.all()
    return render(request, 'consultaDoador.html', {'doadores': doadores})

# Doacoes
def cons_doacoes(request):
    doacoes = Movimentacao.objects.filter(tipo="DOACAO")
    return render(request, 'formContabilidade.html', {'doacoes': doacoes})

# Estoque
def form_produto(request):
    form = ProdutoForm()
    return render(request, 'formProduto.html', {'form': form})

def post_produto(request):
    form = ProdutoForm(request.POST)
    if form.is_valid():
        form.save(commit = True)
    return HttpResponseRedirect('/')

def cons_estoque(request):
    produtos = Produto.objects.all()
    return render(request, 'consultaEstoque.html', {'produtos': produtos})

# Contabilidade
def form_contab(request):
    movs = Movimentacao.objects.all()
    return render(request, 'formContabilidade.html', {'movs': movs})

def get_movimentacao(request):
    form = MovimentacaoForm()
    return render(request, 'formMovimentacao.html', {'form': form})

def post_mov(request):
    form = MovimentacaoForm(request.POST)
    if form.is_valid():
        form.save(commit = True)
        print (form.errors)
    return HttpResponseRedirect('/')

# Configurações
def form_config(request):
    form = ConfiguracaoForm()
    #form = ProdutoForm()
    return render(request, 'formConfig.html', {'form': form})