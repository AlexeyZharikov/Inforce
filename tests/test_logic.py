import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_registration():
    client = APIClient()
    response = client.post('/api/register/', {
        'username': 'test_user',
        'password': 'test_password123'
    })
    assert response.status_code == 201


@pytest.mark.django_db
def test_get_menu_authorized():
    client = APIClient()
    user = User.objects.create_user(username='worker', password='password123')
    client.force_authenticate(user=user)
    response = client.get('/api/menu/today/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_menu_unauthorized():
    client = APIClient()
    response = client.get('/api/menu/today/')
    assert response.status_code == 401
