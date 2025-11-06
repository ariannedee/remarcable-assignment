from django.shortcuts import render

from .models import Category, Product, Tag


def index(request):
    filter_dict = request.GET
    search = filter_dict.get('search')
    category = filter_dict.get('category')

    qs = Product.objects.all()

    if search:
        qs = qs.filter(name__contains=search)

    if category:
        qs = qs.filter(category__pk=category)

    context = {
        "categories": Category.objects.all(),
        "tags": Tag.objects.all(),
        "products": qs,
    }
    return render(request, "products/index.html", context=context)
