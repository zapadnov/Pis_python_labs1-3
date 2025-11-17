from django.contrib import admin
from .models import Article

# Настройки отображения модели Article в админке
class ArticleAdmin(admin.ModelAdmin):
    # указываю, какие поля показывать в списке статей в админ-панели
    list_display = ("title", "author", "get_excerpt", "created_date")

# регистрирую модель Article в админке с настройками ArticleAdmin
admin.site.register(Article, ArticleAdmin)