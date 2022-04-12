from django.test import TestCase
from django.urls import reverse

class IssuedBookDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_issued_book_delete_page(self):
        response = self.client.get(reverse('issued_book_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'issued_book/issued_book_delete.html')