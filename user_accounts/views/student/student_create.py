from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from user_accounts.models import Student

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    template_name = "student/student_create.html"
    success_url = reverse_lazy('student_list')
