from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home.html')

def my_view(request):
  return HttpResponse("Uma teste string de resposta")

def user_view(request, username):
  return HttpResponse(f"Perfil do usuario: {username}")

def root_view(request):
  return HttpResponse("Estamos na Raiz. Porta 8000")