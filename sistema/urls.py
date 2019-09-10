from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'index', views.index),

    # Acolhidos
    url(r'^acolhido/novo/$', views.form_acolhido, name="cad_acolhido"),
    url(r'^acolhido/(?P<id>\d+)/$', views.get_acolhido, name="get_acolhido"),
    url(r'^acolhido/(?P<id>\d+)/edit$', views.edit_acolhido, name="edit_acolhido"),
    url(r'post_acolhido/$', views.post_acolhido),
    url(r'^acolhido/$', views.cons_acolhido, name="cons_acolhido"),
    url(r'^api/grafico/acolhido/$', views.get_dados_acolhido, name="dados_acolhido"),

    # url(r'formAcolhido', views.form_acolhido),
    # url(r'getAcolhido/(?P<id>\d+)/$', views.get_acolhido),
    # url(r'^post_acolhido/$', views.post_acolhido),
    # url(r'consultaAcolhido', views.cons_acolhido),

    # Doadores
    url(r'^doador/novo/$', views.form_doador, name="cad_doador"),
    url(r'post_doador/$', views.post_doador),
    url(r'^doador/$', views.cons_doador, name="cons_doador"),
    url(r'^src_doador/$', views.src_doador),

    # Doações
    url(r'^doacao/novo/$', views.form_doacao, name="cad_doacao"),
    url(r'^doacao/(?P<id>\d+)/$', views.get_doacao, name="get_doacao"),
    url(r'post_doacao/$', views.post_doacao),
    url(r'^doacao/$', views.cons_doacao, name="cons_doacao"),

    # Estoque
    url(r'^estoque/$', views.cons_estoque, name="estoque"),
    url(r'post_produto/$', views.post_produto),
    url(r'mov_estoque/(?P<id>\d+)/$', views.mov_estoque),
    url(r'^api/grafico/estoque', views.get_dados_estoque, name="dados_estoque"),

    # Contabilidade
    url(r'formContabilidade', views.form_contab),
    url(r'^movimentacao/$', views.get_movimentacao, name="movimentacao"),
    url(r'^post_mov/$', views.post_mov),

    # Configurações
    url(r'^configuracao/$', views.form_config, name="edit_configs"),

    # PIA
    url(r'formPIA', views.form_pia),
    url(r'([0-9]+)/$', views.get_pia),  # Procurar sobre o name='blabla'
    url(r'^post_pia', views.post_pia),

]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)', serve, 
        {'document_root': settings.MEDIA_ROOT,}),
    ]