from django.contrib import admin
from .models import Article

# Register your models here.

# 新版支持写法
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "content", "created_time")
	ordering = ("id", )

# admin.site.register(Article, ArticleAdmin)