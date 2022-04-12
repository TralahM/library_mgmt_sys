from django.test import TestCase
from django.urls import reverse

class StudentListTestCase(TestCase):
    def setUp(self):
        pass

    def test_student_list_page(self):
        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/student_list.html')