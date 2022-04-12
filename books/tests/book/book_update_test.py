from django.test import TestCase
from django.urls import reverse

class BookUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_book_update_page(self):
        response = self.client.get(reverse('book_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/book_update.html')