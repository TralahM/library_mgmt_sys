from django.views.generic import DetailView

from user_accounts.models import Student


class StudentDetailView(DetailView):
    model = Student
    template_name = "student/student_detail.html"
