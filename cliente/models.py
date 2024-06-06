from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=40)
    cpf = models.CharField(max_length=15, unique=True)
    email = models.CharField(max_length=40, unique = True)
    senha = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
