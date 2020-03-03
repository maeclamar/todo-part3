from django.contrib import admin

# Register your models here.
from .models import Blog, Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', 'updated_date')
    list_display_links = ('id', 'title')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'text', 'created_date')
    list_display_links = ('id',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
