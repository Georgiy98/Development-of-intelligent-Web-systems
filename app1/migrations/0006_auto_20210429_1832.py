# Generated by Django 3.1.8 on 2021-04-29 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20210429_1147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'article', 'verbose_name_plural': 'articles'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'comment', 'verbose_name_plural': 'comments'},
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content_en',
            field=models.TextField(null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content_ru',
            field=models.TextField(null=True, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='static', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=120, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_en',
            field=models.CharField(max_length=120, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_ru',
            field=models.CharField(max_length=120, null=True, verbose_name='title'),
        ),
    ]