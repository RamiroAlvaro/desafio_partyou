import pytest
from django.contrib.auth.models import User
from model_bakery import baker

from partyou.django_assertions import assert_true
from partyou.registration.models import Profile


@pytest.fixture
def user(db, django_user_model):
    user = baker.make(django_user_model, username='Ramiro')
    return user


def test_profile_exists(user: User):
    exists = Profile.objects.filter(user__username=user.username).exists()
    assert_true(exists)
