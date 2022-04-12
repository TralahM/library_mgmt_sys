from django.views.generic import DetailView

from books.models import Book


class BookDetailView(DetailView):
    model = Book
    template_name = "book/book_detail.html"
