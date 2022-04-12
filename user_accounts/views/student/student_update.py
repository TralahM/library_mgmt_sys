from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from user_accounts.models import Student

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    template_name = "student/student_update.html"
    success_url = reverse_lazy('student_list')
