# noinspection PyPackageRequirements
from django.contrib import admin

from .models import Artigo, Utilizador, Comentario, Categoria, Tag, Serie
from .models import Estatuto, Perfil, Visita, ConfigPontuacao

@admin.register(Utilizador)
class UtilizadorAdmin(admin.ModelAdmin):
    pass

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'resumo', 'conteudo', 'slug', 'estado',
                    'img_destaque', 'data_publicacao']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    pass

@admin.register(Estatuto)
class EstatutoAdmin(admin.ModelAdmin):
    pass

@admin.register(ConfigPontuacao)
class ConfigPontuacaoAdmin(admin.ModelAdmin):
    pass

@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    pass


@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    pass


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    pass
