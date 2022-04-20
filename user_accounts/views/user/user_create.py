from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django import forms
from user_accounts.models import User


class UserCreateForm(UserCreationForm):
    """User creation Form."""

    def save(self, commit=True):
        """Save the User."""
        user = super(UserCreationForm, self).save(commit=False)
        print(self.cleaned_data["password"])
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        """Meta class."""

        model = User

        fields = "__all__"


class UserCreateView(CreateView):
    model = User
    template_name = "user/user_create.html"
    success_url = reverse_lazy("user_list")
    form_class = UserCreateForm
