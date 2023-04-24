from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import include, path, reverse

from .models import Process, ProcessType


class ProcessTypesTest(APITestCase):
    def test_create_process_type(self):
        url = reverse('processType-list')
        data = {'name': 'unit testing process type'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProcessType.objects.get().title,
                         'unit testing process type')


class ProcessesTest(APITestCase):
    def test_create_process(self):
        url = reverse('process-list')
        data = {'title': 'unit testing process',
                'description': 'test description', 'process_type': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Process.objects.get().title, 'unit testing process')

    def test_get_all_processes(self):
        url = reverse('process-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
