from django.test import TestCase
from django.urls import reverse

class StudentDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_student_detail_page(self):
        response = self.client.get(reverse('student_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/student_detail.html')