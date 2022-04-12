from django.test import TestCase
from django.urls import reverse

class IssuedBookUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_issued_book_update_page(self):
        response = self.client.get(reverse('issued_book_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'issued_book/issued_book_update.html')