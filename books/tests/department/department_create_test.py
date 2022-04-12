from django.test import TestCase
from django.urls import reverse

class DepartmentCreateTestCase(TestCase):
    def setUp(self):
        pass

    def test_department_create_page(self):
        response = self.client.get(reverse('department_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department/department_create.html')