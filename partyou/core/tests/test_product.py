import pytest
from model_bakery import baker

from partyou.core.models import Product
from partyou.django_assertions import assert_true, assert_equal, assert_false


@pytest.fixture
def product(db):
    return baker.make(Product)


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
