from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path ('', views.index, name="index"),
    path('sobre/', views.sobre, name="sobre"),
    path('contato/', views.contato, name="contato"),
    path('ajuda/', views.ajuda, name="ajuda"),
    path('perfil/<str:usuario>/', views.perfil, name='perfil'),
    path('dia/<int:dia>/', views.dia_da_semana, name='dia_da_semana'),
    path('item/<int:id>/', views.exibir_item, name='exibir_item'),
    path('produto/', views.produto, name='produto'),    
    path('produto/form/', views.form_produto, name='form_produto'),
    path('produto/detalhes/<int:id>/', views.detalhes_produto, name='detalhes_produto'),
    path('produto/editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('produto/excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),

]
