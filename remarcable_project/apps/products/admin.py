from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'get_tags')
    list_filter = ('category', 'tags')
    search_fields = ('name', 'category__name', 'tags__name')

    def get_tags(self, obj):
        return " | ".join([t.name for t in obj.tags.all()])

