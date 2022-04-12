from django.views.generic import DetailView

from user_accounts.models import User


class UserDetailView(DetailView):
    model = User
    template_name = "user/user_detail.html"
