from django.test import TestCase
from django.urls import reverse

class BookDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_book_delete_page(self):
        response = self.client.get(reverse('book_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/book_delete.html')