from django.test import TestCase
from django.urls import reverse

class DepartmentListTestCase(TestCase):
    def setUp(self):
        pass

    def test_department_list_page(self):
        response = self.client.get(reverse('department_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department/department_list.html')