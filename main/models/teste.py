from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='funcionarios')
    projetos = models.ManyToManyField('Projeto', related_name='funcionarios')

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    departamentos = models.ManyToManyField(Departamento, related_name='projetos')
    funcionarios = models.ManyToManyField(Funcionario, related_name='projetos')

    def __str__(self):
        return self.nome














funcionario = Funcionario.objects.filter(
    email = 'joaopedro@gmail.com'
).select_related('departamento').prefetch_related('projetos')