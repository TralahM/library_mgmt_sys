from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from books.models import Department

class DepartmentUpdateView(UpdateView):
    model = Department
    fields = '__all__'
    template_name = "department/department_update.html"
    success_url = reverse_lazy('department_list')
