# Generated by Django 3.0.6 on 2020-05-24 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200520_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='artigos_relacionados',
            field=models.ManyToManyField(blank=True, related_name='_artigo_artigos_relacionados_+', to='blog.Artigo'),
        ),
        migrations.AlterField(
            model_name='artigo',
            name='img_destaque',
            field=models.ImageField(blank=True, null=True, upload_to='images/artigos', verbose_name='Imagem de destaque'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='img',
            field=models.ImageField(upload_to='images/categorias'),
        ),
        migrations.AlterField(
            model_name='estatuto',
            name='icone',
            field=models.ImageField(upload_to='images/estatutos'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='img_destaque',
            field=models.ImageField(blank=True, null=True, upload_to='images/series', verbose_name='Imagem de destaque'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/tags'),
        ),
        migrations.AlterField(
            model_name='utilizador',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='images/utilizadores', verbose_name='Fotografia'),
        ),
    ]
