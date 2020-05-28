import pytest
from django.urls import reverse

from partyou.django_assertions import assert_contains, assert_equal, assert_template_used


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('login'))
    return resp


def test_status_code(resp):
    assert_equal(resp.status_code, 200)


def test_login_template(resp):
    assert_template_used(resp, 'registration/login.html')


def test_title(resp):
    assert_contains(resp, '<title>Iniciar sessão</title>')


def test_home_link(resp):
    assert_contains(resp, f'<a class="navbar-brand" href="{reverse("home")}">Partyou</a>')


def test_login_link(resp):
    assert_contains(resp, f'<a class="nav-link" href="{reverse("login")}">Acessar</a>')
