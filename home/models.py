from django.db import models

# Create your models here.
from django.db import models

class Usuario(models.Model):
    cpf = models.IntegerField(unique=True)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self):
        return f'{self.nome} ({self.cpf})'

