from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

@login_required(login_url="login")
def index(request):
    return render(request, 'index.html')

def consultar(request):
    clientes = User.objects.all()
    return render(request, 'consulta-clientes.html', {'clientes': clientes})

def excluir(request, id):
    cliente = get_object_or_404(User, id=id)
    cliente.delete()
    return render(request, 'consulta-clientes.html')


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

    user = User.objects.filter(username=username).first()
    
    if user:
        # User with that username already exists
        mensagem = "Já existe um usuário com esse username."
        return render(request, 'cadastro.html', {'mensagem': mensagem})

    
    user = User.objects.create_user(username=username, email=email, password=senha)
    user.save()

    mensagem = "Usuário cadastrado com sucesso!"
    return render(request, 'login.html', {'mensagem': mensagem})
    
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(request, username=username, password=senha)

        if user:
            if not user.is_staff:
                login_django(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                login_django(request, user)
                return HttpResponseRedirect(reverse('escolha-super'))
        else:
            mensagem = "Usuario ou Senha inválidos"
            return render(request, 'cadastro.html', {'mensagem': mensagem})
        
def logout(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponseRedirect(reverse('login'))
    
def escolhaSuper(request):
    return render(request,'escolha-super.html')




def reset_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        errors = {}
        if not username:
            errors['username'] = "Nome de usuário é obrigatório."
        if not new_password:
            errors['new_password'] = "Nova senha é obrigatória."
        if new_password != confirm_password:
            errors['confirm_password'] = "As senhas não coincidem."

        if errors:
            return render(request, 'reset_password.html', {'errors': errors})

        user = User.objects.filter(username=username).first()
        if user:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Senha redefinida com sucesso.')
            return redirect('login')
        else:
            errors['username'] = "Usuário não encontrado."
            return render(request, 'reset_password.html', {'errors': errors})
    return render(request, 'reset_password.html')





