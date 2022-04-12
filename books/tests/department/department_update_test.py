from django.test import TestCase
from django.urls import reverse

class DepartmentUpdateTestCase(TestCase):
    def setUp(self):
        pass

    def test_department_update_page(self):
        response = self.client.get(reverse('department_update'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department/department_update.html')