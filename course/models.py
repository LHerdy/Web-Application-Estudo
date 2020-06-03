from django.db import models

# Create your models here.

class Course(models.Model):
    nome = models.CharField( max_length=100)
    atalho = models.SlugField()
    descricao = models.TextField(blank=True)
    data_de_inicio = models.DateField(null=True, blank=True)
    imagem = models.ImageField(upload_to='image', blank=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

