from django.urls import path
from . import views


urlpatterns = [
    path ('', views.inicio, name="inicio"),
    path('cadastrar/', views.cadastrar, name='cadastrar_alunos'),
    path('listar/', views.listar, name='listar_alunos'),
]