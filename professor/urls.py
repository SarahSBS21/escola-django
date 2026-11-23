from django.urls import path
from . import views


urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar_professor'),
    path('listar/', views.listar, name='listar_professores'),
]