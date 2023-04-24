from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import include, path, reverse

from .models import Role


class RoleTest(APITestCase):
    def test_create_role(self):
        url = reverse('role-list')
        data = {'name': 'unit testing role'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Role.objects.get().title,
                         'unit testing role')

