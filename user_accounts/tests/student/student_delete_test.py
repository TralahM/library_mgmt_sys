from django.test import TestCase
from django.urls import reverse

class StudentDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_student_delete_page(self):
        response = self.client.get(reverse('student_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/student_delete.html')