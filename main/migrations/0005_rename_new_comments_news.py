# Generated by Django 5.0.7 on 2024-07-26 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='new',
            new_name='news',
        ),
    ]
