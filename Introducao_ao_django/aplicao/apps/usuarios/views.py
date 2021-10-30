from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita


def cadastro(request):
    '''Cadastra uma nova pessoa no sistema'''
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']

        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cadastro')

        if campo_vazio(email):
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect('cadastro')

        if senhas_nao_iguais(senha, senha2):
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail de usuário já cadastrado')
            return redirect('cadastro')

        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Nome de usuario já cadastrado')
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuario cadastrado com sucesso.')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    '''Realiza o login de um usuario'''

    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Os campos email e senha não podem ficar em branco')
            return redirect('login')

        if User.objects.filter(email=email).exists():
            q = User.objects.filter(email=email)
            nome = q.values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso')
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuario ou senha errados')
            return redirect('login')
    else:
        return render(request, 'usuarios/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    '''Mostra as receitas do usaurio logado'''
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-date_receita').filter(pessoa=id)
        dados = {
            'receitas': receitas
        }
        return render(request, 'usuarios/dashboard.html', context=dados)
    else:
        return redirect('index')


def campo_vazio(campo):
    '''Checa se um campo é vazio'''
    return not campo.strip()


def senhas_nao_iguais(senha1, senha2):
    '''Checa se a senha1 e igual a senha 2'''
    return senha2 != senha1
