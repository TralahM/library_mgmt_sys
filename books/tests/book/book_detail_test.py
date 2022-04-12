from django.test import TestCase
from django.urls import reverse

class BookDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_book_detail_page(self):
        response = self.client.get(reverse('book_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/book_detail.html')