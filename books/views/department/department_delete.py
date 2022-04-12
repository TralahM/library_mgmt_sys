from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from books.models import Department

class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = "department/department_delete.html"
    success_url = reverse_lazy('department_list')