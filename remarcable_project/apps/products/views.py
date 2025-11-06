from django.shortcuts import render

from .models import Category, Product, Tag


def index(request):
    filter_dict = request.GET
    search = filter_dict.get('search')
    category = filter_dict.get('category')
    tags = [int(pk) for pk in filter_dict.getlist('tags')]

    qs = Product.objects.all()

    if search:
        qs = qs.filter(name__icontains=search)

    if category:
        qs = qs.filter(category__pk=category)

    if tags:
        qs = qs.filter(tags__pk__in=tags)

    context = {
        "categories": Category.objects.all(),
        "tags": Tag.objects.all(),
        "products": qs.select_related('category').prefetch_related('tags'),
        "selected_tags": tags,
    }
    return render(request, "products/index.html", context=context)
