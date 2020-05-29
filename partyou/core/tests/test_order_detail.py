import pytest
from django.urls import reverse
from model_bakery import baker

from partyou.core.models import Order, OrderProduct
from partyou.django_assertions import assert_equal, assert_template_used, assert_contains


@pytest.fixture
def order(db):
    return baker.make(Order)


@pytest.fixture
def order_product(db):
    return baker.make(OrderProduct)


@pytest.fixture
def resp(client_user_admin, order, order_product, user_admin):
    resp = client_user_admin.get(reverse('order_detail', args=[order.id]))
    return resp


def test_update_order_status_code(resp):
    assert_equal(resp.status_code, 200)


def test_list_orders_template(resp):
    assert_template_used(resp, 'core/order_detail.html')


def test_number_of_order(resp, order: Order):
    assert_contains(resp, order.id)


def test_email_client(resp, order: Order):
    assert_contains(resp, order.user.email)


def test_order_status(resp, order: Order):
    assert_contains(resp, order.get_status_display())


def test_product_quantity(resp, order_product: OrderProduct):
    assert_contains(resp, order_product.quantity)
