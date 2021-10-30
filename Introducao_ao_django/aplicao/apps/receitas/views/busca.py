from receitas.views.receita import Receita
from django.shortcuts import render


def busca(request):

    lista_receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    receita_a_exibir = {
        'receitas': lista_receitas
    }

    return render(request, 'receitas/buscar.html', context=receita_a_exibir)
