from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from .models import *
from .forms import *

# Create your views here.

# Pagina principal
def index(request):
    HttpResponseRedirect('/')
    return render(request, 'index.html')

# Acolhidos
def form_acolhido(request):
    form_a = AcolhidoForm()
    form_r = ResidenciaForm()
    form_j = JuridicoForm()
    return render(request, 'formAcolhido.html', {
        'form': form_a,
        'form_r': form_r,
        'form_j': form_j
    })

def get_acolhido(request, id=None):
    acolhido = get_object_or_404(Acolhido, id=id)

    # Retorna uma tupla com o obj e um bool se ele teve que ser criado ou não
    residencia = Residencia.objects.get_or_create(acolhido=acolhido)[0]
    juridico = Juridico.objects.get_or_create(acolhido=acolhido)[0]

    return render(request, 'getAcolhido.html', {
        'acolhido': acolhido,
        'residencia': residencia,
        'juridico': juridico
    })

def edit_acolhido(request, id=None):
    acolhido = get_object_or_404(Acolhido, id=id)

    # Retorna uma tupla com o obj e um bool se ele teve que ser criado ou não
    residencia = Residencia.objects.get_or_create(acolhido=acolhido)[0]
    juridico = Juridico.objects.get_or_create(acolhido=acolhido)[0]

    form_a = AcolhidoForm(request.POST or None, instance=acolhido)
    form_r = ResidenciaForm(request.POST or None, instance=residencia)
    form_j = JuridicoForm(request.POST or None, instance=juridico)
    return render(request, 'formAcolhido.html', {
        'form': form_a,
        'form_r': form_r,
        'form_j': form_j
    })

def post_acolhido(request):
    form_a = AcolhidoForm(request.POST, request.FILES)
    form_r = ResidenciaForm(request.POST, request.FILES)
    form_j = JuridicoForm(request.POST, request.FILES)
    if form_a.is_valid():
        #print (form_a.cleaned_data)
        acolhido = form_a.save(commit=False)
        acolhido.save()

        if form_r.is_valid():
            if form_r.has_changed():    # Checa se o endereço não tá em branco
                residencia = form_r.save(commit=False)
                residencia.acolhido = acolhido
                residencia.save()

            if form_j.is_valid():
                if form_j.has_changed():    # Checa se o jurídico não tá em branco
                    juridico = form_j.save(commit=False)
                    juridico.acolhido = acolhido
                    juridico.save()                

                return HttpResponseRedirect("/consultaAcolhido/")
            else:
                print("Não deu pro juridico")
        else:
            print("Não deu pra residencia")
    else:
        print("Não deu pro acolhido")

    return HttpResponseRedirect('/')

def cons_acolhido(request):
    acolhidos = Acolhido.objects.all() #{} 
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
    print(form.cleaned_data)
    if form.is_valid():
        form.save() # commit é True se não for mencionado
    #     form.save(commit = True)
    return HttpResponseRedirect('/')

def cons_doador(request):
    doadores = Doador.objects.all()
    return render(request, 'consultaDoador.html', {'doadores': doadores})

def src_doador(request):
    palavra = request.GET.get('term', '')
    doadores = Doador.objects.filter(nome__icontains=palavra)
    resultado = []
    for d in doadores:
        d_json = {}     # TEM que ser label e value, senão não funciona
        d_json['label'] = d.nome    # O que vai aparecer nos resultados da pesquisa
        d_json['value'] = d.nome    # O que vai aparecer ao selecionar o resultado
        d_json['id'] = d.id
        resultado.append(d_json)

    return JsonResponse(resultado, safe=False)

# Doacoes
def form_doacao(request):
    form = DoacaoForm()
    return render(request, 'formDoacao.html', {'form': form})

def post_doacao(request):
    form = DoacaoForm(request.POST)
    if form.is_valid():
        form.save(commit = True)
    return HttpResponseRedirect('/')

def cons_doacao(request):
    doacoes = Movimentacao.objects.filter(tipo="DOACAO")        # Verificar se essa é a forma certa de fazer isso
    return render(request, 'consultaDoacao.html', {'doacoes': doacoes})

# Estoque
def form_produto(request):
    form = ProdutoForm()
    return render(request, 'formProduto.html', {'form': form})

def post_produto(request):
    form = ProdutoForm(request.POST)
    if form.is_valid():
        print (form.cleaned_data)
        form.save(commit = True)
    return HttpResponseRedirect('/')

def cons_estoque(request):
    produtos = Produto.objects.all()
    form_p = ProdutoForm()
    form_e = EstoqueForm()
    return render(request, 'consultaEstoque.html', {'form_p': form_p, 'form_e': form_e, 'produtos': produtos})

def mov_estoque(request, id=None):
    form = EstoqueForm(request.POST)
    tipo = request.POST["tipo"]

    if form.is_valid():
        produto = Produto.objects.get(id=id)
        if tipo == "saida":
            produto.qtd -= form.cleaned_data['qtd']
        elif tipo == "entrada":
            produto.qtd += form.cleaned_data['qtd']
        
        produto.save()
        qtd = produto.qtd

    print (tipo)

    dados = {
        'tipo': tipo,
        'id': id,
        'qtd': qtd,
    }
    #return HttpResponseRedirect('/')
    return JsonResponse(dados)

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