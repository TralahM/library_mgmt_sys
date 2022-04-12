from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from user_accounts.models import Student

class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student/student_delete.html"
    success_url = reverse_lazy('student_list')