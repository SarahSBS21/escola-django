from django.shortcuts import render, redirect
from .models import Livro

# Create your views here.

def cadastrar(request):

    if request.method == 'POST':
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        editora = request.POST['editora']
        ano_publicacao = request.POST['ano_publicacao']
        isbn = request.POST['isbn']

        livro = Livro(
            titulo=titulo,
            autor=autor,
            editora=editora,
            ano_publicacao=ano_publicacao,
            isbn=isbn
        )

        livro.save()

        return redirect('listar_livros')

    return render(request, 'livros/cadastrar.html')


def listar(request):

    livros = Livro.objects.all()

    return render(
        request,
        'livros/listar.html',
        {'livros': livros}
    )