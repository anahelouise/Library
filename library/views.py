from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Se o formulário for válido, autentica o usuário
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Verifica se as credenciais estão corretas
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Se o usuário for autenticado, faz o login
                login(request, user)
                return redirect('home')  # Redireciona para a página inicial ou outra página
            else:
                # Se o login falhar
                error_message = "Usuário ou senha inválidos."
                return render(request, 'login.html', {'error_message': error_message})

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)  # Isso vai encerrar a sessão do usuário
    return redirect('login')  # Redireciona de volta para a página de login


from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'login.html')


def my_view(request):
  return HttpResponse("Uma teste string de resposta")

def user_view(request, username):
  return HttpResponse(f"Perfil do usuario: {username}")

def root_view(request):
   return render(request, 'library/login.html') 

def recuperar(request):
    return render(request, 'library/recuperar.html')  # Verifique o caminho correto para o template



