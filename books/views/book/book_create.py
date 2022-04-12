from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from books.models import Book


class BookCreateView(CreateView):
    model = Book
    fields = "__all__"
    template_name = "book/book_create.html"
    success_url = reverse_lazy("book_list")
