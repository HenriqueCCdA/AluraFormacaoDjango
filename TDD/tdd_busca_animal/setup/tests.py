from django.test import LiveServerTestCase
from selenium import webdriver
from pathlib import Path


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        exec_path = Path(__file__).parent.parent / 'chromedriver.exe'
        self.browser = webdriver.Chrome(exec_path)

    def tearDown(self):
        self.browser.quit()

    def test_buscando_um_novo_animal(self):
        '''
        Teste se um usuário encontra um animal pesquisando
        '''

        self.browser.get(self.live_server_url + '/')

        brand_element = self.browser.find_element_by_css_selector('.navbar')
        self.assertEqual('Busca Animal', brand_element.text)
