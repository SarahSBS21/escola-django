from django.shortcuts import render, redirect
from .models import Professor

# Create your views here.
def cadastrar(request):

    if request.method == 'POST':
        nome = request.POST['nome']
        disciplina = request.POST['disciplina']
        email = request.POST['email']
        telefone = request.POST['telefone']

        professor = Professor(
            nome=nome,
            disciplina=disciplina,
            email=email,
            telefone=telefone
        )

        professor.save()

        return redirect('listar_professores')

    return render(request, 'professor/cadastrar.html')


def listar(request):

    professores = Professor.objects.all()

    return render(
        request,
        'professor/listar.html',
        {'professores': professores}
    )