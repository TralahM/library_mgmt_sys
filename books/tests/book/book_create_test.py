from django.test import TestCase
from django.urls import reverse

class BookCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_book_create_page(self):
        response = self.client.get(reverse('book_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/book_create.html')