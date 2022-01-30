from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita


def cadastro(request):
    """ Realiza o cadastro de um usuário no sistema """
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        
        if campo_vazio(nome):
            messages.error(request, 'Campo nome é obrigatório!')
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request, 'Campo email é obrigatório!')
            return redirect('cadastro')
        if senha != senha2:
            messages.error(request, 'As senhas não coincidem')
            print('Senhas estão diferentes!')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Nome de usuário já cadastrado!')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado!')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('Usuário criado com sucesso!')
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    """ Realiza o login de um usuário no sistema """
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Campo de email e/ou senha inválido(s)!')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
            return redirect('dashboard')

    return render(request, 'usuarios/login.html')

def dashboard(request):
    """ Exibir a dashboard para usuários que estão logados no sistema """
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)

        dados = {
            'receitas': receitas
        }

        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def logout(request):
    """ Faz o logout de usuários no sistema """
    auth.logout(request)
    messages.error(request, 'Usuário deslogado!')
    return redirect('login')

def campo_vazio(campo):
    """ Função para testar campos vazios """
    return campo.strip() == ''