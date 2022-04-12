from django.test import TestCase
from django.urls import reverse

class UserUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_user_update_page(self):
        response = self.client.get(reverse('user_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/user_update.html')