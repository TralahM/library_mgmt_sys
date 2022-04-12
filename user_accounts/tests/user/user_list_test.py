from django.test import TestCase
from django.urls import reverse

class UserListTestCase(TestCase):
    def setUp(self):
        pass

    def test_user_list_page(self):
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/user_list.html')