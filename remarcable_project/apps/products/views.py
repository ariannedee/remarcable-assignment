from django.shortcuts import render

from .models import Category, Product, Tag


def index(request):
    print(request.POST)
    context = {
        "categories": Category.objects.all(),
        "tags": Tag.objects.all(),
        "products": Product.objects.all(),
    }
    return render(request, "products/index.html", context=context)
