from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from user_accounts.models import User

class UserUpdateView(UpdateView):
    model = User
    fields = '__all__'
    template_name = "user/user_update.html"
    success_url = reverse_lazy('user_list')
