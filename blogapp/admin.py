from django.contrib import admin

from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'content']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'user', 'content']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog', 'user', 'text']


