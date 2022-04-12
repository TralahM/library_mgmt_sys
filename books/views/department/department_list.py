from django.views.generic import ListView

from books.models import Department

class DepartmentListView(ListView):
    model = Department
    template_name = "department/department_list.html"
