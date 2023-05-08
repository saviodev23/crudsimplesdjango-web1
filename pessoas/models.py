from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    idade = models.IntegerField(blank=False, null=False)
    cpf = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.nome