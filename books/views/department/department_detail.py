from django.views.generic import DetailView

from books.models import Department


class DepartmentDetailView(DetailView):
    model = Department
    template_name = "department/department_detail.html"
