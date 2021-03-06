# from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils import timezone
from hitcount.models import HitCount


class Artigo(models.Model):
    class EstadoArtigo(models.IntegerChoices):
        NOT_SAVED = 0, "Não guardado"
        RASCUNHO = 1, "Rascunho"
        AGUARDA_MODERACAO = 2, "Aguarda moderação"
        AGENDADO = 3, "Agendado"
        PUBLICADO = 4, "Publicado"

    autores = models.ManyToManyField('Autor')
    titulo = models.CharField('Título', max_length=256)
    resumo = models.CharField(max_length=512)
    conteudo = models.TextField('Conteúdo')
    slug = models.SlugField(max_length=64, default='', blank=True)
    categorias = models.ManyToManyField('Categoria')
    tags = models.ManyToManyField('Tag', related_name="Tópicos")
    serie = models.ForeignKey(
        'Serie',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    artigos_relacionados = models.ManyToManyField(
        'self', 
        related_name="artigos_relacionados", 
        blank=True
    )
    estado = models.IntegerField(
        choices=EstadoArtigo.choices,
        default=EstadoArtigo.NOT_SAVED
    )
    img_destaque = models.ImageField(
        "Imagem de destaque",
        upload_to='images/artigos',
        null=True, 
        blank=True
    )
    # visitas = models.ForeignKey(
    #     'Visita', on_delete=models.SET_NULL, null=True, blank=True)
    hit_count_generic = GenericRelation(
        HitCount,
        object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )
    gostos = models.BigIntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(null=True, blank=True)

    def publicar(self):
        self.data_publicacao = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=512)
    slug = models.SlugField(max_length=64)
    img = models.ImageField(upload_to='images/categorias')

    def __str__(self):
        return self.nome


class Tag(models.Model):
    nome = models.CharField(max_length=64)
    img = models.ImageField(upload_to='images/tags', null=True, blank=True)

    def __str__(self):
        return self.nome


class Serie(models.Model):
    titulo = models.CharField("Título", max_length=256)
    descricao = models.CharField(max_length=512)
    img_destaque = models.ImageField(
        "Imagem de destaque", 
        upload_to='images/series', 
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    class EstadoComentario(models.IntegerChoices):
        NOT_SAVED = 0, "Não guardado"
        RASCUNHO = 1, "Rascunho"
        PENDENTE = 2, "Aguarda moderação"
        ELIMINADO = 3, "Eliminado"
        SPAM = 4, "Marcado como Spam"
        APROVADO = 5, "Aprovado"

    escrito_por = models.ForeignKey('Autor', on_delete=models.CASCADE)
    assunto = models.CharField(max_length=256)
    conteudo = models.TextField('Texto')
    artigo = models.ForeignKey(
        Artigo,
        on_delete=models.CASCADE,
        related_name='Comentários',
    )
    data = models.DateTimeField(default=timezone.now)
    estado = models.IntegerField(
        choices=EstadoComentario.choices,
        default=EstadoComentario.NOT_SAVED
    )
    thumbs_up = models.IntegerField(default=0)
    thumbs_down = models.IntegerField(default=0)

    def __str__(self):
        return self.assunto

    def publicar(self):
        self.data_publicacao = timezone.now()
        self.save()


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(default='')
    foto = models.ImageField(
        verbose_name="Fotografia",
        upload_to='images/autores',
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.nome


class Visita(models.Model):
    pass

    #def __str__(self):
    #    return self.titulo


class Perfil(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Estatuto(models.Model):
    designacao = models.CharField(max_length=64)
    icone = models.ImageField(upload_to='images/estatutos')
    pontuacao_min = models.IntegerField("Pontuação mínima", default=0)
    pontuacao_max = models.IntegerField("Pontuação mínima", default=0)

    def __str__(self):
        return self.designacao


class ConfigPontuacao(models.Model):
    pass

    #def __str__(self):
    #    return self.titulo
