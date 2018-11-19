from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url('^$', views.index),
    url('index', views.index),

    # Acolhidos
    url('formAcolhido', views.form_acolhido),
    url('^post_acolhido/$', views.post_acolhido),
    url('consultaAcolhido', views.cons_acolhido),

    # PIA
    url('formPIA', views.form_pia),
    url('([0-9]+)/$', views.get_pia),  # Procurar sobre o name='blabla'
    url('^post_pia', views.post_pia),

    # Doadores
    url('formDoador', views.form_doador),
    url('^post_doador/$', views.post_doador),
    url('consultaDoador', views.cons_doador),

    # Doações
    url('formDoacao', views.form_doacao),
    url('^post_doacao/$', views.post_doacao),
    url('consultaDoacao', views.cons_doacao),

    # Estoque
    url('formProduto', views.form_produto),
    url('consultaEstoque', views.cons_estoque),
    url('^post_produto/$', views.post_produto),

    # Contabilidade
    url('formContabilidade', views.form_contab),
    url('^formMovimentacao', views.get_movimentacao),
    url('^post_mov/$', views.post_mov),

    # Configurações
    url('formConfig', views.form_config)

]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)', serve, 
        {'document_root': settings.MEDIA_ROOT,}),
    ]