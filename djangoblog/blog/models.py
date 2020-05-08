# from django.conf import settings
from django.db import models
from django.utils import timezone


class Utilizador(models.Model):
    nome = models.CharField(max_length=100)


class Artigo(models.Model):
    class EstadoArtigo(models.IntegerChoices):
        NOT_SAVED = 0, "Não guardado"
        RASCUNHO = 1, "Rascunho"
        AGUARDA_MODERACAO = 2, "Aguarda moderação"
        AGENDADO = 3, "Agendado"
        PUBLICADO = 4, "Publicado"

    autores = models.ManyToManyField(Utilizador)
    titulo = models.CharField("Título", max_length=256)
    resumo = models.CharField(max_length=512)
    conteudo = models.TextField("Conteúdo")
    slug = models.SlugField(max_length=64, blank=True)
    # categorias = ManyToManyField(Categoria)
    # tags = ManyToManyField("Tópicos", Tag)
    # serie = ForeignKey("Série", Serie)
    # artigos_relacionados = models.ManyToManyField(Artigo)
    estado = models.IntegerField(choices=EstadoArtigo.choices,
                                 default=EstadoArtigo.NOT_SAVED)
    img_destaque = models.ImageField("Imagem de destaque", null=True)
    # comentarios = ForeignKey("Comentários", Comentario)
    # visitas = ForeignKey(Visita)
    gostos = models.BigIntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.data_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=512)
    slug = models.SlugField(max_length=64)
    artigos = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    img = models.ImageField()

    def __str__(self):
        return self.nome


class Tag(models.Model):
    nome = models.CharField(max_length=64)
    artigos = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    img = models.ImageField()

    def __str__(self):
        return self.nome


class Serie(models.Model):
    titulo = models.CharField("Título", max_length=256)
    descricao = models.CharField(max_length=512)
    artigos = models.ManyToManyField(Artigo)
    img_destaque = models.ImageField("Imagem de destaque")

    def __str__(self):
        return self.titulo


class EstadoComentario(models.IntegerChoices):
    NOT_SAVED = 0, "Não guardado"
    RASCUNHO = 1, "Rascunho"
    PENDENTE = 2, "Aguarda moderação"
    ELIMINADO = 3, "Eliminado"
    SPAM = 4, "Marcado como Spam"
    APROVADO = 5, "Aprovado"


class Comentario(models.Model):
    # autores
    escrito_por = models.ForeignKey(Utilizador, on_delete=models.CASCADE)
    assunto = models.CharField(max_length=256)
    texto = models.CharField(max_length=1024)
    conteudo = models.TextField()
    artigo = models.ForeignKey(Artigo,
                               on_delete=models.CASCADE,
                               related_name='students',
                               related_query_name='person',
                               )
    data = models.DateTimeField(default=timezone.now)
    estado = models.IntegerField(choices=EstadoComentario.choices,
                                 default=EstadoComentario.NOT_SAVED)
    thumbs_up = models.IntegerField(default=0)
    thumbs_down = models.IntegerField(default=0)

    def publicar(self):
        self.data_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo


class Estatuto(models.Model):
    designacao = models.CharField(max_length=64)
    icone = models.ImageField()
    pontuacao_min = models.IntegerField("Pontuação mínima", default=0)
    pontuacao_max = models.IntegerField("Pontuação mínima", default=0)

    def __str__(self):
        return self.designacao


class Visita(models.Model):
    pass

    def __str__(self):
        return self.titulo


class Perfil(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class ConfigPontuacao(models.Model):
    pass

    def __str__(self):
        return self.titulo
