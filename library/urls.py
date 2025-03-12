from django.contrib import admin
from django.urls import path

from .views import home, logout_view, my_view, login_view, root_view, user_view
from library import views

urlpatterns = [
    path('home/', home),
    path('', root_view),
    path('sobre/', my_view),
    path('user/<str:username>/', user_view),
    path('recuperar/', views.recuperar, name='recuperar'),  # Corrigido o nome da URL
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
