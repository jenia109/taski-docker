from http import HTTPStatus
from api import models
from django.contrib.auth import get_user_model
from django.test import Client, TestCase

User = get_user_model()

class TaskiAPITestCase(TestCase):
    def setUp(self):
        self.guest_client = Client()
        self.user = User.objects.create_user(username='test_user', password='123')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_list_exists(self):
        """Проверка доступности списка задач."""
        response = self.guest_client.get('/api/tasks/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        """Проверка создания задачи авторизованным пользователем."""
        data = {'title': 'Test', 'description': 'Test'}
        response = self.authorized_client.post('/api/tasks/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(models.Task.objects.filter(title='Test').exists())
