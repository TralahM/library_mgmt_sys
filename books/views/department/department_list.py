from django.views.generic import ListView
from django.db.models import Q

from books.models import Department


class DepartmentListView(ListView):
    model = Department
    template_name = "department/department_list.html"

    def get_queryset(self, *args, **kwargs):
        """Return appropriate queryset."""
        if not self.request.GET.get("q"):
            return Department.objects.all()
        return Department.objects.filter((Q(name__icontains=self.request.GET.get("q"))))
