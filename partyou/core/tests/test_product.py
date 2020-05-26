import pytest
from django.urls import reverse
from model_bakery import baker

from partyou.core.models import Product
from partyou.django_assertions import assert_true, assert_equal, assert_false, assert_template_used


@pytest.fixture
def product(db):
    return baker.make(Product)


@pytest.fixture
def resp(client):
    resp = client.get(reverse('create_product'))
    return resp


def test_create_product_status_code(resp):
    assert_equal(resp.status_code, 200)


def test_create_product_template(resp):
    assert_template_used(resp, 'core/create_product.html')


def test_create(product: Product):
    assert_true(Product.objects.exists())
    assert_equal(Product.objects.all().count(), 1)


def test_description_can_be_blank(product: Product):
    field = product._meta.get_field('description')
    assert_true(field.blank)


def test_name_can_not_be_blank(product: Product):
    field = product._meta.get_field('name')
    assert_false(field.blank)


def test_price_can_not_be_blank(product: Product):
    field = product._meta.get_field('price')
    assert_false(field.blank)


def test_str(product: Product):
    assert_equal(product.name, str(product))
