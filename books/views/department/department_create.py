from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from books.models import Department

class DepartmentCreateView(CreateView):
    model = Department
    fields = '__all__'
    template_name = "department/department_create.html"
    success_url = reverse_lazy('department_list')
