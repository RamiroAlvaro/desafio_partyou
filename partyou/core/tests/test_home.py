import pytest
from django.urls import reverse

from partyou.django_assertions import assert_contains, assert_equal, assert_template_used


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('home'))
    return resp


def test_status_code(resp):
    assert_equal(resp.status_code, 200)


def test_home_template(resp):
    assert_template_used(resp, 'core/home.html')


def test_title(resp):
    assert_contains(resp, '<title>Partyou - Desafio</title>')


def test_home_link(resp):
    assert_contains(resp, f'<a class="navbar-brand" href="{reverse("home")}">Partyou</a>')
