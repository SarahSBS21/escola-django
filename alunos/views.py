from django.shortcuts import render, redirect
from .models import Aluno

# Create your views here.

def cadastrar(request):

    if request.method == 'POST':
        nome = request.POST['nome']
        idade = request.POST['idade']
        email = request.POST['email']
        telefone = request.POST['telefone']
        endereco = request.POST['endereco']

        matricula = request.POST['matricula']
        cpf = request.POST['cpf']

        aluno = Aluno(
            nome=nome,
            idade=idade,
            email=email,
            telefone=telefone,
            endereco=endereco,
            matricula=matricula,
            cpf=cpf
        )

        aluno.save()

        return redirect('listar_alunos')

    return render(request, 'alunos/cadastrar.html')


def listar(request):

    alunos = Aluno.objects.all()

    return render(
        request,
        'alunos/listar.html',
        {'alunos': alunos}
    )