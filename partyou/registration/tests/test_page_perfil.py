import pytest
from django.urls import reverse

from partyou.django_assertions import assert_contains, assert_equal, assert_template_used, assert_not_contains


@pytest.fixture
def resp(client_with_logged_user, db):
    resp = client_with_logged_user.get(reverse('profile'))
    return resp


def test_status_code(resp):
    assert_equal(resp.status_code, 200)


def test_profile_template(resp):
    assert_template_used(resp, 'registration/profile_form.html')


def test_title(resp):
    assert_contains(resp, '<title>Perfil</title>')


def test_home_link(resp):
    assert_contains(resp, f'<a class="navbar-brand" href="{reverse("home")}">Partyou</a>')


def test_login_link(resp):
    assert_not_contains(resp, f'<a class="nav-link" href="{reverse("login")}">Acessar</a>')


def test_logout_link(resp):
    assert_contains(resp, f'<a class="nav-link" href="{reverse("logout")}">Sair</a>')
