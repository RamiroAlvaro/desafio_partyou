import pytest
from model_bakery import baker

from partyou.core.models import Product, Order, OrderProduct
from partyou.django_assertions import assert_true, assert_equal


@pytest.fixture
def products(db):
    return baker.make(Product, _quantity=2)


@pytest.fixture
def order(db):
    return baker.make(Order)


@pytest.fixture
def order_product(db, products, order):
    return baker.make(OrderProduct, product=products[1], order=order)


def test_create_products(products):
    assert_equal(Product.objects.all().count(), 2)


def test_create_order(order: Order):
    assert_true(Order.objects.exists())
    assert_equal(Order.objects.all().count(), 1)


def test_create_order_product(order_product: OrderProduct):
    assert_true(OrderProduct.objects.exists())
    assert_equal(OrderProduct.objects.all().count(), 1)
