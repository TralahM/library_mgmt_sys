from django.views.generic import ListView
from django.db.models import Q

from user_accounts.models import Student


class StudentListView(ListView):
    model = Student
    template_name = "student/student_list.html"

    def get_queryset(self, *args, **kwargs):
        """Return appropriate queryset."""
        if not self.request.GET.get("q"):
            return Student.objects.all()
        return Student.objects.filter(
            (Q(library_card_number__icontains=self.request.GET.get("q")))
        )
