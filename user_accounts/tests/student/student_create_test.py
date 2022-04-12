from django.test import TestCase
from django.urls import reverse

class StudentCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_student_create_page(self):
        response = self.client.get(reverse('student_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/student_create.html')