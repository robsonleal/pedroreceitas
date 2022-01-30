from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('receita&=<int:receita_id>', receita, name='receita'),
    path('buscar/', buscar, name='buscar'),
    path('criar/receita', criar_receita, name='criar_receita'),
    path('deletar/<int:receita_id>', deletar_receita, name='deletar_receita'),
    path('editar/<int:receita_id>', editar_receita, name='editar_receita'),
    path('atualizar_receita', atualizar_receita, name='atualizar_receita'),
]