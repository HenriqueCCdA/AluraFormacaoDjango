from django.shortcuts import get_object_or_404, render
from .models import Receita

# Create your views here.


def index(request):

    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)

    dados = {'receitas': receitas}

    return render(request, 'receitas/index.html', context=dados)


def receita(request, receita_id):

    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {'receita': receita}

    return render(request, 'receitas/receita.html', context=receita_a_exibir)


def buscar(request):

    lista_receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            print(nome_a_buscar)
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    receita_a_exibir = {
        'receitas': lista_receitas
    }
    print(receita_a_exibir)

    return render(request, 'receitas/buscar.html', context=receita_a_exibir)
