from django.urls import path
from .views import index, receita, buscar


urlpatterns = [
    path('', index, name='index'),
    path('<int:receita_id>', receita, name='receita'),
    path('busca', buscar, name='buscar'),
]
