from django.db import models

# Create your models here.

class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(nome_icontains=query) |
            models.Q(description_icontains=query)
        )


class Course(models.Model):
    nome = models.CharField('Nome', max_length=100)
    atalho = models.SlugField('Atalho')
    descricao = models.TextField('Descrição', blank=True)
    data_de_inicio = models.DateField('Data de início', null=True, blank=True)
    imagem = models.ImageField('Imagem', upload_to='image', blank=True)
    criado = models.DateTimeField('Criado em:', auto_now_add=True)
    atualizado = models.DateTimeField('Atualizado', auto_now=True)


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Curso'
        ordering = ['nome']
