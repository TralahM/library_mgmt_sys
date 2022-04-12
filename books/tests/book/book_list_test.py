from django.test import TestCase
from django.urls import reverse

class BookListTestCase(TestCase):
    def setUp(self):
        pass

    def test_book_list_page(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/book_list.html')