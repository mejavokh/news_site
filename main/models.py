from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название новости')
    desc = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    photo = models.ImageField(upload_to='news/', null=True, blank=True, verbose_name='Изображение')
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категории')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name='Комментарии')

    def __str__(self):
        return self.author.username



