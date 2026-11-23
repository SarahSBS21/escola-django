from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)

    matricula = models.CharField(max_length=20, blank=True)
    cpf = models.CharField(max_length=11, blank=True)

    
    def __str__(self):
        return self.nome