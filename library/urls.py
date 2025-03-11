from django.contrib import admin
from django.urls import path

from library.views import home, my_view, root_view, user_view

urlpatterns = [
    path('home/', home),
    path('', root_view),
    path('sobre/', my_view),
    path('user/<str:username>/', user_view),
]
