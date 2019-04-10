from django.contrib import admin

from .models import Articles, Tags, ArticleTag

class ArticlesTagInline(admin.StackedInline):
    model = ArticleTag
    extra = 1


class ArticlesAdmin(admin.ModelAdmin):
    inlines = [ArticlesTagInline]

# Register your models here.

admin.site.register(Tags)
admin.site.register(Articles, ArticlesAdmin)
