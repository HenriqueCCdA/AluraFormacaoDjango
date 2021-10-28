from django.urls import path
from .views import cadastro, login, dashboard, logout, cria_receita, deleta_receita, edita_receita, atualiza_receita


urlpatterns = [
    path('cadastro', cadastro, name='cadastro'),
    path('login', login, name='login'),
    path('dashboard', dashboard, name='dashboard'),
    path('logout', logout, name='logout'),
    path('cria_receita', cria_receita, name='cria_receita'),
    path('deleta/<int:receita_id>', deleta_receita, name='deleta_receita'),
    path('edita/<int:receita_id>', edita_receita, name='edita_receita'),
    path('atualiza_receita', atualiza_receita, name='atualiza_receita'),

]
