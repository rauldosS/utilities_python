from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import FormContato

# Create your views here.
def login(request):
    if request.method != 'POST':
        return render(request, 'login/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'login/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Você fez login com sucesso')
        return redirect('accounts:dashboard')

def logout(request):
    auth.logout(request)
    return redirect('accounts:login')

def cadastro(request):
    if request.method != 'POST':
        return render(request, 'login/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    valida_senha = request.POST.get('valida_senha')

    # Validações    
    if not nome or not sobrenome or not email or not senha \
        or not valida_senha:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'login/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'E-mail inválido.')
        return render(request, 'login/cadastro.html')

    if len(senha) < 6 or len(usuario) < 6:
        messages.error(request, 'Usuário e senha e  precisam ter no mínimo 6 caracteres.')
        return render(request, 'login/cadastro.html')

    if senha != valida_senha:
        messages.error(request, 'Senhas não conferem.')
        return render(request, 'login/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe.')
        return render(request, 'login/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'E-mail já existe.')
        return render(request, 'login/cadastro.html')
        
    # Registro
    user = User.objects.create_user(
        username=usuario,
        first_name=nome,
        last_name=sobrenome,
        email=email,
        password=senha
    )
    user.save()

    messages.success(request, 'Usuário registrado com sucesso!\n Agora faça login.')
    return redirect('accounts:login')

@login_required(redirect_field_name='accounts:login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContato()
        return render(request, 'login/dashboard.html', {'form': form})

    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar formulário.')

        form = FormContato(request.POST)
        return render(request, 'login/dashboard.html', {'form': form})

    descricao = request.POST.get('descricao')

    if len(descricao) < 5:
        messages.error(request, 'Descrição precisa ter no mínimo 5 caracteres.')

        form = FormContato(request.POST)
        return render(request, 'login/dashboard.html', {'form': form})

    form.save()
    messages.success(request, f'Contato {request.POST.get("nome")} salvo com sucesso!')

    return redirect('accounts:dashboard')