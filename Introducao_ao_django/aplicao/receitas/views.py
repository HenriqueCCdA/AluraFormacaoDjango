from django.shortcuts import render


# Create your views here.
def index(request):
    receitas = {1:'Lasanha', 
                2:'Sopa de legumes',
                3:'Sorvete',
                4:'Bolo de chocolate'
    }

    dados = {'nome_das_receitas': receitas}

    return render(request, 'index.html', context=dados)


def receita(request):
    return render(request, 'receita.html')
