from django.test import TestCase
from animais.models import Animal


class AnimalModelTestCase(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            nome_do_animal='Leão',
            predador='Sim',
            venenoso='Não',
            domestico='Não'
        )

    def test_animal_cadastrado_com_caracteristicas(self):
        '''
        Teste que verifica se o animal esta cadastrado com suas respectivas características
        '''
        self.assertEqual(self.animal.nome_do_animal, 'Leão')
