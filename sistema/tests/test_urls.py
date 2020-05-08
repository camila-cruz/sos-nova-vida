from django.test import SimpleTestCase
from django.urls import reverse, resolve
from sistema.views import cons_acolhido, form_acolhido, get_acolhido, edit_acolhido, cons_doador, form_doador, cons_doacao, form_doacao, get_doacao, get_movimentacao, form_config

class TestUrlsAcolhido(SimpleTestCase):
    
    def test_consulta_url_resolves(self):   # List
        url = reverse('cons_acolhido')
        self.assertEquals(resolve(url).func, cons_acolhido)

    def test_cadastro_url_resolves(self):   # Create
        url = reverse('cad_acolhido')
        self.assertEquals(resolve(url).func, form_acolhido)

    def test_get_url_resolves(self):        # Read
        url = reverse('get_acolhido', args=[0])
        self.assertEquals(resolve(url).func, get_acolhido)

    def test_edit_url_resolves(self):        
        url = reverse('edit_acolhido', args=[0])
        self.assertEquals(resolve(url).func, edit_acolhido)

    # TODO: Post Acolhido

class TestUrlsDoador(SimpleTestCase):

    def test_consulta_url_resolves(self):
        url = reverse('cons_doador')
        self.assertEquals(resolve(url).func, cons_doador)

    def test_cadastro_url_resolves(self):
        url = reverse('cad_doador')
        self.assertEquals(resolve(url).func, form_doador)

        # TODO: Post, Get e Edit Doador

class TestUrlsDoacao(SimpleTestCase):

    def test_consulta_url_resolves(self):
        url = reverse('cons_doacao')
        self.assertEquals(resolve(url).func, cons_doacao)

    def test_cadastro_url_resolves(self):
        url = reverse('cad_doacao')
        self.assertEquals(resolve(url).func, form_doacao)

    def test_get_url_resolves(self):
        url = reverse('get_doacao', args=[0])
        self.assertEquals(resolve(url).func, get_doacao)

        # TODO: Post Doacao

class TestUrlsMovimentacao(SimpleTestCase):

    def test_consulta_url_resolves(self):
        url = reverse('movimentacao')
        self.assertEquals(resolve(url).func, get_movimentacao)

class TestUrlsConfiguracao(SimpleTestCase):

    def test_edit_url_resolves(self):
        url = reverse('edit_configs')
        self.assertEquals(resolve(url).func, form_config)