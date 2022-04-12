from django.test import TestCase
from django.urls import reverse

class IssuedBookCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_issued_book_create_page(self):
        response = self.client.get(reverse('issued_book_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'issued_book/issued_book_create.html')