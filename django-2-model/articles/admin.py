from django.contrib import admin
from .models import Article
# Register your models here.

# admin.site.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)