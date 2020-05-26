from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.text import slugify
from django.views.generic.base import TemplateView

from partyou.core.forms import ProductForm
from partyou.core.models import Product


class HomePageView(TemplateView):
    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': 'Partyou o Desafio'})


def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.name)
            post.save()
            return redirect(reverse('list_products'))
    else:
        form = ProductForm()
    return render(request, 'core/create_product.html', {'form': form})


def list_products(request):
    products = Product.objects.all()
    return render(request, "core/list_products.html", {'products': products})
