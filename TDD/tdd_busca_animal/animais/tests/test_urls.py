from django.test import TestCase, RequestFactory
from animais.views import index


class AnimaisURLSTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_rota_url_utiliza_view_index(self):
        '''
        Teste se a home da aplicação utiliza o index da view
        '''
        request = self.factory.get('/')
        with self.assertTemplateUsed('index.html'):
            reponse = index(request)
            self.assertEqual(reponse.status_code, 200)
