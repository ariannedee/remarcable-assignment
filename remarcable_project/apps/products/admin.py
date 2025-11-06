from django.contrib import admin

from .models import Category, Product, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'description', 'category', 'get_tags')
    list_filter = ('category', 'tags')
    search_fields = ('description', 'category__name', 'tags__name')

    def get_tags(self, obj):
        return " | ".join([t.name for t in obj.tags.all()])

