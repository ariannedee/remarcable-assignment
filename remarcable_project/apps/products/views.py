from django.shortcuts import render

from .models import Product


def index(request):
    qs = Product.objects.all()
    context = {"products": qs}
    return render(request, "products/index.html", context=context)
