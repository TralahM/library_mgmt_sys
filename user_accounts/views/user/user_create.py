from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from user_accounts.models import User

class UserCreateView(CreateView):
    model = User
    fields = '__all__'
    template_name = "user/user_create.html"
    success_url = reverse_lazy('user_list')
