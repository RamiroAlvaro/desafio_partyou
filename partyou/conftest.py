import pytest
from model_bakery import baker


@pytest.fixture
def user_admin(db, django_user_model):
    return baker.make(django_user_model, is_staff=True, is_superuser=True)


@pytest.fixture
def client_user_admin(client, user_admin):
    client.force_login(user_admin)
    return client


@pytest.fixture
def user_logged(db, django_user_model):
    user = baker.make(django_user_model, first_name='Ramiro')
    return user


@pytest.fixture
def client_with_logged_user(user_logged, client):
    client.force_login(user_logged)
    return client
