from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from books.models import Book

class BookDeleteView(DeleteView):
    model = Book
    template_name = "book/book_delete.html"
    success_url = reverse_lazy('book_list')