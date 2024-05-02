from django.contrib import admin

# Register your models here.

from .models import Category, News, Contact


class NewsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'body']
    list_display = ['title', 'category', 'status', 'published_time']
    list_filter = ['category', 'status']
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['nomi', 'id']


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact)
