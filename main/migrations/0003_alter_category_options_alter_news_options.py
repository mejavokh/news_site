# Generated by Django 5.0.7 on 2024-07-24 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_news_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]