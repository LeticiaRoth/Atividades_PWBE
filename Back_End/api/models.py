from django.db import models #Caixa preta, não sei como funciona, mas está sendo executado

# 1 - API faz tudo dentro do django
#Cria a tabela 
class Autor(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    dataNascimento = models.DateField(null=True, blank=True)
    nacao = models.CharField(max_length=30, null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"


