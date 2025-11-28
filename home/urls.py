
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path ('', views.index, name="index"),
    path('sobre/', views.sobre, name="sobre"),
    path('contato/', views.contato, name="contato"),
    path('ajuda/', views.ajuda, name="ajuda"),
    
]
