from django.urls import path
from user_accounts.views import StudentDeleteView
from user_accounts.views import StudentUpdateView
from user_accounts.views import StudentDetailView
from user_accounts.views import StudentCreateView
from user_accounts.views import StudentListView
from user_accounts.views import UserDeleteView
from user_accounts.views import UserUpdateView
from user_accounts.views import UserDetailView
from user_accounts.views import UserCreateView
from user_accounts.views import UserListView

urlpatterns = [
    path("user/list/", UserListView.as_view(), name="user_list"),
    path("user/create/", UserCreateView.as_view(), name="user_create"),
    path("user/detail/<str:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("user/update/<str:pk>/", UserUpdateView.as_view(), name="user_update"),
    path("user/delete/<str:pk>/", UserDeleteView.as_view(), name="user_delete"),
    path("student/list/", StudentListView.as_view(), name="student_list"),
    path("student/create/", StudentCreateView.as_view(), name="student_create"),
    path(
        "student/detail/<int:pk>/", StudentDetailView.as_view(), name="student_detail"
    ),
    path(
        "student/update/<int:pk>/", StudentUpdateView.as_view(), name="student_update"
    ),
    path(
        "student/delete/<int:pk>/", StudentDeleteView.as_view(), name="student_delete"
    ),
]
