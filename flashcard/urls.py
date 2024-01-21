from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.novo , name='novo'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('iniciar_desafio/', views.iniciar_desafio, name='iniciar_desafio'),
    path('listar_desafio/', views.listar_desafio, name='listar_desafio'),
    path('desafio/<int:id>', views.desafio, name='desafio'),
    path('responder/<int:id>', views.responder, name='responder'),
    path('relatorio/<int:id>', views.relatorio, name='relatorio'),
]