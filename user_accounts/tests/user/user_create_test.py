from django.test import TestCase
from django.urls import reverse

class UserCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_user_create_page(self):
        response = self.client.get(reverse('user_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/user_create.html')