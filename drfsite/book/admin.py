from django.contrib import admin

from .models import *

admin.site.register(Genre)


@admin.register(Post)  # регистрация приложения
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    list_display_links = ('id', 'title')
