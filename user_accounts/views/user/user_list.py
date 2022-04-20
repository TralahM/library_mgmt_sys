from django.views.generic import ListView
from django.db.models import Q

from user_accounts.models import User


class UserListView(ListView):
    model = User
    template_name = "user/user_list.html"

    def get_queryset(self, *args, **kwargs):
        """Return appropriate queryset."""
        if not self.request.GET.get("q"):
            return User.objects.all()
        return User.objects.filter(
            (
                Q(first_name__icontains=self.request.GET.get("q"))
                | Q(last_name__icontains=self.request.GET.get("q"))
                | Q(email__icontains=self.request.GET.get("q"))
            )
        )
