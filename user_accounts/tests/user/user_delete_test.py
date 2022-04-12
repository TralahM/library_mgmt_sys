from django.test import TestCase
from django.urls import reverse

class UserDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_user_delete_page(self):
        response = self.client.get(reverse('user_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/user_delete.html')