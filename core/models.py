from django.db import models

class Empresa(models.Model):
    razao_social = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=20) 
    endereco = models.CharField(max_length=255)
    inscricao_estadual = models.CharField(max_length=50)

    def __str__(self):
        return self.razao_social