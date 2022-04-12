from django.urls import path

from books.views import IssuedBookDeleteView
from books.views import IssuedBookUpdateView
from books.views import IssuedBookDetailView
from books.views import IssuedBookCreateView
from books.views import IssuedBookListView
from books.views import BookDeleteView
from books.views import BookUpdateView
from books.views import BookDetailView
from books.views import BookCreateView
from books.views import BookListView
from books.views import DepartmentDeleteView
from books.views import DepartmentUpdateView
from books.views import DepartmentDetailView
from books.views import DepartmentCreateView
from books.views import DepartmentListView

urlpatterns = [
    path("department/list/", DepartmentListView.as_view(), name="department_list"),
    path(
        "department/create/", DepartmentCreateView.as_view(), name="department_create"
    ),
    path(
        "department/detail/<str:pk>/",
        DepartmentDetailView.as_view(),
        name="department_detail",
    ),
    path(
        "department/update/<str:pk>/",
        DepartmentUpdateView.as_view(),
        name="department_update",
    ),
    path(
        "department/delete/<str:pk>/",
        DepartmentDeleteView.as_view(),
        name="department_delete",
    ),
    path("book/list/", BookListView.as_view(), name="book_list"),
    path("book/create/", BookCreateView.as_view(), name="book_create"),
    path("book/detail/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("book/update/<int:pk>/", BookUpdateView.as_view(), name="book_update"),
    path("book/delete/<int:pk>/", BookDeleteView.as_view(), name="book_delete"),
    path("issued_book/list/", IssuedBookListView.as_view(), name="issued_book_list"),
    path(
        "issued_book/create/", IssuedBookCreateView.as_view(), name="issued_book_create"
    ),
    path(
        "issued_book/detail/<int:pk>/",
        IssuedBookDetailView.as_view(),
        name="issued_book_detail",
    ),
    path(
        "issued_book/update/<int:pk>/",
        IssuedBookUpdateView.as_view(),
        name="issued_book_update",
    ),
    path(
        "issued_book/delete/<int:pk>/",
        IssuedBookDeleteView.as_view(),
        name="issued_book_delete",
    ),
]
