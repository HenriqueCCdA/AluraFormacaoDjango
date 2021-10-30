from django.urls import path
from .views import receita, busca


urlpatterns = [
    path('', receita.index, name='index'),
    path('<int:receita_id>', receita.receita, name='receita'),
    path('busca', busca.busca, name='buscar'),
    path('cria_receita', receita.cria_receita, name='cria_receita'),
    path('deleta/<int:receita_id>', receita.deleta_receita, name='deleta_receita'),
    path('edita/<int:receita_id>', receita.edita_receita, name='edita_receita'),
    path('atualiza_receita', receita.atualiza_receita, name='atualiza_receita'),
]
