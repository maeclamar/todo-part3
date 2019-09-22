from django.contrib import admin

# Register your models here.
from .models import Blog, Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', 'updated_date')
    list_display_links = ('id', 'title')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
