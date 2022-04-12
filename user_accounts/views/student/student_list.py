from django.views.generic import ListView

from user_accounts.models import Student

class StudentListView(ListView):
    model = Student
    template_name = "student/student_list.html"
