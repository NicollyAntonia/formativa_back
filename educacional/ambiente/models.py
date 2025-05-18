from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    is_gestor = models.BooleanField(default=False)
    telefone = models.CharField(max_length=20, blank=True)


class Professor(models.Model):
    usuario = models.OneToOneField('ambiente.Usuario', on_delete=models.CASCADE)
    ni = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    data_contratacao = models.DateField()

    def __str__(self):
        return self.usuario.get_full_name()


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    descricao = models.TextField()
    professor_responsavel = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, related_name='disciplinas')

    def __str__(self):
        return self.nome


class ReservaAmbiente(models.Model):
    PERIODO_CHOICES = [('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')]

    data_inicio = models.DateField()
    data_termino = models.DateField()
    periodo = models.CharField(max_length=1, choices=PERIODO_CHOICES)
    sala = models.CharField(max_length=50)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sala} ({self.data_inicio} - {self.data_termino})"
