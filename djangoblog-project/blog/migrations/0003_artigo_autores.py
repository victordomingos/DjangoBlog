# Generated by Django 3.0.6 on 2020-05-20 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200520_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='autores',
            field=models.ManyToManyField(to='blog.Utilizador'),
        ),
    ]
