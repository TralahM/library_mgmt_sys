from django.test import TestCase
from django.urls import reverse

class UserDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_user_detail_page(self):
        response = self.client.get(reverse('user_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/user_detail.html')