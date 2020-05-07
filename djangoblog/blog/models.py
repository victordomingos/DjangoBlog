from django.conf import settings
from django.db import models
from django.utils import timezone


class Artigo(models.Model):
    #autores
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=256)
    resumo = models.CharField(max_length=512)
    conteudo = models.TextField()
    #slug
    #categorias
    #topicos
    #artigos_relacionados
    #estado
    #img_destaque
    #comentarios
    #visualizacoes
    #gostos
    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.data_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo



