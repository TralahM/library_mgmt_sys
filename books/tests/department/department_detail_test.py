from django.test import TestCase
from django.urls import reverse

class DepartmentDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_department_detail_page(self):
        response = self.client.get(reverse('department_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'department/department_detail.html')