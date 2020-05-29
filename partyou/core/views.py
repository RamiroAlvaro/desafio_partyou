from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.text import slugify
from django.views.generic.base import TemplateView

from partyou.core.forms import ProductForm
from partyou.core.models import Product, Order, OrderProduct


class HomePageView(TemplateView):
    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': 'Partyou o Desafio'})


@permission_required('is_staff')
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


@permission_required('is_staff')
def list_products(request):
    products = Product.objects.all()
    return render(request, "core/list_products.html", {'products': products})


@permission_required('is_staff')
def list_orders(request):
    orders = Order.objects.all()
    return render(request, "core/list_orders.html", {'orders': orders})


@permission_required('is_staff')
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_products = OrderProduct.objects.select_related('order').filter(order_id=order_id)
    return render(request, "core/order_detail.html", {'order_products': order_products, 'order': order})


@permission_required('is_staff')
def update_order(request, order_id):
    if request.method == "POST":
        order = get_object_or_404(Order, id=order_id)
        order.status = request.POST['status']
        order.save()

    return redirect(reverse('list_orders'))
