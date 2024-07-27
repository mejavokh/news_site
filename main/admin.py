from django.contrib import admin

from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'created_at', 'photo', 'views', 'category')


admin.site.register(News, NewsAdmin)
admin.site.register(Category)
