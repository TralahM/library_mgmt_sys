from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user_accounts.models import User

# Register your models here.


class UserAdmin(BaseUserAdmin):
    """Base User Admin."""


admin.site.register(User, UserAdmin)
