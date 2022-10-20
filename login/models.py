from email.policy import default
from django.db import models
from pessoas.models import Pessoa

# Create your models here.
class Aulas(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_aula = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    foto_aula = models.ImageField(upload_to='fotos/%d%m%Y/', blank=True)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_aula