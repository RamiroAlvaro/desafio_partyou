import pytest
from django.urls import reverse
from model_bakery import baker

from partyou.core.models import Order
from partyou.django_assertions import assert_equal, assert_template_used, assert_contains


@pytest.fixture
def order(db):
    return baker.make(Order)


@pytest.fixture
def resp(client, order):
    resp = client.get(reverse('list_orders'))
    return resp


def test_list_orders_status_code(resp):
    assert_equal(resp.status_code, 200)


def test_list_orders_template(resp):
    assert_template_used(resp, 'core/list_orders.html')


def test_number_of_order(resp, order: Order):
    assert_contains(resp, order.id)


def test_email_client(resp, order: Order):
    assert_contains(resp, order.user.email)


def test_order_status(resp, order: Order):
    assert_contains(resp, order.get_status_display())
