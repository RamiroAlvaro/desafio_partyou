import pytest
from django.urls import reverse
from model_bakery import baker

from partyou.core.models import Product
from partyou.django_assertions import assert_equal, assert_template_used, assert_contains


@pytest.fixture
def product(db):
    return baker.make(Product)


@pytest.fixture
def resp(client_user_admin, product):
    resp = client_user_admin.get(reverse('list_products'))
    return resp


def test_list_products_status_code(resp):
    assert_equal(resp.status_code, 200)


def test_list_products_template(resp):
    assert_template_used(resp, 'core/list_products.html')


def test_product_name(resp, product: Product):
    assert_contains(resp, product.name)


def test_product_description(resp, product: Product):
    assert_contains(resp, product.description)


def test_product_price(resp, product: Product):
    assert_contains(resp, (str(product.price)).replace('.', ','))
