from django.test import TestCase
from django.urls import reverse

class StudentUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_student_update_page(self):
        response = self.client.get(reverse('student_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/student_update.html')