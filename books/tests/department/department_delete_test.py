from django.test import TestCase
from django.urls import reverse

class DepartmentDeleteTestCase(TestCase):
    def setUp(self):
        pass

    def test_department_delete_page(self):
        response = self.client.get(reverse('department_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department/department_delete.html')