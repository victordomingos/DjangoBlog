# Generated by Django 3.0.6 on 2020-05-20 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200520_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='img_destaque',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagem de destaque'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
