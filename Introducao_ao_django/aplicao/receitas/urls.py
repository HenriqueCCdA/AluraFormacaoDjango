from django.urls import path
from .views import index, receita


urlpatterns = [
    path('', index, name='index'),
    path('<int:receita_id>', receita, name='receita')
]
