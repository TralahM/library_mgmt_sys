from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from user_accounts.models import User

class UserDeleteView(DeleteView):
    model = User
    template_name = "user/user_delete.html"
    success_url = reverse_lazy('user_list')