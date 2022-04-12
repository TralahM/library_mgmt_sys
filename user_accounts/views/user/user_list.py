from django.views.generic import ListView

from user_accounts.models import User

class UserListView(ListView):
    model = User
    template_name = "user/user_list.html"
